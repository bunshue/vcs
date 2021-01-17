using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace howto_graph_pi_approximation
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
            DrawGraph(e.Graphics, 22);
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
            RectangleF rect = new RectangleF(-1, 2.5f, num_terms - 1, 2);
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
                    for (int y = 3; y <= 4; y++)
                    {
                        // See where this point will be after it is transformed.
                        PointF[] txt_pts = { new PointF(-0.25f, y) };
                        transform.TransformPoints(txt_pts);
                        gr.DrawString(y.ToString(), font,
                            Brushes.Black, txt_pts[0].X, txt_pts[0].Y, sf);
                    }
                } // Font

                // Label pi.
                sf.Alignment = StringAlignment.Near;
                sf.LineAlignment = StringAlignment.Far;
                using (Font font = new Font("Times New Roman", 16))
                {
                    PointF[] pi_pts = { new PointF(0.5f, (float)Math.PI) };
                    transform.TransformPoints(pi_pts);
                    gr.DrawString("π", font,
                        Brushes.Black, pi_pts[0].X, pi_pts[0].Y, sf);
                } // Font
            } // StringFormat

            // Draw the rest in the transformed coordinates.
            gr.Transform = transform;

            // Use an unscaled pen.
            using (Pen thin_pen = new Pen(Color.Blue, 0))
            {
                // Draw the line y = pi.
                gr.DrawLine(thin_pen, 0, (float)Math.PI, num_terms, (float)Math.PI);

                // Draw the Y axis.
                thin_pen.Color = Color.Gray;
                gr.DrawLine(thin_pen, 0, -1, 0, 5);
                for (int y = 1; y <= 4; y++)
                {
                    gr.DrawLine(thin_pen, -0.25f, y, 0.25f, y);
                }

                // Draw the approximations.
                thin_pen.Color = Color.Green;
                PointF[] pts = new PointF[num_terms];
                for (int i = 0; i < num_terms; i++)
                {
                    pts[i] = new PointF(i, (float)values[i]);
                }
                gr.DrawCurve(thin_pen, pts);

                // Draw the upper enveloping curve.
                thin_pen.DashStyle = DashStyle.Custom;
                thin_pen.DashPattern = new float[] { 30, 30 };

                thin_pen.Color = Color.Red;
                pts = new PointF[num_terms / 2];
                for (int i = 0; i < num_terms / 2; i++)
                {
                    pts[i] = new PointF(2 * i, (float)values[2 * i]);
                }
                gr.DrawCurve(thin_pen, pts);

                // Draw the lower enveloping curve.
                pts = new PointF[num_terms / 2];
                for (int i = 0; i < num_terms / 2; i++)
                {
                    pts[i] = new PointF(2 * i + 1, (float)values[2 * i + 1]);
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
    }
}
