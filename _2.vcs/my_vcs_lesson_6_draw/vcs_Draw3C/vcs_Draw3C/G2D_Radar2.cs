using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;
using System.Drawing.Drawing2D;

namespace vcs_Draw3C
{
    class G2D_Radar2
    {
        int Cx = 100;
        int Cy = 100;
        int D = 200;
        int theta = 0;

        public G2D_Radar2(int Cx, int Cy, int D)
        {
            this.Cx = Cx;
            this.Cy = Cy;
            this.D = D;
        }

        public void Draw(Graphics G)
        {
            G.SmoothingMode = SmoothingMode.AntiAlias;

            Matrix A = new Matrix();

            for (int i = theta; i < 180 + theta; i = i + 10)
            {
                A.Reset();
                A.Rotate(i, MatrixOrder.Append);
                A.Translate(Cx, Cy, MatrixOrder.Append);

                G.Transform = A;
                G.DrawEllipse(Pens.Black, -D / 32, -D / 2, D / 16, D);
            }

            //G.ResetTransform();
            //G.FillEllipse(Brushes.Black, Cx-10, Cy-10, 20, 20);

            theta = theta + 1;
        }
    }
}
