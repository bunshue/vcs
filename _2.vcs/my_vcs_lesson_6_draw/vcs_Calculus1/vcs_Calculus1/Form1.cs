using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace vcs_Calculus1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox1.ClientSize = new Size(500, 500);
        }

        private double sind(double d)
        {
            return Math.Sin(d * Math.PI / 180.0);
        }


        private float F_normal2(float x)
        {
            //return (float)(x * x + 2 * x + 1);
            return (float)(sind(3 * x) * 200-0);
        }

        void plot_figure(List<PointF> points)
        {
            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;
            int border_w = 0;
            int border_h = 0;
            int offset_x = 0;
            int offset_y = 0;
            int w = W - border_w * 2;
            int h = H - border_h * 2;

            offset_x = border_w;
            offset_y = border_h;

            Bitmap bitmap1 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap1);

            g.SmoothingMode = SmoothingMode.AntiAlias;

            //處理數據
            int len = points.Count();
            richTextBox1.Text += "len = " + len.ToString() + "\n";
            int i;
            float x_max = 0;
            float x_min = 0;
            float y_max = 0;
            float y_min = 0;

            for (i = 0; i < len; i++)
            {
                if (x_max < points[i].X)
                    x_max = points[i].X;
                if (x_min > points[i].X)
                    x_min = points[i].X;

                if (y_max < points[i].Y)
                    y_max = points[i].Y;
                if (y_min > points[i].Y)
                    y_min = points[i].Y;

            }
            richTextBox1.Text += "x_max = " + x_max.ToString() + "\n";
            richTextBox1.Text += "x_min = " + x_min.ToString() + "\n";
            richTextBox1.Text += "y_max = " + y_max.ToString() + "\n";
            richTextBox1.Text += "y_min = " + y_min.ToString() + "\n";

            if (x_min < 0)
            {
                offset_x = -(int)x_min;
            }
            if (y_min < 0)
            {
                offset_y = -(int)y_min;
            }

            float ratio_x = 0;
            float ratio_y = 0;

            ratio_x = w / (x_max - x_min + 1);
            ratio_y = h / (y_max - y_min + 1);

            ratio_x = 1;
            ratio_y = 1;

            richTextBox1.Text += "ratio_x = " + ratio_x.ToString() + "\n";
            richTextBox1.Text += "ratio_y = " + ratio_y.ToString() + "\n";

            richTextBox1.Text += "offset_x = " + offset_x.ToString() + "\n";
            richTextBox1.Text += "offset_y = " + offset_y.ToString() + "\n";

            List<PointF> points_new = new List<PointF>();

            for (i = 0; i < len; i++)
            {
                points_new.Add(new PointF(offset_x + points[i].X * ratio_x, h - (offset_y + points[i].Y * ratio_y)));
            }

            Pen p = new Pen(Color.Red, 0);
            g.DrawLines(p, points_new.ToArray());

            Point p1;
            Point p2;

            p1 = new Point(0, h-offset_y);
            p2 = new Point(w, h-offset_y);
            g.DrawLine(p, p1, p2);

            richTextBox1.Text += "p1 : " + p1.ToString() + "\n";
            richTextBox1.Text += "p2 : " + p2.ToString() + "\n";

            p1 = new Point(offset_x, h-0);
            p2 = new Point(offset_x, h-h);
            g.DrawLine(p, p1, p2);

            richTextBox1.Text += "p1 : " + p1.ToString() + "\n";
            richTextBox1.Text += "p2 : " + p2.ToString() + "\n";

            g.DrawRectangle(Pens.Red, border_w, border_h, w, h);
            richTextBox1.Text += "w = " + w.ToString() + "\n";
            richTextBox1.Text += "h = " + h.ToString() + "\n";
            pictureBox1.Image = bitmap1;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            float dx = 1.0f;
            List<PointF> points = new List<PointF>();
            //for (float x = -5; x <= 5; x += dx)
            for (float x = -250; x <= 250; x += dx)
            {
                float y = F_normal2(x);
                points.Add(new PointF(x, y));
            }

            richTextBox1.Text += "len = " + points.Count.ToString() + "\n";

            plot_figure(points);
        }
    }
}
