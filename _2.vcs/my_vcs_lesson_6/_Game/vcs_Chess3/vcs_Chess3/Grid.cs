using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing;

namespace vcs_Chess3
{
    class Grid // 格線類別
    {
        // w: 視窗寬  h:視窗高  D:格子寬   Center: 原點  
        static public void Draw(int w, int h, int D, Point Center, Graphics G)
        {
            G.DrawLine(Pens.Black, Center.X, 0, Center.X, h); // 垂直中線
            G.DrawLine(Pens.Black, 0, Center.Y, w, Center.Y); // 水平中線

            // 垂直線 往左
            for (int i = Center.X - D; i > 0; i = i - D)
                G.DrawLine(Pens.Silver, i, 0, i, h);

            // 垂直線 往右
            for (int i = Center.X + D; i < w; i = i + D)
                G.DrawLine(Pens.Silver, i, 0, i, h);

            // 水平線 往上
            for (int i = Center.Y - D; i > 0; i = i - D)
                G.DrawLine(Pens.Silver, 0, i, w, i);

            // 水平線 往下
            for (int i = Center.Y + D; i < h; i = i + D)
                G.DrawLine(Pens.Silver, 0, i, w, i);
        }
    }
}
