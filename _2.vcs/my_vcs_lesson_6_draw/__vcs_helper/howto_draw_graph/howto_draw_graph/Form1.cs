using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace howto_draw_graph
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Some data.
        // U.S. gross national debt in $ billions.
        // Souurce: http://en.wikipedia.org/wiki/United_States_public_debt.
        private PointF[] Values = 
        {
            new PointF(1910, 2.6f),
            new PointF(1920, 25.9f),
            new PointF(1928, 18.5f),
            new PointF(1930, 16.2f),
            new PointF(1940, 50.6f),
            new PointF(1950, 256.8f),
            new PointF(1960, 290.5f),
            new PointF(1970, 380.9f),
            new PointF(1980, 909.0f),
            new PointF(1990, 3206.3f),
            new PointF(2000, 5628.7f),
            new PointF(2005, 7905.3f),
        };

        // The values transformed for drawing.
        PointF[] TransformedValues;

        // World coordinate information.
        private const int Wxmin = 1900;
        private const int Wxmax = 2010;
        private const int Wymin = 0;
        private const int Wymax = 8000;

        // The area where we will draw the graph.
        private int GraphXmin, GraphXmax, GraphYmin, GraphYmax;

        // The radius of a drawn point.
        private const float Radius = 4;

        // Draw the graph.
        private void picGraph_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw with the identity transformation.
            DrawWithoutTransformation(e.Graphics);

            // Define the graph area.
            GraphXmin = 70;
            GraphXmax = picGraph.ClientSize.Width - 10;
            GraphYmin = 40;
            GraphYmax = picGraph.ClientSize.Height - 70;
            Rectangle graph_area = new Rectangle(
                GraphXmin, GraphYmin, GraphXmax - GraphXmin, GraphYmax - GraphYmin);
            e.Graphics.FillRectangle(Brushes.White, graph_area);

            // Draw things in the graph's world coordinate space.
            DrawInGraphCoordinates(e.Graphics, GraphXmin, GraphXmax, GraphYmin, GraphYmax);

            // Save the graph's coordinate transformation.
            Matrix graph_transformation = e.Graphics.Transform;

            // Draw things that are positioned using the graph's
            // transformation but that are drawn in pixels.
            DrawWithGraphTransformation(e.Graphics, graph_transformation);
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
                    Point title_center = new Point(picGraph.ClientSize.Width / 2, 20);
                    gr.DrawString("U.S. Gross National Debt",
                        title_font, Brushes.Blue,
                        title_center, string_format);
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
                for (int i = 1; i < Values.Length; i++)
                {
                    gr.DrawLine(green_pen, Values[i - 1], Values[i]);
                }
            }
        }

        // Draw things that are positioned using the graph's
        // transformation but that are drawn in pixels.
        private void DrawWithGraphTransformation(Graphics gr, Matrix graph_matrix)
        {
            // Reset to the identity transformation.
            gr.ResetTransform();

            // Plot the data points.
            // Copy the points so we don't mess up the original values.
            TransformedValues = (PointF[])Values.Clone();

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

            // Draw the axes.
            using (Font label_font = new Font("Times New Roman", 8))
            {
                // Draw the Y axis.
                using (StringFormat label_format = new StringFormat())
                {
                    label_format.Alignment = StringAlignment.Far;
                    label_format.LineAlignment = StringAlignment.Center;

                    // Draw the axis.
                    PointF[] y_points = 
                    {
                        new PointF(Wxmin, Wymin),
                        new PointF(Wxmin, Wymax),
                    };
                    graph_matrix.TransformPoints(y_points);
                    gr.DrawLine(Pens.Black, y_points[0], y_points[1]);

                    // Draw the tick marks and labels.
                    for (int y = Wymin; y <= Wymax; y += 1000)
                    {
                        // Tick mark.
                        PointF[] tick_point = { new PointF(Wxmin, y) };
                        graph_matrix.TransformPoints(tick_point);
                        gr.DrawLine(Pens.Black,
                            tick_point[0].X, tick_point[0].Y,
                            tick_point[0].X + 10, tick_point[0].Y);

                        // Label.
                        PointF[] label_point = { new PointF(0, y) };
                        graph_matrix.TransformPoints(label_point);
                        gr.DrawString(y.ToString("0"), label_font,
                            Brushes.Black, GraphXmin - 10, label_point[0].Y,
                            label_format);
                    }
                }

                // Draw the X axis.
                // Draw the axis.
                PointF[] x_points = 
                {
                    new PointF(Wxmin, Wymin),
                    new PointF(Wxmax, Wymin),
                };
                graph_matrix.TransformPoints(x_points);
                gr.DrawLine(Pens.Black, x_points[0], x_points[1]);

                // Draw the tick marks and labels.
                for (int x = Wxmin; x <= Wxmax; x += 10)
                {
                    // Tick mark.
                    PointF[] tick_point = { new PointF(x, Wymin) };
                    graph_matrix.TransformPoints(tick_point);
                    gr.DrawLine(Pens.Black,
                        tick_point[0].X, tick_point[0].Y,
                        tick_point[0].X, tick_point[0].Y - 10);

                    // Label.
                    DrawXLabel(gr, x.ToString("0"), label_font,
                        Brushes.Black, tick_point[0].X, GraphYmax + 10);
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
                    gr.DrawString("Debt ($ billions)", axis_font,
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
                        picGraph.ClientSize.Height - GraphYmax);
                    gr.DrawString("Year", axis_font,
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
        private void picGraph_MouseMove(object sender, MouseEventArgs e)
        {
            if (TransformedValues == null) return;

            // See what tool tip to display.
            string tip = "";
            for (int i = 0; i < TransformedValues.Length; i++)
            {
                if ((Math.Abs(e.X - TransformedValues[i].X) < Radius) &&
                    (Math.Abs(e.Y - TransformedValues[i].Y) < Radius))
                {
                    tip = "$" + Values[i].Y.ToString() + "B";
                    break;
                }
            }

            // Set the new tool tip.
            if (tipData.GetToolTip(picGraph) != tip)
            {
                tipData.SetToolTip(picGraph, tip);
            }
        }
    }
}
