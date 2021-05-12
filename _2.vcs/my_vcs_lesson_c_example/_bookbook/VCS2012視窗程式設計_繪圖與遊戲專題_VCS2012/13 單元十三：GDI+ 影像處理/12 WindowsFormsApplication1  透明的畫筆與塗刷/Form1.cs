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
        Pen myPen =
          new Pen(Color.FromArgb(64, 0, 255, 0), 40); // 透明的畫筆
        SolidBrush myBrush =
          new SolidBrush(Color.FromArgb(64, 0, 0, 255)); // 透明的塗刷

        public Form1()
        {
            InitializeComponent();
            img = Properties.Resources.Monet; // 影像從資源載入
            //this.ClientSize = new Size(img.Width, img.Height);// 調整視窗客戶區寬高
        }

        // 表單重畫事件
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Rectangle rectDest = new Rectangle(0, 0, img.Width, img.Height);
            e.Graphics.DrawImage(img, rectDest); // 呈現原圖

            e.Graphics.DrawLine(myPen, 0, 100, img.Width, 100); // 畫出透明的直線

            int Cx = this.ClientSize.Width / 2; // 視窗客戶區 正中心
            int Cy = this.ClientSize.Height / 2;
            e.Graphics.FillEllipse(myBrush, Cx - 100, Cy - 100, 200, 200); // 繪畫出透明的圓形
        }
    }
}