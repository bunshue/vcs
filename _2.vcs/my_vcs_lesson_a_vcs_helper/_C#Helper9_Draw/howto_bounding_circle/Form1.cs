using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace howto_bounding_circle
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // All of the points.
        private List<PointF> m_Points = new List<PointF>();

        // The convex hull points.
        private List<PointF> ConvexHull = null;

        // The bounding circle.
        private PointF CircleCenter;
        private float CircleRadius = -1;

        private void btnClear_Click(object sender, EventArgs e)
        {
            m_Points = new List<PointF>();
            CircleRadius = -1;
            this.Invalidate();
        }

        // Add a new Point.
        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            // Add the new point.
            m_Points.Add(new Point(e.X, e.Y));

            // Get the convex hull.
            ConvexHull = Geometry.MakeConvexHull(m_Points);

            // Get a minimal bounding circle.
            Geometry.FindMinimalBoundingCircle(ConvexHull,
                out CircleCenter, out CircleRadius);

            // Redraw.
            this.Invalidate();
        }

        // Redraw.
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(this.BackColor);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Fill all of the points.
            foreach (PointF pt in m_Points)
            {
                e.Graphics.FillEllipse(Brushes.Cyan, pt.X - 3, pt.Y - 3, 7, 7);
            }

            // Fill the non-culled points.
            if (Geometry.g_NonCulledPoints != null)
            {
                foreach (PointF pt in Geometry.g_NonCulledPoints)
                {
                    e.Graphics.FillEllipse(Brushes.White, pt.X - 3, pt.Y - 3, 7, 7);
                }
            }

            // Draw all of the points.
            foreach (PointF pt in m_Points)
            {
                e.Graphics.DrawEllipse(Pens.Black, pt.X - 3, pt.Y - 3, 7, 7);
            }

            if (m_Points.Count >= 3)
            {
                // Draw the MinMax quadrilateral.
                e.Graphics.DrawPolygon(Pens.Red, Geometry.g_MinMaxCorners);

                // Draw the culling box.
                e.Graphics.DrawRectangle(Pens.Orange, Geometry.g_MinMaxBox);

                // Draw the convex hull.
                PointF[] hull_points = new PointF[ConvexHull.Count];
                ConvexHull.CopyTo(hull_points);
                e.Graphics.DrawPolygon(Pens.Blue, hull_points);
            }

            // If we have a counding circle, draw it.
            if (CircleRadius > 0)
            {
                RectangleF rect = new RectangleF(
                    CircleCenter.X - CircleRadius,
                    CircleCenter.Y - CircleRadius,
                    2 * CircleRadius, 2 * CircleRadius);
                e.Graphics.DrawEllipse(Pens.Green, rect);
                e.Graphics.FillEllipse(Brushes.Green,
                    CircleCenter.X - 2,
                    CircleCenter.Y - 2, 5, 5);
            }
        }
    }
}
