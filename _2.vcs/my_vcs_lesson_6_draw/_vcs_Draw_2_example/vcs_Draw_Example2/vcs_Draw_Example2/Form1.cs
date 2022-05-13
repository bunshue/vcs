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

namespace vcs_Draw_Example2
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;

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

            p = new Pen(Color.Red, 10);     // 設定畫筆為紅色、粗細為 10 點。
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
            x_st = 1050;
            y_st = 10;
            dx = 140;
            dy = 50;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button3.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            button4.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            button5.Location = new Point(x_st + dx * 5, y_st + dy * 0);

            button6.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button7.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button8.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button9.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            button10.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            button11.Location = new Point(x_st + dx * 5, y_st + dy * 1);

            button12.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button14.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button15.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            button16.Location = new Point(x_st + dx * 4, y_st + dy * 2);
            button17.Location = new Point(x_st + dx * 5, y_st + dy * 2);

            button18.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button21.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            button22.Location = new Point(x_st + dx * 4, y_st + dy * 3);
            button23.Location = new Point(x_st + dx * 5, y_st + dy * 3);

            button24.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button27.Location = new Point(x_st + dx * 3, y_st + dy * 4);
            button28.Location = new Point(x_st + dx * 4, y_st + dy * 4);
            button29.Location = new Point(x_st + dx * 5, y_st + dy * 4);

            button30.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button31.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button32.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button33.Location = new Point(x_st + dx * 3, y_st + dy * 5);
            button34.Location = new Point(x_st + dx * 4, y_st + dy * 5);
            button35.Location = new Point(x_st + dx * 5, y_st + dy * 5);

            button36.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button37.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button38.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button39.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            button40.Location = new Point(x_st + dx * 4, y_st + dy * 6);
            button41.Location = new Point(x_st + dx * 5, y_st + dy * 6);

            button42.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button43.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button44.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button45.Location = new Point(x_st + dx * 3, y_st + dy * 7);
            button46.Location = new Point(x_st + dx * 4, y_st + dy * 7);
            button47.Location = new Point(x_st + dx * 5, y_st + dy * 7);

            button48.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button49.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button50.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button51.Location = new Point(x_st + dx * 3, y_st + dy * 8);
            button52.Location = new Point(x_st + dx * 4, y_st + dy * 8);
            button53.Location = new Point(x_st + dx * 5, y_st + dy * 8);

            button54.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            button55.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            button56.Location = new Point(x_st + dx * 2, y_st + dy * 9);
            button57.Location = new Point(x_st + dx * 3, y_st + dy * 9);
            button58.Location = new Point(x_st + dx * 4, y_st + dy * 9);
            button59.Location = new Point(x_st + dx * 5, y_st + dy * 9);

            button60.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            button61.Location = new Point(x_st + dx * 1, y_st + dy * 10);
            button62.Location = new Point(x_st + dx * 2, y_st + dy * 10);
            button63.Location = new Point(x_st + dx * 3, y_st + dy * 10);
            button64.Location = new Point(x_st + dx * 4, y_st + dy * 10);
            button65.Location = new Point(x_st + dx * 5, y_st + dy * 10);

            button66.Location = new Point(x_st + dx * 0, y_st + dy * 11);
            button67.Location = new Point(x_st + dx * 1, y_st + dy * 11);
            button68.Location = new Point(x_st + dx * 2, y_st + dy * 11);
            button69.Location = new Point(x_st + dx * 3, y_st + dy * 11);
            button70.Location = new Point(x_st + dx * 4, y_st + dy * 11);
            button71.Location = new Point(x_st + dx * 5, y_st + dy * 11);

            groupBox1.Location = new Point(x_st + dx * 0, y_st + dy * 12);

            bt_reset.Location = new Point(x_st + dx * 4, y_st + dy * 15);
            bt_save.Location = new Point(x_st + dx * 5, y_st + dy * 15);

            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 16);
            richTextBox1.Size = new Size(richTextBox1.Size.Width + 200, 250);

            pictureBox1.Location = new Point(10, 10);
            pictureBox1.Size = new Size(900, 600);
            pictureBox1.BackColor = Color.White;

            pictureBox_wave.Location = new Point(10, 710);
            pictureBox_wave.Size = new Size(1024, 256);
            pictureBox_wave.BackColor = Color.Pink;

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            bt_exit_setup();
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
        }

        private void button6_Click(object sender, EventArgs e)
        {
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
        }

        private void button11_Click(object sender, EventArgs e)
        {
        }

        private void button12_Click(object sender, EventArgs e)
        {
        }

        private void button13_Click(object sender, EventArgs e)
        {
        }

        private void button14_Click(object sender, EventArgs e)
        {
        }

        private void button15_Click(object sender, EventArgs e)
        {
        }

        private void button16_Click(object sender, EventArgs e)
        {
        }

        private void button17_Click(object sender, EventArgs e)
        {
        }

        private void button18_Click(object sender, EventArgs e)
        {
        }

        private void button19_Click(object sender, EventArgs e)
        {
        }

        private void button20_Click(object sender, EventArgs e)
        {
        }

        private void button21_Click(object sender, EventArgs e)
        {
        }

        private void button22_Click(object sender, EventArgs e)
        {
        }

        private void button23_Click(object sender, EventArgs e)
        {
        }

        private void button24_Click(object sender, EventArgs e)
        {
        }

        private void button25_Click(object sender, EventArgs e)
        {
        }

        private void button26_Click(object sender, EventArgs e)
        {
        }

        private void button27_Click(object sender, EventArgs e)
        {
        }

        private void button28_Click(object sender, EventArgs e)
        {
        }

        private void button29_Click(object sender, EventArgs e)
        {
        }

        private void button30_Click(object sender, EventArgs e)
        {
        }

        private void button31_Click(object sender, EventArgs e)
        {
        }

        private void button32_Click(object sender, EventArgs e)
        {
        }

        private void button33_Click(object sender, EventArgs e)
        {
        }

        private void button34_Click(object sender, EventArgs e)
        {
        }

        private void button35_Click(object sender, EventArgs e)
        {
        }

        private void button36_Click(object sender, EventArgs e)
        {
        }

        private void button37_Click(object sender, EventArgs e)
        {
        }

        private void button38_Click(object sender, EventArgs e)
        {
        }

        private void button39_Click(object sender, EventArgs e)
        {
        }

        private void button40_Click(object sender, EventArgs e)
        {
        }

        private void button41_Click(object sender, EventArgs e)
        {
        }

        private void button42_Click(object sender, EventArgs e)
        {
        }

        private void button43_Click(object sender, EventArgs e)
        {
        }

        private void button44_Click(object sender, EventArgs e)
        {
        }

        private void button45_Click(object sender, EventArgs e)
        {
        }

        private void button46_Click(object sender, EventArgs e)
        {
        }

        private void button47_Click(object sender, EventArgs e)
        {
        }

        private void button48_Click(object sender, EventArgs e)
        {
        }

        private void button49_Click(object sender, EventArgs e)
        {
        }

        private void button50_Click(object sender, EventArgs e)
        {
        }

        private void button51_Click(object sender, EventArgs e)
        {
        }

        private void button52_Click(object sender, EventArgs e)
        {
        }

        private void button53_Click(object sender, EventArgs e)
        {
        }

        private void button54_Click(object sender, EventArgs e)
        {
        }

        private void button55_Click(object sender, EventArgs e)
        {
        }

        private void button56_Click(object sender, EventArgs e)
        {
        }

        private void button57_Click(object sender, EventArgs e)
        {
        }

        private void button58_Click(object sender, EventArgs e)
        {
        }

        private void button59_Click(object sender, EventArgs e)
        {
        }

        private void button60_Click(object sender, EventArgs e)
        {
        }

        private void button61_Click(object sender, EventArgs e)
        {
        }

        private void button62_Click(object sender, EventArgs e)
        {
        }

        private void button63_Click(object sender, EventArgs e)
        {
        }

        private void button64_Click(object sender, EventArgs e)
        {
        }

        private void button65_Click(object sender, EventArgs e)
        {
        }

        private void button66_Click(object sender, EventArgs e)
        {
        }

        private void button67_Click(object sender, EventArgs e)
        {
        }

        private void button68_Click(object sender, EventArgs e)
        {
        }

        private void button69_Click(object sender, EventArgs e)
        {
        }

        private void button70_Click(object sender, EventArgs e)
        {
        }

        private void button71_Click(object sender, EventArgs e)
        {
        }

        private void bt_long0_Click(object sender, EventArgs e)
        {
        }

        private void bt_long1_Click(object sender, EventArgs e)
        {
        }

        private void bt_long2_Click(object sender, EventArgs e)
        {
        }

        private void bt_long3_Click(object sender, EventArgs e)
        {
        }

        private void bt_long4_Click(object sender, EventArgs e)
        {
        }

        private void bt_long5_Click(object sender, EventArgs e)
        {
        }

        private void bt_long6_Click(object sender, EventArgs e)
        {
        }

        private void bt_long7_Click(object sender, EventArgs e)
        {
        }

        private void bt_long8_Click(object sender, EventArgs e)
        {
        }

        private void bt_long9_Click(object sender, EventArgs e)
        {
        }

        private void bt_long10_Click(object sender, EventArgs e)
        {
        }

        private void bt_long11_Click(object sender, EventArgs e)
        {
        }

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

        int x_st = 0;
        int y_st = 0;

        private void pictureBox_wave_Paint(object sender, PaintEventArgs e)
        {
            int W = 1024;
            int H = 256;
            int i;

            // Create pens.
            Pen redPen = new Pen(Color.Red, 4);
            Point[] curvePoints = new Point[W];    //一維陣列內有 W 個Point

            //畫紅色的分布
            for (i = 0; i < W; i++)
            {
                y_st = 256 * 1 - (int)(128 * (sind(x_st + i) + 1));
                //curvePoints[i].X = x_st;
                //curvePoints[i].Y = y_st;
                //richTextBox1.Text += y_st.ToString() + " ";
                //curvePoints[i].Y = 2 * i;

                if (y_st > 255)
                    y_st = 255;
                else if (y_st < 0)
                    y_st = 0;
                Pen p = new Pen(Color.Red, 1);
                p.Color = Color.FromArgb(y_st, y_st, y_st);
                e.Graphics.DrawLine(p, i, 0, i, 256);
            }
            //e.Graphics.DrawLines(redPen, curvePoints);   //畫直線
            x_st -= 5;

            for (i = 0; i < W; i++)
            {
                //richTextBox1.Text += c
            }
        }

        private void timer_wave_Tick(object sender, EventArgs e)
        {
            pictureBox_wave.Invalidate();
        }

    }
}

