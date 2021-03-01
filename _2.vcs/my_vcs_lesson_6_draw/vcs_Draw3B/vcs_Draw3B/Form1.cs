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

namespace vcs_Draw3B
{
    public partial class Form1 : Form
    {
        //for random color ST
        //Reference : https://home.gamer.com.tw/creationDetail.php?sn=4281924
        private Label[] lb_color = new Label[101];
        Random r = new Random(Guid.NewGuid().GetHashCode());
        private int _R = 0, _G = 0, _B = 0;
        private int lb_color_x = 0, lb_color_y = 0;
        //for random color SP

        Graphics ge;    //for draw ellipse
        Graphics gs;    //for draw star
        private const int EllipseMargin = 10;
        private int EllipseCx, EllipseCy, EllipseWidth, EllipseHeight;
        private List<PointF> LinePoints = null;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 1810;
            y_st = 80;
            dx = 120;
            dy = 50;

            richTextBox1.Location = new Point(x_st + dx * 0 - 200, y_st + dy * 12);
            richTextBox1.Size = new Size(300, 320);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            bt_exit_setup();

            ge = pictureBox_ellipse.CreateGraphics();
            gs = pictureBox_star.CreateGraphics();
            // Calculate the ellipse parameters.
            EllipseWidth = this.pictureBox_ellipse.ClientSize.Width - 2 * EllipseMargin;
            EllipseHeight = this.pictureBox_ellipse.ClientSize.Height - 2 * EllipseMargin;

            draw_random_color();
            draw_spiral();
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

        void draw_spiral()
        {
            int W = pictureBox_spiral.ClientSize.Width;
            int H = pictureBox_spiral.ClientSize.Height;

            //螺旋
            Graphics g = pictureBox_spiral.CreateGraphics();
            int r = 50;
            int cx = W / 2;
            int cy = H / 2;
            int dx;
            int dy;
            for (int i = 0; i < 360 * 3; i += 10)
            {
                dx = (int)(r * Math.Cos(i * Math.PI / 180));
                dy = (int)(r * Math.Sin(i * Math.PI / 180));
                cx = 100 + dx;
                cy = 100 + dy;
                DrawPoint(g, cx, cy, 5, Color.Red);
                delay(20);
                if ((i % 100) == 0)
                {
                    r += 5;
                }
            }
            //g.DrawLine(Pens.Red, 0, 0, 100, 100);
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
            int x_st = 500;
            int y_st = 500;
            int WIDTH = 40;
            for (int i = 1; i < lb_color.Length; i++)
            {
                lb_color[i] = new Label();
                lb_color[i].Width = WIDTH;
                lb_color[i].Height = WIDTH;
                lb_color[i].Text = " ";
                lb_color[i].Location = new Point(x_st + lb_color_x, y_st + lb_color_y);
                _R = r.Next(255);
                _G = r.Next(255);
                _B = r.Next(255);
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
                _R = r.Next(255);
                _G = r.Next(255);
                _B = r.Next(255);
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
            DrawStar(gs, center, radius, linewidth, Color.Red);
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

                richTextBox1.Text += "pt[" + i.ToString() + "].X " + pt[i].X.ToString() + "\t" + "pt[" + i.ToString() + "].Y " + pt[i].Y.ToString() + "\n";
                pt[i].X += center.X;
                pt[i].Y += center.Y;
            }

            g.DrawPolygon(new Pen(Brushes.Red, linewidth), pt);     //空心星形
            //g.FillPolygon(Brushes.Blue, pt);                      //實心星形

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
                richTextBox1.Text += "points[" + i.ToString() + "], X = " + points[i].X + ", Y = " + points[i].Y + "\n";
            }

            for (i = 0; i < n; i++)
            {
                for (j = (i + 1); j < n; j++)
                {
                    richTextBox1.Text += "draw " + i.ToString() + " - " + j.ToString() + "\n";
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
            richTextBox1.Text += vaildNumAnswer + "\n";

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

    }
}
