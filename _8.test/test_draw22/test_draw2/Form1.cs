using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace test_draw2
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;

        int PointCounter = 0;
        Point[] arrayPoint = new Point[99];

        public Form1()
        {
            InitializeComponent();
            g = this.CreateGraphics();
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            arrayPoint[PointCounter] = new Point(e.X, e.Y);
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                PointCounter++;
                arrayPoint[PointCounter] = new Point(e.X, e.Y);
                PointCounter++;

            }
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            /*
            int x1, y1, x2, y2;
            g.Clear(Color.LightGreen);
            //SolidBrush brush = new SolidBrush(Color.Blue);
            //Font font = new Font("標楷體", 20);

            for (int i = 0; i <= PointCounter; i += 2)
            {
                x1 = arrayPoint[i].X;
                y1 = arrayPoint[i].Y;
                x2 = arrayPoint[i+1].X;
                y2 = arrayPoint[i+1].Y;
                g.DrawLine(p, x1, y1, x2, y2);

            }
            */


        }
    }
}
