using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using KeyHook;
using System.Diagnostics;
using System.Runtime.InteropServices;
using System.Threading;
using System.Media;
using System.IO;

namespace PrintScreen
{
    enum MonitorState
    {
        ON = -1,
        OFF = 2,
        STANDBY = 1
    }

    public partial class PrintScreenForm : Form
    {
        private int SC_MONITORPOWER = 0xF170;
        private uint WM_SYSCOMMAND = 0x0112;
        private String ConfigFileName = "PrintScreen.cfg";

        [DllImport("user32.dll")]
        static extern IntPtr SendMessage(IntPtr hWnd, uint Msg, IntPtr wParam, IntPtr lParam);

        KeyHooker KeyHookHandler = new KeyHooker();
        static String RootPath;
        static String FilePath;

        public PrintScreenForm()
        {
            InitializeComponent();
        }

        #region WIndow Form Events

        private void PrintScreenForm_Load(object sender, EventArgs e)
        {
            RootPath = @"C:\dddddddddd";

            tbFilePath.Text = @"C:\dddddddddd";
            // 判斷是否已有程式在執行
            string proc = Process.GetCurrentProcess().ProcessName;
            Process[] processes = Process.GetProcessesByName(proc);
            if (processes.Length > 1)
            {
                MessageBox.Show("PrintScreen " + proc + " 已經在執行", "重複執行錯誤", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                Close();
            }
            //LoadConfig();
            KeyHookHandler.Hook();
            timerKeyboard.Enabled = true;
        } //PrintScreenForm_Load()

        private void PrintScreenForm_FormClosed(object sender, FormClosedEventArgs e)
        {
            KeyHookHandler.UnHook();
        } //PrintScreenForm_FormClosed()

        private void PrintScreenForm_Resize(object sender, EventArgs e)
        {
            if (this.WindowState == FormWindowState.Minimized)
            {
                this.ShowInTaskbar = false;
                notifyIcon.Visible = true;
                notifyIcon.BalloonTipText = "Print Screen";
                notifyIcon.ShowBalloonTip(300);
                this.Hide();
            }
        } //PrintScreenForm_Resize()

        private void notifyIcon_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            this.WindowState = FormWindowState.Normal;
            this.ShowInTaskbar = true;
            notifyIcon.Visible = false;
            this.Show();
            //this.BringToFront();
        } //notifyIcon_MouseDoubleClick()

        #endregion

        #region Support Functions
        
        void LoadConfig()
        {
            if (!File.Exists(ConfigFileName))
            {
                // Config not exists
                RootPath = Environment.GetEnvironmentVariable("HOMEDRIVE")
                            + Environment.GetEnvironmentVariable("HOMEPATH")
                            + @"\ScreenCapture";
                SaveConfig();
            }
            else
            {
                StreamReader ConfigFileStream = new StreamReader(ConfigFileName);

                String Line;
                while ((Line = ConfigFileStream.ReadLine()) != null)
                {
                    if (Line[0] == '#')
                    {
                        //skip comment line
                    }
                    else if (Line.Contains("RootPath="))
                    {
                        RootPath = Line.Substring("RootPath=".Length);
                    }
                    else if (Line.Contains("BalloonTips="))
                    {
                        chkBalloonTips.Checked = Convert.ToBoolean( Line.Substring("BalloonTips=".Length));
                    }
                    else if (Line.Contains("Sound="))
                    {
                        chkSound.Checked = Convert.ToBoolean(Line.Substring("Sound=".Length));
                    }
                }
                ConfigFileStream.Close();
            }
            tbFilePath.Text = RootPath;
        } // LoadConfig()

        void SaveConfig()
        {
            StreamWriter ConfigFileStream = new StreamWriter(ConfigFileName);

            ConfigFileStream.WriteLine("RootPath=" + RootPath);
            ConfigFileStream.WriteLine("BalloonTips=" + chkBalloonTips.Checked);
            ConfigFileStream.WriteLine("Sound=" + chkSound.Checked);

            ConfigFileStream.Close();
        } //SaveConfig()

        private void SetMonitorState(MonitorState state)
        {
            SendMessage(this.FindForm().Handle, WM_SYSCOMMAND, (IntPtr)SC_MONITORPOWER, (IntPtr)state);
        } //SetMonitorState(

        private void BuildPath()
        {
            FilePath = RootPath + "\\" + DateTime.Now.ToString("yyyy-MM-dd");
            //FilePath = @"C:\dddddddddd" + "\\" + DateTime.Now.ToString("yyyy-MM-dd");

            richTextBox1.Text += "RootPath = " + RootPath + "\n";
            richTextBox1.Text += "FilePath = " + FilePath + "\n";

            if (!System.IO.Directory.Exists(RootPath))
            {
                System.IO.Directory.CreateDirectory(RootPath);
            }

            if (!System.IO.Directory.Exists(FilePath))
            {
                System.IO.Directory.CreateDirectory(FilePath);
            }
        } //BuildPath()

        private void ScreenCapture()
        {
            int MonitorIndex = 0; //default monitor number

            // Turn on screen before capture to enable buffer refresh
            SetMonitorState(MonitorState.ON);
            Thread.Sleep(100); //wait monitor on

            using (Bitmap bmpScreenCapture = new Bitmap(Screen.AllScreens[MonitorIndex].Bounds.Width,
                                            Screen.AllScreens[MonitorIndex].Bounds.Height))
            {
                using (Graphics g = Graphics.FromImage(bmpScreenCapture))
                {
                    g.CopyFromScreen(Screen.AllScreens[MonitorIndex].Bounds.X,
                                     Screen.AllScreens[MonitorIndex].Bounds.Y,
                                     0, 0,
                                     bmpScreenCapture.Size,
                                     CopyPixelOperation.SourceCopy);
                }
                BuildPath();
                String FileName = "PrintScreen" + DateTime.Now.ToString("yyyy-MM-dd_HH-mm-ss") + ".jpg";
                String BmpFileName = FilePath + "\\"+ FileName;

                richTextBox1.Text += "FileName = " + FileName + "\n";
                richTextBox1.Text += "BmpFileName = " + BmpFileName + "\n";

                bmpScreenCapture.Save(BmpFileName);

                if (chkSound.Checked)
                {
                    SoundPlayer simpleSound = new SoundPlayer(@"shutter.wav");
                    simpleSound.Play();
                }

                //if (chkBalloonTips.Checked && this.WindowState == FormWindowState.Minimized)
                {
                    notifyIcon.BalloonTipText = FileName;
                    notifyIcon.ShowBalloonTip(200);
                }
            }
        } //ScreenCapture()

        private void timerKeyboard_Tick(object sender, EventArgs e)
        {
            if (KeyHooker.IsPrintScreenPressed) //有鍵盤輸入
            {
                ScreenCapture();
                KeyHooker.IsPrintScreenPressed = false;
            }
        } //imerKeyboard_Tick()

        #endregion

        #region UI Events

        private void btnBrowse_Click(object sender, EventArgs e)
        {
            folderBrowserDialog.ShowDialog();
            RootPath = tbFilePath.Text = folderBrowserDialog.SelectedPath;
            SaveConfig();
        } //btnBrowse_Click()

        private void chkBalloonTips_Click(object sender, EventArgs e)
        {
            SaveConfig();
        } //chkBalloonTips_Click()

        private void chkSound_Click(object sender, EventArgs e)
        {
            SaveConfig();
        } //chkSound_Click()


        #endregion

    }
}
