using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;

namespace vcs_ColorPicker5
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        [DllImport("user32.dll", EntryPoint = "GetCursorPos")]//獲取鼠標坐標
        public static extern int GetCursorPos(
            ref POINTAPI lpPoint
        );

        [StructLayout(LayoutKind.Sequential)]//定義與API相兼容結構體，實際上是一種內存轉換
        public struct POINTAPI
        {
            public int X;
            public int Y;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            POINTAPI point = new POINTAPI();//非托管內存坐標結構體
            int r = GetCursorPos(ref point);//獲取坐標
            using (Bitmap myBitmap = GetTopColor.GetDesktop())//將桌面保存到myBitmap中去，其實有點類似桌面截圖了，當然仍舊對DirectX沒有辦法
            {
                Color myColor = myBitmap.GetPixel(point.X, point.Y);//取指定坐標點的顏色
                label1.Text = point.X.ToString() + " : " + point.Y.ToString();
                label2.Text = myColor.ToString();
            }


        }

    }

    class GetTopColor
    {
        [DllImport("gdi32.dll", EntryPoint = "DeleteDC")]
        public static extern IntPtr DeleteDC(IntPtr hdc);

        [DllImport("gdi32.dll", EntryPoint = "DeleteObject")]
        public static extern IntPtr DeleteObject(IntPtr hObject);

        [DllImport("gdi32.dll", EntryPoint = "BitBlt")]
        public static extern bool BitBlt(IntPtr hdcDest, int nXDest,
        int nYDest, int nWidth, int nHeight, IntPtr hdcSrc,
        int nXSrc, int nYSrc, int dwRop);

        [DllImport("gdi32.dll", EntryPoint = "CreateCompatibleBitmap")]
        public static extern IntPtr CreateCompatibleBitmap(IntPtr hdc,
        int nWidth, int nHeight);

        [DllImport("gdi32.dll", EntryPoint = "CreateCompatibleDC")]
        public static extern IntPtr CreateCompatibleDC(IntPtr hdc);

        [DllImport("gdi32.dll", EntryPoint = "SelectObject")]
        public static extern IntPtr SelectObject(IntPtr hdc, IntPtr hgdiobjBmp);

        [DllImport("user32.dll", EntryPoint = "GetDesktopWindow")]
        public static extern IntPtr GetDesktopWindow();

        [DllImport("user32.dll", EntryPoint = "GetDC")]
        public static extern IntPtr GetDC(IntPtr hWnd);

        [DllImport("user32.dll", EntryPoint = "GetSystemMetrics")]
        public static extern int GetSystemMetrics(int nIndex);

        [DllImport("user32.dll", EntryPoint = "ReleaseDC")]
        public static extern IntPtr ReleaseDC(IntPtr hWnd, IntPtr hDC);

        public static Bitmap GetDesktop()
        {
            int screenX;
            int screenY;
            IntPtr hBmp;
            IntPtr hdcScreen = GetDC(GetDesktopWindow());
            IntPtr hdcCompatible = CreateCompatibleDC(hdcScreen);

            screenX = GetSystemMetrics(0);
            screenY = GetSystemMetrics(1);
            hBmp = CreateCompatibleBitmap(hdcScreen, screenX, screenY);

            if (hBmp != IntPtr.Zero)
            {
                IntPtr hOldBmp = (IntPtr)SelectObject(hdcCompatible, hBmp);
                BitBlt(hdcCompatible, 0, 0, screenX, screenY, hdcScreen, 0, 0, 13369376);

                SelectObject(hdcCompatible, hOldBmp);
                DeleteDC(hdcCompatible);
                ReleaseDC(GetDesktopWindow(), hdcScreen);

                Bitmap bmp = System.Drawing.Image.FromHbitmap(hBmp);

                DeleteObject(hBmp);
                GC.Collect();

                return bmp;
            }

            return null;
        }
    }
}
