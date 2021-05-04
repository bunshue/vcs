using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing;

namespace WindowsApplication1
{
    class ClassMovingPoint
    {
        public PointF p = new PointF(); // 點的標準座標

        public int D;  // 格子單位寬
        public int W, H; // 視窗寬高
        int dx, dy; //滑鼠和點中心 的 偏移值

        public ClassMovingPoint(PointF p, int W, int H, int D)
        {
            this.p = p;
            this.W = W;
            this.H = H;
            this.D = D;
        }

        // 檢查是否選到這個點
        public bool CheckSelected(int x, int y)  // 滑鼠的位置 (視窗座標)
        {
            Point point = new Point(); // 點 的 視窗座標 
            point.X = (int)(W / 2 + p.X * D);
            point.Y = (int)(H / 2 - p.Y * D);

            double dist = Math.Sqrt((point.X - x) * (point.X - x) + (point.Y - y) * (point.Y - y));
            if (dist <= D/2)
            {
                dx = x - point.X;
                dy = y - point.Y;
                return true;
            }
            else return false;
        }

        // 更新 點的標準座標
        public void Move(int x, int y)  // 滑鼠的位置
        {
            p.X = ((x - dx) - W / 2.0f) / D; 
            p.Y = -((y - dy) - H / 2.0f) / D;
        }

    }
}
