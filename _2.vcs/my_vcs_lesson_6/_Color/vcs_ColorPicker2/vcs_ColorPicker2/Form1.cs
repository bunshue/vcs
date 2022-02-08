using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;

//C#動態獲取鼠標位置的顏色

namespace vcs_ColorPicker2
{
    public partial class Form1 : Form
    {
        /// <summary>
        /// 獲取指定窗口的設備場景
        /// </summary>
        /// <param name="hwnd">將獲取其設備場景的窗口的句柄。若為0，則要獲取整個屏幕的DC</param>
        /// <returns>指定窗口的設備場景句柄，出錯則為0</returns>
        [DllImport("user32.dll")]
        public static extern IntPtr GetDC(IntPtr hwnd);

        /// <summary>
        /// 釋放由調用GetDC函數獲取的指定設備場景
        /// </summary>
        /// <param name="hwnd">要釋放的設備場景相關的窗口句柄</param>
        /// <param name="hdc">要釋放的設備場景句柄</param>
        /// <returns>執行成功為1，否則為0</returns>
        [DllImport("user32.dll")]
        public static extern Int32 ReleaseDC(IntPtr hwnd, IntPtr hdc);

        /// <summary>
        /// 在指定的設備場景中取得一個像素的RGB值
        /// </summary>
        /// <param name="hdc">一個設備場景的句柄</param>
        /// <param name="nXPos">邏輯坐標中要檢查的橫坐標</param>
        /// <param name="nYPos">邏輯坐標中要檢查的縱坐標</param>
        /// <returns>指定點的顏色</returns>
        [DllImport("gdi32.dll")]
        public static extern uint GetPixel(IntPtr hdc, int nXPos, int nYPos);

        public Color GetColor(int x, int y)
        {
            IntPtr hdc = GetDC(IntPtr.Zero);
            uint pixel = GetPixel(hdc, x, y);
            ReleaseDC(IntPtr.Zero, hdc);
            Color color = Color.FromArgb((int)(pixel & 0x000000FF), (int)(pixel & 0x0000FF00) >> 8, (int)(pixel & 0x00FF0000) >> 16);
            return color;
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            Point pt = new Point(Control.MousePosition.X, Control.MousePosition.Y);
            Color cl = GetColor(pt.X, pt.Y);
            label1.Text = cl.R.ToString() + ", " + cl.G.ToString() + ", " + cl.B.ToString();
        }
    }
}
