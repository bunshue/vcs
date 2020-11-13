using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Drawing;

namespace vcs_Clock5
{
    public static class Extensions
    {
        public static void DrawRectangle(this Graphics gr,
            Pen pen, RectangleF rect)
        {
            gr.DrawRectangle(pen, rect.X, rect.Y, rect.Width, rect.Height);
        }
    }
}
