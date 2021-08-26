using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_DrawMaze
{
    public partial class Form1 : Form
    {
        private const int N = 4;
        private const int L = 50;

        int x = 300;
        int y = 300;

        List<Point> points = new List<Point>();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            x = pictureBox1.Width / 2;
            y = pictureBox1.Height / 2;

            points.Clear();
            points.Add(new Point(x, y));
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            Pen p = new Pen(Color.Red, 5);
            if (points.Count > 1)
            {
                e.Graphics.DrawLines(p, points.ToArray());
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            Random r = new Random();

            int result = r.Next(4);
            if (result == 0)
            {
                //向右
                x += L;
            }
            else if (result == 1)
            {
                //向下
                y += L;
            }
            else if (result == 2)
            {
                //向左
                x -= L;
            }
            else if (result == 3)
            {
                //向上
                y -= L;
            }
            else
            {
                richTextBox1.Text += "xxxxx\n";
            }
            if (x < 0)
                x = 0;
            if (y < 0)
                y = 0;
            if (x > pictureBox1.Width)
                x = pictureBox1.Width;
            if (y > pictureBox1.Height)
                y = pictureBox1.Height;


            richTextBox1.Text += "x = " + x.ToString() + ", y = " + y.ToString() + "\n";
            points.Add(new Point(x, y));

            this.pictureBox1.Invalidate();


        }

    }
}
