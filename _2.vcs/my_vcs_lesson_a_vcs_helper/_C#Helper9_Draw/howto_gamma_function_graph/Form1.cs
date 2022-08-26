using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;
using System.Drawing.Text;

namespace howto_gamma_function_graph
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }


        private void btnDraw_Click(object sender, EventArgs e)
        {
            DrawGraph();
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            DrawGraph();
        }
        private void DrawGraph()
        {
            Cursor = Cursors.WaitCursor;
            picCanvas.Image = null;
            picCanvas.Refresh();

            int wid = picCanvas.ClientSize.Width;
            int hgt = picCanvas.ClientSize.Height;

            float wxmin = float.Parse(txtXmin.Text);
            float wxmax = float.Parse(txtXmax.Text);
            float wymin = float.Parse(txtYmin.Text);
            float wymax = float.Parse(txtYmax.Text);
            float dx = float.Parse(txtDx.Text);

            Bitmap bm = new Bitmap(wid, hgt);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.SmoothingMode = SmoothingMode.AntiAlias;
                gr.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;

                float dxmin = 0;
                float dxmax = picCanvas.ClientSize.Width - 1;
                float dymin = 0;
                float dymax = picCanvas.ClientSize.Height - 1;
                Matrix transform, inverse;
                gr.MakeTransforms(
                    wxmin, wymin, wxmax, wymax,
                    dxmin, dymin, dxmax, dymax,
                    false, out transform, out inverse);

                Font font = this.Font;
                // X axis.
                gr.WDrawLine(transform, Pens.Black,
                    wxmin - 100, 0, wxmax + 100, 0);
                using (StringFormat sf = new StringFormat())
                {
                    sf.Alignment = StringAlignment.Center;
                    sf.LineAlignment = StringAlignment.Near;
                    float xstep = SmallerPowerOfTen(Math.Max(wxmax, wxmin));
                    if (xstep < 1) xstep = 1;
                    float xstart = xstep * (int)(wxmin / xstep);
                    for (float x = xstart; x <= wxmax; x += xstep)
                    {
                        if (Math.Abs(x) > 0.5)
                        {
                            gr.WDrawTick(transform, Pens.Black,
                                new PointF(x, 0), 0, 5);
                            gr.WDrawString(transform, x.ToString(),
                                font, Brushes.Black,
                                new PointF(x, 0), 0, 5, sf);
                        }
                    }
                }

                // Y axis.
                gr.WDrawLine(transform, Pens.Black,
                    0, wymin - 100, 0, wymax + 100);
                using (StringFormat sf = new StringFormat())
                {
                    sf.Alignment = StringAlignment.Far;
                    sf.LineAlignment = StringAlignment.Center;
                    float ystep = SmallerPowerOfTen(Math.Max(wymax, wymin));
                    float ystart = ystep * (int)(wymin / ystep);
                    for (float y = ystart; y <= wymax; y += ystep)
                    {
                        if (Math.Abs(y) > 0.5)
                        {
                            gr.WDrawTick(transform, Pens.Black,
                                new PointF(0, y), 5, 0);
                            gr.WDrawString(transform, y.ToString(),
                                font, Brushes.Black,
                                new PointF(0, y), -3, 0, sf);
                        }
                    }
                }

                // Plot the numerically integrated gamma function.
                PlotCurve(gr, transform, Pens.Red, Gamma, wxmin, wxmax, dx);

                // Plot MyGamma
                PlotCurve(gr, transform, Pens.Green, MyGammaDouble, wxmin, wxmax, dx);

                // Plot integral factorials.
                int imin = (int)wxmin;
                if (imin < 1) imin = 1;
                for (int x = imin; x <= wxmax; x++)
                {
                    float y = (float)Factorial(x - 1);
                    if (y < 10000)
                    {
                        gr.WPlotPoint(transform,
                            Brushes.LightGreen, Pens.Green,
                            new PointF(x, y), 4, 4);
                    }
                }
            }
            picCanvas.Image = bm;

            Cursor = Cursors.Default;
        }

        // Return x!.
        private double Factorial(int x)
        {
            double result = 1;
            for (int i = 2; i <= x; i++)
                result *= i;
            return result;
        }

        // Numerically integrate: x^(z-1)*e^(-x) dx
        // from 0 to infinity.
        private double Gamma(double z)
        {
            const double dx = 0.1;
            const int num_slices = 10000;
            double result = 0;
            double x = 0;
            for (int i = 0; i < num_slices; i++)
            {
                double new_term = Math.Pow(x, z - 1) * Math.Exp(-x);
                if (!double.IsNaN(new_term) &&
                    !double.IsInfinity(new_term))
                        result += new_term;
                x += dx;
            }
            return result * dx;
        }

        // Find the largest power of 10 smaller than this value.
        private float SmallerPowerOfTen(float x)
        {
            int power = (int)Math.Floor(Math.Log10(x));
            float result = (float)Math.Pow(10, power);
            if (result < 0.1f) result = 0.1f;
            return result;
        }

        // See the response by woodmage at:
        // https://stackoverflow.com/questions/51789669/is-there-mathematical-gamma-function-in-c
        // See also:
        // https://rosettacode.org/wiki/Gamma_function#C.23
        // https://en.wikipedia.org/wiki/Lanczos_approximation
        private static int g = 7;
        private static double[] p =
        {
            0.99999999999980993,
            676.5203681218851,
            -1259.1392167224028,
	        771.32342877765313,
            -176.61502916214059,
            12.507343278686905,
	        -0.13857109526572012,
            9.9843695780195716e-6,
            1.5056327351493116e-7
        };
        private double MyGammaDouble(double z)
        {
            if (z < 0.5)
                return Math.PI / (Math.Sin(Math.PI * z) * MyGammaDouble(1 - z));
            z -= 1;
            double x = p[0];
            for (var i = 1; i < g + 2; i++)
                x += p[i] / (z + i);
            double t = z + g + 0.5;
            return Math.Sqrt(2 * Math.PI) * (Math.Pow(t, z + 0.5)) * Math.Exp(-t) * x;
        }

        private void PlotCurve(Graphics gr, Matrix transform,
            Pen pen, Func<double, double> function,
            double xmin, double xmax, double dx)
        {
            const double ymin = -10000;
            const double ymax = 10000;

            List<PointF> points = new List<PointF>();
            double last_y = function(xmin);
            for (double x = xmin; x <= xmax; x += dx)
            {
                // Calculate y.
                double y = function(x);
                if (y < ymin) y = ymin;
                if (y > ymax) y = ymax;

                // If y changed by too much, draw whatever we have.
                if (Math.Abs(y - last_y) > 1000)
                {
                    if (points.Count > 1)
                    {
                        gr.WDrawLines(transform, pen, points.ToArray());
                    }
                    points.Clear();
                }
                points.Add(new PointF((float)x, (float)y));
                last_y = y;
            }

            // Draw any remaining points.
            if (points.Count > 1)
            {
                gr.WDrawLines(transform, pen, points.ToArray());
            }
        }
    }
}
