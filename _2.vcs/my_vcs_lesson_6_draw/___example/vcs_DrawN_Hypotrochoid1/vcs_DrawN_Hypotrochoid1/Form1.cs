using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace vcs_DrawN_Hypotrochoid1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Draw the hypotrochoid.
        private void btnDraw_Click(object sender, EventArgs e)
        {
            int A = int.Parse(txtA.Text);
            int B = int.Parse(txtB.Text);
            int C = int.Parse(txtC.Text);
            int iter = int.Parse(txtIter.Text);

            int wid = picCanvas.ClientSize.Width;
            int hgt = picCanvas.ClientSize.Height;
            Bitmap bm = new Bitmap(wid, hgt);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.SmoothingMode = SmoothingMode.AntiAlias;

                int cx = wid / 2;
                int cy = hgt / 2;
                double t = 0;
                double dt = Math.PI / iter;
                double max_t = 2 * Math.PI * B / GCD(A, B);
                double x1 = cx + X(t, A, B, C);
                double y1 = cy + Y(t, A, B, C);
                List<PointF> points = new List<PointF>();
                points.Add(new PointF((float)x1, (float)y1));
                while (t <= max_t)
                {
                    t += dt;
                    x1 = cx + X(t, A, B, C);
                    y1 = cy + Y(t, A, B, C);
                    points.Add(new PointF((float)x1, (float)y1));
                }
                // Draw the polygon.
                gr.DrawPolygon(Pens.Red, points.ToArray());
            }

            picCanvas.Image = bm;
        }

        // The parametric function X(t).
        private double X(double t, double A, double B, double C)
        {
            return (A - B) * Math.Cos(t) + C * Math.Cos((A - B) / B * t);
        }

        // The parametric function Y(t).
        private double Y(double t, double A, double B, double C)
        {
            return (A - B) * Math.Sin(t) - C * Math.Sin((A - B) / B * t);
        }

        // Use Euclid's algorithm to calculate the
        // greatest common divisor (GCD) of two numbers.
        private long GCD(long a, long b)
        {
            // Make a >= b.
            a = Math.Abs(a);
            b = Math.Abs(b);
            if (a < b)
            {
                long tmp = a;
                a = b;
                b = tmp;
            }

            // Pull out remainders.
            for (;;)
            {
                long remainder = a % b;
                if (remainder == 0) return b;
                a = b;
                b = remainder;
            };
        }

        // Return the least common multiple
        // (LCM) of two numbers.
        private long LCM(long a, long b)
        {
            return a * b / GCD(a, b);
        }
    }
}
