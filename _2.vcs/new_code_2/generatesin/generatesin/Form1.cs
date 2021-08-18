using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace generatesin
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            this.pictureBox1.Invalidate();
        }

        private double rad(double d)
        {
            return d * Math.PI / 180.0;
        }

        private double sind(double d)
        {
            return Math.Sin(d * Math.PI / 180.0);
        }

        private double cosd(double d)
        {
            return Math.Cos(d * Math.PI / 180.0);
        }

        private void DrawCircle(Graphics g, PointF center, int radius, int linewidth, Color c)
        {
            // Create a new pen.
            //顏色、線寬分開寫
            //Pen p = new Pen(c);
            // Set the pen's width.
            //p.Width = linewidth;

            //顏色、線寬寫在一起
            Pen p = new Pen(c, linewidth);
            // Draw the circle
            g.DrawEllipse(p, center.X - radius, center.Y - radius, radius * 2, radius * 2);
            //Dispose of the pen.
            p.Dispose();
        }

        private void FillCircle(Graphics g, PointF center, int radius, Color c)
        {
            SolidBrush sb = new SolidBrush(c);

            // Fill the circle
            g.FillEllipse(sb, new RectangleF(center.X - radius, center.Y - radius, radius * 2, radius * 2));

            //Dispose of the brush
            sb.Dispose();
        }

        double angle = 0;
        int x_st = 100;
        int y_st = 100;
        int L = 170;
        int cx = 200;
        int cy = 200;
        PointF pt = new PointF();

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.DrawLine(new Pen(Color.Black, 2), cx - 200, cy, cx + 200, cy);
            e.Graphics.DrawLine(new Pen(Color.Black, 2), cx, cy - 200, cx, cy + 200);

            pt = new PointF(cx, cy);
            //e.Graphics.DrawEllipse(new Pen(Color.Red, 3), x_st, y_st, L, L);
            DrawCircle(e.Graphics, pt, L, 3, Color.Yellow);

            x_st = cx + (int)(L * cosd(angle));
            y_st = cy + (int)(L * sind(angle));

            e.Graphics.DrawLine(new Pen(Color.Black, 2), 200, y_st, x_st, y_st);
            e.Graphics.DrawLine(new Pen(Color.Black, 2), x_st, 200, x_st, y_st);


            pt = new PointF(x_st, y_st);
            FillCircle(e.Graphics, pt, 10, Color.Red);

            angle -= 6;




        }
    }
}
