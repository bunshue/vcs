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

namespace vcs_DrawA_Radar
{
    public class CarData
    {
        public string Name;
        public Color Color;
        public float[] Values;
        public PointF[] Points = null;

        public CarData(string name, Color color, params float[] values)
        {
            Name = name;
            Color = color;
            Values = (float[])values.Clone();
        }
    }

    public class AxisInfo
    {
        public string Name, FormatString;
        public float Min, Max;

        public AxisInfo(string name, string format_string, float min, float max)
        {
            Name = name;
            FormatString = format_string;
            Min = min;
            Max = max;
        }
    }

    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private List<CarData> Cars = null;
        private List<AxisInfo> AxisInfos = null;

        // Initialize the car data.
        // From https://www.edmunds.com/electric-car/.
        private void Form1_Load(object sender, EventArgs e)
        {
            Cars = new List<CarData>();
            Cars.Add(new CarData("Audi e-tron", Color.Red, 69850, 80900, 8.4f, 218, 100f / 44));
            Cars.Add(new CarData("Jaguar I-PACE", Color.Green, 39090, 44590, 8.2f, 234, 100f / 30));
            Cars.Add(new CarData("Polestar 2", Color.Blue, 59900, 59900, 8.2f, 275, 100f / 27));

            AxisInfos = new List<AxisInfo>();
            AxisInfos.Add(new AxisInfo("PriceLow", "c", 90000, 30000));
            AxisInfos.Add(new AxisInfo("PriceHigh", "c", 90000, 30000));
            AxisInfos.Add(new AxisInfo("Rating", "0.0", 0, 10));
            AxisInfos.Add(new AxisInfo("Range", "0", 0, 300));
            AxisInfos.Add(new AxisInfo("Miles/kWh", "0.00", 0, 5));
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            e.Graphics.TextRenderingHint = TextRenderingHint.AntiAlias;
            e.Graphics.Clear(pictureBox1.BackColor);

            // Draw the axes.
            DrawCharts(e.Graphics, chkFillAreas.Checked);
        }

        // Draw the radar charts.
        private void DrawCharts(Graphics gr, bool fill_areas)
        {
            // Find the center and radii.
            float cx = pictureBox1.ClientSize.Width / 2f;
            float cy = pictureBox1.ClientSize.Height / 2f;
            float rx = cx - 20;
            float ry = cy - 20;

            // Find the angular distance between wedges.
            double dtheta = 2 * Math.PI / AxisInfos.Count;

            // Draw.
            DrawAxes(gr, cx, cy, rx, ry, dtheta);
            DrawLevels(gr, cx, cy, rx, ry, dtheta);
            DrawRadarCharts(gr, fill_areas, cx, cy, rx, ry, dtheta);
        }

        // Draw the axes.
        private void DrawAxes(Graphics gr, float cx, float cy, float rx, float ry, double dtheta)
        {
            double theta = -Math.PI / 2;
            using (Font font = new Font("Arial", 12))
            {
                for (int i = 0; i < AxisInfos.Count; i++)
                {
                    double x = cx + rx * Math.Cos(theta);
                    double y = cy + ry * Math.Sin(theta);
                    gr.DrawLine(Pens.Black, cx, cy, (float)x, (float)y);

                    x = cx + (rx + 10) * Math.Cos(theta);
                    y = cy + (ry + 10) * Math.Sin(theta);
                    DrawRotatedText(gr, font, Brushes.Black, AxisInfos[i].Name, x, y, theta + Math.PI / 2);

                    theta += dtheta;
                }
            }
        }

        // Draw level polygons.
        private void DrawLevels(Graphics gr, float cx, float cy, float rx, float ry, double dtheta)
        {
            // Draw the level polygons.
            double theta = -Math.PI / 2;
            int num_levels = 5;
            double dfraction = 1.0 / num_levels;
            double fraction = dfraction;
            PointF[] points = new PointF[AxisInfos.Count];
            for (int level = 0; level < num_levels; level++)
            {
                for (int i = 0; i < AxisInfos.Count; i++)
                {
                    double x = cx + fraction * rx * Math.Cos(theta);
                    double y = cy + fraction * ry * Math.Sin(theta);
                    points[i] = new PointF((float)x, (float)y);
                    theta += dtheta;
                }
                gr.DrawPolygon(Pens.Black, points);
                fraction += dfraction;
            }
        }

        // Draw a radar chart for each car.
        private void DrawRadarCharts(Graphics gr, bool fill_areas, float cx, float cy, float rx, float ry, double dtheta)
        {
            // Plot the data.
            foreach (CarData car_data in Cars)
            {
                DrawRadarChart(car_data, gr, fill_areas, cx, cy, rx, ry, dtheta);
            }
        }

        // Draw one car's radar chart.
        private void DrawRadarChart(CarData car_data, Graphics gr, bool fill_areas, float cx, float cy, float rx, float ry, double dtheta)
        {
            // Get this car's polygon.
            PointF[] points = new PointF[AxisInfos.Count];
            double theta = -Math.PI / 2;
            for (int i = 0; i < AxisInfos.Count; i++)
            {
                double frac = (car_data.Values[i] - AxisInfos[i].Min) / (AxisInfos[i].Max - AxisInfos[i].Min);
                double x = cx + frac * rx * Math.Cos(theta);
                double y = cy + frac * ry * Math.Sin(theta);
                points[i] = new PointF((float)x, (float)y);
                theta += dtheta;
            }

            // Save the points.
            car_data.Points = points;

            // Draw the polygon.
            if (fill_areas)
            {
                Color color = Color.FromArgb(64, car_data.Color);
                using (Brush brush = new SolidBrush(color))
                {
                    gr.FillPolygon(brush, points);
                }
            }
            using (Pen pen = new Pen(car_data.Color, 3))
            {
                gr.DrawPolygon(pen, points);
            }
        }

        // Draw text rotated at the indicated point.
        private void DrawRotatedText(Graphics gr, Font font, Brush brush, string text, double x, double y, double theta)
        {
            GraphicsState state = gr.Save();
            gr.ResetTransform();

            gr.RotateTransform((float)(theta * 180 / Math.PI));
            gr.TranslateTransform((float)x, (float)y, MatrixOrder.Append);
            using (StringFormat sf = new StringFormat())
            {
                sf.Alignment = StringAlignment.Center;
                sf.LineAlignment = StringAlignment.Center;
                gr.DrawString(text, font, brush, 0, 0, sf);
            }

            gr.Restore(state);
        }

        // Display a tooltip if appropriate.
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            string tip_text = "";
            foreach (CarData car in Cars)
            {
                // Skip this car if it has no points yet.
                if (car.Points == null)
                {
                    continue;
                }

                // Check the car's points.
                for (int i = 0; i < car.Values.Length; i++)
                {
                    if (PointIsClose(e.Location, car.Points[i], 8))
                    {
                        tip_text = car.Name + " " + AxisInfos[i].Name + ": " + car.Values[i].ToString(AxisInfos[i].FormatString);
                        break;
                    }
                    if (tip_text != "")
                    {
                        break;
                    }
                }
            }

            if (tip_text != tipPoint.GetToolTip(pictureBox1))
            {
                tipPoint.SetToolTip(pictureBox1, tip_text);
                richTextBox1.Text += tip_text + "\n";
            }
        }

        private bool PointIsClose(PointF point1, PointF point2, float radius)
        {
            float dx = point1.X - point2.X;
            float dy = point1.Y - point2.Y;
            return (dx * dx + dy * dy) < (radius * radius);
        }

        private void chkFillAreas_CheckedChanged(object sender, EventArgs e)
        {
            pictureBox1.Refresh();
            pictureBox_radar.Refresh();
        }

        // Display a tooltip if appropriate.
        private void pictureBox_radar_MouseMove(object sender, MouseEventArgs e)
        {
            string tip_text = "";
            foreach (CarData car in Cars)
            {
                // Skip this car if it has no points yet.
                if (car.Points == null)
                {
                    continue;
                }

                // Check the car's points.
                for (int i = 0; i < car.Values.Length; i++)
                {
                    if (PointIsClose(e.Location, car.Points[i], 8))
                    {
                        tip_text = car.Name + " " + AxisInfos[i].Name + ": " + car.Values[i].ToString(AxisInfos[i].FormatString);
                        break;
                    }
                    if (tip_text != "")
                    {
                        break;
                    }
                }
            }

            if (tip_text != toolTip_radar.GetToolTip(pictureBox1))
            {
                toolTip_radar.SetToolTip(pictureBox1, tip_text);
                richTextBox1.Text += tip_text + "\n";
            }
        }

        private void pictureBox_radar_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            e.Graphics.TextRenderingHint = TextRenderingHint.AntiAlias;
            e.Graphics.Clear(pictureBox1.BackColor);

            // Draw the axes.
            DrawCharts(e.Graphics, chkFillAreas.Checked);
        }
    }
}
