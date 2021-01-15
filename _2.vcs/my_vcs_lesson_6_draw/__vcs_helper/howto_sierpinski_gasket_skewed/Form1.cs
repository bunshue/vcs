using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace howto_sierpinski_gasket_skewed
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The selected points.
        private List<Point> Corners = new List<Point>();
        private Point LastPoint ;
        private int RADIUS = 2;

        private void Form1_MouseClick(object sender, MouseEventArgs e)
        {
            if (tmrDraw.Enabled)
            {
                // Stop running.
                tmrDraw.Enabled = false;
                Corners = new List<Point>();
            }
            else
            {
                // Left or right button?
                if (e.Button == MouseButtons.Right)
                {
                    // Start running.
                    if (Corners.Count < 2)
                    {
                        // We need more points.
                        MessageBox.Show(
                            "Left-click at least two points before right-clicking.",
                            "Need More Points", MessageBoxButtons.OK,
                            MessageBoxIcon.Exclamation);
                    }
                    else
                    {
                        // Start at the first point.
                        LastPoint = Corners[0];

                        // Start.
                        tmrDraw.Enabled = true;
                    }
                }
                else // Left button.
                {
                    // Save the point.
                    Corners.Add(new Point(e.X, e.Y));

                    // Draw the new point.
                    using (Graphics gr = this.CreateGraphics())
                    {
                        if (Corners.Count == 1) gr.Clear(this.BackColor);
                        gr.DrawEllipse(Pens.Blue,
                            e.X - RADIUS, e.Y - RADIUS,
                            2 * RADIUS, 2 * RADIUS);
                    }
                }
            }
        }

        // Draw 1,000 points.
        private void tmrDraw_Tick(object sender, EventArgs e)
        {
            // Draw points.
            Random rand = new Random();
            using (Graphics gr = this.CreateGraphics())
            {
                // Draw the corners.
                foreach (PointF pt in Corners)
                {
                    gr.FillEllipse(Brushes.White, pt.X - RADIUS, pt.Y - RADIUS, 2 * RADIUS, 2 * RADIUS);
                    gr.DrawEllipse(Pens.Blue, pt.X - RADIUS, pt.Y - RADIUS, 2 * RADIUS, 2 * RADIUS);
                }

                // Draw 1000 points.
                for (int i = 1; i <= 1000; i++)
                {
                    int j = rand.Next(0, Corners.Count);
                    LastPoint = new Point(
                        (LastPoint.X + Corners[j].X) / 2,
                        (LastPoint.Y + Corners[j].Y) / 2);
                    gr.DrawLine(Pens.Blue, LastPoint.X, LastPoint.Y,
                        LastPoint.X + 1, LastPoint.Y + 1);
                }
            }
        }
    }
}

