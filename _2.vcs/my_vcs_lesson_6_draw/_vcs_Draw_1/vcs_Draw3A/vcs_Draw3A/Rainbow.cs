using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Drawing;
using System.Drawing.Drawing2D;

namespace vcs_Draw3A
{
    static class Rainbow
    {
        // Return a rainbow brush.
        // The calling code should dispose of the brush.
        public static LinearGradientBrush RainbowBrush(Point point1, Point point2)
        {
            LinearGradientBrush rainbow_brush =
                new LinearGradientBrush(point1, point2,
                    Color.Red, Color.Red);

            // Define the colors along the gradient.
            ColorBlend color_blend = new ColorBlend();
            color_blend.Colors = new Color[]
                { Color.Red, Color.Yellow, Color.Lime, Color.Aqua,
                  Color.Blue, Color.Fuchsia, Color.Red };
            color_blend.Positions = new float[] { 0, 1 / 6f, 2 / 6f, 3 / 6f, 4 / 6f, 5 / 6f, 1 };
            rainbow_brush.InterpolationColors = color_blend;

            return rainbow_brush;
        }

        // Map a color to a rainbow number between 0 and 1 on the
        // Red-Yellow-Lime-Aqua-Blue-Fuchsia-Red rainbow.
        public static float ColorToRainbowNumber(Color clr)
        {
            // See which color is weakest.
            int r = clr.R;
            int g = clr.G;
            int b = clr.B;
            if ((r <= g) && (r <= b))
            {
                // Red is weakest. It's mostly blue and green.
                g -= r;
                b -= r;
                if (g + b == 0) return 0;
                return (2 / 6f * g + 4 / 6f * b) / (g + b);
            }
            else if ((g <= r) && (g <= b))
            {
                // Green is weakest. It's mostly red and blue.
                r -= g;
                b -= g;
                if (r + b == 0) return 0;
                return (1f * r + 4 / 6f * b) / (r + b);
            }
            else
            {
                // Blue is weakest. It's mostly red and green.
                r -= b;
                g -= b;
                if (r + g == 0) return 0;
                return (0f * r + 2 / 6f * g) / (r + g);
            }
        }

        // Map a rainbow number between 0 and 1 to a color on the
        // Red-Yellow-Lime-Aqua-Blue-Fuchsia-Red rainbow.
        public static Color RainbowNumberToColor(float number)
        {
            byte r = 0, g = 0, b = 0;
            if (number < 1 / 6f)
            {
                // Mostly red with some green.
                r = 255;
                g = (byte)(r * (number - 0) / (2 / 6f - number));
            }
            else if (number < 2 / 6f)
            {
                // Mostly green with some red.
                g = 255;
                r = (byte)(g * (2 / 6f - number) / (number - 0));
            }
            else if (number < 3 / 6f)
            {
                // Mostly green with some blue.
                g = 255;
                b = (byte)(g * (2 / 6f - number) / (number - 4 / 6f));
            }
            else if (number < 4 / 6f)
            {
                // Mostly blue with some green.
                b = 255;
                g = (byte)(b * (number - 4 / 6f) / (2 / 6f - number));
            }
            else if (number < 5 / 6f)
            {
                // Mostly blue with some red.
                b = 255;
                r = (byte)(b * (4 / 6f - number) / (number - 1f));
            }
            else
            {
                // Mostly red with some blue.
                r = 255;
                b = (byte)(r * (number - 1f) / (4 / 6f - number));
            }
            return Color.FromArgb(r, g, b);
        }
    }
}
