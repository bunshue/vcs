using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing.Drawing2D;
using System.Drawing;

namespace WindowsFormsApplication1
{
    class G2D_Flag_Canada
    {
        // 中心點、寬
        static public void DrawFlag(Graphics G, int Cx, int Cy, float w)
        {
            float h = w  / 2.0f; // 高是 寬的 1/2
            float x0 = Cx - w / 2;
            float y0 = Cy - h / 2;
            G.FillRectangle(Brushes.White, x0, y0, w, h);

            float h1 = h / 32; // 格子的寬
            G.FillRectangle(Brushes.Red, x0, y0, h1 * 16, h); // 左紅色寬邊

            float x1 = Cx - w / 2 + (h1 * (16 + 32));
            float y1 = Cy - h / 2;
            G.FillRectangle(Brushes.Red, x1, y1, h1 * 16, h); // 右紅色寬邊

            Maple(G, Cx, Cy, h1); // 紅色楓葉

            G.DrawRectangle(Pens.Black, x0, y0, w, h);
        }

        static void Maple(Graphics G, float Cx, float Cy, float D)
        {
            GraphicsPath gp = new GraphicsPath();
            
            PointF[] pt1 = new PointF[3];
            pt1[0] = new PointF(Cx + 0 * D, Cy - 13 * D);
            pt1[1] = new PointF(Cx + 2.5f * D, Cy - 8.8f * D);
            pt1[2] = new PointF(Cx + 5.1f * D, Cy - 9.6f * D);
            gp.AddCurve(pt1, 0.4f);

            PointF[] pt2 = new PointF[3];
            pt2[0] = new PointF(Cx + 5.1f * D, Cy - 9.6f * D);
            pt2[1] = new PointF(Cx + 4 * D, Cy - 2 * D);
            pt2[2] = new PointF(Cx + 7.5f * D, Cy - 5.5f * D);
            gp.AddCurve(pt2, 0.5f);

            PointF[] pt3 = new PointF[3];
            pt3[0] = new PointF(Cx + 7.5f * D, Cy - 5.5f * D);
            pt3[1] = new PointF(Cx + 8.1f * D, Cy - 3.6f * D);
            pt3[2] = new PointF(Cx + 12 * D, Cy - 4 * D);
            gp.AddCurve(pt3, 0.3f);

            PointF[] pt4 = new PointF[3];
            pt4[0] = new PointF(Cx + 12 * D, Cy - 4 * D);
            pt4[1] = new PointF(Cx + 11 * D, Cy - 0 * D);
            pt4[2] = new PointF(Cx + 12.5f * D, Cy + 1 * D);
            gp.AddCurve(pt4, 0.3f);

            PointF[] pt5 = new PointF[3];
            pt5[0] = new PointF(Cx + 12.5f * D, Cy + 1 * D);
            pt5[1] = new PointF(Cx + 6 * D, Cy + 6 * D);
            pt5[2] = new PointF(Cx + 6.5f * D, Cy + 8.5f * D);
            gp.AddCurve(pt5, 0.3f);

            PointF[] pt6 = new PointF[12];  // 點陣列
            pt6[0] = new PointF(Cx + 6.5f * D, Cy + 8.5f * D);
            pt6[1] = new PointF(Cx + 0.5f * D, Cy + 7.5f * D);
            pt6[2] = new PointF(Cx + 0.2f * D, Cy + 8.0f * D);
            pt6[3] = new PointF(Cx + 0.2f * D, Cy + 10.5f * D);
            pt6[4] = new PointF(Cx + 0.5f * D, Cy + 10.5f * D);
            pt6[5] = new PointF(Cx + 0.5f * D, Cy + 14.0f * D);
            pt6[6] = new PointF(Cx - 0.5f * D, Cy + 14.0f * D);
            pt6[7] = new PointF(Cx - 0.5f * D, Cy + 10.5f * D);
            pt6[8] = new PointF(Cx - 0.2f * D, Cy + 10.5f * D);
            pt6[9] = new PointF(Cx - 0.2f * D, Cy + 8.0f * D);
            pt6[10] = new PointF(Cx - 0.5f * D, Cy + 7.5f * D);
            pt6[11] = new PointF(Cx - 6.5f * D, Cy + 8.5f * D);
            gp.AddLines(pt6); // 將 一系列的直線 加入到 GraphicsPath物件

            PointF[] pt7 = new PointF[3];
            pt7[2] = new PointF(Cx - 12.5f * D, Cy + 1 * D);
            pt7[1] = new PointF(Cx - 6 * D, Cy + 6 * D);
            pt7[0] = new PointF(Cx - 6.5f * D, Cy + 8.5f * D);
            gp.AddCurve(pt7, 0.3f);

            PointF[] pt8 = new PointF[3];
            pt8[2] = new PointF(Cx - 12 * D, Cy - 4 * D);
            pt8[1] = new PointF(Cx - 11 * D, Cy - 0 * D);
            pt8[0] = new PointF(Cx - 12.5f * D, Cy + 1 * D);
            gp.AddCurve(pt8, 0.3f);

            PointF[] pt9 = new PointF[3];
            pt9[2] = new PointF(Cx - 7.5f * D, Cy - 5.5f * D);
            pt9[1] = new PointF(Cx - 8.1f * D, Cy - 3.6f * D);
            pt9[0] = new PointF(Cx - 12 * D, Cy - 4 * D);
            gp.AddCurve(pt9, 0.3f);

            PointF[] pt10 = new PointF[3];
            pt10[2] = new PointF(Cx - 5.1f * D, Cy - 9.6f * D);
            pt10[1] = new PointF(Cx - 4 * D, Cy - 2 * D);
            pt10[0] = new PointF(Cx - 7.5f * D, Cy - 5.5f * D);
            gp.AddCurve(pt10, 0.5f);

            PointF[] pt11 = new PointF[3];
            pt11[2] = new PointF(Cx - 0 * D, Cy - 13 * D);
            pt11[1] = new PointF(Cx - 2.5f * D, Cy - 8.8f * D);
            pt11[0] = new PointF(Cx - 5.1f * D, Cy - 9.6f * D);
            gp.AddCurve(pt11, 0.4f);

            gp.CloseFigure();

            G.FillPath(Brushes.Red, gp);
        }
    }
}
