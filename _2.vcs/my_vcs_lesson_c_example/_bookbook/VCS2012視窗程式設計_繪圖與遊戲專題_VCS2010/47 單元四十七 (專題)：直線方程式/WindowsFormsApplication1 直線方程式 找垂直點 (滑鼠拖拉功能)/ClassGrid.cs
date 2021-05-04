/* 作者：鄞永傳老師‧xnabook@yahoo.com.tw‧2009-09 */
using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing;

namespace WindowsFormsApplication1
{
    class ClassGrid
    {
        int d = 10;
        Pen myPen2 = new Pen(Color.Gray, 1);
        Pen myPen1 = new Pen(Color.LightGray, 1);

        public void Draw(Graphics G, int w, int h, int d)
        {
            this.d = d;

            for (int i = w / 2 - d; i > 0; i = i - d)
            {
                G.DrawLine(myPen1, i, 0, i, h);
            }

            for (int i = w / 2 + d; i < w; i = i + d)
            {
                G.DrawLine(myPen1, i, 0, i, h);
            }

            for (int i = h / 2 - d; i > 0; i = i - d)
            {
                G.DrawLine(myPen1, 0, i, w, i);
            }

            for (int i = h / 2 + d; i < h; i = i + d)
            {
                G.DrawLine(myPen1, 0, i, w, i);
            }

            G.DrawLine(myPen2, w / 2, 0, w / 2, h);
            G.DrawLine(myPen2, 0, h / 2, w, h / 2);

        }

    }
}
