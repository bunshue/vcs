using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace howto_graph_pi_approximations
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Redraw the graph.
        private void picGraph_Resize(object sender, EventArgs e)
        {
            picGraph.Refresh();
        }

        // Draw the graph.
        private void picGraph_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            DrawGraph(e.Graphics, 10);
        }

        // Draw the graph on a Graphics object.
        private void DrawGraph(Graphics gr, int num_terms)
        {
            // Calculate the approximation values.
            double[] values = new double[num_terms];
            double four = 4;
            double pi = 0;
            for (int i = 0; i < num_terms; i++)
            {
                pi += four / (2 * i + 1);
                values[i] = pi;
                four = -four;
            }

            // Set up a transformation to fit
            // the graph to the PictureBox.
            RectangleF rect = new RectangleF(-0.5f, 1.75f, num_terms - 1, 2.5f);
            PointF[] points =
            {
                new PointF(0, picGraph.ClientSize.Height),
                new PointF(picGraph.ClientSize.Width, picGraph.ClientSize.Height),
                new PointF(0, -0.5f),
            };
            Matrix transform = new Matrix(rect, points);

            // Draw labels.
            using (StringFormat sf = new StringFormat())
            {
                // Label the Y axis.
                sf.Alignment = StringAlignment.Far;
                sf.LineAlignment = StringAlignment.Center;
                using (Font font = new Font("Times New Roman", 12))
                {
                    for (int y = 2; y <= 4; y++)
                    {
                        // See where this point will be after it is transformed.
                        PointF[] txt_pts = { new PointF(-0.25f, y) };
                        transform.TransformPoints(txt_pts);
                        gr.DrawString(y.ToString(), font,
                            Brushes.Black, txt_pts[0].X, txt_pts[0].Y, sf);
                    }

                    // Draw the key.
                    float text_x = 135;
                    float text_y = 300;
                    float line_space = font.Size * 2;
                    gr.DrawString("Gregory-Leibniz", font,
                        Brushes.Green, text_y, text_x);
                    text_x += line_space;

                    gr.DrawString("Nilakantha", font,
                        Brushes.Red, text_y, text_x);
                    text_x += line_space;

                    gr.DrawString("Newton", font,
                        Brushes.Blue, text_y, text_x);
                    text_x += line_space;

                    gr.DrawString("Arcsine", font,
                        Brushes.Black, text_y, text_x);
                    text_x += line_space;
                } // Font

                // Label pi.
                sf.Alignment = StringAlignment.Near;
                sf.LineAlignment = StringAlignment.Far;
                using (Font font = new Font("Times New Roman", 16))
                {
                    PointF[] pi_pts = { new PointF(0, (float)Math.PI) };
                    transform.TransformPoints(pi_pts);
                    gr.DrawString("π", font,
                        Brushes.Black, pi_pts[0].X, pi_pts[0].Y, sf);
                } // Font
            } // StringFormat

            // Draw the rest in the transformed coordinates.
            gr.Transform = transform;

            // Use an unscaled pen.
            using (Pen thin_pen = new Pen(Color.Lime, 0))
            {
                // Draw the line y = pi.
                gr.DrawLine(thin_pen, 0, (float)Math.PI,
                    num_terms, (float)Math.PI);

                // Draw the Y axis.
                thin_pen.Color = Color.Gray;
                gr.DrawLine(thin_pen, 0, -1, 0, 5);
                for (int y = 1; y <= 4; y++)
                {
                    gr.DrawLine(thin_pen, -0.25f, y, 0.25f, y);
                }

                // Draw the X tic marks.
                thin_pen.Color = Color.Gray;
                float y0 = (float)Math.PI - 0.05f;
                float y1 = (float)Math.PI + 0.05f;
                for (int x = 1; x <= num_terms; x++)
                {
                    gr.DrawLine(thin_pen, x, y0, x, y1);
                }

                // Draw the approximations.
                thin_pen.Color = Color.Green;
                PointF[] pts = new PointF[num_terms];
                for (int i = 0; i < num_terms; i++)
                {
                    pts[i] = new PointF(i, (float)values[i]);
                }
                gr.DrawCurve(thin_pen, pts);

                // Draw Nilakantha's approximation.
                thin_pen.Color = Color.Red;
                pts = new PointF[num_terms];
                for (int i = 0; i < num_terms; i++)
                {
                    pts[i] = new PointF(i, (float)NilakanthaPi(i));
                }
                gr.DrawCurve(thin_pen, pts);

                // Draw Newton's approximation.
                thin_pen.Color = Color.Blue;
                pts = new PointF[num_terms];
                for (int i = 0; i < num_terms; i++)
                {
                    pts[i] = new PointF(i, (float)Pi(i));
                }
                gr.DrawCurve(thin_pen, pts);

                // Draw the arcsine approximation.
                thin_pen.Color = Color.Black;
                pts = new PointF[num_terms];
                for (int i = 0; i < num_terms; i++)
                {
                    pts[i] = new PointF(i, (float)ArcsinePi(i));
                }
                gr.DrawCurve(thin_pen, pts);
            } // Pen
        }

        // Calculate the term_index-th term for the pi approximation.
        // Term 1 has index 0.
        private double PiTerm(int term_index)
        {
            return 4 * Math.Pow(-1, term_index) / (2 * term_index + 1);
        }

        #region Newton's approximation

        // Pi/2 = Sum(k!/(2k+1)!!)
        private double Pi(int num_terms)
        {
            double result = 0;
            for (int k = 0; k < num_terms; k++)
                result += Factorial(k) / OddProd(2 * k + 1);
            return result * 2;
        }

        // Return n!
        private double Factorial(long n)
        {
            double result = 1;
            for (long i = 2; i <= n; i++) result *= i;
            return result;
        }

        // Return the product of the odd integers up to the number.
        private double OddProd(long n)
        {
            double result = 1;
            for (long i = 3; i <= n; i += 2) result *= i;
            return result;
        }

        #endregion Newton's approximation

        #region Nilakantha

        // Nilakantha series.
        // Pi/2 = Sum(-1^k/(2k+2)(2k+3)(2k+4))
        private double NilakanthaPi(int num_terms)
        {
            double result = 0;
            double sign = 1;
            for (int i = 0; i < num_terms; i++)
            {
                result += sign / (2 * i + 2) / (2 * i + 3) / (2 * i + 4);
                sign = -sign;
            }
            return 3 + result * 4;
        }

        #endregion Nilakantha

        #region Arcsine

        // Arcsine series.
        // Pi = Sum(3*(2n choose n) / 16^n (2*n+1))
        private double ArcsinePi(int num_terms)
        {
            double result = 0;
            for (int i = 0; i < num_terms; i++)
                result += 3 * Choose(2 * i, i)
                    / Math.Pow(16, i)
                    / (2 * i + 1);
            return result;
        }

        // Return n choose k.
        private double Choose(int n, int k)
        {
            double result = 1;
            for (int i = 1; i <= k; i++)
            {
                result *= n - (k - i);
                result /= i;
            }
            return result;
        }

        #endregion Arcsine

    }
}
