using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Drawing;

namespace vcs_PictureMontage
{
    public class ImageInfo
    {
        // The image we will draw.
        public Bitmap Picture = null;

        // The source and destination for drawing.
        public Rectangle SourceRect, DestRect;

        // Constructor. Open the image file.
        public ImageInfo(string filename)
        {
            using (Bitmap temp = new Bitmap(filename))
            {
                Picture = (Bitmap)temp.Clone();
                SourceRect = new Rectangle(0, 0, Picture.Width, Picture.Height);
                DestRect = new Rectangle(10, 10,
                    Picture.Width, Picture.Height);
            }
        }

        // Draw the image.
        private const int half_gap = 4;
        private const int gap = half_gap * 2;
        public void Draw(Graphics gr, bool with_border)
        {
            gr.DrawImage(Picture, DestRect, SourceRect, GraphicsUnit.Pixel);

            if (with_border)
            {
                using (Pen pen = new Pen(Color.White, 4))
                {
                    Rectangle rect = DestRect;
                    if (rect.Width < 0)
                    {
                        rect.X += rect.Width;
                        rect.Width = -rect.Width;
                    }
                    if (rect.Height < 0)
                    {
                        rect.Y += rect.Height;
                        rect.Height = -rect.Height;
                    }

                    gr.DrawRectangle(pen, rect);

                    pen.Color = Color.Black;
                    pen.CompoundArray = new float[] { 0.0f, 0.25f, 0.75f, 1.0f };
                    gr.DrawRectangle(pen, rect);
                }
                foreach (Rectangle rect in CornerRects())
                {
                    gr.FillRectangle(Brushes.White, rect);
                    gr.DrawRectangle(Pens.Black, rect);
                }
            }
        }

        // Return an array representing the picture's
        // corners in order NW, NE, SW, SE.
        private Rectangle[] CornerRects()
        {
            return new Rectangle[]
            {
                new Rectangle(DestRect.Left - half_gap, DestRect.Top - half_gap, gap, gap),
                new Rectangle(DestRect.Right - half_gap, DestRect.Top - half_gap, gap, gap),
                new Rectangle(DestRect.Left - half_gap, DestRect.Bottom - half_gap, gap, gap),
                new Rectangle(DestRect.Right - half_gap, DestRect.Bottom - half_gap, gap, gap),
            };
        }

        // Return a value indicating whether the position is over the image.
        public enum HitTypes
        {
            None,
            NwCorner,
            NeCorner,
            SwCorner,
            SeCorner,
            Body,
        }
        public HitTypes HitType(Point point)
        {
            Rectangle[] rects = CornerRects();
            if (rects[0].Contains(point)) return HitTypes.NwCorner;
            if (rects[1].Contains(point)) return HitTypes.NeCorner;
            if (rects[2].Contains(point)) return HitTypes.SwCorner;
            if (rects[3].Contains(point)) return HitTypes.SeCorner;
            if (DestRect.Contains(point)) return HitTypes.Body;
            return HitTypes.None;
        }
    }
}
