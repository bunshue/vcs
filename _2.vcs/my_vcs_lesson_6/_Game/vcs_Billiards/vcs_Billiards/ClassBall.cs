using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing;
using System.Diagnostics;

namespace vcs_Billiards
{
    class ClassBall
    {
        public PointF position; // 球的位置
        public PointF velocity; // 球的速度
        public Size clientSize; // 視窗寬高
        public int Ball_Width = 10; // 球的半徑
        SolidBrush myBrush = new SolidBrush(Color.Blue); // 球的顏色
        public Stopwatch sw = new Stopwatch(); // 碼表
        public float Mass = 1.0f; // 球的質量

        public PointF position_Last; // 球的上一個位置 碰撞時要能夠回朔
        public bool Dead = false; // 球是否已經入袋

        public ClassBall(PointF position, 
                         PointF velocity, 
                         Size clientSize, 
                         int Ball_Width,
                         Color color)
        {
            this.position = this.position_Last = position; // 球的位置
            this.velocity = velocity; // 球的速度
            this.clientSize = clientSize; // 視窗寬高
            this.Ball_Width = Ball_Width; // 球的半徑
            myBrush.Color = color;
        }

        // 繪出球體
        public void Draw(Graphics G)
        {
            G.FillEllipse(myBrush, (int)(position.X - Ball_Width), (int)(position.Y - Ball_Width), Ball_Width * 2, Ball_Width * 2);
            G.DrawEllipse(Pens.Black, (int)(position.X - Ball_Width), (int)(position.Y - Ball_Width), Ball_Width * 2, Ball_Width * 2);
        }

        // 回朔 因為 球球之間有穿透的狀況
        public void Move_Back()
        {
            position.X = (position_Last.X + position.X) / 2.0f;
            position.Y = (position_Last.Y + position.Y) / 2.0f;
            sw.Reset(); // 碼表歸零
            sw.Start(); // 碼表開始計時
        }

        // 往前更新
        public void Move()
        {
            position_Last = position;

            velocity.X *= 0.99f; // 摩擦力
            velocity.Y *= 0.99f;

            long et = sw.ElapsedMilliseconds;
            position.X += velocity.X * et * 0.1f;
            position.Y += velocity.Y * et * 0.1f;
            sw.Reset(); // 碼表歸零
            sw.Start(); // 碼表開始計時

            //  右邊界
            if (position.X > clientSize.Width - Ball_Width)
            {
                velocity.X = -velocity.X;
                position.X = clientSize.Width - Ball_Width;
            }
            //  下邊界
            if (position.Y > clientSize.Height - Ball_Width)
            {
                velocity.Y = -velocity.Y;
                position.Y = clientSize.Height - Ball_Width;
            }
            //  左邊界
            if (position.X < Ball_Width)
            {
                velocity.X = -velocity.X;
                position.X = Ball_Width;
            }

            //  上邊界
            if (position.Y < Ball_Width)
            {
                velocity.Y = -velocity.Y;
                position.Y = Ball_Width;
            }
        }
    }
}
