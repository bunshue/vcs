// http://en.wikipedia.org/wiki/Butterfly_curve_(transcendental)
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
        double x0, y0, x1, y1;  // 兩個點畫一直線

        int n = 1;   // 畫幾圈 蝴蝶曲線
        
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            // 反鋸齒設定 -- 畫布設定為較佳的輸出品質 
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            int Cx = this.ClientSize.Width / 2;  // 中心點
            int Cy = this.ClientSize.Height / 2;
            double d = Math.Min(this.ClientSize.Width, this.ClientSize.Height) / 8.0;  // 半徑

            double t;  // 極座標的θ
            double r;  // 極座標的 r
            for (int k = 0; k <= 360 * n; k++)
            {
                x0 = x1;  // 先儲存 成為上個點
                y0 = y1;

                // 計算該點 (極座標)
                t = k * Math.PI / 180;
                r = d * (Math.Pow(Math.E, Math.Cos(t)) - 2 * Math.Cos(4 * t) - Math.Pow(Math.Sin(t / 12), 5));

                // 轉成直角座標
                x1 = r * Math.Sin(t); 
                y1 = r * Math.Cos(t);

                if (t != 0)  // 第一個點不畫
                  e.Graphics.DrawLine(Pens.Black, Cx + (float)x0, Cy - (float)y0, Cx + (float)x1, Cy - (float)y1);
            }
        }

        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {
            n = (int)numericUpDown1.Value;
            this.Invalidate();
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }
    }
}
