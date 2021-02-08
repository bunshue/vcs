using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Drawing;
using System.Drawing.Drawing2D;

namespace vcs_Draw_Pie
{
    public static class DrawingExtensions
    {
        // Add a pie slice to a GraphicsPath and take a RectangleF as a parameter.
        public static void AddPie(this GraphicsPath path, RectangleF rect, float start_angle, float sweep_angle)
        {
            path.AddPie(rect.X, rect.Y,
                rect.Width, rect.Height,
                start_angle, sweep_angle);
        }

        // Fill a pie slice and take a RectangleF as a parameter.
        public static void FillPie(this Graphics gr, Brush brush, RectangleF rect, float start_angle, float sweep_angle)
        {
            gr.FillPie(brush, rect.X, rect.Y,
                rect.Width, rect.Height,
                start_angle, sweep_angle);
        }
    }
}
