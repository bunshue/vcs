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

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            int i;
            Pen thin_pen = new Pen(Color.Black, 0);
            thin_pen.Color = Color.LightBlue;
            int num_numbers = 40;
            int[] numbers = new int[num_numbers];
            Random rand = new Random();
            for (i = 0; i < num_numbers; i++)
            {
                numbers[i] = rand.Next(1, 9);
                richTextBox1.Text += numbers[i].ToString() + " ";
            }
            DrawHistogram(pictureBox1, Brushes.Blue, thin_pen, numbers);
        }

        // Display a histogram.
        private void DrawHistogram(PictureBox pic, Brush brush, Pen pen, int[] values)
        {
            //david 改畫長條圖 int array
            int border_x = 4;   //percentage of width
            int border_y = 12;  //percentage of height
            int W = pic.ClientSize.Width;
            int H = pic.ClientSize.Height;
            int N = values.Length;
            int w = W * (100 - border_x * 2) / N / 100;
            //int h = 0;

            int y_max = values.Max();
            int y_min = values.Min();
            int y_diff = y_max - y_min;
            //int ratio_x = 0;
            int ratio_y = H * (100 - border_y * 2) / (y_diff + 1) / 100;

            int x_st = border_x * W / 100;
            int y_st = border_y * H / 100;
            //richTextBox1.Text += "y_st = " + y_st.ToString() + "\n";

            //先考慮滿框狀態

            int i;

            // Make a Bitmap.
            Bitmap bitmap1 = new Bitmap(W, H);
            using (Graphics g = Graphics.FromImage(bitmap1))
            {
                g.SmoothingMode = SmoothingMode.AntiAlias;

                // Fill the histogram.
                for (i = 0; i < N; i++)
                {
                    g.FillRectangle(brush, x_st + i * w, H - values[i] * ratio_y - y_st, w, values[i] * ratio_y);
                    g.DrawString(values[i].ToString(), new Font("標楷體", 8), new SolidBrush(Color.Red), new PointF(x_st + i * w + w / 3, H - y_st+3));
                }

                // Draw the histogram.
                if (N < 200)
                {
                    for (i = 0; i < N; i++)
                    {
                        //g.DrawRectangle(pen, i * w, 0, w, values[i] * ratio_y);
                        g.DrawRectangle(pen, x_st + i * w, H - values[i] * ratio_y - y_st, w, values[i] * ratio_y);
                    }
                }
            }

            // Display the histogram.
            pic.Image = bitmap1;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            //右下小圖
            int i;
            Pen thin_pen = new Pen(Color.Black, 0);
            thin_pen.Color = Color.LightBlue;
            int num_numbers = 12;
            int[] numbers = new int[num_numbers];
            Random rand = new Random();
            for (i = 0; i < num_numbers; i++)
            {
                numbers[i] = rand.Next(1, 9);
                //richTextBox1.Text += numbers[i].ToString() + " ";
            }
            DrawHistogram(pictureBox_histogram, Brushes.Blue, thin_pen, numbers);

            //原本範例, 下方大長條圖
            draw_histogram_old();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            int i;
            Pen thin_pen = new Pen(Color.Black, 0);
            thin_pen.Color = Color.LightBlue;
            int num_numbers = 10;
            float[] numbers = new float[num_numbers];
            Random rand = new Random();
            for (i = 0; i < num_numbers; i++)
            {
                //result4 += r.NextDouble().ToString() + " ";
                numbers[i] = (float)rand.NextDouble() * 100;
                richTextBox1.Text += numbers[i].ToString() + " ";
            }
            DrawHistogramF(pictureBox1, Brushes.Blue, thin_pen, numbers);
        }

        // Display a histogram.
        private void DrawHistogramF(PictureBox pic, Brush brush, Pen pen, float[] values)
        {
            //david 改畫長條圖 float array
            int border_x = 4;   //percentage of width
            int border_y = 12;  //percentage of height
            int W = pic.ClientSize.Width;
            int H = pic.ClientSize.Height;
            int N = values.Length;
            int w = W * (100 - border_x * 2) / N / 100;
            //int h = 0;

            float y_max = values.Max();
            float y_min = values.Min();
            float y_diff = y_max - y_min;
            //int ratio_x = 0;
            float ratio_y = H * (100 - border_y * 2) / (y_diff + 1) / 100;

            int x_st = border_x * W / 100;
            int y_st = border_y * H / 100;
            //richTextBox1.Text += "y_st = " + y_st.ToString() + "\n";

            //先考慮滿框狀態

            int i;

            // Make a Bitmap.
            Bitmap bitmap1 = new Bitmap(W, H);
            using (Graphics g = Graphics.FromImage(bitmap1))
            {
                g.SmoothingMode = SmoothingMode.AntiAlias;

                // Fill the histogram.
                for (i = 0; i < N; i++)
                {
                    g.FillRectangle(brush, x_st + i * w, H - values[i] * ratio_y - y_st, w, values[i] * ratio_y);
                    g.DrawString(values[i].ToString(), new Font("標楷體", 8), new SolidBrush(Color.Red), new PointF(x_st + i * w + w / 3, H - y_st + 3));
                }

                // Draw the histogram.
                if (N < 200)
                {
                    for (i = 0; i < N; i++)
                    {
                        //g.DrawRectangle(pen, i * w, 0, w, values[i] * ratio_y);
                        g.DrawRectangle(pen, x_st + i * w, H - values[i] * ratio_y - y_st, w, values[i] * ratio_y);
                    }
                }
            }

            // Display the histogram.
            pic.Image = bitmap1;
        }


        //原本範例 ST
        void draw_histogram_old()
        {
            using (Pen thin_pen = new Pen(Color.Black, 0))
            {
                pictureBox_old.Image = null;
                Refresh();

                // Generate values with Random.
                int num_numbers = 1000;
                int min = 1;
                int max = 100;
                Random rand = new Random();
                int[] rand_numbers = new int[num_numbers];
                for (int i = 0; i < num_numbers; i++)
                    rand_numbers[i] = rand.Next(min, max);

                // Display a histogram.
                thin_pen.Color = Color.LightBlue;
                DrawHistogram_old(pictureBox_old, Brushes.Blue, thin_pen, rand_numbers);
            }
        }

        // Display a histogram.
        private void DrawHistogram_old(PictureBox pic, Brush brush, Pen pen, int[] values)
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
            Bitmap bitmap1 = new Bitmap(pic.ClientSize.Width, pic.ClientSize.Height);
            using (Graphics g = Graphics.FromImage(bitmap1))
            {
                g.SmoothingMode = SmoothingMode.AntiAlias;

                // Scale to fit the data.
                RectangleF rect = new RectangleF(0, 0, counts.Length, max_count);
                PointF[] pts = 
                {
                    new PointF(0, pic.ClientSize.Height),
                    new PointF(pic.ClientSize.Width, pic.ClientSize.Height),
                    new PointF(0, 0),
                };
                g.Transform = new Matrix(rect, pts);

                // Fill the histogram.
                for (int i = 0; i < counts.Length; i++)
                {
                    g.FillRectangle(brush, i, 0, 1, counts[i]);
                }

                // Draw the histogram.
                if (counts.Length < 200)
                {
                    for (int i = 0; i < counts.Length; i++)
                    {
                        g.DrawRectangle(pen, i, 0, 1, counts[i]);
                    }
                }
            }

            // Display the histogram.
            pic.Image = bitmap1;
        }
        //原本範例 SP




    }
}
