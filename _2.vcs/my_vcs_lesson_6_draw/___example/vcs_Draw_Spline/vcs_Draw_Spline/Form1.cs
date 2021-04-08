using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace vcs_Draw_Spline
{
    public partial class Form1 : Form
    {
        // The points selected by the user.
        private List<Point> Points = new List<Point>();

        // The tension for the curve.
        private float Tension = 0.5f;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the points.
            foreach (Point point in Points)
                e.Graphics.FillEllipse(Brushes.Black,
                    point.X - 3, point.Y - 3, 5, 5);
            if (Points.Count < 2) return;

            // Draw the curve.
            if (rb1.Checked == true)
            {
                e.Graphics.DrawCurve(Pens.Red, Points.ToArray(), Tension);
            }
            else if (rb2.Checked == true)
            {
                using (Pen pen = new Pen(Color.Red))
                {
                    for (int t = 0; t <= 20; t += 2)
                    {
                        pen.Color = Color.FromArgb(255 * t / 20, 0, 255 - 255 * t / 20);
                        e.Graphics.DrawCurve(pen, Points.ToArray(), t / 10f);
                    }
                }
            }
        }

        // Select a point.
        private void Form1_MouseClick(object sender, MouseEventArgs e)
        {
            Points.Add(e.Location);
            Refresh();
        }

        // Change the tension.
        private void trkTension_Scroll(object sender, EventArgs e)
        {
            Tension = trkTension.Value / 10f;
            txtTension.Text = Tension.ToString("0.0");
            Refresh();
        }

        // Start a new point list.
        private void bt_clear_Click(object sender, EventArgs e)
        {
            Points = new List<Point>();
            Refresh();
        }
    }
}
