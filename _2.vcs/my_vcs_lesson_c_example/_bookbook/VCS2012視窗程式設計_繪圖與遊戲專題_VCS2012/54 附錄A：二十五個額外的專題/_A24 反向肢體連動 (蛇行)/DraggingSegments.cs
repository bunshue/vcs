using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing;

namespace WindowsApplication1
{
    class DraggingSegments
    {
        Segment[] seg ;

        // snake01 = new DraggingSegments(10, 60, 20, Color.Red, Color.Blue);
        public DraggingSegments(int segNo, int segW, int segH, Color color1, Color color2)
        {
            seg = new Segment[segNo];

            seg[0] = new Segment(segW, segH, color1);
            seg[0].SetPos(new PointF(10, 10));

            for (int i = 1; i < seg.Length; i++)
            {
                if (i % 2 == 0)
                    seg[i] = new Segment(segW, segH, color1);
                else
                    seg[i] = new Segment(segW, segH, color2);

                seg[i].SetPos(seg[i - 1].GetPin2());
            }

        }

        public void Update(int X, int Y)
        {
            drag(seg[seg.Length - 1], X, Y);

            for (int i = seg.Length - 2; i >= 0; i--)
            {
                drag(seg[i], (int)seg[i + 1].pin1.X, (int)seg[i + 1].pin1.Y);
            }
        }
        
        void drag(Segment seg, int X, int Y)
        {
            float dx = X - seg.pin1.X;
            float dy = Y - seg.pin1.Y;
            double theta = Math.Atan2(dy, dx);
            float angle = (float)(theta * 180 / Math.PI);
            seg.Angle = angle;

            PointF pin2 = seg.GetPin2();
            float dw = pin2.X - seg.pin1.X;
            float dh = pin2.Y - seg.pin1.Y;
            seg.SetPos(new PointF(X - dw, Y - dh));
        }

        public void Draw(Graphics G)
        {
            // Ã¸¥X 
            for (int i = 0; i < seg.Length; i++)
            {
                seg[i].Draw(G);
            }
        }
    }
}
