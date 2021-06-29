using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Drawing;

namespace vcs_PictureCrop2
{
    public static class Extensions
    {
        public static void DrawRectangle(this Graphics gr, Pen pen, RectangleF rect)
        {
            gr.DrawRectangle(pen, rect.X, rect.Y, rect.Width, rect.Height);
        }

        public static void DrawBox(this Graphics gr,
            Brush brush, Pen pen, PointF center, float radius)
        {
            RectangleF rect = new RectangleF(
                center.X - radius,
                center.Y - radius,
                2 * radius, 2 * radius);
            gr.FillRectangle(brush, rect);
            gr.DrawRectangle(pen, rect);
        }
    }
}
