using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_RandomWalk3
{
    public partial class Form1 : Form
    {
        private const int N = 300;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            make_random_walk_data();
        }

        List<Point> random_walk_data = new List<Point>();
        void make_random_walk_data()
        {
            int i;
            int x = 0;
            int y = 0;
            Random r = new Random();
            int rrrr;
            random_walk_data.Clear();
            random_walk_data.Add(new Point(x, y));

            for (i = 0; i < N; i++)
            {
                rrrr = r.Next(0, 4);
                if (rrrr == 0)
                {
                    //richTextBox1.Text += "上";
                    y -= 1;
                }
                else if (rrrr == 1)
                {
                    //richTextBox1.Text += "下";
                    y += 1;
                }
                else if (rrrr == 2)
                {
                    //richTextBox1.Text += "左";
                    x -= 1;
                }
                else if (rrrr == 3)
                {
                    //richTextBox1.Text += "右";
                    x += 1;
                }
                else
                {
                    richTextBox1.Text += "XXXX";
                }
                //richTextBox1.Text += " ";
                random_walk_data.Add(new Point(x, y));
            }

            richTextBox1.Text += "\n";
            for (i = 0; i < N; i++)
            {
                //richTextBox1.Text += random_walk_data[i].ToString() + "  ";

            }
        }

        int total_steps = 0;
        int current_step = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            total_steps = random_walk_data.Count;

            int i;
            int W = pictureBox1.Width;
            int H = pictureBox1.Height;
            int step = 50;

            //richTextBox1.Text += "111 W = " + W.ToString() + ", H = " + H.ToString() + "\n";
            W = (W / step) * step;
            H = (H / step) * step;
            //richTextBox1.Text += "222 W = " + W.ToString() + ", H = " + H.ToString() + "\n";
            int cx = (W / step + 1) / 2;
            int cy = (H / step + 1) / 2;

            //richTextBox1.Text += "cx = " + cx.ToString() + ", cy = " + cy.ToString() + "\n";

            Bitmap bitmap1 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap1);
            Pen bluePen = new Pen(Color.Blue, 8);
            Pen redPen = new Pen(Color.Red, 8);
            Pen grayPen = new Pen(Color.Gray, 3);

            int offset_x = 0;
            int offset_y = 0;
            int x1 = 0;
            int y1 = 0;
            int x2 = 0;
            int y2 = 0;

            for (i = 0; i <= W; i += step)
            {
                x1 = i;
                y1 = 0;
                x2 = i;
                y2 = H;
                Point px1 = new Point(x1, y1);
                Point px2 = new Point(x2, y2);
                g.DrawLine(grayPen, px1, px2);
                //richTextBox1.Text += "i = " + i.ToString() + "  ";
                //g.DrawRectangle(redPen, 100, 100, 100, 100);
            }

            for (i = 0; i <= H; i += step)
            {
                x1 = 0;
                y1 = i;
                x2 = W;
                y2 = i;
                Point px1 = new Point(x1, y1);
                Point px2 = new Point(x2, y2);
                g.DrawLine(grayPen, px1, px2);
                //richTextBox1.Text += "i = " + i.ToString() + "  ";
                //g.DrawRectangle(redPen, 100, 100, 100, 100);
            }

            Point corner = new Point(cx, cy); //起始點
            List<Point> points_draw1 = new List<Point>();
            List<Point> points_draw2 = new List<Point>();

            for (i = 0; i < current_step; i++)
            {
                x1 = corner.X + random_walk_data[i].X;
                y1 = corner.Y + random_walk_data[i].Y;

                x2 = offset_x + x1 * step;
                y2 = offset_y + y1 * step;

                points_draw1.Add(new Point(x2, y2));
            }
            if (points_draw1.Count > 1)
            {
                g.DrawLines(bluePen, points_draw1.ToArray());  //畫直線
            }

            if (current_step < total_steps)
            {
                current_step++;
            }
            else
            {
                richTextBox1.Text += "完成\n";
                timer1.Enabled = false;

                //current_step = 0;
            }

            pictureBox1.Image = bitmap1;

            g.Dispose();
        }
    }
}
