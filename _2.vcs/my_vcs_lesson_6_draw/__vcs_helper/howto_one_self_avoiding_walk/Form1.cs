using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace howto_one_self_avoiding_walk
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The lattice size.
        private int WalkWidth, WalkHeight;

        // Used to pick a random starting vertex.
        private Random Rand = new Random();

        private void btnGenerate_Click(object sender, EventArgs e)
        {
            if (btnGenerate.Text == "Generate")
            {
                // Start generating walks.
                btnGenerate.Text = "Stop";
                picCanvas.Image = null;

                WalkWidth = int.Parse(txtWidth.Text);
                WalkHeight = int.Parse(txtHeight.Text);

                tmrShowWalk.Enabled = true;
            }
            else
            {
                // Stop generating walks.
                btnGenerate.Text = "Generate";
                tmrShowWalk.Enabled = false;
            }
        }

        // Find one random self-avoiding walk.
        private List<Point> FindOneWalk(int width, int height)
        {
            // Make an array to show where we have been.
            bool[,] visited = new bool[width + 1, height + 1];

            // Get the number of points we need to visit.
            int num_points = (width + 1) * (height + 1);

            // Start at a random vertex.
            int x = Rand.Next(0, width + 1);
            int y = Rand.Next(0, height + 1);

            // Start the walk at (0, 0).
            Stack<Point> current_walk = new Stack<Point>();
            current_walk.Push(new Point(x, y));
            visited[x, y] = true;

            // Search for walks.
            List<Point> walk = FindOneWalk(num_points, current_walk,
                x, y, width, height, visited);
            if (walk != null) return walk;
            return current_walk.ToList();
        }

        // Extend the walk that is at (current_x, current_y).
        private List<Point> FindOneWalk(int num_points,
            Stack<Point> current_walk,
            int current_x, int current_y,
            int width, int height, bool[,] visited)
        {
            // If we have visited every position, and the
            // last point is in the lower right corner,
            // then this is a complete walk.
            if (current_walk.Count == num_points)
            {
                return current_walk.ToList();
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

                // Randomize the moves to try.
                next_points.Randomize();

                // Try the moves.
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

                    List<Point> walk = FindOneWalk(num_points, current_walk,
                        point.X, point.Y, width, height, visited);
                    if (walk != null) return walk;

                    // We're done visiting this point.
                    visited[point.X, point.Y] = false;
                    current_walk.Pop();
                }
                return null;
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
                if (walk.Count == 1)
                {
                    RectangleF rect = new RectangleF(
                        offset_x + walk[0].X * scale - 2 * dot_r,
                        offset_y + walk[0].Y * scale - 2 * dot_r,
                        4 * dot_r, 4 * dot_r);
                    gr.DrawEllipse(pen, rect);                            
                }
                else
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

        // Generate and display the next walk.
        private void tmrShowWalk_Tick(object sender, EventArgs e)
        {
            List<Point> walk = FindOneWalk(WalkWidth, WalkHeight);
            if (walk == null)
                picCanvas.Image = null;
            else
            {
                using (Pen pen = new Pen(Color.Blue, 2))
                {
                    Bitmap bm = DrawWalk(walk,
                        WalkWidth, WalkHeight,
                        picCanvas.ClientSize.Width,
                        picCanvas.ClientSize.Height,
                        Color.White, Brushes.Green, pen);
                    picCanvas.Image = bm;
                }
            }
        }

        private void scrSpeed_Scroll(object sender, ScrollEventArgs e)
        {
            tmrShowWalk.Interval = 1000 / scrSpeed.Value;
        }
    }
}
