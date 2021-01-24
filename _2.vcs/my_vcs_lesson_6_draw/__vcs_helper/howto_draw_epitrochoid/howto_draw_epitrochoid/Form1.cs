using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace howto_draw_epitrochoid
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Redraw on resize.
        private void Form1_Load(object sender, EventArgs e)
        {
            this.ResizeRedraw = true;
        }

        // Redraw.
        private void btnRedraw_Click(object sender, EventArgs e)
        {
            picCanvas.Invalidate();
        }

        // Draw the epitrochoid.
        private void picCanvas_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            e.Graphics.Clear(picCanvas.BackColor);

            // Scale and center.
            float scale = Math.Min(
                picCanvas.ClientSize.Width * 0.45f,
                picCanvas.ClientSize.Height * 0.45f);
            e.Graphics.ScaleTransform(scale, scale);
            e.Graphics.TranslateTransform(
                picCanvas.ClientSize.Width / 2,
                picCanvas.ClientSize.Height / 2,
                System.Drawing.Drawing2D.MatrixOrder.Append);

            // Draw the curve.
            float a = float.Parse(txtA.Text);
            float b = float.Parse(txtB.Text);
            float h = float.Parse(txtH.Text);
            float dt = float.Parse(txtDt.Text);
            DrawEpitrochoid(e.Graphics, a, b, h, dt);
        }

        // Draw the curve on the indicated Graphics object.
        private void DrawEpitrochoid(Graphics gr, float a, float b, float h, float dt)
        {
            // Calculate the stop value for t.
            float stop_t = (float)(b * 2 * Math.PI);

            // Find the points.
            using (Pen the_pen = new Pen(Color.White, 0))
            {
                PointF pt0, pt1;
                pt0 = new PointF(X(a, b, h, 0), Y(a, b, h, 0));
                for (float t = dt; t <= stop_t; t += dt)
                {
                    pt1 = new PointF(X(a, b, h, t), Y(a, b, h, t));
                    gr.DrawLine(the_pen, pt0, pt1);
                    pt0 = pt1;
                }
            }
        }

        // The parametric function X(t).
        private float X(float a, float b, float h, float t)
        {
            float value = (float)((a + b) * Math.Cos(t) - h * Math.Cos(t * (a + b) / b));
            return value / (a + b + h);
        }

        // The parametric function Y(t).
        private float Y(float a, float b, float h, float t)
        {
            float value = (float)((a + b) * Math.Sin(t) - h * Math.Sin(t * (a + b) / b));
            return value / (a + b + h);
        }
    }
}
