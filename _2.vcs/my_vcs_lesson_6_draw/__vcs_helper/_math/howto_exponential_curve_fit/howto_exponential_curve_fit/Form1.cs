using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace howto_exponential_curve_fit
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Drawing constants.
        private const float Xmin =  -0.1f;
        private const float Xmax =   4.1f;
        private const float Ymin = -10.0f;
        private const float Ymax = 100.0f;
        private Matrix DrawingTransform;
        private Matrix InverseTransform;

        private bool HasSolution = false;
        private double BestA, BestB, BestC;
        private List<PointF> Points = new List<PointF>();

        // Make a drawing transformation.
        private void Form1_Load(object sender, EventArgs e)
        {
            RectangleF world_rect = new RectangleF(Xmin, Ymin, Xmax - Xmin, Ymax - Ymin);
            PointF[] pts =
            {
                new PointF(0, picGraph.ClientSize.Height),
                new PointF(picGraph.ClientSize.Width, picGraph.ClientSize.Height),
                new PointF(0, 0),
            };
            DrawingTransform = new Matrix(world_rect, pts);
            InverseTransform = DrawingTransform.Clone();
            InverseTransform.Invert();

            rchEquation.Select(9, 2);
            rchEquation.SelectionCharOffset = 15;
        }

        // Save a new point.
        private void picGraph_MouseClick(object sender, MouseEventArgs e)
        {
            // Transform the point to world coordinates.
            PointF[] pts = { new PointF(e.X, e.Y) };
            InverseTransform.TransformPoints(pts);
            // Console.WriteLine(pts[0].ToString());

            // Save the point.
            Points.Add(pts[0]);
            picGraph.Refresh();
        }

        // Draw the points and best fit curve.
        private void picGraph_Paint(object sender, PaintEventArgs e)
        {
            // Use the drawing transformation.
            e.Graphics.Transform = DrawingTransform;
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the axes.
            DrawAxes(e.Graphics);

            // Draw the curve.
            if (HasSolution)
            {
                const double Xstep = 0.01;
                double x0 = Xmin;
                double y0 = CurveFunctions.F(Xmin, BestA, BestB, BestC);
                using (Pen thin_pen = new Pen(Color.Blue, 0))
                {
                    for (double x = Xmin + Xstep; x <= Xmax; x += Xstep)
                    {
                        double y1 = CurveFunctions.F(x, BestA, BestB, BestC);
                        e.Graphics.DrawLine(thin_pen,
                            (float)x0, (float)y0, (float)x, (float)y1);
                        x0 = x;
                        y0 = y1;
                        if (y0 > 1e8) break;
                    }
                }
            }

            // Draw the points.
            const float dx = (Xmax - Xmin) / 100;
            const float dy = (Ymax - Ymin) / 100;
            using (Pen thin_pen = new Pen(Color.Black, 0))
            {
                foreach (PointF pt in Points)
                {
                    e.Graphics.FillRectangle(Brushes.White,
                        pt.X - dx, pt.Y - dy, 2 * dx, 2 * dy);
                    e.Graphics.DrawRectangle(thin_pen,
                        pt.X - dx, pt.Y - dy, 2 * dx, 2 * dy);
                }
            }
        }

        // Draw the axes.
        private void DrawAxes(Graphics gr)
        {
            using (Pen thin_pen = new Pen(Color.Black, 0))
            {
                const float xthick = 0.05f;
                const float ythick = 2f;
                
                gr.DrawLine(thin_pen, Xmin, 0, Xmax, 0);
                for (float x = 0.5f; x < Xmax; x += 0.5f)
                {
                    gr.DrawLine(thin_pen, x, -ythick, x, ythick);
                }

                gr.DrawLine(thin_pen, 0, Ymin, 0, Ymax);
                for (float y = 10f; y < Ymax; y += 10f)
                {
                    gr.DrawLine(thin_pen, -xthick, y, xthick, y);
                }
            }
        }

        // Clear the points.
        private void btnClear_Click(object sender, EventArgs e)
        {
            Points = new List<PointF>();
            HasSolution = false;
            picGraph.Refresh();

            txtA.Clear();
            txtB.Clear();
            txtC.Clear();
            txtError.Clear();
            txtPercentError.Clear();
        }

        // Find parameters for a weibull curve fit.
        private void btnFit_Click(object sender, EventArgs e)
        {
            this.Cursor = Cursors.WaitCursor;
            txtA.Clear();
            txtB.Clear();
            txtC.Clear();
            txtError.Clear();
            txtPercentError.Clear();
            Application.DoEvents();
            DateTime start_time = DateTime.Now;

            // Find a good fit.
            // The final parameter, num_steps, determines how many initial
            // values are tested for a, b, c, and d. For example, if num_steps = 4,
            // then a, b, c, and d each take on 4 values for 4 ^ 4 = 256 initial points.
            double error = CurveFunctions.FindGoodFit(Points,
                out BestA, out BestB, out BestC, 10, 100);

            DateTime stop_time = DateTime.Now;
            TimeSpan elapsed = stop_time - start_time;
            Console.WriteLine("Time: " +
                elapsed.TotalSeconds.ToString("0.00") + " seconds");

            txtA.Text = BestA.ToString();
            txtB.Text = BestB.ToString();
            txtC.Text = BestC.ToString();

            // Display the error.
            ShowError();

            // We have a solution.
            HasSolution = true;
            picGraph.Refresh();

            this.Cursor = Cursors.Default;
        }

        // Regraph with the given parameters.
        private void btnGraph_Click(object sender, EventArgs e)
        {
            BestA = double.Parse(txtA.Text);
            BestB = double.Parse(txtB.Text);
            BestC = double.Parse(txtC.Text);
            ShowError();
            picGraph.Refresh();
        }

        // Display the error.
        private void ShowError()
        {
            // Get the error.
            double error = Math.Sqrt(CurveFunctions.ErrorSquared(
                Points, BestA, BestB, BestC));
            txtError.Text = error.ToString();

            // Get the total of the function's values to
            // calculate a percentage.
            double total = 0;
            foreach (PointF pt in Points)
            {
                total += CurveFunctions.F(pt.X, BestA, BestB, BestC);
            }
            total = error / total * 100;
            txtPercentError.Text = total.ToString();
        }
    }
}
