/* 作者：鄞永傳老師‧xnabook@yahoo.com.tw‧2009-09 */
using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing;

namespace WindowsFormsApplication1
{
    class BallInACircle  // 在一個圓形中的球
    {
        public PointF position; // 球的位置
        public PointF velocity; // 球的速度
        public RectangleF CircleRect; // 邊界圓形的矩形區域
        PointF CircleCenter;  // 邊界圓形的 中心點
        float CircleD;        // 邊界圓形的 半徑
        public int Ball_Width = 10; // 球的半徑
        Random rd = new Random();

        public BallInACircle(PointF position, 
                         PointF velocity,
                         RectangleF CircleRect, 
                         int Ball_Width,
                         Color color)
        {
            this.position = position; // 球的位置
            this.velocity = velocity; // 球的速度
            this.CircleRect = CircleRect; // 視窗寬高
            this.Ball_Width = Ball_Width; // 球的半徑

            CircleCenter = new PointF(CircleRect.X + CircleRect.Width / 2,
                CircleRect.Y + CircleRect.Height / 2);  // 邊界圓形的 中心點
            CircleD = CircleRect.Width / 2.0f;  // 邊界圓形的 半徑
        }

        // 繪出 邊界圓形
        public void DrawCircle(Graphics G, Color color)
        {
            Pen myPen = new Pen(color);
            G.DrawEllipse(myPen, CircleRect);
        }

        // 繪出 球體
        public void Draw(Graphics G, Color color)
        {
            SolidBrush myBrush = new SolidBrush(color);  // 球內部的顏色

            G.FillEllipse(myBrush, position.X - Ball_Width, position.Y - Ball_Width, Ball_Width * 2, Ball_Width * 2);
            G.DrawEllipse(Pens.Black, position.X - Ball_Width, position.Y - Ball_Width, Ball_Width * 2, Ball_Width * 2);
        }

        // 更新 小球 的位置
        public void Update()
        {
            PointF LastPos = position;  // 暫存 小球 的位置

            position.X += velocity.X; // 更新 小球 的位置
            position.Y += velocity.Y;

            // 小球 離 邊界圓形中心點 的 位置
            double dis = Math.Sqrt(
                (position.X - CircleCenter.X) * (position.X - CircleCenter.X) +
                (position.Y - CircleCenter.Y) * (position.Y - CircleCenter.Y));

            // 如果 小球已經出界了
            if (dis > CircleD - Ball_Width)
            {
                // 由 邊界圓形中心點、小球出界的位置、小球未出界前的位置 計算出 小球下一步的位置
                double D = 0; // 距離 D 
                PointF H = new PointF(); // 交叉點 H 
                PointF q2 = new PointF();// 對側點 q2
                G2D_PointAndLine.PointToLine(CircleCenter, position, LastPos, ref D, ref H, ref q2);

                // 由 小球出界的位置、小球下一步的位置 計算出 新的速度
                velocity.X = q2.X - position.X;
                velocity.Y = q2.Y - position.Y;

                // 再次確定 小球 新的位置是在 邊界圓形 內
                dis = Math.Sqrt((q2.X - CircleCenter.X) * (q2.X - CircleCenter.X) +
                                (q2.Y - CircleCenter.Y) * (q2.Y - CircleCenter.Y));
                if (dis < CircleD - Ball_Width) // 在 邊界圓形 內
                    position = q2;              // 小球新的位置
                else  // 不在 邊界圓形 內 => 就硬拉回 邊界圓形 內
                {
                    PointF N = G2D_PointAndLine.VectorNormalize(CircleCenter, q2);
                    position.X = CircleCenter.X + N.X * (CircleD - Ball_Width);
                    position.Y = CircleCenter.Y + N.Y * (CircleD - Ball_Width);
                }
            }

            // 再次確定 小球 不會因此而停下來
            if (velocity.X == 0 && velocity.Y == 0)
            {
                velocity.X = rd.Next(3) - 1;
                velocity.Y = rd.Next(3) - 1;
            }
        }
    }
}
