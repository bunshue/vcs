using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Text;

namespace howto_outline_graphics
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Create some sample text.
        private void Form1_Load(object sender, EventArgs e)
        {
            picGraphics.Image = Properties.Resources.Image;
            picGraphics.Refresh();
        }

        // Draw an outline.
        private void btnGo_Click(object sender, EventArgs e)
        {
            Cursor = Cursors.WaitCursor;
            picGraphics.Image = Properties.Resources.Image;
            picGraphics.Refresh();

            // Get the parameters.
            int min_radius = int.Parse(txtMinRadius.Text);
            int max_radius = int.Parse(txtMaxRadius.Text);

            // Get the outline image.
            Bitmap outline_bm = MakeOutline(Properties.Resources.Mask,
                min_radius, max_radius);
            
            // Combine the original image with the outline.
            Bitmap new_bm = (Bitmap)Properties.Resources.Image.Clone();
            using (Graphics gr = Graphics.FromImage(new_bm))
            {
                Rectangle rect = new Rectangle(0, 0, new_bm.Width, new_bm.Height);
                gr.DrawImageUnscaledAndClipped(outline_bm, rect);
            }

            picGraphics.Image = new_bm;
            picGraphics.Refresh();

            Cursor = Cursors.Default;
        }

        // Make an outline image.
        private Bitmap MakeOutline(Bitmap mask, int min_radius, int max_radius)
        {
            Bitmap32 mask_bm32 = new Bitmap32(mask);
            mask_bm32.LockBitmap();

            // Make the result bitmap.
            Bitmap new_bm = new Bitmap(mask.Width, mask.Height);
            using (Graphics gr = Graphics.FromImage(new_bm))
            {
                gr.Clear(Color.Transparent);
            }
            Bitmap32 new_bm32 = new Bitmap32(new_bm);
            new_bm32.LockBitmap();

            for (int x = 0; x < mask_bm32.Width; x++)
            {
                for (int y = 0; y < mask_bm32.Height; y++)
                {
                    float dist = DistToNonWhite(mask_bm32, x, y, max_radius);
                    if ((dist > min_radius) && (dist < max_radius))
                    {
                        byte alpha = 255;
                        if (dist - min_radius < 1)
                            alpha = (byte)(255 * (dist - min_radius));
                        else if (max_radius - dist < 1)
                            alpha = (byte)(255 * (max_radius - dist));

                        new_bm32.SetPixel(x, y, 255, 0, 0, alpha);
                    }
                }
            }

            mask_bm32.UnlockBitmap();
            new_bm32.UnlockBitmap();
            return new_bm;
        }

        // Return the distance to the nearest non-white pixel within the radius.
        private float DistToNonWhite(Bitmap32 bm32, int x, int y, int radius)
        {
            int minx = Math.Max(x - radius, 0);
            int maxx = Math.Min(x + radius, bm32.Width - 1);
            int miny = Math.Max(y - radius, 0);
            int maxy = Math.Min(y + radius, bm32.Height - 1);
            int dist2 = radius * radius + 1;

            for (int tx = minx; tx < maxx; tx++)
            {
                for (int ty = miny; ty <= maxy; ty++)
                {
                    byte r, g, b, a;
                    bm32.GetPixel(tx, ty, out r, out g, out b, out a);

                    if ((r < 200) || (g < 200) || (b < 200))
                    {
                        int dx = tx - x;
                        int dy = ty - y;
                        int test_dist2 = dx * dx + dy * dy;
                        if (test_dist2 < dist2) dist2 = test_dist2;
                    }
                }
            }

            return (float)Math.Sqrt(dist2);
        }





    }
}
