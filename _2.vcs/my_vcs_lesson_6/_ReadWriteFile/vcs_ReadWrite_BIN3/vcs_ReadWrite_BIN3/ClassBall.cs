using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing; // for Point, Color

namespace vcs_ReadWrite_BIN3
{
    class ClassBall
    {
        public Point pt; // 球的位置
        public Color color; // 球的顏色
        int D = 10; // 球的半徑
        int dx, dy; // 滑鼠和球的中心位置 的 偏移值

        // 建構元
        public ClassBall(Point pt, Color color)
        {
            this.pt = pt;
            this.color = color;
        }

        // 檢查是否選到這個點
        public bool CheckSelected(int x, int y)  // 滑鼠的位置 (視窗座標)
        {
            // 滑鼠游標 和 球的 距離
            double dist = Math.Sqrt((pt.X - x) * (pt.X - x) + (pt.Y - y) * (pt.Y - y));
            if (dist <= D)
            {
                dx = x - pt.X; 
                dy = y - pt.Y;
                return true;
            }
            else return false;
        }

        // 更新 球的位置
        public void Move(int x, int y)  // 參數是 滑鼠的位置
        {
            pt.X = x - dx;
            pt.Y = y - dy;
        }
    }
}
