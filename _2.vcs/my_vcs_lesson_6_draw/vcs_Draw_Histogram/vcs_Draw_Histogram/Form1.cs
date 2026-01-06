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
            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 5;
            dy = 60 + 5;


            //richTextBox1.Size = new Size(790, 295);
            //richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 7 + 60);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //this.Size = new Size(1250, 880);
            this.Text = "vcs_Draw_Histogram";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "數字很小, 最大值 小於 pictureBox1的高度 H = " + pictureBox1.ClientSize.Height.ToString() + "\t需要放大數字\n";

            Pen p = new Pen(Color.LightBlue, 0);
            int num_numbers = 20;
            int[] numbers = new int[num_numbers];
            Random rand = new Random();
            int i;
            for (i = 0; i < num_numbers; i++)
            {
                numbers[i] = rand.Next(1, 9);
                richTextBox1.Text += numbers[i].ToString() + " ";
            }
            DrawHistogram(pictureBox1, Brushes.Blue, p, numbers);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "數字很大, 最大值 大於 pictureBox1的高度 H = " + pictureBox1.ClientSize.Height.ToString() + "\t需要縮小數字\n";

            Pen p = new Pen(Color.LightBlue, 0);
            int[] numbers = new int[] {
                                13092, 2607, 2229, 1512, 1140, 914, 66, 442, 902, 881, 880, 695, 657, 294, 5, 348,
                                514, 421, 361, 316, 135, 176, 261, 113, 162, 231, 236, 86, 140, 323, 172, 79,
                                122, 199, 78, 120, 146, 136, 134, 41, 107, 55, 92, 162, 139, 123, 117, 131,
                                52, 12, 77, 145, 132, 127, 112, 32, 77, 39, 74, 104, 113, 97, 33, 60,
                                102, 122, 36, 85, 101, 40, 96, 110, 111, 121, 38, 223, 235, 32, 84, 103,
                                107, 121, 43, 86, 50, 78, 105, 106, 108, 148, 116, 59, 8, 81, 101, 129,
                                131, 118, 43, 71, 45, 100, 124, 110, 134, 60, 83, 151, 160, 68, 112, 162,
                                84, 144, 228, 280, 280, 122, 220, 109, 259, 459, 479, 545, 636, 219, 30, 846,
                                920, 908, 1132, 1217, 1226, 476, 997, 540, 1118, 1742, 2031, 2059, 683, 1442, 2195, 636,
                                1738, 2280, 2645, 2722, 790, 2126, 3037, 3303, 948, 2378, 3442, 854, 2653, 3552, 3900, 4069,
                                1236, 2921, 1384, 2997, 5051, 4949, 5519, 5204, 1935, 21, 3379, 5397, 5430, 5334, 5339, 5387,
                                2071, 3318, 2014, 3585, 5597, 5989, 5565, 1983, 3353, 5493, 1921, 3275, 5010, 4887, 1719, 3356,
                                5778, 5101, 5606, 1548, 4009, 1396, 4560, 6157, 5765, 5524, 6112, 1434, 272, 4199, 5558, 5259,
                                4092, 3278, 2459, 516, 4, 1249, 1169, 698, 260, 55, 12, 15, 4, 26, 25, 7,
                                6, 1281, 10, 9, 6, 8, 17, 13, 7, 34, 8, 1, 0, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
            };
            DrawHistogram(pictureBox1, Brushes.Blue, p, numbers);
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

            richTextBox1.Text += "N = " + N.ToString() + "\n";

            int i;
            float ratio_y = 0;
            int y_max = values.Max();

            ratio_y = ((float)H * (100 - border_y * 2) / y_max) / 100;
            richTextBox1.Text += "ratio_y = " + ratio_y.ToString() + "\n";

            richTextBox1.Text += "old ";
            for (i = 0; i < N; i++)
            {
                richTextBox1.Text += values[i].ToString("D3") + " ";
            }
            richTextBox1.Text += "\n";

            for (i = 0; i < N; i++)
            {
                values[i] = (int)(values[i] * ratio_y);
            }

            richTextBox1.Text += "new ";
            for (i = 0; i < N; i++)
            {
                richTextBox1.Text += values[i].ToString("D3") + " ";
            }
            richTextBox1.Text += "\n";

            if (ratio_y < 1)
            {
                richTextBox1.Text += "數字很大\t需要縮小數字\n";
            }
            else
            {
                richTextBox1.Text += "數字很小\t需要放大數字\n";
            }

            y_max = values.Max();
            int y_min = values.Min();
            int y_diff = y_max - y_min;
            //int ratio_x = 0;
            ratio_y = H * (100 - border_y * 2) / (y_diff + 1) / 100;
            ratio_y = 1;

            richTextBox1.Text += "y_max = " + y_max.ToString() + "\n";
            richTextBox1.Text += "y_min = " + y_min.ToString() + "\n";
            richTextBox1.Text += "y_diff = " + y_diff.ToString() + "\n";
            richTextBox1.Text += "ratio_y = " + ratio_y.ToString() + "\n";

            int x_st = border_x * W / 100;
            int y_st = border_y * H / 100;
            //richTextBox1.Text += "y_st = " + y_st.ToString() + "\n";

            //先考慮滿框狀態


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

        private void timer1_Tick(object sender, EventArgs e)
        {
            //右下小圖
            int i;
            Pen p = new Pen(Color.LightBlue, 0);
            int num_numbers = 12;
            int[] numbers = new int[num_numbers];
            Random rand = new Random();
            for (i = 0; i < num_numbers; i++)
            {
                numbers[i] = rand.Next(1, 9);
                //richTextBox1.Text += numbers[i].ToString() + " ";
            }
            DrawHistogram(pictureBox_histogram, Brushes.Blue, p, numbers);

            //原本範例, 下方大長條圖
            draw_histogram_old();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            int i;
            Pen p = new Pen(Color.LightBlue, 0);
            int num_numbers = 10;
            float[] numbers = new float[num_numbers];
            Random rand = new Random();
            for (i = 0; i < num_numbers; i++)
            {
                //result4 += r.NextDouble().ToString() + " ";
                numbers[i] = (float)rand.NextDouble() * 100;
                richTextBox1.Text += numbers[i].ToString() + " ";
            }
            DrawHistogramF(pictureBox1, Brushes.Blue, p, numbers);
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
            using (Pen p = new Pen(Color.LightBlue, 0))
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
                DrawHistogram_old(pictureBox_old, Brushes.Blue, p, rand_numbers);
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
