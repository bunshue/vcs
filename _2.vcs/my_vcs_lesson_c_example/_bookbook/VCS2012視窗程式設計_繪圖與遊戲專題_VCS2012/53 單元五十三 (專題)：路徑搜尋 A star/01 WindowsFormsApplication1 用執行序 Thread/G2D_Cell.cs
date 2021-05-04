using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;

namespace WindowsFormsApplication1
{
    class G2D_Cell
    {
        public Point pos; // 中心點
        short D; // 半徑
        public short no; // 這個點 在 cList 清單 的編號
        short Gap = 2; // 方塊內縮的像素
        public Rectangle rect0; // 完整的 方塊周圍
        public Rectangle rect; // 內縮的 方塊周圍
        Rectangle rect2; // 圓點周圍
        public bool start = false; // 是否為 開始點
        public bool target = false;// 是否為 目標點
        public bool wall = false;  // 是否為 牆壁點
        public int G = 0; // 從 開始點 到 這個點 的 成本
        public int H = 0; // 從 這個點 到 目標點 的 預估成本
        public short Parent = -1; // 在最佳路徑中 這個點 的 父親的編號

        //    7    0    1
        //    6    *    2
        //    5    4    3
        public short[] Neighbor = new short[8]; /// 這個點 的 鄰接點 的編號
        public short row, column; // 這個點 的 行列 位置 for G and H calculation

        public G2D_Cell(Point pos, short D, short no)
        {
            this.pos = pos;
            this.D = D;
            this.no = no;
            rect0 = new Rectangle(pos.X - D, pos.Y - D, 2 * D, 2 * D);
            rect = new Rectangle(pos.X - (D - Gap), pos.Y - (D - Gap), 2 * (D - Gap), 2 * (D - Gap));
            rect2 = new Rectangle(pos.X - (D - 2 * Gap), pos.Y - (D - 2 * Gap), 2 * (D - 2 * Gap), 2 * (D - 2 * Gap));
        }

        public int F() // 總成本
        {
            return G + H;
        }

        // 繪出 方塊
        public void Draw(Graphics G)
        {
            if (start)   // 開始點 的小矩形
                G.FillRectangle(Brushes.LightBlue, rect);  // .Blue
            if (target)  // 目標點 的小矩形
                G.FillRectangle(Brushes.Pink, rect); // .Red
            if (wall)    // 牆壁點 的小矩形
                G.FillRectangle(Brushes.DarkGray, rect);
            G.DrawRectangle(Pens.Black, rect); // 繪出 方塊的邊界矩形
        }

        // 繪出 小圓形
        // Brushes.Green 路徑點、Brushes.Violet 開放點、Brushes.Teal 關閉點
        public void DrawEllipse(Graphics G, Brush brush)
        {
            G.FillEllipse(brush, rect2);
        }

        // 是否有選到這個 方塊
        public bool isInRectangle(Point pt)
        {
            if (pt.X >= pos.X - D && pt.X <= pos.X + D &&
                pt.Y >= pos.Y - D && pt.Y <= pos.Y + D)
                return true;
            return false;
        }
    }
}
