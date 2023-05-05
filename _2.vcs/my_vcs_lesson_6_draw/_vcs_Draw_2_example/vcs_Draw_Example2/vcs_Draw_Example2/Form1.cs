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

            ucOscilloscope1.Location = new Point(10, 620);
            ucOscilloscope1.Size = new Size(1024, 200);
            ucOscilloscope1.BackColor = Color.Pink;

            pictureBox_wave.Location = new Point(10, 830);
            pictureBox_wave.Size = new Size(1024, 240);
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
            string filename1 = @"C:\_git\vcs\_1.data\______test_files1\_wav\start.wav";
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
            string filename = @"C:\_git\vcs\_1.data\______test_files1\_wav\start.wav";

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

        private void button20_Click(object sender, EventArgs e)
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
            Graphics g;

            //新建圖檔, 初始化畫布
            Bitmap bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;

            int i;
            double gamma;

            int[] data_in = new int[256];
            int[] data_out = new int[256];
            Point[] curvePoints = new Point[256];    //一維陣列內有 N 個Point

            Pen gammaPen = new Pen(Color.Red, 2);
            /*
                                                        gamma = 2.2;
                                                        //畫出真正的Gamma 2.2曲線
                                                        for (i = 0; i < 256; i++)
                                                        {
                                                            data_in[i] = i;
                                                            data_out[i] = (int)(Math.Pow(((double)data_in[i]) / 255, 1 / gamma) * 255);

                                                            curvePoints[i].X = data_in[i] * 3;
                                                            curvePoints[i].Y = 256 * 2 - 1 - data_out[i] * 2;
                                                        }
                                                        g.DrawLines(gammaPen, curvePoints);   //畫直線
            */




            gammaPen = new Pen(Color.Green, 2);

            data_in[0] = 0; data_out[0] = 92;
            data_in[1] = 1; data_out[1] = 96;
            data_in[2] = 2; data_out[2] = 99;
            data_in[3] = 3; data_out[3] = 103;
            data_in[4] = 4; data_out[4] = 106;
            data_in[5] = 5; data_out[5] = 108;
            data_in[6] = 6; data_out[6] = 111;
            data_in[7] = 7; data_out[7] = 113;
            data_in[8] = 8; data_out[8] = 115;
            data_in[9] = 9; data_out[9] = 117;
            data_in[10] = 10; data_out[10] = 120;
            data_in[11] = 11; data_out[11] = 122;
            data_in[12] = 12; data_out[12] = 123;
            data_in[13] = 13; data_out[13] = 125;
            data_in[14] = 14; data_out[14] = 127;
            data_in[15] = 15; data_out[15] = 129;
            data_in[16] = 16; data_out[16] = 132;
            data_in[17] = 17; data_out[17] = 135;
            data_in[18] = 18; data_out[18] = 138;
            data_in[19] = 19; data_out[19] = 141;
            data_in[20] = 20; data_out[20] = 143;
            data_in[21] = 21; data_out[21] = 146;
            data_in[22] = 22; data_out[22] = 148;
            data_in[23] = 23; data_out[23] = 151;
            data_in[24] = 24; data_out[24] = 153;
            data_in[25] = 25; data_out[25] = 155;
            data_in[26] = 26; data_out[26] = 158;
            data_in[27] = 27; data_out[27] = 160;
            data_in[28] = 28; data_out[28] = 162;
            data_in[29] = 29; data_out[29] = 164;
            data_in[30] = 30; data_out[30] = 166;
            data_in[31] = 31; data_out[31] = 167;
            data_in[32] = 32; data_out[32] = 153;
            data_in[33] = 33; data_out[33] = 157;
            data_in[34] = 34; data_out[34] = 160;
            data_in[35] = 35; data_out[35] = 163;
            data_in[36] = 36; data_out[36] = 166;
            data_in[37] = 37; data_out[37] = 169;
            data_in[38] = 38; data_out[38] = 171;
            data_in[39] = 39; data_out[39] = 174;
            data_in[40] = 40; data_out[40] = 176;
            data_in[41] = 41; data_out[41] = 179;
            data_in[42] = 42; data_out[42] = 181;
            data_in[43] = 43; data_out[43] = 183;
            data_in[44] = 44; data_out[44] = 185;
            data_in[45] = 45; data_out[45] = 187;
            data_in[46] = 46; data_out[46] = 189;
            data_in[47] = 47; data_out[47] = 191;
            data_in[48] = 48; data_out[48] = 170;
            data_in[49] = 49; data_out[49] = 173;
            data_in[50] = 50; data_out[50] = 177;
            data_in[51] = 51; data_out[51] = 180;
            data_in[52] = 52; data_out[52] = 183;
            data_in[53] = 53; data_out[53] = 185;
            data_in[54] = 54; data_out[54] = 188;
            data_in[55] = 55; data_out[55] = 190;
            data_in[56] = 56; data_out[56] = 192;
            data_in[57] = 57; data_out[57] = 195;
            data_in[58] = 58; data_out[58] = 197;
            data_in[59] = 59; data_out[59] = 198;
            data_in[60] = 60; data_out[60] = 200;
            data_in[61] = 61; data_out[61] = 202;
            data_in[62] = 62; data_out[62] = 203;
            data_in[63] = 63; data_out[63] = 205;
            data_in[64] = 64; data_out[64] = 183;
            data_in[65] = 65; data_out[65] = 187;
            data_in[66] = 66; data_out[66] = 190;
            data_in[67] = 67; data_out[67] = 193;
            data_in[68] = 68; data_out[68] = 195;
            data_in[69] = 69; data_out[69] = 198;
            data_in[70] = 70; data_out[70] = 200;
            data_in[71] = 71; data_out[71] = 202;
            data_in[72] = 72; data_out[72] = 204;
            data_in[73] = 73; data_out[73] = 205;
            data_in[74] = 74; data_out[74] = 207;
            data_in[75] = 75; data_out[75] = 208;
            data_in[76] = 76; data_out[76] = 210;
            data_in[77] = 77; data_out[77] = 211;
            data_in[78] = 78; data_out[78] = 212;
            data_in[79] = 79; data_out[79] = 213;
            data_in[80] = 80; data_out[80] = 193;
            data_in[81] = 81; data_out[81] = 196;
            data_in[82] = 82; data_out[82] = 199;
            data_in[83] = 83; data_out[83] = 201;
            data_in[84] = 84; data_out[84] = 204;
            data_in[85] = 85; data_out[85] = 206;
            data_in[86] = 86; data_out[86] = 208;
            data_in[87] = 87; data_out[87] = 209;
            data_in[88] = 88; data_out[88] = 211;
            data_in[89] = 89; data_out[89] = 212;
            data_in[90] = 90; data_out[90] = 213;
            data_in[91] = 91; data_out[91] = 215;
            data_in[92] = 92; data_out[92] = 216;
            data_in[93] = 93; data_out[93] = 216;
            data_in[94] = 94; data_out[94] = 217;
            data_in[95] = 95; data_out[95] = 218;
            data_in[96] = 96; data_out[96] = 201;
            data_in[97] = 97; data_out[97] = 203;
            data_in[98] = 98; data_out[98] = 206;
            data_in[99] = 99; data_out[99] = 208;
            data_in[100] = 100; data_out[100] = 210;
            data_in[101] = 101; data_out[101] = 212;
            data_in[102] = 102; data_out[102] = 213;
            data_in[103] = 103; data_out[103] = 214;
            data_in[104] = 104; data_out[104] = 216;
            data_in[105] = 105; data_out[105] = 217;
            data_in[106] = 106; data_out[106] = 217;
            data_in[107] = 107; data_out[107] = 218;
            data_in[108] = 108; data_out[108] = 219;
            data_in[109] = 109; data_out[109] = 219;
            data_in[110] = 110; data_out[110] = 220;
            data_in[111] = 111; data_out[111] = 220;
            data_in[112] = 112; data_out[112] = 207;
            data_in[113] = 113; data_out[113] = 209;
            data_in[114] = 114; data_out[114] = 211;
            data_in[115] = 115; data_out[115] = 213;
            data_in[116] = 116; data_out[116] = 214;
            data_in[117] = 117; data_out[117] = 216;
            data_in[118] = 118; data_out[118] = 217;
            data_in[119] = 119; data_out[119] = 218;
            data_in[120] = 120; data_out[120] = 218;
            data_in[121] = 121; data_out[121] = 219;
            data_in[122] = 122; data_out[122] = 220;
            data_in[123] = 123; data_out[123] = 220;
            data_in[124] = 124; data_out[124] = 221;
            data_in[125] = 125; data_out[125] = 221;
            data_in[126] = 126; data_out[126] = 221;
            data_in[127] = 127; data_out[127] = 222;
            data_in[128] = 128; data_out[128] = 131;
            data_in[129] = 129; data_out[129] = 135;
            data_in[130] = 130; data_out[130] = 138;
            data_in[131] = 131; data_out[131] = 140;
            data_in[132] = 132; data_out[132] = 143;
            data_in[133] = 133; data_out[133] = 146;
            data_in[134] = 134; data_out[134] = 148;
            data_in[135] = 135; data_out[135] = 151;
            data_in[136] = 136; data_out[136] = 153;
            data_in[137] = 137; data_out[137] = 155;
            data_in[138] = 138; data_out[138] = 157;
            data_in[139] = 139; data_out[139] = 159;
            data_in[140] = 140; data_out[140] = 161;
            data_in[141] = 141; data_out[141] = 163;
            data_in[142] = 142; data_out[142] = 165;
            data_in[143] = 143; data_out[143] = 167;
            data_in[144] = 144; data_out[144] = 170;
            data_in[145] = 145; data_out[145] = 173;
            data_in[146] = 146; data_out[146] = 177;
            data_in[147] = 147; data_out[147] = 180;
            data_in[148] = 148; data_out[148] = 183;
            data_in[149] = 149; data_out[149] = 185;
            data_in[150] = 150; data_out[150] = 188;
            data_in[151] = 151; data_out[151] = 190;
            data_in[152] = 152; data_out[152] = 193;
            data_in[153] = 153; data_out[153] = 195;
            data_in[154] = 154; data_out[154] = 197;
            data_in[155] = 155; data_out[155] = 199;
            data_in[156] = 156; data_out[156] = 200;
            data_in[157] = 157; data_out[157] = 202;
            data_in[158] = 158; data_out[158] = 203;
            data_in[159] = 159; data_out[159] = 205;
            data_in[160] = 160; data_out[160] = 193;
            data_in[161] = 161; data_out[161] = 196;
            data_in[162] = 162; data_out[162] = 199;
            data_in[163] = 163; data_out[163] = 201;
            data_in[164] = 164; data_out[164] = 204;
            data_in[165] = 165; data_out[165] = 206;
            data_in[166] = 166; data_out[166] = 207;
            data_in[167] = 167; data_out[167] = 209;
            data_in[168] = 168; data_out[168] = 211;
            data_in[169] = 169; data_out[169] = 212;
            data_in[170] = 170; data_out[170] = 213;
            data_in[171] = 171; data_out[171] = 214;
            data_in[172] = 172; data_out[172] = 215;
            data_in[173] = 173; data_out[173] = 216;
            data_in[174] = 174; data_out[174] = 217;
            data_in[175] = 175; data_out[175] = 218;
            data_in[176] = 176; data_out[176] = 206;
            data_in[177] = 177; data_out[177] = 209;
            data_in[178] = 178; data_out[178] = 211;
            data_in[179] = 179; data_out[179] = 213;
            data_in[180] = 180; data_out[180] = 214;
            data_in[181] = 181; data_out[181] = 216;
            data_in[182] = 182; data_out[182] = 217;
            data_in[183] = 183; data_out[183] = 218;
            data_in[184] = 184; data_out[184] = 218;
            data_in[185] = 185; data_out[185] = 219;
            data_in[186] = 186; data_out[186] = 220;
            data_in[187] = 187; data_out[187] = 220;
            data_in[188] = 188; data_out[188] = 221;
            data_in[189] = 189; data_out[189] = 221;
            data_in[190] = 190; data_out[190] = 221;
            data_in[191] = 191; data_out[191] = 222;
            data_in[192] = 192; data_out[192] = 215;
            data_in[193] = 193; data_out[193] = 216;
            data_in[194] = 194; data_out[194] = 217;
            data_in[195] = 195; data_out[195] = 218;
            data_in[196] = 196; data_out[196] = 219;
            data_in[197] = 197; data_out[197] = 220;
            data_in[198] = 198; data_out[198] = 221;
            data_in[199] = 199; data_out[199] = 221;
            data_in[200] = 200; data_out[200] = 222;
            data_in[201] = 201; data_out[201] = 222;
            data_in[202] = 202; data_out[202] = 222;
            data_in[203] = 203; data_out[203] = 222;
            data_in[204] = 204; data_out[204] = 223;
            data_in[205] = 205; data_out[205] = 223;
            data_in[206] = 206; data_out[206] = 223;
            data_in[207] = 207; data_out[207] = 223;
            data_in[208] = 208; data_out[208] = 219;
            data_in[209] = 209; data_out[209] = 220;
            data_in[210] = 210; data_out[210] = 220;
            data_in[211] = 211; data_out[211] = 221;
            data_in[212] = 212; data_out[212] = 222;
            data_in[213] = 213; data_out[213] = 222;
            data_in[214] = 214; data_out[214] = 222;
            data_in[215] = 215; data_out[215] = 223;
            data_in[216] = 216; data_out[216] = 223;
            data_in[217] = 217; data_out[217] = 223;
            data_in[218] = 218; data_out[218] = 223;
            data_in[219] = 219; data_out[219] = 224;
            data_in[220] = 220; data_out[220] = 224;
            data_in[221] = 221; data_out[221] = 224;
            data_in[222] = 222; data_out[222] = 224;
            data_in[223] = 223; data_out[223] = 224;
            data_in[224] = 224; data_out[224] = 221;
            data_in[225] = 225; data_out[225] = 221;
            data_in[226] = 226; data_out[226] = 222;
            data_in[227] = 227; data_out[227] = 222;
            data_in[228] = 228; data_out[228] = 223;
            data_in[229] = 229; data_out[229] = 223;
            data_in[230] = 230; data_out[230] = 223;
            data_in[231] = 231; data_out[231] = 223;
            data_in[232] = 232; data_out[232] = 224;
            data_in[233] = 233; data_out[233] = 224;
            data_in[234] = 234; data_out[234] = 224;
            data_in[235] = 235; data_out[235] = 224;
            data_in[236] = 236; data_out[236] = 224;
            data_in[237] = 237; data_out[237] = 224;
            data_in[238] = 238; data_out[238] = 224;
            data_in[239] = 239; data_out[239] = 224;
            data_in[240] = 240; data_out[240] = 222;
            data_in[241] = 241; data_out[241] = 223;
            data_in[242] = 242; data_out[242] = 223;
            data_in[243] = 243; data_out[243] = 223;
            data_in[244] = 244; data_out[244] = 223;
            data_in[245] = 245; data_out[245] = 224;
            data_in[246] = 246; data_out[246] = 224;
            data_in[247] = 247; data_out[247] = 224;
            data_in[248] = 248; data_out[248] = 224;
            data_in[249] = 249; data_out[249] = 224;
            data_in[250] = 250; data_out[250] = 224;
            data_in[251] = 251; data_out[251] = 224;
            data_in[252] = 252; data_out[252] = 225;
            data_in[253] = 253; data_out[253] = 225;
            data_in[254] = 254; data_out[254] = 225;
            data_in[255] = 255; data_out[255] = 225;

            for (i = 0; i < 256; i++)
            {
                curvePoints[i].X = data_in[i] * 3;
                curvePoints[i].Y = 256 * 2 - 1 - data_out[i] * 2;
            }
            //g.DrawLines(gammaPen, curvePoints);   //畫直線




            Pen bluePen = new Pen(Color.Blue, 2);





            data_in[0] = 0; data_out[0] = 93;
            data_in[1] = 1; data_out[1] = 97;
            data_in[2] = 2; data_out[2] = 100;
            data_in[3] = 3; data_out[3] = 103;
            data_in[4] = 4; data_out[4] = 107;
            data_in[5] = 5; data_out[5] = 109;
            data_in[6] = 6; data_out[6] = 112;
            data_in[7] = 7; data_out[7] = 115;
            data_in[8] = 8; data_out[8] = 118;
            data_in[9] = 9; data_out[9] = 120;
            data_in[10] = 10; data_out[10] = 123;
            data_in[11] = 11; data_out[11] = 126;
            data_in[12] = 12; data_out[12] = 128;
            data_in[13] = 13; data_out[13] = 130;
            data_in[14] = 14; data_out[14] = 133;
            data_in[15] = 15; data_out[15] = 135;
            data_in[16] = 16; data_out[16] = 139;
            data_in[17] = 17; data_out[17] = 143;
            data_in[18] = 18; data_out[18] = 147;
            data_in[19] = 19; data_out[19] = 151;
            data_in[20] = 20; data_out[20] = 154;
            data_in[21] = 21; data_out[21] = 157;
            data_in[22] = 22; data_out[22] = 160;
            data_in[23] = 23; data_out[23] = 164;
            data_in[24] = 24; data_out[24] = 166;
            data_in[25] = 25; data_out[25] = 169;
            data_in[26] = 26; data_out[26] = 172;
            data_in[27] = 27; data_out[27] = 175;
            data_in[28] = 28; data_out[28] = 178;
            data_in[29] = 29; data_out[29] = 180;
            data_in[30] = 30; data_out[30] = 183;
            data_in[31] = 31; data_out[31] = 185;
            data_in[32] = 32; data_out[32] = 168;
            data_in[33] = 33; data_out[33] = 173;
            data_in[34] = 34; data_out[34] = 177;
            data_in[35] = 35; data_out[35] = 181;
            data_in[36] = 36; data_out[36] = 185;
            data_in[37] = 37; data_out[37] = 188;
            data_in[38] = 38; data_out[38] = 192;
            data_in[39] = 39; data_out[39] = 195;
            data_in[40] = 40; data_out[40] = 198;
            data_in[41] = 41; data_out[41] = 201;
            data_in[42] = 42; data_out[42] = 204;
            data_in[43] = 43; data_out[43] = 207;
            data_in[44] = 44; data_out[44] = 209;
            data_in[45] = 45; data_out[45] = 212;
            data_in[46] = 46; data_out[46] = 214;
            data_in[47] = 47; data_out[47] = 216;
            data_in[48] = 48; data_out[48] = 188;
            data_in[49] = 49; data_out[49] = 193;
            data_in[50] = 50; data_out[50] = 197;
            data_in[51] = 51; data_out[51] = 201;
            data_in[52] = 52; data_out[52] = 204;
            data_in[53] = 53; data_out[53] = 208;
            data_in[54] = 54; data_out[54] = 211;
            data_in[55] = 55; data_out[55] = 214;
            data_in[56] = 56; data_out[56] = 217;
            data_in[57] = 57; data_out[57] = 219;
            data_in[58] = 58; data_out[58] = 222;
            data_in[59] = 59; data_out[59] = 224;
            data_in[60] = 60; data_out[60] = 226;
            data_in[61] = 61; data_out[61] = 228;
            data_in[62] = 62; data_out[62] = 230;
            data_in[63] = 63; data_out[63] = 231;
            data_in[64] = 64; data_out[64] = 209;
            data_in[65] = 65; data_out[65] = 213;
            data_in[66] = 66; data_out[66] = 217;
            data_in[67] = 67; data_out[67] = 221;
            data_in[68] = 68; data_out[68] = 224;
            data_in[69] = 69; data_out[69] = 227;
            data_in[70] = 70; data_out[70] = 229;
            data_in[71] = 71; data_out[71] = 232;
            data_in[72] = 72; data_out[72] = 234;
            data_in[73] = 73; data_out[73] = 236;
            data_in[74] = 74; data_out[74] = 237;
            data_in[75] = 75; data_out[75] = 239;
            data_in[76] = 76; data_out[76] = 240;
            data_in[77] = 77; data_out[77] = 241;
            data_in[78] = 78; data_out[78] = 242;
            data_in[79] = 79; data_out[79] = 243;
            data_in[80] = 80; data_out[80] = 220;
            data_in[81] = 81; data_out[81] = 224;
            data_in[82] = 82; data_out[82] = 227;
            data_in[83] = 83; data_out[83] = 230;
            data_in[84] = 84; data_out[84] = 232;
            data_in[85] = 85; data_out[85] = 235;
            data_in[86] = 86; data_out[86] = 236;
            data_in[87] = 87; data_out[87] = 238;
            data_in[88] = 88; data_out[88] = 240;
            data_in[89] = 89; data_out[89] = 241;
            data_in[90] = 90; data_out[90] = 242;
            data_in[91] = 91; data_out[91] = 243;
            data_in[92] = 92; data_out[92] = 244;
            data_in[93] = 93; data_out[93] = 245;
            data_in[94] = 94; data_out[94] = 245;
            data_in[95] = 95; data_out[95] = 246;
            data_in[96] = 96; data_out[96] = 230;
            data_in[97] = 97; data_out[97] = 233;
            data_in[98] = 98; data_out[98] = 235;
            data_in[99] = 99; data_out[99] = 237;
            data_in[100] = 100; data_out[100] = 239;
            data_in[101] = 101; data_out[101] = 241;
            data_in[102] = 102; data_out[102] = 242;
            data_in[103] = 103; data_out[103] = 243;
            data_in[104] = 104; data_out[104] = 244;
            data_in[105] = 105; data_out[105] = 245;
            data_in[106] = 106; data_out[106] = 246;
            data_in[107] = 107; data_out[107] = 247;
            data_in[108] = 108; data_out[108] = 247;
            data_in[109] = 109; data_out[109] = 248;
            data_in[110] = 110; data_out[110] = 248;
            data_in[111] = 111; data_out[111] = 248;
            data_in[112] = 112; data_out[112] = 233;
            data_in[113] = 113; data_out[113] = 236;
            data_in[114] = 114; data_out[114] = 238;
            data_in[115] = 115; data_out[115] = 239;
            data_in[116] = 116; data_out[116] = 241;
            data_in[117] = 117; data_out[117] = 242;
            data_in[118] = 118; data_out[118] = 243;
            data_in[119] = 119; data_out[119] = 244;
            data_in[120] = 120; data_out[120] = 245;
            data_in[121] = 121; data_out[121] = 246;
            data_in[122] = 122; data_out[122] = 246;
            data_in[123] = 123; data_out[123] = 247;
            data_in[124] = 124; data_out[124] = 248;
            data_in[125] = 125; data_out[125] = 248;
            data_in[126] = 126; data_out[126] = 249;
            data_in[127] = 127; data_out[127] = 249;
            data_in[128] = 128; data_out[128] = 138;
            data_in[129] = 129; data_out[129] = 142;
            data_in[130] = 130; data_out[130] = 146;
            data_in[131] = 131; data_out[131] = 150;
            data_in[132] = 132; data_out[132] = 154;
            data_in[133] = 133; data_out[133] = 157;
            data_in[134] = 134; data_out[134] = 160;
            data_in[135] = 135; data_out[135] = 163;
            data_in[136] = 136; data_out[136] = 166;
            data_in[137] = 137; data_out[137] = 169;
            data_in[138] = 138; data_out[138] = 172;
            data_in[139] = 139; data_out[139] = 174;
            data_in[140] = 140; data_out[140] = 177;
            data_in[141] = 141; data_out[141] = 180;
            data_in[142] = 142; data_out[142] = 182;
            data_in[143] = 143; data_out[143] = 184;
            data_in[144] = 144; data_out[144] = 188;
            data_in[145] = 145; data_out[145] = 193;
            data_in[146] = 146; data_out[146] = 197;
            data_in[147] = 147; data_out[147] = 201;
            data_in[148] = 148; data_out[148] = 205;
            data_in[149] = 149; data_out[149] = 208;
            data_in[150] = 150; data_out[150] = 211;
            data_in[151] = 151; data_out[151] = 214;
            data_in[152] = 152; data_out[152] = 217;
            data_in[153] = 153; data_out[153] = 219;
            data_in[154] = 154; data_out[154] = 222;
            data_in[155] = 155; data_out[155] = 224;
            data_in[156] = 156; data_out[156] = 226;
            data_in[157] = 157; data_out[157] = 228;
            data_in[158] = 158; data_out[158] = 230;
            data_in[159] = 159; data_out[159] = 231;
            data_in[160] = 160; data_out[160] = 219;
            data_in[161] = 161; data_out[161] = 223;
            data_in[162] = 162; data_out[162] = 227;
            data_in[163] = 163; data_out[163] = 230;
            data_in[164] = 164; data_out[164] = 232;
            data_in[165] = 165; data_out[165] = 234;
            data_in[166] = 166; data_out[166] = 236;
            data_in[167] = 167; data_out[167] = 238;
            data_in[168] = 168; data_out[168] = 239;
            data_in[169] = 169; data_out[169] = 241;
            data_in[170] = 170; data_out[170] = 242;
            data_in[171] = 171; data_out[171] = 243;
            data_in[172] = 172; data_out[172] = 244;
            data_in[173] = 173; data_out[173] = 245;
            data_in[174] = 174; data_out[174] = 245;
            data_in[175] = 175; data_out[175] = 246;
            data_in[176] = 176; data_out[176] = 233;
            data_in[177] = 177; data_out[177] = 236;
            data_in[178] = 178; data_out[178] = 238;
            data_in[179] = 179; data_out[179] = 239;
            data_in[180] = 180; data_out[180] = 241;
            data_in[181] = 181; data_out[181] = 242;
            data_in[182] = 182; data_out[182] = 243;
            data_in[183] = 183; data_out[183] = 244;
            data_in[184] = 184; data_out[184] = 245;
            data_in[185] = 185; data_out[185] = 246;
            data_in[186] = 186; data_out[186] = 246;
            data_in[187] = 187; data_out[187] = 247;
            data_in[188] = 188; data_out[188] = 248;
            data_in[189] = 189; data_out[189] = 248;
            data_in[190] = 190; data_out[190] = 248;
            data_in[191] = 191; data_out[191] = 249;
            data_in[192] = 192; data_out[192] = 244;
            data_in[193] = 193; data_out[193] = 246;
            data_in[194] = 194; data_out[194] = 247;
            data_in[195] = 195; data_out[195] = 248;
            data_in[196] = 196; data_out[196] = 248;
            data_in[197] = 197; data_out[197] = 249;
            data_in[198] = 198; data_out[198] = 249;
            data_in[199] = 199; data_out[199] = 250;
            data_in[200] = 200; data_out[200] = 250;
            data_in[201] = 201; data_out[201] = 250;
            data_in[202] = 202; data_out[202] = 251;
            data_in[203] = 203; data_out[203] = 251;
            data_in[204] = 204; data_out[204] = 251;
            data_in[205] = 205; data_out[205] = 251;
            data_in[206] = 206; data_out[206] = 251;
            data_in[207] = 207; data_out[207] = 251;
            data_in[208] = 208; data_out[208] = 247;
            data_in[209] = 209; data_out[209] = 248;
            data_in[210] = 210; data_out[210] = 248;
            data_in[211] = 211; data_out[211] = 249;
            data_in[212] = 212; data_out[212] = 249;
            data_in[213] = 213; data_out[213] = 250;
            data_in[214] = 214; data_out[214] = 250;
            data_in[215] = 215; data_out[215] = 250;
            data_in[216] = 216; data_out[216] = 250;
            data_in[217] = 217; data_out[217] = 251;
            data_in[218] = 218; data_out[218] = 251;
            data_in[219] = 219; data_out[219] = 251;
            data_in[220] = 220; data_out[220] = 251;
            data_in[221] = 221; data_out[221] = 251;
            data_in[222] = 222; data_out[222] = 251;
            data_in[223] = 223; data_out[223] = 251;
            data_in[224] = 224; data_out[224] = 249;
            data_in[225] = 225; data_out[225] = 249;
            data_in[226] = 226; data_out[226] = 250;
            data_in[227] = 227; data_out[227] = 250;
            data_in[228] = 228; data_out[228] = 250;
            data_in[229] = 229; data_out[229] = 251;
            data_in[230] = 230; data_out[230] = 251;
            data_in[231] = 231; data_out[231] = 251;
            data_in[232] = 232; data_out[232] = 251;
            data_in[233] = 233; data_out[233] = 251;
            data_in[234] = 234; data_out[234] = 251;
            data_in[235] = 235; data_out[235] = 252;
            data_in[236] = 236; data_out[236] = 252;
            data_in[237] = 237; data_out[237] = 252;
            data_in[238] = 238; data_out[238] = 252;
            data_in[239] = 239; data_out[239] = 252;
            data_in[240] = 240; data_out[240] = 249;
            data_in[241] = 241; data_out[241] = 250;
            data_in[242] = 242; data_out[242] = 250;
            data_in[243] = 243; data_out[243] = 251;
            data_in[244] = 244; data_out[244] = 251;
            data_in[245] = 245; data_out[245] = 251;
            data_in[246] = 246; data_out[246] = 251;
            data_in[247] = 247; data_out[247] = 251;
            data_in[248] = 248; data_out[248] = 252;
            data_in[249] = 249; data_out[249] = 252;
            data_in[250] = 250; data_out[250] = 252;
            data_in[251] = 251; data_out[251] = 252;
            data_in[252] = 252; data_out[252] = 252;
            data_in[253] = 253; data_out[253] = 252;
            data_in[254] = 254; data_out[254] = 252;
            data_in[255] = 255; data_out[255] = 252;





            for (i = 0; i < 256; i++)
            {
                curvePoints[i].X = data_in[i] * 3;
                curvePoints[i].Y = 256 * 2 - 1 - data_out[i] * 2;
            }
            g.DrawLines(bluePen, curvePoints);   //畫直線


            for (i = 0; i < 256; i++)
            {
                data_in[i] = 0;
                data_out[i] = 0;
                curvePoints[i].X = 0;
                curvePoints[i].Y = 0;
            }



            data_in[0] = 0; data_out[0] = 3;
            data_in[1] = 1; data_out[1] = 6;
            data_in[2] = 2; data_out[2] = 9;
            data_in[3] = 3; data_out[3] = 12;
            data_in[4] = 4; data_out[4] = 15;
            data_in[5] = 5; data_out[5] = 18;
            data_in[6] = 6; data_out[6] = 20;
            data_in[7] = 7; data_out[7] = 23;
            data_in[8] = 8; data_out[8] = 25;
            data_in[9] = 9; data_out[9] = 28;
            data_in[10] = 10; data_out[10] = 30;
            data_in[11] = 11; data_out[11] = 32;
            data_in[12] = 12; data_out[12] = 34;
            data_in[13] = 13; data_out[13] = 36;
            data_in[14] = 14; data_out[14] = 38;
            data_in[15] = 15; data_out[15] = 39;
            data_in[16] = 16; data_out[16] = 41;
            data_in[17] = 17; data_out[17] = 43;
            data_in[18] = 18; data_out[18] = 45;
            data_in[19] = 19; data_out[19] = 46;
            data_in[20] = 20; data_out[20] = 48;
            data_in[21] = 21; data_out[21] = 50;
            data_in[22] = 22; data_out[22] = 52;
            data_in[23] = 23; data_out[23] = 53;
            data_in[24] = 24; data_out[24] = 55;
            data_in[25] = 25; data_out[25] = 56;
            data_in[26] = 26; data_out[26] = 58;
            data_in[27] = 27; data_out[27] = 60;
            data_in[28] = 28; data_out[28] = 61;
            data_in[29] = 29; data_out[29] = 63;
            data_in[30] = 30; data_out[30] = 64;
            data_in[31] = 31; data_out[31] = 66;
            data_in[32] = 32; data_out[32] = 68;
            data_in[33] = 33; data_out[33] = 69;
            data_in[34] = 34; data_out[34] = 71;
            data_in[35] = 35; data_out[35] = 72;
            data_in[36] = 36; data_out[36] = 74;
            data_in[37] = 37; data_out[37] = 75;
            data_in[38] = 38; data_out[38] = 76;
            data_in[39] = 39; data_out[39] = 78;
            data_in[40] = 40; data_out[40] = 79;
            data_in[41] = 41; data_out[41] = 81;
            data_in[42] = 42; data_out[42] = 82;
            data_in[43] = 43; data_out[43] = 83;
            data_in[44] = 44; data_out[44] = 85;
            data_in[45] = 45; data_out[45] = 86;
            data_in[46] = 46; data_out[46] = 87;
            data_in[47] = 47; data_out[47] = 88;
            data_in[48] = 48; data_out[48] = 90;
            data_in[49] = 49; data_out[49] = 91;
            data_in[50] = 50; data_out[50] = 92;
            data_in[51] = 51; data_out[51] = 93;
            data_in[52] = 52; data_out[52] = 94;
            data_in[53] = 53; data_out[53] = 96;
            data_in[54] = 54; data_out[54] = 97;
            data_in[55] = 55; data_out[55] = 98;
            data_in[56] = 56; data_out[56] = 99;
            data_in[57] = 57; data_out[57] = 100;
            data_in[58] = 58; data_out[58] = 101;
            data_in[59] = 59; data_out[59] = 102;
            data_in[60] = 60; data_out[60] = 103;
            data_in[61] = 61; data_out[61] = 104;
            data_in[62] = 62; data_out[62] = 105;
            data_in[63] = 63; data_out[63] = 106;
            data_in[64] = 64; data_out[64] = 107;
            data_in[65] = 65; data_out[65] = 108;
            data_in[66] = 66; data_out[66] = 109;
            data_in[67] = 67; data_out[67] = 110;
            data_in[68] = 68; data_out[68] = 111;
            data_in[69] = 69; data_out[69] = 112;
            data_in[70] = 70; data_out[70] = 113;
            data_in[71] = 71; data_out[71] = 114;
            data_in[72] = 72; data_out[72] = 115;
            data_in[73] = 73; data_out[73] = 116;
            data_in[74] = 74; data_out[74] = 117;
            data_in[75] = 75; data_out[75] = 118;
            data_in[76] = 76; data_out[76] = 119;
            data_in[77] = 77; data_out[77] = 120;
            data_in[78] = 78; data_out[78] = 120;
            data_in[79] = 79; data_out[79] = 121;
            data_in[80] = 80; data_out[80] = 122;
            data_in[81] = 81; data_out[81] = 123;
            data_in[82] = 82; data_out[82] = 124;
            data_in[83] = 83; data_out[83] = 125;
            data_in[84] = 84; data_out[84] = 126;
            data_in[85] = 85; data_out[85] = 126;
            data_in[86] = 86; data_out[86] = 127;
            data_in[87] = 87; data_out[87] = 128;
            data_in[88] = 88; data_out[88] = 129;
            data_in[89] = 89; data_out[89] = 130;
            data_in[90] = 90; data_out[90] = 131;
            data_in[91] = 91; data_out[91] = 131;
            data_in[92] = 92; data_out[92] = 132;
            data_in[93] = 93; data_out[93] = 133;
            data_in[94] = 94; data_out[94] = 134;
            data_in[95] = 95; data_out[95] = 134;
            data_in[96] = 96; data_out[96] = 135;
            data_in[97] = 97; data_out[97] = 136;
            data_in[98] = 98; data_out[98] = 137;
            data_in[99] = 99; data_out[99] = 137;
            data_in[100] = 100; data_out[100] = 138;
            data_in[101] = 101; data_out[101] = 139;
            data_in[102] = 102; data_out[102] = 140;
            data_in[103] = 103; data_out[103] = 140;
            data_in[104] = 104; data_out[104] = 141;
            data_in[105] = 105; data_out[105] = 142;
            data_in[106] = 106; data_out[106] = 142;
            data_in[107] = 107; data_out[107] = 143;
            data_in[108] = 108; data_out[108] = 144;
            data_in[109] = 109; data_out[109] = 144;
            data_in[110] = 110; data_out[110] = 145;
            data_in[111] = 111; data_out[111] = 146;
            data_in[112] = 112; data_out[112] = 146;
            data_in[113] = 113; data_out[113] = 147;
            data_in[114] = 114; data_out[114] = 148;
            data_in[115] = 115; data_out[115] = 148;
            data_in[116] = 116; data_out[116] = 149;
            data_in[117] = 117; data_out[117] = 150;
            data_in[118] = 118; data_out[118] = 150;
            data_in[119] = 119; data_out[119] = 151;
            data_in[120] = 120; data_out[120] = 152;
            data_in[121] = 121; data_out[121] = 152;
            data_in[122] = 122; data_out[122] = 153;
            data_in[123] = 123; data_out[123] = 153;
            data_in[124] = 124; data_out[124] = 154;
            data_in[125] = 125; data_out[125] = 155;
            data_in[126] = 126; data_out[126] = 155;
            data_in[127] = 127; data_out[127] = 156;
            data_in[128] = 128; data_out[128] = 156;
            data_in[129] = 129; data_out[129] = 157;
            data_in[130] = 130; data_out[130] = 158;
            data_in[131] = 131; data_out[131] = 158;
            data_in[132] = 132; data_out[132] = 159;
            data_in[133] = 133; data_out[133] = 159;
            data_in[134] = 134; data_out[134] = 160;
            data_in[135] = 135; data_out[135] = 160;
            data_in[136] = 136; data_out[136] = 161;
            data_in[137] = 137; data_out[137] = 161;
            data_in[138] = 138; data_out[138] = 162;
            data_in[139] = 139; data_out[139] = 163;
            data_in[140] = 140; data_out[140] = 163;
            data_in[141] = 141; data_out[141] = 164;
            data_in[142] = 142; data_out[142] = 164;
            data_in[143] = 143; data_out[143] = 165;
            data_in[144] = 144; data_out[144] = 165;
            data_in[145] = 145; data_out[145] = 166;
            data_in[146] = 146; data_out[146] = 166;
            data_in[147] = 147; data_out[147] = 167;
            data_in[148] = 148; data_out[148] = 167;
            data_in[149] = 149; data_out[149] = 168;
            data_in[150] = 150; data_out[150] = 168;
            data_in[151] = 151; data_out[151] = 169;
            data_in[152] = 152; data_out[152] = 169;
            data_in[153] = 153; data_out[153] = 170;
            data_in[154] = 154; data_out[154] = 170;
            data_in[155] = 155; data_out[155] = 171;
            data_in[156] = 156; data_out[156] = 171;
            data_in[157] = 157; data_out[157] = 172;
            data_in[158] = 158; data_out[158] = 172;
            data_in[159] = 159; data_out[159] = 173;
            data_in[160] = 160; data_out[160] = 173;
            data_in[161] = 161; data_out[161] = 174;
            data_in[162] = 162; data_out[162] = 174;
            data_in[163] = 163; data_out[163] = 175;
            data_in[164] = 164; data_out[164] = 175;
            data_in[165] = 165; data_out[165] = 176;
            data_in[166] = 166; data_out[166] = 176;
            data_in[167] = 167; data_out[167] = 177;
            data_in[168] = 168; data_out[168] = 177;
            data_in[169] = 169; data_out[169] = 178;
            data_in[170] = 170; data_out[170] = 178;
            data_in[171] = 171; data_out[171] = 179;
            data_in[172] = 172; data_out[172] = 179;
            data_in[173] = 173; data_out[173] = 179;
            data_in[174] = 174; data_out[174] = 180;
            data_in[175] = 175; data_out[175] = 180;
            data_in[176] = 176; data_out[176] = 181;
            data_in[177] = 177; data_out[177] = 181;
            data_in[178] = 178; data_out[178] = 182;
            data_in[179] = 179; data_out[179] = 182;
            data_in[180] = 180; data_out[180] = 183;
            data_in[181] = 181; data_out[181] = 183;
            data_in[182] = 182; data_out[182] = 184;
            data_in[183] = 183; data_out[183] = 184;
            data_in[184] = 184; data_out[184] = 184;
            data_in[185] = 185; data_out[185] = 185;
            data_in[186] = 186; data_out[186] = 185;
            data_in[187] = 187; data_out[187] = 186;
            data_in[188] = 188; data_out[188] = 186;
            data_in[189] = 189; data_out[189] = 187;
            data_in[190] = 190; data_out[190] = 187;
            data_in[191] = 191; data_out[191] = 187;
            data_in[192] = 192; data_out[192] = 188;
            data_in[193] = 193; data_out[193] = 188;
            data_in[194] = 194; data_out[194] = 189;
            data_in[195] = 195; data_out[195] = 189;
            data_in[196] = 196; data_out[196] = 189;
            data_in[197] = 197; data_out[197] = 190;
            data_in[198] = 198; data_out[198] = 190;
            data_in[199] = 199; data_out[199] = 191;
            data_in[200] = 200; data_out[200] = 191;
            data_in[201] = 201; data_out[201] = 192;
            data_in[202] = 202; data_out[202] = 192;
            data_in[203] = 203; data_out[203] = 192;
            data_in[204] = 204; data_out[204] = 193;
            data_in[205] = 205; data_out[205] = 193;
            data_in[206] = 206; data_out[206] = 194;
            data_in[207] = 207; data_out[207] = 194;
            data_in[208] = 208; data_out[208] = 194;
            data_in[209] = 209; data_out[209] = 195;
            data_in[210] = 210; data_out[210] = 195;
            data_in[211] = 211; data_out[211] = 195;
            data_in[212] = 212; data_out[212] = 196;
            data_in[213] = 213; data_out[213] = 196;
            data_in[214] = 214; data_out[214] = 197;
            data_in[215] = 215; data_out[215] = 197;
            data_in[216] = 216; data_out[216] = 197;
            data_in[217] = 217; data_out[217] = 198;
            data_in[218] = 218; data_out[218] = 198;
            data_in[219] = 219; data_out[219] = 198;
            data_in[220] = 220; data_out[220] = 199;
            data_in[221] = 221; data_out[221] = 199;
            data_in[222] = 222; data_out[222] = 200;
            data_in[223] = 223; data_out[223] = 200;
            data_in[224] = 224; data_out[224] = 200;
            data_in[225] = 225; data_out[225] = 201;
            data_in[226] = 226; data_out[226] = 201;
            data_in[227] = 227; data_out[227] = 201;
            data_in[228] = 228; data_out[228] = 202;
            data_in[229] = 229; data_out[229] = 202;
            data_in[230] = 230; data_out[230] = 202;
            data_in[231] = 231; data_out[231] = 203;
            data_in[232] = 232; data_out[232] = 203;
            data_in[233] = 233; data_out[233] = 203;
            data_in[234] = 234; data_out[234] = 204;
            data_in[235] = 235; data_out[235] = 204;
            data_in[236] = 236; data_out[236] = 204;
            data_in[237] = 237; data_out[237] = 205;
            data_in[238] = 238; data_out[238] = 205;
            data_in[239] = 239; data_out[239] = 206;
            data_in[240] = 240; data_out[240] = 206;
            data_in[241] = 241; data_out[241] = 206;
            data_in[242] = 242; data_out[242] = 206;
            data_in[243] = 243; data_out[243] = 207;
            data_in[244] = 244; data_out[244] = 207;
            data_in[245] = 245; data_out[245] = 207;
            data_in[246] = 246; data_out[246] = 208;
            data_in[247] = 247; data_out[247] = 208;
            data_in[248] = 248; data_out[248] = 208;
            data_in[249] = 249; data_out[249] = 209;
            data_in[250] = 250; data_out[250] = 209;
            data_in[251] = 251; data_out[251] = 209;
            data_in[252] = 252; data_out[252] = 210;
            data_in[253] = 253; data_out[253] = 210;
            data_in[254] = 254; data_out[254] = 210;
            data_in[255] = 255; data_out[255] = 211;


            for (i = 0; i < 256; i++)
            {
                curvePoints[i].X = data_in[i] * 10;
                curvePoints[i].Y = 256 * 2 - 1 - data_out[i] * 2;
            }


            for (i = 135; i < 256; i++)
            {
                //curvePoints[i].X = i * 10;
                //curvePoints[i].Y = 256 * 2 - 1;
            }


            g.DrawLines(new Pen(Color.DarkRed, 10), curvePoints);   //畫直線



            data_in[0] = 0; data_out[0] = 59;
            data_in[1] = 1; data_out[1] = 62;
            data_in[2] = 2; data_out[2] = 64;
            data_in[3] = 3; data_out[3] = 67;
            data_in[4] = 4; data_out[4] = 69;
            data_in[5] = 5; data_out[5] = 71;
            data_in[6] = 6; data_out[6] = 73;
            data_in[7] = 7; data_out[7] = 75;
            data_in[8] = 8; data_out[8] = 78;
            data_in[9] = 9; data_out[9] = 79;
            data_in[10] = 10; data_out[10] = 81;
            data_in[11] = 11; data_out[11] = 83;
            data_in[12] = 12; data_out[12] = 85;
            data_in[13] = 13; data_out[13] = 87;
            data_in[14] = 14; data_out[14] = 88;
            data_in[15] = 15; data_out[15] = 90;
            data_in[16] = 16; data_out[16] = 93;
            data_in[17] = 17; data_out[17] = 96;
            data_in[18] = 18; data_out[18] = 99;
            data_in[19] = 19; data_out[19] = 103;
            data_in[20] = 20; data_out[20] = 105;
            data_in[21] = 21; data_out[21] = 108;
            data_in[22] = 22; data_out[22] = 111;
            data_in[23] = 23; data_out[23] = 114;
            data_in[24] = 24; data_out[24] = 116;
            data_in[25] = 25; data_out[25] = 118;
            data_in[26] = 26; data_out[26] = 121;
            data_in[27] = 27; data_out[27] = 123;
            data_in[28] = 28; data_out[28] = 126;
            data_in[29] = 29; data_out[29] = 128;
            data_in[30] = 30; data_out[30] = 130;
            data_in[31] = 31; data_out[31] = 132;
            data_in[32] = 32; data_out[32] = 135;
            data_in[33] = 33; data_out[33] = 138;
            data_in[34] = 34; data_out[34] = 141;
            data_in[35] = 35; data_out[35] = 143;
            data_in[36] = 36; data_out[36] = 146;
            data_in[37] = 37; data_out[37] = 149;
            data_in[38] = 38; data_out[38] = 151;
            data_in[39] = 39; data_out[39] = 153;
            data_in[40] = 40; data_out[40] = 156;
            data_in[41] = 41; data_out[41] = 158;
            data_in[42] = 42; data_out[42] = 160;
            data_in[43] = 43; data_out[43] = 161;
            data_in[44] = 44; data_out[44] = 163;
            data_in[45] = 45; data_out[45] = 166;
            data_in[46] = 46; data_out[46] = 168;
            data_in[47] = 47; data_out[47] = 171;
            data_in[48] = 48; data_out[48] = 173;
            data_in[49] = 49; data_out[49] = 175;
            data_in[50] = 50; data_out[50] = 177;
            data_in[51] = 51; data_out[51] = 178;
            data_in[52] = 52; data_out[52] = 181;
            data_in[53] = 53; data_out[53] = 184;
            data_in[54] = 54; data_out[54] = 186;
            data_in[55] = 55; data_out[55] = 189;
            data_in[56] = 56; data_out[56] = 191;
            data_in[57] = 57; data_out[57] = 194;
            data_in[58] = 58; data_out[58] = 196;
            data_in[59] = 59; data_out[59] = 198;
            data_in[60] = 60; data_out[60] = 200;
            data_in[61] = 61; data_out[61] = 204;
            data_in[62] = 62; data_out[62] = 206;
            data_in[63] = 63; data_out[63] = 210;
            data_in[64] = 64; data_out[64] = 212;
            data_in[65] = 65; data_out[65] = 217;
            data_in[66] = 66; data_out[66] = 223;
            data_in[67] = 67; data_out[67] = 228;
            data_in[68] = 68; data_out[68] = 236;
            data_in[69] = 69; data_out[69] = 237;


            for (i = 0; i < 70; i++)
            {
                curvePoints[i].X = data_in[i] * 10;
                curvePoints[i].Y = 256 * 2 - 1 - data_out[i] * 2;
            }


            for (i = 70; i < 256; i++)
            {
                curvePoints[i].X = i * 10;
                curvePoints[i].Y = 256 * 2 - 1;
            }


            //g.DrawLines(new Pen(Color.Purple, 4), curvePoints);   //畫直線



            Pen redPen = new Pen(Color.Red, 2);

            /*
   0    1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1
  32    0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0 1 0 1 1 1 1 1 1 1 1 1 1
             */


            for (i = 0; i < 256; i++)
            {
                data_in[i] = i; data_out[i] = 0;
            }

            for (i = 0; i < 32; i++)
            {
                data_out[i] = 200;
            }

            data_out[30] = 0;

            data_out[48] = 200;
            data_out[50] = 200;
            data_out[52] = 200;
            for (i = 54; i < 64; i++)
            {
                data_out[i] = 200;
            }

            for (i = 112; i < 128; i++)
            {
                data_out[i] = 200;
            }




            for (i = 0; i < 256; i++)
            {
                curvePoints[i].X = data_in[i] * 3;
                curvePoints[i].Y = 256 * 2 - 1 - data_out[i] * 2;
            }
            //g.DrawLines(redPen, curvePoints);   //畫直線


            int[] expo_data_in = new int[256];
            int[] expo_data_out = new int[256];
            int[] gain_data_in = new int[256];
            int[] gain_data_out = new int[256];




            expo_data_in[0] = 0; expo_data_out[0] = 3;

            expo_data_in[1] = 1; expo_data_out[1] = 3;

            expo_data_in[2] = 2; expo_data_out[2] = 4;

            expo_data_in[3] = 3; expo_data_out[3] = 5;

            expo_data_in[4] = 4; expo_data_out[4] = 6;

            expo_data_in[5] = 5; expo_data_out[5] = 7;

            expo_data_in[6] = 6; expo_data_out[6] = 9;

            expo_data_in[7] = 7; expo_data_out[7] = 10;

            expo_data_in[8] = 8; expo_data_out[8] = 11;

            expo_data_in[9] = 9; expo_data_out[9] = 12;

            expo_data_in[10] = 10; expo_data_out[10] = 13;

            expo_data_in[11] = 11; expo_data_out[11] = 14;

            expo_data_in[12] = 12; expo_data_out[12] = 15;

            expo_data_in[13] = 13; expo_data_out[13] = 16;

            expo_data_in[14] = 14; expo_data_out[14] = 17;

            expo_data_in[15] = 15; expo_data_out[15] = 19;

            expo_data_in[16] = 16; expo_data_out[16] = 20;

            expo_data_in[17] = 17; expo_data_out[17] = 20;

            expo_data_in[18] = 18; expo_data_out[18] = 21;

            expo_data_in[19] = 19; expo_data_out[19] = 22;

            expo_data_in[20] = 20; expo_data_out[20] = 23;

            expo_data_in[21] = 21; expo_data_out[21] = 24;

            expo_data_in[22] = 22; expo_data_out[22] = 25;

            expo_data_in[23] = 23; expo_data_out[23] = 26;

            expo_data_in[24] = 24; expo_data_out[24] = 27;

            expo_data_in[25] = 25; expo_data_out[25] = 28;

            expo_data_in[26] = 26; expo_data_out[26] = 28;

            expo_data_in[27] = 27; expo_data_out[27] = 29;

            expo_data_in[28] = 28; expo_data_out[28] = 30;

            expo_data_in[29] = 29; expo_data_out[29] = 31;

            expo_data_in[30] = 30; expo_data_out[30] = 32;

            expo_data_in[31] = 31; expo_data_out[31] = 32;

            expo_data_in[32] = 32; expo_data_out[32] = 33;

            expo_data_in[33] = 33; expo_data_out[33] = 34;

            expo_data_in[34] = 34; expo_data_out[34] = 35;

            expo_data_in[35] = 35; expo_data_out[35] = 35;

            expo_data_in[36] = 36; expo_data_out[36] = 36;

            expo_data_in[37] = 37; expo_data_out[37] = 37;

            expo_data_in[38] = 38; expo_data_out[38] = 37;

            expo_data_in[39] = 39; expo_data_out[39] = 38;

            expo_data_in[40] = 40; expo_data_out[40] = 39;

            expo_data_in[41] = 41; expo_data_out[41] = 39;

            expo_data_in[42] = 42; expo_data_out[42] = 40;

            expo_data_in[43] = 43; expo_data_out[43] = 41;

            expo_data_in[44] = 44; expo_data_out[44] = 41;

            expo_data_in[45] = 45; expo_data_out[45] = 42;

            expo_data_in[46] = 46; expo_data_out[46] = 43;

            expo_data_in[47] = 47; expo_data_out[47] = 43;

            expo_data_in[48] = 48; expo_data_out[48] = 44;

            expo_data_in[49] = 49; expo_data_out[49] = 45;

            expo_data_in[50] = 50; expo_data_out[50] = 45;

            expo_data_in[51] = 51; expo_data_out[51] = 46;

            expo_data_in[52] = 52; expo_data_out[52] = 47;

            expo_data_in[53] = 53; expo_data_out[53] = 47;

            expo_data_in[54] = 54; expo_data_out[54] = 48;

            expo_data_in[55] = 55; expo_data_out[55] = 48;

            expo_data_in[56] = 56; expo_data_out[56] = 49;

            expo_data_in[57] = 57; expo_data_out[57] = 50;

            expo_data_in[58] = 58; expo_data_out[58] = 50;

            expo_data_in[59] = 59; expo_data_out[59] = 51;

            expo_data_in[60] = 60; expo_data_out[60] = 52;

            expo_data_in[61] = 61; expo_data_out[61] = 52;

            expo_data_in[62] = 62; expo_data_out[62] = 53;

            expo_data_in[63] = 63; expo_data_out[63] = 53;

            expo_data_in[64] = 64; expo_data_out[64] = 54;

            expo_data_in[65] = 65; expo_data_out[65] = 55;

            expo_data_in[66] = 66; expo_data_out[66] = 55;

            expo_data_in[67] = 67; expo_data_out[67] = 56;

            expo_data_in[68] = 68; expo_data_out[68] = 56;

            expo_data_in[69] = 69; expo_data_out[69] = 57;

            expo_data_in[70] = 70; expo_data_out[70] = 58;

            expo_data_in[71] = 71; expo_data_out[71] = 58;

            expo_data_in[72] = 72; expo_data_out[72] = 59;

            expo_data_in[73] = 73; expo_data_out[73] = 59;

            expo_data_in[74] = 74; expo_data_out[74] = 60;

            expo_data_in[75] = 75; expo_data_out[75] = 61;

            expo_data_in[76] = 76; expo_data_out[76] = 61;

            expo_data_in[77] = 77; expo_data_out[77] = 62;

            expo_data_in[78] = 78; expo_data_out[78] = 62;

            expo_data_in[79] = 79; expo_data_out[79] = 63;

            expo_data_in[80] = 80; expo_data_out[80] = 64;

            expo_data_in[81] = 81; expo_data_out[81] = 64;

            expo_data_in[82] = 82; expo_data_out[82] = 65;

            expo_data_in[83] = 83; expo_data_out[83] = 65;

            expo_data_in[84] = 84; expo_data_out[84] = 66;

            expo_data_in[85] = 85; expo_data_out[85] = 66;

            expo_data_in[86] = 86; expo_data_out[86] = 67;

            expo_data_in[87] = 87; expo_data_out[87] = 68;

            expo_data_in[88] = 88; expo_data_out[88] = 68;

            expo_data_in[89] = 89; expo_data_out[89] = 69;

            expo_data_in[90] = 90; expo_data_out[90] = 69;

            expo_data_in[91] = 91; expo_data_out[91] = 70;

            expo_data_in[92] = 92; expo_data_out[92] = 70;

            expo_data_in[93] = 93; expo_data_out[93] = 71;

            expo_data_in[94] = 94; expo_data_out[94] = 72;

            expo_data_in[95] = 95; expo_data_out[95] = 72;

            expo_data_in[96] = 96; expo_data_out[96] = 73;

            expo_data_in[97] = 97; expo_data_out[97] = 73;

            expo_data_in[98] = 98; expo_data_out[98] = 74;

            expo_data_in[99] = 99; expo_data_out[99] = 74;

            expo_data_in[100] = 100; expo_data_out[100] = 75;

            expo_data_in[101] = 101; expo_data_out[101] = 75;

            expo_data_in[102] = 102; expo_data_out[102] = 76;

            expo_data_in[103] = 103; expo_data_out[103] = 76;

            expo_data_in[104] = 104; expo_data_out[104] = 77;

            expo_data_in[105] = 105; expo_data_out[105] = 77;

            expo_data_in[106] = 106; expo_data_out[106] = 78;

            expo_data_in[107] = 107; expo_data_out[107] = 78;

            expo_data_in[108] = 108; expo_data_out[108] = 79;

            expo_data_in[109] = 109; expo_data_out[109] = 80;

            expo_data_in[110] = 110; expo_data_out[110] = 80;

            expo_data_in[111] = 111; expo_data_out[111] = 81;

            expo_data_in[112] = 112; expo_data_out[112] = 81;

            expo_data_in[113] = 113; expo_data_out[113] = 82;

            expo_data_in[114] = 114; expo_data_out[114] = 82;

            expo_data_in[115] = 115; expo_data_out[115] = 83;

            expo_data_in[116] = 116; expo_data_out[116] = 83;

            expo_data_in[117] = 117; expo_data_out[117] = 84;

            expo_data_in[118] = 118; expo_data_out[118] = 84;

            expo_data_in[119] = 119; expo_data_out[119] = 85;

            expo_data_in[120] = 120; expo_data_out[120] = 85;

            expo_data_in[121] = 121; expo_data_out[121] = 86;

            expo_data_in[122] = 122; expo_data_out[122] = 86;

            expo_data_in[123] = 123; expo_data_out[123] = 86;

            expo_data_in[124] = 124; expo_data_out[124] = 87;

            expo_data_in[125] = 125; expo_data_out[125] = 87;

            expo_data_in[126] = 126; expo_data_out[126] = 88;

            expo_data_in[127] = 127; expo_data_out[127] = 88;

            expo_data_in[128] = 128; expo_data_out[128] = 89;

            expo_data_in[129] = 129; expo_data_out[129] = 89;

            expo_data_in[130] = 130; expo_data_out[130] = 90;

            expo_data_in[131] = 131; expo_data_out[131] = 90;

            expo_data_in[132] = 132; expo_data_out[132] = 91;

            expo_data_in[133] = 133; expo_data_out[133] = 91;

            expo_data_in[134] = 134; expo_data_out[134] = 92;



            gain_data_in[0] = 0; gain_data_out[0] = 91;

            gain_data_in[1] = 1; gain_data_out[1] = 96;

            gain_data_in[2] = 2; gain_data_out[2] = 99;

            gain_data_in[3] = 3; gain_data_out[3] = 102;

            gain_data_in[4] = 4; gain_data_out[4] = 106;

            gain_data_in[5] = 5; gain_data_out[5] = 108;

            gain_data_in[6] = 6; gain_data_out[6] = 111;

            gain_data_in[7] = 7; gain_data_out[7] = 114;

            gain_data_in[8] = 8; gain_data_out[8] = 117;

            gain_data_in[9] = 9; gain_data_out[9] = 119;

            gain_data_in[10] = 10; gain_data_out[10] = 122;

            gain_data_in[11] = 11; gain_data_out[11] = 125;

            gain_data_in[12] = 12; gain_data_out[12] = 127;

            gain_data_in[13] = 13; gain_data_out[13] = 129;

            gain_data_in[14] = 14; gain_data_out[14] = 132;

            gain_data_in[15] = 15; gain_data_out[15] = 134;

            gain_data_in[16] = 16; gain_data_out[16] = 138;

            gain_data_in[17] = 17; gain_data_out[17] = 142;

            gain_data_in[18] = 18; gain_data_out[18] = 146;

            gain_data_in[19] = 19; gain_data_out[19] = 150;

            gain_data_in[20] = 20; gain_data_out[20] = 153;

            gain_data_in[21] = 21; gain_data_out[21] = 156;

            gain_data_in[22] = 22; gain_data_out[22] = 160;

            gain_data_in[23] = 23; gain_data_out[23] = 163;

            gain_data_in[24] = 24; gain_data_out[24] = 166;

            gain_data_in[25] = 25; gain_data_out[25] = 169;

            gain_data_in[26] = 26; gain_data_out[26] = 171;

            gain_data_in[27] = 27; gain_data_out[27] = 174;

            gain_data_in[28] = 28; gain_data_out[28] = 177;

            gain_data_in[29] = 29; gain_data_out[29] = 179;

            gain_data_in[30] = 30; gain_data_out[30] = 182;

            gain_data_in[31] = 31; gain_data_out[31] = 184;

            gain_data_in[32] = 32; gain_data_out[32] = 167;

            gain_data_in[33] = 33; gain_data_out[33] = 172;

            gain_data_in[34] = 34; gain_data_out[34] = 176;

            gain_data_in[35] = 35; gain_data_out[35] = 180;

            gain_data_in[36] = 36; gain_data_out[36] = 184;

            gain_data_in[37] = 37; gain_data_out[37] = 188;

            gain_data_in[38] = 38; gain_data_out[38] = 191;

            gain_data_in[39] = 39; gain_data_out[39] = 194;

            gain_data_in[40] = 40; gain_data_out[40] = 197;

            gain_data_in[41] = 41; gain_data_out[41] = 200;

            gain_data_in[42] = 42; gain_data_out[42] = 203;

            gain_data_in[43] = 43; gain_data_out[43] = 206;

            gain_data_in[44] = 44; gain_data_out[44] = 209;

            gain_data_in[45] = 45; gain_data_out[45] = 211;

            gain_data_in[46] = 46; gain_data_out[46] = 214;

            gain_data_in[47] = 47; gain_data_out[47] = 216;

            gain_data_in[48] = 48; gain_data_out[48] = 188;

            gain_data_in[49] = 49; gain_data_out[49] = 192;

            gain_data_in[50] = 50; gain_data_out[50] = 196;

            gain_data_in[51] = 51; gain_data_out[51] = 200;

            gain_data_in[52] = 52; gain_data_out[52] = 204;

            gain_data_in[53] = 53; gain_data_out[53] = 207;

            gain_data_in[54] = 54; gain_data_out[54] = 210;

            gain_data_in[55] = 55; gain_data_out[55] = 214;

            gain_data_in[56] = 56; gain_data_out[56] = 216;

            gain_data_in[57] = 57; gain_data_out[57] = 219;

            gain_data_in[58] = 58; gain_data_out[58] = 221;

            gain_data_in[59] = 59; gain_data_out[59] = 224;

            gain_data_in[60] = 60; gain_data_out[60] = 226;

            gain_data_in[61] = 61; gain_data_out[61] = 228;

            gain_data_in[62] = 62; gain_data_out[62] = 230;

            gain_data_in[63] = 63; gain_data_out[63] = 231;

            gain_data_in[64] = 64; gain_data_out[64] = 208;

            gain_data_in[65] = 65; gain_data_out[65] = 213;

            gain_data_in[66] = 66; gain_data_out[66] = 217;

            gain_data_in[67] = 67; gain_data_out[67] = 220;

            gain_data_in[68] = 68; gain_data_out[68] = 224;

            gain_data_in[69] = 69; gain_data_out[69] = 227;

            gain_data_in[70] = 70; gain_data_out[70] = 229;

            gain_data_in[71] = 71; gain_data_out[71] = 232;

            gain_data_in[72] = 72; gain_data_out[72] = 234;

            gain_data_in[73] = 73; gain_data_out[73] = 236;

            gain_data_in[74] = 74; gain_data_out[74] = 237;

            gain_data_in[75] = 75; gain_data_out[75] = 239;

            gain_data_in[76] = 76; gain_data_out[76] = 240;

            gain_data_in[77] = 77; gain_data_out[77] = 241;

            gain_data_in[78] = 78; gain_data_out[78] = 242;

            gain_data_in[79] = 79; gain_data_out[79] = 243;

            gain_data_in[80] = 80; gain_data_out[80] = 219;

            gain_data_in[81] = 81; gain_data_out[81] = 223;

            gain_data_in[82] = 82; gain_data_out[82] = 227;

            gain_data_in[83] = 83; gain_data_out[83] = 230;

            gain_data_in[84] = 84; gain_data_out[84] = 233;

            gain_data_in[85] = 85; gain_data_out[85] = 235;

            gain_data_in[86] = 86; gain_data_out[86] = 237;

            gain_data_in[87] = 87; gain_data_out[87] = 238;

            gain_data_in[88] = 88; gain_data_out[88] = 240;

            gain_data_in[89] = 89; gain_data_out[89] = 241;

            gain_data_in[90] = 90; gain_data_out[90] = 242;

            gain_data_in[91] = 91; gain_data_out[91] = 243;

            gain_data_in[92] = 92; gain_data_out[92] = 244;

            gain_data_in[93] = 93; gain_data_out[93] = 245;

            gain_data_in[94] = 94; gain_data_out[94] = 245;

            gain_data_in[95] = 95; gain_data_out[95] = 246;

            gain_data_in[96] = 96; gain_data_out[96] = 229;

            gain_data_in[97] = 97; gain_data_out[97] = 233;

            gain_data_in[98] = 98; gain_data_out[98] = 235;

            gain_data_in[99] = 99; gain_data_out[99] = 238;

            gain_data_in[100] = 100; gain_data_out[100] = 239;

            gain_data_in[101] = 101; gain_data_out[101] = 241;

            gain_data_in[102] = 102; gain_data_out[102] = 242;

            gain_data_in[103] = 103; gain_data_out[103] = 243;

            gain_data_in[104] = 104; gain_data_out[104] = 244;

            gain_data_in[105] = 105; gain_data_out[105] = 245;

            gain_data_in[106] = 106; gain_data_out[106] = 246;

            gain_data_in[107] = 107; gain_data_out[107] = 247;

            gain_data_in[108] = 108; gain_data_out[108] = 247;

            gain_data_in[109] = 109; gain_data_out[109] = 248;

            gain_data_in[110] = 110; gain_data_out[110] = 248;

            gain_data_in[111] = 111; gain_data_out[111] = 248;

            gain_data_in[112] = 112; gain_data_out[112] = 233;

            gain_data_in[113] = 113; gain_data_out[113] = 236;

            gain_data_in[114] = 114; gain_data_out[114] = 238;

            gain_data_in[115] = 115; gain_data_out[115] = 240;

            gain_data_in[116] = 116; gain_data_out[116] = 241;

            gain_data_in[117] = 117; gain_data_out[117] = 242;

            gain_data_in[118] = 118; gain_data_out[118] = 243;

            gain_data_in[119] = 119; gain_data_out[119] = 244;

            gain_data_in[120] = 120; gain_data_out[120] = 245;

            gain_data_in[121] = 121; gain_data_out[121] = 246;

            gain_data_in[122] = 122; gain_data_out[122] = 246;

            gain_data_in[123] = 123; gain_data_out[123] = 247;

            gain_data_in[124] = 124; gain_data_out[124] = 247;

            gain_data_in[125] = 125; gain_data_out[125] = 248;

            gain_data_in[126] = 126; gain_data_out[126] = 248;

            gain_data_in[127] = 127; gain_data_out[127] = 249;


            expo_data_in[135] = 135; expo_data_out[135] = 249;

            expo_data_in[136] = 136; expo_data_out[136] = 249;

            expo_data_in[137] = 137; expo_data_out[137] = 249;

            expo_data_in[138] = 138; expo_data_out[138] = 249;

            expo_data_in[139] = 139; expo_data_out[139] = 249;

            expo_data_in[140] = 140; expo_data_out[140] = 249;

            expo_data_in[141] = 141; expo_data_out[141] = 249;

            expo_data_in[142] = 142; expo_data_out[142] = 249;

            expo_data_in[143] = 143; expo_data_out[143] = 249;

            expo_data_in[144] = 144; expo_data_out[144] = 249;

            expo_data_in[145] = 145; expo_data_out[145] = 249;

            expo_data_in[146] = 146; expo_data_out[146] = 250;

            expo_data_in[147] = 147; expo_data_out[147] = 250;

            expo_data_in[148] = 148; expo_data_out[148] = 250;

            expo_data_in[149] = 149; expo_data_out[149] = 250;

            expo_data_in[150] = 150; expo_data_out[150] = 250;

            expo_data_in[151] = 151; expo_data_out[151] = 250;

            expo_data_in[152] = 152; expo_data_out[152] = 250;

            expo_data_in[153] = 153; expo_data_out[153] = 250;

            expo_data_in[154] = 154; expo_data_out[154] = 250;

            expo_data_in[155] = 155; expo_data_out[155] = 250;

            expo_data_in[156] = 156; expo_data_out[156] = 250;

            expo_data_in[157] = 157; expo_data_out[157] = 250;

            expo_data_in[158] = 158; expo_data_out[158] = 250;

            expo_data_in[159] = 159; expo_data_out[159] = 250;

            expo_data_in[160] = 160; expo_data_out[160] = 250;

            expo_data_in[161] = 161; expo_data_out[161] = 250;

            expo_data_in[162] = 162; expo_data_out[162] = 250;

            expo_data_in[163] = 163; expo_data_out[163] = 250;

            expo_data_in[164] = 164; expo_data_out[164] = 250;

            expo_data_in[165] = 165; expo_data_out[165] = 250;

            expo_data_in[166] = 166; expo_data_out[166] = 251;

            expo_data_in[167] = 167; expo_data_out[167] = 251;

            expo_data_in[168] = 168; expo_data_out[168] = 251;

            expo_data_in[169] = 169; expo_data_out[169] = 251;

            expo_data_in[170] = 170; expo_data_out[170] = 251;

            expo_data_in[171] = 171; expo_data_out[171] = 251;

            expo_data_in[172] = 172; expo_data_out[172] = 251;

            expo_data_in[173] = 173; expo_data_out[173] = 251;

            expo_data_in[174] = 174; expo_data_out[174] = 251;

            expo_data_in[175] = 175; expo_data_out[175] = 251;

            expo_data_in[176] = 176; expo_data_out[176] = 251;

            expo_data_in[177] = 177; expo_data_out[177] = 251;

            expo_data_in[178] = 178; expo_data_out[178] = 251;

            expo_data_in[179] = 179; expo_data_out[179] = 251;

            expo_data_in[180] = 180; expo_data_out[180] = 251;

            expo_data_in[181] = 181; expo_data_out[181] = 251;

            expo_data_in[182] = 182; expo_data_out[182] = 251;

            expo_data_in[183] = 183; expo_data_out[183] = 251;

            expo_data_in[184] = 184; expo_data_out[184] = 251;

            expo_data_in[185] = 185; expo_data_out[185] = 251;

            expo_data_in[186] = 186; expo_data_out[186] = 251;

            expo_data_in[187] = 187; expo_data_out[187] = 251;

            expo_data_in[188] = 188; expo_data_out[188] = 251;

            expo_data_in[189] = 189; expo_data_out[189] = 251;

            expo_data_in[190] = 190; expo_data_out[190] = 251;

            expo_data_in[191] = 191; expo_data_out[191] = 251;

            expo_data_in[192] = 192; expo_data_out[192] = 251;

            expo_data_in[193] = 193; expo_data_out[193] = 251;

            expo_data_in[194] = 194; expo_data_out[194] = 251;

            expo_data_in[195] = 195; expo_data_out[195] = 251;

            expo_data_in[196] = 196; expo_data_out[196] = 251;

            expo_data_in[197] = 197; expo_data_out[197] = 251;

            expo_data_in[198] = 198; expo_data_out[198] = 251;

            expo_data_in[199] = 199; expo_data_out[199] = 251;

            expo_data_in[200] = 200; expo_data_out[200] = 251;

            expo_data_in[201] = 201; expo_data_out[201] = 251;

            expo_data_in[202] = 202; expo_data_out[202] = 251;

            expo_data_in[203] = 203; expo_data_out[203] = 252;

            expo_data_in[204] = 204; expo_data_out[204] = 252;

            expo_data_in[205] = 205; expo_data_out[205] = 252;

            expo_data_in[206] = 206; expo_data_out[206] = 252;

            expo_data_in[207] = 207; expo_data_out[207] = 252;

            expo_data_in[208] = 208; expo_data_out[208] = 252;

            expo_data_in[209] = 209; expo_data_out[209] = 252;

            expo_data_in[210] = 210; expo_data_out[210] = 252;

            expo_data_in[211] = 211; expo_data_out[211] = 252;

            expo_data_in[212] = 212; expo_data_out[212] = 252;

            expo_data_in[213] = 213; expo_data_out[213] = 252;

            expo_data_in[214] = 214; expo_data_out[214] = 252;

            expo_data_in[215] = 215; expo_data_out[215] = 252;

            expo_data_in[216] = 216; expo_data_out[216] = 252;

            expo_data_in[217] = 217; expo_data_out[217] = 252;

            expo_data_in[218] = 218; expo_data_out[218] = 252;

            expo_data_in[219] = 219; expo_data_out[219] = 252;

            expo_data_in[220] = 220; expo_data_out[220] = 252;

            expo_data_in[221] = 221; expo_data_out[221] = 252;

            expo_data_in[222] = 222; expo_data_out[222] = 252;

            expo_data_in[223] = 223; expo_data_out[223] = 252;

            expo_data_in[224] = 224; expo_data_out[224] = 252;

            expo_data_in[225] = 225; expo_data_out[225] = 252;

            expo_data_in[226] = 226; expo_data_out[226] = 252;

            expo_data_in[227] = 227; expo_data_out[227] = 252;

            expo_data_in[228] = 228; expo_data_out[228] = 252;

            expo_data_in[229] = 229; expo_data_out[229] = 252;

            expo_data_in[230] = 230; expo_data_out[230] = 252;

            expo_data_in[231] = 231; expo_data_out[231] = 252;

            expo_data_in[232] = 232; expo_data_out[232] = 252;

            expo_data_in[233] = 233; expo_data_out[233] = 252;

            expo_data_in[234] = 234; expo_data_out[234] = 252;

            expo_data_in[235] = 235; expo_data_out[235] = 252;

            expo_data_in[236] = 236; expo_data_out[236] = 252;

            expo_data_in[237] = 237; expo_data_out[237] = 252;

            expo_data_in[238] = 238; expo_data_out[238] = 252;

            expo_data_in[239] = 239; expo_data_out[239] = 252;

            expo_data_in[240] = 240; expo_data_out[240] = 252;

            expo_data_in[241] = 241; expo_data_out[241] = 252;

            expo_data_in[242] = 242; expo_data_out[242] = 252;

            expo_data_in[243] = 243; expo_data_out[243] = 252;

            expo_data_in[244] = 244; expo_data_out[244] = 252;

            expo_data_in[245] = 245; expo_data_out[245] = 252;

            expo_data_in[246] = 246; expo_data_out[246] = 252;

            expo_data_in[247] = 247; expo_data_out[247] = 252;

            expo_data_in[248] = 248; expo_data_out[248] = 252;

            expo_data_in[249] = 249; expo_data_out[249] = 252;

            expo_data_in[250] = 250; expo_data_out[250] = 252;

            expo_data_in[251] = 251; expo_data_out[251] = 252;

            expo_data_in[252] = 252; expo_data_out[252] = 252;

            expo_data_in[253] = 253; expo_data_out[253] = 252;

            expo_data_in[254] = 254; expo_data_out[254] = 252;

            expo_data_in[255] = 255; expo_data_out[255] = 252;









            for (i = 0; i < 256; i++)
            {
                curvePoints[i].X = 0;
                curvePoints[i].Y = 0;
            }


            for (i = 0; i < 256; i++)
            {
                curvePoints[i].X = expo_data_in[i] * 3;
                curvePoints[i].Y = 256 * 2 - 1 - expo_data_out[i] * 2;
            }

            //g.DrawLines(new Pen(Color.Green, 10), curvePoints);   //畫直線

            for (i = 0; i < 256; i++)
            {
                curvePoints[i].X = gain_data_in[i] * 3;
                curvePoints[i].Y = 256 * 2 - 1 - gain_data_out[i] * 2;
            }

            g.DrawLines(new Pen(Color.Navy, 10), curvePoints);   //畫直線























            g.DrawRectangle(new Pen(Color.Red), new Rectangle(0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1));

            pictureBox1.Image = bitmap1;

        }

        private void button25_Click(object sender, EventArgs e)
        {
            //畫OV亮度圖2

            Graphics g;
            //新建圖檔, 初始化畫布
            Bitmap bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;

            int i;

            int[] expo_data_in = new int[135];
            int[] expo_data_out = new int[135];

            int[] data_in = new int[64];
            int[] data_out = new int[64];

            Point[] curvePoints = new Point[135 + 64];    //一維陣列內有 N 個Point

            for (i = 0; i < (135 + 64); i++)
            {
                curvePoints[i].X = 0;
                curvePoints[i].Y = 0;
            }


            expo_data_in[0] = 0; expo_data_out[0] = 3;
            expo_data_in[1] = 1; expo_data_out[1] = 4;
            expo_data_in[2] = 2; expo_data_out[2] = 5;
            expo_data_in[3] = 3; expo_data_out[3] = 6;
            expo_data_in[4] = 4; expo_data_out[4] = 7;
            expo_data_in[5] = 5; expo_data_out[5] = 9;
            expo_data_in[6] = 6; expo_data_out[6] = 10;
            expo_data_in[7] = 7; expo_data_out[7] = 11;
            expo_data_in[8] = 8; expo_data_out[8] = 13;
            expo_data_in[9] = 9; expo_data_out[9] = 14;
            expo_data_in[10] = 10; expo_data_out[10] = 15;
            expo_data_in[11] = 11; expo_data_out[11] = 17;
            expo_data_in[12] = 12; expo_data_out[12] = 18;
            expo_data_in[13] = 13; expo_data_out[13] = 19;
            expo_data_in[14] = 14; expo_data_out[14] = 21;
            expo_data_in[15] = 15; expo_data_out[15] = 22;
            expo_data_in[16] = 16; expo_data_out[16] = 23;
            expo_data_in[17] = 17; expo_data_out[17] = 24;
            expo_data_in[18] = 18; expo_data_out[18] = 25;
            expo_data_in[19] = 19; expo_data_out[19] = 26;
            expo_data_in[20] = 20; expo_data_out[20] = 27;
            expo_data_in[21] = 21; expo_data_out[21] = 28;
            expo_data_in[22] = 22; expo_data_out[22] = 29;
            expo_data_in[23] = 23; expo_data_out[23] = 30;
            expo_data_in[24] = 24; expo_data_out[24] = 31;
            expo_data_in[25] = 25; expo_data_out[25] = 32;
            expo_data_in[26] = 26; expo_data_out[26] = 33;
            expo_data_in[27] = 27; expo_data_out[27] = 34;
            expo_data_in[28] = 28; expo_data_out[28] = 35;
            expo_data_in[29] = 29; expo_data_out[29] = 36;
            expo_data_in[30] = 30; expo_data_out[30] = 36;
            expo_data_in[31] = 31; expo_data_out[31] = 37;
            expo_data_in[32] = 32; expo_data_out[32] = 38;
            expo_data_in[33] = 33; expo_data_out[33] = 39;
            expo_data_in[34] = 34; expo_data_out[34] = 40;
            expo_data_in[35] = 35; expo_data_out[35] = 41;
            expo_data_in[36] = 36; expo_data_out[36] = 41;
            expo_data_in[37] = 37; expo_data_out[37] = 42;
            expo_data_in[38] = 38; expo_data_out[38] = 43;
            expo_data_in[39] = 39; expo_data_out[39] = 44;
            expo_data_in[40] = 40; expo_data_out[40] = 45;
            expo_data_in[41] = 41; expo_data_out[41] = 45;
            expo_data_in[42] = 42; expo_data_out[42] = 46;
            expo_data_in[43] = 43; expo_data_out[43] = 47;
            expo_data_in[44] = 44; expo_data_out[44] = 48;
            expo_data_in[45] = 45; expo_data_out[45] = 48;
            expo_data_in[46] = 46; expo_data_out[46] = 49;
            expo_data_in[47] = 47; expo_data_out[47] = 50;
            expo_data_in[48] = 48; expo_data_out[48] = 51;
            expo_data_in[49] = 49; expo_data_out[49] = 51;
            expo_data_in[50] = 50; expo_data_out[50] = 52;
            expo_data_in[51] = 51; expo_data_out[51] = 53;
            expo_data_in[52] = 52; expo_data_out[52] = 53;
            expo_data_in[53] = 53; expo_data_out[53] = 54;
            expo_data_in[54] = 54; expo_data_out[54] = 55;
            expo_data_in[55] = 55; expo_data_out[55] = 56;
            expo_data_in[56] = 56; expo_data_out[56] = 56;
            expo_data_in[57] = 57; expo_data_out[57] = 57;
            expo_data_in[58] = 58; expo_data_out[58] = 58;
            expo_data_in[59] = 59; expo_data_out[59] = 58;
            expo_data_in[60] = 60; expo_data_out[60] = 59;
            expo_data_in[61] = 61; expo_data_out[61] = 60;
            expo_data_in[62] = 62; expo_data_out[62] = 61;
            expo_data_in[63] = 63; expo_data_out[63] = 61;
            expo_data_in[64] = 64; expo_data_out[64] = 62;
            expo_data_in[65] = 65; expo_data_out[65] = 63;
            expo_data_in[66] = 66; expo_data_out[66] = 63;
            expo_data_in[67] = 67; expo_data_out[67] = 64;
            expo_data_in[68] = 68; expo_data_out[68] = 65;
            expo_data_in[69] = 69; expo_data_out[69] = 65;
            expo_data_in[70] = 70; expo_data_out[70] = 66;
            expo_data_in[71] = 71; expo_data_out[71] = 67;
            expo_data_in[72] = 72; expo_data_out[72] = 67;
            expo_data_in[73] = 73; expo_data_out[73] = 68;
            expo_data_in[74] = 74; expo_data_out[74] = 69;
            expo_data_in[75] = 75; expo_data_out[75] = 69;
            expo_data_in[76] = 76; expo_data_out[76] = 70;
            expo_data_in[77] = 77; expo_data_out[77] = 71;
            expo_data_in[78] = 78; expo_data_out[78] = 71;
            expo_data_in[79] = 79; expo_data_out[79] = 72;
            expo_data_in[80] = 80; expo_data_out[80] = 73;
            expo_data_in[81] = 81; expo_data_out[81] = 73;
            expo_data_in[82] = 82; expo_data_out[82] = 74;
            expo_data_in[83] = 83; expo_data_out[83] = 75;
            expo_data_in[84] = 84; expo_data_out[84] = 75;
            expo_data_in[85] = 85; expo_data_out[85] = 76;
            expo_data_in[86] = 86; expo_data_out[86] = 77;
            expo_data_in[87] = 87; expo_data_out[87] = 77;
            expo_data_in[88] = 88; expo_data_out[88] = 78;
            expo_data_in[89] = 89; expo_data_out[89] = 78;
            expo_data_in[90] = 90; expo_data_out[90] = 79;
            expo_data_in[91] = 91; expo_data_out[91] = 80;
            expo_data_in[92] = 92; expo_data_out[92] = 80;
            expo_data_in[93] = 93; expo_data_out[93] = 81;
            expo_data_in[94] = 94; expo_data_out[94] = 82;
            expo_data_in[95] = 95; expo_data_out[95] = 82;
            expo_data_in[96] = 96; expo_data_out[96] = 83;
            expo_data_in[97] = 97; expo_data_out[97] = 83;
            expo_data_in[98] = 98; expo_data_out[98] = 84;
            expo_data_in[99] = 99; expo_data_out[99] = 85;
            expo_data_in[100] = 100; expo_data_out[100] = 85;
            expo_data_in[101] = 101; expo_data_out[101] = 86;
            expo_data_in[102] = 102; expo_data_out[102] = 86;
            expo_data_in[103] = 103; expo_data_out[103] = 87;
            expo_data_in[104] = 104; expo_data_out[104] = 87;
            expo_data_in[105] = 105; expo_data_out[105] = 88;
            expo_data_in[106] = 106; expo_data_out[106] = 89;
            expo_data_in[107] = 107; expo_data_out[107] = 89;
            expo_data_in[108] = 108; expo_data_out[108] = 90;
            expo_data_in[109] = 109; expo_data_out[109] = 90;
            expo_data_in[110] = 110; expo_data_out[110] = 91;
            expo_data_in[111] = 111; expo_data_out[111] = 91;
            expo_data_in[112] = 112; expo_data_out[112] = 92;
            expo_data_in[113] = 113; expo_data_out[113] = 93;
            expo_data_in[114] = 114; expo_data_out[114] = 93;
            expo_data_in[115] = 115; expo_data_out[115] = 94;
            expo_data_in[116] = 116; expo_data_out[116] = 94;
            expo_data_in[117] = 117; expo_data_out[117] = 95;
            expo_data_in[118] = 118; expo_data_out[118] = 95;
            expo_data_in[119] = 119; expo_data_out[119] = 96;
            expo_data_in[120] = 120; expo_data_out[120] = 96;
            expo_data_in[121] = 121; expo_data_out[121] = 97;
            expo_data_in[122] = 122; expo_data_out[122] = 97;
            expo_data_in[123] = 123; expo_data_out[123] = 98;
            expo_data_in[124] = 124; expo_data_out[124] = 98;
            expo_data_in[125] = 125; expo_data_out[125] = 99;
            expo_data_in[126] = 126; expo_data_out[126] = 99;
            expo_data_in[127] = 127; expo_data_out[127] = 100;
            expo_data_in[128] = 128; expo_data_out[128] = 100;
            expo_data_in[129] = 129; expo_data_out[129] = 101;
            expo_data_in[130] = 130; expo_data_out[130] = 101;
            expo_data_in[131] = 131; expo_data_out[131] = 102;
            expo_data_in[132] = 132; expo_data_out[132] = 102;
            expo_data_in[133] = 133; expo_data_out[133] = 103;
            expo_data_in[134] = 134; expo_data_out[134] = 103;



            data_in[0] = 0; data_out[0] = 103;
            data_in[1] = 1; data_out[1] = 107;
            data_in[2] = 2; data_out[2] = 111;
            data_in[3] = 3; data_out[3] = 114;
            data_in[4] = 4; data_out[4] = 118;
            data_in[5] = 5; data_out[5] = 121;
            data_in[6] = 6; data_out[6] = 124;
            data_in[7] = 7; data_out[7] = 127;
            data_in[8] = 8; data_out[8] = 130;
            data_in[9] = 9; data_out[9] = 133;
            data_in[10] = 10; data_out[10] = 135;
            data_in[11] = 11; data_out[11] = 138;
            data_in[12] = 12; data_out[12] = 140;
            data_in[13] = 13; data_out[13] = 143;
            data_in[14] = 14; data_out[14] = 146;
            data_in[15] = 15; data_out[15] = 148;
            data_in[16] = 16; data_out[16] = 152;
            data_in[17] = 17; data_out[17] = 156;
            data_in[18] = 18; data_out[18] = 160;
            data_in[19] = 19; data_out[19] = 164;
            data_in[20] = 20; data_out[20] = 167;
            data_in[21] = 21; data_out[21] = 171;
            data_in[22] = 22; data_out[22] = 174;
            data_in[23] = 23; data_out[23] = 177;
            data_in[24] = 24; data_out[24] = 180;
            data_in[25] = 25; data_out[25] = 183;
            data_in[26] = 26; data_out[26] = 186;
            data_in[27] = 27; data_out[27] = 189;
            data_in[28] = 28; data_out[28] = 191;
            data_in[29] = 29; data_out[29] = 194;
            data_in[30] = 30; data_out[30] = 197;
            data_in[31] = 31; data_out[31] = 199;
            data_in[32] = 48; data_out[32] = 203;
            data_in[33] = 49; data_out[33] = 207;
            data_in[34] = 50; data_out[34] = 211;
            data_in[35] = 51; data_out[35] = 215;
            data_in[36] = 52; data_out[36] = 219;
            data_in[37] = 53; data_out[37] = 222;
            data_in[38] = 54; data_out[38] = 225;
            data_in[39] = 55; data_out[39] = 228;
            data_in[40] = 56; data_out[40] = 231;
            data_in[41] = 57; data_out[41] = 233;
            data_in[42] = 58; data_out[42] = 235;
            data_in[43] = 59; data_out[43] = 238;
            data_in[44] = 60; data_out[44] = 239;
            data_in[45] = 61; data_out[45] = 241;
            data_in[46] = 62; data_out[46] = 242;
            data_in[47] = 63; data_out[47] = 244;
            data_in[48] = 112; data_out[48] = 245;
            data_in[49] = 113; data_out[49] = 247;
            data_in[50] = 114; data_out[50] = 248;
            data_in[51] = 115; data_out[51] = 249;
            data_in[52] = 116; data_out[52] = 250;
            data_in[53] = 117; data_out[53] = 251;
            data_in[54] = 118; data_out[54] = 251;
            data_in[55] = 119; data_out[55] = 252;
            data_in[56] = 120; data_out[56] = 252;
            data_in[57] = 121; data_out[57] = 253;
            data_in[58] = 122; data_out[58] = 253;
            data_in[59] = 123; data_out[59] = 253;
            data_in[60] = 124; data_out[60] = 254;
            data_in[61] = 125; data_out[61] = 254;
            data_in[62] = 126; data_out[62] = 254;
            data_in[63] = 127; data_out[63] = 254;

            int H = pictureBox1.Height;

            for (i = 0; i < 135; i++)
            {
                curvePoints[i].X = expo_data_in[i] * 3;
                curvePoints[i].Y = H - expo_data_out[i] * 2;
            }


            for (i = 135; i < (135 + 64); i++)
            {
                //curvePoints[i].X = data_in[i - 135] * 10;
                //curvePoints[i].Y = 256 * 2 - 1 - data_out[i - 135] * 2;

                curvePoints[i].X = (data_in[i - 135] + 135) * 3;
                curvePoints[i].Y = H - data_out[i - 135] * 2;
            }

            for (i = 0; i < curvePoints.Length; i++)
            {
                richTextBox1.Text += "(" + curvePoints[i].X.ToString() + ", " + curvePoints[i].Y.ToString() + ") ";
                if ((i % 12) == 11)
                    richTextBox1.Text += "\n";

            }
            richTextBox1.Text += "\n";

            g.DrawLines(new Pen(Color.DarkRed, 10), curvePoints);   //畫直線




            g.DrawRectangle(new Pen(Color.Red), new Rectangle(0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1));

            pictureBox1.Image = bitmap1;


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

