using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;
using System.Drawing.Drawing2D;

namespace howto_rotating_arms
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Geometry.
        private float Ax = 100;
        private float Ay = 150;
        private float Cx = 200;
        private float Cy = 150;
        private float D = 100;
        private float L1 = 100;
        private float L2 = 110;
        private float L3 = 60;
        private float Radius = 30;

        // The wheel's current angle of rotation.
        private const double Dtheta = Math.PI / 10;
        private double Theta = 0;

        // For displaying the current image.
        private Bitmap Picture = null;
        private Graphics Gr;

        // Find the points where the two circles intersect.
        private int FindCircleCircleIntersections(
            float cx0, float cy0, float radius0,
            float cx1, float cy1, float radius1,
            out PointF intersection1, out PointF intersection2)
        {
            // Find the distance between the centers.
            float dx = cx0 - cx1;
            float dy = cy0 - cy1;
            double dist = Math.Sqrt(dx * dx + dy * dy);

            // See how manhym solutions there are.
            if (dist > radius0 + radius1)
            {
                // No solutions, the circles are too far apart.
                intersection1 = new PointF(float.NaN, float.NaN);
                intersection2 = new PointF(float.NaN, float.NaN);
                return 0;
            }
            else if (dist < Math.Abs(radius0 - radius1))
            {
                // No solutions, one circle contains the other.
                intersection1 = new PointF(float.NaN, float.NaN);
                intersection2 = new PointF(float.NaN, float.NaN);
                return 0;
            }
            else if ((dist == 0) && (radius0 == radius1))
            {
                // No solutions, the circles coincide.
                intersection1 = new PointF(float.NaN, float.NaN);
                intersection2 = new PointF(float.NaN, float.NaN);
                return 0;
            }
            else
            {
                // Find a and h.
                double a = (radius0 * radius0 -
                    radius1 * radius1 + dist * dist) / (2 * dist);
                double h = Math.Sqrt(radius0 * radius0 - a * a);

                // Find P2.
                double cx2 = cx0 + a * (cx1 - cx0) / dist;
                double cy2 = cy0 + a * (cy1 - cy0) / dist;

                // Get the points P3.
                intersection1 = new PointF(
                    (float)(cx2 + h * (cy1 - cy0) / dist),
                    (float)(cy2 - h * (cx1 - cx0) / dist));
                intersection2 = new PointF(
                    (float)(cx2 - h * (cy1 - cy0) / dist),
                    (float)(cy2 + h * (cx1 - cx0) / dist));

                // See if we have 1 or 2 solutions.
                if (dist == radius0 + radius1) return 1;
                return 2;
            }
        }

        // Rotate the wheel.
        private void tmrTurnWheel_Tick(object sender, EventArgs e)
        {
            Theta += Dtheta;
            DrawSystem();
            picCanvas.Refresh();
        }

        // Draw everything.
        private void DrawSystem()
        {
            Gr.Clear(this.BackColor);
            Gr.SmoothingMode = SmoothingMode.AntiAlias;

            using (Pen custom_pen = new Pen(Color.Blue, 2))
            {
                // Draw the wheel.
                RectangleF wheel_rect = new RectangleF(
                    Cx - Radius, Cy - Radius,
                    2 * Radius, 2 * Radius);
                Gr.FillEllipse(Brushes.LightBlue, wheel_rect);
                custom_pen.Color = Color.Blue;
                custom_pen.Width = 2;
                Gr.DrawEllipse(custom_pen, wheel_rect);

                // Find the ends of the linkage.
                float linkage_x1 = (float)(Cx + Math.Cos(Theta) * Radius);
                float linkage_y1 = (float)(Cy + Math.Sin(Theta) * Radius);
                PointF pt1, pt2;
                FindCircleCircleIntersections(
                    Ax, Ay, L2,
                    linkage_x1, linkage_y1, L1,
                    out pt1, out pt2);
                float linkage_x2 = pt1.X;
                float linkage_y2 = pt1.Y;

                // Draw the linkage.
                custom_pen.Color = Color.Green;
                custom_pen.Width = 5;
                Gr.DrawLine(custom_pen, linkage_x1, linkage_y1, linkage_x2, linkage_y2);
                custom_pen.Color = Color.Lime;
                custom_pen.Width = 2;
                Gr.DrawLine(custom_pen, linkage_x1, linkage_y1, linkage_x2, linkage_y2);

                // Draw the upper arm.
                custom_pen.Color = Color.Blue;
                custom_pen.Width = 5;
                Gr.DrawLine(custom_pen, Ax, Ay, linkage_x2, linkage_y2);
                custom_pen.Color = Color.LightBlue;
                custom_pen.Width = 2;
                Gr.DrawLine(custom_pen, Ax, Ay, linkage_x2, linkage_y2);

                // Draw the lower arm.
                float dx = Ax - linkage_x2;
                float dy = Ay - linkage_y2;
                double length = Math.Sqrt(dx * dx + dy * dy);
                float lower_x1 = (float)(Ax + dx * L3 / length);
                float lower_y1 = (float)(Ay + dy * L3 / length);
                custom_pen.Color = Color.Blue;
                custom_pen.Width = 5;
                Gr.DrawLine(custom_pen, Ax, Ay, lower_x1, lower_y1);
                custom_pen.Color = Color.LightBlue;
                custom_pen.Width = 2;
                Gr.DrawLine(custom_pen, Ax, Ay, lower_x1, lower_y1);

                // Draw joints.
                Gr.FillEllipse(Brushes.Black, Cx - 4, Cy - 4, 8, 8);
                Gr.FillEllipse(Brushes.Green,
                    linkage_x1 - 4, linkage_y1 - 4, 8, 8);
                Gr.FillEllipse(Brushes.Green,
                    linkage_x2 - 4, linkage_y2 - 4, 8, 8);
                Gr.FillEllipse(Brushes.Black, Ax - 4, Ay - 4, 8, 8);
                Gr.FillEllipse(Brushes.Blue, lower_x1 - 4, lower_y1 - 4, 8, 8);
            }
        }

        // Start or stop the timer.
        private void btnStartStop_Click(object sender, EventArgs e)
        {
            if (btnStartStop.Text == "Start")
            {
                btnStartStop.Text = "Stop";
                D = float.Parse(txtD.Text);
                L1 = float.Parse(txtL1.Text);
                L2 = float.Parse(txtL2.Text);
                L3 = float.Parse(txtL3.Text);
                Cx = Ax + D;
                Radius = float.Parse(txtRadius.Text);
                Theta = 0;
                Picture = new Bitmap(
                    picCanvas.ClientSize.Width,
                    picCanvas.ClientSize.Height);
                Gr = Graphics.FromImage(Picture);
                picCanvas.Image = Picture;

                tmrTurnWheel.Enabled = true;
            }
            else
            {
                btnStartStop.Text = "Start";
                tmrTurnWheel.Enabled = false;
            }
        }
    }
}
