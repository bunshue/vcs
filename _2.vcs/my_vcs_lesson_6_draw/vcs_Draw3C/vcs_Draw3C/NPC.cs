using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing;

namespace vcs_Draw3C
{
    class NPC
    {
        public int X, Y;      // 圖形目前的位置
        public double Angle;  // 圖形目前的旋轉角度
        double OffsetAngle;  // 圖形的角度偏移値 向右是零度
        float Speed = 10;     // 蝴蝶的行進速度

        Image image;         // 圖形 
        Rectangle Boundary;  // 視窗邊界
        Point Target = new Point(); // 追蹤點 的座標

        public NPC(Bitmap b) // 建構元
        {
            image = new Bitmap(b);
        }

        // 設定開始的座標
        public void SetLocation(int x, int y)
        {
            X = x;
            Y = y;
        }

        // 設定開始的角度 和 圖形本身的偏移角度
        public void SetAngle(double a, double o)
        {
            Angle = a;
            OffsetAngle = o;
        }

        // 改變角度
        public void Turn(double a)
        {
            Angle = Angle + a;
        }

        // 改變速度
        public void ChangeSpeed(float a)
        {
           Speed = Speed + a;
           if (Speed < 0) Speed = 0;
        }

        // 更新 追蹤點的座標
        public void Update(Point Target)
        {
            this.Target = Target;

            // 更新 圖形的旋轉角度
            double A ;
            // 如果 圖形的座標 和 追蹤點的座標 不在同一個鉛錘線上
            if (Target.X != X) 
            {
                // 算出兩個座標的夾角徑度
                A = Math.Atan((double)(Target.Y - Y) / (Target.X - X));
                // 如果圖形的座標 在左側
                if (Target.X < X)
                {
                    if (Target.Y <= Y)  // 追蹤點的座標 在上方
                        A = A - Math.PI;
                    else                // 追蹤點的座標 在下方
                        A = A + Math.PI;
                }
                A = A * 180 / Math.PI; // 將夾角徑度 轉換成 角度
            }
            else // 如果 兩個座標 在同一個鉛錘線上
            {
                if (Target.Y > Y) A = 90; // 如果圖形的座標 在上方
                else A = -90; // 如果圖形的座標 在下方
            }

            Angle = A; 
        }

        public void Draw(Graphics G)
        {
            G.ResetTransform();

            // 根據 目前的速度 和 夾角徑度 算出 圖形的下一步位置
            X = X + (int)(Speed * Math.Cos(Angle * Math.PI / 180.0));
            Y = Y + (int)(Speed * Math.Sin(Angle * Math.PI / 180.0));

            // 邊界碰撞 測試
            if (X < (Boundary.Left + image.Width / 2))
            {
                X = Boundary.Left + image.Width / 2;
            }
            if (X > (Boundary.Right - image.Width / 2))
            {
                X = Boundary.Right - image.Width / 2;
            }
            if (Y < (Boundary.Top + image.Height / 2))
            {
                Y = Boundary.Top + image.Height / 2;
            }
            if (Y > (Boundary.Bottom - image.Height / 2))
            {
                Y = Boundary.Bottom - image.Height / 2;
            }

            // 根據 夾角徑度 轉動圖形的方向
            G.TranslateTransform(X, Y);
            G.RotateTransform((float)(Angle - OffsetAngle));

            // 繪出圖形
            G.DrawImage(image, -image.Width/2, -image.Height/2, image.Width, image.Height);
        }

        // 設定邊界
        public void SetBoundary(Rectangle r)
        {
            Boundary = r;
        }
    }
}
