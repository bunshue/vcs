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

        private double rad(double d)
        {
            return d * Math.PI / 180.0;
        }

        private double sind(double d)
        {
            return Math.Sin(d * Math.PI / 180.0);
        }

        private double cosd(double d)
        {
            return Math.Cos(d * Math.PI / 180.0);
        }

        private void DrawColorWheel2()
        {
            Graphics g = this.pictureBox1.CreateGraphics();
            g.Clear(Color.White);

            int i = 0;
            int j = 0;
            int R = 0;
            int G = 0;
            int B = 0;
            int color_r_st;
            int color_r_sp;
            int color_g_st;
            int color_g_sp;
            int color_b_st;
            int color_b_sp;

            int cx = 200;
            int cy = 200;
            int r = 200;

            for (i = 0; i < 360; i += 1)
            {
                if (i < 60)
                {
                    color_r_st = 255;
                    color_g_st = 0;
                    color_b_st = 0;
                    color_r_sp = 255;
                    color_g_sp = 255;
                    color_b_sp = 0;
                }
                else if (i < 120)
                {
                    color_r_st = 255;
                    color_g_st = 255;
                    color_b_st = 0;
                    color_r_sp = 0;
                    color_g_sp = 255;
                    color_b_sp = 0;
                }
                else if (i < 180)
                {
                    color_r_st = 0;
                    color_g_st = 255;
                    color_b_st = 0;
                    color_r_sp = 0;
                    color_g_sp = 255;
                    color_b_sp = 255;
                }
                else if (i < 240)
                {
                    color_r_st = 0;
                    color_g_st = 255;
                    color_b_st = 255;
                    color_r_sp = 0;
                    color_g_sp = 0;
                    color_b_sp = 255;
                }
                else if (i < 300)
                {
                    color_r_st = 0;
                    color_g_st = 0;
                    color_b_st = 255;
                    color_r_sp = 255;
                    color_g_sp = 0;
                    color_b_sp = 255;
                }
                else
                {
                    color_r_st = 255;
                    color_g_st = 0;
                    color_b_st = 255;
                    color_r_sp = 255;
                    color_g_sp = 0;
                    color_b_sp = 0;
                }
                if (color_r_st == color_r_sp)
                {
                    R = color_r_st;
                }
                else
                {
                    j = i % 60;
                    R = color_r_st + (j * (color_r_sp - color_r_st) / 60);
                }
                if (color_g_st == color_g_sp)
                {
                    G = color_g_st;
                }
                else
                {
                    j = i % 60;
                    G = color_g_st + (j * (color_g_sp - color_g_st) / 60);
                }
                if (color_b_st == color_b_sp)
                {
                    B = color_b_st;
                }
                else
                {
                    j = i % 60;
                    B = color_b_st + (j * (color_b_sp - color_b_st) / 60);
                }

                Pen p = new Pen(Color.FromArgb(255, R, G, B), 2);

                g.DrawLine(p, cx, cy, cx + r * (float)cosd(i), cy + r * (float)sind(i));



                richTextBox1.Text += "i = " + i.ToString() + ", R = " + R.ToString() + ", G = " + G.ToString() + ", B = " + B.ToString() + "\n";
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            DrawColorWheel2();
        }
    }
}
