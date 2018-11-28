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

        private void button1_Click(object sender, EventArgs e)
        {
            SolidBrush brush = new SolidBrush(Color.Blue);
            Font font = new Font("標楷體", 20);
            g.DrawString("想要寫的文字", font, brush, 20, 20);
            g.DrawString("想要寫的文字", font, brush, 50, 50);
            g.DrawString("想要寫的文字", font, brush, 80, 80);
            
        }

        private void button2_Click(object sender, EventArgs e)
        {
            p = new Pen(Color.Blue, 5);
            g.DrawLine(p, 100, 100, 400, 100);
            g.DrawLine(p, 100, 150, 400, 150);
            g.DrawLine(p, 100, 200, 400, 200);
            g.DrawLine(p, 100, 250, 400, 250);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Point[] arrayPoint = new Point[20];
            p = new Pen(Color.Blue, 5);
            double zz;

            for (int i = 0; i < 20; i++)
            {
                zz = Math.Sin(Math.PI * i * 30 / 180) * 200 + 200;
                arrayPoint[i].X = i * 20;
                arrayPoint[i].Y = (int)zz;
            }
            g.DrawLines(p, arrayPoint);
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
