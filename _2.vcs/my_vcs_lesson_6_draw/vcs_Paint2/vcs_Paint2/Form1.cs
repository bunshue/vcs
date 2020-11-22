using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Paint2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Draw.
        private bool Drawing = false;
        private List<Point> Points = new List<Point>();

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            Drawing = true;
            Points = new List<Point>();
            Points.Add(e.Location);
            Refresh();


        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (!Drawing) return;
            if (Points.Count > 0)
            {
                Point last_point = Points[Points.Count - 1];
                if ((last_point.X != e.X) || (last_point.Y != e.Y))
                    Points.Add(e.Location);
            }
            else
                Points.Add(e.Location);
            Refresh();


        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            Drawing = false;

        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            if (Points.Count > 1)
                e.Graphics.DrawLines(Pens.Black, Points.ToArray());

        }
    }
}
