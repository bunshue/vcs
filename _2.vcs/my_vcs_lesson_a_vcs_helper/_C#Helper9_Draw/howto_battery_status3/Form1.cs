using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace howto_battery_status3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            ShowPowerStatus();
        }
        private void timer1_Tick(object sender, EventArgs e)
        {
            ShowPowerStatus();
        }

        float a = 0;
        private void ShowPowerStatus()
        {
            PowerStatus status = SystemInformation.PowerStatus;
            float percent = status.BatteryLifePercent;

            a += 0.023f;
            percent -= a;

            if (percent < 0)
            {
                percent = 1;
                a = 0;
            }

            //richTextBox1.Text += percent.ToString("P0") + "\n";

            // Draw the battery image.
            Color bg_color = Color.Transparent;
            Color outline_color = Color.Gray;
            Color charged_color = Color.LightGreen;
            Color uncharged_color = Color.White;
            if (percent < 0.15f)
            {
                outline_color = Color.Black;
                charged_color = Color.Red;
                uncharged_color = Color.Yellow;
            }
            else if (percent < 0.25f)
            {
                outline_color = Color.Black;
                charged_color = Color.Orange;
            }
            pictureBox1.Image = DrawBattery(
                percent,
                pictureBox1.ClientSize.Width,
                pictureBox1.ClientSize.Height,
                bg_color, outline_color,
                charged_color, uncharged_color,
                true);
        }

        private Bitmap DrawBattery(
            float percent, int w, int h,
            Color bg_color, Color outline_color,
            Color charged_color, Color uncharged_color,
            bool striped)
        {
            // Bail if there's no room to draw.
            if ((w < 1) || (h < 1))
            {
                return null;
            }

            Bitmap bm = new Bitmap(w, h);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                // If the battery has a horizontal orientation,
                // rotate so we can draw it vertically.
                if (w > h)
                {
                    gr.RotateTransform(90, MatrixOrder.Append);
                    gr.TranslateTransform(w, 0, MatrixOrder.Append);
                    int temp = w;
                    w = h;
                    h = temp;
                }

                // Draw the battery.
                DrawVerticalBattery(gr, percent, w, h, bg_color,
                    outline_color, charged_color, uncharged_color, striped);
            }
            return bm;
        }

        // Draw a vertically oriented battery with
        // the indicated percentage filled in.
        private void DrawVerticalBattery(Graphics gr,
            float percent, int w, int h,
            Color bg_color, Color outline_color,
            Color charged_color, Color uncharged_color,
            bool striped)
        {
            gr.Clear(bg_color);
            gr.SmoothingMode = SmoothingMode.AntiAlias;

            // Make a rectangle for the main body.
            float thickness = h / 20f;
            RectangleF body_rect = new RectangleF(
                thickness * 0.5f, thickness * 1.5f,
                w - thickness, h - thickness * 2f);

            using (Pen pen = new Pen(outline_color, thickness))
            {
                // Fill the body with the uncharged color.
                using (Brush brush = new SolidBrush(uncharged_color))
                {
                    gr.FillRectangle(brush, body_rect);
                }

                // Fill the charged area.
                float charged_hgt = body_rect.Height * percent;
                RectangleF charged_rect = new RectangleF(
                    body_rect.Left, body_rect.Bottom - charged_hgt,
                    body_rect.Width, charged_hgt);
                using (Brush brush = new SolidBrush(charged_color))
                {
                    gr.FillRectangle(brush, charged_rect);
                }

                // Optionally stripe multiples of 25%
                if (striped)
                    for (int i = 1; i <= 3; i++)
                    {
                        float y = body_rect.Bottom - i * 0.25f * body_rect.Height;
                        gr.DrawLine(pen, body_rect.Left, y, body_rect.Right, y);
                    }

                // Draw the main body.
                gr.DrawPath(pen, MakeRoundedRect(body_rect, thickness, thickness, true, true, true, true));

                // Draw the positive terminal.
                RectangleF terminal_rect = new RectangleF(w / 2f - thickness, 0, 2 * thickness, thickness);
                gr.DrawPath(pen, MakeRoundedRect(terminal_rect, thickness / 2f, thickness / 2f, true, true, false, false));
            }
        }

        // Draw a rectangle in the indicated Rectangle
        // rounding the indicated corners.
        private GraphicsPath MakeRoundedRect(
            RectangleF rect, float xradius, float yradius,
            bool round_ul, bool round_ur, bool round_lr, bool round_ll)
        {
            // Make a GraphicsPath to draw the rectangle.
            PointF point1, point2;
            GraphicsPath path = new GraphicsPath();

            // Upper left corner.
            if (round_ul)
            {
                RectangleF corner = new RectangleF(rect.X, rect.Y, 2 * xradius, 2 * yradius);
                path.AddArc(corner, 180, 90);
                point1 = new PointF(rect.X + xradius, rect.Y);
            }
            else point1 = new PointF(rect.X, rect.Y);

            // Top side.
            if (round_ur)
            {
                point2 = new PointF(rect.Right - xradius, rect.Y);
            }
            else
            {
                point2 = new PointF(rect.Right, rect.Y);
            }
            path.AddLine(point1, point2);

            // Upper right corner.
            if (round_ur)
            {
                RectangleF corner = new RectangleF(rect.Right - 2 * xradius, rect.Y, 2 * xradius, 2 * yradius);
                path.AddArc(corner, 270, 90);
                point1 = new PointF(rect.Right, rect.Y + yradius);
            }
            else point1 = new PointF(rect.Right, rect.Y);

            // Right side.
            if (round_lr)
            {
                point2 = new PointF(rect.Right, rect.Bottom - yradius);
            }
            else
            {
                point2 = new PointF(rect.Right, rect.Bottom);
            }
            path.AddLine(point1, point2);

            // Lower right corner.
            if (round_lr)
            {
                RectangleF corner = new RectangleF(rect.Right - 2 * xradius, rect.Bottom - 2 * yradius, 2 * xradius, 2 * yradius);
                path.AddArc(corner, 0, 90);
                point1 = new PointF(rect.Right - xradius, rect.Bottom);
            }
            else point1 = new PointF(rect.Right, rect.Bottom);

            // Bottom side.
            if (round_ll)
            {
                point2 = new PointF(rect.X + xradius, rect.Bottom);
            }
            else
            {
                point2 = new PointF(rect.X, rect.Bottom);
            }
            path.AddLine(point1, point2);

            // Lower left corner.
            if (round_ll)
            {
                RectangleF corner = new RectangleF(rect.X, rect.Bottom - 2 * yradius, 2 * xradius, 2 * yradius);
                path.AddArc(corner, 90, 90);
                point1 = new PointF(rect.X, rect.Bottom - yradius);
            }
            else
            {
                point1 = new PointF(rect.X, rect.Bottom);
            }

            // Left side.
            if (round_ul)
            {
                point2 = new PointF(rect.X, rect.Y + yradius);
            }
            else
            {
                point2 = new PointF(rect.X, rect.Y);
            }
            path.AddLine(point1, point2);

            // Join with the start point.
            path.CloseFigure();

            return path;
        }
    }
}

