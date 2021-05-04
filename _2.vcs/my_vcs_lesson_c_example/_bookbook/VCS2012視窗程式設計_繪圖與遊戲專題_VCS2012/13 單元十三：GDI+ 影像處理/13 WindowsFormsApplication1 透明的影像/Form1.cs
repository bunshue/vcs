using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Imaging; //  for ColorMatrix, ImageAttributes

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        Bitmap img; // Bitmap 影像
        Bitmap img2;  // 透明的影像
        Point MousePos;

        public Form1()
        {
            InitializeComponent();
            img = Properties.Resources.Monet; // 影像從資源載入
            this.ClientSize = new Size(img.Width, img.Height);// 調整視窗客戶區寬高

            img2 = Properties.Resources.Amarillo200; // 影像從資源載入
        }

        // 表單重畫事件
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Rectangle rectDest = new Rectangle(0, 0, img.Width, img.Height);
            e.Graphics.DrawImage(img, rectDest); // 呈現原圖

            // 色彩調整矩陣
            float[][] cmArray =
               {
                  new float[] {1, 0, 0, 0,    0},
                  new float[] {0, 1, 0, 0,    0},
                  new float[] {0, 0, 1, 0,    0},
                  new float[] {0, 0, 0, 0.5f, 0},
                  new float[] {0, 0, 0, 0,    1}
               };

            ColorMatrix cm = new ColorMatrix(cmArray);
            ImageAttributes ia = new ImageAttributes();
            ia.SetColorMatrix(cm,
                ColorMatrixFlag.Default,
                ColorAdjustType.Bitmap);

            // 繪出透明的影像
            e.Graphics.DrawImage(img2,
                new Rectangle(MousePos.X - img2.Width / 2, MousePos.Y - img2.Height / 2, img2.Width, img2.Height),
                0, 0, img2.Width, img2.Height,
                GraphicsUnit.Pixel, ia);

        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            MousePos = e.Location;
            this.Invalidate();
        }
    }
}