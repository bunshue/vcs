using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace howto_rects_from_segment
{
    public partial class Form1 : Form
    {
        private PointF Point1, Point2;
        private List<PointF[]> Rectangles = new List<PointF[]>();
        private bool Drawing = false;

        private Brush[] RectBrushes =
        {
            new SolidBrush(Color.FromArgb(128, Color.Red)),
            new SolidBrush(Color.FromArgb(128, Color.Red)),
            new SolidBrush(Color.FromArgb(128, Color.Blue)),
            new SolidBrush(Color.FromArgb(128, Color.Blue)),
        };

        private Pen[] RectPens =
        {
            Pens.Red,
            Pens.Red,
            Pens.Blue,
            Pens.Blue,
        };

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            Point1 = e.Location;
            Point2 = e.Location;
            Rectangles = new List<PointF[]>();
            pictureBox1.Refresh();
            Drawing = true;
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (!Drawing) return;
            Point2 = e.Location;
            pictureBox1.Refresh();
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            if (!Drawing) return;
            Drawing = false;

            float aspect_ratio = 0.75f;

            Rectangles = FindRectangles(aspect_ratio, Point1, Point2);

            pictureBox1.Refresh();
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(pictureBox1.BackColor);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            for (int i = 0; i < Rectangles.Count; i++)
            {
                e.Graphics.FillPolygon(RectBrushes[i], Rectangles[i]);
                e.Graphics.DrawPolygon(RectPens[i], Rectangles[i]);
            }

            if (Point1 != Point2)
            {
                e.Graphics.DrawLine(Pens.Black, Point1, Point2);
            }
        }

        private List<PointF[]> FindRectangles(float aspect_ratio, PointF p1, PointF p2)
        {
            // Get the vector p1 --> p2.
            float vx = p2.X - p1.X;
            float vy = p2.Y - p1.Y;
            if (Math.Sqrt(vx * vx + vy * vy) < 0.1) return null;

            PointF p3, p4;
            List<PointF[]> result = new List<PointF[]>();
            float perp_x, perp_y;

            // Make rectangle 1.
            perp_x = vy * aspect_ratio;
            perp_y = -vx * aspect_ratio;
            p3 = new PointF(p2.X + perp_x, p2.Y + perp_y);
            p4 = new PointF(p1.X + perp_x, p1.Y + perp_y);
            result.Add(new PointF[] { p1, p2, p3, p4 });

            // Make rectangle 2.
            p3 = new PointF(p2.X - perp_x, p2.Y - perp_y);
            p4 = new PointF(p1.X - perp_x, p1.Y - perp_y);
            result.Add(new PointF[] { p1, p2, p3, p4 });

            // Make rectangle 3.
            perp_x = vy / aspect_ratio;
            perp_y = -vx / aspect_ratio;
            p3 = new PointF(p2.X + perp_x, p2.Y + perp_y);
            p4 = new PointF(p1.X + perp_x, p1.Y + perp_y);
            result.Add(new PointF[] { p1, p2, p3, p4 });

            // Make rectangle 4.
            p3 = new PointF(p2.X - perp_x, p2.Y - perp_y);
            p4 = new PointF(p1.X - perp_x, p1.Y - perp_y);
            result.Add(new PointF[] { p1, p2, p3, p4 });

            return result;
        }

        private void txtAspectRatio_TextChanged(object sender, EventArgs e)
        {
            Point1 = new PointF();
            Point2 = new PointF();
            Rectangles = new List<PointF[]>();
            pictureBox1.Refresh();
        }

    }
}
