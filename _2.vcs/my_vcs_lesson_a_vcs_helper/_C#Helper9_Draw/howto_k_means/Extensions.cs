using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Drawing;

namespace howto_k_means
{
    public static class Extensions
    {
        private static Random Rand = new Random();

        public static void DrawPoints(this Graphics gr,
            List<PointF> points, Brush brush, Pen pen, float radius)
        {
            if (points == null) return;
            foreach (PointF point in points)
                gr.DrawPoint(point, brush, pen, radius);
        }

        public static void DrawRectangle(this Graphics gr,
            Pen pen, RectangleF rect)
        {
            gr.DrawRectangle(pen,
                rect.X, rect.Y, rect.Width, rect.Height);
        }
        public static void DrawRect(this Graphics gr, PointF point,
            Brush brush, Pen pen, float radius)
        {
            RectangleF rect = new RectangleF(
                point.X - radius, point.Y - radius,
                2 * radius, 2 * radius);
            gr.FillRectangle(brush, rect);
            gr.DrawRectangle(pen, rect);
        }
        public static void DrawPoint(this Graphics gr, PointF point,
            Brush brush, Pen pen, float radius)
        {
            RectangleF rect = new RectangleF(
                point.X - radius, point.Y - radius,
                2 * radius, 2 * radius);
            gr.FillEllipse(brush, rect);
            gr.DrawEllipse(pen, rect);
        }
        public static void DrawCross(this Graphics gr,
            Pen pen, PointF point, float radius)
        {
            gr.DrawLine(pen, point.X - radius, point.Y, point.X + radius, point.Y);
            gr.DrawLine(pen, point.X, point.Y - radius, point.X, point.Y + radius);
        }
        public static void DrawCross(this Graphics gr,
            Color outer_color, Color inner_color, PointF point, float radius)
        {
            using (Pen pen = new Pen(outer_color, 3))
            {
                gr.DrawLine(pen, point.X - radius - 1, point.Y, point.X + radius + 1, point.Y);
                gr.DrawLine(pen, point.X, point.Y - radius - 1, point.X, point.Y + radius + 1);
            }
            using (Pen pen = new Pen(inner_color, 1))
            {
                gr.DrawLine(pen, point.X - radius, point.Y, point.X + radius, point.Y);
                gr.DrawLine(pen, point.X, point.Y - radius, point.X, point.Y + radius);
            }
        }

        // Pick a random item from the list.
        public static T Random<T>(List<T> items)
        {
            return items[Rand.Next(items.Count)];
        }

        // Randomize an array.
        public static void Randomize<T>(this T[] items)
        {
            // For each spot in the array, pick
            // a random item to swap into that spot.
            for (int i = 0; i < items.Length - 1; i++)
            {
                int j = Rand.Next(i, items.Length);
                T temp = items[i];
                items[i] = items[j];
                items[j] = temp;
            }
        }

        // Randomize a list.
        public static void Randomize<T>(this List<T> items)
        {
            // Convert into an array.
            T[] item_array = items.ToArray();

            // Randomize.
            item_array.Randomize();

            // Copy the items back into the list.
            items.Clear();
            items.AddRange(item_array);
        }
    }
}
