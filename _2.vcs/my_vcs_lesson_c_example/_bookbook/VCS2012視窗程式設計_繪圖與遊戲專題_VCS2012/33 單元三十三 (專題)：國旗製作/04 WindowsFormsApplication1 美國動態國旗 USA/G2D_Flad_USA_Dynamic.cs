using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing.Drawing2D;
using System.Drawing;

namespace WindowsFormsApplication1
{
    class G2D_Flad_USA_Dynamic
    {
        Random rd = new Random();
        float offset = 0;
        // 中心點、寬
        public void DrawFlag(Graphics G, int Cx, int Cy, float w)
        {
            float h = w * 10 / 19.0f; // 高是 寬的 10 / 19
            G.FillRectangle(Brushes.White, Cx - w / 2, Cy - h / 2, w, h);

            float L = h / 13; // 條紋的寬
            float x1, y1;
            offset = offset + 2;
            if (offset > L) offset = -L;
            for (int i = 0; i <= 6; i++)
            {
                x1 = Cx - w / 2.0f;
                y1 = (Cy - h / 2.0f) + i * 2 * L + offset;
                if (i == 0 && offset < 0)
                {
                    y1 = (Cy - h / 2.0f) + i * 2 * L;
                    G.FillRectangle(Brushes.Red, x1, y1, w, L + offset);
                }
                else if (i == 6 && offset > 0)
                {
                    G.FillRectangle(Brushes.Red, x1, y1, w, L - offset);
                }
                else
                  G.FillRectangle(Brushes.Red, x1, y1, w, L);
            }

            float D = (int)(h * 0.76); // 左上 藍天
            float C = h * 7 / 13;
            G.FillRectangle(Brushes.Blue, Cx - w / 2, Cy - h / 2, D, C);

            float E = h * 0.054f;
            float H = h * 0.063f;

            float K = h * 0.0616f / 2.0f;

            float x0 = Cx - w / 2;
            float y0 = Cy - h / 2;
            float x, y;
            for (int i = 0; i < 5; i++) // 繪出奇數列 (共5列，每列6顆星星)
            {
                for (int j = 0; j < 6; j++)
                {
                    x = x0 + H + j * 2 * H + (rd.Next(5) - 2);
                    y = y0 + E + i * 2 * E + (rd.Next(5) - 2);
                    Star(G, x, y, K, -90);
                }
            }

            for (int i = 0; i < 4; i++) // 繪出偶數列 (共4列，每列5顆星星)
            {
                for (int j = 0; j < 5; j++)
                {
                    x = x0 + 2 * H + j * 2 * H + (rd.Next(5) - 2);
                    y = y0 + 2 * E + i * 2 * E + (rd.Next(5) - 2);
                    Star(G, x, y, K, -90);
                }
            }
            
            G.DrawRectangle(Pens.Black, Cx - w / 2, Cy - h / 2, w, h);
        }

        void Star(Graphics G, float Cx, float Cy, float D, double theta0)
        {
            PointF[] pt = new PointF[5];

            for (int i = 0; i < pt.Length; i++)
            {
                float x = (float)(Cx + D * Math.Cos((theta0 + i * 144) * Math.PI / 180));
                float y = (float)(Cy + D * Math.Sin((theta0 + i * 144) * Math.PI / 180));
                pt[i] = new PointF(x, y);
            }

            GraphicsPath gp = new GraphicsPath();
            gp.AddLines(pt);
            gp.CloseFigure();
            gp.FillMode = FillMode.Winding; // 指定填滿模式

            G.FillPath(Brushes.White, gp);
        }
    }
}
