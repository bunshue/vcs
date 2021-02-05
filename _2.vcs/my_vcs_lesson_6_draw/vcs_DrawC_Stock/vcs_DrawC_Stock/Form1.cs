using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace vcs_DrawC_Stock
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The ticker symbol.
        private const string Symbol = "Company";

        // The data.
        private List<DateTime> Times = new List<DateTime>();
        private List<PointF> Prices = new List<PointF>();

        // The values transformed for drawing.
        PointF[] TransformedValues;

        // World coordinate information.
        private float Wxmin, Wxmax, Wymin, Wymax;

        // The area where we will draw the graph.
        private int GraphXmin, GraphXmax, GraphYmin, GraphYmax;

        // The radius of a drawn point.
        private const float Radius = 4;

        // Prepare the timer.
        private void Form1_Load(object sender, EventArgs e)
        {
            // Get the first price.
            SavePrice();
        }

        // Get a new stock price.
        private int PointNum = 0;
        private void SavePrice()
        {
            Prices.Add(new PointF(PointNum++, GetPrice()));
            Times.Add(DateTime.Now);

            // Redraw.
            pictureBox1.Refresh();
        }

        // Get the stock price.
        private float GetPrice()
        {
            Random r = new Random();
            return r.Next(10);
        }

        // Draw the graph.
        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(pictureBox1.BackColor);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            if (Times.Count == 0)
                return;

            // Define the graph area.
            GraphXmin = 80;
            GraphXmax = pictureBox1.ClientSize.Width - 10;
            GraphYmin = 40;
            GraphYmax = pictureBox1.ClientSize.Height - 80;
            Rectangle graph_area = new Rectangle(GraphXmin, GraphYmin, GraphXmax - GraphXmin, GraphYmax - GraphYmin);

            // Get bounds.
            GetBounds();

            // Draw with the identity transformation.
            DrawWithoutTransformation(e.Graphics);

            // Fill the graph area.
            e.Graphics.FillRectangle(Brushes.White, graph_area);

            // Draw things in the graph's world coordinate space.
            DrawInGraphCoordinates(e.Graphics, GraphXmin, GraphXmax, GraphYmin, GraphYmax);

            // Save the graph's coordinate transformation.
            Matrix graph_transformation = e.Graphics.Transform;

            // Draw things that are positioned using the graph's
            // transformation but that are drawn in pixels.
            DrawWithGraphTransformation(e.Graphics, graph_transformation);
        }

        // Get the world coordinate bounds.
        private void GetBounds()
        {
            float ymin = Prices.Min(pt => pt.Y);
            float ymax = Prices.Max(pt => pt.Y);
            float ydiff = 1.2f * (ymax - ymin);
            if (ydiff < 20)
                ydiff = 20;
            float ymid = (ymin + ymax) / 2f;
            Wymin = ymid - ydiff / 2f;
            Wymax = Wymin + ydiff;

            // Make sure we don't have too many values.
            const float pix_per_x = 20;
            while ((Times.Count - 1) * pix_per_x > (GraphXmax - GraphXmin))
            {
                Times.RemoveAt(0);
                Prices.RemoveAt(0);
            }
            
            Wxmin = Prices.Min(pt => pt.X);
            Wxmax = Wxmin + (GraphXmax - GraphXmin) / pix_per_x;
        }

        // Draw things that use the identity transformation.
        private void DrawWithoutTransformation(Graphics gr)
        {
            // Draw the main title centered on the top.
            using (Font title_font = new Font("Times New Roman", 20))
            {
                using (StringFormat string_format = new StringFormat())
                {
                    string_format.Alignment = StringAlignment.Center;
                    string_format.LineAlignment = StringAlignment.Center;
                    Point title_center = new Point(pictureBox1.ClientSize.Width / 2, 20);
                    gr.DrawString(Symbol, title_font, Brushes.Blue, title_center, string_format);
                }
            }
        }

        // Draw things in the graph's world coordinate.
        private void DrawInGraphCoordinates(Graphics gr, int xmin, int xmax, int ymin, int ymax)
        {
            // Define the world coordinate rectangle.
            RectangleF world_rect = new RectangleF(Wxmin, Wymin, Wxmax - Wxmin, Wymax - Wymin);

            // Define the points to which the rectangle's upper left,
            // upper right, and lower right corners should map.
            // Note the vertical flip so large Y values are at the top.
            PointF[] window_points =
            {
                new PointF(xmin, ymax),
                new PointF(xmax, ymax),
                new PointF(xmin, ymin),
            };

            // Define the transformation.
            Matrix graph_transformation = new Matrix(world_rect, window_points);

            // Apply the transformation.
            gr.Transform = graph_transformation;

            // Plot the data lines.
            using (Pen green_pen = new Pen(Color.Green, 0))
            {
                for (int i = 1; i < Prices.Count; i++)
                {
                    gr.DrawLine(green_pen, Prices[i - 1], Prices[i]);
                }
            }
        }

        // Draw things that are positioned using the graph's
        // transformation but that are drawn in pixels.
        private void DrawWithGraphTransformation(Graphics gr, Matrix graph_matrix)
        {
            // Reset to the identity transformation.
            gr.ResetTransform();

            // Draw the axes.
            using (Font label_font = new Font("Times New Roman", 8))
            {
                // Draw the Y axis.
                using (StringFormat label_format = new StringFormat())
                {
                    label_format.Alignment = StringAlignment.Far;
                    label_format.LineAlignment = StringAlignment.Center;

                    // Draw the tick marks and labels.
                    int ystart = 10 * (int)(Wymin / 10);
                    if (ystart < Wymin) ystart += 10;
                    for (int y = ystart; y <= Wymax; y += 10)
                    {
                        // Axis mark.
                        PointF[] tick_points = 
                        {
                            new PointF(Wxmin, y),
                            new PointF(Wxmax, y),
                        };
                        graph_matrix.TransformPoints(tick_points);
                        // Horizontal line.
                        gr.DrawLine(Pens.LightBlue,
                            tick_points[0].X, tick_points[0].Y,
                            tick_points[1].X, tick_points[1].Y);
                        //// Tic mark.
                        //gr.DrawLine(Pens.Black,
                        //    tick_points[0].X, tick_points[0].Y,
                        //    tick_points[0].X + 10, tick_points[0].Y);

                        // Label.
                        PointF[] label_point = { new PointF(0, y) };
                        graph_matrix.TransformPoints(label_point);
                        gr.DrawString(y.ToString("C3"), label_font, Brushes.Black, GraphXmin - 10, label_point[0].Y, label_format);
                    }
                }

                // Draw the X axis.
                // Draw the tick marks and labels.
                for (int x = 0; x < Times.Count; x++)
                {
                    // Axis mark.
                    PointF[] tick_points =
                    {
                        new PointF(Wxmin + x, Wymin),
                        new PointF(Wxmin + x, Wymax)
                    };
                    graph_matrix.TransformPoints(tick_points);
                    // Vertical line.
                    gr.DrawLine(Pens.LightBlue,
                        tick_points[0].X, tick_points[0].Y,
                        tick_points[1].X, tick_points[1].Y);
                    // Tick mark.
                    gr.DrawLine(Pens.Black,
                        tick_points[0].X, tick_points[0].Y,
                        tick_points[0].X, tick_points[0].Y - 10);

                    // Label.
                    DrawXLabel(gr,
                        Times[x].ToShortTimeString(),
                        label_font, Brushes.Black,
                        tick_points[0].X, GraphYmax + 10);
                }

                // Draw the X axis.
                PointF[] x_points = 
                {
                    new PointF(Wxmin, Wymin),
                    new PointF(Wxmax, Wymin),
                };
                graph_matrix.TransformPoints(x_points);
                gr.DrawLine(Pens.Black, x_points[0], x_points[1]);

                // Draw the Y axis.
                PointF[] y_points = 
                    {
                        new PointF(Wxmin, Wymin),
                        new PointF(Wxmin, Wymax),
                    };
                graph_matrix.TransformPoints(y_points);
                gr.DrawLine(Pens.Black, y_points[0], y_points[1]);


                // Plot the data points.
                // Copy the points so we don't mess up the original values.
                TransformedValues = (PointF[])Prices.ToArray().Clone();

                // Transform the points to see where they are on the PictureBox.
                graph_matrix.TransformPoints(TransformedValues);

                // Draw the points.
                foreach (PointF pt in TransformedValues)
                {
                    gr.FillEllipse(Brushes.Lime,
                        pt.X - Radius, pt.Y - Radius, 2 * Radius, 2 * Radius);
                    gr.DrawEllipse(Pens.Black,
                        pt.X - Radius, pt.Y - Radius, 2 * Radius, 2 * Radius);
                }
            }

            // Label the axes.
            using (Font axis_font = new Font("Times New Roman", 14))
            {
                // Label the Y axis.
                using (StringFormat ylabel_format = new StringFormat())
                {
                    ylabel_format.Alignment = StringAlignment.Center;
                    ylabel_format.LineAlignment = StringAlignment.Near;
                    gr.ResetTransform();
                    gr.RotateTransform(-90);
                    float cx = 0;
                    float cy = (GraphYmin + GraphYmax) / 2;
                    gr.TranslateTransform(cx, cy, MatrixOrder.Append);
                    gr.DrawString("Price", axis_font,
                        Brushes.Green, 0, 0, ylabel_format);
                    gr.ResetTransform();
                }

                // Label the X axis.
                using (StringFormat xlabel_format = new StringFormat())
                {
                    xlabel_format.Alignment = StringAlignment.Center;
                    xlabel_format.LineAlignment = StringAlignment.Far;
                    RectangleF xlabel_rect = new RectangleF(
                        GraphXmin, GraphYmax,
                        GraphXmax - GraphXmin,
                        pictureBox1.ClientSize.Height - GraphYmax);
                    gr.DrawString("Time", axis_font,
                        Brushes.Green, xlabel_rect, xlabel_format);
                }
            }
        }

        // Draw a string rotated 90 degrees at the given position.
        private void DrawXLabel(Graphics gr, string txt, Font label_font,
            Brush label_brush, float x, float y)
        {
            // Transform to center the label's right edge
            // at the origin when we draw at the origin.
            gr.ResetTransform();

            // Rotate the translated text.
            gr.RotateTransform(90, MatrixOrder.Append);

            // Translate to the final destination.
            gr.TranslateTransform(x, y, MatrixOrder.Append);

            // Draw the label.
            using (StringFormat label_format = new StringFormat())
            {
                // Draw so the text is centered vertically and
                // left aligned at the origin.
                label_format.Alignment = StringAlignment.Near;
                label_format.LineAlignment = StringAlignment.Center;

                // Draw the text at the origin.
                gr.DrawString(txt, label_font, label_brush, 0, 0, label_format);
            }

            gr.ResetTransform();
        }

        // If the mouse is hovering over a data point,
        // set the PictureBox's tooltip.
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (TransformedValues == null) return;

            // See what tool tip to display.
            string tip = "";
            for (int i = 0; i < TransformedValues.Length; i++)
            {
                if ((Math.Abs(e.X - TransformedValues[i].X) < Radius) &&
                    (Math.Abs(e.Y - TransformedValues[i].Y) < Radius))
                {
                    tip = Prices[i].Y.ToString("C3");
                    break;
                }
            }

            // Set the new tool tip.
            if (tipData.GetToolTip(pictureBox1) != tip)
            {
                tipData.SetToolTip(pictureBox1, tip);
            }
        }

        // Get the next price.
        private void timer_stock_Tick(object sender, EventArgs e)
        {
            SavePrice();
        }
    }
}
