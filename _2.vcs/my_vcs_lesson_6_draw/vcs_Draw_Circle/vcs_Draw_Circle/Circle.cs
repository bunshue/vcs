using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Drawing;
using System.Diagnostics;

namespace vcs_Draw_Circle
{
    // Represents a circle.
    class Circle
    {
        public PointF Center;
        public float Radius;
        public Circle()
            : this(0, 0, 0)
        {
        }
        public Circle(float new_x, float new_y, float new_radius)
        {
            Center = new PointF(new_x, new_y);
            Radius = Math.Abs(new_radius);
            Debug.Assert((Radius > 0.000001) && (Radius < 1000),
                "Cannot create a circle with radius " + Radius + ".");
        }

        // Return the circle's bounds.
        public RectangleF GetBounds()
        {
            return new RectangleF(
                Center.X - Radius, Center.Y - Radius,
                2 * Radius, 2 * Radius);
        }

        // Draw the circle.
        public void Draw(Graphics gr, Pen pen)
        {
            if (Radius > 0) gr.DrawEllipse(pen, GetBounds());
        }
        public void Draw(Graphics gr, Brush brush)
        {
            if (Radius > 0) gr.FillEllipse(brush, GetBounds());
        }
        public void Draw(Graphics gr, Brush brush, Pen pen)
        {
            Draw(gr, brush);
            Draw(gr, pen);
        }

        // Return a textual representation.
        public override string ToString()
        {
            return String.Format("({0}, {1}), {2}", Center.X, Center.Y, Radius);
        }
    }
}
