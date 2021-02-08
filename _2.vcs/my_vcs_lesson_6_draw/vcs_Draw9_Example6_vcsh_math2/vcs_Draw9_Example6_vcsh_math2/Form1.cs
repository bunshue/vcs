using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for CompositingQuality, SmoothingMode
using System.Drawing.Imaging;   //for ImageFormat
using System.Drawing.Text;      //for TextRenderingHint

namespace vcs_Draw9_Example6_vcsh_math2
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;
        int W = 250;
        int H = 250;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // Reduce flicker.
            DoubleBuffered = true;

            show_item_location();

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;

            bt_exit_setup();

            DrawFractal();
            Application.DoEvents();
            DrawLevelCurves(pictureBox7, F1, -75, 65, 20);
            Application.DoEvents();
            DrawLevelCurves(pictureBox8, F2, -200, 200, 40);
            Application.DoEvents();
            DrawLevelCurves(pictureBox9, F3, 0, 800, 100);
            Application.DoEvents();
            DrawLevelCurves(pictureBox10, F4, 0, 5, 0.75f);
            Application.DoEvents();
        }

        void show_item_location()
        {
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new System.Drawing.Point(0, 0);

            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 1700;
            y_st = 10;
            dx = 140;
            dy = 55;

            bt_save.Location = new Point(x_st + dx * 0 + 110, y_st + dy * 12);
            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 13);
            richTextBox1.Size = new Size(210, 350);

            x_st = 10;
            y_st = 60;
            dx = W + 30;
            dy = H + 60;

            pictureBox_pi1.Size = new Size(W * 3 / 2, H);
            pictureBox_pi2.Size = new Size(W * 3 / 2, H);
            pictureBox4.Size = new Size(W, H);
            pictureBox_fractal.Size = new Size(W * 2 + 100, H * 2 + 100);
            pictureBox7.Size = new Size(W, H);
            pictureBox8.Size = new Size(W, H);
            pictureBox9.Size = new Size(W, H);
            pictureBox10.Size = new Size(W, H);
            pictureBox13.Size = new Size(W, H);
            pictureBox14.Size = new Size(W, H);
            pictureBox15.Size = new Size(W, H);
            pictureBox16.Size = new Size(W, H);
            pictureBox17.Size = new Size(W, H);
            pictureBox18.Size = new Size(W, H);

            pictureBox_pi1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox_pi2.Location = new Point(x_st + dx * 1 + dx / 2, y_st + dy * 0);
            pictureBox4.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            pictureBox_fractal.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            label17.Location = new Point(x_st + dx * 4, y_st + dy * 0 - 40);
            lblNumPoints.Location = new Point(x_st + dx * 4 + 100, y_st + dy * 0 - 40);
            label16.Location = new Point(x_st + dx * 4 + 300, y_st + dy * 0 - 40);
            lblPrime.Location = new Point(x_st + dx * 4 + 300 + 100, y_st + dy * 0 - 40);

            pictureBox7.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox8.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            pictureBox9.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            pictureBox10.Location = new Point(x_st + dx * 3, y_st + dy * 1);

            pictureBox13.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            pictureBox14.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            pictureBox15.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            pictureBox16.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            pictureBox17.Location = new Point(x_st + dx * 4, y_st + dy * 2);
            pictureBox18.Location = new Point(x_st + dx * 5, y_st + dy * 2);


            label1.Location = new Point(x_st + dx * 0, y_st + dy * 0 - 25);
            label2.Location = new Point(x_st + dx * 1, y_st + dy * 0 - 25);
            label3.Location = new Point(x_st + dx * 2, y_st + dy * 0 - 25);
            label4.Location = new Point(x_st + dx * 3, y_st + dy * 0 - 25);
            label5.Location = new Point(x_st + dx * 4, y_st + dy * 0 - 25);
            label6.Location = new Point(x_st + dx * 5, y_st + dy * 0 - 25);

            label7.Location = new Point(x_st + dx * 0, y_st + dy * 1 - 25);
            label8.Location = new Point(x_st + dx * 1, y_st + dy * 1 - 25);
            label9.Location = new Point(x_st + dx * 2, y_st + dy * 1 - 25);
            label10.Location = new Point(x_st + dx * 3, y_st + dy * 1 - 25);
            label11.Location = new Point(x_st + dx * 4, y_st + dy * 1 - 25);
            label12.Location = new Point(x_st + dx * 5, y_st + dy * 1 - 25);

            label13.Location = new Point(x_st + dx * 0, y_st + dy * 2 - 25);
            label14.Location = new Point(x_st + dx * 1, y_st + dy * 2 - 25);
            label15.Location = new Point(x_st + dx * 24, y_st + dy * 2 - 25);

            label1.Text = "";
            label2.Text = "";
            label3.Text = "";
            label4.Text = "";
            label5.Text = "";
            label6.Text = "";
            label7.Text = "Bowl: z = x^2 + (y*2)^2 - 75";
            label8.Text = "Monkey saddle: x * (x^2 - 3 * y^2)";
            label9.Text = "Crossed trough: x^2 * y^2";
            label10.Text = "Hemisphere: Sqrt(25 - (x^2 + y^2))";
            label11.Text = "";
            label12.Text = "";
            label13.Text = "";
            label14.Text = "";
            label15.Text = "";

            //richTextBox1.Size = new Size(bt_exit.Right - richTextBox1.Location.X - 5, this.Height - richTextBox1.Location.Y - 25);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            bitmap1 = null;
            richTextBox1.Clear();
        }

        void save_image_to_drive()
        {
            if (bitmap1 != null)
            {
                string filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                string filename1 = filename + ".jpg";
                string filename2 = filename + ".bmp";
                string filename3 = filename + ".png";

                try
                {
                    bitmap1.Save(@filename1, ImageFormat.Jpeg);
                    bitmap1.Save(@filename2, ImageFormat.Bmp);
                    bitmap1.Save(@filename3, ImageFormat.Png);

                    richTextBox1.Text += "存檔成功\n";
                    richTextBox1.Text += "已存檔 : " + filename1 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename3 + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }
            else
                richTextBox1.Text += "無圖可存\n";
        }

        private void bt_save_Click(object sender, EventArgs e)
        {
            save_image_to_drive();
        }

        private void pictureBox_pi1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            DrawGraph1(e.Graphics, 22);
        }

        // Draw the graph on a Graphics object.
        private void DrawGraph1(Graphics gr, int num_terms)
        {
            // Calculate the approximation values.
            double[] values = new double[num_terms];
            double four = 4;
            double pi = 0;
            for (int i = 0; i < num_terms; i++)
            {
                pi += four / (2 * i + 1);
                values[i] = pi;
                four = -four;
            }

            // Set up a transformation to fit
            // the graph to the PictureBox.
            RectangleF rect = new RectangleF(-1, 2.5f, num_terms - 1, 2);
            PointF[] points =
            {
                new PointF(0, pictureBox_pi1.ClientSize.Height),
                new PointF(pictureBox_pi1.ClientSize.Width, pictureBox_pi1.ClientSize.Height),
                new PointF(0, -0.5f),
            };
            Matrix transform = new Matrix(rect, points);

            // Draw labels.
            using (StringFormat sf = new StringFormat())
            {
                // Label the Y axis.
                sf.Alignment = StringAlignment.Far;
                sf.LineAlignment = StringAlignment.Center;
                using (Font font = new Font("Times New Roman", 12))
                {
                    for (int y = 3; y <= 4; y++)
                    {
                        // See where this point will be after it is transformed.
                        PointF[] txt_pts = { new PointF(-0.25f, y) };
                        transform.TransformPoints(txt_pts);
                        gr.DrawString(y.ToString(), font,
                            Brushes.Black, txt_pts[0].X, txt_pts[0].Y, sf);
                    }
                } // Font

                // Label pi.
                sf.Alignment = StringAlignment.Near;
                sf.LineAlignment = StringAlignment.Far;
                using (Font font = new Font("Times New Roman", 16))
                {
                    PointF[] pi_pts = { new PointF(0.5f, (float)Math.PI) };
                    transform.TransformPoints(pi_pts);
                    gr.DrawString("π", font,
                        Brushes.Black, pi_pts[0].X, pi_pts[0].Y, sf);
                } // Font
            } // StringFormat

            // Draw the rest in the transformed coordinates.
            gr.Transform = transform;

            // Use an unscaled pen.
            using (Pen thin_pen = new Pen(Color.Blue, 0))
            {
                // Draw the line y = pi.
                gr.DrawLine(thin_pen, 0, (float)Math.PI, num_terms, (float)Math.PI);

                // Draw the Y axis.
                thin_pen.Color = Color.Gray;
                gr.DrawLine(thin_pen, 0, -1, 0, 5);
                for (int y = 1; y <= 4; y++)
                {
                    gr.DrawLine(thin_pen, -0.25f, y, 0.25f, y);
                }

                // Draw the approximations.
                thin_pen.Color = Color.Green;
                PointF[] pts = new PointF[num_terms];
                for (int i = 0; i < num_terms; i++)
                {
                    pts[i] = new PointF(i, (float)values[i]);
                }
                gr.DrawCurve(thin_pen, pts);

                // Draw the upper enveloping curve.
                thin_pen.DashStyle = DashStyle.Custom;
                thin_pen.DashPattern = new float[] { 30, 30 };

                thin_pen.Color = Color.Red;
                pts = new PointF[num_terms / 2];
                for (int i = 0; i < num_terms / 2; i++)
                {
                    pts[i] = new PointF(2 * i, (float)values[2 * i]);
                }
                gr.DrawCurve(thin_pen, pts);

                // Draw the lower enveloping curve.
                pts = new PointF[num_terms / 2];
                for (int i = 0; i < num_terms / 2; i++)
                {
                    pts[i] = new PointF(2 * i + 1, (float)values[2 * i + 1]);
                }
                gr.DrawCurve(thin_pen, pts);

            } // Pen
        }

        /*
        // Calculate the term_index-th term for the pi approximation.
        // Term 1 has index 0.
        private double PiTerm(int term_index)
        {
            return 4 * Math.Pow(-1, term_index) / (2 * term_index + 1);
        }
        */


        // Draw the graph.
        private void pictureBox_pi2_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            DrawGraph2(e.Graphics, 10);
        }

        // Draw the graph on a Graphics object.
        private void DrawGraph2(Graphics gr, int num_terms)
        {
            // Calculate the approximation values.
            double[] values = new double[num_terms];
            double four = 4;
            double pi = 0;
            for (int i = 0; i < num_terms; i++)
            {
                pi += four / (2 * i + 1);
                values[i] = pi;
                four = -four;
            }

            // Set up a transformation to fit
            // the graph to the PictureBox.
            RectangleF rect = new RectangleF(-0.5f, 1.75f, num_terms - 1, 2.5f);
            PointF[] points =
            {
                new PointF(0, pictureBox_pi2.ClientSize.Height),
                new PointF(pictureBox_pi2.ClientSize.Width, pictureBox_pi2.ClientSize.Height),
                new PointF(0, -0.5f),
            };
            Matrix transform = new Matrix(rect, points);

            // Draw labels.
            using (StringFormat sf = new StringFormat())
            {
                // Label the Y axis.
                sf.Alignment = StringAlignment.Far;
                sf.LineAlignment = StringAlignment.Center;
                using (Font font = new Font("Times New Roman", 12))
                {
                    for (int y = 2; y <= 4; y++)
                    {
                        // See where this point will be after it is transformed.
                        PointF[] txt_pts = { new PointF(-0.25f, y) };
                        transform.TransformPoints(txt_pts);
                        gr.DrawString(y.ToString(), font,
                            Brushes.Black, txt_pts[0].X, txt_pts[0].Y, sf);
                    }

                    // Draw the key.
                    float text_x = 135;
                    float text_y = 300;
                    float line_space = font.Size * 2;
                    gr.DrawString("Gregory-Leibniz", font,
                        Brushes.Green, text_y, text_x);
                    text_x += line_space;

                    gr.DrawString("Nilakantha", font,
                        Brushes.Red, text_y, text_x);
                    text_x += line_space;

                    gr.DrawString("Newton", font,
                        Brushes.Blue, text_y, text_x);
                    text_x += line_space;

                    gr.DrawString("Arcsine", font,
                        Brushes.Black, text_y, text_x);
                    text_x += line_space;
                } // Font

                // Label pi.
                sf.Alignment = StringAlignment.Near;
                sf.LineAlignment = StringAlignment.Far;
                using (Font font = new Font("Times New Roman", 16))
                {
                    PointF[] pi_pts = { new PointF(0, (float)Math.PI) };
                    transform.TransformPoints(pi_pts);
                    gr.DrawString("π", font,
                        Brushes.Black, pi_pts[0].X, pi_pts[0].Y, sf);
                } // Font
            } // StringFormat

            // Draw the rest in the transformed coordinates.
            gr.Transform = transform;

            // Use an unscaled pen.
            using (Pen thin_pen = new Pen(Color.Lime, 0))
            {
                // Draw the line y = pi.
                gr.DrawLine(thin_pen, 0, (float)Math.PI,
                    num_terms, (float)Math.PI);

                // Draw the Y axis.
                thin_pen.Color = Color.Gray;
                gr.DrawLine(thin_pen, 0, -1, 0, 5);
                for (int y = 1; y <= 4; y++)
                {
                    gr.DrawLine(thin_pen, -0.25f, y, 0.25f, y);
                }

                // Draw the X tic marks.
                thin_pen.Color = Color.Gray;
                float y0 = (float)Math.PI - 0.05f;
                float y1 = (float)Math.PI + 0.05f;
                for (int x = 1; x <= num_terms; x++)
                {
                    gr.DrawLine(thin_pen, x, y0, x, y1);
                }

                // Draw the approximations.
                thin_pen.Color = Color.Green;
                PointF[] pts = new PointF[num_terms];
                for (int i = 0; i < num_terms; i++)
                {
                    pts[i] = new PointF(i, (float)values[i]);
                }
                gr.DrawCurve(thin_pen, pts);

                // Draw Nilakantha's approximation.
                thin_pen.Color = Color.Red;
                pts = new PointF[num_terms];
                for (int i = 0; i < num_terms; i++)
                {
                    pts[i] = new PointF(i, (float)NilakanthaPi(i));
                }
                gr.DrawCurve(thin_pen, pts);

                // Draw Newton's approximation.
                thin_pen.Color = Color.Blue;
                pts = new PointF[num_terms];
                for (int i = 0; i < num_terms; i++)
                {
                    pts[i] = new PointF(i, (float)Pi(i));
                }
                gr.DrawCurve(thin_pen, pts);

                // Draw the arcsine approximation.
                thin_pen.Color = Color.Black;
                pts = new PointF[num_terms];
                for (int i = 0; i < num_terms; i++)
                {
                    pts[i] = new PointF(i, (float)ArcsinePi(i));
                }
                gr.DrawCurve(thin_pen, pts);
            } // Pen
        }

        /*
        // Calculate the term_index-th term for the pi approximation.
        // Term 1 has index 0.
        private double PiTerm(int term_index)
        {
            return 4 * Math.Pow(-1, term_index) / (2 * term_index + 1);
        }
        */

        #region Newton's approximation

        // Pi/2 = Sum(k!/(2k+1)!!)
        private double Pi(int num_terms)
        {
            double result = 0;
            for (int k = 0; k < num_terms; k++)
                result += Factorial(k) / OddProd(2 * k + 1);
            return result * 2;
        }

        // Return n!
        private double Factorial(long n)
        {
            double result = 1;
            for (long i = 2; i <= n; i++) result *= i;
            return result;
        }

        // Return the product of the odd integers up to the number.
        private double OddProd(long n)
        {
            double result = 1;
            for (long i = 3; i <= n; i += 2) result *= i;
            return result;
        }

        #endregion Newton's approximation

        #region Nilakantha

        // Nilakantha series.
        // Pi/2 = Sum(-1^k/(2k+2)(2k+3)(2k+4))
        private double NilakanthaPi(int num_terms)
        {
            double result = 0;
            double sign = 1;
            for (int i = 0; i < num_terms; i++)
            {
                result += sign / (2 * i + 2) / (2 * i + 3) / (2 * i + 4);
                sign = -sign;
            }
            return 3 + result * 4;
        }

        #endregion Nilakantha

        #region Arcsine

        // Arcsine series.
        // Pi = Sum(3*(2n choose n) / 16^n (2*n+1))
        private double ArcsinePi(int num_terms)
        {
            double result = 0;
            for (int i = 0; i < num_terms; i++)
                result += 3 * Choose(2 * i, i)
                    / Math.Pow(16, i)
                    / (2 * i + 1);
            return result;
        }

        // Return n choose k.
        private double Choose(int n, int k)
        {
            double result = 1;
            for (int i = 1; i <= k; i++)
            {
                result *= n - (k - i);
                result /= i;
            }
            return result;
        }

        #endregion Arcsine


        #region draw fractal

        private const int Wid = 250 * 2 + 100;
        private const int Hgt = 250 * 2 + 100;
        private const int XOff = 150;
        private const int YOff = 200;

        private int[,] Hits = new int[Wid, Hgt];
        private Point CurrentPoint = new Point(0, 0);
        private long CurrentPrime = 1;

        // Start or stop.
        private bool Running = true;

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

                if (NumPoints > 200000)
                {
                    Running = false;
                }
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
            pictureBox_fractal.Image = bm;
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
        #endregion draw fractal



        #region 四個等高線圖 picturebox 7 8 9 10


        // The function type.
        private delegate float FofXY(float x, float y);

        // Draw level curves for this function.
        private void DrawLevelCurves(PictureBox pbox, FofXY func, float zmin, float zmax, float dz)
        {
            this.Cursor = Cursors.WaitCursor;

            // Make the Bitmap.
            Bitmap bm = new Bitmap(pbox.ClientSize.Width, pbox.ClientSize.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                // Clear.
                gr.Clear(Color.White);
                gr.ScaleTransform(24f, -24f, System.Drawing.Drawing2D.MatrixOrder.Append);
                gr.TranslateTransform(bm.Width * 0.5f, bm.Height * 0.5f,
                    System.Drawing.Drawing2D.MatrixOrder.Append);

                // Draw axes.
                using (Pen axis_pen = new Pen(Color.Gray, 0))
                {
                    gr.DrawLine(axis_pen, -6, 0, 6, 0);
                    gr.DrawLine(axis_pen, 0, -6, 0, 6);
                    for (int i = -6; i <= 6; i++)
                    {
                        gr.DrawLine(axis_pen, i, -0.1f, i, 0.1f);
                        gr.DrawLine(axis_pen, -0.1f, i, 0.1f, i);
                    }
                }

                // Draw the level curves.
                float dx = 2f / bm.Width;
                float dy = 2f / bm.Height;
                for (float z = zmin; z <= zmax; z += dz)
                {
                    DrawLevelCurve(gr, func, z, dx, dy);
                }
            } // using gr.

            // Display the result.
            pbox.Image = bm;
            this.Cursor = Cursors.Default;
        }

        // Plot a function.
        private void DrawLevelCurve(Graphics gr, FofXY func, float z, float dx, float dy)
        {
            // Console.WriteLine("z = " + z.ToString());

            // Plot the function.
            using (Pen thin_pen = new Pen(Color.Black, 0))
            {
                // Red for z < 0, blue for z > 0.
                if (z < 0)
                {
                    thin_pen.Color = Color.Red;
                }
                else if (z > 0)
                {
                    thin_pen.Color = Color.Blue;
                }

                // Horizontal comparisons.
                for (float x = -6f; x <= 6f; x += dx)
                {
                    float last_y = z - func(x, -6f);
                    for (float y = -6f + dy; y <= 6f; y += dy)
                    {
                        float next_y = z - func(x, y);
                        if (
                            ((last_y <= 0f) && (next_y >= 0f)) ||
                            ((last_y >= 0f) && (next_y <= 0f))
                           )
                        {
                            // Plot this point.
                            gr.DrawLine(thin_pen, x, y - dy, x, y);
                        }
                        last_y = next_y;
                    }
                } // Horizontal comparisons.

                // Vertical comparisons.
                for (float y = -6f + dy; y <= 6f; y += dy)
                {
                    float last_x = z - func(-6f, y);
                    for (float x = -6f; x <= 6f; x += dx)
                    {
                        float next_x = z - func(x, y);
                        if (
                            ((last_x <= 0f) && (next_x >= 0f)) ||
                            ((last_x >= 0f) && (next_x <= 0f))
                           )
                        {
                            // Plot this point.
                            gr.DrawLine(thin_pen, x - dx, y, x, y);
                        }
                        last_x = next_x;
                    }
                } // Vertical comparisons.
            } // using thin_pen.
        }

        // Bowl.
        private float F1(float x, float y)
        {
            return x * x + (y * 2) * (y * 2) - 75;
        }

        // Monkey saddle.
        private float F2(float x, float y)
        {
            return x * (x * x - 3 * y * y);
        }

        // Crossed trough.
        private float F3(float x, float y)
        {
            return x * x * y * y;
        }

        // Hemisphere.
        private float F4(float x, float y)
        {
            return (float)Math.Sqrt(25 - (x * x + y * y));
        }

        #endregion 四個等高線圖
    }
}
