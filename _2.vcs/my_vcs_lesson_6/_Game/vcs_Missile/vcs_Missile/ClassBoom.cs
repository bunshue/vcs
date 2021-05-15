using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing; // for Brush class

namespace vcs_Missile
{
    class ClassBoom
    {
        Brush[] boom = new Brush[]
			{
				Brushes.WhiteSmoke,
				Brushes.Gold,
				Brushes.Magenta, //Orange,
				Brushes.Red //Crimson
			};

        int boom_index = 0;

        int X = 0;       // 爆炸發生的位置
        int Y = 0;

        int D = 50;      // 最大半徑
        int r = 0;       // 變大變小的 半徑
        int Delta_r = 1; // 半徑的變化量 

        public enum status { active, suspend, die }; // 可能的狀態
        public status Current_Status; // 目前的狀態

        public enum BoomType { active, passive } // 主動 或 被動 
        public BoomType boom_Type = BoomType.active; // 爆炸的型態 主動 或 被動 

        int Count = 0;   // 現在是第幾次
        int Total_Count; // 要呈現幾次

        // 取出顏色值
        public int GetColor(int k)
        {
            return (new Pen(boom[k])).Color.ToArgb();
        }

        public ClassBoom(int X, int Y, int Total_Count, status Current_Status)
        {
            this.X = X;
            this.Y = Y;
            this.Total_Count = Total_Count;
            this.Current_Status = Current_Status;
        }

        public bool CheckCollision(int bomb_x, int bomb_y)
        {
            if (Current_Status != status.active) return false;

            double dist = Math.Sqrt((X - bomb_x) * (X - bomb_x) + (Y - bomb_y) * (Y - bomb_y));
            if (dist <= r) return true; // 有碰撞
            else return false;
        }

        public void Draw(Graphics G)
        {
            if (Current_Status != status.active) return;
            boom_index %= boom.Length; // 確定在 0 ~ 4 之間 變換顏色

            if (r > D || r < 0) Delta_r = -Delta_r;
            r = r + Delta_r;
            G.FillEllipse(boom[boom_index++], X - r, Y - r, 2 * r, 2 * r);

            if (r == -1)
            {
                Count++;
                if (Count >= Total_Count)
                    Current_Status = status.die;
            }
        }
    }
}
