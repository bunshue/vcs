using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Drawing;
using System.Drawing.Drawing2D;
using System.Drawing.Text;
using System.Windows.Forms;

namespace vcs_ComboBox1
{
    public class ImageAndText
    {
        // Margins around owner drawn ComboBoxes.
        private const int MarginWidth = 4;
        private const int MarginHeight = 4;

        public Image Picture;
        public string Text;
        public Font Font;

        public ImageAndText(Image picture, string text, Font font)
        {
            Picture = picture;
            Text = text;
            Font = font;
        }

        // Set the size needed to display the image and text.
        private int Width, Height;
        private bool SizeCalculated = false;
        public void MeasureItem(MeasureItemEventArgs e)
        {
            // See if we've already calculated this.
            if (!SizeCalculated)
            {
                SizeCalculated = true;

                // See how much room the text needs.
                SizeF text_size = e.Graphics.MeasureString(Text, Font);

                // The height is the maximum of the image height and text height.
                Height = 2 * MarginHeight +
                    (int)Math.Max(Picture.Height, text_size.Height);

                // The width is the sum of the image and text widths.
                Width = (int)(4 * MarginWidth + Picture.Width + text_size.Width);
            }

            e.ItemWidth = Width;
            e.ItemHeight = Height;
        }

        // Draw the item.
        public void DrawItem(DrawItemEventArgs e)
        {
            // Clear the background appropriately.
            e.DrawBackground();

            // Draw the image.
            float hgt = e.Bounds.Height - 2 * MarginHeight;
            float scale = hgt / Picture.Height;
            float wid = Picture.Width * scale;
            RectangleF rect = new RectangleF(
                e.Bounds.X + MarginWidth,
                e.Bounds.Y + MarginHeight,
                wid, hgt);
            e.Graphics.InterpolationMode = InterpolationMode.HighQualityBilinear;
            e.Graphics.DrawImage(Picture, rect);

            // Draw the text.
            // If we're drawing on the control,
            // draw only the first line of text.
            string visible_text = Text;
            if (e.Bounds.Height < Picture.Height)
                visible_text = Text.Substring(0, Text.IndexOf('\n'));

            // Make a rectangle to hold the text.
            wid = e.Bounds.Width - rect.Right - 3 * MarginWidth;
            rect = new RectangleF(
                rect.Right + 2 * MarginWidth, rect.Y,
                wid, hgt);
            using (StringFormat sf = new StringFormat())
            {
                sf.Alignment = StringAlignment.Near;
                sf.LineAlignment = StringAlignment.Center;
                e.Graphics.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;
                e.Graphics.DrawString(visible_text, Font, Brushes.Black, rect, sf);
            }
            e.Graphics.DrawRectangle(Pens.Blue, Rectangle.Round(rect));

            // Draw the focus rectangle if appropriate.
            e.DrawFocusRectangle();
        }
    }
}
