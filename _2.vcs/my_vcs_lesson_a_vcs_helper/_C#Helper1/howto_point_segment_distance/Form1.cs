using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace howto_point_segment_distance
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The points that define the segment and point.
        List<PointF> Points = new List<PointF>();

        // The closest point on the segment.
        PointF Closest;
        bool HaveSolution = false;

        // Get a new point.
        private void Form1_MouseClick(object sender, MouseEventArgs e)
        {
            // If we have 3 points, start over.
            if (Points.Count == 3)
            {
                Points = new List<PointF>();
                HaveSolution = false;
            }

            // Get the new point.
            Points.Add(new PointF(e.X, e.Y));

            // If we have 3 points, solve.
            if (Points.Count == 3)
            {
                FindDistanceToSegment(Points[2], Points[0], Points[1], out Closest);
                HaveSolution = true;
            }

            // Redraw.
            this.Invalidate();
        }

        // Draw.
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the segment.
            if (Points.Count >= 2)
            {
                e.Graphics.DrawLine(Pens.Green, Points[0], Points[1]);
            }

            // Draw the points.
            foreach (PointF pt in Points)
            {
                DrawPoint(e.Graphics, pt, Brushes.White, Pens.Green);
            }

            // Draw the closest point on the segment.
            if (HaveSolution)
            {
                using (Pen dashed_pen = new Pen(Color.Red))
                {
                    dashed_pen.DashStyle = DashStyle.Custom;
                    dashed_pen.DashPattern = new float[] { 4, 4 };
                    e.Graphics.DrawLine(dashed_pen, Closest, Points[2]);
                }
                DrawPoint(e.Graphics, Closest, Brushes.HotPink, Pens.Red);
                DrawPoint(e.Graphics, Points[2], Brushes.HotPink, Pens.Red);
            }
        }

        // Draw a point.
        private void DrawPoint(Graphics gr, PointF pt, Brush brush, Pen pen)
        {
            const int RADIUS = 3;
            gr.FillEllipse(brush,
                pt.X - RADIUS, pt.Y - RADIUS,
                2 * RADIUS, 2 * RADIUS);
            gr.DrawEllipse(pen,
                pt.X - RADIUS, pt.Y - RADIUS,
                2 * RADIUS, 2 * RADIUS);
        }

        // Calculate the distance between
        // point pt and the segment p1 --> p2.
        private double FindDistanceToSegment(
            PointF pt, PointF p1, PointF p2, out PointF closest)
        {
            float dx = p2.X - p1.X;
            float dy = p2.Y - p1.Y;
            if ((dx == 0) && (dy == 0))
            {
                // It's a point not a line segment.
                closest = p1;
                dx = pt.X - p1.X;
                dy = pt.Y - p1.Y;
                return Math.Sqrt(dx * dx + dy * dy);
            }

            // Calculate the t that minimizes the distance.
            float t = ((pt.X - p1.X) * dx + (pt.Y - p1.Y) * dy) / (dx * dx + dy * dy);

            // See if this represents one of the segment's
            // end points or a point in the middle.
            if (t < 0)
            {
                closest = new PointF(p1.X, p1.Y);
                dx = pt.X - p1.X;
                dy = pt.Y - p1.Y;
            }
            else if (t > 1)
            {
                closest = new PointF(p2.X, p2.Y);
                dx = pt.X - p2.X;
                dy = pt.Y - p2.Y;
            }
            else
            {
                closest = new PointF(p1.X + t * dx, p1.Y + t * dy);
                dx = pt.X - closest.X;
                dy = pt.Y - closest.Y;
            }

            return Math.Sqrt(dx * dx + dy * dy);
        }
    }
}
