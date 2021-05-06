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
        Bitmap img;  // Bitmap 影像
        public Form1()
        {
            InitializeComponent();
            img = Properties.Resources.Sun200x200; // 影像從資源載入 
            //img = new Bitmap(Properties.Resources.Wenci); // 影像從資源載入
        }

        // 90 度旋轉按鈕
        private void button2_Click(object sender, EventArgs e)
        {
            img.RotateFlip(RotateFlipType.Rotate90FlipNone); // 影像旋轉90度
            this.Invalidate(); // 要求重畫
        }

        // 表單重畫事件
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            if (img != null)
                e.Graphics.DrawImage(img, 10, 50, img.Width, img.Height);
        }
    }
}