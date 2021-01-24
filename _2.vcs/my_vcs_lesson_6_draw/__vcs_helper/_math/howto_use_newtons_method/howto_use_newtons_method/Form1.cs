using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

// See Eric W. Weisstein's article "Newton's Method."
// From MathWorld--A Wolfram Web Resource. 
// http://mathworld.wolfram.com/NewtonsMethod.html 

namespace howto_use_newtons_method
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Redraw when resized.
        private void Form1_Load(object sender, EventArgs e)
        {
            this.ResizeRedraw = true;

            // Dont't resize when the font changes size.
            this.AutoScaleMode = AutoScaleMode.None;

            // Set the initial transformation.
            SetTransformation();
        }

        // The transformation.
        private Matrix transformation;
        private float xmax, ymax;

        // Set up a transformation to draw everything nicely.
        private void Form1_Resize(object sender, EventArgs e)
        {
            SetTransformation();
        }
        private void SetTransformation()
        {
            // Scale.
            xmax = 10;
            ymax = 10;
            float scale = Math.Min(
                this.ClientSize.Width / xmax / 2,
                this.ClientSize.Height / ymax / 2);

            xmax = this.ClientSize.Width / scale;
            ymax = this.ClientSize.Height / scale;

            transformation = new Matrix();
            transformation.Scale(scale, scale, MatrixOrder.Append);
            transformation.Translate(
                this.ClientSize.Width / 2,
                this.ClientSize.Height / 2,
                MatrixOrder.Append);
        }

        // The function.
        private float F(float x)
        {
            return -(x * x * x / 3 - 2 * x * x + 5);
        }

        // The function's derivative.
        private float dFdx(float x)
        {
            return -(x * x - 4 * x);
        }

        // The most recent point clicked.
        private float X0 = 1, Y0 = 0;

        // Find a root starting at the clicked position.
        private void Form1_MouseClick(object sender, MouseEventArgs e)
        {
            // Convert the mouse's X coordinate into world coordinates.
            Matrix m = transformation.Clone();
            m.Invert();
            PointF[] pts = { new PointF(e.X, e.Y) };
            m.TransformPoints(pts);
            X0 = pts[0].X;
            Y0 = pts[0].Y;

            // Redraw.
            this.Invalidate();
        }

        // Draw the underlying graph.
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            if (transformation == null) return;
            e.Graphics.Transform = transformation;
            DrawGraph(e.Graphics);
        }
        private void DrawGraph(Graphics gr)
        {
            gr.SmoothingMode = SmoothingMode.AntiAlias;
            gr.Clear(this.BackColor);

            // Make a font that isn't too huge.
            this.Font = new Font("Arial", 1, GraphicsUnit.World);

            // Draw the axes.
            using (Pen axis_pen= new Pen(Color.Blue, 0))
            {
                for (int x = (int)(-xmax); x <= xmax; x++)
                {
                    gr.DrawLine(axis_pen, x, -0.5f, x, 0.5f);
                }
                for (int y = (int)(-ymax); y <= ymax; y++)
                {
                    gr.DrawLine(axis_pen, -0.5f, y, 0.5f, y);
                }
                gr.DrawLine(axis_pen, -xmax, 0, xmax, 0);
                gr.DrawLine(axis_pen, 0, -ymax, 0, ymax);
            }

            // Draw the curve.
            using (Pen curve_pen = new Pen(Color.Green, 0))
            {
                float y1, y2 = F(-10);
                const float step_size = 0.1f;
                for (float x = -xmax + step_size; x <= xmax; x += step_size)
                {
                    y1 = y2;
                    y2 = F(x);
                    gr.DrawLine(curve_pen, x - step_size, y1, x, y2);
                }
            }

            // Draw the point clicked.
            using (Pen point_pen = new Pen(Color.Black, 0))
            {
                gr.DrawLine(point_pen, X0 - 0.25f, Y0 - 0.25f, X0 + 0.25f, Y0 + 0.25f);
                gr.DrawLine(point_pen, X0 - 0.25f, Y0 + 0.25f, X0 + 0.25f, Y0 - 0.25f);
            }

            // Use Newton's method.
            UseNewtonsMethod(gr, X0);
        }

        // Find a root by using Newton's method.
        private void UseNewtonsMethod(Graphics gr, float x0)
        {
            const float cutoff = 0.0000001f;
            const float tiny = 0.00001f;
            const int max_iterations = 100;
            float epsilon;
            int iterations = 0;
            using (StringFormat string_format = new StringFormat())
            {
                string_format.Alignment = StringAlignment.Center;
                using (Pen guess_pen = new Pen(Color.Red, 0))
                {
                    do
                    {
                        // Display this guess x0.
                        iterations++;
                        gr.DrawString(iterations.ToString(),
                            this.Font, Brushes.Black, x0, iterations,
                            string_format);
                        gr.DrawLine(guess_pen, x0, iterations, x0, 0.25f);
                        Console.WriteLine(iterations + ": " + x0);

                        // Make sure x0 isn't on a flat spot.
                        while (Math.Abs(dFdx(x0)) < tiny) x0 += tiny;

                        // Calculate the next esxtimate for x0.
                        epsilon = -F(x0) / dFdx(x0);
                        x0 += epsilon;
                    } while ((Math.Abs(epsilon) > cutoff) && (iterations < max_iterations));
                    gr.FillEllipse(Brushes.Green, x0 - 0.25f, -0.25f, 0.5f, 0.5f);
                }
            }

            this.Text = x0.ToString() + " +/-" +
                epsilon.ToString() + " in " +
                iterations.ToString() + " iterations";
        }
    }
}
