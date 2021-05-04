using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D; // for Matrix, MatrixOrder

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        Bitmap bm = Properties.Resources.Butterfly;
        float theta = 0; // 旋轉角度
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            int Cx = this.ClientSize.Width / 2; // 視窗客戶區正中心點
            int Cy = this.ClientSize.Height / 2;//

            e.Graphics.ResetTransform(); // 畫布的矩陣 = 單位矩陣

            Matrix A = new Matrix(); // 轉換矩陣
            A.Translate(-bm.Width / 2, -bm.Height / 2, MatrixOrder.Append);  // 先將圖形的中心點平移到原點
            A.Rotate(theta, MatrixOrder.Append);  // 乘上 旋轉矩陣
            A.Translate(Cx, Cy, MatrixOrder.Append); // 再搬到視窗客戶區正中心點

            e.Graphics.Transform = A;
            e.Graphics.DrawImage(bm, 0, 0); // 繪出圖形
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            theta = theta + 2;  // 旋轉角度 遞增
            this.Invalidate();
        }
    }
}