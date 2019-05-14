using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_draw_on
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            p = new Pen(Color.Red, 6);

        }

        private void button1_Click(object sender, EventArgs e)
        {
            g = this.CreateGraphics();
            int w = 546;
            int h = 167;

            DrawTest(g, w, h);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            g = panel1.CreateGraphics();
            int w = panel1.ClientSize.Width;
            int h = panel1.ClientSize.Height;

            DrawTest(g, w, h);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            g = pictureBox1.CreateGraphics();
            int w = pictureBox1.ClientSize.Width;
            int h = pictureBox1.ClientSize.Height;

            DrawTest(g, w, h);

        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            g = this.CreateGraphics();
            g.Clear(Color.Gray);
            g = panel1.CreateGraphics();
            g.Clear(Color.Gray);
            g = pictureBox1.CreateGraphics();
            g.Clear(Color.Gray);
            
        }

        private void button5_Click(object sender, EventArgs e)
        {
            int w = button5.ClientSize.Width;
            int h = button5.ClientSize.Height;
            g = button5.CreateGraphics();
            g.DrawEllipse(p, 0, 0, w - 1, h - 1);


        }

        private void DrawTest(Graphics g, int w, int h)
        {

            g.DrawRectangle(p, 0, 0, w - 1, h - 1);
            Rectangle rect = new Rectangle(0, 0, w - 1, h - 1);
            g.DrawEllipse(p, rect);

            p = new Pen(Color.FromArgb(255, 0, 123, 0), 5);
            Point px1 = new Point(w / 10, h / 2);
            Point px2 = new Point(w * 9 / 10, h / 2);
            g.DrawLine(new Pen(Brushes.Black, 5), px1, px2);

            p = new Pen(Brushes.Green, 3);
            Point[] points = new Point[7];
            points[0] = new Point(w / 2, 10);
            points[1] = new Point(0, h - 10);
            points[2] = new Point(w / 4, h - 10);
            points[3] = new Point(w / 4, h - 10 - 30);
            points[4] = new Point(w * 3 / 4, h - 10 - 30);
            points[5] = new Point(w * 3 / 4, h - 10);
            points[6] = new Point(w, h - 10);
            g.DrawPolygon(p, points);

            richTextBox1.Text += "w = " + w.ToString() + "\n";
            richTextBox1.Text += "h = " + h.ToString() + "\n";

            p = new Pen(Color.Blue, 3);
            g.DrawRectangle(p, 0, 0, w - 1, h - 1);
            g.DrawRectangle(p, 0, 0, w - 1 - 50, h - 1 - 50);
            g.DrawRectangle(p, 0, 0, w - 1 - 100, h - 1 - 100);

            //Brush b = new SolidBrush(Color.Blue);
            Brush b = new SolidBrush(Color.FromArgb(30, 0, 123, 0));
            g.FillRectangle(b, w / 4, 50, w / 2, 50);
        
        }

    }
}
