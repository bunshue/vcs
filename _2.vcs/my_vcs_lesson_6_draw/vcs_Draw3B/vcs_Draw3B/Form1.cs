using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for SmoothingMode

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


        Graphics ge;
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
            for (int i = 0; i < 360*3; i += 10)
            {
                dx = (int)(r * Math.Cos(i * Math.PI / 180));
                dy = (int)(r * Math.Sin(i * Math.PI / 180));
                cx = 100 + dx;
                cy = 100 + dy;
                DrawPoint(g, cx, cy, 5, Color.Red);
                delay(20);
                if ((i % 100) == 0)
                    r += 5;
            }
            g.DrawLine(Pens.Red, 0, 0, 100, 100);
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


    }
}
