using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

// Add a reference to WindowsBase.

using System.Drawing.Drawing2D;
using System.Diagnostics;
using System.Windows;

namespace vcs_Draw_Polygons2
{
    public partial class Form1 : Form
    {
        private List<PointF> Points = new List<PointF>();
        private PointF CurrentPoint;
        private bool Drawing = false;
        private int EnlargeBy = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void picCanvas_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(picCanvas.BackColor);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            e.Graphics.DrawString("左鍵點選頂點", new Font("標楷體", 30), new SolidBrush(Color.Green), new PointF(10, 10));
            e.Graphics.DrawString("右鍵結束", new Font("標楷體", 30), new SolidBrush(Color.Green), new PointF(10, 10 + 40));

            if (Drawing)
            {
                if (Points.Count >= 2)
                {
                    e.Graphics.DrawLines(Pens.Red, Points.ToArray());
                }
                e.Graphics.DrawLine(Pens.Pink, Points[Points.Count - 1], CurrentPoint);
            }
            else
            {
                if (Points.Count >= 3)
                {
                    e.Graphics.DrawPolygon(Pens.Red, Points.ToArray());
                    if (EnlargeBy > 0)
                    {
                        DrawEnlargedPolygon(e.Graphics);
                    }
                }
            }
        }

        private void picCanvas_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Right)
            {
                if (Drawing)
                {
                    Drawing = false;

                    // Make sure the polygon is oriented counter clockwise.
                    if (PolygonIsOrientedClockwise(Points))
                    {
                        // Reverse the points.
                        List<PointF> pts = new List<PointF>();
                        for (int i = Points.Count - 1; i >= 0; i--)
                        {
                            pts.Add(Points[i]);
                        }
                        Points = pts;
                    }
                }
            }
            else
            {
                if (!Drawing)
                {
                    Drawing = true;
                    Points = new List<PointF>();
                }
                CurrentPoint = e.Location;
                Points.Add(CurrentPoint);
            }
            picCanvas.Refresh();
        }

        private void picCanvas_MouseMove(object sender, MouseEventArgs e)
        {
            if (!Drawing)
            {
                return;
            }
            CurrentPoint = e.Location;
            picCanvas.Refresh();
        }

        private void hscrPixels_Scroll(object sender, ScrollEventArgs e)
        {
            lblPixels.Text = hscrPixels.Value.ToString();
            EnlargeBy = hscrPixels.Value;
            picCanvas.Refresh();
        }

        // Enlarge the polygon and draw it.
        private void DrawEnlargedPolygon(Graphics gr)
        {
            List<PointF> enlarged_points = GetEnlargedPolygon(Points, hscrPixels.Value);
            gr.DrawPolygon(Pens.Green, enlarged_points.ToArray());
        }

        // Return points representing an enlarged polygon.
        private List<PointF> GetEnlargedPolygon(List<PointF> old_points, float offset)
        {
            List<PointF> enlarged_points = new List<PointF>();
            int num_points = old_points.Count;
            for (int j = 0; j < num_points; j++)
            {
                // Find the new location for point j.
                // Find the points before and after j.
                int i = (j - 1);
                if (i < 0)
                {
                    i += num_points;
                }
                int k = (j + 1) % num_points;

                // Move the points by the offset.
                Vector v1 = new Vector(old_points[j].X - old_points[i].X, old_points[j].Y - old_points[i].Y);
                v1.Normalize();
                v1 *= offset;
                Vector n1 = new Vector(-v1.Y, v1.X);

                PointF pij1 = new PointF((float)(old_points[i].X + n1.X), (float)(old_points[i].Y + n1.Y));
                PointF pij2 = new PointF((float)(old_points[j].X + n1.X), (float)(old_points[j].Y + n1.Y));

                Vector v2 = new Vector(old_points[k].X - old_points[j].X, old_points[k].Y - old_points[j].Y);
                v2.Normalize();
                v2 *= offset;
                Vector n2 = new Vector(-v2.Y, v2.X);

                PointF pjk1 = new PointF((float)(old_points[j].X + n2.X), (float)(old_points[j].Y + n2.Y));
                PointF pjk2 = new PointF((float)(old_points[k].X + n2.X), (float)(old_points[k].Y + n2.Y));

                // See where the shifted lines ij and jk intersect.
                bool lines_intersect, segments_intersect;
                PointF poi, close1, close2;
                FindIntersection(pij1, pij2, pjk1, pjk2, out lines_intersect, out segments_intersect, out poi, out close1, out close2);
                Debug.Assert(lines_intersect, "Edges " + i + "-->" + j + " and " + j + "-->" + k + " are parallel");

                enlarged_points.Add(poi);
            }

            return enlarged_points;
        }

        // Find the point of intersection between
        // the lines p1 --> p2 and p3 --> p4.
        private void FindIntersection(
            PointF p1, PointF p2, PointF p3, PointF p4,
            out bool lines_intersect, out bool segments_intersect,
            out PointF intersection,
            out PointF close_p1, out PointF close_p2)
        {
            // Get the segments' parameters.
            float dx12 = p2.X - p1.X;
            float dy12 = p2.Y - p1.Y;
            float dx34 = p4.X - p3.X;
            float dy34 = p4.Y - p3.Y;

            // Solve for t1 and t2
            float denominator = (dy12 * dx34 - dx12 * dy34);

            float t1 = ((p1.X - p3.X) * dy34 + (p3.Y - p1.Y) * dx34) / denominator;
            if (float.IsInfinity(t1))
            {
                // The lines are parallel (or close enough to it).
                lines_intersect = false;
                segments_intersect = false;
                intersection = new PointF(float.NaN, float.NaN);
                close_p1 = new PointF(float.NaN, float.NaN);
                close_p2 = new PointF(float.NaN, float.NaN);
                return;
            }
            lines_intersect = true;

            float t2 = ((p3.X - p1.X) * dy12 + (p1.Y - p3.Y) * dx12) / -denominator;

            // Find the point of intersection.
            intersection = new PointF(p1.X + dx12 * t1, p1.Y + dy12 * t1);

            // The segments intersect if t1 and t2 are between 0 and 1.
            segments_intersect = ((t1 >= 0) && (t1 <= 1) && (t2 >= 0) && (t2 <= 1));

            // Find the closest points on the segments.
            if (t1 < 0)
            {
                t1 = 0;
            }
            else if (t1 > 1)
            {
                t1 = 1;
            }

            if (t2 < 0)
            {
                t2 = 0;
            }
            else if (t2 > 1)
            {
                t2 = 1;
            }

            close_p1 = new PointF(p1.X + dx12 * t1, p1.Y + dy12 * t1);
            close_p2 = new PointF(p3.X + dx34 * t2, p3.Y + dy34 * t2);
        }

        // Return true if the polygon is oriented clockwise.
        public bool PolygonIsOrientedClockwise(List<PointF> points)
        {
            return (SignedPolygonArea(points) < 0);
        }

        // Return the polygon's area in "square units."
        // The value will be negative if the polygon is
        // oriented clockwise.
        private float SignedPolygonArea(List<PointF> points)
        {
            // Add the first point to the end.
            int num_points = points.Count;
            PointF[] pts = new PointF[num_points + 1];
            points.CopyTo(pts, 0);
            pts[num_points] = points[0];

            // Get the areas.
            float area = 0;
            for (int i = 0; i < num_points; i++)
            {
                area += (pts[i + 1].X - pts[i].X) * (pts[i + 1].Y + pts[i].Y) / 2;
            }

            // Return the result.
            return area;
        }

        // Clear the Points list.
        private void mnuFileNew_Click(object sender, EventArgs e)
        {
            Points = new List<PointF>();
            picCanvas.Refresh();
            hscrPixels.Value = 0;
        }
    }
}
