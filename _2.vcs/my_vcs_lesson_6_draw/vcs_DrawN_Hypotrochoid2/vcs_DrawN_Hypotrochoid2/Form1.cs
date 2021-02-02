using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace vcs_DrawN_Hypotrochoid2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The angle from one circle's center to the other.
        private float theta = 0;
        private float dtheta;

        // Drawing parameters.
        private int A, B, C, wid, hgt, cx, cy;
        private double max_t;
        private List<PointF> points;

        // Draw the hypotrochoid.
        private void btnDraw_Click(object sender, EventArgs e)
        {
            A = int.Parse(txtA.Text);
            B = int.Parse(txtB.Text);
            C = int.Parse(txtC.Text);
            max_t = 2 * Math.PI * B / GCD(A, B);

            wid = picCanvas.ClientSize.Width;
            hgt = picCanvas.ClientSize.Height;
            cx = wid / 2;
            cy = hgt / 2;

            points = new List<PointF>();
            points.Add(new PointF(cx + A - B + C, cy));
            theta = 0;
            dtheta = (float)(Math.PI * 2 / int.Parse(txtFrPerRev.Text));

            tmrDraw.Enabled = true;
        }

        // Redraw the curve.
        private void tmrDraw_Tick(object sender, EventArgs e)
        {
            theta += dtheta;
            DrawCurve();
        }

        // Draw the curve.
        private void DrawCurve()
        {
            Bitmap bm = new Bitmap(wid, hgt);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.SmoothingMode = SmoothingMode.AntiAlias;

                // Draw the outer circle.
                gr.DrawEllipse(Pens.Blue, cx - A, cy - A, 2 * A, 2 * A);

                // Draw the inner circle.
                int r = A - B;
                float cx1 = (float)(cx + r * Math.Cos(theta));
                float cy1 = (float)(cy + r * Math.Sin(theta));
                gr.DrawEllipse(Pens.Blue, cx1 - B, cy1 - B, 2 * B, 2 * B);

                // Add the next point.
                PointF new_point = new PointF(
                    (float)(cx + X(theta, A, B, C)),
                    (float)(cy + Y(theta, A, B, C)));
                points.Add(new_point);

                // Draw the line.
                gr.DrawLine(Pens.Blue, new PointF(cx1, cy1), new_point);

                // Draw the points.
                if (points.Count > 1) gr.DrawLines(Pens.Red, points.ToArray());
            }

            picCanvas.Image = bm;

            if (theta > max_t) tmrDraw.Enabled = false;
        }

        // The parametric function X(t).
        private double X(double t, double A, double B, double C)
        {
            return (A - B) * Math.Cos(t) + C * Math.Cos(t * (A - B) / B);
        }

        // The parametric function Y(t).
        private double Y(double t, double A, double B, double C)
        {
            return (A - B) * Math.Sin(t) - C * Math.Sin(t * (A - B) / B);
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
