using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace howto_round_scaled_ellipses
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The drawing transformation and its inverse.
        private Matrix Transform, Inverse;

        // Initialize the drawing transformation.
        private const float XScale = 20;
        private const float YScale = 10;
        private void Form1_Load(object sender, EventArgs e)
        {
            // Make the drawing transformation.
            Transform = new Matrix();
            Transform.Scale(XScale, YScale);

            // Make the inverse transformation.
            Inverse = Transform.Clone();
            Inverse.Invert();
        }

        // Draw a scaled grid.
        private void DrawGrid(PictureBox pic, Graphics gr)
        {
            // Draw the grid.
            int hgt = (int)(1 + pic.ClientSize.Height / YScale);
            int wid = (int)(1 + pic.ClientSize.Width / XScale);
            using (Pen thin_pen = new Pen(Color.Blue, 0))
            {
                for (int x = 0; x < wid; x++)
                    gr.DrawLine(thin_pen, x, 0, x, hgt);
                for (int y = 0; y < hgt; y++)
                    gr.DrawLine(thin_pen, 0, y, wid, y);
            }
        }

        // The clicked points.
        private List<PointF> PointsClicked = new List<PointF>();

        // Draw the grid and any clicked points.
        private void picNormal_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            e.Graphics.Transform = Transform;

            // Draw the grid.
            DrawGrid(picNormal, e.Graphics);

            // If there are no points, do nothing else.
            if (PointsClicked.Count == 0) return;

            // Draw the points.
            foreach (PointF point in PointsClicked)
            {
                e.Graphics.DrawEllipse(Pens.Red, point.X - 1, point.Y - 1, 2, 2);
            }
        }

        // Draw the grid and any clicked points.
        private void picThinPen_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            e.Graphics.Transform = Transform;

            // Draw the grid.
            DrawGrid(picThinPen, e.Graphics);

            // If there are no points, do nothing else.
            if (PointsClicked.Count == 0) return;

            // Draw the points.
            using (Pen thin_pen = new Pen(Color.Red, 0))
            {
                foreach (PointF point in PointsClicked)
                    e.Graphics.DrawEllipse(thin_pen,
                        point.X - 1, point.Y - 1, 2, 2);
            }
        }

        // Draw the grid and any clicked points.
        private void picRound_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            e.Graphics.Transform = Transform;

            // Draw the grid.
            DrawGrid(picNormal, e.Graphics);

            // If there are no points, do nothing else.
            if (PointsClicked.Count == 0) return;

            // Reset the Graphics object's transformation.
            e.Graphics.ResetTransform();

            // Draw the points.
            using (Pen thick_pen = new Pen(Color.Red, 3))
            {
                // Use the inverse transform to convert
                // from world coordinates to device coordinates.
                PointF[] points = PointsClicked.ToArray();
                Transform.TransformPoints(points);

                // Draw the points' circles in device coordinates.
                foreach (PointF point in points)
                {
                    e.Graphics.DrawEllipse(thick_pen,
                        point.X - 5, point.Y - 5, 10, 10);
                }
            }
        }

        // Save a clicked point.
        private void pic_MouseClick(object sender, MouseEventArgs e)
        {
            // Transform the point to convert it from
            // device coordinates to world coordinates.
            PointF[] points = { new PointF(e.X, e.Y) };
            Inverse.TransformPoints(points);

            // Save the point's world coordinates.
            PointsClicked.Add(points[0]);

            // Redraw to show the new point.
            picNormal.Refresh();
            picThinPen.Refresh();
            picRound.Refresh();
        }
    }
}
