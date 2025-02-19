using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for SmoothingMode
using System.Drawing.Text;      //for TextRenderingHint
using System.IO;                //for File

namespace vcs_Draw3B
{
    public partial class Form1 : Form
    {
        int W = 250;
        int H = 250;

        Graphics ge;    //for draw ellipse
        Graphics gs;    //for draw star
        private const int EllipseMargin = 10;
        private int EllipseCx, EllipseCy, EllipseWidth, EllipseHeight;
        private List<PointF> LinePoints = null;

        double pbUnit;
        int W_progressbar;
        int H_progressbar;
        int Complete_progressbar;
        Bitmap bmp_progressbar;
        Graphics g_progressbar;

        private int CurrentValue = 0;   //指南針

        //箱中球 ST
        BallInABox ball;   // 宣告 一個箱中球 物件
        Rectangle boxRect; // 宣告 一個箱子的位置與寬高
        //箱中球 SP

        //雙圓旋轉 ST
        Pen pen01 = new Pen(Color.Red, 4); // 內圓 的筆刷
        Pen pen02 = new Pen(Color.Blue, 4);// 外圓 的筆刷

        double angle1 = 0;            // 內圓 的角度
        double angle2 = Math.PI; // 外圓 的角度
        double angleDelta = 0.1;     // 旋轉的角度遞增值

        int inner = 80; // 內圓 的半徑
        int outer = 120; // 外圓 的半徑
        int innerNo = 1; // 內圓 的小圓球數目
        int outerNo = 1; // 外圓 的小圓球數目
        //雙圓旋轉 SP

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //自製ProgressBar
            W_progressbar = pictureBox_progressbar.Width;
            H_progressbar = pictureBox_progressbar.Height;
            pbUnit = W_progressbar / 100.0;
            //Complete_progressbar - This is equal to work completed in % [min = 0 max = 100]
            Complete_progressbar = 0;
            //create bitmap
            bmp_progressbar = new Bitmap(W_progressbar, H_progressbar);
            timer_progressbar.Enabled = true;

            ge = pictureBox_ellipse.CreateGraphics();
            gs = pictureBox_star.CreateGraphics();
            // Calculate the ellipse parameters.
            EllipseWidth = this.pictureBox_ellipse.ClientSize.Width - 2 * EllipseMargin;
            EllipseHeight = this.pictureBox_ellipse.ClientSize.Height - 2 * EllipseMargin;

            //三顆跳跳球 ST
            ball1 = new ClassBall(new Point(this.pictureBox_ball.ClientSize.Width / 2, this.pictureBox_ball.ClientSize.Height / 2),
                                new Point(3, 5),
                                new Size(this.pictureBox_ball.ClientSize.Width, this.pictureBox_ball.ClientSize.Height),
                                30,
                                Color.Red);

            ball2 = new ClassBall(new Point(this.pictureBox_ball.ClientSize.Width / 4, this.pictureBox_ball.ClientSize.Height / 4),
                                new Point(-3, 5),
                                new Size(this.pictureBox_ball.ClientSize.Width, this.pictureBox_ball.ClientSize.Height),
                                30,
                                Color.Blue);

            ball3 = new ClassBall(new Point(this.pictureBox_ball.ClientSize.Width / 4, this.pictureBox_ball.ClientSize.Height / 2),
                                new Point(3, -8),
                                new Size(this.pictureBox_ball.ClientSize.Width, this.pictureBox_ball.ClientSize.Height),
                                30,
                                Color.Green);
            //三顆跳跳球 SP

            //箱中球 ST
            // 設定 箱子的位置與寬高
            boxRect = new Rectangle(20, 20, 200, 150);
            // 新增 一個箱中球 物件
            ball = new BallInABox(new Point(100, 100),
                         new Point(2, 3),
                         boxRect,
                         20);
            //箱中球 SP

            //雙圓旋轉 ST
            // 內外圓 的筆刷樣式設定
            pen01.DashStyle = System.Drawing.Drawing2D.DashStyle.Dot;
            pen02.DashStyle = System.Drawing.Drawing2D.DashStyle.Dot;
            this.pictureBox_double_circle.KeyDown += new KeyEventHandler(pictureBox_double_circle_KeyDown);
            //雙圓旋轉 SP
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

            x_st = 20;
            y_st = 20;
            dx = 160;
            dy = 50;

            pictureBox_star.Size = new Size(W, H);
            pictureBox_polygon.Size = new Size(W, H);
            pictureBox_round.Size = new Size(W, H);
            pictureBox_ellipse.Size = new Size(350, 200);
            pictureBox_circular.Size = new Size(W, H);
            pictureBox_ball.Size = new Size(W, H);
            pictureBox_ball_in_box.Size = new Size(W, H);
            pictureBox_double_circle.Size = new Size(W, H);

            pictureBox_progressbar.Size = new Size(600, 100);
            pictureBox_rectangle.Size = new Size(600, 350);

            x_st = 10;
            y_st = 10;
            dx = W + 70;
            dy = H + 45;

            pictureBox_star.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox_polygon.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox_round.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            pictureBox_circular.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox_ball.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            pictureBox_ball_in_box.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            pictureBox_double_circle.Location = new Point(x_st + dx * 3, y_st + dy * 1);

            groupBox1.Location = new Point(x_st + dx * 5, y_st + dy * 0 + 50);
            pictureBox_ellipse.Location = new Point(x_st + dx * 4 - 40, y_st + dy * 1);

            pictureBox_progressbar.Location = new Point(x_st + dx * 3 - 80, y_st + dy * 2 + 80 - 100);
            pictureBox_rectangle.Location = new Point(x_st + dx * 3 - 80, y_st + dy * 2 + 100);

            x_st = 1810;
            y_st = 80;
            dx = 120;
            dy = 50;

            richTextBox1.Location = new Point(x_st + dx * 0 - 300, y_st + dy * 12);
            richTextBox1.Size = new Size(400, 380);
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
            richTextBox1.Clear();
        }

        //delay 10000 約 10秒
        //C# 不lag的延遲時間
        private void delay(int delay_milliseconds)
        {
            delay_milliseconds *= 2;
            DateTime time_before = DateTime.Now;
            while (((TimeSpan)(DateTime.Now - time_before)).TotalMilliseconds < delay_milliseconds)
            {
                Application.DoEvents();
            }
        }

        private void timer_draw_ellipse_Tick(object sender, EventArgs e)
        {
            MakeDrawingObjects();

            if ((EllipseWidth <= 0) || (EllipseHeight <= 0))
                return;

            ge.SmoothingMode = SmoothingMode.AntiAlias;

            // Fill and outline the ellipse.
            ge.FillEllipse(Brushes.LightBlue, EllipseMargin, EllipseMargin, EllipseWidth, EllipseHeight);
            ge.DrawEllipse(Pens.Blue, EllipseMargin, EllipseMargin, EllipseWidth, EllipseHeight);

            // Draw the lines.
            ge.DrawLines(Pens.Blue, LinePoints.ToArray());
        }

        // Make the drawing objects.
        private void MakeDrawingObjects()
        {
            // Make random lines connecting points
            // on the edge of the ellipse.
            EllipseCx = this.pictureBox_ellipse.ClientSize.Width / 2;
            EllipseCy = this.pictureBox_ellipse.ClientSize.Height / 2;
            Random rand = new Random();
            double circumference = 2 * Math.PI * Math.Sqrt(
                (EllipseWidth * EllipseWidth + EllipseHeight * EllipseHeight) / 2);
            int num_points = (int)(circumference / 40);
            LinePoints = new List<PointF>();
            for (int i = 0; i < num_points; i++)
            {
                double theta1 = 2 * Math.PI * rand.NextDouble();
                float x1 = (float)(EllipseCx + Math.Cos(theta1) * EllipseWidth / 2);
                float y1 = (float)(EllipseCy + Math.Sin(theta1) * EllipseHeight / 2);
                LinePoints.Add(new PointF(x1, y1));

                double theta2 = 2 * Math.PI * rand.NextDouble();
                float x2 = (float)(EllipseCx + Math.Cos(theta2) * EllipseWidth / 2);
                float y2 = (float)(EllipseCy + Math.Sin(theta2) * EllipseHeight / 2);
                LinePoints.Add(new PointF(x2, y2));
            }
        }

        // Force all threads to end.
        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            Environment.Exit(0);
        }

        int radius = 50;
        private void timer_draw_star_Tick(object sender, EventArgs e)
        {
            gs.Clear(Color.White);
            int linewidth = 5;
            Point center = new Point();

            center = new Point(pictureBox_star.Width / 2, pictureBox_star.Height / 2);

            Random rr = new Random();

            DrawStar(gs, center, radius, linewidth, Color.FromArgb(rr.Next(256), rr.Next(256), rr.Next(256)));

            radius += 5;
            if (radius > 120)
            {
                gs.Clear(Color.White);
                radius = 50;
            }
        }

        private void DrawStar(Graphics g, PointF center, int radius, int linewidth, Color c)
        {
            g.SmoothingMode = SmoothingMode.AntiAlias;

            // Create a new pen.
            //顏色、線寬分開寫
            //Pen p = new Pen(c);
            // Set the pen's width.
            //p.Width = linewidth;

            //顏色、線寬寫在一起
            Pen p = new Pen(c, linewidth);

            PointF[] pt = new PointF[11];    //一維陣列內有11個Point
            int angle;

            int r = radius;

            int i;
            for (i = 0; i < 11; i++)
            {
                angle = -90 + 36 * i;
                if ((i % 2) == 0)
                    r = radius;
                else
                {
                    r = (int)(radius * (Math.Cos(36 * Math.PI / 180) - Math.Sin(36 * Math.PI / 180) / Math.Tan(54 * Math.PI / 180)));
                    //richTextBox1.Text += "radius = " + radius.ToString() + ", r = " + r.ToString() + "\n";
                }
                pt[i].X = (int)(r * Math.Cos(angle * Math.PI / 180));
                pt[i].Y = (int)(r * Math.Sin(angle * Math.PI / 180));

                //richTextBox1.Text += "pt[" + i.ToString() + "].X " + pt[i].X.ToString() + "\t" + "pt[" + i.ToString() + "].Y " + pt[i].Y.ToString() + "\n";
                pt[i].X += center.X;
                pt[i].Y += center.Y;
            }

            g.DrawPolygon(p, pt);                       //空心星形
            //g.FillPolygon(Brushes.Blue, pt);          //實心星形

            //Dispose of the pen.
            p.Dispose();
        }

        //畫圓內接正多邊形 ST
        int polygon_number = 3;
        private void timer_draw_polygon_Tick(object sender, EventArgs e)
        {
            int W = pictureBox_polygon.ClientSize.Width;
            int H = pictureBox_polygon.ClientSize.Height;

            int cx = W / 2;
            int cy = H / 2;
            int r = Math.Min(W, H) / 2 - 50;
            int n;

            Graphics g;
            Pen p;
            SolidBrush sb;
            Bitmap bitmap1;

            //----開新的Bitmap----
            bitmap1 = new Bitmap(W, H);
            //----使用上面的Bitmap畫圖----
            g = Graphics.FromImage(bitmap1);

            p = new Pen(Color.Red, 10);     // 設定畫筆為紅色、粗細為 10 點。

            g.Clear(Color.White);
            draw_polygon(g, p, cx, cy, r, polygon_number);
            pictureBox_polygon.Image = bitmap1;

            polygon_number++;
            if (polygon_number > 10)
                polygon_number = 3;
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

        private void draw_polygon(Graphics g, Pen p, int dx, int dy, int r, int n)
        {
            Point[] points = new Point[n];
            int i;
            int j;
            int angle = 360 / n;
            int offset = 360 / n / 2;

            if ((n % 2) == 1)
            {
                for (i = 0; i < n; i++)
                {
                    points[i].X = dx + (int)(r * cosd(-90 + angle * i));
                    points[i].Y = dy + (int)(r * sind(-90 + angle * i));
                }
            }
            else
            {
                for (i = 0; i < n; i++)
                {
                    points[i].X = dx + (int)(r * cosd(offset + angle * i));
                    points[i].Y = dy + (int)(r * sind(offset + angle * i));
                }

            }

            p = new Pen(Color.Red, 3);     // 設定畫筆為紅色、粗細為 10 點。

            DrawCircle(g, p, dx, dy, r);

            for (i = 0; i < n; i++)
            {
                //richTextBox1.Text += "points[" + i.ToString() + "], X = " + points[i].X + ", Y = " + points[i].Y + "\n";
            }

            for (i = 0; i < n; i++)
            {
                for (j = (i + 1); j < n; j++)
                {
                    //richTextBox1.Text += "draw " + i.ToString() + " - " + j.ToString() + "\n";
                    g.DrawLine(p, points[i], points[j]);
                }
            }
        }

        void DrawCircle(Graphics g, Pen p, int cx, int cy, int r)
        {
            g.DrawEllipse(p, cx - r, cy - r, r * 2, r * 2);
        }

        //畫圓內接正多邊形 SP

        void draw_color_rectangles()
        {
            int W = pictureBox_rectangle.ClientSize.Width;
            int H = pictureBox_rectangle.ClientSize.Height;

            Graphics g = pictureBox_rectangle.CreateGraphics();

            g.Clear(Color.White);
            g.DrawRectangle(Pens.Navy, 0, 0, W - 1, H - 1);

            Brush bb = new SolidBrush(Color.Orange);
            g.FillRectangle(bb, 70, 70, 200, 100);  //畫出一個填滿的方框

            Pen p = new Pen(Color.Black, 4);
            g.DrawRectangle(p, 70, 70, 200, 100);
            //在同樣起點畫出黑色的長方型線，即實現加外框            

            Random rr = new Random();
            Brush db;
            for (int i = 1; i <= 4; i++)
            {
                db = new SolidBrush(Color.FromArgb(rr.Next(256), rr.Next(256), rr.Next(256)));
                //Color.FromArgb() 可以設定3原色，這裡3原色的代碼是亂數產生的

                g.FillRectangle(db, 70 + (i * 40), 70 + (i * 40), 200, 100);
                //畫布上畫出方框，每次位置的X及Y值都加70，以實現往右下角移動
            }
        }

        private void timer_draw_rectangle_Tick(object sender, EventArgs e)
        {
            draw_color_rectangles();
        }

        private void timer_progressbar_Tick(object sender, EventArgs e)
        {
            //graphics
            g_progressbar = Graphics.FromImage(bmp_progressbar);	// 取得繪圖區物件

            //clear graphics
            g_progressbar.Clear(Color.LightSkyBlue);

            //draw progressbar
            g_progressbar.FillRectangle(Brushes.CornflowerBlue, new Rectangle(0, 0, (int)(Complete_progressbar * pbUnit), H_progressbar));

            //draw % complete
            g_progressbar.DrawString(Complete_progressbar + "%", new Font("Arial", H_progressbar / 2), Brushes.Black, new PointF(W_progressbar / 2 - H_progressbar, H_progressbar / 10));

            //load bitmap in picturebox picboxPB
            pictureBox_progressbar.Image = bmp_progressbar;

            //update Complete_progressbar
            //Note!
            //To keep things simple I am adding +1 to Complete_progressbar every 50ms
            //You can change this as per your requirement :)
            Complete_progressbar++;
            if (Complete_progressbar > 100)
            {
                //dispose
                g_progressbar.Dispose();
                timer_progressbar.Stop();
            }
        }

        //指南針ST
        private void pictureBox_compass2_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            e.Graphics.TextRenderingHint = TextRenderingHint.AntiAlias;

            DrawCompass(e.Graphics, CurrentValue);
        }

        private void DrawCompass(Graphics gr, int value)
        {
            // Draw the background.
            DrawBackground(gr);

            // Draw tick marks.
            using (Font nsew_font = new Font("Arial", 14, FontStyle.Italic | FontStyle.Bold))
            {
                using (Font degrees_font = new Font("Arial", 12, FontStyle.Italic))
                {
                    DrawTickMarks(gr, CurrentValue, nsew_font, degrees_font);
                }
            }

            // Draw the pointer.
            DrawPointer(gr);
        }

        private void DrawBackground(Graphics gr)
        {
            int wid = pictureBox_compass2.ClientSize.Width;
            int hgt = pictureBox_compass2.ClientSize.Height;
            using (LinearGradientBrush brush = new LinearGradientBrush(pictureBox_compass2.ClientRectangle, Color.White, Color.Gray, 90))
            {
                ColorBlend color_blend = new ColorBlend();
                color_blend.Colors = new Color[]
                {
                    Color.White, Color.Black, Color.Black, Color.White,
                };
                color_blend.Positions = new float[]
                {
                    0.0f, 0.3f, 0.8f, 1.0f, 
                };
                brush.InterpolationColors = color_blend;
                gr.FillRectangle(brush, pictureBox_compass2.ClientRectangle);
            }
        }

        private void DrawTickMarks(Graphics gr, float center_value, Font nsew_font, Font degrees_font)
        {
            // Set the number of degrees that are visible.
            const int width_in_degrees = 180;

            // Calculate tick geometry.
            const int letter_freq = 90;     // Draw a letter every 90 degrees.
            const int large_tick_freq = 30; // Draw a large tick mark every 30 degrees.
            const int small_tick_freq = 15; // Draw a small tick mark every 15 degrees.
            float large_tick_hgt = pictureBox_compass2.ClientSize.Height / 5f;
            float small_tick_hgt = large_tick_hgt / 2f;
            float large_tick_y0 = pictureBox_compass2.ClientSize.Height / 10f;
            float large_tick_y1 = large_tick_y0 + large_tick_hgt;
            float small_tick_y0 = large_tick_y0;
            float small_tick_y1 = small_tick_y0 + small_tick_hgt;

            // Find the center.
            int wid = pictureBox_compass2.ClientSize.Width;
            float x_mid = wid / 2f;
            float letter_y = large_tick_y1 * 1.2f;

            // Find the width of one degree on the control.
            float pix_per_degree = (float)pictureBox_compass2.ClientSize.Width / width_in_degrees;

            // Find the value at the left edge of the control.
            float left_value = center_value - (wid / 2f) / pix_per_degree;

            // Find the next smaller multiple of small_tick_freq.
            int degrees = small_tick_freq * (int)(left_value / small_tick_freq);
            degrees -= small_tick_freq;

            // Find the corresponding X position.
            float x = x_mid - (center_value - degrees) * pix_per_degree;

            // Adjust degrees so it is between 1 and 360.
            if (degrees <= 0) degrees += 360;

            // Draw tick marks.
            using (StringFormat sf = new StringFormat())
            {
                sf.Alignment = StringAlignment.Center;

                for (int i = 0; i <= width_in_degrees; i += small_tick_freq)
                {
                    // See what we should draw.
                    string letter = "";
                    if (degrees % letter_freq == 0)
                    {
                        switch (degrees / letter_freq)
                        {
                            case 1:
                                letter = "E";
                                break;
                            case 2:
                                letter = "S";
                                break;
                            case 3:
                                letter = "W";
                                break;
                            case 4:
                                letter = "N";
                                break;
                        }
                        gr.DrawLine(Pens.White, x, large_tick_y0, x, large_tick_y1);
                        gr.DrawString(letter, nsew_font, Brushes.White, new PointF(x, letter_y), sf);
                    }
                    else if (degrees % large_tick_freq == 0)
                    {
                        gr.DrawLine(Pens.White, x, large_tick_y0, x, large_tick_y1);
                        gr.DrawString(degrees.ToString(), degrees_font, Brushes.White, new PointF(x, letter_y), sf);
                    }
                    else
                    {
                        gr.DrawLine(Pens.White, x, small_tick_y0, x, small_tick_y1);
                    }

                    degrees += small_tick_freq;
                    if (degrees > 360)
                    {
                        degrees -= 360;
                    }
                    x += small_tick_freq * pix_per_degree;
                }
            }
        }

        private void DrawPointer(Graphics gr)
        {
            float y0 = 0;
            float y2 = pictureBox_compass2.ClientSize.Height / 10f;
            float y1 = y2 / 2f;
            float half_wid = y2;

            // Find the center.
            int wid = pictureBox_compass2.ClientSize.Width;
            float x_mid = wid / 2f;

            // Define the points.
            PointF[] points =
            {
                new PointF(x_mid - half_wid, y0),
                new PointF(x_mid + half_wid, y0),
                new PointF(x_mid + half_wid, y1),
                new PointF(x_mid, y2),
                new PointF(x_mid - half_wid, y1),
            };
            gr.FillPolygon(Brushes.LightBlue, points);
            gr.DrawPolygon(Pens.Black, points);
        }

        private void hbarDegrees_Scroll(object sender, ScrollEventArgs e)
        {
            CurrentValue = hbarDegrees.Value;
            lblDegrees.Text = CurrentValue.ToString() + "°";
            pictureBox_compass2.Refresh();
            pictureBox_compass1.Refresh();
        }

        private void pictureBox_compass1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(pictureBox_compass1.BackColor);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            e.Graphics.TextRenderingHint = TextRenderingHint.AntiAlias;

            // Draw the heading picture.
            using (Font nsew_font = new Font("Times New Roman", 18, FontStyle.Bold))
            {
                DrawHeading(e.Graphics, CurrentValue, nsew_font);
            }
        }

        private void DrawHeading(Graphics gr, int value, Font font)
        {
            float cx = pictureBox_compass1.ClientSize.Width / 2f;
            float cy = pictureBox_compass1.ClientSize.Height / 2f;

            // Draw NSEW.
            float letter_r = Math.Min(cx, cy) * 0.85f;
            string[] letters = { "N", "E", "S", "W" };
            int[] degrees = { 270, 0, 90, 180 };
            for (int i = 0; i < 4; i++)
            {
                float letter_x = letter_r * (float)Math.Cos(DegreesToRadians(degrees[i]));
                float letter_y = letter_r * (float)Math.Sin(DegreesToRadians(degrees[i]));
                PointF point = new PointF(cx + letter_x, cy + letter_y);
                DrawRotatedText(gr, font, Brushes.Black, letters[i], point, degrees[i] + 90);
            }

            // Draw tick marks.
            const int large_tick_freq = 30; // Draw a large tick mark every 30 degrees.
            const int small_tick_freq = 15; // Draw a small tick mark every 15 degrees.
            const int tiny_tick_freq = 3;   // Draw a tiny tick mark every 3 degrees.
            float outer_r = letter_r * 0.9f;
            float large_r = outer_r * 0.8f;
            float small_r = outer_r * 0.9f;
            float tiny_r = outer_r * 0.95f;
            using (Pen pen = new Pen(Color.Blue, 3))
            {
                for (int i = tiny_tick_freq; i <= 360; i += tiny_tick_freq)
                {
                    float cos = (float)Math.Cos(DegreesToRadians(i));
                    float sin = (float)Math.Sin(DegreesToRadians(i));
                    float x0 = cx + outer_r * cos;
                    float y0 = cy + outer_r * sin;

                    float x1, y1;
                    if (i % large_tick_freq == 0)
                    {
                        pen.Width = 3;
                        x1 = cx + large_r * cos;
                        y1 = cy + large_r * sin;
                    }
                    else if (i % small_tick_freq == 0)
                    {
                        pen.Width = 2;
                        x1 = cx + small_r * cos;
                        y1 = cy + small_r * sin;
                    }
                    else
                    {
                        pen.Width = 1;
                        x1 = cx + tiny_r * cos;
                        y1 = cy + tiny_r * sin;
                    }
                    gr.DrawLine(pen, x0, y0, x1, y1);
                }
            }

            // Draw the pointer.
            // Rotate 90 degrees so North is at 0.
            double radians = DegreesToRadians(value - 90);

            const int tip_r = 4;
            float pointer_r = large_r * 1.0f;
            float tip_x = cx + pointer_r * (float)Math.Cos(radians);
            float tip_y = cx + pointer_r * (float)Math.Sin(radians);
            float tip_x1 = cx + tip_r * (float)Math.Cos(radians + Math.PI / 2.0);
            float tip_y1 = cy + tip_r * (float)Math.Sin(radians + Math.PI / 2.0);
            float tip_x2 = cx + tip_r * (float)Math.Cos(radians - Math.PI / 2.0);
            float tip_y2 = cy + tip_r * (float)Math.Sin(radians - Math.PI / 2.0);
            PointF[] points =
            {
                new PointF(tip_x, tip_y),
                new PointF(tip_x1, tip_y1),
                new PointF(tip_x2, tip_y2),
            };
            gr.FillPolygon(Brushes.Black, points);

            // Draw the center.
            const int center_r = 6;
            RectangleF rect = new RectangleF(cx - center_r, cy - center_r, 2 * center_r, 2 * center_r);
            gr.FillEllipse(Brushes.LightBlue, rect);
            gr.DrawEllipse(Pens.Black, rect);
        }

        private double DegreesToRadians(float degrees)
        {
            return degrees * Math.PI / 180;
        }

        private void DrawRotatedText(Graphics gr, Font font, Brush brush, string text, PointF location, float degrees)
        {
            GraphicsState state = gr.Save();
            gr.ResetTransform();
            gr.RotateTransform(degrees);
            gr.TranslateTransform(location.X, location.Y, MatrixOrder.Append);
            using (StringFormat sf = new StringFormat())
            {
                sf.Alignment = StringAlignment.Center;
                sf.LineAlignment = StringAlignment.Center;
                gr.DrawString(text, font, brush, 0, 0, sf);
            }
            gr.Restore(state);
        }

        private void timer_compass_Tick(object sender, EventArgs e)
        {
            CurrentValue++;
            if (CurrentValue == 360)
                CurrentValue = 0;

            hbarDegrees.Value = CurrentValue;
            lblDegrees.Text = CurrentValue.ToString() + "°";
            pictureBox_compass2.Refresh();
            pictureBox_compass1.Refresh();

        }
        //指南針SP

        int cnt = 0;
        void draw_spin_signal()
        {
            int N = 60 + 1;
            Point[] pt;

            int W = pictureBox_round.ClientSize.Width;
            int H = pictureBox_round.ClientSize.Height;
            int i;
            int cx = W / 2;
            int cy = H / 2;
            int r = Math.Min(W, H) / 2 * 9 / 10;

            pt = new Point[N];    //一維陣列內有N個Point

            for (i = 0; i < N; i++)
            {
                pt[i] = new Point(cx + (int)(r * cosd(i * 360 / (N - 1))), cy + (int)(r * sind(i * 360 / (N - 1))));
            }

            //新建圖檔, 初始化畫布
            Bitmap bitmap1 = new Bitmap(pictureBox_round.Width, pictureBox_round.Height);
            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);
            pictureBox_round.Image = bitmap1;

            g.DrawLines(Pens.Red, pt);

            int rr = 3;
            for (i = 0; i < N; i++)
            {
                if ((i % 5) == 0)
                {
                    rr = 5;
                    g.FillEllipse(Brushes.Red, pt[i].X - rr, pt[i].Y - rr, rr * 2, rr * 2);
                }
                else
                {
                    rr = 3;
                    g.FillEllipse(Brushes.Red, pt[i].X - rr, pt[i].Y - rr, rr * 2, rr * 2);
                }
            }
            rr = 6;
            //g.FillEllipse(Brushes.Blue, pt[cnt].X - rr, pt[cnt].Y - rr, rr * 2, rr * 2);
            g.DrawEllipse(Pens.Blue, pt[cnt].X - rr, pt[cnt].Y - rr, rr * 2, rr * 2);
            g.DrawLine(Pens.Blue, cx, cy, pt[cnt].X, pt[cnt].Y);
            cnt++;
            if (cnt >= (N - 1))
                cnt = 0;
        }

        private void timer_round_Tick(object sender, EventArgs e)
        {
            draw_spin_signal();
        }

        int Sect = 20;
        float[] x = new float[31];
        float[] y = new float[31];

        public void draw_circular()
        {
            int i;
            float r;
            //this.ClientSize = new Size(300, 300);
            r = this.pictureBox_circular.ClientSize.Width / 2;
            Graphics g = this.pictureBox_circular.CreateGraphics();
            for (i = 0; i < Sect; i++)
            {
                x[i] = (float)(r * Math.Cos(i * 2 * Math.PI / Sect) + this.pictureBox_circular.ClientSize.Width / 2);
                y[i] = (float)(r * Math.Sin(i * 2 * Math.PI / Sect) + this.pictureBox_circular.ClientSize.Height / 2);
            }
            for (int m = 0; m < Sect - 1; m++)
            {
                for (int n = 0; n < Sect; n++)
                {
                    g.DrawLine(Pens.Blue, x[m], y[m], x[n], y[n]);
                    Application.DoEvents();
                }
            }
        }

        private void timer_circular_Tick(object sender, EventArgs e)
        {
            Graphics g = this.pictureBox_circular.CreateGraphics();
            g.Clear(Color.WhiteSmoke);
            draw_circular();
        }


        //三顆跳跳球 ST
        ClassBall ball1, ball2, ball3;

        bool Collides(ClassBall A, ClassBall B)
        {
            Double D = Math.Sqrt(
            (A.position.X - B.position.X) * (A.position.X - B.position.X) +
            (A.position.Y - B.position.Y) * (A.position.Y - B.position.Y));

            if (D <= A.Ball_Width + B.Ball_Width)
                return true;
            else
                return false;
        }

        void Swap(ClassBall A, ClassBall B)
        {
            Point temp = A.velocity;
            A.velocity = B.velocity;
            B.velocity = temp;
        }

        private void pictureBox_ball_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            ball1.Draw(e.Graphics);
            ball2.Draw(e.Graphics);
            ball3.Draw(e.Graphics);
        }

        private void timer_ball_Tick(object sender, EventArgs e)
        {
            ball1.Move();
            ball2.Move();
            ball3.Move();

            if (Collides(ball1, ball2)) Swap(ball1, ball2);
            if (Collides(ball2, ball3)) Swap(ball2, ball3);
            if (Collides(ball1, ball3)) Swap(ball1, ball3);

            //this.Invalidate();
            this.pictureBox_ball.Invalidate();
        }
        //三顆跳跳球 SP

        //箱中球 ST
        private void pictureBox_ball_in_box_Paint(object sender, PaintEventArgs e)
        {
            // 反鋸齒設定 ==> 比較好的輸出品質
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            ball.DrawBox(e.Graphics, Color.Black); // 繪出 箱子
            ball.Draw(e.Graphics, Color.Blue);     // 繪出 箱中球
        }

        private void timer_ball_in_box_Tick(object sender, EventArgs e)
        {
            ball.Update(); // 更新 箱中球 的位置
            this.pictureBox_ball_in_box.Invalidate();   // 向作業系統要求重畫
        }
        //箱中球 SP

        //雙圓旋轉 ST

        // 鍵盤事件
        void pictureBox_double_circle_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyData == Keys.Space) // 空白鍵 旋轉反向
            {
                angleDelta = -angleDelta;
            }
            else if (e.KeyData == Keys.Up) // ↑鍵 旋轉加速
            {
                if (angleDelta > 0)
                    angleDelta += 0.1;
                else
                    angleDelta -= 0.1;
            }
            else if (e.KeyData == Keys.Down) // ↓鍵 旋轉減慢
            {
                if (angleDelta > 0)
                    angleDelta -= 0.1;
                else
                    angleDelta += 0.1;
            }
        }

        // 滑鼠按下事件
        private void pictureBox_double_circle_MouseDown(object sender, MouseEventArgs e)
        {
            int x0 = this.pictureBox_double_circle.ClientSize.Width / 2;
            int y0 = this.pictureBox_double_circle.ClientSize.Height / 2;
            double dist = Math.Sqrt((e.X - x0) * (e.X - x0) + (e.Y - y0) * (e.Y - y0));

            if (dist < inner) // 滑鼠在內圓按下
            {
                if (e.Button == MouseButtons.Left)  // 滑鼠左鍵 增加小圓球
                    innerNo++;
                else if (e.Button == MouseButtons.Right) // 滑鼠右鍵 減少小圓球
                {
                    if (innerNo > 0)
                        innerNo--;
                }
            }
            else if (dist < outer) // 滑鼠在外圓按下
            {
                if (e.Button == MouseButtons.Left)
                    outerNo++;
                else if (e.Button == MouseButtons.Right)
                {
                    if (outerNo > 0)
                        outerNo--;
                }
            }
        }

        private void pictureBox_double_circle_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            // 視窗客戶區 中心點
            int x0 = this.pictureBox_double_circle.ClientSize.Width / 2;
            int y0 = this.pictureBox_double_circle.ClientSize.Height / 2;
            // 繪出內外圓 的大圓
            e.Graphics.DrawEllipse(pen01, x0 - inner, y0 - inner, inner * 2, inner * 2);
            e.Graphics.DrawEllipse(pen02, x0 - outer, y0 - outer, outer * 2, outer * 2);

            int x, y;
            // 繪出內圓 的旋轉小圓球
            for (int i = 0; i < innerNo; i++)
            {
                // 依旋轉角度angle1算出 座標
                x = x0 + (int)((inner - 10) * Math.Cos(angle1 + i * (Math.PI * 2 / innerNo)));
                y = y0 + (int)((inner - 10) * Math.Sin(angle1 + i * (Math.PI * 2 / innerNo)));
                e.Graphics.FillEllipse(Brushes.Red, x - 10, y - 10, 20, 20);
            }

            // 繪出外圓 的旋轉小圓球
            for (int i = 0; i < outerNo; i++)
            {
                // 依旋轉角度angle2算出 座標
                x = x0 + (int)((outer - 10) * Math.Cos(angle2 + i * (Math.PI * 2 / outerNo)));
                y = y0 + (int)((outer - 10) * Math.Sin(angle2 + i * (Math.PI * 2 / outerNo)));
                e.Graphics.FillEllipse(Brushes.Blue, x - 10, y - 10, 20, 20);
            }
        }

        // 使用計時器定時更新 小圓球 的旋轉角度
        private void timer_double_circle_Tick(object sender, EventArgs e)
        {
            angle1 = angle1 + angleDelta;
            angle2 = angle2 - angleDelta;
            this.pictureBox_double_circle.Invalidate();
        }
        //雙圓旋轉 SP
    }
}
