using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace howto_scale_drawing
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

        // Draw some smiley faces.
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            int W = 500;
            int H = 500;
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            RectangleF smiley_rect = new RectangleF(-1, -1, 2, 2);

            float wid = (W - 1) / 2;
            float hgt = (H - 1) / 2;

            // 左上
            MapDrawing(e.Graphics, smiley_rect, new RectangleF(0, 0, wid, hgt), false);
            DrawSmiley(e.Graphics);

            // 左下
            MapDrawing(e.Graphics, smiley_rect, new RectangleF(0, hgt, wid, hgt), false);
            DrawSmiley(e.Graphics);

            // 右
            MapDrawing(e.Graphics, smiley_rect, new RectangleF(wid, 0, wid, 2 * hgt), true);
            DrawSmiley(e.Graphics);
        }

        // Map a drawing coordinate rectangle to a graphics object rectangle.
        private void MapDrawing(Graphics g, RectangleF drawing_rect, RectangleF target_rect, bool stretch)
        {
            if ((target_rect.Width < 1) || (target_rect.Height < 1))
            {
                return;
            }

            g.ResetTransform();

            // Center the drawing area at the origin.
            float drawing_cx = (drawing_rect.Left + drawing_rect.Right) / 2;
            float drawing_cy = (drawing_rect.Top + drawing_rect.Bottom) / 2;
            g.TranslateTransform(-drawing_cx, -drawing_cy);

            // Scale.
            // Get scale factors for both directions.
            float scale_x = target_rect.Width / drawing_rect.Width;
            float scale_y = target_rect.Height / drawing_rect.Height;
            if (!stretch)
            {
                // To preserve the aspect ratio, use the smaller scale factor.
                scale_x = Math.Min(scale_x, scale_y);
                scale_y = scale_x;
            }
            g.ScaleTransform(scale_x, scale_y, MatrixOrder.Append);

            // Translate to center over the drawing area.
            float graphics_cx = (target_rect.Left + target_rect.Right) / 2;
            float graphics_cy = (target_rect.Top + target_rect.Bottom) / 2;
            g.TranslateTransform(graphics_cx, graphics_cy, MatrixOrder.Append);
        }

        // Draw a smiley face in the area (-1, -1)-(1, 1).
        private void DrawSmiley(Graphics g)
        {
            g.DrawRectangle(new Pen(Color.Red, 0), -1, -1, 2, 2);

            Pen thin_pen = new Pen(Color.Black, 0);
            g.FillEllipse(Brushes.Yellow, -1, -1, 2, 2);
            g.DrawEllipse(thin_pen, -1, -1, 2, 2);

            g.FillEllipse(Brushes.LightGreen, -0.5f, -0.5f, 0.3f, 0.5f);
            g.DrawEllipse(thin_pen, -0.5f, -0.5f, 0.3f, 0.5f);
            g.FillEllipse(Brushes.Black, -0.4f, -0.4f, 0.2f, 0.3f);

            g.FillEllipse(Brushes.LightGreen, 0.2f, -0.5f, 0.3f, 0.5f);
            g.DrawEllipse(thin_pen, 0.2f, -0.5f, 0.3f, 0.5f);
            g.FillEllipse(Brushes.Black, 0.3f, -0.4f, 0.2f, 0.3f);

            g.FillEllipse(Brushes.LightBlue, -0.2f, -0.1f, 0.4f, 0.6f);
            g.DrawEllipse(thin_pen, -0.2f, -0.1f, 0.4f, 0.6f);

            g.DrawArc(thin_pen, -0.75f, -0.75f, 1.5f, 1.5f, 20, 120);
        }
    }
}
