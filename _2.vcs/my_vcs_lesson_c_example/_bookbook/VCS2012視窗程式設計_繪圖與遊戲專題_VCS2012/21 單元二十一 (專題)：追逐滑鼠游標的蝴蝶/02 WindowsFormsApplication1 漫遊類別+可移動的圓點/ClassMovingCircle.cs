/* 作者：鄞永傳老師‧xnabook@yahoo.com.tw‧2009-09 */
using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing;

namespace WindowsFormsApplication1
{
    class ClassMovingCircle
    {
        public Point pos = new Point(); // 圓點的座標
        int D = 100;  // 圓點的半徑

        int dx, dy; //滑鼠和點中心 的 偏移值
        public bool dragging = false; // 是否拖拉中

        public ClassMovingCircle(int D, Point pos)
        {
            this.D = D;
            this.pos = pos;
        }

        // 檢查是否選到這個圓點
        public bool CheckSelected(int x, int y)  // 滑鼠的位置 (視窗座標)
        {
            double dis = Math.Sqrt((pos.X - x) * (pos.X - x) + (pos.Y - y) * (pos.Y - y));
            if (dis <= D)
            {
                dx = x - pos.X;
                dy = y - pos.Y;
                dragging = true;
                return true;
            }
            else
            {
                dragging = false;
                return false;
            }
        }

        // 更新 圓點的座標
        public void Move(int x, int y)  // 滑鼠的位置
        {
            pos.X = x - dx;
            pos.Y = y - dy;
        }

        // 更新 圓點的座標
        public void Update(int x, int y)  // 滑鼠的位置
        {
            if (dragging)
            {
                Move(x, y);
            }
        }

        // 繪出 圓點
        public void Draw(Graphics G)  
        {
            G.FillEllipse(Brushes.Pink, pos.X-D, pos.Y-D, 2* D, 2* D);
            G.DrawEllipse(Pens.Black, pos.X - D, pos.Y - D, 2 * D, 2 * D);
        }

    }
}
