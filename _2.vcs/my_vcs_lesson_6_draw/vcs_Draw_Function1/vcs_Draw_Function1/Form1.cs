using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;  // for PixelFormat
using System.Drawing.Drawing2D;
using System.Drawing.Text;  // for TextRenderingHint

namespace vcs_Draw_Function1
{
    public partial class Form1 : Form
    {
        double theta = 0;// 徑度 (一圈為 Math.PI * 2)
        double r; // 半徑
        int x1, x2, y1, y2; //直線的兩個點
        bool First = true;//定義第一點 (通常不畫)
        Graphics g;  // 畫布
        int a, b;  // 方程式的 參數
        Pen MyPen = new Pen(Color.Black, 3);  //黑色筆 寬為 3

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            label4.Text = "";
            //this.ClientSize = new Size(800, 600);
            g = this.pictureBox2.CreateGraphics();
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
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            groupBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            groupBox2.Location = new Point(x_st + dx * 1, y_st + dy * 1 + 40);
            groupBox3.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            label4.Location = new Point(x_st + dx * 4 - 30, y_st + dy * 0);

            pictureBox1.Size = new Size(720, 480);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            pictureBox2.Size = new Size(300 + 100, 300 + 100);
            pictureBox2.Location = new Point(x_st + dx * 4 + 100, y_st + dy * 0);

            comboBox1.Location = new Point(x_st + dx * 4 + 100, y_st + dy * 0);
            richTextBox1.Size = new Size(300 + 100, 250);
            richTextBox1.Location = new Point(x_st + dx * 4 + 100, y_st + dy * 0 + 420);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1400, 750);
            this.Text = "vcs_Draw_Function1";

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

        private void bt_draw1_Click(object sender, EventArgs e)
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
            Bitmap bmp = new Bitmap(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height);
            Graphics g = Graphics.FromImage(bmp);
            g.SmoothingMode = SmoothingMode.AntiAlias;

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
            Pen p = new Pen(Color.Red, 0);
            Font f = new Font("Arial", 8);
            // Draw the X axis.
            g.Transform = transform;
            p.Color = Color.Black;
            g.DrawLine(p, wxmin, 0, wxmax, 0);
            for (int x = (int)wxmin - 1; x <= wxmax; x++)
            {
                g.DrawLine(p, x, -tick_dy * 2, x, tick_dy * 2);
                g.DrawLine(p, x + 0.25f, -tick_dy, x + 0.25f, tick_dy);
                g.DrawLine(p, x + 0.50f, -tick_dy, x + 0.50f, tick_dy);
                g.DrawLine(p, x + 0.75f, -tick_dy, x + 0.75f, tick_dy);
            }

            // Label the X axis.
            g.Transform = new Matrix();
            g.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;
            List<PointF> ints = new List<PointF>();
            for (int x = (int)wxmin; x <= wxmax; x++)
            {
                ints.Add(new PointF(x, -2 * tick_dy));
            }
            PointF[] ints_array = ints.ToArray();
            transform.TransformPoints(ints_array);

            StringFormat sf = new StringFormat();
            sf.Alignment = StringAlignment.Center;
            sf.LineAlignment = StringAlignment.Near;
            int index = 0;
            for (int x = (int)wxmin; x <= wxmax; x++)
            {
                g.DrawString(x.ToString(), f, Brushes.Black, ints_array[index++], sf);
            }

            // Draw the Y axis.
            g.Transform = transform;
            p.Color = Color.Black;
            g.DrawLine(p, 0, wymin, 0, wymax);
            for (int y = (int)wymin - 1; y <= wymax; y++)
            {
                g.DrawLine(p, -tick_dx * 2, y, tick_dx * 2, y);
                g.DrawLine(p, -tick_dx, y + 0.25f, tick_dx, y + 0.25f);
                g.DrawLine(p, -tick_dx, y + 0.50f, tick_dx, y + 0.50f);
                g.DrawLine(p, -tick_dx, y + 0.75f, tick_dx, y + 0.75f);
            }

            // Label the Y axis.
            g.Transform = new Matrix();
            g.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;
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

            sf = new StringFormat();
            sf.Alignment = StringAlignment.Near;
            sf.LineAlignment = StringAlignment.Center;
            index = 0;
            for (float y = 0.25f; y < wymax; y += 0.25f)
            {
                g.DrawString(y.ToString("0.00"), f, Brushes.Black, ints_array[index++], sf);
            }

            // Draw the curve.
            g.Transform = transform;
            List<PointF> points = new List<PointF>();

            float dx = (wxmax - wxmin) / pictureBox1.ClientSize.Width;
            for (float x = wxmin; x <= wxmax; x += dx)
            {
                float y = F_normal1(x, one_over_2pi, mean, stddev, var);
                points.Add(new PointF(x, y));
            }
            p.Color = Color.Red;
            g.DrawLines(p, points.ToArray());
            return bmp;
        }

        //------------------------------------------------------------  # 60個

        //畫三角函數 ST
        // The image used for the graph.
        private Bitmap GraphImage;

        private void bt_draw3_Click(object sender, EventArgs e)
        {
            GraphImage = new Bitmap(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height);
            Graphics g = Graphics.FromImage(GraphImage);
            g.Clear(Color.White);
            g.SmoothingMode = SmoothingMode.AntiAlias;

            Pen thin_pen = new Pen(Color.Purple, 0);
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
            g.Transform = new Matrix(world_coords, device_coords);

            // Draw the X-axis.
            // Start at the multiple of Pi < xmin.
            double start_x = Math.PI * ((int)(xmin - 1));
            g.DrawLine(thin_pen, (float)xmin, 0, (float)xmax, 0);

            float dy = (float)((ymax - ymin) / 30.0);
            for (double x = start_x; x <= xmax; x += Math.PI)
            {
                g.DrawLine(thin_pen, (float)x, -2 * dy, (float)x, 2 * dy);
            }
            for (double x = start_x + Math.PI / 2.0; x <= xmax; x += Math.PI)
            {
                g.DrawLine(thin_pen, (float)x, -dy, (float)x, dy);
            }

            // Draw the Y-axis.
            // Start at the multiple of 1 < ymin.
            double start_y = (int)ymin - 1;
            g.DrawLine(thin_pen, 0, (float)ymin, 0, (float)ymax);

            float dx = (float)((xmax - xmin) / 60.0);
            for (double y = start_y; y <= ymax; y += 1.0)
            {
                g.DrawLine(thin_pen, -2 * dx, (float)y, 2 * dx, (float)y);
            }
            for (double y = start_y + 0.5; y <= ymax; y += 1.0)
            {
                g.DrawLine(thin_pen, -dx, (float)y, dx, (float)y);
            }

            // Draw vertical asymptotes.
            thin_pen.DashPattern = new float[] { 5, 5 };
            for (double x = start_x + Math.PI / 2.0; x <= xmax; x += Math.PI)
            {
                g.DrawLine(thin_pen, (float)x, (float)ymin, (float)x, (float)ymax);
            }

            // Draw horizontal limits for sine and cosine.
            g.DrawLine(thin_pen, (float)xmin, 1, (float)xmax, 1);
            g.DrawLine(thin_pen, (float)xmin, -1, (float)xmax, -1);
            thin_pen.DashStyle = DashStyle.Solid;

            // See how big a pixel is before scaling.
            Matrix inverse = g.Transform;
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
            g.DrawLines(thin_pen, sine_points.ToArray());

            // Cosine.
            List<PointF> cosine_points = new List<PointF>();
            for (float x = (float)xmin; x <= xmax; x += dx)
            {
                cosine_points.Add(new PointF(x, (float)Math.Cos(x)));
            }
            thin_pen.Color = Color.Green;
            g.DrawLines(thin_pen, cosine_points.ToArray());

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
                        g.DrawLines(thin_pen, tangent_points.ToArray());
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
                g.DrawLines(thin_pen, tangent_points.ToArray());
            }
            pictureBox1.Image = GraphImage;
        }

        //畫三角函數 SP

        //------------------------------------------------------------  # 60個

        //#region 常態分佈

        private void bt_draw2_Click(object sender, EventArgs e)
        {
            float mean = float.Parse(txtMean.Text);
            float stddev = float.Parse(txtStdDev.Text);
            float var = stddev * stddev;

            Bitmap bmp = new Bitmap(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height);
            Graphics g = Graphics.FromImage(bmp);
            g.SmoothingMode = SmoothingMode.AntiAlias;

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

            Pen p = new Pen(Color.Red, 0);
            Font f = new Font("Arial", 8);
            // Draw the X axis.
            g.Transform = transform;
            p.Color = Color.Black;
            g.DrawLine(p, wxmin, 0, wxmax, 0);
            for (int x = (int)wxmin; x <= wxmax; x++)
            {
                g.DrawLine(p, x, -0.05f, x, 0.05f);
                g.DrawLine(p, x + 0.25f, -0.025f, x + 0.25f, 0.025f);
                g.DrawLine(p, x + 0.50f, -0.025f, x + 0.50f, 0.025f);
                g.DrawLine(p, x + 0.75f, -0.025f, x + 0.75f, 0.025f);
            }

            // Label the X axis.
            g.Transform = new Matrix();
            g.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;
            List<PointF> ints = new List<PointF>();
            for (int x = (int)wxmin; x <= wxmax; x++)
            {
                ints.Add(new PointF(x, -0.07f));
            }
            PointF[] ints_array = ints.ToArray();
            transform.TransformPoints(ints_array);

            StringFormat sf = new StringFormat();
            sf.Alignment = StringAlignment.Center;
            sf.LineAlignment = StringAlignment.Near;
            int index = 0;
            for (int x = (int)wxmin; x <= wxmax; x++)
            {
                g.DrawString(x.ToString(), f, Brushes.Black, ints_array[index++], sf);
            }

            // Draw the Y axis.
            g.Transform = transform;
            p.Color = Color.Black;
            g.DrawLine(p, 0, wymin, 0, wymax);
            for (int y = (int)wymin; y <= wymax; y++)
            {
                g.DrawLine(p, -0.2f, y, 0.2f, y);
                g.DrawLine(p, -0.1f, y + 0.25f, 0.1f, y + 0.25f);
                g.DrawLine(p, -0.1f, y + 0.50f, 0.1f, y + 0.50f);
                g.DrawLine(p, -0.1f, y + 0.75f, 0.1f, y + 0.75f);
            }

            // Label the Y axis.
            g.Transform = new Matrix();
            g.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;
            ints = new List<PointF>();
            for (float y = 0.25f; y < 1.01; y += 0.25f)
            {
                ints.Add(new PointF(0.2f, y));
            }
            ints_array = ints.ToArray();
            transform.TransformPoints(ints_array);

            sf = new StringFormat();
            sf.Alignment = StringAlignment.Near;
            sf.LineAlignment = StringAlignment.Center;
            index = 0;
            foreach (float y in new float[] { 0.25f, 0.5f, 0.75f, 1.0f })
            {
                g.DrawString(y.ToString("0.00"), f, Brushes.Black, ints_array[index++], sf);
            }

            // Draw the curve.
            g.Transform = transform;
            List<PointF> points = new List<PointF>();
            float one_over_2pi = (float)(1.0 / (stddev * Math.Sqrt(2 * Math.PI)));

            float dx = (wxmax - wxmin) / pictureBox1.ClientSize.Width;
            for (float x = wxmin; x <= wxmax; x += dx)
            {
                float y = F_normal2(x, one_over_2pi, mean, stddev, var);
                points.Add(new PointF(x, y));
            }
            p.Color = Color.Red;
            g.DrawLines(p, points.ToArray());
            pictureBox1.Image = bmp;
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
            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);
            g.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the curves.
            Pen thick_pen = new Pen(Color.Red, 2);
            for (int i = 0; i < len; i++)
            {
                points[i] = new PointF((points[i].X + 10) * x_ratio, H - (points[i].Y) * y_ratio);
            }

            thick_pen.Color = Color.Red;
            if (points.Count > 1)
            {
                g.DrawLines(thick_pen, points.ToArray());
            }

            pictureBox1.Image = bitmap1;
        }

        //------------------------------------------------------------  # 60個

        private void button1_Click(object sender, EventArgs e)
        {
            //畫XY平面
            //輸入兩點並劃出直線

            // X,Y顯示範圍為-10~10
            Random rand = new Random();
            float x0 = (float)rand.Next(-100, 100) / 10;
            float y0 = (float)rand.Next(-100, 100) / 10;
            float x1 = (float)rand.Next(-100, 100) / 10;
            float y1 = (float)rand.Next(-100, 100) / 10;

            //----畫筆顏色----
            Pen p = new Pen(Color.Black);
            SolidBrush sb = new SolidBrush(p.Color);
            //----取得picturebox寬度與高度----
            float w = pictureBox1.Width;
            float h = pictureBox1.Height;

            //----計算放大倍率----
            float ratio_x = (w - 50) / 20;
            float ratio_y = (h - 50) / 20;

            //----開新的Bitmap----
            Bitmap bitmap1 = new Bitmap((int)w, (int)h);

            //----使用上面的Bitmap畫圖----
            Graphics g = Graphics.FromImage(bitmap1);

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
            g.Dispose();

            pictureBox1.Image = bitmap1;
        }

        //------------------------------------------------------------  # 60個

        private float F(float x)
        {
            //return (float)((1 / x + 1 / (x + 1) - 2 * x * x) / 10);
            //return (float)Math.Sin(Math.PI * x);  // sine
            return (float)(10 * Math.Sin(Math.PI * x) / (Math.PI * x));  // sinc
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //畫Sinc 1
            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;
            Bitmap bitmap1 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap1);
            g.ResetTransform();  // 重置轉換, 恢復
            g.SmoothingMode = SmoothingMode.AntiAlias;
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;

            //畫Sinc

            // Transform to map the graph bounds to the Bitmap.
            // The bounds to draw.
            float xmin = -5;
            float xmax = 5;
            float ymin = -5;
            float ymax = 12;
            RectangleF rect = new RectangleF(xmin, ymin, xmax - xmin, ymax - ymin);
            g.DrawRectangle(Pens.Red, rect.X, rect.Y, rect.Width, rect.Height);
            richTextBox1.Text += rect.ToString() + "\n";

            PointF[] pts = 
            {
                new PointF(0, H),  // 左上
                new PointF(W, H),  // 右上
                new PointF(0, 0),  // 左下
            };

            // 轉置矩陣 mtx, 矩形範圍 轉 平行四邊形範圍
            Matrix mtx = new Matrix(rect, pts);
            g.Transform = mtx;  // 設定仿射矩陣, 矩陣轉置

            // Draw the graph.
            Pen p = new Pen(Color.Blue, 0);
            // Draw the axes.
            g.DrawLine(p, xmin, 0, xmax, 0);
            g.DrawLine(p, 0, ymin, 0, ymax);
            for (int x = (int)xmin; x <= xmax; x++)
            {
                g.DrawLine(p, x, -0.1f, x, 0.1f);
            }
            for (int y = (int)ymin; y <= ymax; y++)
            {
                g.DrawLine(p, -0.1f, y, 0.1f, y);
            }
            p.Color = Color.Red;

            // See how big 1 pixel is horizontally.
            Matrix inverse = g.Transform;
            inverse.Invert();

            PointF[] pixel_pts =
            {
                new PointF(0, 0),
                new PointF(1, 0)
            };
            inverse.TransformPoints(pixel_pts);

            float dx = pixel_pts[1].X - pixel_pts[0].X;
            dx /= 2;

            List<PointF> points = new List<PointF>();
            for (float x = xmin; x <= xmax; x += dx)
            {
                bool valid_point = false;
                try
                {
                    // Get the next point.
                    float y = F(x);

                    // If the slope is reasonable, this is a valid point.
                    if (points.Count == 0)
                    {
                        valid_point = true;
                    }
                    else
                    {
                        float dy = y - points[points.Count - 1].Y;
                        if (Math.Abs(dy / dx) < 1000)
                        {
                            valid_point = true;
                        }
                    }
                    if (valid_point)
                    {
                        points.Add(new PointF(x, y));
                    }
                }
                catch
                {
                }

                // If the new point is invalid, draw
                // the points in the latest batch.
                if (!valid_point)
                {
                    if (points.Count > 1)
                    {
                        g.DrawLines(p, points.ToArray());
                    }
                    points.Clear();
                }
            }

            // Draw the last batch of points.
            if (points.Count > 1)
            {
                g.DrawLines(p, points.ToArray());
            }

            pictureBox1.Image = bitmap1;
        }

        //------------------------------------------------------------  # 60個

        bool flag_grid_on = true;

        private float f_sin(float x)
        {
            return (float)(0f - Math.Sin(Math.PI * x));
        }

        private float f_sinc(float x)
        {
            if (x == 0f)
            {
                return 0;
            }
            else
            {
                return (0f - ((float)(Math.Sin(Math.PI * x) / (Math.PI * x))));
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //畫Sinc 2
            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;
            Bitmap bitmap1 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap1);
            g.ResetTransform();  // 重置轉換, 恢復
            g.SmoothingMode = SmoothingMode.AntiAlias;
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;

            //畫Sinc

            List<PointF> points1 = new List<PointF>();
            List<PointF> points2 = new List<PointF>();

            double xmin = -5;
            double xmax = 5;
            double ymin = -1;
            double ymax = 1;

            float ratio_x = 100f;
            float ratio_y = 100f;
            float offset_x = 5.0f;
            float offset_y = 1.0f;

            // 來源矩形, 矩形範圍 src_rect
            int sx = -5;
            int sy = -1;
            int sw = 10;
            int sh = 2;
            Rectangle src_rect = new Rectangle(sx, sy, sw, sh);

            // 欲映射的繪圖範圍, 目標矩形, 平行四邊形範圍 dst_rect
            int dx = 0;
            int dy = 0;
            int dw = 500;
            int dh = 200;
            Rectangle dst_rect = new Rectangle(dx, dy, dw, dh);
            Point[] dst_points1 = new Point[]
            {
                new Point(dx, dy),  // 左上
                new Point(dx + dw, dy),  // 右上
                new Point(dx, dy + dh),  // 左下
            };

            // 轉置矩陣 mtx, 矩形範圍 轉 平行四邊形範圍
            Matrix mtx = new Matrix(src_rect, dst_points1);
            g.Transform = mtx;  // 設定仿射矩陣, 矩陣轉置

            float xx;
            float yy1;
            float yy2;
            int dd = 2;  // sinc 圖下移的距離
            for (float x = (float)xmin; x <= xmax; x += 0.1f)
            {
                xx = x;
                yy1 = f_sin(x);
                yy2 = f_sinc(x) + dd;

                points1.Add(new PointF(xx, yy1));
                points2.Add(new PointF(xx, yy2));
            }

            Pen thin_pen = new Pen(Color.Purple, 0);
            thin_pen.Color = Color.Red;
            g.DrawLines(thin_pen, points1.ToArray());

            thin_pen.Color = Color.Green;
            g.DrawLines(thin_pen, points2.ToArray());

            Pen grayPen = new Pen(Color.LightGray, 0);

            for (float x = (float)xmin; x <= xmax; x += 1.0f)
            {
                xx = x;
                yy1 = 0;
                if (x == 0)
                {
                    yy2 = 1;
                }
                else
                {
                    yy2 = 2;
                }
                g.FillEllipse(Brushes.Green, xx - 0.1f, yy1 - 0.1f, 0.2f, 0.2f);
                g.FillEllipse(Brushes.Green, xx - 0.1f, yy2 - 0.1f, 0.2f, 0.2f);
            }

            if (flag_grid_on == true)
            {
                for (float x = (float)xmin; x <= xmax; x += 1.0f)
                {
                    //直線
                    g.DrawLine(grayPen, x, -1, x, 3);  // 垂直線
                }
                for (float yy = -1.0f; yy <= 3.0f; yy += 0.5f)
                {
                    //橫線
                    g.DrawLine(grayPen, -5.0f, yy, 5.0f, yy);  // 水平線
                }
            }

            Pen p = new Pen(Color.Blue, 0);
            g.DrawRectangle(p, -5, -1, 10, 2);
            g.DrawRectangle(p, -5, -1 + dd, 10, 2);

            Pen blackPen = new Pen(Color.Black, 0);
            g.DrawLine(blackPen, -5.0f, 0, 5.0f, 0);  // X軸
            g.DrawLine(blackPen, -5.0f, 2, 5.0f, 2);  // X軸
            g.DrawLine(blackPen, 0f, -1, 0f, 3);  // Y軸
        }

        //------------------------------------------------------------  # 60個

        private void button4_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button5_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button6_Click(object sender, EventArgs e)
        {
            //畫函數

            Bitmap bmp = new Bitmap(300, 300);
            Graphics g = Graphics.FromImage(bmp);
            g.SmoothingMode = SmoothingMode.AntiAlias;
            g.Clear(Color.White);
            g.ScaleTransform(15f, -15f, MatrixOrder.Append);
            g.TranslateTransform(bmp.Width * 0.5f, bmp.Height * 0.5f, MatrixOrder.Append);

            // 畫坐標軸
            Pen axis_pen = new Pen(Color.LightGray, 0);
            g.DrawLine(axis_pen, -8, 0, 8, 0);
            g.DrawLine(axis_pen, 0, -8, 0, 8);
            for (int i = -8; i <= 8; i++)
            {
                g.DrawLine(axis_pen, i, -0.1f, i, 0.1f);
                g.DrawLine(axis_pen, -0.1f, i, 0.1f, i);
            }

            // Graph the equation.
            float dx = 2f / bmp.Width;
            float dy = 2f / bmp.Height;
            //PlotFunction(g, func, -8, -8, 8, 8, dx, dy);
            //        private void PlotFunction(Graphics g, Func<float, float, float> func,
            //float xmin, float ymin, float xmax, float ymax,
            //float dx, float dy)
            float xmin = -8;
            float ymin = -8;
            float xmax = 8;
            float ymax = 8;

            // Plot the function.
            Pen thin_pen = new Pen(Color.Black, 0);
            // Horizontal comparisons.
            for (float x = xmin; x <= xmax; x += dx)
            {
                for (float y = ymin + dy; y <= ymax; y += dy)
                {
                    //g.DrawLine(thin_pen, x, y - dy, x, y);
                }
            } // Horizontal comparisons.

            // Vertical comparisons.
            for (float y = ymin + dy; y <= ymax; y += dy)
            {
                for (float x = xmin + dx; x <= xmax; x += dx)
                {
                    //g.DrawLine(thin_pen, x - dx, y, x, y);
                }
            }
            pictureBox1.Image = bmp;
        }

        //------------------------------------------------------------  # 60個

        Point getNewPoint(Point p, Point pZero, int bx, int by)
        {
            Point myp = new Point();
            myp.X = pZero.X + p.X / bx;
            if (p.Y > 0)
            {
                myp.Y = pZero.Y - Math.Abs(p.Y / by);
            }
            else
            {
                myp.Y = pZero.Y + Math.Abs(p.Y / by);
            }
            return myp;
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //座標圖
            //使用GDI畫坐標圖(支持負值)

            Bitmap bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height, PixelFormat.Format24bppRgb);
            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);
            Font f = new Font(Font.Name, 11);
            SolidBrush sb = new SolidBrush(Color.Black);
            Pen p = new Pen(Color.Black);
            p.EndCap = LineCap.ArrowAnchor;
            p.DashStyle = DashStyle.Solid;
            //坐标轴
            Point pCenter = new Point(300, 260);
            g.DrawLine(p, new Point(pCenter.X - 200, pCenter.Y), new Point(pCenter.X + 200, pCenter.Y));//x
            g.DrawLine(p, new Point(pCenter.X, pCenter.Y + 200), new Point(pCenter.X, pCenter.Y - 200));//y            
            //轴标格
            int iX = 30;
            for (int i = 0; i < 5; i++)
            {
                //零點向左
                g.DrawLine(Pens.Black, new Point(pCenter.X - iX * i, pCenter.Y), new Point(pCenter.X - iX * i, pCenter.Y - 4));//x
                g.DrawString((-i).ToString(), f, sb, new PointF(pCenter.X - iX * i, pCenter.Y));

                //零點向右
                g.DrawLine(Pens.Black, new Point(pCenter.X + iX * i, pCenter.Y), new Point(pCenter.X + iX * i, pCenter.Y - 4));//x
                g.DrawString(i.ToString(), f, sb, new PointF(pCenter.X + iX * i, pCenter.Y));

                //零點向上
                g.DrawLine(Pens.Black, new Point(pCenter.X, pCenter.Y - iX * i), new Point(pCenter.X + 4, pCenter.Y - iX * i));//y
                g.DrawString(i.ToString(), f, sb, new PointF(pCenter.X, pCenter.Y - iX * i));

                //零點向下
                g.DrawLine(Pens.Black, new Point(pCenter.X, pCenter.Y + iX * i), new Point(pCenter.X + 4, pCenter.Y + iX * i));//y
                g.DrawString((-i).ToString(), f, sb, new PointF(pCenter.X, pCenter.Y + iX * i));
            }

            g.DrawString("x", f, sb, new PointF(pCenter.X + 200, pCenter.Y));
            g.DrawString("y", f, sb, new PointF(pCenter.X, pCenter.Y - 200));
            g.DrawString("0", f, sb, new PointF(pCenter.X, pCenter.Y));
            //定义比例尺
            int BX = 4;
            int BY = 4;
            Point new1 = getNewPoint(new Point(200, 300), pCenter, BX, BY);
            Point new2 = getNewPoint(new Point(-300, 400), pCenter, BX, BY);
            Point new3 = getNewPoint(new Point(-400, -500), pCenter, BX, BY);
            Point new4 = getNewPoint(new Point(500, -300), pCenter, BX, BY);
            //g.DrawLine(Pens.Black, pCenter, new1);
            g.DrawArc(Pens.Black, new1.X, new1.Y, 1, 1, 45.0F, 360.0F);
            g.DrawString("p1", f, sb, new PointF(new1.X, new1.Y));
            g.DrawArc(Pens.Black, new2.X, new2.Y, 1, 1, 45.0F, 360.0F);
            g.DrawString("p2", f, sb, new PointF(new2.X, new2.Y));
            g.DrawArc(Pens.Black, new3.X, new3.Y, 1, 1, 45.0F, 360.0F);
            g.DrawString("p3", f, sb, new PointF(new3.X, new3.Y));
            g.DrawArc(Pens.Black, new4.X, new4.Y, 1, 1, 45.0F, 360.0F);
            g.DrawString("p4", f, sb, new PointF(new4.X, new4.Y));
            g.DrawLine(Pens.Black, new1, new2);
            g.DrawLine(Pens.Black, new2, new3);
            g.DrawLine(Pens.Black, new3, new4);
            g.DrawLine(Pens.Black, new4, new1);

            pictureBox1.Image = bitmap1;
        }

        //------------------------------------------------------------  # 60個

        private void button8_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button9_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個
        //------------------------------------------------------------  # 60個

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
                y2 = pictureBox2.Height / 5 + (int)(r * Math.Sin(theta));
            }
            else if (comboBox1.Text == "Cardiod")
            {
                if (theta >= Math.PI * 2)
                {
                    timer1.Enabled = false;
                    label4.Text = "";
                }
                a = 100;// b = 50;
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
                a = 150;
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
                a = 150;
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
                a = 150;
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
                g.DrawLine(MyPen, x1, y1, x2, y2);
            }
            x1 = x2;
            y1 = y2;
        }
        //------------------------------------------------------------  # 60個
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*
角度-180~+180
正弦值 -1~+1

xmin = -180;
xmax = 180;
ymin = -1;
ymax = 1;
xmargin = 10;
ymargin = 0.2;

顯示區域寬度W  if 720
顯示區域高度H  if 360

xratio = W / (xmax - xmin + xmargin * 2);  // 2 倍
yratio = H / (ymax - ymin + ymargin * 2);  // 180 倍

x=xmin:1:xmax;
y=sind(x);

先不考慮margin  把圖畫在中間

畫x時 每點相距 2 pixel

畫y時 要放大180倍

for(i = 0; i < 360; i++)
{
	x_new = x_old * 2;
	y_new = y_old * 180;
}

//------------------------------------------------------------  # 60個

            List<PointF> points_new = new List<PointF>();
            Pen p = new Pen(Color.Red, 0);
            g.DrawLines(p, points_new.ToArray());

//------------------------------------------------------------  # 60個

        private double rad(double d)
        {
            return d * Math.PI / 180.0;
        }

        private double sind(double d)
        {
            return Math.Sin(d * Math.PI / 180.0);
        }

        private double cosd(double d)
        {
            return Math.Cos(d * Math.PI / 180.0);
        }

        private float function(float x)
        {
            //return (float)(x * x + 2 * x + 1);
            return (float)(sind(3 * x) * 100);
        }
*/

