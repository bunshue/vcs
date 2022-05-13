using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;
using System.Drawing.Text;  //for TextRenderingHint

namespace vcs_Draw_Function
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

       //畫平均分佈
        private void button4_Click(object sender, EventArgs e)
        {
            float mean = float.Parse(txtMean.Text);
            float stddev = float.Parse(txtStdDev.Text);
            float var = stddev * stddev;
            float devs = float.Parse(txtDevs.Text);

            pictureBox1.Image = DrawDistribution(devs, pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height, mean, stddev, var);
        }

        // The normal distribution function.
        private float F_normal1(float x, float one_over_2pi, float mean, float stddev, float var)
        {
            return (float)(one_over_2pi * Math.Exp(-(x - mean) * (x - mean) / (2 * var)));
        }

        // Draw the normal distribution scaled to fit the curve
        // within stddev_multiple deviations.
        private Bitmap DrawDistribution(float stddev_multiple, int wid, int hgt, float mean, float stddev, float var)
        {
            // Make a bitmap.
            Bitmap bm = new Bitmap(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.SmoothingMode = SmoothingMode.AntiAlias;

                // Define the mapping from world
                // coordinates onto the PictureBox.
                float wxmin = mean - stddev * stddev_multiple;
                float wxmax = mean + stddev * stddev_multiple;
                float one_over_2pi = (float)(1.0 / (stddev * Math.Sqrt(2 * Math.PI)));
                float wymax = F_normal1(mean, one_over_2pi, mean, stddev_multiple, var) * 1.1f;
                float wymin = -0.2f * wymax;

                float wwid = wxmax - wxmin;
                float whgt = wymax - wymin;
                RectangleF world = new RectangleF(wxmin, wymin, wwid, whgt);
                PointF[] device_points =
                {
                    new PointF(0, pictureBox1.ClientSize.Height),
                    new PointF(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height),
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

                        float dx = (wxmax - wxmin) / pictureBox1.ClientSize.Width;
                        for (float x = wxmin; x <= wxmax; x += dx)
                        {
                            float y = F_normal1(x, one_over_2pi, mean, stddev, var);
                            points.Add(new PointF(x, y));
                        }
                        pen.Color = Color.Red;
                        gr.DrawLines(pen, points.ToArray());
                    } // Font
                } // Pen
            }
            return bm;
        }

        //畫三角函數 ST
        // The image used for the graph.
        private Bitmap GraphImage;

        // Graph.
        private void button6_Click(object sender, EventArgs e)
        {
            GraphImage = new Bitmap(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height);
            using (Graphics gr = Graphics.FromImage(GraphImage))
            {
                gr.Clear(Color.White);
                gr.SmoothingMode = SmoothingMode.AntiAlias;

                using (Pen thin_pen = new Pen(Color.Purple, 0))
                {
                    // Get the bounds.
                    double xmin = double.Parse(txtXmin.Text) * Math.PI;
                    double xmax = double.Parse(txtXmax.Text) * Math.PI;
                    double ymin = double.Parse(txtYmin.Text);
                    double ymax = double.Parse(txtYmax.Text);

                    // Scale to make the area fit the PictureBox.
                    RectangleF world_coords = new RectangleF(
                        (float)xmin, (float)ymax,
                        (float)(xmax - xmin),
                        (float)(ymin - ymax));
                    PointF[] device_coords =
                    {
                        new PointF(0, 0),
                        new PointF(pictureBox1.ClientSize.Width, 0),
                        new PointF(0, pictureBox1.ClientSize.Height),
                    };
                    gr.Transform = new Matrix(world_coords, device_coords);

                    // Draw the X-axis.
                    // Start at the multiple of Pi < xmin.
                    double start_x = Math.PI * ((int)(xmin - 1));
                    gr.DrawLine(thin_pen, (float)xmin, 0, (float)xmax, 0);
                    float dy = (float)((ymax - ymin) / 30.0);
                    for (double x = start_x; x <= xmax; x += Math.PI)
                    {
                        gr.DrawLine(thin_pen, (float)x, -2 * dy, (float)x, 2 * dy);
                    }
                    for (double x = start_x + Math.PI / 2.0; x <= xmax; x += Math.PI)
                    {
                        gr.DrawLine(thin_pen, (float)x, -dy, (float)x, dy);
                    }

                    // Draw the Y-axis.
                    // Start at the multiple of 1 < ymin.
                    double start_y = (int)ymin - 1;
                    gr.DrawLine(thin_pen, 0, (float)ymin, 0, (float)ymax);
                    float dx = (float)((xmax - xmin) / 60.0);
                    for (double y = start_y; y <= ymax; y += 1.0)
                    {
                        gr.DrawLine(thin_pen, -2 * dx, (float)y, 2 * dx, (float)y);
                    }
                    for (double y = start_y + 0.5; y <= ymax; y += 1.0)
                    {
                        gr.DrawLine(thin_pen, -dx, (float)y, dx, (float)y);
                    }

                    // Draw vertical asymptotes.
                    thin_pen.DashPattern = new float[] { 5, 5 };
                    for (double x = start_x + Math.PI / 2.0; x <= xmax; x += Math.PI)
                    {
                        gr.DrawLine(thin_pen, (float)x, (float)ymin, (float)x, (float)ymax);
                    }

                    // Draw horizontal limits for sine and cosine.
                    gr.DrawLine(thin_pen, (float)xmin, 1, (float)xmax, 1);
                    gr.DrawLine(thin_pen, (float)xmin, -1, (float)xmax, -1);
                    thin_pen.DashStyle = DashStyle.Solid;

                    // See how big a pixel is before scaling.
                    Matrix inverse = gr.Transform;
                    inverse.Invert();
                    PointF[] pixel_pts =
                    {
                        new PointF(0, 0),
                        new PointF(1, 0),
                    };
                    inverse.TransformPoints(pixel_pts);
                    dx = pixel_pts[1].X - pixel_pts[0].X;

                    // Sine.
                    List<PointF> sine_points = new List<PointF>();
                    for (float x = (float)xmin; x <= xmax; x += dx)
                    {
                        sine_points.Add(new PointF(x, (float)Math.Sin(x)));
                    }
                    thin_pen.Color = Color.Red;
                    gr.DrawLines(thin_pen, sine_points.ToArray());

                    // Cosine.
                    List<PointF> cosine_points = new List<PointF>();
                    for (float x = (float)xmin; x <= xmax; x += dx)
                    {
                        cosine_points.Add(new PointF(x, (float)Math.Cos(x)));
                    }
                    thin_pen.Color = Color.Green;
                    gr.DrawLines(thin_pen, cosine_points.ToArray());

                    // Tangent.
                    List<PointF> tangent_points = new List<PointF>();
                    double old_value = Math.Tan(xmin);
                    thin_pen.Color = Color.Blue;
                    for (float x = (float)xmin; x <= xmax; x += dx)
                    {
                        // See if we're at a discontinuity.
                        double new_value = Math.Tan(x);
                        if ((Math.Abs(new_value - old_value) > 10) &&
                            (Math.Sign(new_value) != Math.Sign(old_value)))
                        {
                            if (tangent_points.Count > 1)
                                gr.DrawLines(thin_pen, tangent_points.ToArray());
                            tangent_points = new List<PointF>();
                        }
                        else
                        {
                            tangent_points.Add(new PointF(x, (float)Math.Tan(x)));
                        }
                    }
                    if (tangent_points.Count > 1)
                        gr.DrawLines(thin_pen, tangent_points.ToArray());
                }
            }

            // Display the result.
            pictureBox1.Image = GraphImage;


        }

        //畫三角函數 SP

        #region 常態分佈
        private void btnDraw_Click(object sender, EventArgs e)
        {
            float mean = float.Parse(txtMean.Text);
            float stddev = float.Parse(txtStdDev.Text);
            float var = stddev * stddev;

            // Make a bitmap.
            Bitmap bm = new Bitmap(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.SmoothingMode = SmoothingMode.AntiAlias;

                // Define the mapping from world
                // coordinates onto the PictureBox.
                const float wxmin = -5.1f;
                const float wymin = -0.2f;
                const float wxmax = -wxmin;
                const float wymax = 1.1f;
                const float wwid = wxmax - wxmin;
                const float whgt = wymax - wymin;
                RectangleF world = new RectangleF(wxmin, wymin, wwid, whgt);
                PointF[] device_points =
                {
                    new PointF(0, pictureBox1.ClientSize.Height),
                    new PointF(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height),
                    new PointF(0, 0),
                };
                Matrix transform = new Matrix(world, device_points);

                // Make a thin Pen to use.
                using (Pen pen = new Pen(Color.Red, 0))
                {
                    using (Font font = new Font("Arial", 8))
                    {
                        // Draw the X axis.
                        gr.Transform = transform;
                        pen.Color = Color.Black;
                        gr.DrawLine(pen, wxmin, 0, wxmax, 0);
                        for (int x = (int)wxmin; x <= wxmax; x++)
                        {
                            gr.DrawLine(pen, x, -0.05f, x, 0.05f);
                            gr.DrawLine(pen, x + 0.25f, -0.025f, x + 0.25f, 0.025f);
                            gr.DrawLine(pen, x + 0.50f, -0.025f, x + 0.50f, 0.025f);
                            gr.DrawLine(pen, x + 0.75f, -0.025f, x + 0.75f, 0.025f);
                        }

                        // Label the X axis.
                        gr.Transform = new Matrix();
                        gr.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;
                        List<PointF> ints = new List<PointF>();
                        for (int x = (int)wxmin; x <= wxmax; x++)
                            ints.Add(new PointF(x, -0.07f));
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
                        for (int y = (int)wymin; y <= wymax; y++)
                        {
                            gr.DrawLine(pen, -0.2f, y, 0.2f, y);
                            gr.DrawLine(pen, -0.1f, y + 0.25f, 0.1f, y + 0.25f);
                            gr.DrawLine(pen, -0.1f, y + 0.50f, 0.1f, y + 0.50f);
                            gr.DrawLine(pen, -0.1f, y + 0.75f, 0.1f, y + 0.75f);
                        }

                        // Label the Y axis.
                        gr.Transform = new Matrix();
                        gr.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;
                        ints = new List<PointF>();
                        for (float y = 0.25f; y < 1.01; y += 0.25f)
                            ints.Add(new PointF(0.2f, y));
                        ints_array = ints.ToArray();
                        transform.TransformPoints(ints_array);

                        using (StringFormat sf = new StringFormat())
                        {
                            sf.Alignment = StringAlignment.Near;
                            sf.LineAlignment = StringAlignment.Center;
                            int index = 0;
                            foreach (float y in new float[] { 0.25f, 0.5f, 0.75f, 1.0f })
                            {
                                gr.DrawString(y.ToString("0.00"), font, Brushes.Black,
                                    ints_array[index++], sf);
                            }
                        }

                        // Draw the curve.
                        gr.Transform = transform;
                        List<PointF> points = new List<PointF>();
                        float one_over_2pi =
                            (float)(1.0 / (stddev * Math.Sqrt(2 * Math.PI)));

                        float dx = (wxmax - wxmin) / pictureBox1.ClientSize.Width;
                        for (float x = wxmin; x <= wxmax; x += dx)
                        {
                            float y = F_normal2(x, one_over_2pi, mean, stddev, var);
                            points.Add(new PointF(x, y));
                        }
                        pen.Color = Color.Red;
                        gr.DrawLines(pen, points.ToArray());
                    } // Font
                } // Pen

                pictureBox1.Image = bm;
            }
        }

        // The normal distribution function.
        private float F_normal2(float x, float one_over_2pi, float mean, float stddev, float var)
        {
            return (float)(one_over_2pi * Math.Exp(-(x - mean) * (x - mean) / (2 * var)));
        }

        #endregion 常態分佈



    }
}
