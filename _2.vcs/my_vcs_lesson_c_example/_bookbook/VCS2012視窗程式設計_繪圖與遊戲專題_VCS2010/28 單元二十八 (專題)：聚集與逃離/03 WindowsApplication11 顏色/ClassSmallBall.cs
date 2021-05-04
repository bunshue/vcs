using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing;

namespace WindowsApplication11
{
    class ClassSmallBall
    {
        PointF pos = new PointF(); 
        Random rd;  // 變數
        int ClientWidth, ClientHeight; // 活動的寬高
        Color color;

        public ClassSmallBall(int ClientWidth, int ClientHeight, int seed)
        {
            rd = new Random(seed);
            pos.X = rd.Next(ClientWidth);
            pos.Y = rd.Next(ClientHeight);
            this.ClientWidth = ClientWidth;
            this.ClientHeight = ClientHeight;
            if (rd.NextDouble() < 0.3) color = Color.Red;
            else if (rd.NextDouble() < 0.6) color = Color.Green;
            else color = Color.Blue;
        }

        public void Update(PointF BigBall)
        {
            double X, Y; // 小球 新的座標
            double D;    // 小球 和 大球 的距離
            double Dx, Dy; // 小球 新的座標 和 大球 的距離

            D = Math.Sqrt(
                    (pos.X - BigBall.X) * (pos.X - BigBall.X) +
                    (pos.Y - BigBall.Y) * (pos.Y - BigBall.Y));

            if (D < 50) // 距離 50 以內 快速逃離
            {
                Dx = (pos.X - BigBall.X) * (D + 10) / D; // 逃離速度 10 單位
                X = BigBall.X + Dx;
                X = X + rd.Next(11) - 5; // 還是要擺動

                Dy = (pos.Y - BigBall.Y) * (D + 10) / D;
                Y = BigBall.Y + Dy;
                Y = Y + rd.Next(11) - 5;

                pos = new Point((int)X, (int)Y);
            }
            else // 距離 50 以上  不受影響(漫遊)
            {
                // 在邊界內漫遊
                X = pos.X + rd.Next(11) - 5;  // -5 ~ 5 之間變動
                if (X > ClientWidth) X = ClientWidth;
                else if (X < 0) X = 0;

                Y = pos.Y + rd.Next(11) - 5;
                if (Y > ClientHeight) Y = ClientHeight;
                else if (Y < 0) Y = 0;

                pos = new Point((int)X, (int)Y);
            }
        }
        public void Draw(Graphics G)
        {
            //G.FillEllipse(Brushes.Black, pos.X - 5, pos.Y - 5, 10, 10);
            G.FillEllipse(new SolidBrush(color), pos.X - 5, pos.Y - 5, 10, 10);
        }
    }
}
