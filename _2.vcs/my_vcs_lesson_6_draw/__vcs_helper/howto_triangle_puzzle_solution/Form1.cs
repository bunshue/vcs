using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace howto_triangle_puzzle_solution
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The points.
        private PointF[] Points;

        // The solutions.
        private List<int[]> Solutions;

        // The solution we should display.
        private int CurrentSolution = 100;

        // Define the points and solutions.
        private void Form1_Load(object sender, EventArgs e)
        {
            DoubleBuffered = true;

            // Define the points.
            float dy = ClientSize.Height / 4;
            float dx = (float)(dy / Math.Sqrt(3));
            float top_x = ClientSize.Width / 2;
            float top_y = -dy / 2;
            Points = new PointF[]
            {
                new PointF(top_x - dx, top_y + dy),
                new PointF(top_x + dx, top_y + dy),
                new PointF(top_x - 2 * dx, top_y + 2 * dy),
                new PointF(top_x - 0 * dx, top_y + 2 * dy),
                new PointF(top_x + 2 * dx, top_y + 2 * dy),
                new PointF(top_x - 3 * dx, top_y + 3 * dy),
                new PointF(top_x - 1 * dx, top_y + 3 * dy),
                new PointF(top_x + 1 * dx, top_y + 3 * dy),
                new PointF(top_x + 3 * dx, top_y + 3 * dy),
                new PointF(top_x - 2 * dx, top_y + 4 * dy),
                new PointF(top_x - 0 * dx, top_y + 4 * dy),
                new PointF(top_x + 2 * dx, top_y + 4 * dy),
            };

            // Define the solutions.
            Solutions = new List<int[]>();
            Solutions.Add(new int[] { 0, 2, 3 });
            Solutions.Add(new int[] { 0, 3, 1 });
            Solutions.Add(new int[] { 1, 3, 4 });
            Solutions.Add(new int[] { 2, 5, 6 });
            Solutions.Add(new int[] { 2, 6, 3 });
            Solutions.Add(new int[] { 3, 6, 7 });
            Solutions.Add(new int[] { 3, 7, 4 });
            Solutions.Add(new int[] { 4, 7, 8 });
            Solutions.Add(new int[] { 5, 9, 6 });
            Solutions.Add(new int[] { 6, 9, 10 });
            Solutions.Add(new int[] { 6, 10, 7 });
            Solutions.Add(new int[] { 7, 10, 11 });
            Solutions.Add(new int[] { 7, 11, 8 });

            Solutions.Add(new int[] { 0, 5, 7 });
            Solutions.Add(new int[] { 1, 6, 8 });
            Solutions.Add(new int[] { 3, 9, 11 });
            Solutions.Add(new int[] { 10, 2, 4 });

            Solutions.Add(new int[] { 5, 10, 3 });
            Solutions.Add(new int[] { 2, 7, 1 });
            Solutions.Add(new int[] { 6, 11, 4 });
            Solutions.Add(new int[] { 8, 3, 10 });
            Solutions.Add(new int[] { 4, 6, 0 });
            Solutions.Add(new int[] { 7, 9, 2 });

            Solutions.Add(new int[] { 0, 9, 8 });
            Solutions.Add(new int[] { 1, 5, 11 });
        }

        // Draw the circles and any triangles currently defined.
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the points.
            const float radius = 5;
            foreach (PointF pt in Points)
            {
                e.Graphics.FillEllipse(Brushes.Blue,
                    pt.X - radius, pt.Y - radius,
                    2 * radius, 2 * radius);
            }

            // Draw the current solution.
            if (CurrentSolution < 0)
            {
                // Draw all solutions.
                for (int i = 0; i < Solutions.Count; i++)
                {
                    DrawSolution(e.Graphics, i);
                }
                lblCount.Text = Solutions.Count.ToString();
            }
            else
            {
                // Draw the current solution.
                DrawSolution(e.Graphics, CurrentSolution);
                if (CurrentSolution < Solutions.Count)
                    lblCount.Text = (CurrentSolution + 1).ToString();
            }
        }

        // Draw a solution.
        private void DrawSolution(Graphics gr, int solution_num)
        {
            if (solution_num >= Solutions.Count) return;

            // Get the right color for this solution.
            Pen the_pen;
            if (solution_num < 13) the_pen = Pens.Red;
            else if (solution_num < 17) the_pen = Pens.Green;
            else if (solution_num < 23) the_pen = Pens.Purple;
            else the_pen = Pens.Orange;

            // Make a list of the points in this solution.
            List<PointF> pts = new List<PointF>();
            foreach (int i in Solutions[solution_num]) pts.Add(Points[i]);
            gr.DrawPolygon(the_pen, pts.ToArray());
        }

        // Start showing solutions.
        private void btnShowSolutions_Click(object sender, EventArgs e)
        {
            // Disable the button.
            btnShowSolutions.Enabled = false;
            lblCount.Text = "";

            // Start at the first solution.
            CurrentSolution = 0;

            // Start the timer.
            tmrChangeSolution.Enabled = true;

            // Redraw.
            Refresh();
        }

        // Show the next solution.
        private void tmrChangeSolution_Tick(object sender, EventArgs e)
        {
            // Increment CurrentSolution. If the result is greater than the
            // last solution's index, disable the timer.
            tmrChangeSolution.Enabled = (++CurrentSolution < Solutions.Count);

            // If we're done drawing, enable the button.
            btnShowSolutions.Enabled = (!tmrChangeSolution.Enabled);

            // Redraw.
            Refresh();
        }

        // Show all of the solutions.
        private void btnShowAllSolutions_Click(object sender, EventArgs e)
        {
            CurrentSolution = -1;
            tmrChangeSolution.Enabled = false;
            btnShowSolutions.Enabled = true;
            Refresh();
        }
    }
}
