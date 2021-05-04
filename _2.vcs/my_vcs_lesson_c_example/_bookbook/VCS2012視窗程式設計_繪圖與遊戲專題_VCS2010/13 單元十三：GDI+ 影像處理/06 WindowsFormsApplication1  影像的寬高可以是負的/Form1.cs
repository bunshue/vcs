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
            img = Properties.Resources.Amarillo200; // 影像從資源載入
            this.ClientSize = new Size(img.Width * 2, img.Height * 2);// 調整視窗客戶區寬高
        }

        // 表單重畫事件
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            int Cx = this.ClientSize.Width / 2; // 視窗客戶區 正中心
            int Cy = this.ClientSize.Height / 2;

            e.Graphics.DrawImage(img, Cx, Cy, img.Width, img.Height);
            e.Graphics.DrawImage(img, Cx, Cy, -img.Width, img.Height);
            e.Graphics.DrawImage(img, Cx, Cy, img.Width, -img.Height);
            e.Graphics.DrawImage(img, Cx, Cy, -img.Width, -img.Height);
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }


    }
}
