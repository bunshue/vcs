using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace vcs_ColorWheel
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The color wheel bitmap.
        private Bitmap WheelBm = null;

        // Draw the initial color wheel.
        private void Form1_Load(object sender, EventArgs e)
        {
            DrawColorWheel();
        }

        // Draw the color wheel.
        private void DrawColorWheel()
        {
            // Create the color wheel bitmap.
            int width = picWheel.Width;
            int height = picWheel.Height;
            WheelBm = new Bitmap(width, height);
            using (Graphics gr = Graphics.FromImage(WheelBm))
            {
                gr.SmoothingMode = SmoothingMode.AntiAlias;

                // Draw the color wheel.
                DrawColorWheel(gr, Color.White,
                    0, 0, width, height);
            }

            // Create a display bitmap.
            Bitmap bm = new Bitmap(width, height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                // Fill with a grid.
                gr.SmoothingMode = SmoothingMode.AntiAlias;
                DrawGrid(gr, width, height);

                // Draw the color wheel on top.
                DrawColorWheel(gr, Color.White,
                    0, 0, width, height);
            }

            // Display the result.
            picWheel.Image = bm;
        }

        // Draw a color wheel in the indicated area.
        private void DrawColorWheel(Graphics gr, Color outline_color,
            int xmin, int ymin, int wid, int hgt)
        {
            Rectangle rect = new Rectangle(xmin, ymin, wid, hgt);
            GraphicsPath wheel_path = new GraphicsPath();
            wheel_path.AddEllipse(rect);
            wheel_path.Flatten();

            // Get alpha and saturation.
            int alpha = hscrAlpha.Value;
            int sat = hscrSaturation.Value;

            float num_pts = (wheel_path.PointCount - 1) / 6;
            Color[] surround_colors = new Color[wheel_path.PointCount];

            int index = 0;
            InterpolateColors(surround_colors, ref index,
                1 * num_pts, alpha, sat, 0, 0, alpha, sat, 0, sat);
            InterpolateColors(surround_colors, ref index,
                2 * num_pts, alpha, sat, 0, sat, alpha, 0, 0, sat);
            InterpolateColors(surround_colors, ref index,
                3 * num_pts, alpha, 0, 0, sat, alpha, 0, sat, sat);
            InterpolateColors(surround_colors, ref index,
                4 * num_pts, alpha, 0, sat, sat, alpha, 0, sat, 0);
            InterpolateColors(surround_colors, ref index,
                5 * num_pts, alpha, 0, sat, 0, alpha, sat, sat, 0);
            InterpolateColors(surround_colors, ref index,
                wheel_path.PointCount, alpha, sat, sat, 0, alpha, sat, 0, 0);

            using (PathGradientBrush path_brush =
                new PathGradientBrush(wheel_path))
            {
                path_brush.CenterColor =
                    Color.FromArgb(alpha, 255, 255, 255);
                path_brush.SurroundColors = surround_colors;

                gr.FillPath(path_brush, wheel_path);

                // It looks better if we outline the wheel.
                using (Pen thick_pen = new Pen(outline_color, 2))
                {
                    gr.DrawPath(thick_pen, wheel_path);
                }
            }

            //// Uncomment the following to draw the path's points.
            //for (int i = 0; i < wheel_path.PointCount; i++)
            //{
            //    gr.FillEllipse(Brushes.Black,
            //        wheel_path.PathPoints[i].X - 2,
            //        wheel_path.PathPoints[i].Y - 2,
            //        4, 4);
            //}
        }

        // Fill in colors interpolating between the from and to values.
        private void InterpolateColors(Color[] surround_colors,
            ref int index, float stop_pt,
            int from_a, int from_r, int from_g, int from_b,
            int to_a, int to_r, int to_g, int to_b)
        {
            int num_pts = (int)stop_pt - index;
            float a = from_a, r = from_r, g = from_g, b = from_b;
            float da = (to_a - from_a) / (num_pts - 1);
            float dr = (to_r - from_r) / (num_pts - 1);
            float dg = (to_g - from_g) / (num_pts - 1);
            float db = (to_b - from_b) / (num_pts - 1);

            for (int i = 0; i < num_pts; i++)
            {
                surround_colors[index++] =
                    Color.FromArgb((int)a, (int)r, (int)g, (int)b);
                a += da;
                r += dr;
                g += dg;
                b += db;
            }
        }

        // Draw a black grid over a white background.
        private void DrawGrid(Graphics gr, int width, int height)
        {
            gr.Clear(Color.White);
            using (Pen pen = new Pen(Color.Black, 2))
            {
                for (int x = 10; x < width; x += 20)
                    gr.DrawLine(pen, x, 0, x, height - 1);
                for (int y = 10; y < height; y += 20)
                    gr.DrawLine(pen, 0, y, width - 1, y);
            }
        }

        // Update the color wheel.
        private void hscrAlpha_Scroll(object sender, ScrollEventArgs e)
        {
            txtAlpha.Text = hscrAlpha.Value.ToString();
            DrawColorWheel();
        }
        private void hscrSaturation_Scroll(object sender, ScrollEventArgs e)
        {
            txtSaturation.Text = hscrSaturation.Value.ToString();
            DrawColorWheel();
        }


        // The selected colors.
        private Color Color1 = Color.FromArgb(128, 255, 0, 0);
        private Color Color2 = Color.FromArgb(128, 0, 0, 255);

        // Set color 1.
        private void btnColor1_Click(object sender, EventArgs e)
        {
            ColorWheelDialog dlg = new ColorWheelDialog();
            dlg.SelectedColor = Color1;
            if (dlg.ShowDialog() == DialogResult.OK)
                Color1 = dlg.SelectedColor;

            picSample.Refresh();
        }

        // Set color 2.
        private void btnColor2_Click(object sender, EventArgs e)
        {
            ColorWheelDialog dlg = new ColorWheelDialog();
            dlg.SelectedColor = Color2;
            if (dlg.ShowDialog() == DialogResult.OK)
                Color2 = dlg.SelectedColor;

            picSample.Refresh();
        }

        // Draw a sample to show the alpha component.
        private void picSample_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(Color.White);

            // Draw some lines.
            int wid = picSample.ClientSize.Width;
            int hgt = picSample.ClientSize.Height;
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            using (Pen pen = new Pen(Color.Black, 3))
            {
                for (int x = 10; x <= wid; x += 20)
                    e.Graphics.DrawLine(pen, x, 0, x, hgt);
                for (int y = 10; y <= hgt; y += 20)
                    e.Graphics.DrawLine(pen, 0, y, wid, y);
            }

            // Draw an ellipse.
            int third = picSample.ClientSize.Width / 3;
            using (Brush brush = new SolidBrush(Color1))
            {
                e.Graphics.FillEllipse(brush, 0, 0, 2 * third, hgt);
            }
            using (Brush brush = new SolidBrush(Color2))
            {
                e.Graphics.FillEllipse(brush, third, 0, 2 * third, hgt);
            }
        }

        private void picSample_Resize(object sender, EventArgs e)
        {
            picSample.Refresh();
        }
    
    }
}
