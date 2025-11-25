using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;

//快捷鍵部分已搬出

namespace vcs_PictureMagnify2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // 定義快捷鍵 ST
        //如果函數執行成功，返回值不為0。       
        //如果函數執行失敗，返回值為0。要得到擴展錯誤信息，調用GetLastError。        
        [DllImport("user32.dll", SetLastError = true)]
        public static extern bool RegisterHotKey(
        IntPtr hWnd,                //要定義熱鍵的窗口的句柄            
        int id,                     //定義熱鍵ID（不能與其它ID重復）                       
        KeyModifiers fsModifiers,   //標識熱鍵是否在按Alt、Ctrl、Shift、Windows等鍵時才會生效         
        Keys vk                     //定義熱鍵的內容            
    );
        [DllImport("user32.dll", SetLastError = true)]
        public static extern bool UnregisterHotKey(
            IntPtr hWnd,                //要取消熱鍵的窗口的句柄            
            int id                      //要取消熱鍵的ID            
        );
        //定義了輔助鍵的名稱（將數字轉變為字符以便于記憶，也可去除此枚舉而直接使用數值）        
        [Flags()]
        public enum KeyModifiers
        {
            None = 0,
            Alt = 1,
            Ctrl = 2,
            Shift = 4,
            WindowsKey = 8
        }
        // 定義快捷鍵 SP

        // 獲取鼠標像素的RGB ST
        [DllImport("gdi32.dll")]
        static public extern uint GetPixel(IntPtr hDC, int XPos, int YPos);
        [DllImport("gdi32.dll")]
        static public extern IntPtr CreateDC(string driverName, string deviceName, string output, IntPtr lpinitData);
        [DllImport("gdi32.dll")]
        static public extern bool DeleteDC(IntPtr DC);
        static public byte GetRValue(uint color)
        {
            return (byte)color;
        }
        static public byte GetGValue(uint color)
        {
            return ((byte)(((short)(color)) >> 8));
        }
        static public byte GetBValue(uint color)
        {
            return ((byte)((color) >> 16));
        }
        static public byte GetAValue(uint color)
        {
            return ((byte)((color) >> 24));
        }
        public Color GetColor(Point screenPoint)
        {
            IntPtr displayDC = CreateDC("DISPLAY", null, null, IntPtr.Zero);
            uint colorref = GetPixel(displayDC, screenPoint.X, screenPoint.Y);
            DeleteDC(displayDC);
            byte Red = GetRValue(colorref);
            byte Green = GetGValue(colorref);
            byte Blue = GetBValue(colorref);
            return Color.FromArgb(Red, Green, Blue);
        }
        // 獲取鼠標像素的RGB SP

        int screenWidth;        //屏幕寬度
        int screenHeight;       //屏幕高度
        int mx;                 //鼠標x坐標
        int my;                 //鼠標y坐標
        const int imgWidth = 234;//放大后圖片的寬度
        const int imgHeight = 134;//放大后圖片的高度

        private void Form1_Load(object sender, EventArgs e)
        {
            this.Location = new Point(0, 0);
            screenWidth = Screen.PrimaryScreen.WorkingArea.Width;
            screenHeight = Screen.PrimaryScreen.WorkingArea.Height;
            this.TopMost = true;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            RegisterHotKey(Handle, 81, KeyModifiers.None, Keys.Escape);//已搬出
            mx = Control.MousePosition.X;
            my = Control.MousePosition.Y;
            lblmPos.Text = "(" + mx.ToString() + "," + my.ToString() + ")";
            Point pt = new Point(mx, my);
            Color cl = GetColor(pt);
            lblRGB.Text = "(" + cl.R.ToString() + "," + cl.G.ToString() + "," + cl.B + ")";
            if (mx <= this.Width && my <= this.Height)
            {
                this.Location = new Point(screenWidth - this.Width, 0);
            }
            if (mx >= screenWidth - this.Width && my <= this.Height)
            {
                this.Location = new Point(0, 0);
            }
            Bitmap bt = new Bitmap(imgWidth / 2, imgHeight / 2);
            Graphics g = Graphics.FromImage(bt);
            g.CopyFromScreen(new Point(Cursor.Position.X - imgWidth / 4, Cursor.Position.Y - imgHeight / 4), new Point(0, 0), new Size(imgWidth / 2, imgHeight / 2));
            IntPtr dc1 = g.GetHdc();
            g.ReleaseHdc(dc1);
            pictureBox1.Image = (Image)bt;
        }

        //已搬出
        protected override void WndProc(ref Message m)
        {
            const int WM_HOTKEY = 0x0312;
            //按快捷鍵     
            switch (m.Msg)
            {
                case WM_HOTKEY:
                    switch (m.WParam.ToInt32())
                    {
                        case 81:    //按下的是ESC     
                            Application.Exit();
                            break;
                    }
                    break;
            }
            base.WndProc(ref m);
        }

        //已搬出
        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            //注銷Id號為81的熱鍵設定
            UnregisterHotKey(Handle, 81);
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            Graphics g = e.Graphics;
            g.DrawLine(new Pen(Color.Red), new PointF(pictureBox1.Width / 2, 0), new PointF(pictureBox1.Width / 2, pictureBox1.Height));
            g.DrawLine(new Pen(Color.Red, 2), new PointF(0, pictureBox1.Height / 2), new PointF(pictureBox1.Width, pictureBox1.Height / 2));
        }
    }
}
