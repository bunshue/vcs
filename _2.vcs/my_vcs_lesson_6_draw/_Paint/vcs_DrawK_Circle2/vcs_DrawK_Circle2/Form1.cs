using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace vcs_DrawK_Circle2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // A rectangle that define the circle.
        private bool GotCircle = false;
        private Rectangle Circle;

        // Used while drawing circles.
        private bool DrawingCircle = false;
        private int StartX, StartY, EndX, EndY;

        // The circle's equation.
        private float Dx, Dy, R;

        private void Form1_Load(object sender, EventArgs e)
        {
            this.DoubleBuffered = true;
        }

        // Draw the circle.
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(this.BackColor);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the circle if we have one.
            if (GotCircle)
            {
                // Fill the circle.
                e.Graphics.FillEllipse(Brushes.LightBlue, Circle);

                // Plot the circle's equation.
                List<PointF> points = new List<PointF>();
                for (float x = Dx - R; x <= Dx + R; x++)
                {
                    float radicand = x - Dx;
                    radicand = R * R - radicand * radicand;
                    if (radicand >= 0f)
                    {
                        points.Add(new PointF(
                            x, (float)(Dy + Math.Sqrt(radicand))));
                    }
                }
                for (float x = Dx + R; x >= Dx - R; x--)
                {
                    float radicand = x - Dx;
                    radicand = R * R - radicand * radicand;
                    if (radicand > 0f)
                    {
                        points.Add(new PointF(
                            x, (float)(Dy - Math.Sqrt(radicand))));
                    }
                }
                e.Graphics.DrawPolygon(Pens.Blue, points.ToArray());
            }

            // Draw the new circle if we are drawing one.
            if (DrawingCircle)
            {
                // Make it a circle.
                int diameter = Math.Max(Math.Abs(StartX - EndX), Math.Abs(StartY - EndY));
                e.Graphics.DrawEllipse(Pens.Red, Math.Min(StartX, EndX), Math.Min(StartY, EndY), diameter, diameter);
                e.Graphics.DrawRectangle(Pens.Red, Math.Min(StartX, EndX), Math.Min(StartY, EndY), diameter, diameter);
            }
        }

        // Let the user click and drag to select a circle.
        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            DrawingCircle = true;
            GotCircle = false;

            StartX = e.X;
            StartY = e.Y;
            EndX = e.X;
            EndY = e.Y;
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            this.Text = e.X.ToString() + ", " + e.Y.ToString();

            // Do nothing if we are not drawing.
            if (!DrawingCircle)
                return;

            EndX = e.X;
            EndY = e.Y;

            // Redraw.
            this.Refresh();
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            // Do nothing if we are not drawing.
            if (!DrawingCircle) return;

            EndX = e.X;
            EndY = e.Y;

            // Make sure the circle has non-zero width and height.
            if ((StartX != EndX) && (StartY != EndY))
            {
                richTextBox1.Text += "Down : \t(" + StartX.ToString() + ", " + StartY.ToString() + ")\n";
                richTextBox1.Text += "Up :   \t(" + EndX.ToString() + ", " + EndY.ToString() + ")\n";

                // Make it a circle.
                int circle_radius = Math.Max(
                    Math.Abs(StartX - EndX), Math.Abs(StartY - EndY));
                Circle = new Rectangle(
                    Math.Min(StartX, EndX), Math.Min(StartY, EndY),
                    circle_radius, circle_radius);
                GotCircle = true;

                // Find and display the circle's formula.
                richTextBox1.Text += "矩形 (" + Circle.X.ToString() + ", " + Circle.Y.ToString() + ", " + Circle.Size.Width.ToString() + ", " + Circle.Size.Height.ToString() + "\n";
                GetCircleFormula(Circle, out Dx, out Dy, out R);
                richTextBox1.Text += "圓心 (" + Dx.ToString() + ", " + Dy.ToString() + "), 半徑 = " + R.ToString() + "\n";
            }

            // We are no longer drawing a new circle.
            DrawingCircle = false;

            // Redraw.
            this.Refresh();
        }

        // Get the equation for this circle.
        private void GetCircleFormula(RectangleF rect, out float dx, out float dy, out float r)
        {
            dx = rect.X + rect.Width / 2f;
            dy = rect.Y + rect.Height / 2f;
            r = rect.Width / 2f;
        }
    }
}
