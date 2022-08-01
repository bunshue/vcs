using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_random_draw
{
    public partial class Form1 : Form
    {
        List<PointF> points = new List<PointF>();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox1.Invalidate();


        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            pictureBox1.Invalidate();
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            int W = pictureBox1.Width;
            int H = pictureBox1.Height;
            int nx = 5;
            int ny = 5;
            int border = 20;
            int dx = (W - border * 2) / nx;
            int dy = (H - border * 2) / ny;

            Bitmap bitmap1 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap1);
            Pen p1 = new Pen(Color.Gray, 5);
            Pen p2 = new Pen(Color.Red, 1);

            g.DrawRectangle(p2, 0, 0, W - 1, H - 1);

            int i;
            for (i = 0; i <= ny; i++)
            {
                g.DrawLine(p1, border + 0, border + dy * i, W - border, border + dy * i);
            }

            for (i = 0; i <= ny; i++)
            {
                g.DrawLine(p1, border + dx * i, border, border + dx * i, H - border);
            }
            pictureBox1.Image = bitmap1;
        }
    }
}
