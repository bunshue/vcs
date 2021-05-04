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
        BallInACircle ball; // 一個在圓形中的小球
        Rectangle CircleRect; // 邊界圓形的矩形區域
        List<BallInACircle> balls = new List<BallInACircle>(); // 動態陣列 儲存多顆球
        Random rd = new Random();

        public Form1()
        {
            InitializeComponent();

            // 設定 邊界圓形的位置與寬高
            CircleRect = new Rectangle(20, 20, 400, 400);

            int D = 10; // 球的半徑
            int Cx = CircleRect.Width / 2 + CircleRect.X;
            int Cy = CircleRect.Height / 2 + CircleRect.Y;
            int Cd = CircleRect.Width / 3;
            float x, y;
            double theta = 0;
            // 新增 10 個圓中球 物件
            for (int i = 0; i < 10; i++)
            {
                x = (int)(Cx + Cd * Math.Cos(theta));
                y = (int)(Cy + Cd * Math.Sin(theta));
                ball = new BallInACircle(
                             new PointF(x, y),
                             new PointF(rd.Next(5)+1, rd.Next(6) +1),
                             CircleRect,
                             D,
                             Color.Red);
                balls.Add(ball);
                theta = theta + Math.PI * 2 / 10;
            }

            // 調整 視窗的寬高
            this.ClientSize = new Size(CircleRect.Width + CircleRect.X * 2,
                                       CircleRect.Height + CircleRect.Y * 2);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            // 反鋸齒設定 ==> 比較好的輸出品質
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            // 輔助線條
            e.Graphics.DrawLine(Pens.Silver, CircleRect.X, CircleRect.Y + CircleRect.Height / 2,
                CircleRect.X + CircleRect.Width, CircleRect.Y + CircleRect.Height / 2);

            e.Graphics.DrawLine(Pens.Silver, CircleRect.X + CircleRect.Width / 2, CircleRect.Y,
                CircleRect.X + CircleRect.Width / 2, CircleRect.Y + CircleRect.Height);

            ball.DrawCircle(e.Graphics, Color.Blue); // 繪出 邊界圓形
            // 繪出 全部的圓中球
            for (int i = 0; i < balls.Count; i++)
                balls[i].Draw(e.Graphics, Color.Red);
        }

        // 計時器 事件處理函數
        private void timer1_Tick(object sender, EventArgs e)
        {
            // 更新 全部小球 的位置
            for (int i = 0; i < balls.Count; i++)
                balls[i].Update();

            // 小球 的碰撞處理
            for (int i = 0; i < balls.Count - 1; i++)
                for (int j = i + 1; j < balls.Count; j++)
                {
                    if (Collides(balls[i], balls[j]))
                    {
                        MovingBack(balls[i], balls[j]);
                        Swap(balls[i], balls[j]);
                    }
                }

            this.Invalidate();
        }

        // 碰撞測試
        bool Collides(BallInACircle A, BallInACircle B)
        {
            Double D = Math.Sqrt(
            (A.position.X - B.position.X) * (A.position.X - B.position.X) +
            (A.position.Y - B.position.Y) * (A.position.Y - B.position.Y));

            if (D <= A.Ball_Width + B.Ball_Width)
                return true;
            else
                return false;
        }

        // 速度交換 
        void Swap(BallInACircle A, BallInACircle B)
        {
            PointF temp = A.velocity;
            A.velocity = B.velocity;
            B.velocity = temp;
        }

        // 有碰撞 各自後退一步
        void MovingBack(BallInACircle A, BallInACircle B)
        {
            A.position.X = A.position.X - A.velocity.X;
            A.position.Y = A.position.Y - A.velocity.Y;

            B.position.X = B.position.X - B.velocity.X;
            B.position.Y = B.position.Y - B.velocity.Y;
        }
    }
}
