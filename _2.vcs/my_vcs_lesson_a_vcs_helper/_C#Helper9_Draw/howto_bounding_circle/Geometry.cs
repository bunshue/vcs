using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Drawing;

namespace howto_bounding_circle
{
    static class Geometry
    {
        // For debugging.
        public static PointF[] g_MinMaxCorners;
        public static RectangleF g_MinMaxBox;
        public static PointF[] g_NonCulledPoints;

        // Find the points nearest the upper left, upper right,
        // lower left, and lower right corners.
        private static void GetMinMaxCorners(List<PointF> points, ref PointF ul, ref PointF ur, ref PointF ll, ref PointF lr)
        {
            // Start with the first point as the solution.
            ul = points[0];
            ur = ul;
            ll = ul;
            lr = ul;

            // Search the other points.
            foreach (PointF pt in points)
            {
                if (-pt.X - pt.Y > -ul.X - ul.Y) ul = pt;
                if (pt.X - pt.Y > ur.X - ur.Y) ur = pt;
                if (-pt.X + pt.Y > -ll.X + ll.Y) ll = pt;
                if (pt.X + pt.Y > lr.X + lr.Y) lr = pt;
            }

            g_MinMaxCorners = new PointF[] {ul, ur, lr, ll}; // For debugging.
        }

        // Find a box that fits inside the MinMax quadrilateral.
        private static RectangleF GetMinMaxBox(List<PointF> points)
        {
            // Find the MinMax quadrilateral.
            PointF ul = new Point(0, 0), ur = ul, ll = ul, lr = ul;
            GetMinMaxCorners(points, ref ul, ref ur, ref ll, ref lr);

            // Get the coordinates of a box that lies inside this quadrilateral.
            float xmin, xmax, ymin, ymax;
            xmin = ul.X;
            ymin = ul.Y;

            xmax = ur.X;
            if (ymin < ur.Y) ymin = ur.Y;

            if (xmax > lr.X) xmax = lr.X;
            ymax = lr.Y;

            if (xmin < ll.X) xmin = ll.X;
            if (ymax > ll.Y) ymax = ll.Y;

            RectangleF result = new RectangleF(xmin, ymin, xmax - xmin, ymax - ymin);
            g_MinMaxBox = result;    // For debugging.
            return result;
        }

        // Cull points out of the convex hull that lie inside the
        // trapezoid defined by the vertices with smallest and
        // largest X and Y coordinates.
        // Return the points that are not culled.
        private static List<PointF> HullCull(List<PointF> points)
        {
            // Find a culling box.
            RectangleF culling_box = GetMinMaxBox(points);

            // Cull the points.
            List<PointF> results = new List<PointF>();
            foreach (PointF pt in points)
            {
                // See if (this point lies outside of the culling box.
                if (pt.X <= culling_box.Left ||
                    pt.X >= culling_box.Right ||
                    pt.Y <= culling_box.Top ||
                    pt.Y >= culling_box.Bottom)
                {
                    // This point cannot be culled.
                    // Add it to the results.
                    results.Add(pt);
                }
            }
            
            g_NonCulledPoints = new PointF[results.Count];   // For debugging.
            results.CopyTo(g_NonCulledPoints);              // For debugging.
            return results;
        }

        // Return the points that make up a polygon's convex hull.
        // This method leaves the points list unchanged.
        public static List<PointF> MakeConvexHull(List<PointF> points)
        {
            // Cull.
            points = HullCull(points);

            // Find the remaining point with the smallest Y value.
            // if (there's a tie, take the one with the smaller X value.
            PointF best_pt = points[0];
            foreach (PointF pt in points)
            {
                if ((pt.Y < best_pt.Y) ||
                   ((pt.Y == best_pt.Y) && (pt.X < best_pt.X)))
                {
                    best_pt = pt;
                }
            }

            // Move this point to the convex hull.
            List<PointF> hull = new List<PointF>();
            hull.Add(best_pt);
            points.Remove(best_pt);

            // Start wrapping up the other points.
            float sweep_angle = 0;
            for (;;)
            {
                // If all of the points are on the hull, we're done.
                if (points.Count == 0) break;

                // Find the point with smallest AngleValue
                // from the last point.
                float X = hull[hull.Count - 1].X;
                float Y = hull[hull.Count - 1].Y;
                best_pt = points[0];
                float best_angle = 3600;

                // Search the rest of the points.
                foreach (PointF pt in points)
                {
                    float test_angle = AngleValue(X, Y, pt.X, pt.Y);
                    if ((test_angle >= sweep_angle) &&
                        (best_angle > test_angle))
                    {
                        best_angle = test_angle;
                        best_pt = pt;
                    }
                }

                // See if the first point is better.
                // If so, we are done.
                float first_angle = AngleValue(X, Y, hull[0].X, hull[0].Y);
                if ((first_angle >= sweep_angle) &&
                    (best_angle >= first_angle))
                {
                    // The first point is better. We're done.
                    break;
                }

                // Add the best point to the convex hull.
                hull.Add(best_pt);
                points.Remove(best_pt);

                sweep_angle = best_angle;
            }

            return hull;
        }

        // Return a number that gives the ordering of angles
        // WRST horizontal from the point (x1, y1) to (x2, y2).
        // In other words, AngleValue(x1, y1, x2, y2) is not
        // the angle, but if:
        //   Angle(x1, y1, x2, y2) > Angle(x1, y1, x2, y2)
        // then
        //   AngleValue(x1, y1, x2, y2) > AngleValue(x1, y1, x2, y2)
        // this angle is greater than the angle for another set
        // of points,) this number for
        //
        // This function is dy / (dy + dx).
        private static float AngleValue(float x1, float y1, float x2, float y2)
        {
            float dx, dy, ax, ay, t;

            dx = x2 - x1;
            ax = Math.Abs(dx);
            dy = y2 - y1;
            ay = Math.Abs(dy);
            if (ax + ay == 0)
            {
                // if (the two points are the same, return 360.
                t = 360f / 9f;
            }
            else
            {
                t = dy / (ax + ay);
            }
            if (dx < 0)
            {
                t = 2 - t;
            }
            else if (dy < 0)
            {
                t = 4 + t;
            }
            return t * 90;
        }

        // Find a minimal bounding circle.
        public static void FindMinimalBoundingCircle(List<PointF> points, out PointF center, out float radius)
        {
            // Find the convex hull.
            List<PointF> hull = MakeConvexHull(points);

            // The best solution so far.
            PointF best_center = points[0];
            float best_radius2 = float.MaxValue;

            // Look at pairs of hull points.
            for (int i = 0; i < hull.Count - 1; i++)
            {
                for (int j = i + 1; j < hull.Count; j++)
                {
                    // Find the circle through these two points.
                    PointF test_center = new PointF(
                        (hull[i].X + hull[j].X) / 2f,
                        (hull[i].Y + hull[j].Y) / 2f);
                    float dx = test_center.X - hull[i].X;
                    float dy = test_center.Y - hull[i].Y;
                    float test_radius2 = dx * dx + dy * dy;

                    // See if this circle would be an improvement.
                    if (test_radius2 < best_radius2)
                    {
                        // See if this circle encloses all of the points.
                        if (CircleEnclosesPoints(test_center, test_radius2, hull, i, j, -1))
                        {
                            // Save this solution.
                            best_center = test_center;
                            best_radius2 = test_radius2;
                        }
                    }
                } // for i
            } // for j

            // Look at triples of hull points.
            for (int i = 0; i < hull.Count - 2; i++)
            {
                for (int j = i + 1; j < hull.Count - 1; j++)
                {
                    for (int k = j + 1; k < hull.Count; k++)
                    {
                        // Find the circle through these three points.
                        PointF test_center;
                        float test_radius2;
                        FindCircle(hull[i], hull[j], hull[k], out test_center, out test_radius2);

                        // See if this circle would be an improvement.
                        if (test_radius2 < best_radius2)
                        {
                            // See if this circle encloses all of the points.
                            if (CircleEnclosesPoints(test_center, test_radius2, hull, i, j, k))
                            {
                                // Save this solution.
                                best_center = test_center;
                                best_radius2 = test_radius2;
                            }
                        }
                    } // for k
                } // for i
            } // for j

            center = best_center;
            if (best_radius2 == float.MaxValue)
                radius = 0;
            else
                radius = (float)Math.Sqrt(best_radius2);
        }

        // Return true if the indicated circle encloses all of the points.
        private static bool CircleEnclosesPoints(PointF center,
            float radius2, List<PointF> points, int skip1, int skip2, int skip3)
        {
            for (int i = 0; i < points.Count; i++)
            {
                if ((i != skip1) && (i != skip2) && (i != skip3))
                {
                    PointF point = points[i];
                    float dx = center.X - point.X;
                    float dy = center.Y - point.Y;
                    float test_radius2 = dx * dx + dy * dy;
                    if (test_radius2 > radius2) return false;
                }
            }
            return true;
        }

        // Find a circle through the three points.
        private static void FindCircle(PointF a, PointF b, PointF c, out PointF center, out float radius2)
        {
            // Get the perpendicular bisector of (x1, y1) and (x2, y2).
            float x1 = (b.X + a.X) / 2;
            float y1 = (b.Y + a.Y) / 2;
            float dy1 = b.X - a.X;
            float dx1 = -(b.Y - a.Y);

            // Get the perpendicular bisector of (x2, y2) and (x3, y3).
            float x2 = (c.X + b.X) / 2;
            float y2 = (c.Y + b.Y) / 2;
            float dy2 = c.X - b.X;
            float dx2 = -(c.Y - b.Y);

            // See where the lines intersect.
            bool lines_intersect, segments_intersect;
            PointF intersection, close_p1, close_p2;
            FindIntersection(
                new PointF(x1, y1),
                new PointF(x1 + dx1, y1 + dy1),
                new PointF(x2, y2),
                new PointF(x2 + dx2, y2 + dy2),
                out lines_intersect,
                out segments_intersect,
                out intersection,
                out close_p1,
                out close_p2);

            center = intersection;
            float dx = center.X - a.X;
            float dy = center.Y - a.Y;
            radius2 = dx * dx + dy * dy;
        }

        // Extension method to draw a RectangleF.
        public static void DrawRectangle(this Graphics graphics, Pen pen, RectangleF rect)
        {
            graphics.DrawRectangle(pen, Rectangle.Round(rect));
        }

        // Find the point of intersection between
        // the lines p1 --> p2 and p3 --> p4.
        private static void FindIntersection(PointF p1, PointF p2, PointF p3, PointF p4,
            out bool lines_intersect, out bool segments_intersect,
            out PointF intersection, out PointF close_p1, out PointF close_p2)
        {
            // Get the segments' parameters.
            float dx12 = p2.X - p1.X;
            float dy12 = p2.Y - p1.Y;
            float dx34 = p4.X - p3.X;
            float dy34 = p4.Y - p3.Y;

            // Solve for t1 and t2
            float denominator = (dy12 * dx34 - dx12 * dy34);

            float t1;
            try
            {
                t1 = ((p1.X - p3.X) * dy34 + (p3.Y - p1.Y) * dx34) / denominator;
            }
            catch
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
    }
}
