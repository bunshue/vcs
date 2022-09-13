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

        }

        private double sind(double d)
        {
            return Math.Sin(d * Math.PI / 180.0);
        }


        private float F_normal2(float x)
        {
            //return (float)(x * x + 2 * x + 1);
            return (float)(sind(3 * x) * 100);
        }

        void plot_figure(List<PointF> points)
        {
            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;

            Bitmap bitmap1 = new Bitmap(W, H);
            using (Graphics g = Graphics.FromImage(bitmap1))
            {
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


                float ratio_x = 0;
                float ratio_y = 0;

                ratio_x = W / (x_max - x_min + 1);
                ratio_y = H / (y_max - y_min + 1);

                richTextBox1.Text += "ratio_x = " + ratio_x.ToString() + "\n";
                richTextBox1.Text += "ratio_y = " + ratio_y.ToString() + "\n";



                using (Pen p = new Pen(Color.Red, 0))
                {

                    List<PointF> points_new = new List<PointF>();

                    for (i = 0; i < len; i++)
                    {
                        points_new.Add(new PointF(points[i].X * ratio_x, H - points[i].Y * ratio_y));
                    }



                    g.DrawLines(p, points_new.ToArray());
                }
            }

            pictureBox1.Image = bitmap1;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            float dx = 1.0f;
            List<PointF> points = new List<PointF>();
            //for (float x = -5; x <= 5; x += dx)
            for (float x = 0; x <= 360; x += dx)
            {
                float y = F_normal2(x);
                points.Add(new PointF(x, y));
            }

            richTextBox1.Text += "len = " + points.Count.ToString() + "\n";

            plot_figure(points);
        }
    }
}
