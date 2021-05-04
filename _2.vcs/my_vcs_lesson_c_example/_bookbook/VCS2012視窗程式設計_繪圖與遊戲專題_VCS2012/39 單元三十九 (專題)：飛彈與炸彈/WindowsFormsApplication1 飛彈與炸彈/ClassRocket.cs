/* 作者：鄞永傳老師‧xnabook@yahoo.com.tw‧2009-09 */
using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing; // for Brush class

namespace WindowsFormsApplication1
{
    class ClassRocket
    {
        public int X = 0;       // 爆炸要發生的位置 (目標)
        public int Y = 0;

        public bool Shooting = true; // 是否上昇中
        int ShootingCount = 0; // 上昇的步數
        int BX, BY; // 發射的起始位置
        double Distance; // 發射離爆炸點的距離
        int DX, DY; // 發射距離爆炸點的 X Y 距離
        double step = 2; // 發射每次前進的距離

        public ClassRocket(int X, int Y, int BX, int BY)
        {
            this.X = X;
            this.Y = Y;

            this.BX = BX;
            this.BY = BY;
            Distance = Math.Sqrt((BX - X) * (BX - X) + (BY - Y) * (BY - Y) );

            DX = X - BX;
            DY = BY - Y;
        }

        public bool CheckCollision(int bomb_x, int bomb_y, int range)
        {
            int x = BX + (int)(ShootingCount * (step / Distance) * DX);
            int y = BY - (int)(ShootingCount * (step / Distance) * DY);

            double dist = Math.Sqrt((x - bomb_x) * (x - bomb_x) + (y - bomb_y) * (y - bomb_y));
            if (dist <= range) return true; // 有碰撞
            else return false;
        }
        
        public void Draw(Graphics G)
        {
            if (!Shooting) return;

            ShootingCount++;

            int x = BX + (int)(ShootingCount * (step / Distance) * DX);
            int y = BY - (int)(ShootingCount * (step / Distance) * DY);
            G.FillEllipse(Brushes.White, x - 2, y - 2, 4, 4);
            if (ShootingCount * step >= Distance) Shooting = false;

        }
    }
}
