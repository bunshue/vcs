using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace howto_linear_least_squares
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Drawing constants.
        private const float Xmin = -10.0f;
        private const float Xmax =  10.0f;
        private const float Ymin = -10.0f;
        private const float Ymax =  10.0f;
        private Matrix DrawingTransform;
        private Matrix InverseTransform;

        private bool HasSolution = false;
        private double BestM, BestB;
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
        }

        // Save a new point.
        private void picGraph_MouseClick(object sender, MouseEventArgs e)
        {
            // Transform the point to world coordinates.
            PointF[] pts = { new PointF(e.X, e.Y) };
            InverseTransform.TransformPoints(pts);

            // Save the point.
            Points.Add(pts[0]);
            picGraph.Refresh();
        }

        // Draw the points and best fit curve.
        private void picGraph_Paint(object sender, PaintEventArgs e)
        {
            // Use the drawing transformation.
            e.Graphics.Transform = DrawingTransform;

            // Draw the axes.
            DrawAxes(e.Graphics);

            // Draw the curve.
            if (HasSolution)
            {
                using (Pen thin_pen = new Pen(Color.Blue, 0))
                {
                    double y0 = BestM * Xmin + BestB;
                    double y1 = BestM * Xmax + BestB;
                    e.Graphics.DrawLine(thin_pen,
                        (float)Xmin, (float)y0, (float)Xmax, (float)y1);
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
                const float xthick = 0.2f;
                const float ythick = 0.2f;
                gr.DrawLine(thin_pen, Xmin, 0, Xmax, 0);
                for (float x = Xmin; x <= Xmax; x += 1.0f)
                {
                    gr.DrawLine(thin_pen, x, -ythick, x, ythick);
                }
                gr.DrawLine(thin_pen, 0, Ymin, 0, Ymax);
                for (float y = Ymin; y <= Ymax; y += 1.0f)
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

            txtM.Clear();
            txtB.Clear();
            txtError.Clear();
        }

        // Find parameters for a weibull curve fit.
        private void btnFit_Click(object sender, EventArgs e)
        {
            this.Cursor = Cursors.WaitCursor;
            txtM.Clear();
            txtB.Clear();
            txtError.Clear();
            Application.DoEvents();
            DateTime start_time = DateTime.Now;

            // Find a good fit.
            CurveFunctions.FindLinearLeastSquaresFit(Points, out BestM, out BestB);
            HasSolution = true;

            DateTime stop_time = DateTime.Now;
            TimeSpan elapsed = stop_time - start_time;
            Console.WriteLine("Time: " +
                elapsed.TotalSeconds.ToString("0.00") + " seconds");

            txtM.Text = BestM.ToString();
            txtB.Text = BestB.ToString();

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
            BestM = double.Parse(txtM.Text);
            BestB = double.Parse(txtB.Text);
            ShowError();
            picGraph.Refresh();
        }

        // Display the error.
        private void ShowError()
        {
            // Get the error.
            double error = Math.Sqrt(CurveFunctions.ErrorSquared(
                Points, BestM, BestB));
            txtError.Text = error.ToString();
        }
    }
}
