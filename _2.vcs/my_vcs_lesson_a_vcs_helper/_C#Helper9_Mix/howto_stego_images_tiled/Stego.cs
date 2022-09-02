using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Drawing;

namespace howto_stego_images_tiled
{
    class Stego
    {
        // Hide bm_hidden inside bm_visible and return the result.
        public static Bitmap HideImage(Bitmap bm_visible, Bitmap bm_hidden, int hidden_bits)
        {
            int shift = (8 - hidden_bits);
            int visible_mask = 0xFF << hidden_bits;
            int hidden_mask = 0xFF >> shift;
            Bitmap bm_combined = new Bitmap(bm_visible.Width, bm_visible.Height);
            for (int x = 0; x < bm_visible.Width; x++)
            {
                for (int y = 0; y < bm_visible.Height; y++)
                {
                    Color clr_visible = bm_visible.GetPixel(x, y);
                    Color clr_hidden = bm_hidden.GetPixel(x, y);
                    int r = (clr_visible.R & visible_mask) + ((clr_hidden.R >> shift) & hidden_mask);
                    int g = (clr_visible.G & visible_mask) + ((clr_hidden.G >> shift) & hidden_mask);
                    int b = (clr_visible.B & visible_mask) + ((clr_hidden.B >> shift) & hidden_mask);
                    bm_combined.SetPixel(x, y, Color.FromArgb(255, r, g, b));
                }
            }
            return bm_combined;
        }

        // Recover a hidden image.
        public static Bitmap RecoverImage(Bitmap bm_combined, int hidden_bits)
        {
            int shift = (8 - hidden_bits);
            int hidden_mask = 0xFF >> shift;
            Bitmap bm_hidden = new Bitmap(bm_combined.Width, bm_combined.Height);
            for (int x = 0; x < bm_combined.Width; x++)
            {
                for (int y = 0; y < bm_combined.Height; y++)
                {
                    Color clr_combined = bm_combined.GetPixel(x, y);
                    int r = (clr_combined.R & hidden_mask) << shift;
                    int g = (clr_combined.G & hidden_mask) << shift;
                    int b = (clr_combined.B & hidden_mask) << shift;
                    bm_hidden.SetPixel(x, y, Color.FromArgb(255, r, g, b));
                }
            }
            return bm_hidden;
        }

        // Hide the four hidden images inside bm_visible and return the result.
        public static Bitmap HideTiledImages(Bitmap bm_visible,
            Bitmap hidden1, Bitmap hidden2, Bitmap hidden3,
            Bitmap hidden4, int hidden_bits)
        {
            // Tile the hidden images onto a
            // bitmap sized to fit the visible image.
            Bitmap bm = (Bitmap)bm_visible.Clone();
            int wid = bm.Width / 2;
            int hgt = bm.Height / 2;

            using (Graphics gr = Graphics.FromImage(bm))
            {
                Rectangle rect = new Rectangle(0, 0, wid, hgt);
                gr.DrawImage(hidden1, rect);

                rect.X += wid;
                gr.DrawImage(hidden2, rect);

                rect.X = 0;
                rect.Y += hgt;
                gr.DrawImage(hidden3, rect);

                rect.X += wid;
                gr.DrawImage(hidden4, rect);
            }

            // Hide the combined image in the main image.
            return HideImage(bm_visible, bm, hidden_bits);
        }

        // Recover four hidden images.
        public static void RecoverTiledImages(Bitmap bm_combined,
            out Bitmap hidden1, out Bitmap hidden2,
            out Bitmap hidden3, out Bitmap hidden4, int hidden_bits)
        {
            // Recover the tiled image.
            Bitmap bm = RecoverImage(bm_combined, hidden_bits);

            // Pull out the pieces.
            int wid = bm_combined.Width / 2;
            int hgt = bm_combined.Height / 2;
            Rectangle dest = new Rectangle(0, 0, wid, hgt);

            Rectangle source = new Rectangle(0, 0, wid, hgt);
            hidden1 = new Bitmap(wid, hgt);
            using (Graphics gr = Graphics.FromImage(hidden1))
            {
                gr.DrawImage(bm, dest, source, GraphicsUnit.Pixel);
            }

            source.X += wid;
            hidden2 = new Bitmap(wid, hgt);
            using (Graphics gr = Graphics.FromImage(hidden2))
            {
                gr.DrawImage(bm, dest, source, GraphicsUnit.Pixel);
            }

            source.X = 0;
            source.Y += hgt;
            hidden3 = new Bitmap(wid, hgt);
            using (Graphics gr = Graphics.FromImage(hidden3))
            {
                gr.DrawImage(bm, dest, source, GraphicsUnit.Pixel);
            }

            source.X += wid;
            hidden4 = new Bitmap(wid, hgt);
            using (Graphics gr = Graphics.FromImage(hidden4))
            {
                gr.DrawImage(bm, dest, source, GraphicsUnit.Pixel);
            }
        }
    }
}
