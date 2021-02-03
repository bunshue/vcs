using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;

namespace howto_primes_fractal
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private const int Wid = 800;
        private const int Hgt = 800;
        private const int XOff = 150;
        private const int YOff = 200;
        private int[,] Hits = new int[Wid, Hgt];
        private Point CurrentPoint = new Point(0, 0);
        private long CurrentPrime = 1;

        // Start or stop.
        private bool Running = false;

        // Add points to the fractal.
        private int NumPoints = 0;
        private void DrawFractal()
        {
            const int points_per_loop = 10000;
            while (Running)
            {
                // Generate a bunch of points.
                for (int i = 0; i < points_per_loop; i++)
                {
                    // Find the next prime.
                    CurrentPrime = FindNextPrime(CurrentPrime);

                    // See which kind of prime it is.
                    switch (CurrentPrime % 5)
                    {
                        case 1:
                            CurrentPoint.Y--;
                            break;
                        case 2:
                            CurrentPoint.X++;
                            break;
                        case 3:
                            CurrentPoint.Y++;
                            break;
                        case 4:
                            CurrentPoint.X--;
                            break;
                    }

                    // Record the hit.
                    int ix = CurrentPoint.X + XOff;
                    int iy = CurrentPoint.Y + YOff;
                    if (ix >= 0 && iy >= 0 && ix < Wid && iy < Hgt)
                    {
                        Hits[ix, iy]++;
                    }
                }

                // Build the image.
                BuildImage();

                // Display the point count.
                NumPoints += points_per_loop;
                lblNumPoints.Text = NumPoints.ToString();
                lblPrime.Text = CurrentPrime.ToString();

                // Process button clicks if there were any.
                Application.DoEvents();
            }
        }

        // Find the next prime after this one.
        private long FindNextPrime(long value)
        {
            // Cheat a little for speed.
            //if (value == 1) return 2;
            //if (value == 2) return 3;
            for (long i = value + 2; ; i += 2)
            {
                if (IsPrime(i)) return i;
            }
        }

        // Return true if the value is prime.
        // For speed, asssume value > 2 and value is odd.
        private bool IsPrime(long value)
        {
            long stop_at = (long)Math.Sqrt(value);
            for (long factor = 3; factor <= stop_at; factor += 2)
            {
                if (value % factor == 0) return false;
            }
            return true;
        }

        // Build and display the image.
        private void BuildImage()
        {
            Bitmap bm = new Bitmap(Wid, Hgt);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                // Clear.
                gr.Clear(Color.Black);

                // Find the largest hit value.
                var max_query =
                    from int count in Hits
                    select count;
                float max = (float)max_query.Max();

                // Plot the hits.
                for (int x = 0; x < Wid; x++)
                    for (int y = 0; y < Hgt; y++)
                        if (Hits[x, y] > 0)
                            bm.SetPixel(x, y, MapRainbowColor(Hits[x, y], 1, max));

                // Draw the axes.
                gr.DrawLine(Pens.Blue, XOff, 0, XOff, Hgt);
                gr.DrawLine(Pens.Blue, 0, YOff, Wid, YOff);
            }

            // Display the result.
            pictureBox1.Image = bm;
        }

        // Map a value to a rainbow color.
        private Color MapRainbowColor(float value, float red_value, float blue_value)
        {
            // Convert into a value between 0 and 1023.
            int int_value = (int)(1023 * (value - red_value) / (blue_value - red_value));

            // Map different color bands.
            if (int_value < 256)
            {
                // Red to yellow. (255, 0, 0) to (255, 255, 0).
                return Color.FromArgb(255, int_value, 0);
            }
            else if (int_value < 512)
            {
                // Yellow to green. (255, 255, 0) to (0, 255, 0).
                int_value -= 256;
                return Color.FromArgb(255 - int_value, 255, 0);
            }
            else if (int_value < 768)
            {
                // Green to aqua. (0, 255, 0) to (0, 255, 255).
                int_value -= 512;
                return Color.FromArgb(0, 255, int_value);
            }
            else
            {
                // Aqua to blue. (0, 255, 255) to (0, 0, 255).
                int_value -= 768;
                return Color.FromArgb(0, 255 - int_value, 255);
            }
        }

        // Stop running.
        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            Running = false;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (button1.Text == "Start")
            {
                // Start.
                Running = true;
                button1.Text = "Stop";

                DrawFractal();

                // Clean up after we finish running.
                button1.Text = "Start";
            }
            else
            {
                // Stop.
                Running = false;
            }

        }        
    }
}
