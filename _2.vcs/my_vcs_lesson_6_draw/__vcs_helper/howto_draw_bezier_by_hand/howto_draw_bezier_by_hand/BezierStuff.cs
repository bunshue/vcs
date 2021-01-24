using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Drawing;
using System.Drawing.Drawing2D;

namespace howto_draw_bezier_by_hand
{
    class BezierStuff
    {
        // Parametric functions for drawing a degree 3 Bezier curve.
        private static float X(float t, float x0, float x1, float x2, float x3)
        {
            return (float)(
                x0 * Math.Pow((1 - t), 3) +
                x1 * 3 * t * Math.Pow((1 - t), 2) +
                x2 * 3 * Math.Pow(t, 2) * (1 - t) +
                x3 * Math.Pow(t, 3)
            );
        }
        private static float Y(float t, float y0, float y1, float y2, float y3)
        {
            return (float)(
                y0 * Math.Pow((1 - t), 3) +
                y1 * 3 * t * Math.Pow((1 - t), 2) +
                y2 * 3 * Math.Pow(t, 2) * (1 - t) +
                y3 * Math.Pow(t, 3)
            );
        }

        // Draw the Bezier curve.
        public static void DrawBezier(Graphics gr, Pen the_pen, float dt, PointF pt0, PointF pt1, PointF pt2, PointF pt3)
        {
            // Draw the curve.
            List<PointF> points = new List<PointF>();
            for (float t = 0.0f; t < 1.0; t += dt)
            {
                points.Add(new PointF(
                    X(t, pt0.X, pt1.X, pt2.X, pt3.X),
                    Y(t, pt0.Y, pt1.Y, pt2.Y, pt3.Y)));
            }

            // Connect to the final point.
            points.Add(new PointF(
                X(1.0f, pt0.X, pt1.X, pt2.X, pt3.X),
                Y(1.0f, pt0.Y, pt1.Y, pt2.Y, pt3.Y)));

            // Draw the curve.
            gr.DrawLines(the_pen, points.ToArray());

            // Draw lines connecting the control points.
            gr.DrawLine(Pens.Red, pt0, pt1);
            gr.DrawLine(Pens.Green, pt1, pt2);
            gr.DrawLine(Pens.Blue, pt2, pt3);
        }
    }
}
