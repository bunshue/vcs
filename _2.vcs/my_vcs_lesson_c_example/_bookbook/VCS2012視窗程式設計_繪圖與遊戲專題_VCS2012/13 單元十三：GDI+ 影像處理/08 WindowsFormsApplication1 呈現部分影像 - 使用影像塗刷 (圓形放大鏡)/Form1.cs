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
        Bitmap img; // Bitmap 影像
        Point mousePos; // 滑鼠位置
        int D = 100; // 放大鏡半徑

        Bitmap imgDouble; // 兩倍影像的點陣圖物件
        TextureBrush texBrush; // 兩倍影像的塗刷

        public Form1()
        {
            InitializeComponent();
            img = Properties.Resources.p135; // 影像從資源載入
            this.ClientSize = new Size(img.Width, img.Height);// 調整視窗客戶區寬高

            imgDouble = new Bitmap(img.Width * 2, img.Height * 2);　// 新增點陣圖物件
            Graphics G = Graphics.FromImage(imgDouble); // 由點陣圖物件產生畫布
            Rectangle rectDest = new Rectangle(0, 0, imgDouble.Width, imgDouble.Height);
            Rectangle rectSrc = new Rectangle(0, 0, img.Width, img.Height);
            G.DrawImage(img, rectDest, rectSrc, GraphicsUnit.Pixel); // 放大兩倍
            texBrush = new TextureBrush(imgDouble);  // 兩倍影像的塗刷
        }

        // 表單重畫事件
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            if (img != null)
            {
                e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
                e.Graphics.DrawImage(img, 0, 00, img.Width, img.Height); // 呈現原圖

                Rectangle rectDest = new Rectangle(mousePos.X - D, mousePos.Y - D, 2 * D, 2 * D);

                texBrush.ResetTransform();  // 塗刷的轉換矩陣 = 單位矩陣
                texBrush.TranslateTransform(-mousePos.X, -mousePos.Y); // 塗刷對齊 滑鼠位置
                e.Graphics.FillEllipse(texBrush, rectDest); // 使用影像塗刷 繪出圓形

                e.Graphics.DrawEllipse(Pens.Black, rectDest); // 放大鏡外框
            }
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            mousePos = e.Location; // 記錄 滑鼠位置
            this.Invalidate(); // 要求更新表單
        }
    }
}