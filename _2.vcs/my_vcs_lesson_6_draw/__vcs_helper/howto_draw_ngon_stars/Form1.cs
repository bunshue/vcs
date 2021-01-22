using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace howto_draw_ngon_stars
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private int NumPoints = 0;

        private void btnGo_Click(object sender, EventArgs e)
        {
            int num_points;
            if (!int.TryParse(txtNumPoints.Text, out num_points))
            {
                MessageBox.Show("The number of points must be an integer.");
            }
            else if (num_points< 3)
            {
                MessageBox.Show("The number of points must be at least 3.");
            }
            else
            {
                NumPoints = num_points;
                picCanvas.Refresh();
            }
        }

        // Draw the stars.
        private void picCanvas_Paint(object sender, PaintEventArgs e)
        {
            if (NumPoints < 3) return;
            e.Graphics.Clear(picCanvas.BackColor);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Get the radii.
            int r1, r2, r3;
            r3 = Math.Min(picCanvas.ClientSize.Width, picCanvas.ClientSize.Height) / 2;
            r1 = r3 / 2;
            r2 = r3 / 4;
            r3 = r1 + r2;

            // Position variables.
            int cx = picCanvas.ClientSize.Width / 2;
            int cy = picCanvas.ClientSize.Height / 2;

            // Position the original points.
            PointF[] pts1 = new PointF[NumPoints];
            PointF[] pts2 = new PointF[NumPoints];
            double theta = -Math.PI / 2;
            double dtheta = 2 * Math.PI / NumPoints;
            for (int i = 0; i < NumPoints; i++)
            {
                pts1[i].X = (float)(r1 * Math.Cos(theta));
                pts1[i].Y = (float)(r1 * Math.Sin(theta));
                pts2[i].X = (float)(r2 * Math.Cos(theta));
                pts2[i].Y = (float)(r2 * Math.Sin(theta));
                theta += dtheta;
            }

            // Draw stars.
            int max = NumPoints - 1;
            if (chkHalfOnly.Checked) max = (int)(NumPoints / 2);
            for (int skip = 1; skip <= max; skip++)
            {
                // See if they are relatively prime.
                bool draw_all = !chkRelPrimeOnly.Checked;
                if (draw_all || GCD(skip, NumPoints) == 1)
                {
                    // Draw the big version of the star.
                    DrawStar(e.Graphics, cx, cy, pts1, skip);

                    // Draw the smaller version.
                    theta = -Math.PI / 2 + skip * 2 * Math.PI / NumPoints;
                    int x = (int)(cx + r3 * Math.Cos(theta));
                    int y = (int)(cy + r3 * Math.Sin(theta));

                    DrawStar(e.Graphics, x, y, pts2, skip);
                }
            }
        }

        // Return the greatest common divisor (GCD) of a and b.
        private long GCD(long a, long b)
        {
            long remainder;

            // Pull out remainders.
            for (;;)
            {
                remainder = a % b;
                if (remainder == 0) break;
                a = b;
                b = remainder;
            }

            return b;
        }

        // Draw a star centered at (x, y) using this skip value.
        private void DrawStar(Graphics gr, int x, int y, PointF[] orig_pts, int skip)
        {
            // Make a PointF array with the points in the proper order.
            PointF[] pts = new PointF[NumPoints];
            for (int i = 0; i < NumPoints; i++)
            {
                pts[i] = orig_pts[(i * skip) % NumPoints];
            }

            // Draw the star.
            gr.TranslateTransform(x, y);
            gr.DrawPolygon(Pens.Blue, pts);
            gr.ResetTransform();
        }

        // Redraw.
        private void picCanvas_Resize(object sender, EventArgs e)
        {
            picCanvas.Refresh();
        }
    }
}
