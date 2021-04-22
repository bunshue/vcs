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

        //for random color ST
        //Reference : https://home.gamer.com.tw/creationDetail.php?sn=4281924
        private Label[] lb_color = new Label[101];
        Random r = new Random(Guid.NewGuid().GetHashCode());
        private int _R = 0, _G = 0, _B = 0;
        private int lb_color_x = 0, lb_color_y = 0;
        //for random color SP

        Graphics g_spiral;  //for draw spiral
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

        #region 畫字
        string filename = "C:\\______test_files\\__RW\\_txt\\琵琶行s.txt";
        int word_position = 0;
        string word_string = "";
        Bitmap bmp;
        Graphics gw;
        #endregion

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

            #region 畫字
            //讀取檔案
            word_string = File.ReadAllText(filename, System.Text.Encoding.Default);
            //richTextBox1.Text += "檔案內容 : " + word_string + "\n";
            //richTextBox1.Text += "長度：" + word_string.Length.ToString() + "\n";
            bmp = new Bitmap(pictureBox_word.ClientSize.Width, pictureBox_word.ClientSize.Height);
            gw = Graphics.FromImage(bmp);
            timer_word.Enabled = true;
            #endregion

            g_spiral = pictureBox_spiral.CreateGraphics();
            draw_spiral();
            timer_spiral.Enabled = true;

            ge = pictureBox_ellipse.CreateGraphics();
            gs = pictureBox_star.CreateGraphics();
            // Calculate the ellipse parameters.
            EllipseWidth = this.pictureBox_ellipse.ClientSize.Width - 2 * EllipseMargin;
            EllipseHeight = this.pictureBox_ellipse.ClientSize.Height - 2 * EllipseMargin;

            draw_random_color();
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

            pictureBox_spiral.Size = new Size(W, H);
            pictureBox_star.Size = new Size(W, H);
            pictureBox_polygon.Size = new Size(W, H);
            pictureBox_brown.Size = new Size(W, H);
            pictureBox_round.Size = new Size(W, H);
            pictureBox_ellipse.Size = new Size(350, 200);
            pictureBox_circular.Size = new Size(W, H);

            pictureBox_captcha1.Size = new Size(W + 50, 110);
            pictureBox_captcha2.Size = new Size(W + 50, 110);
            pictureBox_captcha3.Size = new Size(W + 50, 110);
            pictureBox_random_pixel_image.Size = new Size(W + 50, 110);
            pictureBox_progressbar.Size = new Size(600, 100);
            pictureBox_rectangle.Size = new Size(600, 350);

            x_st = 10;
            y_st = 10;
            dx = W + 70;
            dy = H + 45;

            pictureBox_spiral.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox_star.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox_polygon.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox_brown.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            pictureBox_round.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            pictureBox_circular.Location = new Point(x_st + dx * 0, y_st + dy * 1);

            groupBox1.Location = new Point(x_st + dx * 5, y_st + dy * 0 + 50);
            pictureBox_ellipse.Location = new Point(x_st + dx * 4 - 40, y_st + dy * 1);
            pictureBox_captcha1.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            pictureBox_captcha2.Location = new Point(x_st + dx * 0, y_st + dy * 2 + 120);
            pictureBox_captcha3.Location = new Point(x_st + dx * 0, y_st + dy * 2 + 120 * 2);
            pictureBox_random_pixel_image.Location = new Point(x_st + dx * 0, y_st + dy * 2 + 120 * 3);
            pictureBox_word.Location = new Point(x_st + dx * 1, y_st + dy * 2 + 120 * 3);

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

        private void DrawPoint(Graphics g, int cx, int cy, int size, Color c)
        {
            // Create a new pen.
            //顏色、線寬分開寫
            //Pen p = new Pen(c);
            // Set the pen's width.
            //p.Width = linewidth;

            //顏色、線寬寫在一起
            Pen p = new Pen(c, size);

            // Draw the circle
            g.DrawEllipse(p, new Rectangle(cx, cy, size, size));
            //Dispose of the pen.
            p.Dispose();
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


        //for random color ST
        void draw_random_color()
        {
            int x_st = 470;
            int y_st = 670;
            int WIDTH = 40;
            for (int i = 1; i < lb_color.Length; i++)
            {
                lb_color[i] = new Label();
                lb_color[i].Width = WIDTH;
                lb_color[i].Height = WIDTH;
                lb_color[i].Text = " ";
                lb_color[i].Location = new Point(x_st + lb_color_x, y_st + lb_color_y);
                _R = r.Next(256);
                _G = r.Next(256);
                _B = r.Next(256);
                lb_color[i].BackColor = Color.FromArgb(_R, _G, _B);
                this.Controls.Add(lb_color[i]);
                lb_color_x += WIDTH;

                if (i % 10 == 0)
                {
                    lb_color_x = 0;
                    lb_color_y += WIDTH;
                }
            }
            timer_random_color.Enabled = true;
        }

        private void timer_random_color_Tick(object sender, EventArgs e)
        {
            for (int i = 1; i < lb_color.Length; i++)
            {
                _R = r.Next(256);
                _G = r.Next(256);
                _B = r.Next(256);
                lb_color[i].BackColor = Color.FromArgb(_R, _G, _B);
            }
        }
        //for random color SP

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

        //3種 Captcha ST
        private void timer_draw_captcha_Tick(object sender, EventArgs e)
        {
            draw_captcha1();
            draw_captcha2();
            draw_captcha3();
        }

        void draw_captcha1()
        {
            string txt = "This is a lion-mouse";

            Bitmap bm = MakeCaptchaImge1(txt,
                50, 70,
                pictureBox_captcha1.ClientSize.Width,
                pictureBox_captcha1.ClientSize.Height);
            pictureBox_captcha1.Image = bm;
        }

        void draw_captcha2()
        {
            string txt = "This is a lion-mouse";

            using (Font the_font = new Font("Times New Roman", 30))
            {
                pictureBox_captcha2.Image = MakeCaptchaImage2(txt,
                    pictureBox_captcha2.ClientSize.Width,
                    pictureBox_captcha2.ClientSize.Height,
                    the_font, Brushes.Blue);
            }
        }

        //產生驗證圖片 ST
        void draw_captcha3()
        {
            //產生驗證圖片

            //從已知幾個元素中任意選出幾個
            int num = 10;

            string vaildNumAnswer = "";

            Random rr = new Random();

            List<char> myList = new List<char>();   //用來存放篩選後的字

            /*  不均勻分配
            myList.Add('A');
            myList.Add('A');
            myList.Add('A');
            myList.Add('B');
            myList.Add('C');
            */

            //特定分配
            for (int i = 50; i <= 57; i++)
                //ASCII碼，找出數字
                myList.Add((char)i); //從2開始，排除了0，1，放入列表


            for (int i = 65; i <= 90; i++)
            {
                //ASCII碼，找出大寫英文
                if (i == 73) continue; //排除I
                if (i == 79) continue; //排除O
                myList.Add((char)i);
            }


            for (int i = 97; i <= 122; i++)
            {
                //參考ASCII碼，找出小寫英文
                if (i == 108) continue; //排除l
                if (i == 111) continue; //排除o
                myList.Add((char)i);
            }


            char[] texts = new char[myList.Count];
            texts = myList.ToArray();

            //亂數產生驗證答案
            vaildNumAnswer = "";
            for (int i = 1; i <= num; i++)
            {
                char c = texts[rr.Next(texts.Length)];
                vaildNumAnswer += c;
            }
            //richTextBox1.Text += vaildNumAnswer + "\n";

            RenderImage(vaildNumAnswer);
        }

        //產生驗證圖片
        private void RenderImage(string vaildNumAnswer)
        {
            Random rr = new Random();

            int num = 10;
            int ww = 30 * 2 + num * 20;
            //寬度=(留邊)30*2 + 每個字*20
            int hh = 70;

            Bitmap vaildNumImage = new Bitmap(ww, hh);
            Graphics g = Graphics.FromImage(vaildNumImage);

            //產生背景色
            Color cc = Color.FromArgb(rr.Next(256), rr.Next(256), rr.Next(256));
            Brush bb = new SolidBrush(cc);
            g.FillRectangle(bb, 0, 0, ww, hh);

            //產生字色，斥掉背景色
            bb = new SolidBrush(Color.FromArgb(cc.R ^ 255, cc.G ^ 255, cc.B ^ 255));
            //產生字體
            Font ff = new Font("Arial Black", 18, FontStyle.Regular);
            //逐一畫每一個字

            for (int i = 0; i < vaildNumAnswer.Length; i++)
            {
                g.DrawString(vaildNumAnswer.Substring(i, 1), ff, bb, i * 20 + 30, 20);
            }

            //加入雜點
            bb = new SolidBrush(Color.White);
            for (int i = 1; i <= 500; i++)
            {
                g.FillRectangle(bb, rr.Next(ww), rr.Next(hh), 2, 2);
            }
            pictureBox_captcha3.Image = vaildNumImage;
        }
        //產生驗證圖片 SP

        private Random Rand = new Random();

        // Make a captcha image for the text.
        private Bitmap MakeCaptchaImge1(string txt, int min_size, int max_size, int wid, int hgt)
        {
            // Make the bitmap and associated Graphics object.
            Bitmap bm = new Bitmap(wid, hgt);
            using (Graphics g = Graphics.FromImage(bm))
            {
                g.SmoothingMode = SmoothingMode.HighQuality;
                g.Clear(Color.White);

                // See how much room is available for each character.
                int ch_wid = (int)(wid / txt.Length);

                // Draw each character.
                for (int i = 0; i < txt.Length; i++)
                {
                    float font_size = Rand.Next(min_size, max_size);
                    using (Font the_font = new Font("Times New Roman", font_size, FontStyle.Bold))
                    {
                        DrawCharacter1(txt.Substring(i, 1), g, the_font, i * ch_wid, ch_wid, wid, hgt);
                    }
                }
            }

            return bm;
        }

        // Draw a deformed character at this position.
        private int PreviousAngle = 0;
        private void DrawCharacter1(string txt, Graphics g, Font the_font, int X, int ch_wid, int wid, int hgt)
        {
            // Center the text.
            using (StringFormat string_format = new StringFormat())
            {
                string_format.Alignment = StringAlignment.Center;
                string_format.LineAlignment = StringAlignment.Center;
                RectangleF rectf = new RectangleF(X, 0, ch_wid, hgt);

                // Convert the text into a path.
                using (GraphicsPath graphics_path = new GraphicsPath())
                {
                    graphics_path.AddString(txt,
                        the_font.FontFamily, (int)(Font.Style),
                        the_font.Size, rectf, string_format);

                    // Make random warping parameters.
                    float x1 = (float)(X + Rand.Next(ch_wid) / 2);
                    float y1 = (float)(Rand.Next(hgt) / 2);
                    float x2 = (float)(X + ch_wid / 2 + Rand.Next(ch_wid) / 2);
                    float y2 = (float)(hgt / 2 + Rand.Next(hgt) / 2);
                    PointF[] pts = {
                    new PointF(
                        (float)(X + Rand.Next(ch_wid) / 4),
                        (float)(Rand.Next(hgt) / 4)),
                    new PointF(
                        (float)(X + ch_wid - Rand.Next(ch_wid) / 4),
                        (float)(Rand.Next(hgt) / 4)),
                    new PointF(
                        (float)(X + Rand.Next(ch_wid) / 4),
                        (float)(hgt - Rand.Next(hgt) / 4)),
                    new PointF(
                        (float)(X + ch_wid - Rand.Next(ch_wid) / 4),
                        (float)(hgt - Rand.Next(hgt) / 4))
                };
                    Matrix mat = new Matrix();
                    graphics_path.Warp(pts, rectf, mat,
                        WarpMode.Perspective, 0);

                    // Rotate a bit randomly.
                    float dx = (float)(X + ch_wid / 2);
                    float dy = (float)(hgt / 2);
                    g.TranslateTransform(-dx, -dy, MatrixOrder.Append);
                    int angle = PreviousAngle;
                    do
                    {
                        angle = Rand.Next(-30, 30);
                    } while (Math.Abs(angle - PreviousAngle) < 20);
                    PreviousAngle = angle;
                    g.RotateTransform(angle, MatrixOrder.Append);
                    g.TranslateTransform(dx, dy, MatrixOrder.Append);

                    // Draw the text.
                    g.FillPath(Brushes.Blue, graphics_path);
                    g.ResetTransform();
                }
            }
        }

        // Draw the words with letters overlapping each other.
        private Bitmap MakeCaptchaImage2(string txt, int wid, int hgt, Font the_font, Brush the_brush)
        {
            Bitmap bm = new Bitmap(wid, hgt);
            using (Graphics g = Graphics.FromImage(bm))
            {
                g.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;

                int x = 0;
                foreach (char ch in txt.ToCharArray())
                {
                    SizeF ch_size = g.MeasureString(ch.ToString(), the_font);
                    int y = (int)(Rand.NextDouble() * (hgt - ch_size.Height));
                    g.DrawString(ch.ToString(), the_font, the_brush, x, y);
                    x += (int)(ch_size.Width * 0.35);
                }
            }
            return bm;
        }

        //3種 Captcha SP

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

        void draw_random_pixel_image()
        {
            int W = pictureBox_random_pixel_image.ClientSize.Width;
            int H = pictureBox_random_pixel_image.ClientSize.Height;

            //bitmap
            Bitmap bmp = new Bitmap(W, H);

            //random number
            Random rand = new Random();

            //create random pixels
            for (int y = 0; y < H; y++)
            {
                for (int x = 0; x < W; x++)
                {
                    //generate random ARGB value
                    int a = rand.Next(256);
                    int r = rand.Next(256);
                    int g = rand.Next(256);
                    int b = rand.Next(256);

                    //set ARGB value
                    bmp.SetPixel(x, y, Color.FromArgb(a, r, g, b));
                }
            }

            //load bmp in picturebox1
            pictureBox_random_pixel_image.Image = bmp;
        }

        private void timer_random_pixel_image_Tick(object sender, EventArgs e)
        {
            draw_random_pixel_image();
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

        #region 畫字
        void draw_word()
        {
            //g.DrawRectangle(Pens.Red, 0, 0, 100 - 1, 100 - 1);

            Font f = new Font("標楷體", 60);
            int tmp_width = 0;
            int tmp_height = 0;
            string str = word_string[word_position].ToString();

            tmp_width = gw.MeasureString(str, f).ToSize().Width;
            tmp_height = gw.MeasureString(str, f).ToSize().Height;

            //richTextBox1.Text += tmp_width.ToString() + " " + tmp_height.ToString() + "\n";

            gw.Clear(Color.LightGray);
            gw.DrawRectangle(Pens.Red, 0, 0, tmp_width - 1, tmp_height - 1);

            gw.DrawString(str, new Font("標楷體", 50), Brushes.Navy, 10, 10);

            word_position++;
            if (word_position >= word_string.Length)
                word_position = 0;

            pictureBox_word.Image = bmp;
        }

        private void timer_word_Tick(object sender, EventArgs e)
        {
            draw_word();
        }
        #endregion


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

        //布朗運動 ST
        void draw_brown_motion()
        {
            int N = 50;
            Point[] pt;

            int W = pictureBox_brown.ClientSize.Width;
            int H = pictureBox_brown.ClientSize.Height;
            int i;

            pt = new Point[N];    //一維陣列內有N個Point

            Random rand = new Random();
            for (i = 0; i < N; i++)
            {
                pt[i] = new Point(rand.Next(W), rand.Next(H));

            }

            //新建圖檔, 初始化畫布
            Bitmap bitmap1 = new Bitmap(pictureBox_brown.Width, pictureBox_brown.Height);
            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);
            pictureBox_brown.Image = bitmap1;

            g.DrawLines(Pens.Red, pt);

            int r = 5;
            for (i = 0; i < N; i++)
            {
                g.FillEllipse(Brushes.Red, pt[i].X - r, pt[i].Y - r, r * 2, r * 2);
            }
        }

        private void timer_brown_Tick(object sender, EventArgs e)
        {
            draw_brown_motion();
        }
        //布朗運動 SP

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

        int angle = 0;
        int rr = 30;
        void draw_spiral()
        {
            if (angle == 0)
            {
                g_spiral.Clear(Color.White);
            }

            int W = pictureBox_spiral.ClientSize.Width;
            int H = pictureBox_spiral.ClientSize.Height;

            //螺旋
            int cx = W / 2;
            int cy = H / 2;
            int dx;
            int dy;
            int x_st = 0;
            int y_st = 0;
            dx = (int)(rr * Math.Cos(angle * Math.PI / 180));
            dy = (int)(rr * Math.Sin(angle * Math.PI / 180));
            x_st = cx + dx;
            y_st = cy + dy;

            Random rand = new Random();
            DrawPoint(g_spiral, x_st, y_st, 5, Color.FromArgb(rand.Next(256), rand.Next(256), rand.Next(256)));

            if ((angle % 30) == 0)
                rr++;

            angle += 10;
            if (angle >= 3000)
            {
                angle = 0;
                rr = 30;
            }
        }

        private void timer_spiral_Tick(object sender, EventArgs e)
        {
            draw_spiral();
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
    }
}
