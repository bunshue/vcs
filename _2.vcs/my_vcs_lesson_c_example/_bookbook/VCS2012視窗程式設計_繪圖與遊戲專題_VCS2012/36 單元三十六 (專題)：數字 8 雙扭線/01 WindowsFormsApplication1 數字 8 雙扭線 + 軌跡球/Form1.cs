// http://en.wikipedia.org/wiki/Lemniscate_of_Bernoulli

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
        G2D_LemniscateOfBernoulli lob;

        int t = 0; // 數字 8 曲線公式的參數值(角度 0 ~ 359)

        int Cx, Cy;  // 中心點
        int a; // 半徑

        public Form1()
        {
            InitializeComponent();
            this.pictureBox1.ClientSize = new Size(500, 200);
            Cx = this.pictureBox1.ClientSize.Width / 2;
            Cy = this.pictureBox1.ClientSize.Height / 2;
            a = (int)(Math.Min(Cx, Cy) * 2 * 0.8);

            lob = new G2D_LemniscateOfBernoulli(a);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
          t++;
          t = t % 360;
          this.pictureBox1.Invalidate();
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            lob.Draw(e.Graphics, Cx, Cy);

            PointF pt = lob.GetPos(t, Cx, Cy);
            e.Graphics.FillEllipse(Brushes.Red, pt.X - 10, pt.Y - 10, 20, 20);

        }
    }
}
