using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D;

namespace howto_double_buffer
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private const int period = 24;
        private Color[] Colors;

        // Initialize the colors.
        private void Form1_Load(object sender, EventArgs e)
        {
            // Redraw when resized.
            this.ResizeRedraw = true;

            Colors = new Color[] 
            {
                Color.Pink,
                Color.Red,
                Color.Orange,
                Color.Yellow,
                Color.Lime,
                Color.Cyan,
                Color.Blue,
                Color.Violet,
                Color.Pink,
                Color.Red,
                Color.Orange,
                Color.Yellow,
                Color.Lime,
                Color.Cyan,
                Color.Blue,
                Color.Violet,
                Color.Pink,
                Color.Red,
                Color.Orange,
                Color.Yellow,
                Color.Lime,
                Color.Cyan,
                Color.Blue,
                Color.Violet
            };

            // Draw the initial curves.
            DrawCurves();   //for pictureBox
        }

        // Draw the butterfly.
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            //在Form1上畫蝴蝶，限制蝴蝶大小 400 X 400
            int W = 400;
            int H = 400;

            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            e.Graphics.Clear(this.BackColor);

            // Scale and translate.
            RectangleF world_rect = new RectangleF(-4.0f, -4.4f, 8.0f, 7.3f);
            float cx = (world_rect.Left + world_rect.Right) / 2;
            float cy = (world_rect.Top + world_rect.Bottom) / 2;

            // Center the world coordinates at origin.
            e.Graphics.TranslateTransform(-cx, -cy);

            // Scale to fill the form.
            float scale = Math.Min(W / world_rect.Width, H / world_rect.Height);
            e.Graphics.ScaleTransform(scale, scale, MatrixOrder.Append);

            // Move the result to center on the form.
            e.Graphics.TranslateTransform(W / 2, H / 2, MatrixOrder.Append);

            // Generate the points.
            PointF pt0, pt1;
            double t = 0;
            double expr = Math.Exp(Math.Cos(t)) - 2 * Math.Cos(4 * t) - Math.Pow(Math.Sin(t / 12), 5);
            pt1 = new PointF((float)(Math.Sin(t) * expr), (float)(-Math.Cos(t) * expr));
            using (Pen the_pen = new Pen(Color.Blue, 0))
            {
                const long num_lines = 5000;
                for (long i = 0; i < num_lines; i++)
                {
                    t = i * period * Math.PI / num_lines;
                    expr = Math.Exp(Math.Cos(t)) - 2 * Math.Cos(4 * t) - Math.Pow(Math.Sin(t / 12), 5);
                    pt0 = pt1;
                    pt1 = new PointF((float)(Math.Sin(t) * expr), (float)(-Math.Cos(t) * expr));
                    the_pen.Color = GetColor(t);
                    e.Graphics.DrawLine(the_pen, pt0, pt1);
                }
            }
        }

        // Return an appropriate color for this segment.
        private Color GetColor(double t)
        {
            return Colors[(int)(t / Math.PI)];
        }

        // Turn double buffering on or off and redraw.
        private void chkDoubleBuffer_CheckedChanged(object sender, EventArgs e)
        {
            this.DoubleBuffered = chkDoubleBuffer.Checked;
            this.Refresh();
        }

        // Redraw.
        private void btnRedraw_Click(object sender, EventArgs e)
        {
            if (chkDoubleBuffer.Checked == true)
                label1.Text = "使用 Double Buffer 重畫";
            else
                label1.Text = "不使用 Double Buffer 重畫";

            Application.DoEvents();

            this.Invalidate();

            DrawCurves();   //for pictureBox
        }

        // Draw butterfly curves on both PictureBoxes.
        private void DrawCurves()
        {
            // Clear both images.
            pictureBox1.Image = null;
            pictureBox2.Refresh();
            pictureBox1.Refresh();

            int W = pictureBox2.ClientSize.Width;
            int H = pictureBox2.ClientSize.Height;

            // Draw with double-buffering.
            Bitmap bm = new Bitmap(W, H);
            using (Graphics g = Graphics.FromImage(bm))
            {
                DrawButterfly(g, W, H);
            }
            pictureBox1.Image = bm;
            pictureBox1.Refresh();

            // Draw without double-buffering.
            DrawButterfly(pictureBox2.CreateGraphics(), W, H);
        }

        // Draw the butterfly curve on this Graphics object.
        private void DrawButterfly(Graphics g, int W, int H)
        {
            g.SmoothingMode = SmoothingMode.AntiAlias;
            g.Clear(Color.Black);

            // Scale and translate.
            RectangleF world_rect = new RectangleF(-4.0f, -4.4f, 8.0f, 7.3f);
            float cx = (world_rect.Left + world_rect.Right) / 2;
            float cy = (world_rect.Top + world_rect.Bottom) / 2;

            // Center the world coordinates at origin.
            g.TranslateTransform(-cx, -cy);

            // Scale to fill the form.
            float scale = Math.Min(W / world_rect.Width, H / world_rect.Height);
            g.ScaleTransform(scale, scale, MatrixOrder.Append);

            // Move the result to center on the form.
            g.TranslateTransform(W / 2, H / 2, MatrixOrder.Append);

            // Generate the points.
            PointF pt0, pt1;
            double t = 0;
            double expr = Math.Exp(Math.Cos(t)) - 2 * Math.Cos(4 * t) - Math.Pow(Math.Sin(t / 12), 5);
            pt1 = new PointF((float)(Math.Sin(t) * expr), (float)(-Math.Cos(t) * expr));
            using (Pen the_pen = new Pen(Color.Blue, 0))
            {
                const long num_lines = 5000;
                for (long i = 0; i < num_lines; i++)
                {
                    t = i * period * Math.PI / num_lines;
                    expr = Math.Exp(Math.Cos(t)) - 2 * Math.Cos(4 * t) - Math.Pow(Math.Sin(t / 12), 5);
                    pt0 = pt1;
                    pt1 = new PointF((float)(Math.Sin(t) * expr), (float)(-Math.Cos(t) * expr));
                    the_pen.Color = GetColor(t);
                    g.DrawLine(the_pen, pt0, pt1);
                }
            }
        }

        // Redraw the non-buffered butterfly curve.
        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {
            int W = pictureBox2.ClientSize.Width;
            int H = pictureBox2.ClientSize.Height;
            DrawButterfly(e.Graphics, W, H);
        }
    }
}
