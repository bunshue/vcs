using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;
using System.Drawing.Text;  //for TextRenderingHint

namespace vcs_Draw_Function
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

            //6060

            label4.Text = "";
            //this.ClientSize = new Size(800, 600);
            G = this.pictureBox2.CreateGraphics();
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);

            groupBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            groupBox3.Location = new Point(x_st + dx * 2 + 30, y_st + dy * 0);
            groupBox2.Location = new Point(x_st + dx * 3 + 60, y_st + dy * 0);

            pictureBox1.Size = new Size(840, 480);
            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            pictureBox2.Size = new Size(300, 300);
            pictureBox2.Location = new Point(x_st + dx * 4 + 100, y_st + dy * 0);
            comboBox1.Location = new Point(x_st + dx * 4 + 100, y_st + dy * 0);
            richTextBox1.Size = new Size(300, 690-300-10);
            richTextBox1.Location = new Point(x_st + dx * 4 + 100, y_st + dy * 0+300+10);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1273, 750);
            this.Text = "vcs_Draw_Function";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        //畫平均分佈
        private void button4_Click(object sender, EventArgs e)
        {
            float mean = float.Parse(txtMean.Text);
            float stddev = float.Parse(txtStdDev.Text);
            float var = stddev * stddev;
            float devs = float.Parse(txtDevs.Text);

            pictureBox1.Image = DrawDistribution(devs, pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height, mean, stddev, var);
        }

        // The normal distribution function.
        private float F_normal1(float x, float one_over_2pi, float mean, float stddev, float var)
        {
            return (float)(one_over_2pi * Math.Exp(-(x - mean) * (x - mean) / (2 * var)));
        }

        // Draw the normal distribution scaled to fit the curve
        // within stddev_multiple deviations.
        private Bitmap DrawDistribution(float stddev_multiple, int wid, int hgt, float mean, float stddev, float var)
        {
            // Make a bitmap.
            Bitmap bm = new Bitmap(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.SmoothingMode = SmoothingMode.AntiAlias;

                // Define the mapping from world
                // coordinates onto the PictureBox.
                float wxmin = mean - stddev * stddev_multiple;
                float wxmax = mean + stddev * stddev_multiple;
                float one_over_2pi = (float)(1.0 / (stddev * Math.Sqrt(2 * Math.PI)));
                float wymax = F_normal1(mean, one_over_2pi, mean, stddev_multiple, var) * 1.1f;
                float wymin = -0.2f * wymax;

                float wwid = wxmax - wxmin;
                float whgt = wymax - wymin;
                RectangleF world = new RectangleF(wxmin, wymin, wwid, whgt);
                PointF[] device_points =
                {
                    new PointF(0, pictureBox1.ClientSize.Height),
                    new PointF(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height),
                    new PointF(0, 0),
                };
                Matrix transform = new Matrix(world, device_points);

                // Get the inverse transform.
                Matrix inverse = transform.Clone();
                inverse.Invert();

                // Get tick mark lengths.
                PointF[] ticks = { new PointF(5, 5) };
                inverse.TransformVectors(ticks);
                float tick_dx = ticks[0].X;
                float tick_dy = -ticks[0].Y;

                // Make a thin Pen to use.
                using (Pen pen = new Pen(Color.Red, 0))
                {
                    using (Font font = new Font("Arial", 8))
                    {
                        // Draw the X axis.
                        gr.Transform = transform;
                        pen.Color = Color.Black;
                        gr.DrawLine(pen, wxmin, 0, wxmax, 0);
                        for (int x = (int)wxmin - 1; x <= wxmax; x++)
                        {
                            gr.DrawLine(pen, x, -tick_dy * 2, x, tick_dy * 2);
                            gr.DrawLine(pen, x + 0.25f, -tick_dy, x + 0.25f, tick_dy);
                            gr.DrawLine(pen, x + 0.50f, -tick_dy, x + 0.50f, tick_dy);
                            gr.DrawLine(pen, x + 0.75f, -tick_dy, x + 0.75f, tick_dy);
                        }

                        // Label the X axis.
                        gr.Transform = new Matrix();
                        gr.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;
                        List<PointF> ints = new List<PointF>();
                        for (int x = (int)wxmin; x <= wxmax; x++)
                        {
                            ints.Add(new PointF(x, -2 * tick_dy));
                        }
                        PointF[] ints_array = ints.ToArray();
                        transform.TransformPoints(ints_array);

                        using (StringFormat sf = new StringFormat())
                        {
                            sf.Alignment = StringAlignment.Center;
                            sf.LineAlignment = StringAlignment.Near;
                            int index = 0;
                            for (int x = (int)wxmin; x <= wxmax; x++)
                            {
                                gr.DrawString(x.ToString(), font, Brushes.Black, ints_array[index++], sf);
                            }
                        }

                        // Draw the Y axis.
                        gr.Transform = transform;
                        pen.Color = Color.Black;
                        gr.DrawLine(pen, 0, wymin, 0, wymax);
                        for (int y = (int)wymin - 1; y <= wymax; y++)
                        {
                            gr.DrawLine(pen, -tick_dx * 2, y, tick_dx * 2, y);
                            gr.DrawLine(pen, -tick_dx, y + 0.25f, tick_dx, y + 0.25f);
                            gr.DrawLine(pen, -tick_dx, y + 0.50f, tick_dx, y + 0.50f);
                            gr.DrawLine(pen, -tick_dx, y + 0.75f, tick_dx, y + 0.75f);
                        }

                        // Label the Y axis.
                        gr.Transform = new Matrix();
                        gr.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;
                        ints = new List<PointF>();
                        for (float y = 0.25f; y < wymax; y += 0.25f)
                        {
                            ints.Add(new PointF(2 * tick_dx, y));
                        }
                        if (ints.Count > 0)
                        {
                            ints_array = ints.ToArray();
                            transform.TransformPoints(ints_array);
                        }

                        using (StringFormat sf = new StringFormat())
                        {
                            sf.Alignment = StringAlignment.Near;
                            sf.LineAlignment = StringAlignment.Center;
                            int index = 0;
                            for (float y = 0.25f; y < wymax; y += 0.25f)
                            {
                                gr.DrawString(y.ToString("0.00"), font, Brushes.Black, ints_array[index++], sf);
                            }
                        }

                        // Draw the curve.
                        gr.Transform = transform;
                        List<PointF> points = new List<PointF>();

                        float dx = (wxmax - wxmin) / pictureBox1.ClientSize.Width;
                        for (float x = wxmin; x <= wxmax; x += dx)
                        {
                            float y = F_normal1(x, one_over_2pi, mean, stddev, var);
                            points.Add(new PointF(x, y));
                        }
                        pen.Color = Color.Red;
                        gr.DrawLines(pen, points.ToArray());
                    } // Font
                } // Pen
            }
            return bm;
        }

        //------------------------------------------------------------  # 60個

        //畫三角函數 ST
        // The image used for the graph.
        private Bitmap GraphImage;

        // Graph.
        private void button6_Click(object sender, EventArgs e)
        {
            GraphImage = new Bitmap(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height);
            using (Graphics gr = Graphics.FromImage(GraphImage))
            {
                gr.Clear(Color.White);
                gr.SmoothingMode = SmoothingMode.AntiAlias;

                using (Pen thin_pen = new Pen(Color.Purple, 0))
                {
                    // Get the bounds.
                    double xmin = double.Parse(txtXmin.Text) * Math.PI;
                    double xmax = double.Parse(txtXmax.Text) * Math.PI;
                    double ymin = double.Parse(txtYmin.Text);
                    double ymax = double.Parse(txtYmax.Text);

                    // Scale to make the area fit the PictureBox.
                    RectangleF world_coords = new RectangleF((float)xmin, (float)ymax, (float)(xmax - xmin), (float)(ymin - ymax));
                    PointF[] device_coords =
                    {
                        new PointF(0, 0),
                        new PointF(pictureBox1.ClientSize.Width, 0),
                        new PointF(0, pictureBox1.ClientSize.Height),
                    };
                    gr.Transform = new Matrix(world_coords, device_coords);

                    // Draw the X-axis.
                    // Start at the multiple of Pi < xmin.
                    double start_x = Math.PI * ((int)(xmin - 1));
                    gr.DrawLine(thin_pen, (float)xmin, 0, (float)xmax, 0);

                    float dy = (float)((ymax - ymin) / 30.0);
                    for (double x = start_x; x <= xmax; x += Math.PI)
                    {
                        gr.DrawLine(thin_pen, (float)x, -2 * dy, (float)x, 2 * dy);
                    }
                    for (double x = start_x + Math.PI / 2.0; x <= xmax; x += Math.PI)
                    {
                        gr.DrawLine(thin_pen, (float)x, -dy, (float)x, dy);
                    }

                    // Draw the Y-axis.
                    // Start at the multiple of 1 < ymin.
                    double start_y = (int)ymin - 1;
                    gr.DrawLine(thin_pen, 0, (float)ymin, 0, (float)ymax);

                    float dx = (float)((xmax - xmin) / 60.0);
                    for (double y = start_y; y <= ymax; y += 1.0)
                    {
                        gr.DrawLine(thin_pen, -2 * dx, (float)y, 2 * dx, (float)y);
                    }
                    for (double y = start_y + 0.5; y <= ymax; y += 1.0)
                    {
                        gr.DrawLine(thin_pen, -dx, (float)y, dx, (float)y);
                    }

                    // Draw vertical asymptotes.
                    thin_pen.DashPattern = new float[] { 5, 5 };
                    for (double x = start_x + Math.PI / 2.0; x <= xmax; x += Math.PI)
                    {
                        gr.DrawLine(thin_pen, (float)x, (float)ymin, (float)x, (float)ymax);
                    }

                    // Draw horizontal limits for sine and cosine.
                    gr.DrawLine(thin_pen, (float)xmin, 1, (float)xmax, 1);
                    gr.DrawLine(thin_pen, (float)xmin, -1, (float)xmax, -1);
                    thin_pen.DashStyle = DashStyle.Solid;

                    // See how big a pixel is before scaling.
                    Matrix inverse = gr.Transform;
                    inverse.Invert();
                    PointF[] pixel_pts =
                    {
                        new PointF(0, 0),
                        new PointF(1, 0),
                    };
                    inverse.TransformPoints(pixel_pts);
                    dx = pixel_pts[1].X - pixel_pts[0].X;

                    // Sine.
                    List<PointF> sine_points = new List<PointF>();
                    for (float x = (float)xmin; x <= xmax; x += dx)
                    {
                        sine_points.Add(new PointF(x, (float)Math.Sin(x)));
                    }
                    thin_pen.Color = Color.Red;
                    gr.DrawLines(thin_pen, sine_points.ToArray());

                    // Cosine.
                    List<PointF> cosine_points = new List<PointF>();
                    for (float x = (float)xmin; x <= xmax; x += dx)
                    {
                        cosine_points.Add(new PointF(x, (float)Math.Cos(x)));
                    }
                    thin_pen.Color = Color.Green;
                    gr.DrawLines(thin_pen, cosine_points.ToArray());

                    // Tangent.
                    List<PointF> tangent_points = new List<PointF>();
                    double old_value = Math.Tan(xmin);
                    thin_pen.Color = Color.Blue;
                    for (float x = (float)xmin; x <= xmax; x += dx)
                    {
                        // See if we're at a discontinuity.
                        double new_value = Math.Tan(x);
                        if ((Math.Abs(new_value - old_value) > 10) && (Math.Sign(new_value) != Math.Sign(old_value)))
                        {
                            if (tangent_points.Count > 1)
                            {
                                gr.DrawLines(thin_pen, tangent_points.ToArray());
                            }
                            tangent_points = new List<PointF>();
                        }
                        else
                        {
                            tangent_points.Add(new PointF(x, (float)Math.Tan(x)));
                        }
                    }
                    if (tangent_points.Count > 1)
                    {
                        gr.DrawLines(thin_pen, tangent_points.ToArray());
                    }
                }
            }
            pictureBox1.Image = GraphImage;
        }

        //畫三角函數 SP

        //------------------------------------------------------------  # 60個

        //#region 常態分佈
        private void btnDraw_Click(object sender, EventArgs e)
        {
            float mean = float.Parse(txtMean.Text);
            float stddev = float.Parse(txtStdDev.Text);
            float var = stddev * stddev;

            // Make a bitmap.
            Bitmap bm = new Bitmap(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.SmoothingMode = SmoothingMode.AntiAlias;

                // Define the mapping from world
                // coordinates onto the PictureBox.
                const float wxmin = -5.1f;
                const float wymin = -0.2f;
                const float wxmax = -wxmin;
                const float wymax = 1.1f;
                const float wwid = wxmax - wxmin;
                const float whgt = wymax - wymin;
                RectangleF world = new RectangleF(wxmin, wymin, wwid, whgt);
                PointF[] device_points =
                {
                    new PointF(0, pictureBox1.ClientSize.Height),
                    new PointF(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height),
                    new PointF(0, 0),
                };
                Matrix transform = new Matrix(world, device_points);

                // Make a thin Pen to use.
                using (Pen pen = new Pen(Color.Red, 0))
                {
                    using (Font font = new Font("Arial", 8))
                    {
                        // Draw the X axis.
                        gr.Transform = transform;
                        pen.Color = Color.Black;
                        gr.DrawLine(pen, wxmin, 0, wxmax, 0);
                        for (int x = (int)wxmin; x <= wxmax; x++)
                        {
                            gr.DrawLine(pen, x, -0.05f, x, 0.05f);
                            gr.DrawLine(pen, x + 0.25f, -0.025f, x + 0.25f, 0.025f);
                            gr.DrawLine(pen, x + 0.50f, -0.025f, x + 0.50f, 0.025f);
                            gr.DrawLine(pen, x + 0.75f, -0.025f, x + 0.75f, 0.025f);
                        }

                        // Label the X axis.
                        gr.Transform = new Matrix();
                        gr.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;
                        List<PointF> ints = new List<PointF>();
                        for (int x = (int)wxmin; x <= wxmax; x++)
                        {
                            ints.Add(new PointF(x, -0.07f));
                        }
                        PointF[] ints_array = ints.ToArray();
                        transform.TransformPoints(ints_array);

                        using (StringFormat sf = new StringFormat())
                        {
                            sf.Alignment = StringAlignment.Center;
                            sf.LineAlignment = StringAlignment.Near;
                            int index = 0;
                            for (int x = (int)wxmin; x <= wxmax; x++)
                            {
                                gr.DrawString(x.ToString(), font, Brushes.Black, ints_array[index++], sf);
                            }
                        }

                        // Draw the Y axis.
                        gr.Transform = transform;
                        pen.Color = Color.Black;
                        gr.DrawLine(pen, 0, wymin, 0, wymax);
                        for (int y = (int)wymin; y <= wymax; y++)
                        {
                            gr.DrawLine(pen, -0.2f, y, 0.2f, y);
                            gr.DrawLine(pen, -0.1f, y + 0.25f, 0.1f, y + 0.25f);
                            gr.DrawLine(pen, -0.1f, y + 0.50f, 0.1f, y + 0.50f);
                            gr.DrawLine(pen, -0.1f, y + 0.75f, 0.1f, y + 0.75f);
                        }

                        // Label the Y axis.
                        gr.Transform = new Matrix();
                        gr.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;
                        ints = new List<PointF>();
                        for (float y = 0.25f; y < 1.01; y += 0.25f)
                        {
                            ints.Add(new PointF(0.2f, y));
                        }
                        ints_array = ints.ToArray();
                        transform.TransformPoints(ints_array);

                        using (StringFormat sf = new StringFormat())
                        {
                            sf.Alignment = StringAlignment.Near;
                            sf.LineAlignment = StringAlignment.Center;
                            int index = 0;
                            foreach (float y in new float[] { 0.25f, 0.5f, 0.75f, 1.0f })
                            {
                                gr.DrawString(y.ToString("0.00"), font, Brushes.Black, ints_array[index++], sf);
                            }
                        }

                        // Draw the curve.
                        gr.Transform = transform;
                        List<PointF> points = new List<PointF>();
                        float one_over_2pi = (float)(1.0 / (stddev * Math.Sqrt(2 * Math.PI)));

                        float dx = (wxmax - wxmin) / pictureBox1.ClientSize.Width;
                        for (float x = wxmin; x <= wxmax; x += dx)
                        {
                            float y = F_normal2(x, one_over_2pi, mean, stddev, var);
                            points.Add(new PointF(x, y));
                        }
                        pen.Color = Color.Red;
                        gr.DrawLines(pen, points.ToArray());
                    } // Font
                } // Pen

                pictureBox1.Image = bm;
            }
        }

        // The normal distribution function.
        private float F_normal2(float x, float one_over_2pi, float mean, float stddev, float var)
        {
            return (float)(one_over_2pi * Math.Exp(-(x - mean) * (x - mean) / (2 * var)));
        }

        //#endregion 常態分佈

        //------------------------------------------------------------  # 60個

        // Return true if the number is not infinity or NaN.
        private bool IsNumber(float number)
        {
            return !(float.IsNaN(number) || float.IsInfinity(number));
        }

        // Calculate Polynomial(x)  Polynomial(x) = ax^4+bx^3+cx^2+dx+e
        private float Polynomial(float x, float A, float B, float C, float D, float E)
        {
            float result;
            result = A * x * x * x * x + B * x * x * x + C * x * x + D * x + E;
            return result;
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //畫多項式
            float A;
            float B;
            float C;
            float D;
            float E;

            // Calculate Polynomial(x)  Polynomial(x) = ax^4+bx^3+cx^2+dx+e
            A = 0;
            B = 0;
            C = 1;
            D = 0;
            E = 0;

            // Get the X coordinate bounds.
            float xmin = -10;
            float xmax = 10;
            float ymin = 100;
            float ymax = 0;

            float x_tick = 1;

            // Get points for the negative root on the left.
            List<PointF> points = new List<PointF>();
            float xmid1 = xmax;

            for (float x = xmin; x <= xmax; x += x_tick)
            {
                //float y = G1(x, A, B, C, D, E, F, -1f);
                float y = Polynomial(x, A, B, C, D, E);
                if (!IsNumber(y))
                {
                    xmid1 = x - 1;
                    break;
                }
                points.Add(new PointF(x, y));
            }

            int len = points.Count;
            richTextBox1.Text += "len = " + len.ToString() + "\n";

            for (int i = 0; i < len; i++)
            {
                if (points[i].Y > ymax)
                    ymax = points[i].Y;
                else if (points[i].Y < ymin)
                    ymin = points[i].Y;
                //richTextBox1.Text += "i = " + i.ToString() + "\tx = " + points[i].X.ToString() + "\ty = " + points[i].Y.ToString() + "\n";
            }
            richTextBox1.Text += "ymax = " + ymax.ToString() + "\n";
            richTextBox1.Text += "ymin = " + ymin.ToString() + "\n";

            int x_ratio = 1;
            int y_ratio = 1;
            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;

            x_ratio = (int)(W / (xmax - xmin));
            richTextBox1.Text += "x_ratio = " + x_ratio.ToString() + "\n";
            //x_ratio -= 10;    //to see the boundary

            y_ratio = (int)(H / (ymax - ymin));
            richTextBox1.Text += "y_ratio = " + y_ratio.ToString() + "\n";

            Bitmap bitmap1 = new Bitmap(W, H);
            using (Graphics g = Graphics.FromImage(bitmap1))
            {
                g.Clear(Color.White);
                g.SmoothingMode = SmoothingMode.AntiAlias;

                // Draw the curves.
                using (Pen thick_pen = new Pen(Color.Red, 2))
                {
                    for (int i = 0; i < len; i++)
                    {
                        points[i] = new PointF((points[i].X + 10) * x_ratio, H - (points[i].Y) * y_ratio);
                    }

                    thick_pen.Color = Color.Red;
                    if (points.Count > 1)
                        g.DrawLines(thick_pen, points.ToArray());
                }
            }
            // Display the result.
            pictureBox1.Image = bitmap1;
        }

        //------------------------------------------------------------  # 60個

        private void button1_Click(object sender, EventArgs e)
        {
            //畫XY平面
            Graphics g;
            Pen p;
            SolidBrush sb;
            Bitmap bitmap1;

            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;

            //----開新的Bitmap----
            bitmap1 = new Bitmap(W, H);
            //----使用上面的Bitmap畫圖----
            g = Graphics.FromImage(bitmap1);

            p = new Pen(Color.Red, 10);     // 設定畫筆為紅色、粗細為 10 點。
            sb = new SolidBrush(Color.Blue);

            g.Clear(Color.White);

            float ratio_x, ratio_y;
            float w, h;
            float x0, x1, y0, y1;

            //----畫筆顏色----
            p = new Pen(Color.Black);
            sb = new SolidBrush(p.Color);
            //----取得picturebox寬度與高度----
            w = pictureBox1.Width;
            h = pictureBox1.Height;
            //----是否有上一次的圖片，如果有就清除----
            if (pictureBox1.Image != null)
                pictureBox1.Image = null;
            //if (bitmap1 != null)
            //  bitmap1.Dispose();
            //----轉換使用者輸入的資料----
            x0 = (float)10;
            y0 = (float)10;
            x1 = (float)-5;
            y1 = (float)-9;
            //----計算放大倍率----
            ratio_x = (w - 50) / 20;
            ratio_y = (h - 50) / 20;
            //----開新的Bitmap----
            bitmap1 = new Bitmap((int)w, (int)h);
            //----使用上面的Bitmap畫圖----
            g = Graphics.FromImage(bitmap1);
            //----清除Bitmap為某顏色----
            g.Clear(Color.White);
            //----更改原點位置----
            g.TranslateTransform(pictureBox1.Width / 2, pictureBox1.Height / 2);
            //----畫坐標軸----
            g.DrawLine(p, -1000, 0, 1000, 0);//x軸
            g.DrawLine(p, 0, -1000, 0, 1000);//y軸
            g.DrawString("X", this.Font, sb, w / 2 - 20, 20);
            g.DrawString("Y", this.Font, sb, 20, -h / 2);
            g.DrawLine(p, w / 2, 0, w / 2 - 10, 5);//x軸箭頭
            g.DrawLine(p, w / 2, 0, w / 2 - 10, -5);
            g.DrawLine(p, 0, -h / 2, 5, -h / 2 + 10);//y軸箭頭
            g.DrawLine(p, 0, -h / 2, -5, -h / 2 + 10);
            for (int i = -10; i <= 10; i++)//畫X Y軸座標位置
            {
                g.DrawLine(p, i * ratio_x, -5, i * ratio_x, 5);
                g.DrawString(i.ToString().PadLeft(2, ' '), this.Font, sb, i * ratio_x - 9, 10);
                g.DrawLine(p, -5, i * ratio_y, 5, i * ratio_y);
                if (i != 0)
                    g.DrawString(i.ToString(), this.Font, sb, 15, i * ratio_y - 8);
            }
            //----換顏色----
            p = new Pen(Color.Red);
            sb = new SolidBrush(p.Color);
            //----畫線----
            g.DrawLine(p, x0 * ratio_x, -y0 * ratio_y, x1 * ratio_x, -y1 * ratio_y);
            //----畫兩點----
            g.FillEllipse(sb, new RectangleF(x0 * ratio_x - 2.5f, -y0 * ratio_y - 2.5f, 5, 5));
            g.FillEllipse(sb, new RectangleF(x1 * ratio_x - 2.5f, -y1 * ratio_y - 2.5f, 5, 5));
            //----釋放Graphics資源----
            //g.Dispose();
            //----將Bitmap顯示在Picture上
            g.ResetTransform();
            pictureBox1.Image = bitmap1;
        }

        //------------------------------------------------------------  # 60個

        private void button2_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        double theta = 0;// 徑度 (一圈為 Math.PI * 2)
        double r; // 半徑
        int x1, x2, y1, y2; //直線的兩個點
        bool First = true;//定義第一點 (通常不畫)
        Graphics G;// 畫布
        int a, b;// 方程式的 參數
        Pen MyPen = new Pen(Color.Black, 3);  //黑色筆 寬為 3

        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {

        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            label4.Text = comboBox1.Text.ToString();
            this.Invalidate();
            this.pictureBox2.Invalidate();
            timer1.Enabled = true;
            theta = 0;
            First = true;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            theta = theta + 0.01;

            if (comboBox1.Text == "")
            {
                timer1.Enabled = false;
                label4.Text = "";
                return;
            }
            else if (comboBox1.Text == "Circle")
            {
                if (theta >= Math.PI * 2)
                {
                    timer1.Enabled = false;
                    label4.Text = "";
                }
                r = pictureBox2.Height / 4;
                x2 = pictureBox2.Width / 2 + (int)(r * Math.Cos(theta));
                y2 = pictureBox2.Height / 2 + (int)(r * Math.Sin(theta));
            }
            else if (comboBox1.Text == "Limacon")  // 帕斯卡蝸線
            {
                if (theta >= Math.PI * 2)
                {
                    timer1.Enabled = false;
                    label4.Text = "";
                }
                a = 200;
                b = 100;
                r = a * Math.Cos(theta - Math.PI / 2) + b;
                x2 = pictureBox2.Width / 2 + (int)(r * Math.Cos(theta));
                y2 = pictureBox2.Height / 4 + (int)(r * Math.Sin(theta));
            }
            else if (comboBox1.Text == "Cardiod")
            {
                if (theta >= Math.PI * 2)
                {
                    timer1.Enabled = false;
                    label4.Text = "";
                }
                a = 200;// b = 50;
                r = a * Math.Cos(theta - Math.PI / 2) + a;
                x2 = pictureBox2.Width / 2 + (int)(r * Math.Cos(theta));
                y2 = pictureBox2.Height / 4 + (int)(r * Math.Sin(theta));
            }
            else if (comboBox1.Text == "Three Left")
            {
                if (theta >= Math.PI)
                {
                    timer1.Enabled = false;
                    label4.Text = "";
                }
                a = 275;
                r = a * Math.Cos(3.0 * theta);
                x2 = pictureBox2.Width / 2 + (int)(r * Math.Cos(theta));
                y2 = pictureBox2.Height / 2 + (int)(r * Math.Sin(theta));
            }
            else if (comboBox1.Text == "Four Left")
            {
                if (theta >= Math.PI * 2)
                {
                    timer1.Enabled = false;
                    label4.Text = "";
                }
                a = 275;
                r = a * Math.Cos(2.0 * theta);
                x2 = pictureBox2.Width / 2 + (int)(r * Math.Cos(theta));
                y2 = pictureBox2.Height / 2 + (int)(r * Math.Sin(theta));
            }
            else if (comboBox1.Text == "Spiral")
            {
                if (theta >= Math.PI * 20)
                {
                    timer1.Enabled = false;
                    label4.Text = "";
                }
                a = 175;
                r = a / 40.0 * theta;
                x2 = pictureBox2.Width / 2 + (int)(r * Math.Cos(theta));
                y2 = pictureBox2.Height / 2 + (int)(r * Math.Sin(theta));
            }

            if (First)
            {
                First = !First;
            }
            else
            {
                G.DrawLine(MyPen, x1, y1, x2, y2);
            }
            x1 = x2;
            y1 = y2;
        }


    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個


