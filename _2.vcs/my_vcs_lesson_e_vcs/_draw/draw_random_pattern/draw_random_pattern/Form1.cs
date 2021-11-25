using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace draw_random_pattern
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


        private int RetrievRandomCorners(int minCorners, int maxCorners)
        {
            return new Random(Guid.NewGuid().GetHashCode()).Next(minCorners, maxCorners);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int minCorners = 0;
            int maxCorners = 0;

            if (radioButton1.Checked == true)
            {
                this.Text = "竹葉";
                minCorners = 3;
                maxCorners = 4;
            }
            else if (radioButton2.Checked == true)
            {
                this.Text = "長葉草";
                minCorners = 20;
                maxCorners = 38;
            }
            else if (radioButton3.Checked == true)
            {
                this.Text = "雜亂石頭";
                minCorners = 3;
                maxCorners = 4;
            }
            else if (radioButton4.Checked == true)
            {
                this.Text = "天上繁星";
                minCorners = 3;
                maxCorners = 4;
            }
            else
            {
                this.Text = "未選取";
                return;
            }

            int width = 500;
            int height = 500;
            int x = 0;
            int y = 0;
            int numX = 10;
            int numY = 10;
            float perX = width * 1f / numX;
            float perY = height * 1f / numY;
            Bitmap image = new Bitmap(width, height);
            Graphics g = Graphics.FromImage(image);

            g.CompositingQuality = CompositingQuality.HighQuality;
            g.SmoothingMode = SmoothingMode.HighQuality;
            g.InterpolationMode = InterpolationMode.HighQualityBicubic;

            g.FillRectangle(Brushes.Black, new Rectangle(0, 0, width, height));

            int lastCorners = minCorners;
            for (int i = 0; i < numX; i++)
            {
                for (int j = 0; j < numY; j++)
                {
                    long tick = DateTime.Now.Ticks;
                    Random random = new Random((int)(tick & 0xffffffff) | (int)(tick >> 32));
                    int corners = random.Next(minCorners, maxCorners);
                    if (Math.Abs(corners - lastCorners) < (maxCorners - minCorners) / 2) corners = RetrievRandomCorners(minCorners, maxCorners);
                    lastCorners = corners;


                    if (radioButton1.Checked == true)
                    {
                        this.Text = "竹葉";
                        PointF[] points = Stone.CreateStone(new Point((int)(perX * j), (int)(perY * i)), (int)(perX * 1.4f), (int)(perX * 0.009f), corners);
                        g.FillClosedCurve(Brushes.Green, points, FillMode.Winding);
                    }
                    else if (radioButton2.Checked == true)
                    {
                        this.Text = "長葉草";
                        PointF[] points = Stone.CreateStone(new Point((int)(perX * j), (int)(perY * i)), (int)(perX * 0.88f), (int)(perX * 0.01f), corners);
                        g.FillClosedCurve(Brushes.Green, points, FillMode.Winding);
                    }
                    else if (radioButton3.Checked == true)
                    {
                        this.Text = "雜亂石頭";
                        PointF[] points = Stone.CreateStone(new Point((int)(perX * j), (int)(perY * i)), (int)(perX * 0.4f), (int)(perX * 0.396f), corners);
                        g.FillClosedCurve(Brushes.Gray, points, FillMode.Winding);
                    }
                    else if (radioButton4.Checked == true)
                    {
                        this.Text = "天上繁星";
                        PointF[] points = Stone.CreateStone(new Point((int)(perX * j), (int)(perY * i)), (int)(perX * 0.18f), (int)(perX * 0.06f), corners);
                        g.FillClosedCurve(Brushes.White, points, FillMode.Winding);
                    }
                    else
                    {
                        this.Text = "未選取";
                        return;
                    }

                }
            }
            pictureBox1.Image = image;
        }
    }

    public static class Stone
    {
        public static PointF[] CreateStone(Point center, int outerRadius, int inner_radius, int arms)
        {
            int center_x = center.X;
            int center_y = center.Y;
            PointF[] points = new PointF[arms * 2];
            double offset = Math.PI / 2;
            double arc = 2 * Math.PI / arms;
            double half = arc / 2;
            double angle = 0;
            for (int i = 0; i < arms; i++)
            {
                Random randomOuter = new Random((int)DateTime.Now.Ticks);
                outerRadius = outerRadius - randomOuter.Next((int)(inner_radius * 0.06 * new Random().Next(-20, 20) / 30d), (int)(inner_radius * 0.08));
                //outerRadius = outerRadius - randomOuter.Next((int)(inner_radius * 0.16 * new Random().Next(-20, 20) / 30d), (int)(inner_radius * 0.18));
                Random randomInner = new Random(Guid.NewGuid().GetHashCode());
                inner_radius = inner_radius + randomInner.Next((int)(inner_radius * 0.02 * new Random().Next(-100, 100) / 150d), (int)(inner_radius * 0.08));
                //inner_radius = inner_radius + randomInner.Next((int)(inner_radius * 0.02 * new Random().Next(-100, 100) / 150d), (int)(inner_radius * 0.22));

                if (inner_radius > outerRadius)
                {
                    int temp = outerRadius;
                    outerRadius = inner_radius;
                    inner_radius = temp;
                }
                double angleTemp = arc * randomInner.Next(-5, 5) / 10d;
                angle = i * arc;
                angle += angleTemp;
                points[i * 2].X = (float)(center_x + Math.Cos(angle - offset) * outerRadius);
                points[i * 2].Y = (float)(center_y + Math.Sin(angle - offset) * outerRadius);
                points[i * 2 + 1].X = (float)(center_x + Math.Cos(angle + half - offset) * inner_radius);
                points[i * 2 + 1].Y = (float)(center_y + Math.Sin(angle + half - offset) * inner_radius);
            }

            return points;
        }
    }
}
