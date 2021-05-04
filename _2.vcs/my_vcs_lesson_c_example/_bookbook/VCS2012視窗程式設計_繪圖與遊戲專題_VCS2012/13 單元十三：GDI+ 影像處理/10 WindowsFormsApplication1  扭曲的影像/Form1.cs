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
        Point MousePos = new Point(); //滑鼠位置

        public Form1()
        {
            InitializeComponent();
            img = Properties.Resources.Monet; // 影像從資源載入
            this.ClientSize = new Size(img.Width, img.Height);// 調整視窗客戶區寬高
        }

        // 表單重畫事件
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            int Cx = this.ClientSize.Width / 2; // 視窗客戶區 正中心
            int Cy = this.ClientSize.Height / 2;

            Point[] pt = new Point[3];  // 三個點座標 定義一個平形四邊形
            pt[0] = new Point(MousePos.X - img.Width / 2, MousePos.Y); // 左上
            pt[1] = new Point(MousePos.X + img.Width / 2, MousePos.Y); // 右上
            pt[2] = new Point(Cx - img.Width / 2, Cy + img.Height / 2); // 左下

            e.Graphics.DrawImage(img, pt); // 呈現原圖
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                MousePos = e.Location; // 記錄滑鼠位置
                this.Invalidate(); // 要求表單重畫
            }
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }


    }
}