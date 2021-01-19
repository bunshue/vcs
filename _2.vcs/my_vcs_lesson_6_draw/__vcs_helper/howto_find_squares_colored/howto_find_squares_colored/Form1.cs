using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;
using System.Windows;

namespace howto_find_squares_colored
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

        // The solutions' side lengths.
        private List<int> SideLengths;

        // The solution we should display.
        private int CurrentSolution = 100;

        // Colors used to draw the squares.
        private Color[] Colors =
            { Color.Red, Color.Green, Color.Blue, };

        // Define the points and solutions.
        private void Form1_Load(object sender, EventArgs e)
        {
            DoubleBuffered = true;

            // Define the points.
            float dx = Math.Min(ClientSize.Width, ClientSize.Height) / 4;
            float dy = dx;
            float x0 = (ClientSize.Width - 3 * dx) / 2;
            float y0 = (ClientSize.Height - 3 * dy) / 2;
            Points = new PointF[]
            {
                new PointF(x0 + dx, y0),
                new PointF(x0 + 2 * dx, y0),
                new PointF(x0, y0 + dy),
                new PointF(x0 + dx, y0 + dy),
                new PointF(x0 + 2 * dx, y0 + dy),
                new PointF(x0 + 3 * dx, y0 + dy),
                new PointF(x0, y0 + 2 * dy),
                new PointF(x0 + dx, y0 + 2 * dy),
                new PointF(x0 + 2 * dx, y0 + 2 * dy),
                new PointF(x0 + 3 * dx, y0 + 2 * dy),
                new PointF(x0 + dx, y0 + 3 * dy),
                new PointF(x0 + 2 * dx, y0 + 3 * dy),
            };

            // Define the solutions and side lengths.
            Solutions = new List<int[]>();
            SideLengths = new List<int>();

            // Find the solutions.
            FindSolutions();
        }

        // Find the solutions.
        private void FindSolutions()
        {
            for (int i = 0; i < Points.Length - 3; i++)
            {
                for (int j = i + 1; j < Points.Length - 2; j++)
                {
                    for (int k = j + 1; k < Points.Length - 1; k++)
                    {
                        for (int m = k + 1; m < Points.Length; m++)
                        {
                            // See if these points make a square.
                            int[] square_points = GetSquarePoints(i, j, k, m);
                            if (square_points != null)
                            {
                                Solutions.Add(square_points);

                                // Save the side length.
                                int side_length =
                                    (int)PointFDistance(Points[i], Points[j]);
                                if (!SideLengths.Contains(side_length))
                                    SideLengths.Add(side_length);
                            }
                        }
                    }
                }
            }
        }

        // If these points make up a square, return an array holding
        // them in an order that makes a square.
        // If the points don't make up a square, return null.
        private int[] GetSquarePoints(int i, int j, int k, int m)
        {
            // A small value for equality testing.
            const double tiny = 0.001;

            // Store all but the first index in an array.
            int[] indexes = { j, k, m };

            // Get the distances from point i to the others.
            float[] distances =
            {
                PointFDistance(Points[i], Points[j]),
                PointFDistance(Points[i], Points[k]),
                PointFDistance(Points[i], Points[m]),
            };

            // Sort the distances and the corresponding indexes.
            Array.Sort(distances, indexes);

            // If the two smaller distances are not roughly
            // the same (the side length), then this isn't a square.
            if (Math.Abs(distances[0] - distances[1]) > tiny) return null;

            // If the longer distance isn't roughly Sqr(2) times
            // the side length (the diagonal length), then this isn't a square.
            float diagonal_length = (float)(Math.Sqrt(2) * distances[0]);
            if (Math.Abs(distances[2] - diagonal_length) > tiny) return null;

            // See if the distance between the farther point and
            // the two closer points is roughly the side length.
            float distance1 = PointFDistance(Points[indexes[2]], Points[indexes[0]]);
            if (Math.Abs(distances[0] - distance1) > tiny) return null;
            float distance2 = PointFDistance(Points[indexes[2]], Points[indexes[1]]);
            if (Math.Abs(distances[0] - distance2) > tiny) return null;

            // It's a square!
            return new int[] { i, indexes[0], indexes[2], indexes[1] };
        }

        // Return the distance between two PointFs.
        private float PointFDistance(PointF point1, PointF point2)
        {
            float dx = point1.X - point2.X;
            float dy = point1.Y - point2.Y;
            return (float)Math.Sqrt(dx * dx + dy * dy);
        }

        // Draw the circles and any squares currently defined.
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
            }
            else
            {
                // Draw the current solution.
                DrawSolution(e.Graphics, CurrentSolution);
                if (CurrentSolution < Solutions.Count)
                    lblResults.Text = "Square " + (CurrentSolution + 1).ToString();
            }
        }

        // Draw a solution.
        private void DrawSolution(Graphics gr, int solution_num)
        {
            if (solution_num >= Solutions.Count) return;

            // Make a list of the points in this solution.
            List<PointF> pts = new List<PointF>();
            foreach (int i in Solutions[solution_num]) pts.Add(Points[i]);

            // Get the side length.
            int side_length = (int)PointFDistance(pts[0], pts[1]);
            int index = SideLengths.IndexOf(side_length);

            // Make an appropriately colored brush and pen.
            Color fill_color = Color.FromArgb(64,
                Colors[index].R,
                Colors[index].G,
                Colors[index].B);
            using (Brush brush = new SolidBrush(fill_color))
            {
                gr.FillPolygon(brush, pts.ToArray());
            }

            using (Pen pen = new Pen(Colors[index], 0))
            {
                gr.DrawPolygon(pen, pts.ToArray());
            }
        }

        // Start showing solutions.
        private void btnShowSolutions_Click(object sender, EventArgs e)
        {
            // Disable the button.
            btnShowSolutions.Enabled = false;

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
            if (!tmrChangeSolution.Enabled)
            {
                btnShowSolutions.Enabled = true;
                lblResults.Text = "";
            }

            // Redraw.
            Refresh();
        }

        // Show all of the solutions.
        private void btnShowAllSolutions_Click(object sender, EventArgs e)
        {
            CurrentSolution = -1;
            tmrChangeSolution.Enabled = false;
            btnShowSolutions.Enabled = true;

            // Display the number of solutions.
            lblResults.Text = Solutions.Count.ToString() + " squares";

            // Redraw.
            Refresh();
        }
    }
}
