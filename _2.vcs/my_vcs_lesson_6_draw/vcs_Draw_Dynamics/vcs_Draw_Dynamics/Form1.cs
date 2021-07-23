using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for DashStyle

namespace vcs_Draw_Dynamics
{
    public partial class Form1 : Form
    {
        int W = 0;
        int H = 0;

        int x_st = 0;
        int y_st = 0;

        int t = 0;
        int vx = 10;
        int vy = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            W = pictureBox1.Width;
            H = pictureBox1.Height;
            x_st = 0;
            y_st = 500;
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
            x_st = 850;
            y_st = 10;
            dx = 110;
            dy = 45;

            //richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 11);
            //richTextBox1.Size = new Size(richTextBox1.Size.Width, this.Height - richTextBox1.Location.Y - 50);

            //pictureBox1.Location = new Point(10, 10);
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

        private void DrawCircle(PaintEventArgs e, int center_x, int center_y, int radius, int linewidth, Color c)
        {
            // Create a new pen.
            //顏色、線寬分開寫
            //Pen p = new Pen(c);
            // Set the pen's width.
            //p.Width = linewidth;

            //顏色、線寬寫在一起
            Pen p = new Pen(c, linewidth);

            // Draw the circle
            e.Graphics.DrawEllipse(p, new Rectangle(center_x - radius, center_y - radius, radius * 2, radius * 2));
            //Dispose of the pen.
            p.Dispose();
        }

        private void DrawFillCircle(PaintEventArgs e, int center_x, int center_y, int radius, Color c)
        {
            SolidBrush newBrush = new SolidBrush(c);

            // Fill the circle
            e.Graphics.FillEllipse(newBrush, new Rectangle(center_x - radius, center_y - radius, radius * 2, radius * 2));

            //Dispose of the brush
            newBrush.Dispose();
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            int g = 10;
            /*
            SolidBrush redBrush = new SolidBrush(Color.Red);
            //e.Graphics.DrawRectangle(new Pen(Color.Red, 1), x_st - sw / 2, y_st - sh / 2, sw, sh);

            x_st = 100;
            y_st = 100;

            DrawCircle(e, x_st, H - y_st, 15, 2, Color.Red);

            x_st = 200;
            y_st = 200;

            DrawFillCircle(e, x_st, H - y_st, 15, Color.Red);
            */

            Pen p = new Pen(Color.Red, 2);
            p.DashStyle = DashStyle.Dot;
            Point p1 = new Point();
            Point p2 = new Point();

            p1.X = 0;
            p1.Y = H - 500;
            p2.X = 200;
            p2.Y = H - 500;
            e.Graphics.DrawLine(p, p1, p2);


            p1.X = 200;
            p1.Y = H;
            p2.X = 200;
            p2.Y = H - 500;
            e.Graphics.DrawLine(p, p1, p2);


            DrawFillCircle(e, x_st, H - y_st, 15, Color.Red);


            richTextBox1.Text += "t = " + t.ToString() + "\tx = " + x_st.ToString() + "\ty = " + y_st.ToString() + "\t";
            richTextBox1.Text += "vx = " + vx.ToString() + "\tvy = " + vy.ToString() + "\n";

            x_st += vx * 1;

            if (x_st > 1000)
            {
                timer1.Enabled = false;
            }

            if (x_st > 200)
            {
                vy += g * 1;
                y_st -= vy * 1;

            }
            if (y_st <= 0)
            {
                timer1.Enabled = false;
            }
            t++;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            this.pictureBox1.Invalidate();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            t = 0;
            x_st = 0;
            y_st = 500;
            vx = 10;
            vy = 0;
            timer1.Enabled = true;

            vx = 10 * (int)trackBar1.Value;
            richTextBox1.Text += "初速度 : " + vx.ToString() + " m/s\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            timer1.Enabled = false;
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            vx = 10 * (int)trackBar1.Value;
            richTextBox1.Text += "初速度 : " + vx.ToString() + " m/s\n";
        }
    }
}
