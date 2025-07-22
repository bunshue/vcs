using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;   //for Stopwatch

namespace vcs_ImageProcessing6b
{
    public partial class Form1 : Form
    {
        string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
        Stopwatch sw = new Stopwatch();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox0.Image = Image.FromFile(filename);
            pictureBox1.Image = Image.FromFile(filename);
        }

        private void btnReset_Click(object sender, EventArgs e)
        {
            pictureBox0.Image = Image.FromFile(filename);
            pictureBox1.Image = Image.FromFile(filename);
        }

        private const int NUM_TRIALS = 5;

        // Invert the image without Lockbits.
        private void btnNoLockBits_Click(object sender, EventArgs e)
        {
            const byte BYTE_255 = 255;
            Cursor = Cursors.WaitCursor;

            sw.Reset();
            sw.Start();

            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式

            for (int trial = 0; trial < NUM_TRIALS; trial++)
            {
                // Invert the pixels.
                byte red, green, blue;
                for (int y = 0; y < bitmap1.Height; y++)
                {
                    for (int x = 0; x < bitmap1.Width; x++)
                    {
                        Color clr = bitmap1.GetPixel(x, y);
                        red = (byte)(BYTE_255 - clr.R);
                        green = (byte)(BYTE_255 - clr.G);
                        blue = (byte)(BYTE_255 - clr.B);
                        clr = Color.FromArgb(
                            255 - clr.R,
                            255 - clr.G,
                            255 - clr.B);

                        bitmap1.SetPixel(x, y, Color.FromArgb(red, green, blue));
                    }
                }
            }
            pictureBox1.Image = bitmap1;
            Cursor = Cursors.Default;
            sw.Stop();
            richTextBox1.Text += "耗時 : " + string.Format("{0,10}", sw.ElapsedMilliseconds.ToString()) + "\tmsec\n";

            richTextBox1.Text += "經過時間 : " + sw.Elapsed.TotalSeconds.ToString("0.000000") + " 秒\n";
        }

        // Invert the image using Lockbits.
        private void btnLockBits_Click(object sender, EventArgs e)
        {
            const byte BYTE_255 = 255;

            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式

            Cursor = Cursors.WaitCursor;

            sw.Reset();
            sw.Start();

            for (int trial = 0; trial < NUM_TRIALS; trial++)
            {
                // Make a Bitmap32 object.
                Bitmap32 bm32 = new Bitmap32(bitmap1);

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

                /*
                //same but slower
                // Invert the pixels.
                for (int i = 0; i < bm.Height * bm32.RowSizeBytes; i++)
                {
                    // bm32.ImageBytes[i] = Convert.ToByte(BYTE_255 - bm32.ImageBytes[i]);
                    bm32.ImageBytes[i] = (byte)(BYTE_255 - bm32.ImageBytes[i]);
                }
                */

                // Unlock the bitmap.
                bm32.UnlockBitmap();
            }
            pictureBox1.Image = bitmap1;

            Cursor = Cursors.Default;
            sw.Stop();
            richTextBox1.Text += "耗時 : " + string.Format("{0,10}", sw.ElapsedMilliseconds.ToString()) + "\tmsec\n";

            richTextBox1.Text += "經過時間 : " + sw.Elapsed.TotalSeconds.ToString("0.000000") + " 秒\n";
        }

        private void btnQuarter_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式

            Cursor = Cursors.WaitCursor;

            sw.Reset();
            sw.Start();

            // Make a Bitmap32 object.
            Bitmap32 bm32 = new Bitmap32(bitmap1);

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
pictureBox1.Image = bitmap1;
Cursor = Cursors.Default;

            /*
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
            */
            sw.Stop();
            Cursor = Cursors.Default;

            richTextBox1.Text += "耗時 : " + string.Format("{0,10}", sw.ElapsedMilliseconds.ToString()) + "\tmsec\n";
      
            richTextBox1.Text += "經過時間 : " + sw.Elapsed.TotalSeconds.ToString("0.000000") + " 秒\n";
        }
    }
}
