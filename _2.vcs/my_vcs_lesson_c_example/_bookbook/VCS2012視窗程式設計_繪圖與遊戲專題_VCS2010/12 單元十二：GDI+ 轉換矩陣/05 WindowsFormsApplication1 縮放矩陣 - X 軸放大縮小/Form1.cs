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
        float xScale = 1; // X 軸縮放倍數
        public Form1()
        {
            InitializeComponent();
        }

        // 表單重畫事件
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            int Cx = this.ClientSize.Width / 2; // 視窗客戶區正中心點
            int Cy = this.ClientSize.Height / 2;//
            int D = 100; // 球本身的半徑

            e.Graphics.ResetTransform(); // 畫布的矩陣 = 單位矩陣
            e.Graphics.DrawEllipse(Pens.Silver, Cx - D, Cy - D, 2 * D, 2 * D); //畫出開始的圓

            Matrix A = new Matrix(); // 轉換矩陣
            A.Scale(xScale, 1, MatrixOrder.Append);  // 乘上 縮放矩陣
            A.Translate(Cx, Cy, MatrixOrder.Append); // 再搬到視窗客戶區正中心點

            e.Graphics.Transform = A;  // 畫布的矩陣 = 矩陣 A
            e.Graphics.DrawEllipse(Pens.Red, 0 - D, 0 - D, 2 * D, 2 * D); //畫出縮放後的圓 
        }

        private void button1_Click(object sender, EventArgs e)
        {
            xScale = xScale - 0.1f;
            if (xScale <= 0.1f) xScale = 0.1f;
            this.Invalidate();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            xScale = xScale + 0.1f;
            this.Invalidate();
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }
    }
}
