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

        public Form1()
        {
            InitializeComponent();
            img = Properties.Resources.p135; // 影像從資源載入
            this.ClientSize = new Size(img.Width, img.Height);// 調整視窗客戶區寬高
        }

        // 表單重畫事件
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.DrawImage(img, 0, 0, img.Width, img.Height); // 呈現原圖

            Rectangle rectDest = new Rectangle(mousePos.X - D, mousePos.Y - D, 2 * D, 2 * D);
            Rectangle rectSRC = new Rectangle(mousePos.X - D / 2, mousePos.Y - D / 2, D, D);
            e.Graphics.DrawImage(img, rectDest, rectSRC, GraphicsUnit.Pixel); // 呈現原圖 放大區域

            e.Graphics.DrawRectangle(Pens.Black, rectDest); // 放大鏡外框
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            mousePos = e.Location; // 記錄 滑鼠位置
            this.Invalidate(); // 要求更新表單
        }
    }
}