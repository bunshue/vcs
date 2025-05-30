﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace howto_clip_line_to_polygon
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Tool types.
        private enum ToolTypes
        {
            None,
            Line,
            Polygon,
        }
        private ToolTypes SelectedTool = ToolTypes.None;

        // The mouse's current position.
        private Point MouseLocation;

        // The selected line segment.
        private List<PointF> LinePoints = new List<PointF>();

        // The selected polygon .
        private List<PointF> PolygonPoints = new List<PointF>();

        // Start drawing a polygon or line segment.
        private void picCanvas_MouseDown(object sender, MouseEventArgs e)
        {
            if (SelectedTool == ToolTypes.None) return;

            // See which tool is selected.
            if (SelectedTool == ToolTypes.Line)
            {
                LinePoints.Add(e.Location);

                // If we have both line points, stop.
                if (LinePoints.Count == 2)
                    SelectTool(ToolTypes.None);
            }
            else
            {
                // If this is the right mouse button, stop.
                if (e.Button == MouseButtons.Right)
                    SelectTool(ToolTypes.None);
                else
                    PolygonPoints.Add(e.Location);
            }

            // Redraw to show the new point.
            picCanvas.Refresh();
        }

        // Draw the selected line and polygon.
        private void picCanvas_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(picCanvas.BackColor);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the Polygon if we have one.
            if (SelectedTool == ToolTypes.Polygon)
            {
                if (PolygonPoints.Count > 1)
                    e.Graphics.DrawLines(Pens.Blue,
                        PolygonPoints.ToArray());
                if (PolygonPoints.Count > 0)
                    e.Graphics.DrawLine(Pens.Green,
                        PolygonPoints[PolygonPoints.Count - 1],
                        MouseLocation);
            }
            else if (PolygonPoints.Count > 2)
            {
                e.Graphics.FillPolygon(Brushes.LightBlue,
                    PolygonPoints.ToArray());
                e.Graphics.DrawPolygon(Pens.Blue,
                    PolygonPoints.ToArray());
            }

            // Draw the clipped line segment.
            if ((SelectedTool == ToolTypes.None) &&
                (PolygonPoints.Count > 2) &&
                (LinePoints.Count == 2))
            {
                bool draw;
                PointF[] intersections = ClipLineWithPolygon(
                    out draw, LinePoints[0], LinePoints[1], PolygonPoints);

                using (Pen pen = new Pen(Color.Pink, 5))
                {
                    for (int i = 0; i < intersections.Length - 1; i++)
                    {
                        if (draw) pen.Color = Color.Pink;
                        else pen.Color = Color.Yellow;
                        draw = !draw;

                        e.Graphics.DrawLine(pen,
                            intersections[i], intersections[i + 1]);
                    }
                    foreach (PointF point in intersections)
                        DrawPoint(e.Graphics, point);
                }
            }

            // Draw the line if we have one.
            if (LinePoints.Count == 2)
                e.Graphics.DrawLine(Pens.Red,
                    LinePoints[0], LinePoints[1]);
            else if (LinePoints.Count == 1)
                e.Graphics.DrawLine(Pens.Green,
                    LinePoints[0], MouseLocation);
        }

        private void DrawPoint(Graphics gr, PointF point)
        {
            RectangleF rect = new RectangleF(
                point.X - 3, point.Y - 3, 6, 6);
            gr.FillEllipse(Brushes.White, rect);
            gr.DrawEllipse(Pens.Black, rect);
        }

        // Update the current mouse position.
        private void picCanvas_MouseMove(object sender, MouseEventArgs e)
        {
            if (SelectedTool != ToolTypes.None)
            {
                MouseLocation = e.Location;
                picCanvas.Refresh();
            }
        }

        // Select the appropriate tool.
        private void btnLine_Click(object sender, EventArgs e)
        {
            if (btnLine.Checked) SelectTool(ToolTypes.None);
            else SelectTool(ToolTypes.Line);
        }
        private void btnPolygon_Click(object sender, EventArgs e)
        {
            if (btnPolygon.Checked) SelectTool(ToolTypes.None);
            else SelectTool(ToolTypes.Polygon);
        }

        // Select the tool and use the appropriate cursor.
        private void SelectTool(ToolTypes tool)
        {
            // If we have selected an invalid line, discard it.
            if ((SelectedTool == ToolTypes.Line) &&
                (LinePoints.Count == 1))
                    LinePoints = new List<PointF>();

            // If we have selected an invalid polygon, discard it.
            if ((SelectedTool == ToolTypes.Polygon) &&
                (PolygonPoints.Count < 3))
                    PolygonPoints = new List<PointF>();

            // Select the new tool.
            SelectedTool = tool;
            switch (SelectedTool)
            {
                case ToolTypes.None:
                    Cursor = Cursors.Default;
                    btnLine.Checked = false;
                    btnPolygon.Checked = false;
                    break;

                case ToolTypes.Line:
                    Cursor = Cursors.Cross;
                    btnLine.Checked = true;
                    btnPolygon.Checked = false;
                    LinePoints = new List<PointF>();
                    break;

                case ToolTypes.Polygon:
                    Cursor = Cursors.Cross;
                    btnLine.Checked = false;
                    btnPolygon.Checked = true;
                    PolygonPoints = new List<PointF>();
                    break;
            }
            picCanvas.Refresh();
        }

        // Return points where the segment enters and leaves the polygon.
        private PointF[] ClipLineWithPolygon(
            out bool starts_outside_polygon,
            PointF point1, PointF point2,
            List<PointF> polygon_points)
        {
            // Make lists to hold points of
            // intersection and their t values.
            List<PointF> intersections = new List<PointF>();
            List<float> t_values = new List<float>();

            // Add the segment's starting point.
            intersections.Add(point1);
            t_values.Add(0f);
            starts_outside_polygon =
                !PointIsInPolygon(point1.X, point1.Y,
                    polygon_points.ToArray());

            // Examine the polygon's edges.
            for (int i1 = 0; i1 < polygon_points.Count; i1++)
            {
                // Get the end points for this edge.
                int i2 = (i1 + 1) % polygon_points.Count;

                // See where the edge intersects the segment.
                bool lines_intersect, segments_intersect;
                PointF intersection, close_p1, close_p2;
                float t1, t2;
                FindIntersection(point1, point2,
                    polygon_points[i1], polygon_points[i2],
                    out lines_intersect, out segments_intersect,
                    out intersection, out close_p1, out close_p2,
                    out t1, out t2);

                // See if the segment intersects the edge.
                if (segments_intersect)
                {
                    // See if we need to record this intersection.

                    // Record this intersection.
                    intersections.Add(intersection);
                    t_values.Add(t1);
                }
            }

            // Add the segment's ending point.
            intersections.Add(point2);
            t_values.Add(1f);

            // Sort the points of intersection by t value.
            PointF[] intersections_array = intersections.ToArray();
            float[] t_array = t_values.ToArray();
            Array.Sort(t_array, intersections_array);

            // Return the intersections.
            return intersections_array;
        }

        // Find the point of intersection between
        // the lines p1 --> p2 and p3 --> p4.
        private void FindIntersection(PointF p1, PointF p2, PointF p3, PointF p4,
            out bool lines_intersect, out bool segments_intersect,
            out PointF intersection, out PointF close_p1, out PointF close_p2,
            out float t1, out float t2)
        {
            // Get the segments' parameters.
            float dx12 = p2.X - p1.X;
            float dy12 = p2.Y - p1.Y;
            float dx34 = p4.X - p3.X;
            float dy34 = p4.Y - p3.Y;

            // Solve for t1 and t2
            float denominator = (dy12 * dx34 - dx12 * dy34);
            t1 = ((p1.X - p3.X) * dy34 + (p3.Y - p1.Y) * dx34) / denominator;
            if (float.IsInfinity(t1))
            {
                // The lines are parallel (or close enough to it).
                lines_intersect = false;
                segments_intersect = false;
                intersection = new PointF(float.NaN, float.NaN);
                close_p1 = new PointF(float.NaN, float.NaN);
                close_p2 = new PointF(float.NaN, float.NaN);
                t2 = float.PositiveInfinity;
                return;
            }
            lines_intersect = true;

            t2 = ((p3.X - p1.X) * dy12 + (p1.Y - p3.Y) * dx12) / -denominator;

            // Find the point of intersection.
            intersection = new PointF(p1.X + dx12 * t1, p1.Y + dy12 * t1);

            // The segments intersect if t1 and t2 are between 0 and 1.
            segments_intersect = ((t1 >= 0) && (t1 <= 1) && (t2 >= 0) && (t2 <= 1));

            // Find the closest points on the segments.
            if (t1 < 0) t1 = 0;
            else if (t1 > 1) t1 = 1;

            if (t2 < 0) t2 = 0;
            else if (t2 > 1) t2 = 1;

            close_p1 = new PointF(p1.X + dx12 * t1, p1.Y + dy12 * t1);
            close_p2 = new PointF(p3.X + dx34 * t2, p3.Y + dy34 * t2);
        }

        // Return true if the point is in the polygon.
        public bool PointIsInPolygon(float X, float Y, PointF[] polygon_points)
        {
            // Get the angle between the point and the
            // first and last vertices.
            int max_point = polygon_points.Length - 1;
            float total_angle = GetAngle(
                polygon_points[max_point].X, polygon_points[max_point].Y,
                X, Y,
                polygon_points[0].X, polygon_points[0].Y);

            // Add the angles from the point
            // to each other pair of vertices.
            for (int i = 0; i < max_point; i++)
            {
                total_angle += GetAngle(
                    polygon_points[i].X, polygon_points[i].Y,
                    X, Y,
                    polygon_points[i + 1].X, polygon_points[i + 1].Y);
            }

            // The total angle should be 2 * PI or -2 * PI if
            // the point is in the polygon and close to zero
            // if the point is outside the polygon.
            return (Math.Abs(total_angle) > 0.000001);
        }

        // Return the angle ABC.
        // Return a value between PI and -PI.
        // Note that the value is the opposite of what you might
        // expect because Y coordinates increase downward.
        public static float GetAngle(float Ax, float Ay,
            float Bx, float By, float Cx, float Cy)
        {
            // Get the dot product.
            float dot_product = DotProduct(Ax, Ay, Bx, By, Cx, Cy);

            // Get the cross product.
            float cross_product = CrossProductLength(Ax, Ay, Bx, By, Cx, Cy);

            // Calculate the angle.
            return (float)Math.Atan2(cross_product, dot_product);
        }

        // Return the dot product AB · BC.
        // Note that AB · BC = |AB| * |BC| * Cos(theta).
        private static float DotProduct(float Ax, float Ay,
            float Bx, float By, float Cx, float Cy)
        {
            // Get the vectors' coordinates.
            float BAx = Ax - Bx;
            float BAy = Ay - By;
            float BCx = Cx - Bx;
            float BCy = Cy - By;

            // Calculate the dot product.
            return (BAx * BCx + BAy * BCy);
        }

        // Return the cross product AB x BC.
        // The cross product is a vector perpendicular to AB
        // and BC having length |AB| * |BC| * Sin(theta) and
        // with direction given by the right-hand rule.
        // For two vectors in the X-Y plane, the result is a
        // vector with X and Y components 0 so the Z component
        // gives the vector's length and direction.
        public static float CrossProductLength(float Ax, float Ay,
            float Bx, float By, float Cx, float Cy)
        {
            // Get the vectors' coordinates.
            float BAx = Ax - Bx;
            float BAy = Ay - By;
            float BCx = Cx - Bx;
            float BCy = Cy - By;

            // Calculate the Z coordinate of the cross product.
            return (BAx * BCy - BAy * BCx);
        }
    }
}
