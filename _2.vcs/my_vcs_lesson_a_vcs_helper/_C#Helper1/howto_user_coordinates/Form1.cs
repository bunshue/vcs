using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace howto_user_coordinates
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The user's ellipses.
        private List<RectangleF> Ellipses = new List<RectangleF>();
        private List<Color> Colors = new List<Color>();

        // Used while drawing a new ellipse.
        private bool Drawing = false;
        private PointF StartPoint, EndPoint;

        private const float DrawingScale = 50;

        // The world coordinate bounds.
        private float Wxmin=0;
        private float Wxmax=200;
        private float Wymin=0;
        private float Wymax=200;

        private void Form1_Resize(object sender, EventArgs e)
        {
            picCanvas.Refresh();
        }

        // Draw.
        private void picCanvas_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Use a pen that isn't scaled.
            using (Pen thin_pen = new Pen(Color.Black, 0))
            {
                // Draw the axes.
                float tic = 0.25f;
                thin_pen.Width = 2 / DrawingScale;
                e.Graphics.DrawLine(thin_pen, Wxmin, 0, Wxmax, 0);
                for (int x = (int)Wxmin; x <= Wxmax; x++)
                    e.Graphics.DrawLine(thin_pen, x, -tic, x, tic);
                e.Graphics.DrawLine(thin_pen, 0, Wymin, 0, Wymax);
                for (int y = (int)Wymin; y <= Wymax; y++)
                    e.Graphics.DrawLine(thin_pen, -tic, y, tic, y);

                // Draw the ellipses.
                thin_pen.Width = 0;
                for (int i = 0; i < Ellipses.Count; i++)
                {
                    using (Brush brush = new SolidBrush(Color.FromArgb(128, Colors[i])))
                    {
                        e.Graphics.FillEllipse(brush, Ellipses[i]);
                    }
                    thin_pen.Color = Colors[i];
                    e.Graphics.DrawEllipse(thin_pen, Ellipses[i]);
                }

                // Draw the new ellipse.
                if (Drawing)
                {
                    thin_pen.Color = Color.Black;
                    e.Graphics.DrawEllipse(thin_pen,
                        Math.Min(StartPoint.X, EndPoint.X),
                        Math.Min(StartPoint.Y, EndPoint.Y),
                        Math.Abs(StartPoint.X - EndPoint.X),
                        Math.Abs(StartPoint.Y - EndPoint.Y));
                }
            }
        }

        // Let the user draw a new ellipse.
        private void picCanvas_MouseDown(object sender, MouseEventArgs e)
        {
            Drawing = true;

            // Get the start and end points.
            StartPoint = DeviceToWorld(e.Location);
            EndPoint = StartPoint;
        }

        private void picCanvas_MouseMove(object sender, MouseEventArgs e)
        {
            if (!Drawing) return;

            // Get the end point.
            EndPoint = DeviceToWorld(e.Location);
            Refresh();
        }

        private void picCanvas_MouseUp(object sender, MouseEventArgs e)
        {
            if (!Drawing) return;
            Drawing = false;

            // Get the end point.
            EndPoint = DeviceToWorld(e.Location);

            // If the ellipse has non-zero size, add it to the list.
            if ((StartPoint.X != EndPoint.X) && (StartPoint.Y != EndPoint.Y))
            {
                Ellipses.Add(new RectangleF(
                    Math.Min(StartPoint.X, EndPoint.X),
                    Math.Min(StartPoint.Y, EndPoint.Y),
                    Math.Abs(StartPoint.X - EndPoint.X),
                    Math.Abs(StartPoint.Y - EndPoint.Y)));
                Colors.Add(RandomColor());
            }

            Refresh();
        }

        // Convert from device coordinates to world coordinates.
        private PointF DeviceToWorld(PointF point)
        {
            PointF[] points = { point };
            return points[0];
        }

        // Return a random color.
        private Random rand = new Random();
        private Color[] RandomColors =
        {
            Color.Red,
            Color.ForestGreen,
            Color.Blue,
            Color.BlueViolet,
            Color.Cyan,
            Color.DeepPink,
            Color.DarkOrange,
            Color.Maroon,
            Color.Purple,
            Color.SaddleBrown,
        };
        private Color RandomColor()
        {
            return RandomColors[rand.Next(0, RandomColors.Length)];
        }
    }
}
