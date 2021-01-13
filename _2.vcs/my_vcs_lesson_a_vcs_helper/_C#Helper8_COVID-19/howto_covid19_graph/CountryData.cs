using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Drawing;
using System.Drawing.Drawing2D;

namespace howto_covid19_graph
{
    public class CountryData
    {
        static public DateTime[] Dates = null;
        public string Name = null;
        public int[] Cases = null;
        public int MaxCases = 0;
        public int CountryNumber = -1;

        public PointF[] DeviceCoords = null;

        public override string ToString()
        {
            return Name;
        }

        public void SetMax()
        {
            MaxCases = Cases.Max();
        }

        // Draw this country's data.
        public void Draw(Graphics gr, Pen pen, Matrix transform)
        {
            // Make the array of points.
            int num_cases = Cases.Length;
            PointF[] points = new PointF[num_cases];
            for (int i = 0; i < num_cases; i++)
                points[i] = new PointF(i, Cases[i]);

            // Draw the curve.
            gr.DrawLines(pen, points);

            // Find device coordinates for tooltips.
            transform.TransformPoints(points);
            DeviceCoords = points;
        }

        public bool PointIsAt(PointF device_point, out int day_num,
            out int num_cases, out PointF close_point)
        {
            const double close_dist = 4;
            PointF closest;
            for (int i = 1; i < Cases.Length; i++)
            {
                double dist = FindDistanceToSegment(device_point,
                    DeviceCoords[i - 1], DeviceCoords[i], out closest);
                if (dist <= close_dist)
                {
                    // See whether it is closer to this this
                    // segment's left or right point.
                    if (DistanceBetweenPoints(DeviceCoords[i - 1], closest) <
                        DistanceBetweenPoints(DeviceCoords[i], closest))
                        day_num = i - 1;
                    else
                        day_num = i;
                    num_cases = Cases[day_num];

                    // Use the point on the segment.
                    //close_point = closest;

                    // Use the closer segment end point.
                    close_point = DeviceCoords[day_num];
                    return true;
                }
            }

            day_num = -1;
            num_cases = -1;
            close_point = new PointF(-1, -1);
            return false;
        }

        // http://csharphelper.com/blog/2016/09/find-the-shortest-distance-between-a-point-and-a-line-segment-in-c/
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
            float t = ((pt.X - p1.X) * dx + (pt.Y - p1.Y) * dy) /
                (dx * dx + dy * dy);

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

        private double DistanceBetweenPoints(PointF p1, PointF p2)
        {
            float dx = p2.X - p1.X;
            float dy = p2.Y - p1.Y;
            return Math.Sqrt(dx * dx + dy * dy);
        }
    }
}
