using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        List<Point> R = new List<Point>(); // 紀錄 多顆小球座標的動態陣列
        const int smallBallCount = 500;
        Point Mouse = new Point(); // 滑鼠的座標
        PointF BigBall = new Point(); // 大球的座標
        Random rd = new Random();  // 亂數

        public Form1()
        {
            InitializeComponent();

            int X, Y;
            for (int i = 0; i < smallBallCount; i++)  // 初始化 200 顆小球
            {
                X = rd.Next(this.pictureBox1.ClientSize.Width);
                Y = rd.Next(this.pictureBox1.ClientSize.Height);
                R.Add(new Point(X, Y));
            }
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            /*
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            // 繪出大球
            e.Graphics.FillEllipse(Brushes.Black, (int)(BigBall.X - 15), (int)(BigBall.Y - 15), 30, 30);

            // 繪出小球
            for (int i = 0; i <= R.Count - 1; i++)
            {
                e.Graphics.FillEllipse(Brushes.Silver, R[i].X - 5, R[i].Y - 5, 10, 10);
            }
            */
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            /*
            // 紀錄滑鼠的座標
            Mouse.X = e.X;
            Mouse.Y = e.Y;
            */
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            // 讓大球 逐漸 逼近 滑鼠的座標
            BigBall.X = BigBall.X + (Mouse.X - BigBall.X) / 10;
            if (Math.Abs(Mouse.X - BigBall.X) < 1) BigBall.X = Mouse.X;

            BigBall.Y = BigBall.Y + (Mouse.Y - BigBall.Y) / 10;
            if (Math.Abs(Mouse.Y - BigBall.Y) < 1) BigBall.Y = Mouse.Y;

            double X, Y; // 小球 新的座標
            double D;    // 小球 和 大球 的距離
            double Dx, Dy; // 小球 新的座標 和 大球 的距離

            // 更新 小球的座標
            for (int i = 0; i <= R.Count - 1; i++)
            {
                D = Math.Sqrt(
                    (R[i].X - BigBall.X) * (R[i].X - BigBall.X) +
                    (R[i].Y - BigBall.Y) * (R[i].Y - BigBall.Y));

                if (D < 50) // 距離 50 以內 快速逃離
                {
                    Dx = (R[i].X - BigBall.X) * (D + 10) / D; // 逃離速度 10 單位
                    X = BigBall.X + Dx;
                    X = X + rd.Next(11) - 5; // 還是要擺動

                    Dy = (R[i].Y - BigBall.Y) * (D + 10) / D;
                    Y = BigBall.Y + Dy;
                    Y = Y + rd.Next(11) - 5;

                    R[i] = new Point((int)X, (int)Y);
                }
                else // 距離 50 以上  不受影響(漫遊)
                {
                    // 在邊界內漫遊
                    X = R[i].X + rd.Next(11) - 5;  // -5 ~ 5 之間變動
                    if (X > this.pictureBox1.ClientSize.Width)
                    {
                        X = this.pictureBox1.ClientSize.Width;
                    }
                    else if (X < 0)
                    {
                        X = 0;
                    }

                    Y = R[i].Y + rd.Next(11) - 5;
                    if (Y > this.pictureBox1.ClientSize.Height)
                    {
                        Y = this.pictureBox1.ClientSize.Height;
                    }
                    else if (Y < 0)
                    {
                        Y = 0;
                    }

                    R[i] = new Point((int)X, (int)Y);
                }
            }
            this.pictureBox1.Invalidate();
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            // 繪出大球
            e.Graphics.FillEllipse(Brushes.Black, (int)(BigBall.X - 15), (int)(BigBall.Y - 15), 30, 30);

            // 繪出小球
            for (int i = 0; i <= R.Count - 1; i++)
            {
                e.Graphics.FillEllipse(Brushes.Silver, R[i].X - 5, R[i].Y - 5, 10, 10);
            }

        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            // 紀錄滑鼠的座標
            Mouse.X = e.X;
            Mouse.Y = e.Y;

        }
    }
}