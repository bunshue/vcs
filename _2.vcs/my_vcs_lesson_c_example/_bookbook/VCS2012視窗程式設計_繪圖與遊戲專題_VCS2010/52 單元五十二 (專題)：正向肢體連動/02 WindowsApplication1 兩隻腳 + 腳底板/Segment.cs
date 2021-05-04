using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing;

namespace WindowsApplication1
{
    class Segment
    {
        PointF pin1 = new PointF();
        Size size = new Size(200, 40);
        public float Angle = 30;
        Color color;

        public Segment(int Width, int Height, Color color)
        {
            size.Width = Width;
            size.Height = Height;
            this.color = color;
        }

        public void SetPos(PointF p)
        {
            pin1.X = p.X;
            pin1.Y = p.Y;
        }

        public void Draw(Graphics G)
        {
            Rectangle rect = new Rectangle();
            rect.X = -size.Height / 2;
            rect.Y = -size.Height / 2;
            rect.Width = size.Width + size.Height;
            rect.Height = size.Height;

            int D = 10;

            G.ResetTransform();
            G.TranslateTransform(pin1.X, pin1.Y);
            G.RotateTransform(Angle);

            SolidBrush brush = new SolidBrush(color);
            G.FillRectangle(brush, rect);
            G.FillEllipse(Brushes.White, -D / 2, -D / 2, D, D);
            G.FillEllipse(Brushes.White, size.Width - D / 2, -D / 2, D, D);

            Pen pen = new Pen(Color.Black);
            G.DrawRectangle(pen, rect);
            G.DrawEllipse(pen, -D / 2, -D / 2, D, D);
            G.DrawEllipse(pen, size.Width - D / 2, -D / 2, D, D);
        }

        public PointF GetPin2()
        {
            PointF P = new PointF();
            P.X = pin1.X + (float)(size.Width * Math.Cos(Angle * Math.PI / 180));
            P.Y = pin1.Y + (float)(size.Width * Math.Sin(Angle * Math.PI / 180));

            return P;
        }
    }
}
