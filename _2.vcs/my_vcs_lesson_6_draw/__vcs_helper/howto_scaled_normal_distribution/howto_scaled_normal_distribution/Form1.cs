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

namespace howto_scaled_normal_distribution
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnDraw_Click(object sender, EventArgs e)
        {
            float mean = float.Parse(txtMean.Text);
            float stddev = float.Parse(txtStdDev.Text);
            float var = stddev * stddev;
            float devs = float.Parse(txtDevs.Text);

            picGraph.Image = DrawDistribution(devs,
                picGraph.ClientSize.Width,
                picGraph.ClientSize.Height,
                mean, stddev, var);
        }

        // The normal distribution function.
        private float F(float x, float one_over_2pi, float mean, float stddev, float var)
        {
            return (float)(one_over_2pi * Math.Exp(-(x - mean) * (x - mean) / (2 * var)));
        }

        // Draw the normal distribution scaled to fit the curve
        // within stddev_multiple deviations.
        private Bitmap DrawDistribution(float stddev_multiple,
            int wid, int hgt, float mean, float stddev, float var)
        {
            // Make a bitmap.
            Bitmap bm = new Bitmap(picGraph.ClientSize.Width, picGraph.ClientSize.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.SmoothingMode = SmoothingMode.AntiAlias;

                // Define the mapping from world
                // coordinates onto the PictureBox.
                float wxmin = mean - stddev * stddev_multiple;
                float wxmax = mean + stddev * stddev_multiple;
                float one_over_2pi = (float)(1.0 / (stddev * Math.Sqrt(2 * Math.PI)));
                float wymax = F(mean, one_over_2pi, mean, stddev_multiple, var) * 1.1f;
                float wymin = -0.2f * wymax;

                float wwid = wxmax - wxmin;
                float whgt = wymax - wymin;
                RectangleF world = new RectangleF(wxmin, wymin, wwid, whgt);
                PointF[] device_points =
                {
                    new PointF(0, picGraph.ClientSize.Height),
                    new PointF(picGraph.ClientSize.Width, picGraph.ClientSize.Height),
                    new PointF(0, 0),
                };
                Matrix transform = new Matrix(world, device_points);

                // Get the inverse transform.
                Matrix inverse = transform.Clone();
                inverse.Invert();

                // Get tick mark lengths.
                PointF[] ticks = { new PointF(5, 5) };
                inverse.TransformVectors(ticks);
                float tick_dx = ticks[0].X;
                float tick_dy = -ticks[0].Y;

                // Make a thin Pen to use.
                using (Pen pen = new Pen(Color.Red, 0))
                {
                    using (Font font = new Font("Arial", 8))
                    {
                        // Draw the X axis.
                        gr.Transform = transform;
                        pen.Color = Color.Black;
                        gr.DrawLine(pen, wxmin, 0, wxmax, 0);
                        for (int x = (int)wxmin - 1; x <= wxmax; x++)
                        {
                            gr.DrawLine(pen, x, -tick_dy * 2, x, tick_dy * 2);
                            gr.DrawLine(pen, x + 0.25f, -tick_dy, x + 0.25f, tick_dy);
                            gr.DrawLine(pen, x + 0.50f, -tick_dy, x + 0.50f, tick_dy);
                            gr.DrawLine(pen, x + 0.75f, -tick_dy, x + 0.75f, tick_dy);
                        }

                        // Label the X axis.
                        gr.Transform = new Matrix();
                        gr.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;
                        List<PointF> ints = new List<PointF>();
                        for (int x = (int)wxmin; x <= wxmax; x++)
                            ints.Add(new PointF(x, -2 * tick_dy));
                        PointF[] ints_array = ints.ToArray();
                        transform.TransformPoints(ints_array);

                        using (StringFormat sf = new StringFormat())
                        {
                            sf.Alignment = StringAlignment.Center;
                            sf.LineAlignment = StringAlignment.Near;
                            int index = 0;
                            for (int x = (int)wxmin; x <= wxmax; x++)
                            {
                                gr.DrawString(x.ToString(), font, Brushes.Black,
                                    ints_array[index++], sf);
                            }
                        }

                        // Draw the Y axis.
                        gr.Transform = transform;
                        pen.Color = Color.Black;
                        gr.DrawLine(pen, 0, wymin, 0, wymax);
                        for (int y = (int)wymin - 1; y <= wymax; y++)
                        {
                            gr.DrawLine(pen, -tick_dx * 2, y, tick_dx * 2, y);
                            gr.DrawLine(pen, -tick_dx, y + 0.25f, tick_dx, y + 0.25f);
                            gr.DrawLine(pen, -tick_dx, y + 0.50f, tick_dx, y + 0.50f);
                            gr.DrawLine(pen, -tick_dx, y + 0.75f, tick_dx, y + 0.75f);
                        }

                        // Label the Y axis.
                        gr.Transform = new Matrix();
                        gr.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;
                        ints = new List<PointF>();
                        for (float y = 0.25f; y < wymax; y += 0.25f)
                            ints.Add(new PointF(2 * tick_dx, y));
                        if (ints.Count > 0)
                        {
                            ints_array = ints.ToArray();
                            transform.TransformPoints(ints_array);
                        }

                        using (StringFormat sf = new StringFormat())
                        {
                            sf.Alignment = StringAlignment.Near;
                            sf.LineAlignment = StringAlignment.Center;
                            int index = 0;
                            for (float y = 0.25f; y < wymax; y += 0.25f)
                            {
                                gr.DrawString(y.ToString("0.00"), font, Brushes.Black,
                                    ints_array[index++], sf);
                            }
                        }

                        // Draw the curve.
                        gr.Transform = transform;
                        List<PointF> points = new List<PointF>();

                        float dx = (wxmax - wxmin) / picGraph.ClientSize.Width;
                        for (float x = wxmin; x <= wxmax; x += dx)
                        {
                            float y = F(x, one_over_2pi, mean, stddev, var);
                            points.Add(new PointF(x, y));
                        }
                        pen.Color = Color.Red;
                        gr.DrawLines(pen, points.ToArray());
                    } // Font
                } // Pen
            }

            return bm;
        }
    }
}
