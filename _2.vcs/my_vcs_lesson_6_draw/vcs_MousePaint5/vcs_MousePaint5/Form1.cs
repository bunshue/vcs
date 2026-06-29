using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;  // for SmoothingMode

// 滑鼠操作畫圖相關

namespace vcs_MousePaint5
{
    public partial class Form1 : Form
    {
        //pictureBox0 畫多邊形 ST

        // Each polygon is represented by a List<Point>.
        private List<List<Point>> Polygons0 = new List<List<Point>>();

        // Points for the new polygon.
        private List<Point> NewPolygon0 = null;

        // The current mouse position while drawing a new polygon.
        private Point NewPoint0;

        //pictureBox0 直多邊形 SP


        //pictureBox3 任意填滿直線 ST
        // The points selected by the user.
        private List<Point> ShapePoints = new List<Point>();
        private GraphicsPath ShapePath = null;
        private GraphicsPath LinesPath = null;
        private bool IsDrawing = false;
        //pictureBox3 任意填滿直線 SP


        //pictureBox4 內接最大矩形 ST
        private List<Point> m_Points = new List<Point>();
        //pictureBox4 內接最大矩形 SP

        // pictureBox5 sierpinski_gasket_skewed ST
        private List<Point> Corners = new List<Point>();
        private Point LastPoint;
        private int RADIUS = 2;
        // pictureBox5 sierpinski_gasket_skewed SP

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
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
            checkBox3.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            bt_clear4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            pictureBox5.Location = new Point(x_st + dx * 2, y_st + dy * 1);

            hScrollBar1.Size = new Size(W, 20);
            hScrollBar2.Size = new Size(W, 20);
            hScrollBar1.Location = new Point(x_st + dx * 1, y_st + dy * 0 + H - 20);
            hScrollBar2.Location = new Point(x_st + dx * 2, y_st + dy * 0 + H - 20);

            int dd = 26;
            label0.Location = new Point(x_st + dx * 0, y_st + dy * 0 - dd);
            label1.Location = new Point(x_st + dx * 1, y_st + dy * 0 - dd);
            label2.Location = new Point(x_st + dx * 2, y_st + dy * 0 - dd);
            label3.Location = new Point(x_st + dx * 0, y_st + dy * 1 - dd);
            label4.Location = new Point(x_st + dx * 1, y_st + dy * 1 - dd);
            label5.Location = new Point(x_st + dx * 2, y_st + dy * 1 - dd);
            label0.Text = "";
            label1.Text = "";
            label2.Text = "";
            label3.Text = "任意填滿直線";
            label4.Text = "內接最大矩形";
            label5.Text = "sierpinski gasket skewed";
            richTextBox1.Size = new Size(W - 200, H * 2 + 60);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1740, 940);
            this.Text = "vcs_MousePaint5";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
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

        //------------------------------------------------------------  # 60個

        // Start or continue drawing a new polygon.
        private void pictureBox0_MouseDown(object sender, MouseEventArgs e)
        {
            // See if we are already drawing a polygon.
            if (NewPolygon0 != null)
            {
                // We are already drawing a polygon.
                // If it's the right mouse button, finish this polygon.
                if (e.Button == MouseButtons.Right)
                {
                    // Finish this polygon.
                    if (NewPolygon0.Count > 2)
                    {
                        Polygons0.Add(NewPolygon0);
                    }
                    NewPolygon0 = null;
                }
                else
                {
                    // Add a point to this polygon.
                    if (NewPolygon0[NewPolygon0.Count - 1] != e.Location)
                    {
                        NewPolygon0.Add(e.Location);
                    }
                }
            }
            else
            {
                // Start a new polygon.
                NewPolygon0 = new List<Point>();
                NewPoint0 = e.Location;
                NewPolygon0.Add(e.Location);
            }

            // Redraw.
            pictureBox0.Invalidate();
        }

        // Move the next point in the new polygon.
        private void pictureBox0_MouseMove(object sender, MouseEventArgs e)
        {
            if (NewPolygon0 == null)
            {
                return;
            }
            NewPoint0 = e.Location;
            pictureBox0.Invalidate();
        }

        private void pictureBox0_MouseUp(object sender, MouseEventArgs e)
        {
        }

        // Redraw old polygons in blue. Draw the new polygon in green.
        // Draw the final segment dashed.
        private void pictureBox0_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            e.Graphics.Clear(pictureBox0.BackColor);

            e.Graphics.DrawString("左鍵點選頂點", new Font("標楷體", 30), new SolidBrush(Color.Green), new PointF(10, 10));
            e.Graphics.DrawString("右鍵結束", new Font("標楷體", 30), new SolidBrush(Color.Green), new PointF(10, 10 + 40));

            // Draw the old polygons.
            foreach (List<Point> polygon in Polygons0)
            {
                e.Graphics.FillPolygon(Brushes.White, polygon.ToArray());
                e.Graphics.DrawPolygon(Pens.Blue, polygon.ToArray());
            }

            // Draw the new polygon.
            if (NewPolygon0 != null)
            {
                // Draw the new polygon.
                if (NewPolygon0.Count > 1)
                {
                    e.Graphics.DrawLines(Pens.Green, NewPolygon0.ToArray());
                }

                // Draw the newest edge.
                if (NewPolygon0.Count > 0)
                {
                    using (Pen dashed_pen = new Pen(Color.Green))
                    {
                        dashed_pen.DashPattern = new float[] { 3, 3 };
                        e.Graphics.DrawLine(dashed_pen, NewPolygon0[NewPolygon0.Count - 1], NewPoint0);
                    }
                }
            }
        }

        //------------------------------------------------------------  # 60個

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {

        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void pictureBox2_MouseClick(object sender, MouseEventArgs e)
        {
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

        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void pictureBox3_MouseDown(object sender, MouseEventArgs e)
        {
            ShapePoints = new List<Point>();
            ShapePoints.Add(e.Location);
            IsDrawing = true;
            this.pictureBox3.Refresh();
        }

        private void pictureBox3_MouseMove(object sender, MouseEventArgs e)
        {
            if (!IsDrawing)
            {
                return;
            }
            ShapePoints.Add(e.Location);
            this.pictureBox3.Refresh();
            //Refresh();

            this.DoubleBuffered = true;
        }

        private void pictureBox3_MouseUp(object sender, MouseEventArgs e)
        {
            if (!IsDrawing)
            {
                return;
            }
            IsDrawing = false;

            // Generate the random lines to fill the shape.
            GenerateLines();

            //Refresh();
            this.pictureBox3.Refresh();
        }

        // Generate the random lines to fill the shape.
        private void GenerateLines()
        {
            if (ShapePoints.Count < 3)
            {
                ShapePath = null;
                LinesPath = null;
                return;
            }

            // Make the shape's path.
            ShapePath = new GraphicsPath();
            ShapePath.AddPolygon(ShapePoints.ToArray());

            // Get the shape's bounds.
            RectangleF bounds = ShapePath.GetBounds();
            int xmin = (int)(bounds.Left);
            int xmax = (int)(bounds.Right) + 1;
            int ymin = (int)(bounds.Top);
            int ymax = (int)(bounds.Bottom) + 1;

            // Generate random lines.
            LinesPath = new GraphicsPath();
            int num_lines = (int)((bounds.Width + bounds.Height) / 8);
            Random rand = new Random();
            int x1, y1, x2, y2;
            for (int i = 1; i <= num_lines / 2; i++)
            {
                x1 = rand.Next(xmin, xmax);
                y1 = ymin;
                x2 = rand.Next(xmin, xmax);
                y2 = ymax;
                LinesPath.AddLine(x1, y1, x2, y2);

                x1 = xmin;
                y1 = rand.Next(ymin, ymax);
                x2 = xmax;
                y2 = rand.Next(ymin, ymax);
                LinesPath.AddLine(x1, y1, x2, y2);
            }
        }

        private void pictureBox3_Paint(object sender, PaintEventArgs e)
        {
            // Draw the shape.
            if (IsDrawing)
            {
                // Draw the lines so far.
                if (ShapePoints.Count > 1)
                {
                    e.Graphics.DrawLines(Pens.Green, ShapePoints.ToArray());
                }
            }
            else
            {
                // Fill and outline the finished shape.
                if (ShapePath != null)
                {
                    if (checkBox3.Checked)
                    {
                        e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
                    }

                    e.Graphics.FillPath(Brushes.LightGreen, ShapePath);
                    e.Graphics.DrawPath(Pens.Green, ShapePath);

                    // Fill with the lines.
                    e.Graphics.SetClip(ShapePath);
                    e.Graphics.DrawPath(Pens.Green, LinesPath);
                }
            }
        }

        private void checkBox3_CheckedChanged(object sender, EventArgs e)
        {
            this.pictureBox3.Refresh();

        }

        //------------------------------------------------------------  # 60個

        //convex hull
        //中譯「凸包」或「凸殼」。
        //在高維空間中有一群散佈各處的點，「凸包」是包覆這群點的所有外殼當中，
        //表面積最小的一個外殼，而表面積最小的外殼一定是凸的。

        private void pictureBox4_MouseDown(object sender, MouseEventArgs e)
        {
            m_Points.Add(new Point(e.X, e.Y));
            this.pictureBox4.Invalidate();
        }

        private void pictureBox4_MouseMove(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox4_MouseUp(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox4_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(this.BackColor);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the convex hull.

            // Fill all of the points.
            foreach (Point pt in m_Points)
            {
                e.Graphics.FillEllipse(Brushes.Cyan, pt.X - 3, pt.Y - 3, 7, 7);
            }

            List<Point> hull = null;
            if (m_Points.Count >= 3)
            {
                // Get the convex hull.
                hull = Geometry.MakeConvexHull(m_Points);

                // Draw.
                // Fill the non-culled points.
                foreach (Point pt in Geometry.g_NonCulledPoints)
                {
                    e.Graphics.FillEllipse(Brushes.White, pt.X - 3, pt.Y - 3, 7, 7);
                }
            }

            // Draw all of the points.
            foreach (Point pt in m_Points)
            {
                e.Graphics.DrawEllipse(Pens.Black, pt.X - 3, pt.Y - 3, 7, 7);
            }

            if (m_Points.Count >= 3)
            {
                // Draw the MinMax quadrilateral.
                e.Graphics.DrawPolygon(Pens.Red, Geometry.g_MinMaxCorners);

                // Draw the culling box.
                e.Graphics.DrawRectangle(Pens.Orange, Geometry.g_MinMaxBox);

                // Draw the convex hull.
                Point[] hull_points = new Point[hull.Count];
                hull.CopyTo(hull_points);
                e.Graphics.DrawPolygon(Pens.Blue, hull_points);
            }
        }

        private void bt_clear4_Click(object sender, EventArgs e)
        {
            m_Points = new List<Point>();
            this.pictureBox4.Invalidate();
        }

        //------------------------------------------------------------  # 60個

        // pictureBox5 sierpinski_gasket_skewed ST

        int round5 = 0;

        private void pictureBox5_MouseDown(object sender, MouseEventArgs e)
        {
            if (timer5.Enabled)
            {
                // Stop running.
                timer5.Enabled = false;
                Corners = new List<Point>();
            }
            else
            {
                // Left or right button?
                if (e.Button == MouseButtons.Right)
                {
                    // Start running.
                    if (Corners.Count < 2)
                    {
                        // We need more points.
                        MessageBox.Show("Left-click at least two points before right-clicking.", "Need More Points", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
                    }
                    else
                    {
                        // Start at the first point.
                        LastPoint = Corners[0];

                        round5 = 0;
                        // Start.
                        timer5.Enabled = true;
                    }
                }
                else // Left button.
                {
                    // Save the point.
                    Corners.Add(new Point(e.X, e.Y));

                    // Draw the new point.
                    using (Graphics gr = this.pictureBox5.CreateGraphics())
                    {
                        if (Corners.Count == 1)
                        {
                            gr.Clear(this.pictureBox5.BackColor);
                        }
                        gr.DrawEllipse(Pens.Blue, e.X - RADIUS, e.Y - RADIUS, 2 * RADIUS, 2 * RADIUS);
                    }
                }
            }

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

        // Draw 1,000 points.
        private void timer5_Tick(object sender, EventArgs e)
        {
            richTextBox1.Text += round5.ToString() + " ";
            // Draw points.
            Random rand = new Random();
            using (Graphics gr = this.pictureBox5.CreateGraphics())
            {
                // Draw the corners.
                foreach (PointF pt in Corners)
                {
                    gr.FillEllipse(Brushes.White, pt.X - RADIUS, pt.Y - RADIUS, 2 * RADIUS, 2 * RADIUS);
                    gr.DrawEllipse(Pens.Blue, pt.X - RADIUS, pt.Y - RADIUS, 2 * RADIUS, 2 * RADIUS);
                }

                // Draw 1000 points.
                for (int i = 1; i <= 1000; i++)
                {
                    int j = rand.Next(0, Corners.Count);
                    LastPoint = new Point((LastPoint.X + Corners[j].X) / 2, (LastPoint.Y + Corners[j].Y) / 2);
                    gr.DrawLine(Pens.Blue, LastPoint.X, LastPoint.Y, LastPoint.X + 1, LastPoint.Y + 1);
                }
            }
            round5++;
            if (round5 > 10)
            {
                timer5.Enabled = false;
                Corners = new List<Point>();
            }
        }

        // pictureBox5 sierpinski_gasket_skewed SP

        //------------------------------------------------------------  # 60個
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/

