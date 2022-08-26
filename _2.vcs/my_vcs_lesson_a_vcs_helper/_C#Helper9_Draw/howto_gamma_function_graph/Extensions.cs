using System;
using System.Drawing;
using System.Drawing.Drawing2D;

namespace howto_gamma_function_graph
{
    public static class Extensions
    {
        // Make transformation matrices to map between
        // world coordinates to device coordinates.
        public static void MakeTransforms(this Graphics gr,
            float wxmin, float wymin, float wxmax, float wymax,
            float dxmin, float dymin, float dxmax, float dymax,
            bool apply_transform,
            out Matrix transform, out Matrix inverse)
        {
            RectangleF world_rect = new RectangleF(
                wxmin, wymin, wxmax - wxmin, wymax - wymin);
            PointF[] device_points =
            {
                new PointF(dxmin, dymax),
                new PointF(dxmax, dymax),
                new PointF(dxmin, dymin),
            };

            transform = new Matrix(world_rect, device_points);
            inverse = transform.Clone();
            inverse.Invert();

            if (apply_transform) gr.Transform = transform;
        }

        public static PointF TransformPoint(this Matrix transform, PointF point)
        {
            PointF[] points = { point };
            transform.TransformPoints(points);
            return points[0];
        }

        public static void WDrawLine(
            this Graphics gr, Matrix transform,
            Pen pen, PointF wp0, PointF wp1)
        {
            PointF[] points = { wp0, wp1 };
            transform.TransformPoints(points);
            gr.DrawLine(pen, points[0], points[1]);
        }

        public static void WDrawLine(
            this Graphics gr, Matrix transform,
            Pen pen, float wx0, float wy0, float wx1, float wy1)
        {
            gr.WDrawLine(transform, pen, 
                new PointF(wx0, wy0),
                new PointF(wx1, wy1));
        }

        public static void WDrawLines(
            this Graphics gr, Matrix transform,
            Pen pen, PointF[] wpoints)
        {
            PointF[] dpoints = (PointF[])wpoints.Clone();
            transform.TransformPoints(dpoints);
            gr.DrawLines(pen, dpoints);
        }

        public static void WDrawTick(
            this Graphics gr, Matrix transform,
            Pen pen, PointF wp, float ddx, float ddy)
        {
            wp = transform.TransformPoint(wp);
            gr.DrawLine(pen,
                wp.X - ddx, wp.Y - ddy,
                wp.X + ddx, wp.Y + ddy);
        }

        public static void WPlotPoint(
            this Graphics gr, Matrix transform,
            Brush brush, Pen pen, 
            PointF point, float drx, float dry)
        {
            point = transform.TransformPoint(point);
            RectangleF rect = new RectangleF(
                point.X - drx, point.Y - dry,
                2 * drx, 2 * dry);
            if (brush != null) gr.FillEllipse(brush, rect);
            if (pen != null) gr.DrawEllipse(pen, rect);
        }

        public static void WDrawString(
            this Graphics gr, Matrix transform,
            string text, Font font, Brush brush,
            PointF point, float ddx, float ddy, StringFormat sf)
        {
            point = transform.TransformPoint(point);
            point.X += ddx;
            point.Y += ddy;
            gr.DrawString(text, font, brush, point, sf);
        }
    }
}
