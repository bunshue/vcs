using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D;

// 收集滑鼠點數

namespace vcs_PictureBox7
{
    public partial class Form1 : Form
    {
        private List<PointF> points = new List<PointF>();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            points.Add(new Point(e.X, e.Y));

            this.pictureBox1.Invalidate();
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(this.pictureBox1.BackColor);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Fill all of the points.
            foreach (PointF pt in points)
            {
                e.Graphics.FillEllipse(Brushes.Cyan, pt.X - 3, pt.Y - 3, 7, 7);
            }

            // Draw all of the points.
            foreach (PointF pt in points)
            {
                e.Graphics.DrawEllipse(Pens.Black, pt.X - 3, pt.Y - 3, 7, 7);
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "共有點數 : " + points.Count.ToString() + "\n";
            foreach (PointF pt in points)
            {
                richTextBox1.Text += pt.ToString() + " ";
            }
            richTextBox1.Text += "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            points = new List<PointF>();
            this.pictureBox1.Invalidate();
        }
    }
}
