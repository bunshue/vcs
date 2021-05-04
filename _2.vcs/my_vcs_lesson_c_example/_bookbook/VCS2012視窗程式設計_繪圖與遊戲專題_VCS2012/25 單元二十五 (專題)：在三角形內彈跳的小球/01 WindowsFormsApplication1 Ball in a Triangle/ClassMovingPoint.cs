using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing;

namespace WindowsFormsApplication1
{
    class ClassMovingPoint
    {
        public Point pos = new Point(); // 點的標準座標
        int dx, dy; // 滑鼠和點中心 的 偏移值
        int D = 10 ; // 點繪出成 圓點 的半徑
        int Epsilon =100; // 滑鼠 是否 點選到點 的距離 判斷 (避免 開根號)
        SolidBrush brush;
        Font fn = new Font("Times New Roman", 20);
        string str;

        public ClassMovingPoint(Point pos, int D, Color color, string str)
        {
            this.pos = pos;
            this.D = D;
            Epsilon = D * D;
            brush = new SolidBrush(color);
            this.str = str;
            Epsilon = D * D;
        }

        // 檢查是否選到這個點
        public bool CheckSelected(int x, int y)  // 滑鼠的位置 (視窗座標)
        {
            int dist = ((pos.X - x) * (pos.X - x) + (pos.Y - y) * (pos.Y - y));

            if (dist <= Epsilon) // dis 是尚未開根號 的距離
            {
                dx = x - pos.X;
                dy = y - pos.Y;
                return true;
            }
            else return false;
        }

        // 更新 點的標準座標
        public void Move(int x, int y)  // 滑鼠的位置
        {
            pos.X = x - dx;
            pos.Y = y - dy;
        }

        public void Draw(Graphics G)  
        {
            // G.FillRectangle(brush, pos.X - 10, pos.Y - 10, 20, 20);
            G.DrawRectangle(Pens.Black, pos.X - 10, pos.Y - 10, 20, 20);
            G.DrawString(str, fn, Brushes.Black, pos.X, pos.Y, StringFormat.GenericTypographic);
        }
    }
}
