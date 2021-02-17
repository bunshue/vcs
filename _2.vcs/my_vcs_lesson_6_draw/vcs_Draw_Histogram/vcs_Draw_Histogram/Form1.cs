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

namespace vcs_Draw_Histogram
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        // Display a histogram.
        private void DrawHistogram(PictureBox pic, Brush brush, Pen pen, int[] values)
        {
            // Count the values.
            int min = values.Min();
            int max = values.Max();
            int[] counts = new int[max - min + 1];
            richTextBox1.Text += "counts = " + counts.Length.ToString() + "\n";
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

                int kk = 0;
                // Fill the histogram.
                for (int i = 0; i < counts.Length; i++)
                {
                    gr.FillRectangle(brush, i, 0, 1, counts[i]);
                    kk++;

                }
                richTextBox1.Text += "draw " + kk.ToString() + " fill rectangles\n";

                // Draw the histogram.
                if (counts.Length < 200)
                {
                    kk = 0;
                    for (int i = 0; i < counts.Length; i++)
                    {
                        gr.DrawRectangle(pen, i, 0, 1, counts[i]);
                        kk++;
                    }
                    richTextBox1.Text += "draw " + kk.ToString() + " empty rectangles\n";
                }
            }

            // Display the histogram.
            pic.Image = bm;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = null;
            Refresh();

            // Generate values with Random.
            int num_numbers;
            int min;
            int max;

            num_numbers = 1000;
            min = 1;
            max = 100;

            richTextBox1.Text += "num_numbers = " + num_numbers.ToString() + "\n";
            richTextBox1.Text += "min = " + min.ToString() + "\n";
            richTextBox1.Text += "max = " + max.ToString() + "\n";

            Random rand = new Random();
            int[] numbers = new int[num_numbers];
            for (int i = 0; i < num_numbers; i++)
                numbers[i] = rand.Next(min, max);

            // Display a histogram.
            Pen thin_pen = new Pen(Color.Black, 0);
            thin_pen.Color = Color.LightBlue;
            DrawHistogram(pictureBox1, Brushes.Blue, thin_pen, numbers);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = null;
            Refresh();

            // Generate values with Random.
            int num_numbers;
            int min;
            int max;

            num_numbers = 100;
            min = 1;
            max = 100;

            richTextBox1.Text += "num_numbers = " + num_numbers.ToString() + "\n";
            richTextBox1.Text += "min = " + min.ToString() + "\n";
            richTextBox1.Text += "max = " + max.ToString() + "\n";

            int mean = (min + max) / 2;
            int amp = (max - min) / 2;

            //int[] numbers = new int[num_numbers];
            //for (int i = 0; i < num_numbers; i++)
            {
                //numbers[i] = (int)Math.Sin(i * 2 * Math.PI/1000);
                //numbers[i] = i;
            }

            Random rand = new Random();
            int[] numbers = new int[num_numbers];
            for (int i = 0; i < num_numbers; i++)
            {
                numbers[i] = rand.Next(min, max);
                richTextBox1.Text += numbers[i].ToString() + " ";
            }

            // Display a histogram.
            Pen thin_pen = new Pen(Color.Black, 0);
            thin_pen.Color = Color.LightBlue;
            DrawHistogram(pictureBox1, Brushes.Blue, thin_pen, numbers);

        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        // Display a histogram.
        private void DrawHistogram2(PictureBox pic, Brush brush, Pen pen, int[] values)
        {
            // Count the values.
            int min = values.Min();
            int max = values.Max();
            int[] counts = new int[max - min + 1];
            richTextBox1.Text += "counts = " + counts.Length.ToString() + "\n";
            int i;
            for (i = 0; i < values.Length; i++)
            {
                counts[values[i] - min]++;
            }

            for (i = 0; i < counts.Length; i++)
            {
                counts[i] = i + 5;
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

                int kk = 0;
                // Fill the histogram.
                for (i = 0; i < counts.Length; i++)
                {
                    gr.FillRectangle(brush, i, 0, 1, counts[i]);
                    kk++;

                }
                richTextBox1.Text += "draw " + kk.ToString() + " fill rectangles\n";

                // Draw the histogram.
                if (counts.Length < 200)
                {
                    kk = 0;
                    for (i = 0; i < counts.Length; i++)
                    {
                        gr.DrawRectangle(pen, i, 0, 1, counts[i]);
                        kk++;
                    }
                    richTextBox1.Text += "draw " + kk.ToString() + " empty rectangles\n";
                }
            }

            // Display the histogram.
            pic.Image = bm;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = null;
            Refresh();

            // Generate values with Random.
            int num_numbers;
            int min;
            int max;

            num_numbers = 10;
            min = 40;
            max = 60;

            richTextBox1.Text += "num_numbers = " + num_numbers.ToString() + "\n";
            richTextBox1.Text += "min = " + min.ToString() + "\n";
            richTextBox1.Text += "max = " + max.ToString() + "\n";

            int mean = (min + max) / 2;
            int amp = (max - min) / 2;

            //int[] numbers = new int[num_numbers];
            //for (int i = 0; i < num_numbers; i++)
            {
                //numbers[i] = (int)Math.Sin(i * 2 * Math.PI/1000);
                //numbers[i] = i;
            }

            Random rand = new Random();
            int[] numbers = new int[num_numbers];
            for (int i = 0; i < num_numbers; i++)
            {
                numbers[i] = rand.Next(min, max);
                richTextBox1.Text += numbers[i].ToString() + " ";
            }

            // Display a histogram.
            Pen thin_pen = new Pen(Color.Black, 0);
            thin_pen.Color = Color.LightBlue;
            DrawHistogram2(pictureBox1, Brushes.Blue, thin_pen, numbers);

        }

        private void button4_Click(object sender, EventArgs e)
        {
            // Display a histogram.
            Pen thin_pen = new Pen(Color.Black, 0);
            thin_pen.Color = Color.LightBlue;
            int num_numbers = 6;
            int[] numbers = new int[num_numbers];
            int i;
            for (i = 0; i < num_numbers; i++)
            {
                numbers[i] = i + 5;

            }
            DrawHistogram3(pictureBox1, Brushes.Blue, thin_pen, numbers);
        }

        // Display a histogram.
        private void DrawHistogram3(PictureBox pic, Brush brush, Pen pen, int[] values)
        {
            int i;
            int max_values = values.Max();

            richTextBox1.Text += "max_count = " + max_values.ToString() + "\n";

            // Make a Bitmap.
            Bitmap bm = new Bitmap(pic.ClientSize.Width, pic.ClientSize.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.SmoothingMode = SmoothingMode.AntiAlias;

                // Scale to fit the data.
                RectangleF rect = new RectangleF(0, 0, values.Length, max_values);
                gr.DrawRectangle(new Pen(Color.Red, 0), 0, 0, values.Length * 1, max_values * 1);

                //gr.DrawString("A", new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(20, 20));

                PointF[] pts = 
                {
                    new PointF(0, pic.ClientSize.Height),
                    new PointF(pic.ClientSize.Width, pic.ClientSize.Height),
                    new PointF(0, 0),
                };
                //gr.DrawRectangle(new Pen(Color.Green, 10), 0, 0, pic.ClientSize.Width, pic.ClientSize.Height);

                gr.DrawString("A", new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(30, 30));

                gr.Transform = new Matrix(rect, pts);

                int kk = 0;
                // Fill the histogram.
                for (i = 0; i < values.Length; i++)
                {
                    gr.FillRectangle(brush, i, 0, 1, values[i]);
                    gr.DrawString(i.ToString(), new Font("標楷體", 1), new SolidBrush(Color.Red), new PointF(i * 2, 0));
                    richTextBox1.Text += "kk = " + kk.ToString() + "\t" + i.ToString() + "\t0\t1\t" + values[i].ToString() + "\n";

                    kk++;

                }
                richTextBox1.Text += "draw " + kk.ToString() + " fill rectangles\n";

                // Draw the histogram.
                if (values.Length < 200)
                {
                    kk = 0;
                    for (i = 0; i < values.Length; i++)
                    {
                        gr.DrawRectangle(pen, i, 0, 1, values[i]);
                        kk++;
                    }
                    richTextBox1.Text += "draw " + kk.ToString() + " empty rectangles\n";
                }
            }

            // Display the histogram.
            pic.Image = bm;
        }


    }
}
