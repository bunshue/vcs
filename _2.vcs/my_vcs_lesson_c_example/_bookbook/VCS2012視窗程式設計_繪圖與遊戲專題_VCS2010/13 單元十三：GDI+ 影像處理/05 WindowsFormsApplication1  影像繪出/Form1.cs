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

        public Form1()
        {
            InitializeComponent();
            img = Properties.Resources.Monet; // 影像從資源載入
            this.ClientSize = new Size(img.Width, img.Height);// 調整視窗客戶區寬高
        }

        // 表單重畫事件
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            if (comboBox1.SelectedIndex == 0)
            {
                Rectangle rectDest = new Rectangle(0, 0, img.Width, img.Height);
                Rectangle rectSrc = new Rectangle(0, 0, img.Width, img.Height);
                e.Graphics.DrawImage(img, rectDest, rectSrc, GraphicsUnit.Pixel); // 呈現原圖
            }
            else if (comboBox1.SelectedIndex == 1)
            {
                Rectangle rectDest = new Rectangle(0, 0, img.Width, img.Height);
                e.Graphics.DrawImage(img, rectDest); // 呈現原圖
            }
            else if (comboBox1.SelectedIndex == 2)
            {
                Rectangle rectDest = new Rectangle(0, 0, img.Width * 2, img.Height / 2);
                e.Graphics.DrawImage(img, rectDest); // 呈現原圖
            }
            else if (comboBox1.SelectedIndex == 3)
            {
                Point dest = new Point(0, 0); // 目的地左上角座標
                e.Graphics.DrawImage(img, dest); // 呈現原圖
            }
            else if (comboBox1.SelectedIndex == 4)
            {
                e.Graphics.DrawImage(img, 0, 0); // 呈現原圖
            }
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            this.Invalidate();
        }
    }
}
