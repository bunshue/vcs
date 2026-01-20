using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing; // Point

namespace vcs_MousePaint1
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
            if (dist <= 10)
            {
                dx = x - p.X;
                dy = y - p.Y;
                return true;
            }
            else
            {
                return false;
            }
        }

        // 更新 點的座標
        public void Move(int x, int y)  // 滑鼠的位置
        {
            p.X = (x - dx); 
            p.Y = (y - dy);
        }
    }
}
