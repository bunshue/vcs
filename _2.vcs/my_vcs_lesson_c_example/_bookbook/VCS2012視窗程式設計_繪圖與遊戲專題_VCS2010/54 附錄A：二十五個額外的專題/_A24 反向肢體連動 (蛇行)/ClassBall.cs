/* 作者：鄞永傳老師‧xnabook@yahoo.com.tw‧2009-09 */
using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing;

namespace WindowsApplication1
{
    class ClassBall
    {
        public Point position; // 球的位置
        public Point velocity; // 球的速度
        public Size clientSize; // 視窗寬高
        public int Ball_Width = 10; // 球的半徑
        SolidBrush myBrush = new SolidBrush(Color.Blue);

        public ClassBall(Point position, 
                         Point velocity, 
                         Size clientSize, 
                         int Ball_Width,
                         Color color)
        {
            this.position = position; // 球的位置
            this.velocity = velocity; // 球的速度
            this.clientSize = clientSize; // 視窗寬高
            this.Ball_Width = Ball_Width;
            myBrush.Color = color;
        }

        public void Draw(Graphics G)
        {
            G.FillEllipse(myBrush, position.X - Ball_Width, position.Y - Ball_Width, Ball_Width * 2, Ball_Width * 2);
            G.DrawEllipse(Pens.Black, position.X - Ball_Width, position.Y - Ball_Width, Ball_Width * 2, Ball_Width * 2);
        }

        public void Move()
        {
            position.X += velocity.X;
            position.Y += velocity.Y;
            //  右邊界
            if (position.X > clientSize.Width - Ball_Width)
            {
                velocity.X = -velocity.X;
                position.X = clientSize.Width - Ball_Width;
            }
            //  下邊界
            else if (position.Y > clientSize.Height - Ball_Width)
            {
                velocity.Y = -velocity.Y;
                position.Y = clientSize.Height - Ball_Width;
            }
            //  左邊界
            else if (position.X < Ball_Width)
            {
                velocity.X = -velocity.X;
                position.X = Ball_Width;
            }

            //  上邊界
            else if (position.Y < Ball_Width)
            {
                velocity.Y = -velocity.Y;
                position.Y = Ball_Width;
            }
        }
    }
}
