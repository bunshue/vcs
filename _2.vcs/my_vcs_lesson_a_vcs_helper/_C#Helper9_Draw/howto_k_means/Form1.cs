using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace howto_k_means
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private List<PointF> Seeds = new List<PointF>();
        private List<PointF> Centroids = new List<PointF>();
        private List<PointData> Points = new List<PointData>();
        private int NumSteps = 0;

        private Brush[] PointBrushes =
        {
            Brushes.Pink, Brushes.LightGreen, Brushes.LightBlue, Brushes.Yellow,
            Brushes.Orange, Brushes.Lime, Brushes.Cyan, Brushes.White,
        };
        private Pen[] PointPens =
        {
            Pens.Red, Pens.Green, Pens.Blue, Pens.Black,
            Pens.Red, Pens.Green, Pens.Blue, Pens.Black,
        };
        private Brush[] CentroidBrushes =
        {
            Brushes.Red, Brushes.Green, Brushes.Blue, Brushes.Yellow,
            Brushes.Orange, Brushes.Lime, Brushes.Cyan, Brushes.White,
        };

        private int MaxClusters = 1;
        private void Form1_Load(object sender, EventArgs e)
        {
            MaxClusters = PointBrushes.Length;
        }

        private void picItems_Paint(object sender, PaintEventArgs e)
        {
            const float RADIUS = 4;
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the points.
            foreach (PointData point_data in Points)
            {
                e.Graphics.DrawPoint(point_data.Location,
                    PointBrushes[point_data.ClusterNum % MaxClusters],
                    PointPens[point_data.ClusterNum % MaxClusters], RADIUS);
            }

            // Draw the centroids.
            for (int i = 0; i < Centroids.Count; i++)
            {
                e.Graphics.DrawRect(Centroids[i],
                    CentroidBrushes[i % MaxClusters], Pens.Black, RADIUS);
            }

            // Draw the seeds.
            for (int i = 0; i < Seeds.Count; i++)
            {
                e.Graphics.DrawCross(Color.Black, Color.White,
                    Seeds[i], 2 * RADIUS);
            }
        }

        // Make random points around the seeds.
        private void btnMakePoints_Click(object sender, EventArgs e)
        {
            MakePoints();
        }

        private void MakePoints()
        {
            if (Seeds.Count < 1)
            {
                richTextBox1.Text += "至少要設定一個種子\n";
                return;
            }

            // Clear the Centroids list.
            Centroids.Clear();

            // Make the points.
            Random rand = new Random();
            double max_r = Math.Min(
                picItems.ClientSize.Width,
                picItems.ClientSize.Height) / 6;
            int num_points = int.Parse(txtNumPoints.Text);
            for (int i = 0; i < num_points; i++)
            {
                int seed_num = rand.Next(Seeds.Count);
                double r =
                    max_r * rand.NextDouble() +
                    max_r * rand.NextDouble();
                double theta = rand.Next(360);
                float x = Seeds[seed_num].X + (float)(r * Math.Cos(theta));
                float y = Seeds[seed_num].Y + (float)(r * Math.Sin(theta));
                Points.Add(new PointData(x, y, 0));
            }

            picItems.Refresh();
        }

        private double Score(List<PointF> centroids, List<PointData> points)
        {
            double total = 0;
            foreach (PointData point_data in points)
            {
                total += Distance2(point_data.Location,
                    centroids[point_data.ClusterNum]);
            }
            return total;
        }

        private double Distance2(PointF point1, PointF point2)
        {
            float dx = point1.X - point2.X;
            float dy = point1.Y - point2.Y;
            return dx * dx + dy * dy;
        }
        private double Distance(PointF point1, PointF point2)
        {
            float dx = point1.X - point2.X;
            float dy = point1.Y - point2.Y;
            return Math.Sqrt(dx * dx + dy * dy);
        }

        private void UpdateSolution()
        {
            // Find new centroids.
            int num_clusters = Centroids.Count;
            PointF[] new_centers = new PointF[num_clusters];
            int[] num_points = new int[num_clusters];
            foreach (PointData point in Points)
            {
                double best_dist =
                    Distance(point.Location, Centroids[0]);
                int best_cluster = 0;
                for (int i = 1; i < num_clusters; i++)
                {
                    double test_dist =
                        Distance(point.Location, Centroids[i]);
                    if (test_dist < best_dist)
                    {
                        best_dist = test_dist;
                        best_cluster = i;
                    }
                }
                point.ClusterNum = best_cluster;
                new_centers[best_cluster].X += point.Location.X;
                new_centers[best_cluster].Y += point.Location.Y;
                num_points[best_cluster]++;
            }

            // Calculate the new centroids.
            List<PointF> new_centroids = new List<PointF>();
            for (int i = 0; i < num_clusters; i++)
            {
                new_centroids.Add(new PointF(
                    new_centers[i].X / num_points[i],
                    new_centers[i].Y / num_points[i]));
            }

            // See if the centroids have moved.
            bool centroids_changed = false;
            for (int i = 0; i < num_clusters; i++)
            {
                const float min_change = 0.5f;
                if ((Math.Abs(Centroids[i].X - new_centroids[i].X) > min_change) ||
                    (Math.Abs(Centroids[i].Y - new_centroids[i].Y) > min_change))
                {
                    centroids_changed = true;
                    break;
                }
            }
            if (!centroids_changed)
            {
                tmrUpdate.Enabled = false;
                //System.Media.SystemSounds.Beep.Play();
                lblScore.Text = "Score: " + Score().ToString() +
                    ", # Steps: " + NumSteps.ToString();
                Cursor = Cursors.Default;
                return;
            }

            // Update the centroids.
            Centroids = new_centroids;
        }

        private void btnMakeClusters_Click(object sender, EventArgs e)
        {
            int num_clusters = int.Parse(txtNumClusters.Text);
            if (Points.Count < num_clusters) return;

            // Reset the data.
            // Pick random centroids.
            Centroids = new List<PointF>();
            Points.Randomize();
            for (int i = 0; i < num_clusters; i++)
                Centroids.Add(Points[i].Location);
            foreach (PointData point_data in Points)
                point_data.ClusterNum = 0;

            NumSteps = 0;
            picItems.Refresh();
            lblScore.Text = "";
            Cursor = Cursors.WaitCursor;
            tmrUpdate.Enabled = true;
        }

        private void tmrUpdate_Tick(object sender, EventArgs e)
        {
            NumSteps++;
            UpdateSolution();
            picItems.Refresh();
        }

        private int Score()
        {
            float score = 0;
            foreach (PointData point in Points)
            {
                float dx = Centroids[point.ClusterNum].X - point.Location.X;
                float dy = Centroids[point.ClusterNum].Y - point.Location.Y;
                score += dx * dx + dy * dy;
            }
            return (int)score;
        }

        private void picItems_MouseClick(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
                Seeds.Add(e.Location);
            else
                Points.Add(new PointData(e.Location, 0));
            Centroids.Clear();
            picItems.Refresh();
        }

        private void btnClear_Click(object sender, EventArgs e)
        {
            Seeds.Clear();
            Centroids.Clear();
            Points.Clear();

            picItems.Refresh();
        }

        private void hscrFps_Scroll(object sender, ScrollEventArgs e)
        {
            // Divide by 10 so speed is between 1 and 20.
            int fps = hscrFps.Value / 10;
            if (fps < 1) fps = 1;
            lblFps.Text = fps.ToString();
            tmrUpdate.Interval = 1000 / fps;
        }
    }
}
