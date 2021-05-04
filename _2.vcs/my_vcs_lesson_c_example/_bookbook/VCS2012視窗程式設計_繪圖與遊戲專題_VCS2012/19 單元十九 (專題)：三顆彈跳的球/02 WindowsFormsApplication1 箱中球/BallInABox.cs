/* 作者：鄞永傳老師‧xnabook@yahoo.com.tw‧2009-09 */
using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing;

namespace WindowsFormsApplication1
{
    class BallInABox  // 在一個矩形中的球
    {
        public PointF position; // 球的位置
        public PointF velocity; // 球的速度
        public Rectangle rect; // 箱子的矩形
        public int Ball_Width = 10; // 球的半徑

        public BallInABox(PointF position, 
                          PointF velocity,
                          Rectangle rect, 
                          int Ball_Width)
        {
            this.position = position; // 球的位置
            this.velocity = velocity; // 球的速度
            this.rect = rect; // 視窗寬高
            this.Ball_Width = Ball_Width;
        }

        // 繪出 箱子的矩形
        public void DrawBox(Graphics G, Color color)
        {
            Pen myPen = new Pen(color); // 箱子外框的顏色
            G.DrawRectangle(myPen, rect);
        }

        // 繪出 球的內部顏色和外框
        public void Draw(Graphics G, Color color)
        {
            SolidBrush myBrush = new SolidBrush(color);  // 球內部的顏色
            G.FillEllipse(myBrush, position.X - Ball_Width, position.Y - Ball_Width, Ball_Width * 2, Ball_Width * 2);
            G.DrawEllipse(Pens.Black, position.X - Ball_Width, position.Y - Ball_Width, Ball_Width * 2, Ball_Width * 2);
        }

        // 更新 球的 位置
        public void Update()
        {
            position.X += velocity.X;
            position.Y += velocity.Y;
            //  右邊界
            if (position.X > rect.X + rect.Width - Ball_Width)
            {
                velocity.X = -velocity.X;
                position.X = rect.X + rect.Width - Ball_Width;
            }
            //  左邊界
            else if (position.X < rect.X + Ball_Width)
            {
                velocity.X = -velocity.X;
                position.X = rect.X + Ball_Width;
            }

            //  下邊界
            if (position.Y > rect.Y + rect.Height - Ball_Width)
            {
                velocity.Y = -velocity.Y;
                position.Y = rect.Y + rect.Height - Ball_Width;
            }
            //  上邊界
            else if (position.Y < rect.Y + Ball_Width)
            {
                velocity.Y = -velocity.Y;
                position.Y = rect.Y + Ball_Width;
            }
        }
    }
}
