using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_test_all_99_tmp5_draw
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen pen;
        Font font;
        Brush brush;
        public Form1()
        {
            InitializeComponent();
            g = this.CreateGraphics();
            pen = new Pen(Color.Black, 3);
            font = new Font("標楷體", 16);
            brush = new SolidBrush(Color.Black);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            /*
            Point[] pt = new Point[360];    //一維陣列內有360個Point
            int angle;
            int amplitude = 100;
            for (angle = 0; angle < 360; angle += 1)
            {
                pt[angle].X = angle;
                pt[angle].Y = (int)(amplitude * Math.Sin(angle * 3 * Math.PI / 180)) + amplitude;

            }
            g.DrawLines(new Pen(Brushes.Red, 3), pt);
            */
            /*
            //畫多個Rectangles
            Rectangle[] R = new Rectangle[25];
            int i;
            for (i = 0; i <= 24; i++)
            {
                //R[i] = new Rectangle(0 + 30 * i, 0 + 30 * i);
                R[i] = new Rectangle(i * 10 , i * 5, i*30, i*15);
            }
            g.DrawRectangles(new Pen(Brushes.Red, 3), R);
            */

            /*
            //畫實心橢圓形
            System.Drawing.SolidBrush myBrush = new System.Drawing.SolidBrush(System.Drawing.Color.Red);
            g.FillEllipse(myBrush, new Rectangle(0, 0, 200, 300));
            */

            //畫矩形
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(0, 0, 100, 100));

            //畫曲線
            Point[] pts = new Point[5];
            pts[0].X = 10;
            pts[0].Y = 10;
            pts[1].X = 20;
            pts[1].Y = 60;
            pts[2].X = 30;
            pts[2].Y = 10;
            pts[3].X = 40;
            pts[3].Y = 60;
            pts[4].X = 50;
            pts[4].Y = 10;
            g.DrawCurve(new Pen(Color.Black), pts);



            Pen blackPen = new Pen(Color.FromArgb(255, 0, 0, 0), 5);
            g.DrawRectangle(blackPen, 10, 10, 100, 50);


        }
    }
}
