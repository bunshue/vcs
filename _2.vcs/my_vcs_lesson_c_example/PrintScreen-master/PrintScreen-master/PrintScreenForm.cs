using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;                //for Directory
using System.Drawing.Imaging;   //for ImageFormat
using System.Diagnostics;
using System.Runtime.InteropServices;
using System.Threading;
using System.Media;

using KeyHook;

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
        private String config_filename = "PrintScreen.cfg";

        [DllImport("user32.dll")]
        static extern IntPtr SendMessage(IntPtr hWnd, uint Msg, IntPtr wParam, IntPtr lParam);

        KeyHooker KeyHookHandler = new KeyHooker();
        static String RootPath;
        static String FilePath;

        public PrintScreenForm()
        {
            InitializeComponent();
        }

        private void PrintScreenForm_Load(object sender, EventArgs e)
        {
            richTextBox1.Text += "PrintScreenForm_Load\n";

            // 判斷是否已有程式在執行
            string proc = Process.GetCurrentProcess().ProcessName;
            Process[] processes = Process.GetProcessesByName(proc);

            richTextBox1.Text += "ProcessName : " + proc + "\tlen = " + processes.Length.ToString() + "\n";
            if (processes.Length > 1)
            {
                MessageBox.Show("PrintScreen " + proc + " 已經在執行", "重複執行錯誤", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                Close();
            }

            LoadConfig();

            //檢查存圖的資料夾
            string Path = @"C:\dddddddddd";
            if (Directory.Exists(Path) == false)     //確認資料夾是否存在
            {
                Directory.CreateDirectory(Path);
                richTextBox1.Text += "已建立一個新資料夾: " + Path + "\n";
            }
            else
            {
                //richTextBox1.Text += "資料夾: " + Path + " 已存在，不用再建立\n";
            }
            RootPath = Path;

            KeyHookHandler.Hook();
            timerKeyboard.Enabled = true;
        }

        private void PrintScreenForm_FormClosed(object sender, FormClosedEventArgs e)
        {
            KeyHookHandler.UnHook();
        }

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
        }

        private void notifyIcon_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            this.WindowState = FormWindowState.Normal;
            this.ShowInTaskbar = true;
            notifyIcon.Visible = false;
            this.Show();
            //this.BringToFront();
        }

        void LoadConfig()
        {
            richTextBox1.Text += "LoadConfig, config_filename : " + config_filename + "\n";

            if (!File.Exists(config_filename))
            {
                //設定檔不存在
                RootPath = @"C:\dddddddddd";
                SaveConfig();
                richTextBox1.Text += "LoadConfig 111 RootPath = " + RootPath + "\n";
            }
            else
            {
                StreamReader sr = new StreamReader(config_filename);

                String Line;
                while ((Line = sr.ReadLine()) != null)
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
                        chkBalloonTips.Checked = Convert.ToBoolean(Line.Substring("BalloonTips=".Length));
                    }
                    else if (Line.Contains("Sound="))
                    {
                        chkSound.Checked = Convert.ToBoolean(Line.Substring("Sound=".Length));
                    }
                }
                sr.Close();

                richTextBox1.Text += "LoadConfig 222 config_filename = " + config_filename + "\n";
            }
        }

        void SaveConfig()
        {
            StreamWriter sw = new StreamWriter(config_filename);

            sw.WriteLine("RootPath=" + RootPath);
            sw.WriteLine("BalloonTips=" + chkBalloonTips.Checked);
            sw.WriteLine("Sound=" + chkSound.Checked);

            sw.Close();

            richTextBox1.Text += "SaveConfig\nFilename = " + config_filename + "\n";
            richTextBox1.Text += "RootPath = " + RootPath + "\n";
            richTextBox1.Text += "BalloonTips = " + chkBalloonTips.Checked + "\n";
            richTextBox1.Text += "Sound = " + chkSound.Checked + "\n";
        }

        private void SetMonitorState(MonitorState state)
        {
            SendMessage(this.FindForm().Handle, WM_SYSCOMMAND, (IntPtr)SC_MONITORPOWER, (IntPtr)state);
        }

        private void ScreenCapture()
        {
            int MonitorIndex = 0; //default monitor number

            // Turn on screen before capture to enable buffer refresh
            SetMonitorState(MonitorState.ON);
            Thread.Sleep(100); //wait monitor on

            int W = Screen.AllScreens[MonitorIndex].Bounds.Width;
            int H = Screen.AllScreens[MonitorIndex].Bounds.Height;
            int x_st = Screen.AllScreens[MonitorIndex].Bounds.X;
            int y_st = Screen.AllScreens[MonitorIndex].Bounds.Y;

            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + ", x = " + x_st.ToString() + ", y = " + y_st.ToString() + "\n";

            using (Bitmap bitmap1 = new Bitmap(W, H))
            {
                using (Graphics g = Graphics.FromImage(bitmap1))
                {
                    g.CopyFromScreen(x_st, y_st, 0, 0, bitmap1.Size, CopyPixelOperation.SourceCopy);
                }

                //存成bmp檔
                String filename = "C:\\dddddddddd\\full_image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
                bitmap1.Save(filename, ImageFormat.Bmp);
                richTextBox1.Text += "全螢幕截圖，存檔檔名：\n" + filename + "\n";

                if (chkSound.Checked == true)
                {
                    SoundPlayer simpleSound = new SoundPlayer(@"shutter.wav");
                    simpleSound.Play();
                }

                //if (chkBalloonTips.Checked && this.WindowState == FormWindowState.Minimized)
                {
                    notifyIcon.BalloonTipText = filename;
                    notifyIcon.ShowBalloonTip(200);
                }
            }
        }

        private void timerKeyboard_Tick(object sender, EventArgs e)
        {
            //richTextBox1.Text += "T ";
            if (KeyHooker.IsPrintScreenPressed == true) //有鍵盤輸入
            {
                ScreenCapture();
                KeyHooker.IsPrintScreenPressed = false;
            }
            if (KeyHooker.IsF12Pressed == true) //有鍵盤輸入
            {
                //ScreenCapture();
                richTextBox1.Text += "F12\n";
                KeyHooker.IsF12Pressed = false;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            SaveConfig();
        }
    }
}

