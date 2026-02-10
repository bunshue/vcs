using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace vcs_Draw_Polygons
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Each polygon is represented by a List<Point>.
        private List<List<Point>> Polygons = new List<List<Point>>();

        // Points for the new polygon.
        private List<Point> NewPolygon = null;

        // The current mouse position while drawing a new polygon.
        private Point NewPoint;

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        // Start or continue drawing a new polygon.
        private void picCanvas_MouseDown(object sender, MouseEventArgs e)
        {
            // See if we are already drawing a polygon.
            if (NewPolygon != null)
            {
                // We are already drawing a polygon.
                // If it's the right mouse button, finish this polygon.
                if (e.Button == MouseButtons.Right)
                {
                    // Finish this polygon.
                    if (NewPolygon.Count > 2)
                    {
                        Polygons.Add(NewPolygon);
                    }
                    NewPolygon = null;
                }
                else
                {
                    // Add a point to this polygon.
                    if (NewPolygon[NewPolygon.Count - 1] != e.Location)
                    {
                        NewPolygon.Add(e.Location);
                    }
                }
            }
            else
            {
                // Start a new polygon.
                NewPolygon = new List<Point>();
                NewPoint = e.Location;
                NewPolygon.Add(e.Location);
            }

            // Redraw.
            picCanvas.Invalidate();
        }

        // Move the next point in the new polygon.
        private void picCanvas_MouseMove(object sender, MouseEventArgs e)
        {
            if (NewPolygon == null)
            {
                return;
            }
            NewPoint = e.Location;
            picCanvas.Invalidate();
        }

        // Redraw old polygons in blue. Draw the new polygon in green.
        // Draw the final segment dashed.
        private void picCanvas_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            e.Graphics.Clear(picCanvas.BackColor);

            e.Graphics.DrawString("左鍵點選頂點", new Font("標楷體", 30), new SolidBrush(Color.Green), new PointF(10, 10));
            e.Graphics.DrawString("右鍵結束", new Font("標楷體", 30), new SolidBrush(Color.Green), new PointF(10, 10 + 40));

            // Draw the old polygons.
            foreach (List<Point> polygon in Polygons)
            {
                e.Graphics.FillPolygon(Brushes.White, polygon.ToArray());
                e.Graphics.DrawPolygon(Pens.Blue, polygon.ToArray());
            }

            // Draw the new polygon.
            if (NewPolygon != null)
            {
                // Draw the new polygon.
                if (NewPolygon.Count > 1)
                {
                    e.Graphics.DrawLines(Pens.Green, NewPolygon.ToArray());
                }

                // Draw the newest edge.
                if (NewPolygon.Count > 0)
                {
                    using (Pen dashed_pen = new Pen(Color.Green))
                    {
                        dashed_pen.DashPattern = new float[] { 3, 3 };
                        e.Graphics.DrawLine(dashed_pen, NewPolygon[NewPolygon.Count - 1], NewPoint);
                    }
                }
            }
        }
    }
}
