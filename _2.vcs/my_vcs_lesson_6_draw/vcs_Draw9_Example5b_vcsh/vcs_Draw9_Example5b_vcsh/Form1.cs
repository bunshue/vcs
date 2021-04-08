using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat
using System.Drawing.Drawing2D; //for CompositingQuality, SmoothingMode

namespace vcs_Draw9_Example5b_vcsh
{
    public partial class Form1 : Form
    {
        int W = 450;
        int H = 450;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            // Redraw on resize.
            this.ResizeRedraw = true;
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
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

            x_st = 10;
            y_st = 35;
            dx = W + 30;
            dy = H + 80;

            pictureBox0.Size = new Size(W, H);
            pictureBox1.Size = new Size(W, H);
            pictureBox2.Size = new Size(W, H);
            pictureBox3.Size = new Size(W, H);
            pictureBox4.Size = new Size(W, H - 50);
            pictureBox5.Size = new Size(W, H - 50);
            pictureBox6.Size = new Size(W, H - 100);
            pictureBox7.Size = new Size(W, H - 100);
            pictureBox0.BorderStyle = BorderStyle.Fixed3D;
            pictureBox1.BorderStyle = BorderStyle.Fixed3D;
            pictureBox2.BorderStyle = BorderStyle.Fixed3D;
            pictureBox3.BorderStyle = BorderStyle.Fixed3D;
            pictureBox4.BorderStyle = BorderStyle.Fixed3D;
            pictureBox5.BorderStyle = BorderStyle.Fixed3D;
            pictureBox6.BorderStyle = BorderStyle.Fixed3D;
            pictureBox7.BorderStyle = BorderStyle.Fixed3D;

            pictureBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox3.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            pictureBox4.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox5.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            pictureBox6.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            pictureBox7.Location = new Point(x_st + dx * 3, y_st + dy * 1);

            //groupBox0.Location = new Point(x_st + dx * 0, y_st + dy * 1 - 80);
            groupBox1.Location = new Point(x_st + dx * 1, y_st + dy * 1 - 80);
            //groupBox2.Location = new Point(x_st + dx * 2, y_st + dy * 1 - 80);
            groupBox3.Location = new Point(x_st + dx * 3, y_st + dy * 1 - 80);

            groupBox4.Location = new Point(x_st + dx * 0, y_st + dy * 2 - 120);
            groupBox5.Location = new Point(x_st + dx * 1, y_st + dy * 2 - 120);
            groupBox6.Location = new Point(x_st + dx * 2, y_st + dy * 2 - 160);

            //ClientSize = new Size(bt_exit.Right + 10, richTextBox1.Bottom + 80);    //自動表單邊界

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

        // Force all threads to end.
        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            Environment.Exit(0);
        }

        #region epitrochoid長短輻圓外旋輪線；外旋輪線



        // Draw the epitrochoid.
        private void pictureBox0_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            e.Graphics.Clear(pictureBox0.BackColor);

            // Scale and center.
            float scale = Math.Min(
                pictureBox0.ClientSize.Width * 0.45f,
                pictureBox0.ClientSize.Height * 0.45f);
            e.Graphics.ScaleTransform(scale, scale);
            e.Graphics.TranslateTransform(
                pictureBox0.ClientSize.Width / 2,
                pictureBox0.ClientSize.Height / 2,
                System.Drawing.Drawing2D.MatrixOrder.Append);

            // Draw the curve.
            float a = float.Parse(txtA.Text);
            float b = float.Parse(txtB.Text);
            float h = float.Parse(txtH.Text);
            float dt = float.Parse(txtDt.Text);
            DrawEpitrochoid(e.Graphics, a, b, h, dt);
        }

        // Draw the curve on the indicated Graphics object.
        private void DrawEpitrochoid(Graphics gr, float a, float b, float h, float dt)
        {
            // Calculate the stop value for t.
            float stop_t = (float)(b * 2 * Math.PI);

            // Find the points.
            using (Pen the_pen = new Pen(Color.White, 0))
            {
                PointF pt0, pt1;
                pt0 = new PointF(X1(a, b, h, 0), Y1(a, b, h, 0));
                for (float t = dt; t <= stop_t; t += dt)
                {
                    pt1 = new PointF(X1(a, b, h, t), Y1(a, b, h, t));
                    gr.DrawLine(the_pen, pt0, pt1);
                    pt0 = pt1;
                }
            }
        }

        // The parametric function X(t).
        private float X1(float a, float b, float h, float t)
        {
            float value = (float)((a + b) * Math.Cos(t) - h * Math.Cos(t * (a + b) / b));
            return value / (a + b + h);
        }

        // The parametric function Y(t).
        private float Y1(float a, float b, float h, float t)
        {
            float value = (float)((a + b) * Math.Sin(t) - h * Math.Sin(t * (a + b) / b));
            return value / (a + b + h);
        }

        // The curve's parameters.
        private float a, b, h, dt;

        // The curve's points.
        private PointF[] Points = null;
        private float[] Thetas = null;

        // The maximum index we should draw.
        private int MaxPointToDraw = 0;

        private void button2_Click(object sender, EventArgs e)
        {
            // Redraw.
            pictureBox0.Invalidate();

            if (timer_epitrochoid.Enabled)
            {
                Cursor = Cursors.Default;
                timer_epitrochoid.Enabled = false;
            }
            else
            {
                Cursor = Cursors.WaitCursor;

                // Make the points.
                a = float.Parse(txtA.Text);
                b = float.Parse(txtB.Text);
                h = float.Parse(txtH.Text);
                dt = float.Parse(txtDt.Text);
                MakeEpitrochoidPoints(a, b, h, dt);

                // Start drawing.
                MaxPointToDraw = 0;
                timer_epitrochoid.Enabled = true;
            }
        }

        // Draw the epitrochoid.
        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(pictureBox1.BackColor);
            if (Points == null) return;

            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Scale and center.
            float scale = Math.Min(
                pictureBox1.ClientSize.Width * 0.45f,
                pictureBox1.ClientSize.Height * 0.45f);
            e.Graphics.ScaleTransform(scale / (a + b + h), scale / (a + b + h));
            e.Graphics.TranslateTransform(
                pictureBox1.ClientSize.Width / 2,
                pictureBox1.ClientSize.Height / 2,
                MatrixOrder.Append);

            // Draw the circles.
            using (Pen black_pen = new Pen(Color.Black, 0))
            {
                // Inner circle.
                e.Graphics.DrawEllipse(black_pen, -a, -a, 2 * a, 2 * a);

                // Outer circle.
                float theta = Thetas[MaxPointToDraw];
                float cx = (float)((a + b) * Math.Cos(theta));
                float cy = (float)((a + b) * Math.Sin(theta));

                e.Graphics.DrawEllipse(black_pen, cx - b, cy - b, 2 * b, 2 * b);

                // The line segment.
                e.Graphics.DrawLine(black_pen, cx, cy, Points[MaxPointToDraw].X, Points[MaxPointToDraw].Y);
            }

            // Draw the curve.
            using (Pen white_pen = new Pen(Color.White, 0))
            {
                for (int i = 0; i < MaxPointToDraw; i++)
                {
                    e.Graphics.DrawLine(white_pen, Points[i], Points[i + 1]);
                }
            }
        }

        // Make the curve's points.
        private void MakeEpitrochoidPoints(float a, float b, float h, float dt)
        {
            // Calculate the stop value for t.
            float stop_t = (float)(b * 2 * Math.PI);

            // Find the points.
            List<PointF> point_list = new List<PointF>();
            List<float> theta_list = new List<float>();

            point_list.Add(new PointF(X2(a, b, h, 0), Y2(a, b, h, 0)));
            theta_list.Add(0);
            for (float t = dt; t <= stop_t; t += dt)
            {
                point_list.Add(new PointF(X2(a, b, h, t), Y2(a, b, h, t)));
                theta_list.Add(t);
            }
            point_list.Add(new PointF(X2(a, b, h, 0), Y2(a, b, h, 0)));
            theta_list.Add(0);

            Points = point_list.ToArray();
            Thetas = theta_list.ToArray();
        }

        // The parametric function X(t).
        private float X2(float a, float b, float h, float t)
        {
            return (float)((a + b) * Math.Cos(t) - h * Math.Cos(t * (a + b) / b));
        }

        // The parametric function Y(t).
        private float Y2(float a, float b, float h, float t)
        {
            return (float)((a + b) * Math.Sin(t) - h * Math.Sin(t * (a + b) / b));
        }

        // Draw another point.
        private void timer_epitrochoid_Tick(object sender, EventArgs e)
        {
            MaxPointToDraw++;
            if (MaxPointToDraw >= Points.Length - 1)
            {
                timer_epitrochoid.Enabled = false;
                Cursor = Cursors.Default;
            }
            pictureBox1.Refresh();
        }

        #endregion epitrochoid長短輻圓外旋輪線；外旋輪線


        private void tmrDraw_Tick(object sender, EventArgs e)
        {

        }






    }
}
