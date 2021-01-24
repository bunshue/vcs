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
        private const float Xmax =   1.0f;
        private const float Ymin = -10.0f;
        private const float Ymax = 350.0f;
        private Matrix DrawingTransform, InverseTransform;

        private bool HasSolution = false;
        private double BestA, BestB, BestC, BestD;
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

            //// Start with some test data.
            //Points.Add(new PointF(0.20f, 138.8f));
            //Points.Add(new PointF(0.30f, 210.9f));
            //Points.Add(new PointF(0.40f, 260.2f));
            //Points.Add(new PointF(0.45f, 277.5f));
            //Points.Add(new PointF(0.50f, 294.1f));
            //Points.Add(new PointF(0.55f, 302.4f));
            //Points.Add(new PointF(0.60f, 311.4f));
            //Points.Add(new PointF(0.65f, 318.5f));
            //Points.Add(new PointF(0.70f, 326.4f));
            //Points.Add(new PointF(0.75f, 333.1f));
            //Points.Add(new PointF(0.80f, 336.7f));
            //Points.Add(new PointF(0.85f, 339.0f));
            //Points.Add(new PointF(0.90f, 342.2f));
            //Points.Add(new PointF(0.95f, 343.0f));

            // Pretty up the equation.
            rchEquation.Select(9, 4);
            rchEquation.SelectionCharOffset = 10;
            rchEquation.Select(13, 1);
            rchEquation.SelectionCharOffset = 20;
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
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Use the drawing transformation.
            e.Graphics.Transform = DrawingTransform;

            // Draw the axes.
            DrawAxes(e.Graphics);

            // Draw the curve.
            if (HasSolution)
            {
                const double Xstep = 0.01;
                double x0 = Xmin;
                double y0 = CurveFunctions.F(Xmin, BestA, BestB, BestC, BestD);
                using (Pen thin_pen = new Pen(Color.Blue, 0))
                {
                    for (double x = Xmin + Xstep; x <= Xmax; x += Xstep)
                    {
                        double y1 = CurveFunctions.F(x, BestA, BestB, BestC, BestD);
                        try
                        {
                            e.Graphics.DrawLine(thin_pen,
                                (float)x0, (float)y0, (float)x, (float)y1);
                        }
                        catch
                        {
                        }
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
            const float xthick = 0.025f;
            const float ythick = 10f;
            const float xstep = 0.25f;
            const float ystep = 20f;

            using (Pen thin_pen = new Pen(Color.Black, 0))
            {
               
                gr.DrawLine(thin_pen, Xmin, 0, Xmax, 0);
                for (float x = xstep; x < Xmax; x += xstep)
                {
                    gr.DrawLine(thin_pen, x, -ythick, x, ythick);
                }

                gr.DrawLine(thin_pen, 0, Ymin, 0, Ymax);
                for (float y = ystep; y < Ymax; y += ystep)
                {
                    gr.DrawLine(thin_pen, -xthick, y, xthick, y);
                }
            }

            // Draw axis labels.
            gr.ResetTransform();

            // Transform the points where we need to draw.
            List<PointF> pt_list;
            PointF[] pts;

            // Y axis labels.
            pt_list = new List<PointF>();
            for (float y = 100; y <= Ymax; y += 100)
            {
                pt_list.Add(new PointF(Xmin, y));
            }
            pts = pt_list.ToArray();
            DrawingTransform.TransformPoints(pts);
            using (StringFormat string_format = new StringFormat())
            {
                string_format.Alignment = StringAlignment.Near;
                string_format.LineAlignment = StringAlignment.Center;
                int i = 0;
                for (float y = 100; y <= Ymax; y += 100)
                {
                    gr.DrawString(y.ToString(), this.Font, Brushes.Black,
                        pts[i].X, pts[i].Y, string_format);
                    i++;
                }
            }

            // X axis labels.
            pt_list = new List<PointF>();
            for (float x = xstep; x <= Xmax; x += xstep)
            {
                pt_list.Add(new PointF(x, 0));
            }
            pts = pt_list.ToArray();
            DrawingTransform.TransformPoints(pts);
            using (StringFormat string_format = new StringFormat())
            {
                string_format.Alignment = StringAlignment.Center;
                string_format.LineAlignment = StringAlignment.Far;
                int i = 0;
                for (float x = xstep; x <= Xmax; x += xstep)
                {
                    gr.DrawString(x.ToString(), this.Font, Brushes.Black,
                        pts[i].X, pts[i].Y, string_format);
                    i++;
                }
            }

            // Use the drawing transformation again.
            gr.Transform = DrawingTransform;
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
            txtD.Clear();
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
            txtD.Clear();
            txtError.Clear();
            txtPercentError.Clear();
            Application.DoEvents();
            DateTime start_time = DateTime.Now;

            // Find a good fit.
            // The final parameter, num_steps, determines how many initial
            // values are tested for a, b, c, and d. For example, if num_steps = 4,
            // then a, b, c, and d each take on 4 values for 4 ^ 4 = 256 initial points.
            double error = CurveFunctions.FindGoodFit(Points,
                out BestA, out BestB, out BestC, out BestD,
                5, 50);

            DateTime stop_time = DateTime.Now;
            TimeSpan elapsed = stop_time - start_time;
            Console.WriteLine("Time: " +
                elapsed.TotalSeconds.ToString("0.00") + " seconds");

            txtA.Text = BestA.ToString();
            txtB.Text = BestB.ToString();
            txtC.Text = BestC.ToString();
            txtD.Text = BestD.ToString();

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
            BestD = double.Parse(txtD.Text);
            ShowError();
            picGraph.Refresh();
        }

        // Display the error.
        private void ShowError()
        {
            // Get the error.
            double error = Math.Sqrt(CurveFunctions.ErrorSquared(
                Points, BestA, BestB, BestC, BestD));
            txtError.Text = error.ToString();

            // Get the total of the function's values to
            // calculate a percentage.
            double total = 0;
            foreach (PointF pt in Points)
            {
                total += CurveFunctions.F(pt.X, BestA, BestB, BestC, BestD);
            }
            total = error / total * 100;
            txtPercentError.Text = total.ToString();
        }
    }
}
