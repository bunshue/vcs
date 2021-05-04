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
        PointF[] points = new PointF[9]; // PointF 陣列
        public Form1()
        {
            InitializeComponent();

            int Cx = this.ClientSize.Width / 2; // 視窗客戶區中心點
            int Cy = this.ClientSize.Height / 2;
            int k = 0;
            // 計算 PointF 陣列 的值
            for (int i = 0; i <= 360; i = i + 45)
            {
                points[k].X = (float)(Cx + 100 * Math.Cos(i * Math.PI / 180));
                points[k].Y = (float)(Cy + 100 * Math.Sin(i * Math.PI / 180));
                k++;
            }
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            // 依照 PointF 陣列 繪出直線
            e.Graphics.DrawLines(Pens.Black, points);
        }
    }
}