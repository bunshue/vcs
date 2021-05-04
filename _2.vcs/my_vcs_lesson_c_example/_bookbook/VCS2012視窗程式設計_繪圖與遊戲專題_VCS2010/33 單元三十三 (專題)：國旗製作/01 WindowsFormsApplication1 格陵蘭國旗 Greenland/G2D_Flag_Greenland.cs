using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing.Drawing2D;
using System.Drawing;

namespace WindowsFormsApplication1
{
    class G2D_Flag_Greenland
    {
        // 畫布、中心點、寬
        static public void DrawFlag(Graphics G, int Cx, int Cy, float w)
        {
            float h = w * 2 / 3.0f; // 高是 寬的 2 / 3
            float x = Cx - w / 2;
            float y = Cy - h / 2;
            G.FillRectangle(Brushes.White, x, y, w, h);  // 白底

            float x1 = Cx - w / 2;
            float y1 = Cy;
            G.FillRectangle(Brushes.Red, x1, y1, w, h / 2); // 下半部是紅色

            float d = w * 4.0f / 18.0f;
            float x2 = x + w * 7.0f / 18.0f - d;
            float y2 = y1 - d;
            G.FillEllipse(Brushes.Red, x2, y2, d * 2, d * 2); // 中間是一個紅色圓形

            G.FillPie(Brushes.White, x2, y2, d * 2, d * 2, 0, 180); // 圓形下半部是白色

            G.DrawRectangle(Pens.Black, x, y, w, h); // 國旗外框
        }
    }
}
