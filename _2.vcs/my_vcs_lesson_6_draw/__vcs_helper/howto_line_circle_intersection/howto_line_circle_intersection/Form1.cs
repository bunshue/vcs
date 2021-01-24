using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace howto_line_circle_intersection
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The circle's coordinates.
        float Cx, Cy, Radius;

        // The points on the line.
        PointF Point1, Point2;
        bool Drawing = false, HavePoints = false;

        // The points of intersection.
        PointF Intersection1, Intersection2;
        int NumIntersections;

        // Redraw on resize.
        private void Form1_Load(object sender, EventArgs e)
        {
            this.ResizeRedraw = true;

            // Get the circle's initial geometry.
            InitializeCircle();
        }

        // Calculate the circle's position.
        private void Form1_Resize(object sender, EventArgs e)
        {
            NumIntersections = 0;
            HavePoints = false;
            InitializeCircle();
        }
        private void InitializeCircle()
        {
            Cx = this.ClientSize.Width / 2;
            Cy = this.ClientSize.Height / 2;
            Radius = (float)(Math.Min(Cx, Cy) * 0.8);
            HavePoints = false;
            this.Invalidate();
        }

        // Get the points.
        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            Drawing = true;
            NumIntersections = 0;
            Point1 = new PointF(e.X, e.Y);
            Point2 = new PointF(e.X, e.Y);
            HavePoints = true;
            this.Invalidate();
        }
        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (!Drawing) return;
            Point2 = new PointF(e.X, e.Y);
            this.Invalidate();
        }
        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            Drawing = false;

            // Find and draw the intersections.
            NumIntersections = FindLineCircleIntersections(
                Cx, Cy, Radius, Point1, Point2,
                out Intersection1, out Intersection2);
            this.Invalidate();
        }

        // Draw the circle and the segment if we have it.
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the circle.
            e.Graphics.DrawEllipse(Pens.Blue, 
                Cx - Radius, Cy - Radius, Radius * 2, Radius * 2);

            // Draw a dashed line from the segment points
            // to the points of intersection.
            if (HavePoints && (NumIntersections > 0))
            {
                using (Pen dashed_pen = new Pen(Color.Red))
                {
                    dashed_pen.DashPattern = new float[] { 3, 3 };
                    e.Graphics.DrawLine(dashed_pen, Intersection1, Point1);
                }
            }

            // Draw the intersections (if we have them).
            switch (NumIntersections)
            {
                case 0:
                    break;
                case 1:
                    DrawPoint(e.Graphics, Intersection1, Brushes.HotPink, Pens.Red);
                    break;
                case 2:
                    DrawPoint(e.Graphics, Intersection1, Brushes.HotPink, Pens.Red);
                    DrawPoint(e.Graphics, Intersection2, Brushes.HotPink, Pens.Red);
                    break;
            }

            // Draw the segment.
            if (HavePoints)
            {
                DrawPoint(e.Graphics, Point1, Brushes.White, Pens.Black);
                DrawPoint(e.Graphics, Point2, Brushes.White, Pens.Black);
                e.Graphics.DrawLine(Pens.BlueViolet, Point1, Point2);
            }
        }

        // Find the points of intersection.
        private int FindLineCircleIntersections(float cx, float cy, float radius,
            PointF point1, PointF point2, out PointF intersection1, out PointF intersection2)
        {
            float dx, dy, A, B, C, det, t;

            dx = point2.X - point1.X;
            dy = point2.Y - point1.Y;

            A = dx * dx + dy * dy;
            B = 2 * (dx * (point1.X - cx) + dy * (point1.Y - cy));
            C = (point1.X - cx) * (point1.X - cx) + (point1.Y - cy) * (point1.Y - cy) - radius * radius;

            det = B * B - 4 * A * C;
            if ((A <= 0.0000001) || (det < 0))
            {
                // No real solutions.
                intersection1 = new PointF(float.NaN, float.NaN);
                intersection2 = new PointF(float.NaN, float.NaN);
                return 0;
            }
            else if (det == 0)
            {
                // One solution.
                t = -B / (2 * A);
                intersection1 = new PointF(point1.X + t * dx, point1.Y + t * dy);
                intersection2 = new PointF(float.NaN, float.NaN);
                return 1;
            }
            else
            {
                // Two solutions.
                t = (float)((-B + Math.Sqrt(det)) / (2 * A));
                intersection1 = new PointF(point1.X + t * dx, point1.Y + t * dy);
                t = (float)((-B - Math.Sqrt(det)) / (2 * A));
                intersection2 = new PointF(point1.X + t * dx, point1.Y + t * dy);
                return 2;
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
    }
}
