using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Collections;   //for ArrayList

using System.Drawing.Drawing2D; //for CompositingQuality, SmoothingMode //提供畫高級二維，矢量圖形功能
using System.Drawing.Imaging;   //for ImageFormat   //提供畫GDI+圖形的高級功能

using System.Runtime.InteropServices;   //for Marshal

using System.Drawing.Text;      //for TextRenderingHint //提供畫GDI+圖形的高級功能

using System.Diagnostics;       //for Debug
using System.Reflection;    //PropertyInfo
using System.Threading;

using System.IO;

namespace vcs_Draw_Example2
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;

        string title = "OV Exposure Plot";
        string xlabel = "x";
        string ylabel = "y";

        // Return a random color.
        private Random rand = new Random();
        private Color[] color =
        {
            Color.Red,
            Color.Green,
            Color.Blue,
            Color.Lime,
            Color.Orange,
            Color.Fuchsia,
            Color.Yellow,
            Color.LightGreen,
            Color.LightBlue,
            Color.Cyan,
        };

        private Color RandomColor()
        {
            return color[rand.Next(0, color.Length)];
        }

        public Form1()
        {
            InitializeComponent();
        }

        //重寫表單的OnPaint範例 直接寫在此即可
        protected override void OnPaint(PaintEventArgs e)
        {
            e.Graphics.DrawRectangle(Pens.Red, 5, 5, this.Width - 10, this.Height - 10);
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;

            //----開新的Bitmap----
            bitmap1 = new Bitmap(W, H);
            //----使用上面的Bitmap畫圖----
            g = Graphics.FromImage(bitmap1);

            p = new Pen(Color.Red, 2);     // 設定畫筆為紅色、粗細為 2 點。
            sb = new SolidBrush(Color.Blue);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;
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
            x_st = 10;
            y_st = 10;
            dx = 200 + 10;
            dy = 60 + 10;

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
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox1.Size = new Size(1024, 400);
            pictureBox1.BackColor = Color.White;
            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
            bt_save.Location = new Point(pictureBox1.Location.X + pictureBox1.Size.Width - bt_save.Size.Width * 2, pictureBox1.Location.Y + pictureBox1.Size.Height - bt_save.Size.Height);
            bt_reset.Location = new Point(pictureBox1.Location.X + pictureBox1.Size.Width - bt_reset.Size.Width, pictureBox1.Location.Y + pictureBox1.Size.Height - bt_reset.Size.Height);

            ucOscilloscope1.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            ucOscilloscope1.Size = new Size(1024, 200);
            ucOscilloscope1.BackColor = Color.Pink;

            richTextBox1.Size = new Size(1024, 200);
            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 9);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1500, 900);
            this.Text = "vcs_Draw_Example2";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            bitmap1 = null;
            pictureBox1.Image = null;
            richTextBox1.Clear();
        }

        private void bt_reset_Click(object sender, EventArgs e)
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 10;
            dy = 60 + 10;

            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox1.Size = new Size(900, 400);
            pictureBox1.BackColor = Color.White;
            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;

            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;

            //----開新的Bitmap----
            bitmap1 = new Bitmap(W, H);
            //----使用上面的Bitmap畫圖----
            g = Graphics.FromImage(bitmap1);

            p = new Pen(Color.Red, 10);     // 設定畫筆為紅色、粗細為 10 點。
            sb = new SolidBrush(Color.Blue);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;
        }

        private void bt_save_Click(object sender, EventArgs e)
        {
            save_image_to_drive();
        }

        //沒用到????
        void open_new_file()
        {
            richTextBox1.Text += "開啟一個 640 X 480 的空畫布\n";
            //指定畫布大小
            pictureBox1.Width = 640;
            pictureBox1.Height = 480;
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.DrawRectangle(p, 0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1);
            pictureBox1.Image = bitmap1;
            return;
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

        private void button0_Click(object sender, EventArgs e)
        {
            //使用Circle類別畫圖

            float x = 100;
            float y = 100;
            float r = 50;
            Circle circle0 = new Circle(x, y, r);

            int i;
            for (i = 50; i < 300; i += 50)
            {
                x = i;
                y = i;
                r = i / 2;


                using (Brush the_brush = new SolidBrush(RandomColor()))
                {
                    circle0 = new Circle(x, y, r);
                    circle0.Draw(g, the_brush);    //畫實心
                    richTextBox1.Text += "circle info : " + circle0.ToString() + "\n";
                }

                circle0 = new Circle(x, y, r + 10);
                Pen p = new Pen(Color.Red, 5);

                //circle0.Draw(g, Pens.Red); //畫空心, 未設定筆寬, 即筆寬為1
                circle0.Draw(g, p); //畫空心
                richTextBox1.Text += "circle info : " + circle0.ToString() + "\n";
            }

            pictureBox1.Image = bitmap1;
        }

        //畫多項式 ST
        private void button1_Click(object sender, EventArgs e)
        {
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
        //畫多項式 SP


        //畫XY平面 ST
        private void button2_Click(object sender, EventArgs e)
        {
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
        //畫XY平面 SP

        //畫Sinc ST
        private void button3_Click(object sender, EventArgs e)
        {
            MakeGraph();
        }

        // Make the graph.
        private void MakeGraph()
        {
            // The bounds to draw.
            float xmin = -20;
            float xmax = 20;
            float ymin = -5;
            float ymax = 12;

            // Make the Bitmap.
            int wid = pictureBox1.ClientSize.Width;
            int hgt = pictureBox1.ClientSize.Height;

            g.SmoothingMode = SmoothingMode.AntiAlias;

            // Transform to map the graph bounds to the Bitmap.
            RectangleF rect = new RectangleF(xmin, ymin, xmax - xmin, ymax - ymin);
            PointF[] pts = 
                {
                    new PointF(0, hgt),
                    new PointF(wid, hgt),
                    new PointF(0, 0),
                };
            g.Transform = new Matrix(rect, pts);

            // Draw the graph.
            Pen graph_pen = new Pen(Color.Blue, 0);
            // Draw the axes.
            g.DrawLine(graph_pen, xmin, 0, xmax, 0);
            g.DrawLine(graph_pen, 0, ymin, 0, ymax);
            for (int x = (int)xmin; x <= xmax; x++)
            {
                g.DrawLine(graph_pen, x, -0.1f, x, 0.1f);
            }
            for (int y = (int)ymin; y <= ymax; y++)
            {
                g.DrawLine(graph_pen, -0.1f, y, 0.1f, y);
            }
            graph_pen.Color = Color.Red;

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

            // Loop over x values to generate points.
            List<PointF> points = new List<PointF>();
            for (float x = xmin; x <= xmax; x += dx)
            {
                bool valid_point = false;
                try
                {
                    // Get the next point.
                    float y = F(x);

                    // If the slope is reasonable, this is a valid point.
                    if (points.Count == 0) valid_point = true;
                    else
                    {
                        float dy = y - points[points.Count - 1].Y;
                        if (Math.Abs(dy / dx) < 1000) valid_point = true;
                    }
                    if (valid_point) points.Add(new PointF(x, y));
                }
                catch
                {
                }

                // If the new point is invalid, draw
                // the points in the latest batch.
                if (!valid_point)
                {
                    if (points.Count > 1) g.DrawLines(graph_pen, points.ToArray());
                    points.Clear();
                }
            }

            // Draw the last batch of points.
            if (points.Count > 1)
            {
                g.DrawLines(graph_pen, points.ToArray());
            }

            // Display the result.
            pictureBox1.Image = bitmap1;
        }

        // The function to graph.
        private float F(float x)
        {
            //return (float)((1 / x + 1 / (x + 1) - 2 * x * x) / 10);
            //return x;
            //return (float)Math.Sin(x);
            return (float)(10 * Math.Sin(x) / x);
        }
        //畫Sinc SP


        //畫愛心 ST
        private void button4_Click(object sender, EventArgs e)
        {
            g.SmoothingMode = SmoothingMode.AntiAlias;

            // Generate the points.
            const int num_points = 100;
            List<PointF> points = new List<PointF>();
            float dt = (float)(2 * Math.PI / num_points);
            for (float t = 0; t <= 2 * Math.PI; t += dt)
                points.Add(new PointF(X(t) * 5 + 200, Y(t) * 5 + 200));

            // Get the coordinate bounds.
            float wxmin = points[0].X;
            float wxmax = wxmin;
            float wymin = points[0].Y;
            float wymax = wymin;
            foreach (PointF point in points)
            {
                if (wxmin > point.X) wxmin = point.X;
                if (wxmax < point.X) wxmax = point.X;
                if (wymin > point.Y) wymin = point.Y;
                if (wymax < point.Y) wymax = point.Y;
            }

            // Make the world coordinate rectangle.
            RectangleF world_rect = new RectangleF(
                wxmin, wymin, wxmax - wxmin, wymax - wymin);

            // Make the device coordinate rectangle with a margin.
            const int margin = 5;
            Rectangle device_rect = new Rectangle(
                margin, margin,
                pictureBox1.ClientSize.Width - 2 * margin,
                pictureBox1.ClientSize.Height - 2 * margin);

            // Map world to device coordinates without distortion.
            // Flip vertically so Y increases downward.
            //SetTransformationWithoutDisortion(gr, world_rect, device_rect, false, true);

            // Draw the curve.
            g.FillPolygon(Brushes.Pink, points.ToArray());
            Pen pen = new Pen(Color.Red, 0);

            g.DrawPolygon(pen, points.ToArray());

            // Draw a rectangle around the coordinate bounds.
            pen.Color = Color.Red;
            g.DrawRectangle(pen, Rectangle.Round(world_rect));

            int ratio = 20;
            // Draw the X and Y axes.
            pen.Color = Color.Green;
            g.DrawLine(pen, -20 * ratio, 0, 20 * ratio, 0);
            g.DrawLine(pen, 0, -20 * ratio, 0, 20 * ratio);
            for (int x = -20; x <= 20; x++)
            {
                g.DrawLine(pen, x * ratio, -0.3f * ratio, x * ratio, 0.3f * ratio);
            }
            for (int y = -20; y <= 20; y++)
            {
                g.DrawLine(pen, -0.3f * ratio, y * ratio, 0.3f * ratio, y * ratio);
            }
            pictureBox1.Image = bitmap1;
        }

        // The curve's parametric equations.
        private float X(float t)
        {
            double sin_t = Math.Sin(t);
            return (float)(16 * sin_t * sin_t * sin_t);
        }

        private float Y(float t)
        {
            return (float)(13 * Math.Cos(t) - 5 * Math.Cos(2 * t) - 2 * Math.Cos(3 * t) - Math.Cos(4 * t));
        }
        //畫愛心 SP

        private void button5_Click(object sender, EventArgs e)
        {
            //按鍵樣橢圓
            //pictureBox1.Size = new Size(300, 200);
            Graphics g = pictureBox1.CreateGraphics();
            Brush sb = new SolidBrush(Color.Blue);
            g.SmoothingMode = SmoothingMode.AntiAlias;

            //橢圓的左上角與長寬
            int x_st = 30;
            int y_st = 30;
            int W = 300;
            int H = 200;

            g.DrawRectangle(Pens.Red, x_st, y_st, W - 60, H - 60);

            // Get the area we will fill.
            Rectangle rect = new Rectangle(x_st, y_st, W - 60, H - 60);

            // Fill the ellipse.
            using (LinearGradientBrush br = new LinearGradientBrush(rect, Color.Lime, Color.DarkGreen, 225f))
            {
                g.FillEllipse(br, rect);
            }
            // Outline the ellipse.
            using (LinearGradientBrush br = new LinearGradientBrush(rect, Color.Lime, Color.DarkGreen, 45f))
            {
                using (Pen pen = new Pen(br, 20f))
                {
                    // g.DrawRectangle(Pens.Red, rect);
                    rect.X += 10;
                    rect.Y += 10;
                    rect.Width -= 20;
                    rect.Height -= 20;

                    g.DrawEllipse(pen, rect);
                }
            }
            sb.Dispose();
        }

        void plotXY(int[] x, int[] y)
        {
            int border_x = 10;  //10% border X
            int border_y = 10;  //10% border Y

            int WW = pictureBox1.ClientSize.Width;
            int HH = pictureBox1.ClientSize.Height;

            int x_st = WW * border_x / 100;
            int y_st = HH * border_y / 100;

            richTextBox1.Text += "WW = " + WW.ToString() + "\n";
            richTextBox1.Text += "HH = " + HH.ToString() + "\n";

            int W = WW * (100 - border_x * 2) / 100;
            int H = HH * (100 - border_y * 2) / 100;

            richTextBox1.Text += "W = " + W.ToString() + "\n";
            richTextBox1.Text += "H = " + H.ToString() + "\n";

            int N1 = x.Length;
            int N2 = y.Length;
            int N = Math.Min(N1, N2);
            richTextBox1.Text += "x_len = " + x.Length.ToString() + "\n";
            richTextBox1.Text += "y_len = " + y.Length.ToString() + "\n";
            richTextBox1.Text += "N = " + N.ToString() + "\n";

            int y_max = y.Max();
            int y_min = y.Min();
            richTextBox1.Text += "y_max = " + y_max.ToString() + "\n";
            richTextBox1.Text += "y_min = " + y_min.ToString() + "\n";

            float x_ratio = W / (float)N;
            float y_ratio = H / (float)(y_max - y_min);

            richTextBox1.Text += "x_ratio = " + x_ratio.ToString() + "\n";
            richTextBox1.Text += "y_ratio = " + y_ratio.ToString() + "\n";

            g.Clear(Color.White);

            int i;
            Point[] curvePoints = new Point[N];    //一維陣列內有 N 個Point

            for (i = 0; i < N; i++)
            {
                curvePoints[i].X = x_st + (int)(x[i] * x_ratio);
                //curvePoints[i].Y = HH - (y_st + (int)(y[i] * y_ratio));
                curvePoints[i].Y = HH - (y_st + (int)((y[i] - y_min) * y_ratio));
                if (i == 0)
                {
                    richTextBox1.Text += curvePoints[i].ToString() + "\n";
                    richTextBox1.Text += "x_st = " + x_st.ToString() + ", y_st = " + y_st.ToString() + "\n";
                }
            }
            g.DrawLines(p, curvePoints);   //畫直線

            g.DrawRectangle(new Pen(Color.Red), new Rectangle(x_st, y_st, W - 1, H - 1));

            Font f = new Font("標楷體", 24);
            int tmp_width = 0;
            int tmp_height = 0;
            tmp_width = g.MeasureString(title, f).ToSize().Width;
            tmp_height = g.MeasureString(title, f).ToSize().Height;
            richTextBox1.Text += "tmp_width = " + tmp_width.ToString() + "  tmp_height = " + tmp_height.ToString() + "\n";
            g.DrawString(title, f, new SolidBrush(Color.Blue), new PointF((WW - tmp_width) / 2, (y_st - tmp_height) / 2));

            pictureBox1.Image = bitmap1;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //畫OV曲線 1

            int i;
            int N = 256;
            int[] data_x = new int[N];
            int[] data_y = new int[N];
            double gamma = 2.2;

            for (i = 0; i < N; i++)
            {
                data_x[i] = i;
                //data_y[i] = (int)(Math.Sin(i) * 100 + 100);
                data_y[i] = (int)(Math.Pow(((double)data_x[i]) / 255, 1 / gamma) * 255);
                //data_y[i] = i;

            }
            plotXY(data_x, data_y);
        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //用GDI+畫圖

            Graphics g = this.pictureBox1.CreateGraphics();
            g.FillRectangle(Brushes.White, this.ClientRectangle);
            for (int i = 1; i <= 7; ++i)
            {
                //在窗體上面畫出橙色的矩形

                Rectangle r = new Rectangle(i * 40 - 15, 0, 15, this.ClientRectangle.Height);
                g.FillRectangle(Brushes.Orange, r);
            }
            //在內存中創建一個Bitmap並設置CompositingMode
            Bitmap bmp = new Bitmap(260, 260, PixelFormat.Format32bppArgb);
            Graphics gBmp = Graphics.FromImage(bmp);
            gBmp.CompositingMode = System.Drawing.Drawing2D.CompositingMode.SourceCopy;

            // 創建一個帶有Alpha的紅色區域
            // 並將其畫在內存的位圖裏面
            Color red = Color.FromArgb(0x60, 0xff, 0, 0);
            Brush redBrush = new SolidBrush(red);
            gBmp.FillEllipse(redBrush, 70, 70, 160, 160);
            // 創建一個帶有Alpha的綠色區域
            Color green = Color.FromArgb(0x40, 0, 0xff, 0);
            Brush greenBrush = new SolidBrush(green);
            gBmp.FillRectangle(greenBrush, 10, 10, 140, 140);

            //在窗體上面畫出位圖 now draw the bitmap on our window
            g.DrawImage(bmp, 20, 20, bmp.Width, bmp.Height);

            // 清理資源
            bmp.Dispose();
            gBmp.Dispose();
            redBrush.Dispose();
            greenBrush.Dispose();
        }

        private void button11_Click(object sender, EventArgs e)
        {
        }

        //實現wav波形圖 ST
        const int byteSample = 2;
        const int dataPosition = 40;
        //0x16 2byte 0002  雙聲道
        //0x22 2byte 0010  16位
        //0x18 4byte 0000AC44   44100采樣率

        const bool leftStatus = false;

        private void button12_Click(object sender, EventArgs e)
        {
            //wave轉txt
            richTextBox1.Text += "wave轉txt ST\n";
            Application.DoEvents();

            //讀取wav，保存音頻數據到txt
            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\_wav\start.wav";
            string filename2 = @"start.txt";

            byte[] length = new byte[4];
            FileStream fs = new FileStream(filename1, FileMode.Open, FileAccess.Read);
            fs.Position = dataPosition;
            fs.Read(length, 0, 4);
            byte[] content = new byte[getHexToInt(length)];
            string[] sample = new string[content.Length / byteSample];
            fs.Read(content, 0, content.Length);
            getHex(content);
            sample = getSample(content);
            StreamWriter sw = new StreamWriter(filename2, true, Encoding.Default);
            foreach (string i in sample)
            {
                sw.Flush();
                sw.WriteLine(i);
            }
            sw.Close();
            richTextBox1.Text += "wave轉txt SP\n";
        }

        static int getHexToInt(byte[] x)
        {
            string retValue = "";
            for (int i = x.Length - 1; i >= 0; i--)
            {
                retValue += x[i].ToString("X");
            }
            return Convert.ToInt32(retValue, 16);
        }

        static void getHex(byte[] x)
        {
            byte tmp;
            for (int i = 0; i < x.Length; i++)
            {
                tmp = Convert.ToByte(x[i].ToString("X"), 16);
                x[i] = tmp;
            }
        }

        static string[] getSample(byte[] x)
        {
            string[] retValue = new string[x.Length / byteSample];

            for (int i = 0; i < retValue.Length; i++)
            {
                for (int j = (i + 1) * byteSample - 1; j >= i * byteSample; j--)
                {
                    retValue[i] += x[j].ToString("X");
                }
                retValue[i] = ((double)Convert.ToInt16(retValue[i], 16) / 32768).ToString("F4");
            }
            return retValue;
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //顯示wave 1
            string filename2 = @"start.txt";

            new Thread(new ThreadStart(() =>
            {
                this.Invoke(new MethodInvoker(() => { richTextBox1.Text += leftStatus ? "左聲道" : "右聲道"; }));
                List<double> list = new List<double>();
                StreamReader sr = new StreamReader(filename2, Encoding.Default);
                int m = 0;
                while (!sr.EndOfStream)
                {
                    if (leftStatus)
                    {
                        if (m % 2 == 0)
                            list.Add(double.Parse(sr.ReadLine()));
                    }
                    else
                    {
                        if (m % 2 != 0)
                            list.Add(double.Parse(sr.ReadLine()));
                    }
                    m++;
                }
                sr.Close();
                Bitmap bitmap = new Bitmap(pictureBox1.Width, pictureBox1.Height);
                Graphics g = Graphics.FromImage(bitmap);
                g.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
                g.DrawLine(new Pen(Color.Black, 5), new Point(20, 20), new Point(20, 540));
                g.DrawLine(new Pen(Color.Black, 5), new Point(20, 290), new Point(1600, 290));

                int k = list.Count / 1550;

                for (int i = 0; i < list.Count; i++)
                {
                    g.DrawLine(new Pen(Color.Green, 1), new Point(20 + i / k, 290), new Point(20 + i / k, 290 + (int)(list[i] * 250 * 2)));
                }
                this.pictureBox1.Image = bitmap;
            })).Start();
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //顯示wave 2
            string filename = @"D:\_git\vcs\_1.data\______test_files1\_wav\start.wav";

            WAVReader wr = new WAVReader();
            wr.ReadWAVFile(filename);
            int ww = pictureBox1.Width;
            int hh = pictureBox1.Height;
            Graphics g = pictureBox1.CreateGraphics();
            g.SmoothingMode = SmoothingMode.AntiAlias;
            g.DrawLine(new Pen(Color.DarkSeaGreen, 1), new Point(0, hh / 2), new Point(ww, hh / 2));
            int prex = 0, prey = 0; //上一個座標  
            int x = 0, y = 0;
            double k = hh / 2.0 / 32768.0;
            for (int i = 0; i < ww; i++)
            {
                x = i;
                y = hh - (int)(wr.wavdata[i * 3] * k + hh / 2);
                if (i != 0)
                {
                    g.DrawLine(new Pen(Color.Red, 1), x, y, prex, prey);
                }
                prex = x;
                prey = y;
            }
        }
        //實現wav波形圖 SP

        private void button15_Click(object sender, EventArgs e)
        {
            //畫函數
            // Make the Bitmap.
            Bitmap bm = new Bitmap(300, 300);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                // Clear.
                gr.SmoothingMode = SmoothingMode.AntiAlias;
                gr.Clear(Color.White);
                gr.ScaleTransform(15f, -15f, System.Drawing.Drawing2D.MatrixOrder.Append);
                gr.TranslateTransform(bm.Width * 0.5f, bm.Height * 0.5f,
                    System.Drawing.Drawing2D.MatrixOrder.Append);

                // 畫坐標軸
                using (Pen axis_pen = new Pen(Color.LightGray, 0))
                {
                    gr.DrawLine(axis_pen, -8, 0, 8, 0);
                    gr.DrawLine(axis_pen, 0, -8, 0, 8);
                    for (int i = -8; i <= 8; i++)
                    {
                        gr.DrawLine(axis_pen, i, -0.1f, i, 0.1f);
                        gr.DrawLine(axis_pen, -0.1f, i, 0.1f, i);
                    }
                }

                // Graph the equation.
                float dx = 2f / bm.Width;
                float dy = 2f / bm.Height;
                //PlotFunction(gr, func, -8, -8, 8, 8, dx, dy);
                //        private void PlotFunction(Graphics gr, Func<float, float, float> func,
                //float xmin, float ymin, float xmax, float ymax,
                //float dx, float dy)
                float xmin = -8;
                float ymin = -8;
                float xmax = 8;
                float ymax = 8;

                // Plot the function.
                using (Pen thin_pen = new Pen(Color.Black, 0))
                {
                    // Horizontal comparisons.
                    for (float x = xmin; x <= xmax; x += dx)
                    {
                        for (float y = ymin + dy; y <= ymax; y += dy)
                        {
                            //gr.DrawLine(thin_pen, x, y - dy, x, y);
                        }
                    } // Horizontal comparisons.

                    // Vertical comparisons.
                    for (float y = ymin + dy; y <= ymax; y += dy)
                    {
                        for (float x = xmin + dx; x <= xmax; x += dx)
                        {
                            //gr.DrawLine(thin_pen, x - dx, y, x, y);
                        }
                    }
                }
            }
            pictureBox1.Image = bm;
        }

        private void button16_Click(object sender, EventArgs e)
        {
        }

        private void button17_Click(object sender, EventArgs e)
        {
        }

        void draw_Oscilloscope(string filename)
        {
            ucOscilloscope1.LineColor = Color.Red;

            string data;
            string[] splitData;
            using (TextReader reader = File.OpenText(filename))
            {
                data = reader.ReadToEnd();
                splitData = data.Split(new char[] { '\r', '\n' }, StringSplitOptions.RemoveEmptyEntries);
            }
            List<int> mapData = new List<int>();
            foreach (string info in splitData)
            {
                try
                {
                    int xxx = Convert.ToInt32(info);
                    if (xxx > 0)
                    {
                        mapData.Add(xxx);
                    }
                }
                catch (System.Exception ex)
                {
                }
            }
            ucOscilloscope1.MappingDatas = mapData;
        }

        private void button18_Click(object sender, EventArgs e)
        {
            //畫 Oscilloscope 1
            string filename = @"..\..\data\MappingData1.txt";
            draw_Oscilloscope(filename);
        }

        private void button19_Click(object sender, EventArgs e)
        {
            //畫 Oscilloscope 2
            string filename = @"..\..\data\MappingData2.txt";
            draw_Oscilloscope(filename);
        }
    }

    class WAVReader //wav 文件讀取類
    {
        private string Id; //文件標識
        private double Size;  //文件大小
        private string Type; //文件類型
        private string formatId;
        private double formatSize;      //數值爲16或18，18則最後又附加信息
        private int formatTag;
        private int num_Channels;       //聲道數目
        private int SamplesPerSec;      //採樣率
        private int AvgBytesPerSec;     //每秒所需字節數 
        private int BlockAlign;         //數據塊對齊單位(每個採樣需要的字節數) 
        private int BitsPerSample;      //每個採樣需要的bit數
        private string additionalInfo;  //附加信息
        private string dataId;
        private int dataSize;
        public List<double> wavdata = new List<double>();
        public void ReadWAVFile(string filePath)  //讀取波形文件並顯示
        {
            if (filePath == "") return;
            byte[] id = new byte[4];
            byte[] size = new byte[4];
            byte[] type = new byte[4];
            byte[] formatid = new byte[4];
            byte[] formatsize = new byte[4];
            byte[] formattag = new byte[2];
            byte[] numchannels = new byte[2];
            byte[] samplespersec = new byte[4];
            byte[] avgbytespersec = new byte[4];
            byte[] blockalign = new byte[2];
            byte[] bitspersample = new byte[2];
            byte[] additionalinfo = new byte[2];    //可選
            byte[] factid = new byte[4];
            byte[] factsize = new byte[4];
            byte[] factdata = new byte[4];
            byte[] dataid = new byte[4];
            byte[] datasize = new byte[4];
            using (FileStream fs = new FileStream(filePath, FileMode.Open, FileAccess.Read))
            {
                using (BinaryReader br = new BinaryReader(fs, Encoding.UTF8))
                {
                    #region  RIFF WAVE Chunk
                    br.Read(id, 0, 4);
                    br.Read(size, 0, 4);
                    br.Read(type, 0, 4);
                    Id = getString(id, 4);
                    long longsize = bytArray2Int(size);//十六進制轉爲十進制
                    Size = longsize * 1.0;
                    Type = getString(type, 4);
                    #endregion
                    #region Format Chunk
                    br.Read(formatid, 0, 4);
                    br.Read(formatsize, 0, 4);
                    br.Read(formattag, 0, 2);
                    br.Read(numchannels, 0, 2);
                    br.Read(samplespersec, 0, 4);
                    br.Read(avgbytespersec, 0, 4);
                    br.Read(blockalign, 0, 2);
                    br.Read(bitspersample, 0, 2);
                    if (getString(formatsize, 2) == "18")
                    {
                        br.Read(additionalinfo, 0, 2);
                        additionalInfo = getString(additionalinfo, 2);  //附加信息
                    }
                    formatId = getString(formatid, 4);
                    formatSize = bytArray2Int(formatsize);
                    byte[] tmptag = composeByteArray(formattag);
                    formatTag = bytArray2Int(tmptag);
                    byte[] tmpchanels = composeByteArray(numchannels);
                    num_Channels = bytArray2Int(tmpchanels);                //聲道數目
                    SamplesPerSec = bytArray2Int(samplespersec);            //採樣率
                    AvgBytesPerSec = bytArray2Int(avgbytespersec);          //每秒所需字節數   
                    byte[] tmpblockalign = composeByteArray(blockalign);
                    BlockAlign = bytArray2Int(tmpblockalign);              //數據塊對齊單位(每個採樣需要的字節數)
                    byte[] tmpbitspersample = composeByteArray(bitspersample);
                    BitsPerSample = bytArray2Int(tmpbitspersample);        // 每個採樣需要的bit數     
                    #endregion
                    #region Data Chunk
                    byte[] d_flag = new byte[1];
                    while (true)
                    {
                        br.Read(d_flag, 0, 1);
                        if (getString(d_flag, 1) == "d")
                        {
                            break;
                        }
                    }
                    byte[] dt_id = new byte[4];
                    dt_id[0] = d_flag[0];
                    br.Read(dt_id, 1, 3);
                    dataId = getString(dt_id, 4);
                    br.Read(datasize, 0, 4);
                    dataSize = bytArray2Int(datasize);
                    List<string> testl = new List<string>();
                    if (BitsPerSample == 8)
                    {
                        for (int i = 0; i < dataSize; i++)
                        {
                            byte wavdt = br.ReadByte();
                            wavdata.Add(wavdt);
                        }
                    }
                    else if (BitsPerSample == 16)
                    {
                        for (int i = 0; i < dataSize / 2; i++)
                        {
                            short wavdt = br.ReadInt16();
                            wavdata.Add(wavdt);
                        }
                    }
                    #endregion
                }
            } //wavdata


        }
        // 數字節數組轉換爲int
        private int bytArray2Int(byte[] bytArray)
        {
            return bytArray[0] | (bytArray[1] << 8) | (bytArray[2] << 16) | (bytArray[3] << 24);
        }
        // 將字節數組轉換爲字符串
        private string getString(byte[] bts, int len)
        {
            char[] tmp = new char[len];
            for (int i = 0; i < len; i++)
            {
                tmp[i] = (char)bts[i];
            }
            return new string(tmp);
        }
        // 組成4個元素的字節數組
        private byte[] composeByteArray(byte[] bt)
        {
            byte[] tmptag = new byte[4] { 0, 0, 0, 0 };
            tmptag[0] = bt[0];
            tmptag[1] = bt[1];
            return tmptag;
        }
    }
}
