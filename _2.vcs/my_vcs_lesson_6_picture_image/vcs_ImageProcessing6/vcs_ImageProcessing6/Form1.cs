using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;

namespace vcs_ImageProcessing6
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Display the initial image.
        private void Form1_Load(object sender, EventArgs e)
        {
            picVisible.Image = picHidden.Image.Clone() as Image;
        }

        // Display the original image.
        private void btnReset_Click(object sender, EventArgs e)
        {
            picVisible.Image = picHidden.Image.Clone() as Image;
            lblElapsed.Text = "";
        }

        private const int NUM_TRIALS = 5;

        // Invert the image without Lockbits.
        private void btnNoLockBits_Click(object sender, EventArgs e)
        {
            Cursor = Cursors.WaitCursor;
            Stopwatch watch = new Stopwatch();
            watch.Start();

            Bitmap bm = new Bitmap(picHidden.Image);
            for (int trial = 0; trial < NUM_TRIALS; trial++)
            {
                for (int Y = 0; Y < bm.Height; Y++)
                {
                    for (int X = 0; X < bm.Width; X++)
                    {
                        Color clr = bm.GetPixel(X, Y);
                        clr = Color.FromArgb(
                            255 - clr.R,
                            255 - clr.G,
                            255 - clr.B);
                        bm.SetPixel(X, Y, clr);
                    }
                }
            }
            picVisible.Image = bm;
            watch.Stop();
            Cursor = Cursors.Default;
            lblElapsed.Text = watch.Elapsed.TotalSeconds.ToString("0.000000") + " seconds";
        }

        // Invert the image using Lockbits.
        private void btnLockBits_Click(object sender, EventArgs e)
        {
            const byte BYTE_255 = 255;
            Bitmap bm = new Bitmap(picHidden.Image);
            Cursor = Cursors.WaitCursor;
            Stopwatch watch = new Stopwatch();
            watch.Start();
            
            for (int trial = 0; trial < NUM_TRIALS; trial++)
            {
                // Make a Bitmap24 object.
                Bitmap24 bm24 = new Bitmap24(bm);

                // Lock the bitmap.
                bm24.LockBitmap();

                // Invert the pixels.
                byte red, green, blue;
                for (int y = 0; y < bm24.Height; y++)
                {
                    for (int x = 0; x < bm24.Width; x++)
                    {
                        bm24.GetPixel(x, y, out red, out green, out blue);
                        red = (byte)(BYTE_255 - red);
                        green = (byte)(BYTE_255 - green);
                        blue = (byte)(BYTE_255 - blue);
                        bm24.SetPixel(x, y, red, green, blue);
                    }
                }

                /*
                //same but slower
                // Invert the pixels.
                for (int i = 0; i < bm.Height * bm24.RowSizeBytes; i++)
                {
                    // bm24.ImageBytes[i] = Convert.ToByte(BYTE_255 - bm24.ImageBytes[i]);
                    bm24.ImageBytes[i] = (byte)(BYTE_255 - bm24.ImageBytes[i]);
                }
                */

                // Unlock the bitmap.
                bm24.UnlockBitmap();
            }
            picVisible.Image = bm;

            watch.Stop();
            Cursor = Cursors.Default;
            lblElapsed.Text = watch.Elapsed.TotalSeconds.ToString("0.000000") + " seconds";
        }

        private void btnQuarter_Click(object sender, EventArgs e)
        {
            Bitmap bm = new Bitmap(picHidden.Image);
            Cursor = Cursors.WaitCursor;
            Stopwatch watch = new Stopwatch();
            watch.Start();

            // Make a Bitmap24 object.
            Bitmap24 bm24 = new Bitmap24(bm);

            // Lock the bitmap.
            bm24.LockBitmap();

            // Invert the pixels.
            int xmid = bm24.Width / 2;
            int ymid = bm24.Height / 2;
            for (int y = 0; y < ymid; y++)
            {
                for (int x = 0; x < xmid; x++)
                {
                    bm24.SetGreen(x, y, 0);
                    bm24.SetBlue(x, y, 0);
                }
            }
            for (int y = ymid; y < bm24.Height; y++)
            {
                for (int x = 0; x < xmid; x++)
                {
                    bm24.SetRed(x, y, 0);
                    bm24.SetGreen(x, y, 0);
                }
            }
            for (int y = 0; y < ymid; y++)
            {
                for (int x = xmid; x < bm24.Width; x++)
                {
                    bm24.SetRed(x, y, 0);
                    bm24.SetBlue(x, y, 0);
                }
            }
            byte red, green, blue;
            for (int y = ymid; y < bm24.Height; y++)
            {
                for (int x = xmid; x < bm24.Width; x++)
                {
                    red = (byte)(255 - bm24.GetRed(x, y));
                    green = (byte)(255 - bm24.GetGreen(x, y));
                    blue = (byte)(255 - bm24.GetBlue(x, y));
                    bm24.SetPixel(x, y, red, green, blue);
                }
            }

            // Unlock the bitmap.
            bm24.UnlockBitmap();
            picVisible.Image = bm;

            watch.Stop();
            Cursor = Cursors.Default;
            lblElapsed.Text =
                watch.Elapsed.TotalSeconds.ToString("0.000000") +
                " seconds";
        }
    }
}
