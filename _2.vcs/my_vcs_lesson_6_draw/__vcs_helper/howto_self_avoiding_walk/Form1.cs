using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;
using System.Drawing.Drawing2D;

namespace howto_self_avoiding_walk
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private List<List<Point>> Walks = null;
        private int WalkWidth, WalkHeight;

        private void btnGenerate_Click(object sender, EventArgs e)
        {
            lblResults.Text = "Working...";
            lblWalkNum.Text = "";
            btnGenerate.Enabled = false;
            trkWalk.Visible = false;
            picCanvas.Image = null;
            Cursor = Cursors.WaitCursor;
            Application.DoEvents();

            // Find the walks.
            WalkWidth = int.Parse(txtWidth.Text);
            WalkHeight = int.Parse(txtHeight.Text);
            Stopwatch watch = new Stopwatch();
            watch.Start();
            Walks = FindWalks(WalkWidth, WalkHeight);
            watch.Stop();

            string noun = (Walks.Count == 1 ? " walk " : " walks ");
            lblResults.Text = "Found " +
                Walks.Count.ToString() + noun + "in " +
                watch.Elapsed.TotalSeconds.ToString("0.00") +
                " seconds";

            // Display the first walk.
            if (Walks.Count > 0)
            {
                DisplayWalk(0);
                if (Walks.Count > 1)
                {
                    trkWalk.Maximum = Walks.Count - 1;
                    trkWalk.Value = 0;
                    trkWalk.Visible = true;
                }
            }

            btnGenerate.Enabled = true;
            Cursor = Cursors.Default;
        }

        // Generate all self-avoiding walks.
        private List<List<Point>> FindWalks(int width, int height)
        {
            List<List<Point>> walks = new List<List<Point>>();

            // Make an array to show where we have been.
            bool[,] visited = new bool[width + 1, height + 1];

            // Get the number of points we need to visit.
            int num_points = (width + 1) * (height + 1);

            // Start the walk at (0, 0).
            Stack<Point> current_walk = new Stack<Point>();
            current_walk.Push(new Point(0, 0));
            visited[0, 0] = true;

            // Search for walks.
            FindWalks(num_points, walks, current_walk,
                0, 0, width, height, visited);
            return walks;
        }

        // Extend the walk that is at (current_x, current_y).
        private void FindWalks(int num_points,
            List<List<Point>> walks, Stack<Point> current_walk,
            int current_x, int current_y,
            int width, int height, bool[,] visited)
        {
            // If we have visited every position,
            // then this is a complete walk.
            if (current_walk.Count == num_points)
            {
                walks.Add(current_walk.ToList());

                if (walks.Count % 1000 == 0)
                {
                    lblResults.Text = "... " +
                        walks.Count.ToString() + " ...";
                    Application.DoEvents();
                }
            }
            else
            {
                // Try the possible moves.
                Point[] next_points = new Point[]
                {
                    new Point(current_x - 1, current_y),
                    new Point(current_x + 1, current_y),
                    new Point(current_x, current_y - 1),
                    new Point(current_x, current_y + 1),
                };
                foreach (Point point in next_points)
                {
                    if (point.X < 0) continue;
                    if (point.X > width) continue;
                    if (point.Y < 0) continue;
                    if (point.Y > height) continue;
                    if (visited[point.X, point.Y]) continue;

                    // Try visiting this point.
                    visited[point.X, point.Y] = true;
                    current_walk.Push(point);

                    FindWalks(num_points, walks, current_walk,
                        point.X, point.Y, width, height, visited);

                    // We're done visiting this point.
                    visited[point.X, point.Y] = false;
                    current_walk.Pop();
                }
            }
        }

        // Display the selected walk.
        private void trkWalk_Scroll(object sender, EventArgs e)
        {
            DisplayWalk(trkWalk.Value);
        }
        private void DisplayWalk(int walk_num)
        {
            lblWalkNum.Text = "Walk " + walk_num.ToString();
            using (Pen pen = new Pen(Color.Blue, 2))
            {
                Bitmap bm = DrawWalk(Walks[walk_num],
                    WalkWidth, WalkHeight,
                    picCanvas.ClientSize.Width,
                    picCanvas.ClientSize.Height,
                    Color.White, Brushes.Green, pen);
                picCanvas.Image = bm;
            }
        }

        // Draw a walk.
        private Bitmap DrawWalk(List<Point> walk,
            int width, int height, int bm_width, int bm_height,
            Color bg_color, Brush dot_brush, Pen pen)
        {
            Bitmap bm = new Bitmap(bm_width, bm_height);

            // See how big to make each row and column.
            float scale_x = bm_width / (width + 2);
            float scale_y = bm_height / (height + 2);
            float scale = Math.Min(scale_x, scale_y);
            float offset_x = (bm_width - scale * width) / 2;
            float offset_y = (bm_height - scale * height) / 2;
            float dot_r = scale_x * 0.1f;
            float dot_w = 2 * dot_r;

            // Draw the walk.
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.SmoothingMode = SmoothingMode.AntiAlias;
                gr.Clear(bg_color);

                // Draw a grid of dots.
                for (int x = 0; x <= width; x++)
                {
                    for (int y = 0; y <= height; y++)
                    {
                        gr.FillEllipse(dot_brush,
                            offset_x + x * scale - dot_r,
                            offset_y + y * scale - dot_r,
                            dot_w, dot_w);
                    }
                }

                // Draw the walk.
                if (walk.Count > 1)
                {
                    List<PointF> points = new List<PointF>();
                    foreach (Point point in walk.ToArray())
                    {
                        points.Add(new PointF(
                            offset_x + point.X * scale,
                            offset_y + point.Y * scale));
                    }
                    gr.DrawLines(pen, points.ToArray());
                }
            }

            return bm;
        }
    }
}
