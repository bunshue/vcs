using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;
using System.Drawing.Drawing2D;

namespace howto_minimal_bounding_rectangle
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The polygon's points.
        private PointF[] Points;
        private int NumPoints;

        // The points that have been used in test edges.
        private bool[] EdgeChecked = null;

        // The four caliper control points. They start:
        //       ControlPoints[0]      Left edge       xmin
        //       ControlPoints[1]      Bottom edge     ymax
        //       ControlPoints[2]      Right edge      xmax
        //       ControlPoints[3]      Top edge        ymin
        private int[] ControlPoints = new int[4];

        // The line from this point to the next one forms
        // one side of the rectangle.
        private int CurrentControlPoint = -1;

        // The area of the current bounding rectangle.
        private float CurrentArea = Single.MaxValue;
        private float BestArea = Single.MaxValue;
        private PointF[] BestRectangle = null;

        // The number of bounding rectangles we have examined.
        private int RectanglesExamined = 0;

        private void Form1_Load(object sender, EventArgs e)
        {
            // Make some points.
            Points = new PointF[]
            {
                new PointF(66, 196),
                new PointF(70, 210),
                new PointF(93, 222),
                new PointF(132, 232),
                new PointF(195, 237),
                new PointF(254, 172),
                new PointF(185, 51),
                new PointF(87, 92)
            };
            Points = new PointF[]
            {
                new PointF(67, 201),
                new PointF(104, 250),
                new PointF(140, 268),
                new PointF(183, 272),
                new PointF(226, 253),
                new PointF(262, 211),
                new PointF(279, 149),
                new PointF(270, 95),
                new PointF(250, 62),
                new PointF(217, 37),
                new PointF(172, 29),
                new PointF(131, 35),
                new PointF(94, 57),
                new PointF(71, 86),
                new PointF(60, 119),
                new PointF(59, 156)
            };
            Points = new PointF[]
            {
                new PointF(45, 148),
                new PointF(41, 188),
                new PointF(50, 217),
                new PointF(67, 244),
                new PointF(98, 258),
                new PointF(130, 252),
                new PointF(186, 233),
                new PointF(235, 206),
                new PointF(273, 162),
                new PointF(285, 117),
                new PointF(282, 70),
                new PointF(264, 45),
                new PointF(234, 28),
                new PointF(188, 36),
                new PointF(135, 56),
                new PointF(89, 93),
                new PointF(62, 120)
            };

            NumPoints = Points.Length;

            // Reset to get ready.
            btnReset_Click(null, null);
        }

        // Get ready to start over.
        private void btnReset_Click(object sender, EventArgs e)
        {
            float minx = Points[0].X;
            float maxx = minx;
            float miny = Points[0].Y;
            float maxy = miny;
            int minxi = 0;
            int maxxi = 0;
            int minyi = 0;
            int maxyi = 0;

            for (int i = 1; i < NumPoints; i++)
            {
                if (minx > Points[i].X)
                {
                    minx = Points[i].X;
                    minxi = i;
                }
                if (maxx < Points[i].X)
                {
                    maxx = Points[i].X;
                    maxxi = i;
                }
                if (miny > Points[i].Y)
                {
                    miny = Points[i].Y;
                    minyi = i;
                }
                if (maxy < Points[i].Y)
                {
                    maxy = Points[i].Y;
                    maxyi = i;
                }
            }

            ControlPoints[0] = minxi;
            ControlPoints[1] = maxyi;
            ControlPoints[2] = maxxi;
            ControlPoints[3] = minyi;
            CurrentControlPoint = -1;

            // We have not yet examined any bounding rectangles.
            RectanglesExamined = 0;
            btnStep.Enabled = true;

            // Reset the current and best bounding rectangle.
            CurrentArea = Single.MaxValue;
            BestArea = Single.MaxValue;
            BestRectangle = null;

            // So far we have not checked any edges.
            EdgeChecked = new bool[NumPoints];
            for (int i = 0; i < NumPoints; i++)
            {
                EdgeChecked[i] = false;
            }

            // Redraw.
            picCanvas.Invalidate();
        }

        // Check the next possible edge.
        private void btnStep_Click(object sender, EventArgs e)
        {
            // Increment the current control point.
            // This says we are done using this edge.
            if (CurrentControlPoint >= 0)
            {
                ControlPoints[CurrentControlPoint] =
                    (ControlPoints[CurrentControlPoint] + 1) % NumPoints;
            }

            // Find the next point on an edge.
            float xmindx, xmindy, ymaxdx, ymaxdy;
            float xmaxdx, xmaxdy, ymindx, ymindy;
            FindDxDy(out xmindx, out xmindy, ControlPoints[0]);
            FindDxDy(out ymaxdx, out ymaxdy, ControlPoints[1]);
            FindDxDy(out xmaxdx, out xmaxdy, ControlPoints[2]);
            FindDxDy(out ymindx, out ymindy, ControlPoints[3]);

            // Switch so we can look for the smallest opposite/adjacent ratio.
            float xminopp = xmindx;
            float xminadj = xmindy;
            float ymaxopp = -ymaxdy;
            float ymaxadj = ymaxdx;
            float xmaxopp = -xmaxdx;
            float xmaxadj = -xmaxdy;
            float yminopp = ymindy;
            float yminadj = -ymindx;

            // Pick initial values that will make every point an improvement.
            float bestopp = 1;
            float bestadj = 0;
            int best_control_point = -1;

            if ((xminopp >= 0) && (xminadj >= 0))
            {
                if (xminopp * bestadj < bestopp * xminadj)
                {
                    bestopp = xminopp;
                    bestadj = xminadj;
                    best_control_point = 0;
                }
            }
            if ((ymaxopp >= 0) && (ymaxadj >= 0))
            {
                if (ymaxopp * bestadj < bestopp * ymaxadj)
                {
                    bestopp = ymaxopp;
                    bestadj = ymaxadj;
                    best_control_point = 1;
                }
            }
            if ((xmaxopp >= 0) && (xmaxadj >= 0))
            {
                if (xmaxopp * bestadj < bestopp * xmaxadj)
                {
                    bestopp = xmaxopp;
                    bestadj = xmaxadj;
                    best_control_point = 2;
                }
            }
            if ((yminopp >= 0) && (yminadj >= 0))
            {
                if (yminopp * bestadj < bestopp * yminadj)
                {
                    bestopp = yminopp;
                    bestadj = yminadj;
                    best_control_point = 3;
                }
            }

            // Make sure we found a usable edge.
            Debug.Assert(best_control_point >= 0);

            // Use the new best control point.
            CurrentControlPoint = best_control_point;

            // Remember that we have checked this edge.
            EdgeChecked[ControlPoints[CurrentControlPoint]] = true;

            // See if we have checked all possible bounding rectangles.
            RectanglesExamined++;
            if (RectanglesExamined >= Points.Length)
            {
                btnStep.Enabled = false;
            }

            picCanvas.Invalidate();
        }

        private void picCanvas_Paint(object sender, PaintEventArgs e)
        {
            // See if we have started yet.
            using (Pen box_pen = new Pen(Color.Lime, 3))
            {
                if (CurrentControlPoint == -1)
                {
                    // Draw the initial bounding rectangle.
                    DrawBoundingRectangle(e.Graphics, box_pen,
                        Points[ControlPoints[0]].X, Points[ControlPoints[0]].Y, 0, 1,
                        Points[ControlPoints[1]].X, Points[ControlPoints[1]].Y, 1, 0,
                        Points[ControlPoints[2]].X, Points[ControlPoints[2]].Y, 0, -1,
                        Points[ControlPoints[3]].X, Points[ControlPoints[3]].Y, -1, 0);
                }
                else
                {
                    // See which point has the current edge.
                    int i1 = ControlPoints[CurrentControlPoint];
                    int i2 = (i1 + 1) % NumPoints;
                    float dx = Points[i2].X - Points[i1].X;
                    float dy = Points[i2].Y - Points[i1].Y;

                    // Make dx and dy work for the first line.
                    float temp;
                    switch (CurrentControlPoint)
                    {
                        case 0:  // null to do.
                            break;
                        case 1:  // dx = -dy, dy = dx
                            temp = dx;
                            dx = -dy;
                            dy = temp;
                            break;
                        case 2:  // dx = -dx, dy = -dy
                            dx = -dx;
                            dy = -dy;
                            break;
                        case 3:  // dx = dy, dy = -dx
                            temp = dx;
                            dx = dy;
                            dy = -temp;
                            break;
                    }

                    // Draw the bounding rectangle.
                    DrawBoundingRectangle(e.Graphics, box_pen,
                        Points[ControlPoints[0]].X, Points[ControlPoints[0]].Y, dx, dy,
                        Points[ControlPoints[1]].X, Points[ControlPoints[1]].Y, dy, -dx,
                        Points[ControlPoints[2]].X, Points[ControlPoints[2]].Y, -dx, -dy,
                        Points[ControlPoints[3]].X, Points[ControlPoints[3]].Y, -dy, dx);
                }
            }

            // Draw the best bounding rectangle.
            e.Graphics.DrawPolygon(Pens.Green, BestRectangle);

            // Draw the polygon and its points.
            using (Pen polygon_pen = new Pen(Color.Black, 5))
            {
                e.Graphics.DrawPolygon(polygon_pen, Points);
            }

            // Mark the polygon points.
            using (StringFormat sf = new StringFormat())
            {
                sf.Alignment = StringAlignment.Far;
                sf.LineAlignment = StringAlignment.Far;
                for (int i = 0; i < NumPoints; i++)
                {
                    e.Graphics.FillRectangle(Brushes.White,
                        Points[i].X - 3, Points[i].Y - 3, 6, 6);
                    e.Graphics.DrawRectangle(Pens.Black,
                        Points[i].X - 3, Points[i].Y - 3, 6, 6);
                    e.Graphics.DrawString(i.ToString(), this.Font,
                        Brushes.Black, Points[i].X, Points[i].Y, sf);
                }

                if (true)
                {
                    // Draw the edges that have been checked.
                    for (int i = 0; i < NumPoints; i++)
                    {
                        if (EdgeChecked[i])
                        {
                            int pt2 = (i + 1) % NumPoints;
                            using (Pen blue_pen = new Pen(Color.Cyan, 3))
                            {
                                e.Graphics.DrawLine(blue_pen, Points[i], Points[pt2]);
                            }
                        }
                    }

                    // Mark the control points.
                    sf.Alignment = StringAlignment.Near;
                    sf.LineAlignment = StringAlignment.Near;
                    for (int i = 0; i < 4; i++)
                    {
                        e.Graphics.FillEllipse(Brushes.Lime,
                            Points[ControlPoints[i]].X - 3,
                            Points[ControlPoints[i]].Y - 3, 6, 6);
                        e.Graphics.DrawString(i.ToString(), this.Font, Brushes.Red,
                            Points[ControlPoints[i]].X,
                            Points[ControlPoints[i]].Y, sf);
                    }

                    // Mark the selected control point//s edge.
                    if (CurrentControlPoint >= 0)
                    {
                        int pt1 = ControlPoints[CurrentControlPoint];
                        int pt2 = (pt1 + 1) % NumPoints;
                        using (Pen red_pen = new Pen(Color.Red, 3))
                        {
                            e.Graphics.DrawLine(red_pen, Points[pt1], Points[pt2]);
                        }
                    }
                }
            }
        }

        private void DrawBoundingRectangle(Graphics gr, Pen box_pen,
            float px0, float py0, float dx0, float dy0,
            float px1, float py1, float dx1, float dy1,
            float px2, float py2, float dx2, float dy2,
            float px3, float py3, float dx3, float dy3)
        {
            // Find the points of intersection.
            PointF[] pts = new PointF[4];
            FindIntersection(px0, py0, px0 + dx0, py0 + dy0, px1, py1, px1 + dx1, py1 + dy1, ref pts[0]);
            FindIntersection(px1, py1, px1 + dx1, py1 + dy1, px2, py2, px2 + dx2, py2 + dy2, ref pts[1]);
            FindIntersection(px2, py2, px2 + dx2, py2 + dy2, px3, py3, px3 + dx3, py3 + dy3, ref pts[2]);
            FindIntersection(px3, py3, px3 + dx3, py3 + dy3, px0, py0, px0 + dx0, py0 + dy0, ref pts[3]);

            // Draw the bounding rectangle.
            gr.DrawPolygon(box_pen, pts);

            // See if this is the best bounding rectangle so far.
            // Get the area of the bounding rectangle.
            float vx0 = pts[0].X - pts[1].X;
            float vy0 = pts[0].Y - pts[1].Y;
            float len0 = (float)Math.Sqrt(vx0 * vx0 + vy0 * vy0);

            float vx1 = pts[1].X - pts[2].X;
            float vy1 = pts[1].Y - pts[2].Y;
            float len1 = (float)Math.Sqrt(vx1 * vx1 + vy1 * vy1);

            CurrentArea = len0 * len1;
            if (CurrentArea < BestArea)
            {
                BestArea = CurrentArea;
                BestRectangle = pts;
            }

            lblCurrentArea.Text = CurrentArea.ToString("0.00");
            lblBestArea.Text = BestArea.ToString("0.00");
        }

        // Find the slope of the edge from point i to point i+1.
        private void FindDxDy(out float dx, out float dy, int i)
        {
            int i2 = (i + 1) % NumPoints;
            dx = Points[i2].X - Points[i].X;
            dy = Points[i2].Y - Points[i].Y;
        }

        // Find the point of intersection between two lines.
        private bool FindIntersection(float X1, float Y1, float X2, float Y2, float A1, float B1, float A2, float B2, ref PointF intersection)
        {
            float dx = X2 - X1;
            float dy = Y2 - Y1;
            float da = A2 - A1;
            float db = B2 - B1;
            float s, t;

            // If the segments are parallel, return False.
            if (Math.Abs(da * dy - db * dx) < 0.001) return false;

            // Find the point of intersection.
            s = (dx * (B1 - Y1) + dy * (X1 - A1)) / (da * dy - db * dx);
            t = (da * (Y1 - B1) + db * (A1 - X1)) / (db * dx - da * dy);
            intersection = new PointF(X1 + t * dx, Y1 + t * dy);
            return true;
        }
    }
}
