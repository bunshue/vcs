// http://en.wikipedia.org/wiki/Maurer_rose
//  Maurer rose was introduced by Peter M. Maurer in his article entitled A Rose is a Rose

// (r, θ) = (a * sin(kθ), θ) where (θ = 0, d, 2d, 3d, ..., 360d)
// Converting between polar and Cartesian coordinates
// x = r cos(θ)
// y = r sin(θ)

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
        double x0, y0, x1, y1;
        float k = 2;  // 係數
        float d = 29; // 係數

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            // 畫布設定為較佳的輸出品質 
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
            int Cx = this.ClientSize.Width / 2;  // 中心點
            int Cy = this.ClientSize.Height / 2;
            int a = (int)(Math.Min(Cx, Cy) * 0.9); // 半徑
            double r; // 極座標的 r
            double theta; // 極座標的θ

            for (int t = 0; t <= 360; t = t + 1)  // 361個點  = 360 條直線
            {
                x0 = x1; // 求該點之前 先存成為上個點
                y0 = y1;
                theta = t * d * Math.PI / 180;
                r = a * Math.Sin(k * theta);  // 極座標
                x1 = r * Math.Cos(theta);  // 直角座標
                y1 = r * Math.Sin(theta);
                if (t != 0)  // 第一個點不畫
                    e.Graphics.DrawLine(Pens.Black, Cx + (float)x0, Cy - (float)y0,
                              Cx + (float)x1, Cy - (float)y1);
            }
        }

        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {
            k = (int)numericUpDown1.Value;
            this.Invalidate();
        }

        private void numericUpDown2_ValueChanged(object sender, EventArgs e)
        {
            d = (int)numericUpDown2.Value;
            this.Invalidate();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            k++;
            if (k > (int)numericUpDown1.Maximum) k = (int)numericUpDown1.Minimum;
            numericUpDown1.Value = (decimal)k;
            this.Invalidate();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            timer1.Enabled = !timer1.Enabled;
            if (timer1.Enabled)
                button1.Text = "停止";
            else
                button1.Text = "K 自動增加";
        }
    }
}
