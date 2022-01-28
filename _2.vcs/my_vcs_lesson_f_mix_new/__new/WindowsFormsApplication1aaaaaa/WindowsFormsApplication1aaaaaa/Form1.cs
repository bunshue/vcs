using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

                                                        using System.Runtime.InteropServices;  //StructLayout

namespace WindowsFormsApplication1aaaaaa
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
        const int AnimationCount = 80;

        private Point pt_st;
        private Point pt_sp;
        private int count;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            NativeRECT rect;
            //獲取主窗體句柄
            IntPtr ptrTaskbar = FindWindow("WindowsForms10.Window.8.app.0.2bf8098_r11_ad1", null);

            //獲取窗體中"button1"按鈕
            IntPtr ptrStartBtn = FindWindowEx(ptrTaskbar, IntPtr.Zero, null, "button1");

            //獲取窗體大小
            GetWindowRect(new HandleRef(this, ptrStartBtn), out rect);
            pt_sp.X = (rect.left + rect.right) / 2;
            pt_sp.Y = (rect.top + rect.bottom) / 2;

            //判斷點擊按鈕
            if (checkBox1.Checked)
            {
                //選擇"查看鼠標運行的軌跡"
                this.count = AnimationCount;
                timer1.Start();
            }
            else
            {
                SetCursorPos(pt_sp.X, pt_sp.Y);
                mouse_event(MouseEventFlag.LeftDown, 0, 0, 0, UIntPtr.Zero);
                mouse_event(MouseEventFlag.LeftUp, 0, 0, 0, UIntPtr.Zero);
                textBox1.Text = String.Format("{0},{1}", MousePosition.X, MousePosition.Y);
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            /*
            int stepx = (pt_sp.X - MousePosition.X) / count;
            int stepy = (pt_sp.Y - MousePosition.Y) / count;
            count--;
            if (count == 0)
            {
                timer1.Stop();
                mouse_event(MouseEventFlag.LeftDown, 0, 0, 0, UIntPtr.Zero);
                mouse_event(MouseEventFlag.LeftUp, 0, 0, 0, UIntPtr.Zero);
            }
            */

            //mouse_event(MouseEventFlag.Move, stepx, stepy, 0, UIntPtr.Zero);

            label1.Text = "相較於視窗原點的鼠標位置 : " + String.Format("{0},{1}", MousePosition.X, MousePosition.Y);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            timer2.Enabled = true;
        }

        int x_st = 0;
        int y_st = 0;
        private void timer2_Tick(object sender, EventArgs e)
        {
            //mouse_event(MouseEventFlag.Move, x_st, y_st, 0, UIntPtr.Zero);
            SetCursorPos(x_st, y_st);
            x_st += 100;
            y_st += 100;


            if (y_st > 800)
            {
                timer2.Enabled = false;
                x_st = 0;
                y_st = 0;

            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void timer3_Tick(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

    }
}
