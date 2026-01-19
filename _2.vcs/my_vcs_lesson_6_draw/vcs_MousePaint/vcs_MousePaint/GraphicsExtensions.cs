using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Drawing;

namespace vcs_MousePaint
{
    public static class GraphicsExtensions
    {
        // Draw a two-color dashed rectangle.
        public static void DrawRectangle(this Graphics gr,
            Rectangle rect, Color color1, Color color2,
            float thickness, float offset, float[] dash_pattern)
        {
            using (Pen pen = new Pen(color1, thickness))
            {
                gr.DrawRectangle(pen, rect);

                pen.DashPattern = dash_pattern;
                pen.DashOffset = offset;
                pen.Color = color2;
                gr.DrawRectangle(pen, rect);
            }
        }
    }
}
