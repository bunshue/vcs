using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;  // for PointF
using System.Drawing.Drawing2D; //  for GraphicsPath

namespace vcs_Draw3C
{
    class G2D_LemniscateOfBernoulli
    {
        int a;  // 數字 8 曲線的半徑
        GraphicsPath gp; // 圖形軌跡物件

        public G2D_LemniscateOfBernoulli(int a)
        {
            this.a = a;
            setVertex();
        }

        // 計算出 360  個座標點
        public void setVertex()
        {
            PointF[] pt = new PointF[360];

            double theta;
            double numerator; // 分子
            double denominator; // 分母
            
            for (int t = 0; t < 360; t++)
            {
                theta = t * Math.PI / 180;

                denominator = (Math.Sin(theta) * Math.Sin(theta) + 1);
                numerator = (a * 1.4142 * Math.Cos(theta));

                pt[t].X = (float)(numerator / denominator);
                pt[t].Y = (float)(numerator * Math.Sin(theta) / denominator);
            }

            gp = new GraphicsPath();
            gp.AddLines(pt);
            gp.CloseFigure();
        }

        // 得到第 t 個座標點
        public PointF GetPos(int t, int Cx, int Cy)
        {
            PointF pt = new PointF();

            double theta = t * Math.PI / 180;
            double numerator; // 分子
            double denominator; // 分母

            denominator = (Math.Sin(theta) * Math.Sin(theta) + 1);
            numerator = (a * 1.4142 * Math.Cos(theta));

            pt.X = Cx + (float)(numerator / denominator);
            pt.Y = Cy + (float)(numerator * Math.Sin(theta) / denominator);

            //pt.X = Cx + (float)((a * 1.4142 * Math.Cos(theta)) / (Math.Sin(theta) * Math.Sin(theta) + 1));
            //pt.Y = Cy + (float)((a * 1.4142 * Math.Cos(theta) * Math.Sin(theta)) / (Math.Sin(theta) * Math.Sin(theta) + 1));

            return pt;
        }

        // 繪出
        public void Draw(Graphics G, int Cx, int Cy)
        {
            G.ResetTransform();
            G.TranslateTransform(Cx, Cy, MatrixOrder.Append); // 再平移
            G.DrawPath(Pens.Black, gp);
            G.ResetTransform();
        }
    }
}
