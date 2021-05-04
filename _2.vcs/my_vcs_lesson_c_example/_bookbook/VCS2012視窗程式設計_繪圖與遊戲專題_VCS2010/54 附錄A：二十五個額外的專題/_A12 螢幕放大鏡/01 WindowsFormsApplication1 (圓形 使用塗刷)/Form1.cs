// 作者：鄞永傳老師‧xnabook@yahoo.com.tw‧2012-08 
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        Bitmap bitmap, bitmapDouble;  // 螢幕的圖 和 2倍的圖
        Size ScreenSize;  // 螢幕的 寬高
        TextureBrush texBrush; // 兩倍影像的塗刷
        Point mousePos; // 滑鼠位置
        int D = 100; // 放大鏡半徑

        public Form1()
        {
            InitializeComponent();
            Cursor.Hide(); // 隱藏滑鼠游標
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Rectangle rectDest = new Rectangle(0, 0, ScreenSize.Width, ScreenSize.Height);
            Rectangle rectSRC = new Rectangle(0, 0, ScreenSize.Width, ScreenSize.Height);
            e.Graphics.DrawImage(bitmap, rectDest, rectSRC, GraphicsUnit.Pixel);  // 繪出 螢幕的圖

            rectDest = new Rectangle(mousePos.X - D, mousePos.Y - D, 2 * D, 2 * D);
            texBrush.ResetTransform();  // 塗刷的轉換矩陣 = 單位矩陣
            texBrush.TranslateTransform(-mousePos.X, -mousePos.Y); // 塗刷對齊 滑鼠位置
            e.Graphics.FillEllipse(texBrush, rectDest); // 使用影像塗刷 繪出圓形
            e.Graphics.DrawEllipse(Pens.Black, rectDest); // 放大鏡外框
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            mousePos = e.Location; // 記錄 滑鼠位置
            this.Invalidate(); // 要求更新表單
        }

        private void Form1_Activated(object sender, EventArgs e)
        {
            Initial();
        }

        void Initial()
        {
            ScreenSize = SystemInformation.PrimaryMonitorSize; // 得到 螢幕的 寬高
            bitmap = new Bitmap(ScreenSize.Width, ScreenSize.Height);
            Graphics G = Graphics.FromImage(bitmap);
            G.CopyFromScreen(0, 0, 0, 0, ScreenSize); // 考貝 螢幕的圖 到 bitmap

            bitmapDouble = new Bitmap(ScreenSize.Width * 2, ScreenSize.Height * 2);
            Graphics G2 = Graphics.FromImage(bitmapDouble);
            Rectangle rectDest = new Rectangle(0, 0, ScreenSize.Width * 2, ScreenSize.Height * 2);
            Rectangle rectSRC = new Rectangle(0, 0, ScreenSize.Width, ScreenSize.Height);
            G2.DrawImage(bitmap, rectDest, rectSRC, GraphicsUnit.Pixel); // 考貝 2倍螢幕的圖 到 bitmapDouble

            texBrush = new TextureBrush(bitmapDouble);  // 兩倍影像的塗刷
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyData == Keys.Escape ) // 離開
            {
                Cursor.Show();
                Application.Exit();
            }
            else if (e.KeyData == Keys.F1 || e.KeyData == Keys.Space)  // 程式最小化
            {
                this.WindowState = FormWindowState.Minimized;
            }
            else if (e.KeyData == Keys.Up)  // 放大鏡半徑 變大
            {
                D = D + 10;
                if (D > 500) D = 500;
                this.Invalidate();
            }
            else if (e.KeyData == Keys.Down)  // 放大鏡半徑 變小
            {
                D = D - 10;
                if (D < 30) D = 30;
                this.Invalidate();
            }
        }
    }
}
