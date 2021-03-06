using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace vcs_DrawK_Circle1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The circles.
        List<PointF> Centers = new List<PointF>();
        List<float> Radii = new List<float>();

        // The index of a new circle we are drawing.
        int NewCircle = -1;

        int currentX = 0;
        int currentY = 0;
        List<PointF> MarkPoint = new List<PointF>();

        // Remove all circles.
        private void btnClear_Click(object sender, EventArgs e)
        {
            Centers = new List<PointF>();
            MarkPoint = new List<PointF>();
            Radii = new List<float>();
            this.Invalidate();
        }

        // Draw the circles.
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            int W = this.Size.Width;
            int H = this.Size.Height;
            Point pt1 = new Point();
            Point pt2 = new Point();
            pt1.X = 0;
            pt1.Y = H / 2;
            pt2.X = W;
            pt2.Y = H / 2;

            //e.Graphics.DrawLine(Pens.Red, 0, H / 2, W, H / 2);
            //e.Graphics.DrawLine(Pens.Red, W / 2, 0, W / 2, H);

            e.Graphics.DrawLine(Pens.Red, 0, currentY, W, currentY);  //橫線
            e.Graphics.DrawLine(Pens.Red, currentX, 0, currentX, H);  //直線


            // Find the intersection of all circles.
            Region intersection = FindCircleIntersections(Centers, Radii);

            // Draw the region.
            if (intersection != null)
            {
                e.Graphics.FillRegion(Brushes.LightGreen, intersection);
            }

            int i;
            // Draw the circles.
            for (i = 0; i < Centers.Count; i++)
            {
                e.Graphics.DrawEllipse(Pens.Blue, Centers[i].X - Radii[i], Centers[i].Y - Radii[i], 2 * Radii[i], 2 * Radii[i]);
                e.Graphics.DrawEllipse(Pens.Red, Centers[i].X - 10, Centers[i].Y - 10, 20, 20);
            }

            // Draw the circles.
            for (i = 0; i < MarkPoint.Count; i++)
            {
                e.Graphics.DrawEllipse(Pens.Red, MarkPoint[i].X - 10, MarkPoint[i].Y - 10, 20, 20);
            }

            //e.Graphics.DrawLines(Pens.Pink, MarkPoint);


            //richTextBox1.Text += "i = " + i.ToString() + ", cx = " + MarkPoint[i].X + ", cy = " + MarkPoint[i].Y + "\n";

        }

        // Start drawing a new circle.
        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            MarkPoint.Add(e.Location);
            Centers.Add(e.Location);
            Radii.Add(0);
            NewCircle = Centers.Count - 1;
        }

        // Update the new circle.
        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            currentX = e.X;
            currentY = e.Y;
            this.Invalidate();

            if (NewCircle < 0) return;
            float dx = e.X - Centers[NewCircle].X;
            float dy = e.Y - Centers[NewCircle].Y;
            Radii[NewCircle] = (float)Math.Sqrt(dx * dx + dy * dy);
            currentX = e.X;
            currentY = e.Y;
            this.Invalidate();
        }

        // Finish drawing a new circle.
        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            // If the radius is 0, remove the new circle.
            if (Radii[NewCircle] < 1)
            {
                Centers.RemoveAt(NewCircle);
                Radii.RemoveAt(NewCircle);
            }
            //richTextBox1.Text += "i = " + NewCircle.ToString() + "cx=" + centers[i].X.ToString() + ", cy = " + centers[i].Y.ToString() + ", R = " + radii[i].ToString() + "\n";

            NewCircle = -1;
            this.Invalidate();
        }

        // Find the intersection of all of the circles.
        private Region FindCircleIntersections(List<PointF>centers, List<float>radii)
        {
            if (centers.Count < 1) return null;

            // Make a region.
            Region result_region = new Region();
            
            // Intersect the region with the circles.
            for (int i = 0; i < centers.Count; i++)
            {
                using (GraphicsPath circle_path = new GraphicsPath())
                {
                    circle_path.AddEllipse(
                        centers[i].X - radii[i], centers[i].Y - radii[i],
                        2 * radii[i], 2 * radii[i]);
                    result_region.Intersect(circle_path);
                }
                //richTextBox1.Text += "i = " + i.ToString() + "cx=" + centers[i].X.ToString() + ", cy = " + centers[i].Y.ToString() + ", R = " + radii[i].ToString() + "\n";
            }

            return result_region;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int len = Centers.Count;
            richTextBox1.Text += "len =" + len.ToString() + "\n";
            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + ", cx = " + Centers[i].X + ", cy = " + Centers[i].Y + ", r = " + Radii[i].ToString() + "\n";

            }

            len = MarkPoint.Count;
            richTextBox1.Text += "len =" + len.ToString() + "\n";
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + ", cx = " + MarkPoint[i].X + ", cy = " + MarkPoint[i].Y + "\n";

            }


        }
    }
}
