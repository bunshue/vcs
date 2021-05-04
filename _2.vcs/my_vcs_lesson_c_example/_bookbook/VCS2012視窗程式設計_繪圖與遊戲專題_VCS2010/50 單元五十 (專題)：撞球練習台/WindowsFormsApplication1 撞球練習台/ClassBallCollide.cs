/* 作者：鄞永傳老師‧xnabook@yahoo.com.tw‧2009-09 */
using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing;

namespace WindowsFormsApplication1
{
    class ClassBallCollide
    {
        ClassBall ball1, ball2;
        PointF collisionNormal = new Point(); // 碰撞的法向量
        PointF relativeVelocity = new Point(); // 碰撞的相對速度
        float collisionDot; // collisionNormal 和 relativeVelocity 的內積
        float penetrateT = 2.0f; // 球球穿透容忍度

        public ClassBallCollide(ClassBall ball1, ClassBall ball2)
        {
            this.ball1 = ball1;
            this.ball2 = ball2;
        }

        public void performBallCollide()
        {
            ball1.Move();
            ball2.Move();

            int ret = Collides(ball1, ball2);
            if (ret == 1) Impulse(ball1, ball2); // 球球碰撞
            else if (ret == -1) // 球球之間有穿透的狀況
            {
                while (ret == -1)
                {
                    ball1.Move_Back(); // 回朔 一半 的位置
                    ball2.Move_Back();
                    ret = Collides(ball1, ball2);
                }
                Impulse(ball1, ball2);
            }
        }

        // 測試球球是否 碰撞 或 穿透
        int Collides(ClassBall A, ClassBall B)
        {

            PointF BA = new PointF(); // B -> A 的向量
            BA.X = A.position.X - B.position.X;
            BA.Y = A.position.Y - B.position.Y;
            Double len = Math.Sqrt(BA.X * BA.X + BA.Y * BA.Y); // B -> A 向量的長度

            int D2 = A.Ball_Width + B.Ball_Width;  // A 的半徑 +  B 的半徑
            Double overlap = len - D2; // A B 的穿透值 (有穿透 為 負值)

            //PointF collisionNormal = new Point(); // 碰撞的法向量
            collisionNormal.X = (float)(BA.X / len);
            collisionNormal.Y = (float)(BA.Y / len);

            //PointF relativeVelocity = new Point(); // 碰撞的相對速度
            relativeVelocity.X = A.velocity.X - B.velocity.X;
            relativeVelocity.Y = A.velocity.Y - B.velocity.Y;

            //float collisionDot; // collisionNormal 和 relativeVelocity 的內積
            collisionDot = collisionNormal.X * relativeVelocity.X +
                           collisionNormal.Y * relativeVelocity.Y;

            if (Math.Abs(overlap) <= penetrateT && collisionDot < 0.0) // 稍微穿透 而且角度 小於 90 度
                return 1;  // 碰撞發生中  1.0 是穿透容許值
            else if (overlap < -penetrateT) // 穿透中
                return -1;
            else
                return 0; // 無碰撞
        }

        void Impulse(ClassBall A, ClassBall B) // 碰撞 算出 各自的速度
        {
            float CN = collisionNormal.X * collisionNormal.X +
                           collisionNormal.Y * collisionNormal.Y;

            float k;
            k = (-(1 + 0.5f) * collisionDot) /  // 0.5 是恢復係數
                (CN * ((1.0f / A.Mass) + (1.0f / B.Mass)));

            A.velocity.X += k * collisionNormal.X / A.Mass;
            A.velocity.Y += k * collisionNormal.Y / A.Mass;

            B.velocity.X -= k * collisionNormal.X / B.Mass;
            B.velocity.Y -= k * collisionNormal.Y / B.Mass;
        }
    }
}
