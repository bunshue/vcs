using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace howto_phi_spiral2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Orientations for the rectangles.
        private enum RectOrientations
        {
            RemoveLeft,
            RemoveTop,
            RemoveRight,
            RemoveBottom
        }

        // Draw the rectangles.
        private void Form1_Load(object sender, EventArgs e)
        {
            DrawBitmap();
        }
        private void Form1_Resize(object sender, EventArgs e)
        {
            DrawBitmap();
        }

        // Redraw.
        private void Options_CheckedChanged(object sender, EventArgs e)
        {
            DrawBitmap();
        }

        // Draw the bitmap.
        private void DrawBitmap()
        {
            Bitmap bm;

            // Determine the first rectangle's orientation and dimensions.
            double phi = (1 + Math.Sqrt(5)) / 2;
            RectOrientations orientation;
            int client_wid = picRectangles.ClientSize.Width;
            int client_hgt = picRectangles.ClientSize.Height;
            double wid, hgt;                // The rectangle's size.
            if (client_wid > client_hgt)
            {
                // Horizontal rectangle.
                orientation = RectOrientations.RemoveLeft;
                if (client_wid / (double)client_hgt > phi)
                {
                    hgt = client_hgt;
                    wid = hgt * phi;
                }
                else
                {
                    wid = client_wid;
                    hgt = wid / phi;
                }
            }
            else
            {
                // Vertical rectangle.
                orientation = RectOrientations.RemoveTop;
                if (client_hgt / (double)client_wid > phi)
                {
                    wid = client_wid;
                    hgt = wid * phi;
                }
                else
                {
                    hgt = client_hgt;
                    wid = hgt / phi;
                }
            }

            // Allow a margin.
            wid *= 0.95f;
            hgt *= 0.95f;

            // Center it.
            double x = (client_wid - wid) / 2;
            double y = (client_hgt - hgt) / 2;

            // Make the Bitmap.
            bm = new Bitmap(client_wid, client_hgt);

            // Draw the rectangles.
            using (Graphics gr = Graphics.FromImage(bm))
            {
                // Draw the rectangles.
                gr.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
                List<PointF> points = new List<PointF>();
                DrawPhiRectanglesOnGraphics(gr, points, x, y, wid, hgt, orientation);

                // Draw the square spiral.
                if (chkSquareSpiral.Checked) gr.DrawLines(Pens.Green, points.ToArray());
                // Smoothed square spiral:
                //gr.DrawCurve(Pens.Green, points.ToArray());

                if (chkTrueSpiral.Checked && points.Count > 1)
                {
                    // Draw the true spiral.
                    PointF start = points[0];
                    PointF origin = points[points.Count - 1];
                    float dx = start.X - origin.X;
                    float dy = start.Y - origin.Y;
                    double radius = Math.Sqrt(dx * dx + dy * dy);

                    double theta = Math.Atan2(dy, dx);
                    const int num_slices = 1000;
                    double dtheta = Math.PI / 2 / num_slices;
                    double factor = 1 - (1 / phi) / num_slices * 0.78; //@
                    List<PointF> new_points = new List<PointF>();

                    // Repeat until dist is too small to see.
                    while (radius > 0.1)
                    {
                        PointF new_point = new PointF(
                            (float)(origin.X + radius * Math.Cos(theta)),
                            (float)(origin.Y + radius * Math.Sin(theta)));
                        new_points.Add(new_point);
                        theta += dtheta;
                        radius *= factor;
                    }
                    gr.DrawLines(Pens.Blue, new_points.ToArray());
                }
            }

            // Display the result.
            picRectangles.Image = bm;
            picRectangles.Refresh();
        }

        // Draw rectangles on a Graphics object.
        private void DrawPhiRectanglesOnGraphics(Graphics gr, List<PointF> points, double x, double y, double wid, double hgt, RectOrientations orientation)
        {
            if ((wid < 1) || (hgt < 1)) return;

            // Draw this rectangle.
            if (chkRectangles.Checked) gr.DrawRectangle(Pens.Blue,
                (float)x, (float)y, (float)wid, (float)hgt);

            if (chkCircularSpiral.Checked)
            {
                // Draw a circular arc from the spiral.
                RectangleF rect;
                switch (orientation)
                {
                    case RectOrientations.RemoveLeft:
                        rect = new RectangleF(
                            (float)x, (float)y, (float)(2 * hgt), (float)(2 * hgt));
                        gr.DrawArc(Pens.Red, rect, 180, 90);
                        break;
                    case RectOrientations.RemoveTop:
                        rect = new RectangleF(
                            (float)(x - wid), (float)y, (float)(2 * wid), (float)(2 * wid));
                        gr.DrawArc(Pens.Red, rect, -90, 90);
                        break;
                    case RectOrientations.RemoveRight:
                        rect = new RectangleF(
                            (float)(x + wid - 2 * hgt),
                            (float)(y - hgt), (float)(2 * hgt), (float)(2 * hgt));
                        gr.DrawArc(Pens.Red, rect, 0, 90);
                        break;
                    case RectOrientations.RemoveBottom:
                        rect = new RectangleF((float)x, (float)(y + hgt - 2 * wid),
                            (float)(2 * wid), (float)(2 * wid));
                        gr.DrawArc(Pens.Red, rect, 90, 90);
                        break;
                }
            }

            // Recursively draw the next rectangle.
            switch (orientation)
            {
                case RectOrientations.RemoveLeft:
                    points.Add(new PointF((float)x, (float)(y + hgt)));
                    x += hgt;
                    wid -= hgt;
                    orientation = RectOrientations.RemoveTop;
                    break;
                case RectOrientations.RemoveTop:
                    points.Add(new PointF((float)x, (float)y));
                    y += wid;
                    hgt -= wid;
                    orientation = RectOrientations.RemoveRight;
                    break;
                case RectOrientations.RemoveRight:
                    points.Add(new PointF((float)(x + wid), (float)y));
                    wid -= hgt;
                    orientation = RectOrientations.RemoveBottom;
                    break;
                case RectOrientations.RemoveBottom:
                    points.Add(new PointF((float)(x + wid), (float)(y + hgt)));
                    hgt -= wid;
                    orientation = RectOrientations.RemoveLeft;
                    break;
            }
            DrawPhiRectanglesOnGraphics(gr, points, x, y, wid, hgt, orientation);
        }
    }
}
