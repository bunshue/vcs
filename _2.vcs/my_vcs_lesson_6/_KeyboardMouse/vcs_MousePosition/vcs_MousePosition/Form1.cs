using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;  //StructLayout

namespace vcs_MousePosition
{
    public partial class Form1 : Form
    {
        //結構體布局 本機位置
        [StructLayout(LayoutKind.Sequential)]
        struct NativeRECT
        {
            public int left;
            public int top;
            public int right;
            public int bottom;
        }

        //將枚舉作為位域處理
        [Flags]
        enum MouseEventFlag : uint //設置鼠標動作的鍵值
        {
            Move = 0x0001,               //發生移動
            LeftDown = 0x0002,           //鼠標按下左鍵
            LeftUp = 0x0004,             //鼠標松開左鍵
            RightDown = 0x0008,          //鼠標按下右鍵
            RightUp = 0x0010,            //鼠標松開右鍵
            MiddleDown = 0x0020,         //鼠標按下中鍵
            MiddleUp = 0x0040,           //鼠標松開中鍵
            XDown = 0x0080,
            XUp = 0x0100,
            Wheel = 0x0800,              //鼠標輪被移動
            VirtualDesk = 0x4000,        //虛擬桌面
            Absolute = 0x8000
        }

        //設置鼠標位置
        [DllImport("user32.dll")]
        static extern bool SetCursorPos(int X, int Y);

        //設置鼠標按鍵和動作
        [DllImport("user32.dll")]
        static extern void mouse_event(MouseEventFlag flags, int dx, int dy,
            uint data, UIntPtr extraInfo); //UIntPtr指針多句柄類型

        [DllImport("user32.dll")]
        static extern IntPtr FindWindow(string strClass, string strWindow);

        //該函數獲取一個窗口句柄,該窗口雷鳴和窗口名與給定字符串匹配 hwnParent=Null從桌面窗口查找
        [DllImport("user32.dll")]
        static extern IntPtr FindWindowEx(IntPtr hwndParent, IntPtr hwndChildAfter,
            string strClass, string strWindow);

        [DllImport("user32.dll")]
        static extern bool GetWindowRect(HandleRef hwnd, out NativeRECT rect);

        //定義變量
        const int diff = 30;

        //private Point pt_st;
        //private Point pt_sp;
        //private int count;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        int cnt = 0;
        private void button1_Click(object sender, EventArgs e)
        {
            SetCursorPos(1920 / 2, 1080 / 2);
            cnt = 0;
            timer1.Enabled = true;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            cnt++;
            if (cnt > 50)
            {
                timer1.Enabled = false;
            }
            Random r = new Random();
            int dx = r.Next(-diff, diff);
            int dy = r.Next(-diff, diff);
            //richTextBox1.Text += "(" + dx.ToString() + ", " + dy.ToString() + ") ";

            mouse_event(MouseEventFlag.Move, dx, dy, 0, UIntPtr.Zero);

            //mouse_event(MouseEventFlag.LeftDown, dx, dy, 0, UIntPtr.Zero);
            //mouse_event(MouseEventFlag.LeftUp, dx, dy, 0, UIntPtr.Zero);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            int cx = 1920 / 2;
            int cy = 1080 / 2;
            int dx = 0;
            int dy = 0;
            richTextBox1.Text += "正中心 + dx = " + dx.ToString() + ", dy = " + dy.ToString() + "\n";
            SetCursorPos(cx + dx, cy + dy);
            delay(200);

            dx = 100;
            dy = 0;
            richTextBox1.Text += "正中心 + dx = " + dx.ToString() + ", dy = " + dy.ToString() + "\n";
            SetCursorPos(cx + dx, cy + dy);
            delay(200);

            dx = 100;
            dy = 100;
            richTextBox1.Text += "正中心 + dx = " + dx.ToString() + ", dy = " + dy.ToString() + "\n";
            SetCursorPos(cx + dx, cy + dy);
            delay(200);

            dx = 0;
            dy = 100;
            richTextBox1.Text += "正中心 + dx = " + dx.ToString() + ", dy = " + dy.ToString() + "\n";
            SetCursorPos(cx + dx, cy + dy);
            delay(200);

            dx = -100;
            dy = 100;
            richTextBox1.Text += "正中心 + dx = " + dx.ToString() + ", dy = " + dy.ToString() + "\n";
            SetCursorPos(cx + dx, cy + dy);
            delay(200);

            dx = -100;
            dy = 0;
            richTextBox1.Text += "正中心 + dx = " + dx.ToString() + ", dy = " + dy.ToString() + "\n";
            SetCursorPos(cx + dx, cy + dy);
            delay(200);

            dx = -100;
            dy = -100;
            richTextBox1.Text += "正中心 + dx = " + dx.ToString() + ", dy = " + dy.ToString() + "\n";
            SetCursorPos(cx + dx, cy + dy);
            delay(200);

            dx = 0;
            dy = -100;
            richTextBox1.Text += "正中心 + dx = " + dx.ToString() + ", dy = " + dy.ToString() + "\n";
            SetCursorPos(cx + dx, cy + dy);
            delay(200);

            dx = 100;
            dy = -100;
            richTextBox1.Text += "正中心 + dx = " + dx.ToString() + ", dy = " + dy.ToString() + "\n";
            SetCursorPos(cx + dx, cy + dy);
            delay(200);

            dx = 100;
            dy = 0;
            richTextBox1.Text += "正中心 + dx = " + dx.ToString() + ", dy = " + dy.ToString() + "\n";
            SetCursorPos(cx + dx, cy + dy);
            delay(200);

            dx = 00;
            dy = 0;
            richTextBox1.Text += "正中心 + dx = " + dx.ToString() + ", dy = " + dy.ToString() + "\n";
            SetCursorPos(cx + dx, cy + dy);
            delay(200);
        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void timer_mouse_position_Tick(object sender, EventArgs e)
        {
            this.Text = "相較於視窗原點的鼠標位置 : " + String.Format("{0},{1}", MousePosition.X, MousePosition.Y);
        }

        //delay 10000 約 10秒
        //C# 不lag的延遲時間
        private void delay(int delay_milliseconds)
        {
            delay_milliseconds *= 2;
            DateTime time_before = DateTime.Now;
            while (((TimeSpan)(DateTime.Now - time_before)).TotalMilliseconds < delay_milliseconds)
            {
                Application.DoEvents();
            }
        }
    }
}

