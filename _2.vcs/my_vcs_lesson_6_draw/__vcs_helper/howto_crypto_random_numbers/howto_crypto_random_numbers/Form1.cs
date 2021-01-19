using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;
using System.Security.Cryptography;

namespace howto_crypto_random_numbers
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnGenerate_Click(object sender, EventArgs e)
        {
            using (Pen thin_pen = new Pen(Color.Black, 0))
            {
                lblRandom.Text = "";
                lblRng.Text = "";
                picGraphRandom.Image = null;
                picGraphRNG.Image = null;
                DateTime start_time, stop_time;
                TimeSpan elapsed;
                Cursor = Cursors.WaitCursor;
                Refresh();

                // Generate values with Random.
                int num_numbers = int.Parse(txtNumNumbers.Text);
                int min = int.Parse(txtMin.Text);
                int max = int.Parse(txtMax.Text);
                Random rand = new Random();
                int[] rand_numbers = new int[num_numbers];
                start_time = DateTime.Now;
                for (int i = 0; i < num_numbers; i++)
                    rand_numbers[i] = rand.Next(min, max);
                stop_time = DateTime.Now;
                elapsed = stop_time - start_time;
                lblRandom.Text = "Random (" + elapsed.TotalSeconds.ToString("0.00") + " sec)";

                // Display a histogram.
                thin_pen.Color = Color.LightBlue;
                DrawHistogram(picGraphRandom, Brushes.Blue, thin_pen, rand_numbers);

                // Generate values with RNGCryptoServiceProvider.
                start_time = DateTime.Now;
                for (int i = 0; i < num_numbers; i++)
                    rand_numbers[i] = RandomInteger(min, max);
                stop_time = DateTime.Now;
                elapsed = stop_time - start_time;
                lblRng.Text = "RNGCryptoServiceProvider (" + elapsed.TotalSeconds.ToString("0.00") + " sec)";

                // Display a histogram.
                thin_pen.Color = Color.LightGreen;
                DrawHistogram(picGraphRNG, Brushes.Green, thin_pen, rand_numbers);

                Cursor = Cursors.Default;
            }
        }

        // The random number provider.
        private RNGCryptoServiceProvider Rand = new RNGCryptoServiceProvider();

        // Return a random integer between a min and max value.
        private int RandomInteger(int min, int max)
        {
            uint scale = uint.MaxValue;
            while (scale == uint.MaxValue)
            {
                // Get four random bytes.
                byte[] four_bytes = new byte[4];
                Rand.GetBytes(four_bytes);

                // Convert that into an uint.
                scale = BitConverter.ToUInt32(four_bytes, 0);
            }

            // Add min to the scaled difference between max and min.
            return (int)(min + (max - min) * (scale / (double)uint.MaxValue));
        }

        // Display a histogram.
        private void DrawHistogram(PictureBox pic, Brush brush, Pen pen, int[] values)
        {
            // Count the values.
            int min = values.Min();
            int max = values.Max();
            int[] counts = new int[max - min + 1];
            for (int i = 0; i < values.Length; i++)
            {
                counts[values[i] - min]++;
            }
            int max_count = counts.Max();

            // Make a Bitmap.
            Bitmap bm = new Bitmap(pic.ClientSize.Width, pic.ClientSize.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.SmoothingMode = SmoothingMode.AntiAlias;

                // Scale to fit the data.
                RectangleF rect = new RectangleF(0, 0, counts.Length, max_count);
                PointF[] pts = 
                {
                    new PointF(0, pic.ClientSize.Height),
                    new PointF(pic.ClientSize.Width, pic.ClientSize.Height),
                    new PointF(0, 0),
                };
                gr.Transform = new Matrix(rect, pts);

                // Fill the histogram.
                for (int i = 0; i < counts.Length; i++)
                {
                    gr.FillRectangle(brush, i, 0, 1, counts[i]);
                }

                // Draw the histogram.
                if (counts.Length < 200)
                {
                    for (int i = 0; i < counts.Length; i++)
                    {
                        gr.DrawRectangle(pen, i, 0, 1, counts[i]);
                    }
                }
            }

            // Display the histogram.
            pic.Image = bm;
        }
    }
}
