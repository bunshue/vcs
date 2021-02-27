using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D; //for GraphicsPath

namespace vcs_Draw5
{
    public partial class Form1 : Form
    {
        Graphics g;
        public Form1()
        {
            InitializeComponent();
            pictureBox1.Image = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            //g = pictureBox1.CreateGraphics();
            g = Graphics.FromImage(pictureBox1.Image);
            g.Clear(Color.White);
        }

        private void button19_Click(object sender, EventArgs e)
        {
            //pictureBox1.Image = null;
            //Graphics g = Graphics.FromImage(pictureBox1.Image);
            g.Clear(Color.White);
            pictureBox1.Refresh();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //Graphics g = Graphics.FromImage(pictureBox1.Image);
            g.Clear(Color.White);
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(0, 0, 100, 100));

            //using System.Drawing.Drawing2D;
            GraphicsPath gPath = new GraphicsPath();
            gPath.AddLine(new Point(10, 10), new Point(60, 60));
            gPath.AddLine(new Point(60, 10), new Point(10, 60));
            gPath.AddRectangle(new Rectangle(10, 10, 50, 50));
            g.DrawPath(new Pen(Color.Black), gPath);
            pictureBox1.Refresh();
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //Graphics g = Graphics.FromImage(pictureBox1.Image);
            g.Clear(Color.White);
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(0, 0, 100, 100));
            g.DrawArc(new Pen(Color.Black), new Rectangle(0, 0, 100, 100), 90, 180);
            g.DrawArc(new Pen(Color.Black), new Rectangle(100, 100, 100, 100), 90, 180);
            g.DrawArc(new Pen(Color.Black), new Rectangle(200, 200, 100, 100), 90, 180);
            g.DrawArc(new Pen(Color.Black), new Rectangle(300, 300, 100, 100), 90, 180);
            g.DrawArc(new Pen(Color.Black), new Rectangle(400, 400, 79, 79), 90, 180);
            pictureBox1.Refresh();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //Graphics g = Graphics.FromImage(pictureBox1.Image);
            g.Clear(Color.White);
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(0, 0, 100, 100));
            g.DrawBezier(new Pen(Color.Black), 10, 10, 20, 60, 60, 60, 50, 10);
            pictureBox1.Refresh();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //Graphics g = Graphics.FromImage(pictureBox1.Image);
            g.Clear(Color.White);
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(0, 0, 100, 100));
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
            pictureBox1.Refresh();
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //Graphics g = Graphics.FromImage(pictureBox1.Image);
            g.Clear(Color.White);
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(0, 0, 100, 100));

            //using System.Drawing.Drawing2D;
            GraphicsPath gPath = new GraphicsPath();
            gPath.AddLine(new Point(10, 10), new Point(60, 60));
            gPath.AddLine(new Point(60, 10), new Point(10, 60));
            gPath.AddRectangle(new Rectangle(10, 10, 50, 50));
            g.FillPath(new SolidBrush(Color.Lime), gPath);
            pictureBox1.Refresh();
        }
        
    }
}
