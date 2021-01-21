using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Drawing;
using System.Drawing.Drawing2D;

namespace howto_improved_hex_montage
{
    public static class Hex
    {
        // Return the width of a hexagon.
        public static float HexWidth(float height)
        {
            return (float)(4 * (height / 2 / Math.Sqrt(3)));
        }

        // Return the row and column of the hexagon at this point.
        public static void PointToHex(float x, float y, float height,
            out int row, out int col)
        {
            // Find the test rectangle containing the point.
            float width = HexWidth(height);
            col = (int)(x / (width * 0.75f));

            if (col % 2 == 0)
                row = (int)(y / height);
            else
                row = (int)((y - height / 2) / height);

            // Find the test area.
            float testx = col * width * 0.75f;
            float testy = row * height;
            if (col % 2 == 1) testy += height / 2;

            // See if the point is above or
            // below the test hexagon on the left.
            bool is_above = false, is_below = false;
            float dx = x - testx;
            if (dx < width / 4)
            {
                float dy = y - (testy + height / 2);
                if (dx < 0.001)
                {
                    // The point is on the left edge of the test rectangle.
                    if (dy < 0) is_above = true;
                    if (dy > 0) is_below = true;
                }
                else if (dy < 0)
                {
                    // See if the point is above the test hexagon.
                    if (-dy / dx > Math.Sqrt(3)) is_above = true;
                }
                else
                {
                    // See if the point is below the test hexagon.
                    if (dy / dx > Math.Sqrt(3)) is_below = true;
                }
            }

            // Adjust the row and column if necessary.
            if (is_above)
            {
                if (col % 2 == 0) row--;
                col--;
            }
            else if (is_below)
            {
                if (col % 2 == 1) row++;
                col--;
            }
        }

        // Return the points that define the indicated hexagon.
        public static PointF[] HexToPoints(float height,
            float row, float col, float xmin, float ymin)
        {
            // Start with the leftmost corner of the upper left hexagon.
            float width = HexWidth(height);
            float y = height / 2;
            float x = 0;

            // Move down the required number of rows.
            y += row * height;

            // If the column is odd, move down half a hex more.
            if (col % 2 == 1) y += height / 2;

            // Move over for the column number.
            x += col * (width * 0.75f);

            // Generate the points.
            return new PointF[]
                {
                    new PointF(xmin + x, ymin + y),
                    new PointF(xmin + x + width * 0.25f, ymin + y - height / 2),
                    new PointF(xmin + x + width * 0.75f, ymin + y - height / 2),
                    new PointF(xmin + x + width, ymin + y),
                    new PointF(xmin + x + width * 0.75f, ymin + y + height / 2),
                    new PointF(xmin + x + width * 0.25f, ymin + y + height / 2),
                };
        }

        // Draw a hexagonal grid for the indicated area.
        // (You might be able to draw the hexagons without
        // drawing any duplicate edges, but this is a lot easier.)
        public static void DrawHexGrid(Graphics gr, Pen pen,
            float xmin, float xmax, float ymin, float ymax,
            float height)
        {
            // Loop until a hexagon won't fit.
            for (int row = 0; ; row++)
            {
                // Get the points for the row's first hexagon.
                PointF[] points = Hex.HexToPoints(
                    height, row, 0, xmin, ymin);

                // If it doesn't fit, we're done.
                if (points[4].Y > ymax) break;

                // Draw the row.
                for (int col = 0; ; col++)
                {
                    // Get the points for the row's next hexagon.
                    points = Hex.HexToPoints(height, row, col, xmin, xmin);

                    // If it doesn't fit horizontally,
                    // we're done with this row.
                    if (points[3].X > xmax) break;

                    // If it fits vertically, draw it.
                    if (points[4].Y <= ymax)
                    {
                        gr.DrawPolygon(pen, points);
                    }
                }
            }
        }

        // Draw an image so it fills the polygon.
        public static void DrawImageInPolygon(Graphics gr,
            PointF[] points, Image image)
        {
            // Get the polygon's bounds and center.
            float xmin, xmax, ymin, ymax;
            GetPolygonBounds(points, out xmin, out xmax, out ymin, out ymax);
            float wid = xmax - xmin;
            float hgt = ymax - ymin;
            float cx = (xmin + xmax) / 2f;
            float cy = (ymin + ymax) / 2f;

            // Calculate the scale needed to make
            // the image fill the polygon's bounds.
            float xscale = wid / image.Width;
            float yscale = hgt / image.Height;
            float scale = Math.Max(xscale, yscale);

            // Calculate the image's scaled size.
            float width = image.Width * scale;
            float height = image.Height * scale;
            float rx = width / 2f;
            float ry = height / 2f;

            // Find the source rectangle and destination points.
            RectangleF src_rect = new RectangleF(0, 0,
                image.Width, image.Height);
            PointF[] dest_points =
            {
                new PointF(cx - rx,  cy - ry),
                new PointF(cx + rx,  cy - ry),
                new PointF(cx - rx,  cy + ry),
            };

            // Clip the drawing area to the polygon and draw the image.
            GraphicsPath path = new GraphicsPath();
            path.AddPolygon(points);
            GraphicsState state = gr.Save();
            gr.SetClip(path);   // Comment out to not clip.
            gr.DrawImage(image, dest_points, src_rect, GraphicsUnit.Pixel);
            gr.Restore(state);
        }

        // Return a polygon's bounds.
        public static void GetPolygonBounds(PointF[] points,
            out float xmin, out float xmax, out float ymin, out float ymax)
        {
            xmin = points[0].X;
            xmax = xmin;
            ymin = points[0].Y;
            ymax = ymin;
            foreach (PointF point in points)
            {
                if (xmin > point.X) xmin = point.X;
                if (xmax < point.X) xmax = point.X;
                if (ymin > point.Y) ymin = point.Y;
                if (ymax < point.Y) ymax = point.Y;
            }
        }
    }
}
