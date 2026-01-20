using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for SmoothingMode

// 滑鼠操作畫圖相關

namespace vcs_MousePaint2
{
    public partial class Form1 : Form
    {
        //pictureBox0 直線連線 ST
        Point[] pt = new Point[300];
        int pt_index = -1;
        bool flag_mouse_down = false;
        //pictureBox0 直線連線 SP

        private List<Point> Points = new List<Point>();

        //pictureBox2 畫貝茲線 ST
        // The end points are points 0 and 3. 
        // The interior control points are points 1 and 2.
        private PointF[] Points2 = new PointF[4];
        // The index of the next point to define.
        private int NextPoint = 0;
        //pictureBox2 畫貝茲線 SP


        //pictureBox3 畫直線與圓的交點 ST
        // The circle's coordinates.
        float Cx, Cy, Radius;

        // The points on the line.
        PointF Point1, Point2;
        bool Drawing = false, HavePoints = false;

        // The points of intersection.
        PointF Intersection1, Intersection2;
        int NumIntersections;
        //pictureBox3 畫直線與圓的交點 SP


        //pictureBox4 ST
        // The circles.
        List<PointF> Centers = new List<PointF>();
        List<float> Radii = new List<float>();

        // The index of a new circle we are drawing.
        int NewCircle = -1;

        int currentX = 0;
        int currentY = 0;
        List<PointF> MarkPoint = new List<PointF>();
        //pictureBox4 SP

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            this.DoubleBuffered = true;

            //pictureBox3 畫直線與圓的交點 ST
            this.ResizeRedraw = true;

            // Get the circle's initial geometry.
            InitializeCircle();
            //pictureBox3 畫直線與圓的交點 SP
        }

        void show_item_location()
        {
            int W = 460;
            int H = 400;
            int x_st = 10;
            int y_st = 30;
            int dx = W + 20;
            int dy = H + 50;
            pictureBox0.Size = new Size(W, H);
            pictureBox1.Size = new Size(W, H);
            pictureBox2.Size = new Size(W, H);
            pictureBox3.Size = new Size(W, H);
            pictureBox4.Size = new Size(W, H);
            pictureBox5.Size = new Size(W, H);
            pictureBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox3.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            pictureBox5.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            int dd = 26;
            label0.Location = new Point(x_st + dx * 0, y_st + dy * 0 - dd);
            label1.Location = new Point(x_st + dx * 1, y_st + dy * 0 - dd);
            label2.Location = new Point(x_st + dx * 2, y_st + dy * 0 - dd);
            label3.Location = new Point(x_st + dx * 0, y_st + dy * 1 - dd);
            label4.Location = new Point(x_st + dx * 1, y_st + dy * 1 - dd);
            label5.Location = new Point(x_st + dx * 2, y_st + dy * 1 - dd);
            label0.Text = "直線連線";
            label1.Text = "";
            label2.Text = "點選4點畫貝茲線";
            label3.Text = "畫直線與圓的交點";
            label4.Text = "";
            label5.Text = "";
            richTextBox1.Size = new Size(W - 200, H * 2 + 60);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            bt_clear1.Location = new Point(pictureBox1.Location.X + pictureBox1.Size.Width - bt_clear1.Size.Width, pictureBox1.Location.Y + pictureBox1.Size.Height - bt_clear1.Size.Height);
            bt_clear4.Location = new Point(pictureBox4.Location.X + pictureBox4.Size.Width - bt_clear4.Size.Width, pictureBox4.Location.Y + pictureBox4.Size.Height - bt_clear4.Size.Height);
            bt_info4.Location = new Point(pictureBox4.Location.X + pictureBox4.Size.Width - bt_info4.Size.Width, pictureBox4.Location.Y);

            this.Size = new Size(1740, 940);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        // Force all threads to end.
        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            Environment.Exit(0);
        }

        private void pictureBox0_MouseDown(object sender, MouseEventArgs e)
        {
            flag_mouse_down = true;

            if (pt_index < (pt.Length - 1)) // 如果一維陣列內的 100 個位置還沒裝滿
            {
                pt_index++;  // 一維陣列 的索引往前
                pt[pt_index] = new Point(e.X, e.Y); // 存入 滑鼠游標位置
                this.pictureBox0.Invalidate(); // 要求表單重畫
            }
        }

        private void pictureBox0_MouseMove(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox0_MouseUp(object sender, MouseEventArgs e)
        {
            flag_mouse_down = false;
        }

        private void pictureBox0_Paint(object sender, PaintEventArgs e)
        {
            /*
            for (int i = 0; i <= pt_index; i++)
            {
                e.Graphics.DrawImage(img,
                pt[i].X - img.Width / 2, pt[i].Y - img.Height / 2, //影像左上角在表單的位置
                img.Width, img.Height); //影像的寬高
            }
            */
            //richTextBox1.Text += "index " + pt_index.ToString() + "\n";

            if (pt_index < 1)
            {
                return;
            }

            Point[] pt2 = new Point[pt_index + 1];
            int i;
            for (i = 0; i <= pt_index; i++)
            {
                pt2[i] = pt[i];
            }

            e.Graphics.DrawLines(new Pen(Color.Red, 2), pt2);

            /*
            //richTextBox1.Text += "idx = " + pt_index.ToString() + "\n";
                //Point[] pt2 = new Point[pt_index + 1];
                int i;
                for (i = 0; i <= pt_index; i++)
                {
                    //richTextBox1.Text += "draw i = " + i.ToString() + "\n";
                    e.Graphics.DrawEllipse(new Pen(Color.Red, 1), pt[i].X, pt[i].Y, 20, 20);
                }
            */
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            Points.Add(e.Location);
            Refresh();
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {

        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the points.
            foreach (Point point in Points)
            {
                e.Graphics.FillEllipse(Brushes.Black, point.X - 3, point.Y - 3, 5, 5);
            }
            if (Points.Count < 2)
            {
                return;
            }

            // Draw the curve.
            e.Graphics.DrawCurve(Pens.Red, Points.ToArray());

        }

        private void bt_clear1_Click(object sender, EventArgs e)
        {
            // Start a new point list.
            Points = new List<Point>();
            Refresh();
        }

        // Select a point.
        private void pictureBox2_MouseClick(object sender, MouseEventArgs e)
        {
            // If we're starting a new set of four points,
            // get the first point.
            if (NextPoint > 3)
            {
                NextPoint = 0;
            }

            // Save this point.
            Points2[NextPoint].X = e.X;
            Points2[NextPoint].Y = e.Y;

            // Move to the next point.
            NextPoint++;

            // Redraw.
            pictureBox2.Refresh();
        }

        private void pictureBox2_MouseDown(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox2_MouseMove(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox2_MouseUp(object sender, MouseEventArgs e)
        {
        }

        // Draw the currently selected points. 
        // If we have four points, draw the Bezier curve.
        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            e.Graphics.Clear(pictureBox2.BackColor);
            if (NextPoint >= 4)
            {
                // Draw the curve.
                e.Graphics.DrawBezier(Pens.Red, Points2[0], Points2[1], Points2[2], Points2[3]);
            }

            // Draw the control points.
            for (int i = 0; i < NextPoint; i++)
            {
                e.Graphics.FillRectangle(Brushes.White, Points2[i].X - 3, Points2[i].Y - 3, 6, 6);
                e.Graphics.DrawRectangle(Pens.Black, Points2[i].X - 3, Points2[i].Y - 3, 6, 6);
            }
        }

        //pictureBox3 畫直線與圓的交點 ST

        // Get the points.
        private void pictureBox3_MouseDown(object sender, MouseEventArgs e)
        {
            Drawing = true;
            NumIntersections = 0;
            Point1 = new PointF(e.X, e.Y);
            Point2 = new PointF(e.X, e.Y);
            HavePoints = true;
            this.pictureBox3.Invalidate();
        }

        private void pictureBox3_MouseMove(object sender, MouseEventArgs e)
        {
            if (!Drawing)
            {
                return;
            }
            Point2 = new PointF(e.X, e.Y);
            this.pictureBox3.Invalidate();
        }

        private void pictureBox3_MouseUp(object sender, MouseEventArgs e)
        {
            Drawing = false;

            // Find and draw the intersections.
            NumIntersections = FindLineCircleIntersections(Cx, Cy, Radius, Point1, Point2, out Intersection1, out Intersection2);
            this.pictureBox3.Invalidate();
        }

        // Draw the circle and the segment if we have it.
        private void pictureBox3_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the circle.
            e.Graphics.DrawEllipse(Pens.Blue, Cx - Radius, Cy - Radius, Radius * 2, Radius * 2);

            // Draw a dashed line from the segment points
            // to the points of intersection.
            if (HavePoints && (NumIntersections > 0))
            {
                using (Pen dashed_pen = new Pen(Color.Red))
                {
                    dashed_pen.DashPattern = new float[] { 3, 3 };
                    e.Graphics.DrawLine(dashed_pen, Intersection1, Point1);
                }
            }

            // Draw the intersections (if we have them).
            switch (NumIntersections)
            {
                case 0:
                    break;
                case 1:
                    DrawPoint(e.Graphics, Intersection1, Brushes.HotPink, Pens.Red);
                    break;
                case 2:
                    DrawPoint(e.Graphics, Intersection1, Brushes.HotPink, Pens.Red);
                    DrawPoint(e.Graphics, Intersection2, Brushes.HotPink, Pens.Red);
                    break;
            }

            // Draw the segment.
            if (HavePoints)
            {
                DrawPoint(e.Graphics, Point1, Brushes.White, Pens.Black);
                DrawPoint(e.Graphics, Point2, Brushes.White, Pens.Black);
                e.Graphics.DrawLine(Pens.BlueViolet, Point1, Point2);
            }
        }

        private void InitializeCircle()
        {
            Cx = this.pictureBox3.ClientSize.Width / 2;
            Cy = this.pictureBox3.ClientSize.Height / 2;
            Radius = (float)(Math.Min(Cx, Cy) * 0.8);
            HavePoints = false;
            this.pictureBox3.Invalidate();
        }

        // Find the points of intersection.
        private int FindLineCircleIntersections(float cx, float cy, float radius, PointF point1, PointF point2, out PointF intersection1, out PointF intersection2)
        {
            float dx, dy, A, B, C, det, t;

            dx = point2.X - point1.X;
            dy = point2.Y - point1.Y;

            A = dx * dx + dy * dy;
            B = 2 * (dx * (point1.X - cx) + dy * (point1.Y - cy));
            C = (point1.X - cx) * (point1.X - cx) + (point1.Y - cy) * (point1.Y - cy) - radius * radius;

            det = B * B - 4 * A * C;
            if ((A <= 0.0000001) || (det < 0))
            {
                // No real solutions.
                intersection1 = new PointF(float.NaN, float.NaN);
                intersection2 = new PointF(float.NaN, float.NaN);
                return 0;
            }
            else if (det == 0)
            {
                // One solution.
                t = -B / (2 * A);
                intersection1 = new PointF(point1.X + t * dx, point1.Y + t * dy);
                intersection2 = new PointF(float.NaN, float.NaN);
                return 1;
            }
            else
            {
                // Two solutions.
                t = (float)((-B + Math.Sqrt(det)) / (2 * A));
                intersection1 = new PointF(point1.X + t * dx, point1.Y + t * dy);
                t = (float)((-B - Math.Sqrt(det)) / (2 * A));
                intersection2 = new PointF(point1.X + t * dx, point1.Y + t * dy);
                return 2;
            }
        }

        // Draw a point.
        private void DrawPoint(Graphics gr, PointF pt, Brush brush, Pen pen)
        {
            const int RADIUS = 3;
            gr.FillEllipse(brush, pt.X - RADIUS, pt.Y - RADIUS, 2 * RADIUS, 2 * RADIUS);
            gr.DrawEllipse(pen, pt.X - RADIUS, pt.Y - RADIUS, 2 * RADIUS, 2 * RADIUS);
        }

        //pictureBox3 畫直線與圓的交點 SP


        // Start drawing a new circle.
        private void pictureBox4_MouseDown(object sender, MouseEventArgs e)
        {
            MarkPoint.Add(e.Location);
            Centers.Add(e.Location);
            Radii.Add(0);
            NewCircle = Centers.Count - 1;
        }

        // Update the new circle.
        private void pictureBox4_MouseMove(object sender, MouseEventArgs e)
        {
            currentX = e.X;
            currentY = e.Y;
            this.pictureBox4.Invalidate();

            if (NewCircle < 0) return;
            float dx = e.X - Centers[NewCircle].X;
            float dy = e.Y - Centers[NewCircle].Y;
            Radii[NewCircle] = (float)Math.Sqrt(dx * dx + dy * dy);
            currentX = e.X;
            currentY = e.Y;
            this.pictureBox4.Invalidate();
        }

        // Finish drawing a new circle.
        private void pictureBox4_MouseUp(object sender, MouseEventArgs e)
        {
            // If the radius is 0, remove the new circle.
            if (Radii[NewCircle] < 1)
            {
                Centers.RemoveAt(NewCircle);
                Radii.RemoveAt(NewCircle);
            }
            //richTextBox1.Text += "i = " + NewCircle.ToString() + "cx=" + centers[i].X.ToString() + ", cy = " + centers[i].Y.ToString() + ", R = " + radii[i].ToString() + "\n";

            NewCircle = -1;
            this.pictureBox4.Invalidate();
        }

        // Draw the circles.
        private void pictureBox4_Paint(object sender, PaintEventArgs e)
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

        // Find the intersection of all of the circles.
        private Region FindCircleIntersections(List<PointF> centers, List<float> radii)
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


        private void pictureBox5_MouseDown(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox5_MouseMove(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox5_MouseUp(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox5_Paint(object sender, PaintEventArgs e)
        {
        }

        private void bt_clear4_Click(object sender, EventArgs e)
        {
            // Remove all circles.
            Centers = new List<PointF>();
            MarkPoint = new List<PointF>();
            Radii = new List<float>();
            this.pictureBox4.Invalidate();
        }

        private void bt_info4_Click(object sender, EventArgs e)
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

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//------------------------------------------------------------

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個


/*  可搬出

*/
