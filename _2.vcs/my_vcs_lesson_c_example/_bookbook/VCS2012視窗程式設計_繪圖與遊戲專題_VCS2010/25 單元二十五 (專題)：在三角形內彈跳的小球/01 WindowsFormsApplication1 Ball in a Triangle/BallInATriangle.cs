/* 作者：鄞永傳老師‧xnabook@yahoo.com.tw‧2009-09 */
using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing;

namespace WindowsFormsApplication1
{
    class BallInATriangle  // 在一個三角形內部彈跳的小球
    {
        public PointF position; // 球的位置
        public PointF velocity; // 球的速度 (注意：每一次的更新 速度是要加三次)
        public int Ball_Width = 10; // 球的半徑
        SolidBrush myBrush = new SolidBrush(Color.Blue);

        public BallInATriangle(PointF position, 
                         PointF velocity,
                         int Ball_Width,
                         Color color)
                         //PointF p1, PointF p2, PointF p3)
        {
            this.position = position; // 球的位置
            this.velocity = velocity; // 球的速度
            this.Ball_Width = Ball_Width;  // 球的半徑
            myBrush.Color = color;  // 球的顏色
        }

        // 繪出小球
        public void Draw(Graphics G)
        {
            G.FillEllipse(myBrush, position.X - Ball_Width, position.Y - Ball_Width, Ball_Width * 2, Ball_Width * 2);
            G.DrawEllipse(Pens.Black, position.X - Ball_Width, position.Y - Ball_Width, Ball_Width * 2, Ball_Width * 2);
        }

        // 更新小球的座標 
        // 輸入三角形的座標點 p1, p2, p3 是要做 碰撞測試
        public void Update(PointF p1, PointF p2, PointF p3)
        {
             bool ret = G2D_PointAndLine.IsPointInTriangle(p1, p2, p3, position);
             if (ret == false) return; // 如果小球不在三角形內 就不更新了
             else
             {
                 LineTestAndBallUpdate(p1, p2);
                 LineTestAndBallUpdate(p2, p3);
                 LineTestAndBallUpdate(p1, p3);
             }
        }

        // 小球根據p1 p2 直線，測試碰撞 並且 更新座標 
        void LineTestAndBallUpdate(PointF p1, PointF p2)
        {
            PointF LastPos = position; // 暫存 小球 的位置

            position.X += velocity.X; // 小球 的新位置
            position.Y += velocity.Y;

            double D = 0; // 距離 D 
            PointF H = new PointF(); // 交叉點 H 
            PointF q2 = new PointF();// 對側點 q2
            PointF H2 = new PointF(); // 交叉點 H2 

            // 根據p1 p2 直線、測試小球和 p1 p2 直線的垂直距離 垂直點座標 與 對稱點座標
            G2D_PointAndLine.PointToLine(p1, p2, position, ref D, ref H, ref q2);

            // 如果 垂直距離 小於小球的半徑 就是新位置碰到了 p1 p2 直線
            if (D < Ball_Width)
            {
                // 再求一次 設法得到 小球舊位置 相對於 p1 p2 的垂直線 的 對稱點座標
                G2D_PointAndLine.PointToLine(position, H, LastPos, ref D, ref H2, ref q2);

                velocity.X = q2.X - position.X; // 小球新的速度
                velocity.Y = q2.Y - position.Y;
                position = q2; // 以 對稱點座標 當作 小球的 下一個位置
            }
        }
    }
}
