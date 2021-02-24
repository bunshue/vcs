using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;

namespace vcs_ImageProcessing8
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
            string filename = @"C:\______test_files\picture1.jpg";
            pictureBox0.Image = Image.FromFile(filename);
            pictureBox1.Image = pictureBox0.Image.Clone() as Image;
        }

        // Display the original image.
        private void btnReset_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = pictureBox0.Image.Clone() as Image;
        }

        private int NUM_TRIALS = 5;

        // Invert the image without Lockbits.
        private void btnNoLockBits_Click(object sender, EventArgs e)
        {
            Bitmap bm = new Bitmap(pictureBox0.Image);
            Cursor = Cursors.WaitCursor;
            Stopwatch watch = new Stopwatch();
            watch.Start();

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
            pictureBox1.Image = bm;
            watch.Stop();
            Cursor = Cursors.Default;

            richTextBox1.Text += "經過時間 : " + watch.Elapsed.TotalSeconds.ToString("0.000000") + " 秒\n";
        }

        // Invert the image using Lockbits.
        private void btnLockBits_Click(object sender, EventArgs e)
        {
            const byte BYTE_255 = 255;
            Bitmap bm = new Bitmap(pictureBox0.Image);
            Cursor = Cursors.WaitCursor;
            Stopwatch watch = new Stopwatch();
            watch.Start();

            for (int trial = 0; trial < NUM_TRIALS; trial++)
            {
                // Make a Bitmap24 object.
                Bitmap32 bm32 = new Bitmap32(bm);

                // Lock the bitmap.
                bm32.LockBitmap();

                // Invert the pixels.
                byte red, green, blue, alpha;
                for (int y = 0; y < bm32.Height; y++)
                {
                    for (int x = 0; x < bm32.Width; x++)
                    {
                        bm32.GetPixel(x, y, out red, out green, out blue, out alpha);
                        red = (byte)(BYTE_255 - red);
                        green = (byte)(BYTE_255 - green);
                        blue = (byte)(BYTE_255 - blue);
                        bm32.SetPixel(x, y, red, green, blue, alpha);
                    }
                }

                // Unlock the bitmap.
                bm32.UnlockBitmap();
            }
            pictureBox1.Image = bm;

            watch.Stop();
            Cursor = Cursors.Default;

            richTextBox1.Text += "經過時間 : " + watch.Elapsed.TotalSeconds.ToString("0.000000") + " 秒\n";
        }

        private void btnQuarter_Click(object sender, EventArgs e)
        {
            Bitmap bm = new Bitmap(pictureBox0.Image);
            Cursor = Cursors.WaitCursor;
            Stopwatch watch = new Stopwatch();
            watch.Start();

            // Make a Bitmap24 object.
            Bitmap32 bm32 = new Bitmap32(bm);

            // Lock the bitmap.
            bm32.LockBitmap();

            // Invert the pixels.
            int xmid = bm32.Width / 2;
            int ymid = bm32.Height / 2;
            for (int y = 0; y < ymid; y++)
            {
                for (int x = 0; x < xmid; x++)
                {
                    bm32.SetGreen(x, y, 0);
                    bm32.SetBlue(x, y, 0);
                    bm32.SetAlpha(x, y, 220);
                }
            }
            for (int y = ymid; y < bm32.Height; y++)
            {
                for (int x = 0; x < xmid; x++)
                {
                    bm32.SetRed(x, y, 0);
                    bm32.SetGreen(x, y, 0);
                    bm32.SetAlpha(x, y, 220);
                }
            }
            for (int y = 0; y < ymid; y++)
            {
                for (int x = xmid; x < bm32.Width; x++)
                {
                    bm32.SetRed(x, y, 0);
                    bm32.SetBlue(x, y, 0);
                    bm32.SetAlpha(x, y, 220);
                }
            }
            byte red, green, blue, alpha;
            for (int y = ymid; y < bm32.Height; y++)
            {
                for (int x = xmid; x < bm32.Width; x++)
                {
                    red = (byte)(255 - bm32.GetRed(x, y));
                    green = (byte)(255 - bm32.GetGreen(x, y));
                    blue = (byte)(255 - bm32.GetBlue(x, y));
                    alpha = 220;
                    bm32.SetPixel(x, y, red, green, blue, alpha);
                }
            }

            // Unlock the bitmap.
            bm32.UnlockBitmap();

            // Make a new bitmap.
            Bitmap final_bm = new Bitmap(pictureBox0.Image);
            using (Graphics gr = Graphics.FromImage(final_bm))
            {
                // Draw an ellispe in the center.
                gr.Clear(Color.Black);
                gr.FillEllipse(Brushes.White,
                    new Rectangle((int)(bm.Width * 0.2), (int)(bm.Height * 0.2),
                        (int)(bm.Width * 0.6), (int)(bm.Height * 0.6)));

                // Copy the quartered bitmap onto this one.
                gr.DrawImage(bm, 0, 0);
            }

            // Display the result.
            pictureBox1.Image = final_bm;

            watch.Stop();
            Cursor = Cursors.Default;

            richTextBox1.Text += "經過時間 : " + watch.Elapsed.TotalSeconds.ToString("0.000000") + " 秒\n";
        }
    }
}
