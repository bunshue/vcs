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
        Bitmap bitmap1; // Bitmap 影像
        Point MousePos = new Point(); //滑鼠位置

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bitmap1 = Properties.Resources.Monet; // 影像從資源載入
            pictureBox1.ClientSize = new Size(bitmap1.Width + 100, bitmap1.Height + 100);
            pictureBox1.Location = new Point(50, 50);
            this.ClientSize = new Size(bitmap1.Width + 100 + 100, bitmap1.Height + 100 + 100);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                MousePos = e.Location; // 記錄滑鼠位置
                this.pictureBox1.Invalidate(); // 要求表單重畫
            }
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                MousePos = e.Location; // 記錄滑鼠位置
                this.pictureBox1.Invalidate(); // 要求表單重畫
            }
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            int Cx = this.pictureBox1.ClientSize.Width / 2; // 視窗客戶區 正中心
            int Cy = this.pictureBox1.ClientSize.Height / 2;

            Point[] pt = new Point[3];  // 三個點座標 定義一個平形四邊形
            pt[0] = new Point(MousePos.X - bitmap1.Width / 2, MousePos.Y); // 左上
            pt[1] = new Point(MousePos.X + bitmap1.Width / 2, MousePos.Y); // 右上
            pt[2] = new Point(Cx - bitmap1.Width / 2, Cy + bitmap1.Height / 2); // 左下

            e.Graphics.DrawImage(bitmap1, pt); // 呈現原圖
        }
    }
}
