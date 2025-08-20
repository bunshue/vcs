using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace vcs_DrawCircle
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The circle parameters.
        List<RectangleF> Circles = new List<RectangleF>();

        // Variables to get the newest circle.
        int X1, Y1, X2, Y2;
        bool Drawing = false;

        // The points of intersection.
        PointF Intersection1, Intersection2;
        int NumIntersections = 0;

        // Get a circle.
        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            if (Circles.Count == 2)
            {
                // Start over.
                Circles.Clear();
                NumIntersections = 0;
            }

            // Start this circle.
            X1 = X2 = e.X;
            Y1 = Y2 = e.Y;
            Drawing = true;
        }
        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (!Drawing) return;

            // Update the new circle's second corner.
            X2 = e.X;
            Y2 = e.Y;

            // Redraw.
            this.Invalidate();
        }
        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            Drawing = false;

            // Save the new circle.
            int width = Math.Min(Math.Abs(X1 - X2), Math.Abs(Y1 - Y2));
            RectangleF rect = new RectangleF(
                X1, Y1, width, width);
            if (X1 > X2) rect.X = X1 - width;
            if (Y1 > Y2) rect.Y = Y1 - width;
            Circles.Add(rect);

            // 集滿兩個圓
            if (Circles.Count == 2)
            {
                //第一個圓
                float radius0 = Circles[0].Height / 2;
                float cx0 = Circles[0].X + radius0;
                float cy0 = Circles[0].Y + radius0;

                //第二個圓
                float radius1 = Circles[1].Height / 2;
                float cx1 = Circles[1].X + radius1;
                float cy1 = Circles[1].Y + radius1;

                //取交點
                NumIntersections = FindCircleCircleIntersections(
                    cx0, cy0, radius0, cx1, cy1, radius1,
                    out Intersection1, out Intersection2);
            }

            // Redraw.
            this.Invalidate();
        }

        // Draw whatever we have.
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the circles.
            foreach (RectangleF rect in Circles)
            {
                e.Graphics.DrawEllipse(Pens.Blue, rect);
            }

            // Draw the new circle.
            if (Drawing)
            {
                int width = Math.Min(Math.Abs(X1 - X2), Math.Abs(Y1 - Y2));
                RectangleF rect = new RectangleF(
                    X1, Y1, width, width);
                if (X1 > X2) rect.X = X1 - width;
                if (Y1 > Y2) rect.Y = Y1 - width;
                e.Graphics.DrawEllipse(Pens.Red, rect);
            }

            // If we have a solution, display it.
            if (NumIntersections >= 1)
            {
                DrawPoint(e.Graphics, Intersection1, Brushes.HotPink, Pens.Red);
            }
            if (NumIntersections >= 2)
            {
                DrawPoint(e.Graphics, Intersection2, Brushes.HotPink, Pens.Red);
            }
        }

        // Find the points where the two circles intersect.
        private int FindCircleCircleIntersections(
            float cx0, float cy0, float radius0,
            float cx1, float cy1, float radius1,
            out PointF intersection1, out PointF intersection2)
        {
            // Find the distance between the centers.
            float dx = cx0 - cx1;
            float dy = cy0 - cy1;
            double dist = Math.Sqrt(dx * dx + dy * dy);

            // See how many solutions there are.
            if (dist > radius0 + radius1)
            {
                // No solutions, the circles are too far apart.
                intersection1 = new PointF(float.NaN, float.NaN);
                intersection2 = new PointF(float.NaN, float.NaN);
                return 0;
            }
            else if (dist < Math.Abs(radius0 - radius1))
            {
                // No solutions, one circle contains the other.
                intersection1 = new PointF(float.NaN, float.NaN);
                intersection2 = new PointF(float.NaN, float.NaN);
                return 0;
            }
            else if ((dist == 0) && (radius0 == radius1))
            {
                // No solutions, the circles coincide.
                intersection1 = new PointF(float.NaN, float.NaN);
                intersection2 = new PointF(float.NaN, float.NaN);
                return 0;
            }
            else
            {
                // Find a and h.
                double a = (radius0 * radius0 -
                    radius1 * radius1 + dist * dist) / (2 * dist);
                double h = Math.Sqrt(radius0 * radius0 - a * a);

                // Find P2.
                double cx2 = cx0 + a * (cx1 - cx0) / dist;
                double cy2 = cy0 + a * (cy1 - cy0) / dist;

                // Get the points P3.
                intersection1 = new PointF(
                    (float)(cx2 + h * (cy1 - cy0) / dist),
                    (float)(cy2 - h * (cx1 - cx0) / dist));
                intersection2 = new PointF(
                    (float)(cx2 - h * (cy1 - cy0) / dist),
                    (float)(cy2 + h * (cx1 - cx0) / dist));

                // See if we have 1 or 2 solutions.
                if (dist == radius0 + radius1) return 1;
                return 2;
            }
        }

        // Draw a point.
        private void DrawPoint(Graphics g, PointF pt, Brush brush, Pen pen)
        {
            const int RADIUS = 3;
            g.FillEllipse(brush,
                pt.X - RADIUS, pt.Y - RADIUS,
                2 * RADIUS, 2 * RADIUS);
            g.DrawEllipse(pen,
                pt.X - RADIUS, pt.Y - RADIUS,
                2 * RADIUS, 2 * RADIUS);
        }
    }
}
