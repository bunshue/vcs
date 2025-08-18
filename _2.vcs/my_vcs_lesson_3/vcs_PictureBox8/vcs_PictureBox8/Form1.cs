using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;//for SmoothingMode

namespace vcs_PictureBox8
{
    public partial class Form1 : Form
    {
        private PointF Point1, Point2;
        private bool Drawing = false;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            Point1 = e.Location;
            Point2 = e.Location;
            pictureBox1.Refresh();
            Drawing = true;
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (!Drawing) return;
            Point2 = e.Location;
            pictureBox1.Refresh();
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            if (!Drawing) return;
            Drawing = false;
            pictureBox1.Refresh();
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(pictureBox1.BackColor);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            if (Point1 != Point2)
            {
                //e.Graphics.DrawRectangle(Pens.Black, Point1, Point2);
                e.Graphics.DrawLine(Pens.Black, Point1, Point2);
            }
        }
    }
}
