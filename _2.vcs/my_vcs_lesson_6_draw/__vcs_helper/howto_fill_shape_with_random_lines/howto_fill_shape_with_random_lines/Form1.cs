using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace howto_fill_shape_with_random_lines
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The points selected by the user.
        private List<Point> ShapePoints = new List<Point>();
        private GraphicsPath ShapePath = null;
        private GraphicsPath LinesPath = null;
        private bool IsDrawing = false;

        // Start drawing.
        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            ShapePoints = new List<Point>();
            ShapePoints.Add(e.Location);
            IsDrawing = true;
            Refresh();
        }

        // Continue drawing.
        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (!IsDrawing) return;
            ShapePoints.Add(e.Location);
            Refresh();

            this.DoubleBuffered = true;
        }

        // Finish drawing.
        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            if (!IsDrawing) return;
            IsDrawing = false;

            // Generate the random lines to fill the shape.
            GenerateLines();

            Refresh();
        }

        // Generate the random lines to fill the shape.
        private void GenerateLines()
        {
            if (ShapePoints.Count < 3)
            {
                ShapePath = null;
                LinesPath = null;
                return;
            }

            // Make the shape's path.
            ShapePath = new GraphicsPath();
            ShapePath.AddPolygon(ShapePoints.ToArray());

            // Get the shape's bounds.
            RectangleF bounds = ShapePath.GetBounds();
            int xmin = (int)(bounds.Left);
            int xmax = (int)(bounds.Right) + 1;
            int ymin = (int)(bounds.Top);
            int ymax = (int)(bounds.Bottom) + 1;

            // Generate random lines.
            LinesPath = new GraphicsPath();
            int num_lines = (int)((bounds.Width + bounds.Height) / 8);
            Random rand = new Random();
            int x1, y1, x2, y2;
            for (int i = 1; i <= num_lines / 2; i++)
            {
                x1 = rand.Next(xmin, xmax);
                y1 = ymin;
                x2 = rand.Next(xmin, xmax);
                y2 = ymax;
                LinesPath.AddLine(x1, y1, x2, y2);

                x1 = xmin;
                y1 = rand.Next(ymin, ymax);
                x2 = xmax;
                y2 = rand.Next(ymin, ymax);
                LinesPath.AddLine(x1, y1, x2, y2);
            }
        }

        // Draw the shape.
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            // Draw the shape.
            if (IsDrawing)
            {
                // Draw the lines so far.
                if (ShapePoints.Count > 1)
                {
                    e.Graphics.DrawLines(Pens.Green, ShapePoints.ToArray());
                }
            }
            else
            {
                // Fill and outline the finished shape.
                if (ShapePath != null)
                {
                    if (chkAntiAlias.Checked)
                        e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

                    e.Graphics.FillPath(Brushes.LightGreen, ShapePath);
                    e.Graphics.DrawPath(Pens.Green, ShapePath);

                    // Fill with the lines.
                    e.Graphics.SetClip(ShapePath);
                    e.Graphics.DrawPath(Pens.Green, LinesPath);
                }
            }
        }

        // Redraw.
        private void chkAntiAlias_CheckedChanged(object sender, EventArgs e)
        {
            Refresh();
        }
    }
}
