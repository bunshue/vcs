using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing; // Point

namespace WindowsApplication1
{
    class MovingPoint  // 可更新移動的 點的類別
    {
        public Point p = new Point(); // 點的標準座標
        int dx, dy; // 滑鼠和點中心 的 偏移值

        public MovingPoint(Point p)
        {
            this.p = p;
        }

        // 檢查是否選到這個點
        public bool CheckSelected(int x, int y)  // 滑鼠的位置 (視窗座標)
        {
            double dist = Math.Sqrt((p.X - x) * (p.X - x) + (p.Y - y) * (p.Y - y));
            dx = x - p.X;
            dy = y - p.Y;

            if (dist <= 10)
            {
                return true;
            }
            else return false;
        }

        // 更新 點的座標
        public void Update(int x, int y)  // 滑鼠的位置
        {
            p.X = (x - dx); 
            p.Y = (y - dy);
        }

        public void Draw(Graphics G)  // 
        {
            G.DrawRectangle(Pens.Black, p.X - 10, p.Y - 10, 20, 20);
        }
    }
}
