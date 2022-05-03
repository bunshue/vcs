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

namespace vcs_PicPick1
{
    enum MonitorState
    {
        ON = -1,
        OFF = 2,
        STANDBY = 1
    }

    public partial class Form1 : Form
    {
        private int SC_MONITORPOWER = 0xF170;
        private uint WM_SYSCOMMAND = 0x0112;

        [DllImport("user32.dll")]
        static extern IntPtr SendMessage(IntPtr hWnd, uint Msg, IntPtr wParam, IntPtr lParam);

        KeyHooker KeyHookHandler = new KeyHooker();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // 判斷是否已有程式在執行
            string proc = Process.GetCurrentProcess().ProcessName;
            Process[] processes = Process.GetProcessesByName(proc);

            richTextBox1.Text += "ProcessName : " + proc + "\tlen = " + processes.Length.ToString() + "\n";
            if (processes.Length > 1)
            {
                MessageBox.Show("PrintScreen " + proc + " 已經在執行", "重複執行錯誤", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                Close();
            }

            KeyHookHandler.Hook();
            timer1.Enabled = true;
            this.WindowState = FormWindowState.Minimized;

        }

        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            KeyHookHandler.UnHook();
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            if (this.WindowState == FormWindowState.Minimized)
            {
                this.ShowInTaskbar = false;
                notifyIcon1.Visible = true;
                notifyIcon1.BalloonTipText = "Print Screen";
                notifyIcon1.ShowBalloonTip(300);
                this.Hide();
            }

        }

        private void notifyIcon1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            this.WindowState = FormWindowState.Normal;
            this.ShowInTaskbar = true;
            notifyIcon1.Visible = false;
            this.Show();
            //this.BringToFront();

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

                //if (chkBalloonTips.Checked && this.WindowState == FormWindowState.Minimized)
                {
                    notifyIcon1.BalloonTipText = filename;
                    notifyIcon1.ShowBalloonTip(200);
                }
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
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







    }
}
