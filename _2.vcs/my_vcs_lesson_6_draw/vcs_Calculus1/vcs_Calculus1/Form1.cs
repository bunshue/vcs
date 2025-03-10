﻿using System;
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
        bool flag_grid_on = true;
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 1240;
            y_st = 40;
            dx = 130;
            dy = 50;

            button1.Location = new Point(10, 10);
            pictureBox1.Location = new Point(20 + 120, 10);
            pictureBox1.ClientSize = new Size(800 + 100, 700);
            richTextBox1.Size = new Size(300, 600);
            richTextBox1.Location = new Point(840 + 110 + 100, 10);

            this.Size = new Size(1400, 800);
        }

        private double sind(double d)
        {
            return Math.Sin(d * Math.PI / 180.0);
        }

        void plot_figure(List<PointF> points)
        {
            int i;
            int j;
            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;
            int border_w = 50;
            int border_h = 50;
            int offset_x = 0;
            int offset_y = 0;
            int w = W - border_w * 2;
            int h = H - border_h * 2;

            offset_x = border_w;
            offset_y = border_h;

            Bitmap bitmap1 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap1);

            richTextBox1.Text += "W = " + W.ToString() + "\n";
            richTextBox1.Text += "H = " + H.ToString() + "\n";
            richTextBox1.Text += "w = " + w.ToString() + "\n";
            richTextBox1.Text += "h = " + h.ToString() + "\n";

            g.SmoothingMode = SmoothingMode.AntiAlias;

            if (flag_grid_on == true)
            {
                for (i = 0; i <= W; i += 50)
                {
                    //直線
                    g.DrawLine(Pens.LightGray, i, 0, i, H);

                }
                for (j = 0; j <= H; j += 50)
                {
                    //橫線
                    g.DrawLine(Pens.LightGray, 0, j, W, j);
                }
            }

            //處理數據
            int len = points.Count();
            richTextBox1.Text += "len = " + len.ToString() + "\n";

            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += points[i].ToString() + " ";

            }
            richTextBox1.Text += "\n\n";

            float x_max = -10000;
            float x_min = 10000;
            float y_max = -10000;
            float y_min = 10000;

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

            //if (x_min < 0)
            {
                offset_x = -(int)x_min;
            }
            //if (y_min <= 0)
            {
                offset_y = -(int)y_min;
            }

            float ratio_x = 0;
            float ratio_y = 0;

            ratio_x = w / (x_max - x_min);
            ratio_y = h / (y_max - y_min);

            richTextBox1.Text += "ratio_x = " + ratio_x.ToString() + "\n";
            richTextBox1.Text += "ratio_y = " + ratio_y.ToString() + "\n";

            richTextBox1.Text += "offset_x = " + offset_x.ToString() + "\n";
            richTextBox1.Text += "offset_y = " + offset_y.ToString() + "\n";

            List<PointF> points_new = new List<PointF>();

            for (i = 0; i < len; i++)
            {
                //ratio_y = 1;
                //points_new.Add(new PointF(offset_x + points[i].X * ratio_x, h - (offset_y + points[i].Y * ratio_y)));
                points_new.Add(new PointF(border_w + (offset_x + points[i].X) * ratio_x, h + border_h - (offset_y + points[i].Y) * ratio_y));
            }

            Pen p = new Pen(Color.Red, 0);
            g.DrawLines(p, points_new.ToArray());

            Point p1;
            Point p2;

            if ((y_max > 0) && (y_min < 0))
            {
                p1 = new Point(border_w + 0, h + border_h - (int)((offset_y + 0) * ratio_y));
                p2 = new Point(border_w + w, h + border_h - (int)((offset_y + 0) * ratio_y));
                g.DrawLine(Pens.Black, p1, p2);  //X軸
                richTextBox1.Text += "可以畫X軸\n";
                richTextBox1.Text += "p1 : " + p1.ToString() + "\n";
                richTextBox1.Text += "p2 : " + p2.ToString() + "\n";

                g.DrawString(x_min.ToString(), new Font("標楷體", 10), new SolidBrush(Color.Black), p1.X - 15, p1.Y + 5);
                g.DrawString(x_max.ToString(), new Font("標楷體", 10), new SolidBrush(Color.Black), p2.X - 15, p2.Y + 5);

                //要畫 0

            }

            if ((x_max > 0) && (x_min < 0))
            {
                p1 = new Point(border_w + (int)((0 - x_min) * ratio_x), border_h + 0);
                p2 = new Point(border_w + (int)((0 - x_min) * ratio_x), border_h + h);
                g.DrawLine(Pens.Black, p1, p2);    //Y軸
                richTextBox1.Text += "可以畫Y軸\n";
                richTextBox1.Text += "p1 : " + p1.ToString() + "\n";
                richTextBox1.Text += "p2 : " + p2.ToString() + "\n";

                g.DrawString(y_max.ToString(), new Font("標楷體", 10), new SolidBrush(Color.Black), p1.X - 15, p1.Y + 5);
                g.DrawString(y_min.ToString(), new Font("標楷體", 10), new SolidBrush(Color.Black), p2.X - 15, p2.Y + 5);
            }

            g.DrawRectangle(Pens.Red, border_w, border_h, w, h);
            richTextBox1.Text += "w = " + w.ToString() + "\n";
            richTextBox1.Text += "h = " + h.ToString() + "\n";
            pictureBox1.Image = bitmap1;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            float dx = 10.0f;
            List<PointF> points = new List<PointF>();
            //for (float x = -5; x <= 5; x += dx)
            for (float x = -200; x <= 200; x += dx)
            {
                float y = function(x);
                points.Add(new PointF(x, y));
            }

            richTextBox1.Text += "len = " + points.Count.ToString() + "\n";

            plot_figure(points);
        }

        private float function(float x)
        {
            //return (float)(x * x + 2 * x + 1);
            return (float)(sind(3 * x) * 100);
        }
    }
}

