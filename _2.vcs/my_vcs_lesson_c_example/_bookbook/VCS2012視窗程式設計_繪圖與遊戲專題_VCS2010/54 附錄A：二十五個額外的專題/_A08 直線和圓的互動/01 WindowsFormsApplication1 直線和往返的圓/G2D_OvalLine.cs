using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    class G2D_OvalLine
    {
        int Cx;
        int Cy;
        double D = 100;
        double angle = 0;
        double angleD;
        Pen myPen;

        double D2 = 100;
        double D2_d = 1;
        Timer timer1;

        public G2D_OvalLine(int Cx, int Cy, double angleD, Color color)
        {
            this.Cx = Cx;
            this.Cy = Cy;
            this.angleD = angleD;
            myPen = new Pen(color, 2);

            this.timer1 = new Timer();
            this.timer1.Enabled = true;
            this.timer1.Interval = 10;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            D2 = D2 - D2_d;
            if (D2 >= D || D2 <= -D)
                D2_d = -D2_d;
        }

        public void Draw(Graphics G)
        {
            float x0, y0, x1, y1, x2, y2;

            x0 = Cx + (float)(D * Math.Cos(angle));
            y0 = Cy + (float)(D * Math.Sin(angle));

            x1 = Cx + (float)(D * Math.Cos(angle + Math.PI));
            y1 = Cy + (float)(D * Math.Sin(angle + Math.PI));

            G.DrawLine(myPen, x0, y0, x1, y1);

            G.FillEllipse(Brushes.Black, x0 - 5, y0 - 5, 10, 10); // 兩側的小圓
            G.FillEllipse(Brushes.Black, x1 - 5, y1 - 5, 10, 10);

            x2 = Cx + (float)(D2 * Math.Cos(angle));
            y2 = Cy + (float)(D2 * Math.Sin(angle));
            G.FillEllipse(Brushes.Red, x2 - 5, y2 - 5, 10, 10); // 往返兩側的小圓


            G.FillEllipse(Brushes.Black, Cx - 10, Cy - 10, 20, 20);  // 中間的大圓
        }

        public void Update()
        {
            angle = angle + angleD;
        }

    }
}
