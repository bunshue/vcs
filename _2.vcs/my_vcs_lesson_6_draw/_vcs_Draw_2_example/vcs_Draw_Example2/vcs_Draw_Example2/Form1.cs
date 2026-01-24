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
            pictureBox1.Size = new Size(900, 400);
            pictureBox1.BackColor = Color.White;
            bt_save.Location = new Point(pictureBox1.Location.X + pictureBox1.Size.Width - bt_save.Size.Width * 2, pictureBox1.Location.Y + pictureBox1.Size.Height - bt_save.Size.Height);
            bt_reset.Location = new Point(pictureBox1.Location.X + pictureBox1.Size.Width - bt_reset.Size.Width, pictureBox1.Location.Y + pictureBox1.Size.Height - bt_reset.Size.Height);

            ucOscilloscope1.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            ucOscilloscope1.Size = new Size(1024, 200);
            ucOscilloscope1.BackColor = Color.Pink;

            richTextBox1.Size = new Size(640, 200);
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
            pictureBox1.Location = new Point(10, 10);
            pictureBox1.Size = new Size(900, 600);
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
            Bitmap bm = new Bitmap(wid, hgt);
            using (Graphics g = Graphics.FromImage(bm))
            {
                g.Clear(Color.White);
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
                using (Pen graph_pen = new Pen(Color.Blue, 0))
                {
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
                    if (points.Count > 1) g.DrawLines(graph_pen, points.ToArray());
                }
            }

            // Display the result.
            pictureBox1.Image = bm;
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
            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;
            pictureBox1.Image = DrawHeart(W, H);
        }

        // Draw the curve on a bitmap.
        private Bitmap DrawHeart(int width, int height)
        {
            Bitmap bm = new Bitmap(width, height);
            using (Graphics g = Graphics.FromImage(bm))
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
                using (Pen pen = new Pen(Color.Red, 0))
                {
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
                        g.DrawLine(pen, x * ratio, -0.3f * ratio, x * ratio, 0.3f * ratio);
                    for (int y = -20; y <= 20; y++)
                        g.DrawLine(pen, -0.3f * ratio, y * ratio, 0.3f * ratio, y * ratio);
                }
            }
            return bm;
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
            pictureBox1.Size = new Size(300, 200);
            Graphics g = pictureBox1.CreateGraphics();
            Brush sb = new SolidBrush(Color.Blue);
            g.SmoothingMode = SmoothingMode.AntiAlias;

            int W = this.pictureBox1.Width;
            int H = this.pictureBox1.Height;

            // Get the area we will fill.
            Rectangle rect = new Rectangle(30, 30, W - 60, H - 60);

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


            //g.FillEllipse(sb, 100, 100, 200, 100);




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

            double gamma;
            gamma = 2.2;

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
            //畫OV曲線 2
            int N = 50;
            int i;
            int[] data_x = new int[N];
            int[] data_y = new int[N];

            Random r = new Random();
            for (i = 0; i < N; i++)
            {
                data_x[i] = i;
                //data_y[i] = (int)(100 * Math.Sin(i));
                data_y[i] = r.Next(50, 60000);

            }
            plotXY(data_x, data_y);
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //畫OV曲線 3
            int N = 500;
            //int i;
            int[] expo_data_in = new int[N];
            int[] expo_data_out = new int[N];

            expo_data_in[0] = 0; expo_data_out[0] = 70;

            expo_data_in[1] = 1; expo_data_out[1] = 71;

            expo_data_in[2] = 2; expo_data_out[2] = 71;

            expo_data_in[3] = 3; expo_data_out[3] = 71;

            expo_data_in[4] = 4; expo_data_out[4] = 71;

            expo_data_in[5] = 5; expo_data_out[5] = 71;

            expo_data_in[6] = 6; expo_data_out[6] = 71;

            expo_data_in[7] = 7; expo_data_out[7] = 71;

            expo_data_in[8] = 8; expo_data_out[8] = 71;

            expo_data_in[9] = 9; expo_data_out[9] = 72;

            expo_data_in[10] = 10; expo_data_out[10] = 72;

            expo_data_in[11] = 11; expo_data_out[11] = 72;

            expo_data_in[12] = 12; expo_data_out[12] = 72;

            expo_data_in[13] = 13; expo_data_out[13] = 72;

            expo_data_in[14] = 14; expo_data_out[14] = 72;

            expo_data_in[15] = 15; expo_data_out[15] = 72;

            expo_data_in[16] = 16; expo_data_out[16] = 72;

            expo_data_in[17] = 17; expo_data_out[17] = 73;

            expo_data_in[18] = 18; expo_data_out[18] = 73;

            expo_data_in[19] = 19; expo_data_out[19] = 73;

            expo_data_in[20] = 20; expo_data_out[20] = 73;

            expo_data_in[21] = 21; expo_data_out[21] = 73;

            expo_data_in[22] = 22; expo_data_out[22] = 73;

            expo_data_in[23] = 23; expo_data_out[23] = 73;

            expo_data_in[24] = 24; expo_data_out[24] = 73;

            expo_data_in[25] = 25; expo_data_out[25] = 74;

            expo_data_in[26] = 26; expo_data_out[26] = 74;

            expo_data_in[27] = 27; expo_data_out[27] = 74;

            expo_data_in[28] = 28; expo_data_out[28] = 74;

            expo_data_in[29] = 29; expo_data_out[29] = 74;

            expo_data_in[30] = 30; expo_data_out[30] = 74;

            expo_data_in[31] = 31; expo_data_out[31] = 74;

            expo_data_in[32] = 32; expo_data_out[32] = 75;

            expo_data_in[33] = 33; expo_data_out[33] = 75;

            expo_data_in[34] = 34; expo_data_out[34] = 75;

            expo_data_in[35] = 35; expo_data_out[35] = 75;

            expo_data_in[36] = 36; expo_data_out[36] = 75;

            expo_data_in[37] = 37; expo_data_out[37] = 75;

            expo_data_in[38] = 38; expo_data_out[38] = 75;

            expo_data_in[39] = 39; expo_data_out[39] = 75;

            expo_data_in[40] = 40; expo_data_out[40] = 76;

            expo_data_in[41] = 41; expo_data_out[41] = 76;

            expo_data_in[42] = 42; expo_data_out[42] = 76;

            expo_data_in[43] = 43; expo_data_out[43] = 76;

            expo_data_in[44] = 44; expo_data_out[44] = 76;

            expo_data_in[45] = 45; expo_data_out[45] = 76;

            expo_data_in[46] = 46; expo_data_out[46] = 76;

            expo_data_in[47] = 47; expo_data_out[47] = 76;

            expo_data_in[48] = 48; expo_data_out[48] = 77;

            expo_data_in[49] = 49; expo_data_out[49] = 77;

            expo_data_in[50] = 50; expo_data_out[50] = 77;

            expo_data_in[51] = 51; expo_data_out[51] = 77;

            expo_data_in[52] = 52; expo_data_out[52] = 77;

            expo_data_in[53] = 53; expo_data_out[53] = 77;

            expo_data_in[54] = 54; expo_data_out[54] = 77;

            expo_data_in[55] = 55; expo_data_out[55] = 77;

            expo_data_in[56] = 56; expo_data_out[56] = 78;

            expo_data_in[57] = 57; expo_data_out[57] = 78;

            expo_data_in[58] = 58; expo_data_out[58] = 78;

            expo_data_in[59] = 59; expo_data_out[59] = 78;

            expo_data_in[60] = 60; expo_data_out[60] = 78;

            expo_data_in[61] = 61; expo_data_out[61] = 78;

            expo_data_in[62] = 62; expo_data_out[62] = 78;

            expo_data_in[63] = 63; expo_data_out[63] = 78;

            expo_data_in[64] = 64; expo_data_out[64] = 78;

            expo_data_in[65] = 65; expo_data_out[65] = 79;

            expo_data_in[66] = 66; expo_data_out[66] = 79;

            expo_data_in[67] = 67; expo_data_out[67] = 79;

            expo_data_in[68] = 68; expo_data_out[68] = 79;

            expo_data_in[69] = 69; expo_data_out[69] = 79;

            expo_data_in[70] = 70; expo_data_out[70] = 79;

            expo_data_in[71] = 71; expo_data_out[71] = 79;

            expo_data_in[72] = 72; expo_data_out[72] = 79;

            expo_data_in[73] = 73; expo_data_out[73] = 80;

            expo_data_in[74] = 74; expo_data_out[74] = 80;

            expo_data_in[75] = 75; expo_data_out[75] = 79;

            expo_data_in[76] = 76; expo_data_out[76] = 79;

            expo_data_in[77] = 77; expo_data_out[77] = 80;

            expo_data_in[78] = 78; expo_data_out[78] = 80;

            expo_data_in[79] = 79; expo_data_out[79] = 80;

            expo_data_in[80] = 80; expo_data_out[80] = 80;

            expo_data_in[81] = 81; expo_data_out[81] = 80;

            expo_data_in[82] = 82; expo_data_out[82] = 80;

            expo_data_in[83] = 83; expo_data_out[83] = 80;

            expo_data_in[84] = 84; expo_data_out[84] = 80;

            expo_data_in[85] = 85; expo_data_out[85] = 80;

            expo_data_in[86] = 86; expo_data_out[86] = 81;

            expo_data_in[87] = 87; expo_data_out[87] = 81;

            expo_data_in[88] = 88; expo_data_out[88] = 81;

            expo_data_in[89] = 89; expo_data_out[89] = 81;

            expo_data_in[90] = 90; expo_data_out[90] = 81;

            expo_data_in[91] = 91; expo_data_out[91] = 81;

            expo_data_in[92] = 92; expo_data_out[92] = 81;

            expo_data_in[93] = 93; expo_data_out[93] = 81;

            expo_data_in[94] = 94; expo_data_out[94] = 81;

            expo_data_in[95] = 95; expo_data_out[95] = 82;

            expo_data_in[96] = 96; expo_data_out[96] = 82;

            expo_data_in[97] = 97; expo_data_out[97] = 82;

            expo_data_in[98] = 98; expo_data_out[98] = 82;

            expo_data_in[99] = 99; expo_data_out[99] = 82;

            expo_data_in[100] = 100; expo_data_out[100] = 82;

            expo_data_in[101] = 101; expo_data_out[101] = 82;

            expo_data_in[102] = 102; expo_data_out[102] = 82;

            expo_data_in[103] = 103; expo_data_out[103] = 82;

            expo_data_in[104] = 104; expo_data_out[104] = 83;

            expo_data_in[105] = 105; expo_data_out[105] = 83;

            expo_data_in[106] = 106; expo_data_out[106] = 83;

            expo_data_in[107] = 107; expo_data_out[107] = 83;

            expo_data_in[108] = 108; expo_data_out[108] = 83;

            expo_data_in[109] = 109; expo_data_out[109] = 83;

            expo_data_in[110] = 110; expo_data_out[110] = 83;

            expo_data_in[111] = 111; expo_data_out[111] = 83;

            expo_data_in[112] = 112; expo_data_out[112] = 83;

            expo_data_in[113] = 113; expo_data_out[113] = 83;

            expo_data_in[114] = 114; expo_data_out[114] = 84;

            expo_data_in[115] = 115; expo_data_out[115] = 84;

            expo_data_in[116] = 116; expo_data_out[116] = 84;

            expo_data_in[117] = 117; expo_data_out[117] = 84;

            expo_data_in[118] = 118; expo_data_out[118] = 84;

            expo_data_in[119] = 119; expo_data_out[119] = 84;

            expo_data_in[120] = 120; expo_data_out[120] = 84;

            expo_data_in[121] = 121; expo_data_out[121] = 84;

            expo_data_in[122] = 122; expo_data_out[122] = 84;

            expo_data_in[123] = 123; expo_data_out[123] = 85;

            expo_data_in[124] = 124; expo_data_out[124] = 85;

            expo_data_in[125] = 125; expo_data_out[125] = 85;

            expo_data_in[126] = 126; expo_data_out[126] = 85;

            expo_data_in[127] = 127; expo_data_out[127] = 85;

            expo_data_in[128] = 128; expo_data_out[128] = 85;

            expo_data_in[129] = 129; expo_data_out[129] = 85;

            expo_data_in[130] = 130; expo_data_out[130] = 85;

            expo_data_in[131] = 131; expo_data_out[131] = 85;

            expo_data_in[132] = 132; expo_data_out[132] = 86;

            expo_data_in[133] = 133; expo_data_out[133] = 86;

            expo_data_in[134] = 134; expo_data_out[134] = 86;

            expo_data_in[135] = 135; expo_data_out[135] = 86;

            expo_data_in[136] = 136; expo_data_out[136] = 86;

            expo_data_in[137] = 137; expo_data_out[137] = 86;

            expo_data_in[138] = 138; expo_data_out[138] = 86;

            expo_data_in[139] = 139; expo_data_out[139] = 86;

            expo_data_in[140] = 140; expo_data_out[140] = 86;

            expo_data_in[141] = 141; expo_data_out[141] = 86;

            expo_data_in[142] = 142; expo_data_out[142] = 86;

            expo_data_in[143] = 143; expo_data_out[143] = 87;

            expo_data_in[144] = 144; expo_data_out[144] = 87;

            expo_data_in[145] = 145; expo_data_out[145] = 87;

            expo_data_in[146] = 146; expo_data_out[146] = 87;

            expo_data_in[147] = 147; expo_data_out[147] = 87;

            expo_data_in[148] = 148; expo_data_out[148] = 87;

            expo_data_in[149] = 149; expo_data_out[149] = 87;

            expo_data_in[150] = 150; expo_data_out[150] = 87;

            expo_data_in[151] = 151; expo_data_out[151] = 87;

            expo_data_in[152] = 152; expo_data_out[152] = 87;

            expo_data_in[153] = 153; expo_data_out[153] = 88;

            expo_data_in[154] = 154; expo_data_out[154] = 88;

            expo_data_in[155] = 155; expo_data_out[155] = 88;

            expo_data_in[156] = 156; expo_data_out[156] = 88;

            expo_data_in[157] = 157; expo_data_out[157] = 88;

            expo_data_in[158] = 158; expo_data_out[158] = 88;

            expo_data_in[159] = 159; expo_data_out[159] = 88;

            expo_data_in[160] = 160; expo_data_out[160] = 88;

            expo_data_in[161] = 161; expo_data_out[161] = 88;

            expo_data_in[162] = 162; expo_data_out[162] = 88;

            expo_data_in[163] = 163; expo_data_out[163] = 89;

            expo_data_in[164] = 164; expo_data_out[164] = 89;

            expo_data_in[165] = 165; expo_data_out[165] = 89;

            expo_data_in[166] = 166; expo_data_out[166] = 89;

            expo_data_in[167] = 167; expo_data_out[167] = 89;

            expo_data_in[168] = 168; expo_data_out[168] = 89;

            expo_data_in[169] = 169; expo_data_out[169] = 89;

            expo_data_in[170] = 170; expo_data_out[170] = 89;

            expo_data_in[171] = 171; expo_data_out[171] = 89;

            expo_data_in[172] = 172; expo_data_out[172] = 89;

            expo_data_in[173] = 173; expo_data_out[173] = 89;

            expo_data_in[174] = 174; expo_data_out[174] = 90;

            expo_data_in[175] = 175; expo_data_out[175] = 90;

            expo_data_in[176] = 176; expo_data_out[176] = 90;

            expo_data_in[177] = 177; expo_data_out[177] = 90;

            expo_data_in[178] = 178; expo_data_out[178] = 90;

            expo_data_in[179] = 179; expo_data_out[179] = 90;

            expo_data_in[180] = 180; expo_data_out[180] = 90;

            expo_data_in[181] = 181; expo_data_out[181] = 90;

            expo_data_in[182] = 182; expo_data_out[182] = 90;

            expo_data_in[183] = 183; expo_data_out[183] = 90;

            expo_data_in[184] = 184; expo_data_out[184] = 90;

            expo_data_in[185] = 185; expo_data_out[185] = 91;

            expo_data_in[186] = 186; expo_data_out[186] = 91;

            expo_data_in[187] = 187; expo_data_out[187] = 91;

            expo_data_in[188] = 188; expo_data_out[188] = 91;

            expo_data_in[189] = 189; expo_data_out[189] = 91;

            expo_data_in[190] = 190; expo_data_out[190] = 91;

            expo_data_in[191] = 191; expo_data_out[191] = 91;

            expo_data_in[192] = 192; expo_data_out[192] = 91;

            expo_data_in[193] = 193; expo_data_out[193] = 91;

            expo_data_in[194] = 194; expo_data_out[194] = 91;

            expo_data_in[195] = 195; expo_data_out[195] = 92;

            expo_data_in[196] = 196; expo_data_out[196] = 92;

            expo_data_in[197] = 197; expo_data_out[197] = 92;

            expo_data_in[198] = 198; expo_data_out[198] = 92;

            expo_data_in[199] = 199; expo_data_out[199] = 92;

            expo_data_in[200] = 200; expo_data_out[200] = 92;

            expo_data_in[201] = 201; expo_data_out[201] = 92;

            expo_data_in[202] = 202; expo_data_out[202] = 92;

            expo_data_in[203] = 203; expo_data_out[203] = 92;

            expo_data_in[204] = 204; expo_data_out[204] = 92;

            expo_data_in[205] = 205; expo_data_out[205] = 92;

            expo_data_in[206] = 206; expo_data_out[206] = 93;

            expo_data_in[207] = 207; expo_data_out[207] = 93;

            expo_data_in[208] = 208; expo_data_out[208] = 93;

            expo_data_in[209] = 209; expo_data_out[209] = 93;

            expo_data_in[210] = 210; expo_data_out[210] = 93;

            expo_data_in[211] = 211; expo_data_out[211] = 93;

            expo_data_in[212] = 212; expo_data_out[212] = 93;

            expo_data_in[213] = 213; expo_data_out[213] = 92;

            expo_data_in[214] = 214; expo_data_out[214] = 92;

            expo_data_in[215] = 215; expo_data_out[215] = 92;

            expo_data_in[216] = 216; expo_data_out[216] = 92;

            expo_data_in[217] = 217; expo_data_out[217] = 93;

            expo_data_in[218] = 218; expo_data_out[218] = 93;

            expo_data_in[219] = 219; expo_data_out[219] = 93;

            expo_data_in[220] = 220; expo_data_out[220] = 93;

            expo_data_in[221] = 221; expo_data_out[221] = 93;

            expo_data_in[222] = 222; expo_data_out[222] = 93;

            expo_data_in[223] = 223; expo_data_out[223] = 93;

            expo_data_in[224] = 224; expo_data_out[224] = 93;

            expo_data_in[225] = 225; expo_data_out[225] = 93;

            expo_data_in[226] = 226; expo_data_out[226] = 93;

            expo_data_in[227] = 227; expo_data_out[227] = 94;

            expo_data_in[228] = 228; expo_data_out[228] = 94;

            expo_data_in[229] = 229; expo_data_out[229] = 94;

            expo_data_in[230] = 230; expo_data_out[230] = 94;

            expo_data_in[231] = 231; expo_data_out[231] = 94;

            expo_data_in[232] = 232; expo_data_out[232] = 94;

            expo_data_in[233] = 233; expo_data_out[233] = 94;

            expo_data_in[234] = 234; expo_data_out[234] = 94;

            expo_data_in[235] = 235; expo_data_out[235] = 95;

            expo_data_in[236] = 236; expo_data_out[236] = 95;

            expo_data_in[237] = 237; expo_data_out[237] = 95;

            expo_data_in[238] = 238; expo_data_out[238] = 95;

            expo_data_in[239] = 239; expo_data_out[239] = 95;

            expo_data_in[240] = 240; expo_data_out[240] = 95;

            expo_data_in[241] = 241; expo_data_out[241] = 95;

            expo_data_in[242] = 242; expo_data_out[242] = 95;

            expo_data_in[243] = 243; expo_data_out[243] = 95;

            expo_data_in[244] = 244; expo_data_out[244] = 95;

            expo_data_in[245] = 245; expo_data_out[245] = 95;

            expo_data_in[246] = 246; expo_data_out[246] = 95;

            expo_data_in[247] = 247; expo_data_out[247] = 96;

            expo_data_in[248] = 248; expo_data_out[248] = 96;

            expo_data_in[249] = 249; expo_data_out[249] = 96;

            expo_data_in[250] = 250; expo_data_out[250] = 96;

            expo_data_in[251] = 251; expo_data_out[251] = 96;

            expo_data_in[252] = 252; expo_data_out[252] = 45;

            expo_data_in[253] = 253; expo_data_out[253] = 45;

            expo_data_in[254] = 254; expo_data_out[254] = 45;

            expo_data_in[255] = 255; expo_data_out[255] = 45;

            expo_data_in[256] = 256; expo_data_out[256] = 70;

            expo_data_in[257] = 257; expo_data_out[257] = 70;

            expo_data_in[258] = 258; expo_data_out[258] = 70;

            expo_data_in[259] = 259; expo_data_out[259] = 71;

            expo_data_in[260] = 260; expo_data_out[260] = 71;

            expo_data_in[261] = 261; expo_data_out[261] = 71;

            expo_data_in[262] = 262; expo_data_out[262] = 71;

            expo_data_in[263] = 263; expo_data_out[263] = 71;

            expo_data_in[264] = 264; expo_data_out[264] = 71;

            expo_data_in[265] = 265; expo_data_out[265] = 71;

            expo_data_in[266] = 266; expo_data_out[266] = 71;

            expo_data_in[267] = 267; expo_data_out[267] = 72;

            expo_data_in[268] = 268; expo_data_out[268] = 72;

            expo_data_in[269] = 269; expo_data_out[269] = 72;

            expo_data_in[270] = 270; expo_data_out[270] = 72;

            expo_data_in[271] = 271; expo_data_out[271] = 72;

            expo_data_in[272] = 272; expo_data_out[272] = 72;

            expo_data_in[273] = 273; expo_data_out[273] = 72;

            expo_data_in[274] = 274; expo_data_out[274] = 73;

            expo_data_in[275] = 275; expo_data_out[275] = 73;

            expo_data_in[276] = 276; expo_data_out[276] = 73;

            expo_data_in[277] = 277; expo_data_out[277] = 73;

            expo_data_in[278] = 278; expo_data_out[278] = 73;

            expo_data_in[279] = 279; expo_data_out[279] = 73;

            expo_data_in[280] = 280; expo_data_out[280] = 73;

            expo_data_in[281] = 281; expo_data_out[281] = 73;

            expo_data_in[282] = 282; expo_data_out[282] = 74;

            expo_data_in[283] = 283; expo_data_out[283] = 74;

            expo_data_in[284] = 284; expo_data_out[284] = 74;

            expo_data_in[285] = 285; expo_data_out[285] = 74;

            expo_data_in[286] = 286; expo_data_out[286] = 74;

            expo_data_in[287] = 287; expo_data_out[287] = 74;

            expo_data_in[288] = 288; expo_data_out[288] = 74;

            expo_data_in[289] = 289; expo_data_out[289] = 74;

            expo_data_in[290] = 290; expo_data_out[290] = 75;

            expo_data_in[291] = 291; expo_data_out[291] = 75;

            expo_data_in[292] = 292; expo_data_out[292] = 75;

            expo_data_in[293] = 293; expo_data_out[293] = 75;

            expo_data_in[294] = 294; expo_data_out[294] = 75;

            expo_data_in[295] = 295; expo_data_out[295] = 75;

            expo_data_in[296] = 296; expo_data_out[296] = 75;

            expo_data_in[297] = 297; expo_data_out[297] = 75;

            expo_data_in[298] = 298; expo_data_out[298] = 76;

            expo_data_in[299] = 299; expo_data_out[299] = 76;

            expo_data_in[300] = 300; expo_data_out[300] = 76;

            expo_data_in[301] = 301; expo_data_out[301] = 76;

            expo_data_in[302] = 302; expo_data_out[302] = 76;

            expo_data_in[303] = 303; expo_data_out[303] = 76;

            expo_data_in[304] = 304; expo_data_out[304] = 76;

            expo_data_in[305] = 305; expo_data_out[305] = 76;

            expo_data_in[306] = 306; expo_data_out[306] = 77;

            expo_data_in[307] = 307; expo_data_out[307] = 77;

            expo_data_in[308] = 308; expo_data_out[308] = 77;

            expo_data_in[309] = 309; expo_data_out[309] = 77;

            expo_data_in[310] = 310; expo_data_out[310] = 77;

            expo_data_in[311] = 311; expo_data_out[311] = 77;

            expo_data_in[312] = 312; expo_data_out[312] = 77;

            expo_data_in[313] = 313; expo_data_out[313] = 77;

            expo_data_in[314] = 314; expo_data_out[314] = 78;

            expo_data_in[315] = 315; expo_data_out[315] = 78;

            expo_data_in[316] = 316; expo_data_out[316] = 78;

            expo_data_in[317] = 317; expo_data_out[317] = 78;

            expo_data_in[318] = 318; expo_data_out[318] = 78;

            expo_data_in[319] = 319; expo_data_out[319] = 78;

            expo_data_in[320] = 320; expo_data_out[320] = 78;

            expo_data_in[321] = 321; expo_data_out[321] = 78;

            expo_data_in[322] = 322; expo_data_out[322] = 78;

            expo_data_in[323] = 323; expo_data_out[323] = 79;

            expo_data_in[324] = 324; expo_data_out[324] = 79;

            expo_data_in[325] = 325; expo_data_out[325] = 79;

            expo_data_in[326] = 326; expo_data_out[326] = 79;

            expo_data_in[327] = 327; expo_data_out[327] = 79;

            expo_data_in[328] = 328; expo_data_out[328] = 79;

            expo_data_in[329] = 329; expo_data_out[329] = 79;

            expo_data_in[330] = 330; expo_data_out[330] = 79;

            expo_data_in[331] = 331; expo_data_out[331] = 80;

            expo_data_in[332] = 332; expo_data_out[332] = 80;

            expo_data_in[333] = 333; expo_data_out[333] = 80;

            expo_data_in[334] = 334; expo_data_out[334] = 80;

            expo_data_in[335] = 335; expo_data_out[335] = 80;

            expo_data_in[336] = 336; expo_data_out[336] = 80;

            expo_data_in[337] = 337; expo_data_out[337] = 80;

            expo_data_in[338] = 338; expo_data_out[338] = 80;

            expo_data_in[339] = 339; expo_data_out[339] = 80;

            expo_data_in[340] = 340; expo_data_out[340] = 80;

            expo_data_in[341] = 341; expo_data_out[341] = 81;

            expo_data_in[342] = 342; expo_data_out[342] = 81;

            expo_data_in[343] = 343; expo_data_out[343] = 81;

            expo_data_in[344] = 344; expo_data_out[344] = 81;

            expo_data_in[345] = 345; expo_data_out[345] = 81;

            expo_data_in[346] = 346; expo_data_out[346] = 81;

            expo_data_in[347] = 347; expo_data_out[347] = 81;

            expo_data_in[348] = 348; expo_data_out[348] = 81;

            expo_data_in[349] = 349; expo_data_out[349] = 81;

            expo_data_in[350] = 350; expo_data_out[350] = 82;

            expo_data_in[351] = 351; expo_data_out[351] = 81;

            expo_data_in[352] = 352; expo_data_out[352] = 81;

            expo_data_in[353] = 353; expo_data_out[353] = 81;

            expo_data_in[354] = 354; expo_data_out[354] = 82;

            expo_data_in[355] = 355; expo_data_out[355] = 82;

            expo_data_in[356] = 356; expo_data_out[356] = 82;

            expo_data_in[357] = 357; expo_data_out[357] = 82;

            expo_data_in[358] = 358; expo_data_out[358] = 82;

            expo_data_in[359] = 359; expo_data_out[359] = 82;

            expo_data_in[360] = 360; expo_data_out[360] = 82;

            expo_data_in[361] = 361; expo_data_out[361] = 82;

            expo_data_in[362] = 362; expo_data_out[362] = 82;

            expo_data_in[363] = 363; expo_data_out[363] = 83;

            expo_data_in[364] = 364; expo_data_out[364] = 83;

            expo_data_in[365] = 365; expo_data_out[365] = 83;

            expo_data_in[366] = 366; expo_data_out[366] = 83;

            expo_data_in[367] = 367; expo_data_out[367] = 83;

            expo_data_in[368] = 368; expo_data_out[368] = 83;

            expo_data_in[369] = 369; expo_data_out[369] = 83;

            expo_data_in[370] = 370; expo_data_out[370] = 83;

            expo_data_in[371] = 371; expo_data_out[371] = 83;

            expo_data_in[372] = 372; expo_data_out[372] = 83;

            expo_data_in[373] = 373; expo_data_out[373] = 84;

            expo_data_in[374] = 374; expo_data_out[374] = 84;

            expo_data_in[375] = 375; expo_data_out[375] = 84;

            expo_data_in[376] = 376; expo_data_out[376] = 84;

            expo_data_in[377] = 377; expo_data_out[377] = 84;

            expo_data_in[378] = 378; expo_data_out[378] = 84;

            expo_data_in[379] = 379; expo_data_out[379] = 84;

            expo_data_in[380] = 380; expo_data_out[380] = 84;

            expo_data_in[381] = 381; expo_data_out[381] = 84;

            expo_data_in[382] = 382; expo_data_out[382] = 85;

            expo_data_in[383] = 383; expo_data_out[383] = 85;

            expo_data_in[384] = 384; expo_data_out[384] = 85;

            expo_data_in[385] = 385; expo_data_out[385] = 85;

            expo_data_in[386] = 386; expo_data_out[386] = 85;

            expo_data_in[387] = 387; expo_data_out[387] = 85;

            expo_data_in[388] = 388; expo_data_out[388] = 85;

            expo_data_in[389] = 389; expo_data_out[389] = 85;

            expo_data_in[390] = 390; expo_data_out[390] = 85;

            expo_data_in[391] = 391; expo_data_out[391] = 85;

            expo_data_in[392] = 392; expo_data_out[392] = 86;

            expo_data_in[393] = 393; expo_data_out[393] = 86;

            expo_data_in[394] = 394; expo_data_out[394] = 86;

            expo_data_in[395] = 395; expo_data_out[395] = 86;

            expo_data_in[396] = 396; expo_data_out[396] = 86;

            expo_data_in[397] = 397; expo_data_out[397] = 86;

            expo_data_in[398] = 398; expo_data_out[398] = 86;

            expo_data_in[399] = 399; expo_data_out[399] = 86;

            expo_data_in[400] = 400; expo_data_out[400] = 86;

            expo_data_in[401] = 401; expo_data_out[401] = 86;

            expo_data_in[402] = 402; expo_data_out[402] = 87;

            expo_data_in[403] = 403; expo_data_out[403] = 87;

            expo_data_in[404] = 404; expo_data_out[404] = 87;

            expo_data_in[405] = 405; expo_data_out[405] = 87;

            expo_data_in[406] = 406; expo_data_out[406] = 87;

            expo_data_in[407] = 407; expo_data_out[407] = 87;

            expo_data_in[408] = 408; expo_data_out[408] = 87;

            expo_data_in[409] = 409; expo_data_out[409] = 87;

            expo_data_in[410] = 410; expo_data_out[410] = 87;

            expo_data_in[411] = 411; expo_data_out[411] = 87;

            expo_data_in[412] = 412; expo_data_out[412] = 88;

            expo_data_in[413] = 413; expo_data_out[413] = 88;

            expo_data_in[414] = 414; expo_data_out[414] = 88;

            expo_data_in[415] = 415; expo_data_out[415] = 88;

            expo_data_in[416] = 416; expo_data_out[416] = 88;

            expo_data_in[417] = 417; expo_data_out[417] = 88;

            expo_data_in[418] = 418; expo_data_out[418] = 88;

            expo_data_in[419] = 419; expo_data_out[419] = 88;

            expo_data_in[420] = 420; expo_data_out[420] = 88;

            expo_data_in[421] = 421; expo_data_out[421] = 88;

            expo_data_in[422] = 422; expo_data_out[422] = 88;

            expo_data_in[423] = 423; expo_data_out[423] = 89;

            expo_data_in[424] = 424; expo_data_out[424] = 89;

            expo_data_in[425] = 425; expo_data_out[425] = 89;

            expo_data_in[426] = 426; expo_data_out[426] = 89;

            expo_data_in[427] = 427; expo_data_out[427] = 89;

            expo_data_in[428] = 428; expo_data_out[428] = 89;

            expo_data_in[429] = 429; expo_data_out[429] = 89;

            expo_data_in[430] = 430; expo_data_out[430] = 89;

            expo_data_in[431] = 431; expo_data_out[431] = 89;

            expo_data_in[432] = 432; expo_data_out[432] = 89;

            expo_data_in[433] = 433; expo_data_out[433] = 90;

            expo_data_in[434] = 434; expo_data_out[434] = 90;

            expo_data_in[435] = 435; expo_data_out[435] = 90;

            expo_data_in[436] = 436; expo_data_out[436] = 90;

            expo_data_in[437] = 437; expo_data_out[437] = 90;

            expo_data_in[438] = 438; expo_data_out[438] = 90;

            expo_data_in[439] = 439; expo_data_out[439] = 90;

            expo_data_in[440] = 440; expo_data_out[440] = 90;

            expo_data_in[441] = 441; expo_data_out[441] = 90;

            expo_data_in[442] = 442; expo_data_out[442] = 90;

            expo_data_in[443] = 443; expo_data_out[443] = 91;

            expo_data_in[444] = 444; expo_data_out[444] = 91;

            expo_data_in[445] = 445; expo_data_out[445] = 91;

            expo_data_in[446] = 446; expo_data_out[446] = 91;

            expo_data_in[447] = 447; expo_data_out[447] = 91;

            expo_data_in[448] = 448; expo_data_out[448] = 91;

            expo_data_in[449] = 449; expo_data_out[449] = 91;

            expo_data_in[450] = 450; expo_data_out[450] = 91;

            expo_data_in[451] = 451; expo_data_out[451] = 91;

            expo_data_in[452] = 452; expo_data_out[452] = 91;

            expo_data_in[453] = 453; expo_data_out[453] = 91;

            expo_data_in[454] = 454; expo_data_out[454] = 91;

            expo_data_in[455] = 455; expo_data_out[455] = 92;

            expo_data_in[456] = 456; expo_data_out[456] = 92;

            expo_data_in[457] = 457; expo_data_out[457] = 92;

            expo_data_in[458] = 458; expo_data_out[458] = 92;

            expo_data_in[459] = 459; expo_data_out[459] = 92;

            expo_data_in[460] = 460; expo_data_out[460] = 92;

            expo_data_in[461] = 461; expo_data_out[461] = 92;

            expo_data_in[462] = 462; expo_data_out[462] = 92;

            expo_data_in[463] = 463; expo_data_out[463] = 92;

            expo_data_in[464] = 464; expo_data_out[464] = 92;

            expo_data_in[465] = 465; expo_data_out[465] = 92;

            expo_data_in[466] = 466; expo_data_out[466] = 92;

            expo_data_in[467] = 467; expo_data_out[467] = 92;

            expo_data_in[468] = 468; expo_data_out[468] = 92;

            expo_data_in[469] = 469; expo_data_out[469] = 93;

            expo_data_in[470] = 470; expo_data_out[470] = 93;

            expo_data_in[471] = 471; expo_data_out[471] = 93;

            expo_data_in[472] = 472; expo_data_out[472] = 93;

            expo_data_in[473] = 473; expo_data_out[473] = 93;

            expo_data_in[474] = 474; expo_data_out[474] = 93;

            expo_data_in[475] = 475; expo_data_out[475] = 93;

            expo_data_in[476] = 476; expo_data_out[476] = 93;

            expo_data_in[477] = 477; expo_data_out[477] = 93;

            expo_data_in[478] = 478; expo_data_out[478] = 93;

            expo_data_in[479] = 479; expo_data_out[479] = 93;

            expo_data_in[480] = 480; expo_data_out[480] = 93;

            expo_data_in[481] = 481; expo_data_out[481] = 94;

            expo_data_in[482] = 482; expo_data_out[482] = 94;

            expo_data_in[483] = 483; expo_data_out[483] = 94;

            expo_data_in[484] = 484; expo_data_out[484] = 94;

            expo_data_in[485] = 485; expo_data_out[485] = 94;

            expo_data_in[486] = 486; expo_data_out[486] = 94;

            expo_data_in[487] = 487; expo_data_out[487] = 94;

            expo_data_in[488] = 488; expo_data_out[488] = 94;

            expo_data_in[489] = 489; expo_data_out[489] = 94;

            expo_data_in[490] = 490; expo_data_out[490] = 94;

            expo_data_in[491] = 491; expo_data_out[491] = 94;

            expo_data_in[492] = 492; expo_data_out[492] = 95;

            expo_data_in[493] = 493; expo_data_out[493] = 95;

            expo_data_in[494] = 494; expo_data_out[494] = 95;

            expo_data_in[495] = 495; expo_data_out[495] = 95;

            expo_data_in[496] = 496; expo_data_out[496] = 95;

            expo_data_in[497] = 497; expo_data_out[497] = 95;

            expo_data_in[498] = 498; expo_data_out[498] = 95;

            expo_data_in[499] = 499; expo_data_out[499] = 95;


            plotXY(expo_data_in, expo_data_out);
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //畫OV曲線 4
            int i;
            int N = 20;
            int[] data_x = new int[N];
            int[] data_y = new int[N];

            for (i = 0; i < N; i++)
            {
                data_x[i] = i;
                data_y[i] = (int)(Math.Sin(i) * 100 + 100);
            }
            plotXY(data_x, data_y);

        }

        private void button10_Click(object sender, EventArgs e)
        {
            //用GDI+畫圖

            Graphics g = this.pictureBox1.CreateGraphics();
            g.FillRectangle(Brushes.White, this.ClientRectangle);
            for (int i = 1; i <= 7; ++i)
            {
                //在窗體上面畫出橙色的矩形

                Rectangle r = new Rectangle(i * 40 - 15, 0, 15,
                this.ClientRectangle.Height);
                g.FillRectangle(Brushes.Orange, r);
            }
            //在內存中創建一個Bitmap並設置CompositingMode
            Bitmap bmp = new Bitmap(260, 260,

            System.Drawing.Imaging.PixelFormat.Format32bppArgb);
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

            this.Width = 1650;
            this.Height = 600;

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

