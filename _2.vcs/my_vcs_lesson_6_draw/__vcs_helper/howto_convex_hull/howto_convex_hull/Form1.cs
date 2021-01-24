using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace howto_convex_hull
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private List<Point> m_Points = new List<Point>();

        private void btnClear_Click(object sender, EventArgs e)
        {
            m_Points = new List<Point>();
            this.Invalidate();
        }

        // Add a new Point.
        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            m_Points.Add(new Point(e.X, e.Y));
            this.Invalidate();
        }

        // Redraw.
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(this.BackColor);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the convex hull.

            // Fill all of the points.
            foreach (Point pt in m_Points)
            {
                e.Graphics.FillEllipse(Brushes.Cyan, pt.X - 3, pt.Y - 3, 7, 7);
            }

            List<Point> hull = null;
            if (m_Points.Count >= 3)
            {
                // Get the convex hull.
                hull = Geometry.MakeConvexHull(m_Points);

                // Draw.
                // Fill the non-culled points.
                foreach (Point pt in Geometry.g_NonCulledPoints)
                {
                    e.Graphics.FillEllipse(Brushes.White, pt.X - 3, pt.Y - 3, 7, 7);
                }
            }

            // Draw all of the points.
            foreach (Point pt in m_Points)
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
                Point[] hull_points = new Point[hull.Count];
                hull.CopyTo(hull_points);
                e.Graphics.DrawPolygon(Pens.Blue, hull_points);
            }
        }
    }
}
