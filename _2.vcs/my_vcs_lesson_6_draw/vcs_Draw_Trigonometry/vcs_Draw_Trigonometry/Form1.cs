﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Draw_Trigonometry
{
    public partial class Form1 : Form
    {
        private const int N = 3;    //total_points
        private const int A = 100;  //Amplitude

        int pt_selected = -1;  // 動態陣列 的 第幾個 被選到
        bool flag_dragging_x = false; // 是否拖拉中
        bool flag_dragging_y = false; // 是否拖拉中
        Pen p1 = new Pen(Color.Green, 1);
        Pen p2 = new Pen(Color.Blue, 1);
        Point[] pts = new Point[N];
        int Epsilon = 100; // 滑鼠 是否 點選到點 的距離 判斷 (避免 開根號)
        int[] array_sin = new int[91];
        int[] array_cos = new int[91];
        int[] array_tan = new int[91];

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

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            pts[0] = new Point(500, 100);
            pts[1] = new Point(100, 500);
            pts[2] = new Point(pts[0].X, pts[1].Y);

            int i = 0;
            for (i = 0; i <= 90; i++)
            {
                array_sin[i] = (int)(A * sind(i));
                array_cos[i] = (int)(A * cosd(i));

            }


            for (i = 0; i <= 90; i++)
            {
                //richTextBox1.Text += ((int)(100*sind(i))).ToString() + " ";
                richTextBox1.Text += array_sin[i].ToString() + " ";
            }

        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            int radius = 10;
            int W = 600;
            int H = 600;

            if (flag_dragging_x == true)
                e.Graphics.DrawPolygon(p1, pts);
            else if (flag_dragging_y == true)
                e.Graphics.DrawPolygon(p1, pts);
            else
                e.Graphics.DrawPolygon(p2, pts);

            FillCircle(e.Graphics, pts[0], radius, Color.Green);
            FillCircle(e.Graphics, pts[1], radius, Color.Red);
            FillCircle(e.Graphics, pts[2], radius, Color.Green);
            //e.Graphics.DrawString("移動圓點", new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(10, 370));

            e.Graphics.DrawString("B(" + pts[0].X.ToString() + ", " + (H - pts[0].Y).ToString() + ")", new Font("標楷體", 20), new SolidBrush(Color.Black), new PointF(pts[0].X - 70, pts[0].Y - 40));
            e.Graphics.DrawString("A(" + pts[1].X.ToString() + ", " + (H - pts[1].Y).ToString() + ")", new Font("標楷體", 20), new SolidBrush(Color.Black), new PointF(pts[1].X - 10 - 30, pts[1].Y + 15));
            e.Graphics.DrawString("C(" + pts[2].X.ToString() + ", " + (H - pts[2].Y).ToString() + ")", new Font("標楷體", 20), new SolidBrush(Color.Black), new PointF(pts[2].X - 10 - 70, pts[2].Y + 15));

            double AB = Math.Sqrt((pts[0].X - pts[1].X) * (pts[0].X - pts[1].X) + (pts[0].Y - pts[1].Y) * (pts[0].Y - pts[1].Y));
            double BC = Math.Sqrt((pts[0].X - pts[2].X) * (pts[0].X - pts[2].X) + (pts[0].Y - pts[2].Y) * (pts[0].Y - pts[2].Y));
            double CA = Math.Sqrt((pts[2].X - pts[1].X) * (pts[2].X - pts[1].X) + (pts[2].Y - pts[1].Y) * (pts[2].Y - pts[1].Y));

            e.Graphics.DrawString(AB.ToString("n2"), new Font("標楷體", 20), new SolidBrush(Color.Blue), new PointF((pts[0].X + pts[1].X) / 2, (pts[0].Y + pts[1].Y) / 2));
            e.Graphics.DrawString(BC.ToString(), new Font("標楷體", 20), new SolidBrush(Color.Blue), new PointF((pts[0].X + pts[2].X) / 2, (pts[0].Y + pts[2].Y) / 2));
            e.Graphics.DrawString(CA.ToString(), new Font("標楷體", 20), new SolidBrush(Color.Blue), new PointF((pts[2].X + pts[1].X) / 2 - 20, (pts[2].Y + pts[1].Y) / 2 + 10));

            double angle = Math.Acos(CA / AB) * 180 / Math.PI;
            e.Graphics.DrawString("θ=" + angle.ToString("n2") + "°", new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(pts[1].X + 20, pts[1].Y - 25));

            //XY軸
            e.Graphics.DrawLine(new Pen(Color.Black, 6), 3, 0, 3, H);
            e.Graphics.DrawLine(new Pen(Color.Black, 6), 3, H - 4, W, H - 4);

            int x_st = 650;
            int y_st = 100;
            int dy = 100;

            e.Graphics.DrawString("sin(θ)=       =         = " + (BC / AB).ToString("n6"), new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(x_st, y_st));
            e.Graphics.DrawString("cos(θ)=       =         = " + (CA / AB).ToString("n6"), new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(x_st, y_st + dy * 1));
            e.Graphics.DrawString("tan(θ)=       =         = " + (BC / CA).ToString("n6"), new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(x_st, y_st + dy * 2));
            e.Graphics.DrawString("cot(θ)=       =         = " + (CA / BC).ToString("n6"), new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(x_st, y_st + dy * 3));
            e.Graphics.DrawString("sec(θ)=       =         = " + (AB / CA).ToString("n6"), new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(x_st, y_st + dy * 4));
            e.Graphics.DrawString("csc(θ)=       =         = " + (AB / BC).ToString("n6"), new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(x_st, y_st + dy * 5));

            e.Graphics.DrawLine(Pens.Green, x_st + 120, y_st + 12, x_st + 140 + 60, y_st + 12);
            e.Graphics.DrawLine(Pens.Green, x_st + 120, y_st + 12 + dy * 1, x_st + 140 + 60, y_st + 12 + dy * 1);
            e.Graphics.DrawLine(Pens.Green, x_st + 120, y_st + 12 + dy * 2, x_st + 140 + 60, y_st + 12 + dy * 2);
            e.Graphics.DrawLine(Pens.Green, x_st + 120, y_st + 12 + dy * 3, x_st + 140 + 60, y_st + 12 + dy * 3);
            e.Graphics.DrawLine(Pens.Green, x_st + 120, y_st + 12 + dy * 4, x_st + 140 + 60, y_st + 12 + dy * 4);
            e.Graphics.DrawLine(Pens.Green, x_st + 120, y_st + 12 + dy * 5, x_st + 140 + 60, y_st + 12 + dy * 5);

            int dx = 115;
            e.Graphics.DrawLine(Pens.Green, x_st + 120 + dx, y_st + 12, x_st + 140 + 80 + dx, y_st + 12);
            e.Graphics.DrawLine(Pens.Green, x_st + 120 + dx, y_st + 12 + dy * 1, x_st + 140 + 80 + dx, y_st + 12 + dy * 1);
            e.Graphics.DrawLine(Pens.Green, x_st + 120 + dx, y_st + 12 + dy * 2, x_st + 140 + 80 + dx, y_st + 12 + dy * 2);
            e.Graphics.DrawLine(Pens.Green, x_st + 120 + dx, y_st + 12 + dy * 3, x_st + 140 + 80 + dx, y_st + 12 + dy * 3);
            e.Graphics.DrawLine(Pens.Green, x_st + 120 + dx, y_st + 12 + dy * 4, x_st + 140 + 80 + dx, y_st + 12 + dy * 4);
            e.Graphics.DrawLine(Pens.Green, x_st + 120 + dx, y_st + 12 + dy * 5, x_st + 140 + 80 + dx, y_st + 12 + dy * 5);

            e.Graphics.DrawString("對邊     " + BC.ToString(), new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(x_st + 130, y_st - 20));
            e.Graphics.DrawString("斜邊    " + AB.ToString("n2"), new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(x_st + 130, y_st + 20));

            e.Graphics.DrawString("鄰邊     " + CA.ToString(), new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(x_st + 130, y_st - 20 + dy * 1));
            e.Graphics.DrawString("斜邊    " + AB.ToString("n2"), new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(x_st + 130, y_st + 20 + dy * 1));

            e.Graphics.DrawString("對邊     " + BC.ToString(), new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(x_st + 130, y_st - 20 + dy * 2));
            e.Graphics.DrawString("鄰邊     " + CA.ToString(), new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(x_st + 130, y_st + 20 + dy * 2));



            e.Graphics.DrawString("鄰邊     " + CA.ToString(), new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(x_st + 130, y_st - 20 + dy * 3));
            e.Graphics.DrawString("對邊     " + BC.ToString(), new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(x_st + 130, y_st + 20 + dy * 3));

            e.Graphics.DrawString("斜邊    " + AB.ToString("n2"), new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(x_st + 130, y_st - 20 + dy * 4));
            e.Graphics.DrawString("鄰邊     " + CA.ToString(), new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(x_st + 130, y_st + 20 + dy * 4));

            e.Graphics.DrawString("斜邊    " + AB.ToString("n2"), new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(x_st + 130, y_st - 20 + dy * 5));
            e.Graphics.DrawString("對邊     " + BC.ToString(), new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(x_st + 130, y_st + 20 + dy * 5));

            /*

            x_st = 1200;
            y_st = 50;
            Point[] curvePoints = new Point[91];    //一維陣列內有 91 個Point
            int i;
            for (i = 0; i < 91; i++)
            {
                curvePoints[i].X = x_st + i;
                curvePoints[i].Y = 300 - (array_sin[i] + A);


            }
            e.Graphics.DrawCurve(new Pen(Color.Red, 3), curvePoints);
            //g3.DrawCurve(bluePen, curvePoints); //畫曲線

            //array_sin[i] = (int)sind(i);
            //array_sin[i] = (int)cosd(i);

            */



        }

        // 檢查是哪一個點被 選到
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            for (int i = 0; i < pts.Length; i++)
            {
                if (CheckSelected(pts[i], e.Location) == true)
                {
                    pt_selected = i;
                    //pts[pt_selected].X = e.X;
                    //pts[pt_selected].Y = e.Y;
                    //richTextBox1.Text += "選中 " + i.ToString() + "\n";
                    if (i == 0)
                    {
                        flag_dragging_y = true;
                        pts[pt_selected].Y = e.Y;
                        this.Cursor = Cursors.HSplit;
                    }
                    else if (i == 2)
                    {
                        flag_dragging_x = true;
                        pts[pt_selected].X = e.X;
                        this.Cursor = Cursors.VSplit;
                    }
                    break;
                }
                else
                {
                    //richTextBox1.Text += "沒選中\n";
                }
            }
        }

        // 更新 被選到的點 的座標
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_dragging_x == true)
            {
                if (e.X >= pts[1].X)
                {
                    if (e.X < 1000)
                        pts[pt_selected].X = e.X;
                    else
                        pts[pt_selected].X = 1000;

                }
                else
                    pts[pt_selected].X = pts[1].X;

                pts[0].X = pts[pt_selected].X;

                this.pictureBox1.Invalidate();
            }
            else if (flag_dragging_y == true)
            {
                if (e.Y <= pts[2].Y)
                {
                    if (e.Y < 50)
                        pts[pt_selected].Y = 50;
                    else
                        pts[pt_selected].Y = e.Y;
                }
                else
                    pts[pt_selected].Y = pts[2].Y;

                this.pictureBox1.Invalidate();
            }
        }

        // 解除 被選到的點
        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            if ((flag_dragging_x == true) || (flag_dragging_y == true))
            {
                pt_selected = -1;
                flag_dragging_x = false;
                flag_dragging_y = false;
                this.pictureBox1.Invalidate();
                this.Cursor = Cursors.Default;
            }
        }

        // 檢查是否選到這個點
        bool CheckSelected(Point pt1, Point pt2)
        {
            int dist = (pt1.X - pt2.X) * (pt1.X - pt2.X) + (pt1.Y - pt2.Y) * (pt1.Y - pt2.Y);
            if (dist <= Epsilon) // dis 是尚未開根號 的距離
            {
                return true;
            }
            else
            {
                return false;
            }
        }

        private void FillCircle(Graphics g, PointF center, int radius, Color c)
        {
            SolidBrush sb = new SolidBrush(c);

            // Fill the circle
            g.FillEllipse(sb, new RectangleF(center.X - radius, center.Y - radius, radius * 2, radius * 2));

            //Dispose of the brush
            sb.Dispose();
        }
    }
}
