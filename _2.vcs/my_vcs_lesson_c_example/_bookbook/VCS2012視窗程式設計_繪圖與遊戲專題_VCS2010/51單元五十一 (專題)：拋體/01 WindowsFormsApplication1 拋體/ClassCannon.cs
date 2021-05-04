/* 作者：鄞永傳老師‧xnabook@yahoo.com.tw‧2010-06 */
using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing;

namespace WindowsFormsApplication1
{
    class ClassCannon
    {
        public double v0;         // 起初的速度
        public double vx, vy; // 現在的速度分量

        public double theta;      // 發射的仰角角度
        public int x0, y0; // 起初的位置
        public int x, y;   // 現在的位置
        
        public double v; // 現在的速度
        public double h; // 拋射的最大高度
        public double R; // 拋射距離
        public double T; // 拋體在空中停留的時間
        double g = 9.8;  // 重力加速度 m / (s * s)

        DateTime dt; // 紀錄開始的時間

        public ClassCannon(int x0, int y0, double v0, double theta)
        {
            this.x0 = x0;
            this.y0 = y0;

            this.v0 = v0;
            this.theta = theta;

            vx = v0 * Math.Cos(theta);
            h = (v0 * v0 * Math.Sin(theta) * Math.Sin(theta) / 2 * g) * 0.1 * 0.1;
            T = (-2 * v0 * Math.Sin(theta) / g) * 0.1; // 時間單位是 0.1 秒
            R = v0 * (-2 * v0 * Math.Sin(theta) / g) * Math.Cos(theta);

            dt = DateTime.Now;
        }

       public void Draw(Graphics G)
       {
           TimeSpan ts = DateTime.Now - dt;
           double t = ts.TotalMilliseconds * 0.01;  // 時間單位是 0.1 秒

           x = x0 + (int)(v0 * Math.Cos(theta) * t);
           y = y0 + (int)(v0 * Math.Sin(theta) * t + g * t * t / 2); // -g * t * t / 2

           vy = v0 * Math.Sin(theta) + g * t; // - g * t // 因為時間單位是 0.1 秒
           v = Math.Sqrt(vx * vx + vy * vy);

           G.FillEllipse(Brushes.Green, x - 20, y - 20, 40, 40);
           G.DrawEllipse(Pens.Black, x - 20, y - 20, 40, 40);
       }
    }
}
