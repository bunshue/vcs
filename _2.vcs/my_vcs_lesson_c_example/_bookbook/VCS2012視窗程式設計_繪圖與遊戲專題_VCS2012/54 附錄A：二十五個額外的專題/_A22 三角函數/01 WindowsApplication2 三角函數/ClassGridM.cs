using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing;

namespace WindowsApplication1
{
    class ClassGridM
    {
        int d = 10;
        Pen myPen2 = new Pen(Color.Gray, 1);
        Pen myPen1 = new Pen(Color.LightGray, 1);
        public Point offset = new Point(0, 0);
        public bool FrameVisible = false;

        public void AdjustOffset(int dx, int dy)
        {
            offset.X = offset.X + dx;
            offset.Y = offset.Y + dy;
        }

        public void Draw(Graphics G, int w, int h, int d)
        {
            this.d = d;
            if (FrameVisible)
            {
                for (int i = (w / 2) + offset.X - d; i > 0; i = i - d)
                {
                    G.DrawLine(myPen1, i, 0, i, h);
                }

                for (int i = (w / 2) + offset.X + d; i < w; i = i + d)
                {
                    G.DrawLine(myPen1, i, 0, i, h);
                }

                for (int i = (h / 2) + offset.Y - d; i > 0; i = i - d)
                {
                    G.DrawLine(myPen1, 0, i, w, i);
                }

                for (int i = (h / 2) + offset.Y + d; i < h; i = i + d)
                {
                    G.DrawLine(myPen1, 0, i, w, i);
                }
            }

            G.DrawLine(myPen2, w / 2 + offset.X, 0, w / 2 + offset.X, h);
            G.DrawLine(myPen2, 0, h / 2 + offset.Y, w, h / 2 + offset.Y);

        }

    }
}
