using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat
using System.Drawing.Drawing2D; //for CompositingQuality, SmoothingMode

namespace vcs_Draw9_Example5_vcsh
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;
        int W = 450;
        int H = 450;

        // kaleidoscope_萬花筒
        // The polylines we are drawing.
        List<List<Point>> Polylines = new List<List<Point>>();
        List<Point> NewPolyline = null;


        // Orientations for the rectangles.
        private enum RectOrientations
        {
            RemoveLeft,
            RemoveTop,
            RemoveRight,
            RemoveBottom
        }

        #region spiral_of_theodorus
        // Return an array of rainbow colors.
        private Color[] RainbowColors(byte alpha)
        {
            return new Color[]
            {
                Color.FromArgb(alpha, 255, 0, 0),
                Color.FromArgb(alpha, 255, 255, 0),
                Color.FromArgb(alpha, 255, 128, 0),
                Color.FromArgb(alpha, 0, 255, 0),
                Color.FromArgb(alpha, 0, 255, 255),
                Color.FromArgb(alpha, 0, 0, 255),
                Color.FromArgb(alpha, 255, 0, 255),
            };
        }

        // Convert colors to brushes.
        private Brush[] ColorsToBrushes(Color[] colors)
        {
            int num_colors = colors.Length;
            Brush[] brushes = new Brush[num_colors];
            for (int i = 0; i < num_colors; i++)
                brushes[i] = new SolidBrush(colors[i]);
            return brushes;
        }
        #endregion spiral_of_theodorus


        #region epitrochoid長短輻圓外旋輪線；外旋輪線

        // The curve's parameters.
        private float a, b, h, dt;

        // The curve's points.
        private PointF[] Points = null;
        private float[] Thetas = null;

        // The maximum index we should draw.
        private int MaxPointToDraw = 0;

        #endregion epitrochoid長短輻圓外旋輪線；外旋輪線

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
            DrawPhiSpiralBitmap();
            this.ResizeRedraw = true;
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            DrawPhiSpiralBitmap();
        }

        void show_item_location()
        {
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new System.Drawing.Point(0, 0);

            int x_st;
            int y_st;
            int dx;
            int dy;

            x_st = 10;
            y_st = 35;
            dx = W + 120;
            dy = H + 80;

            pictureBox0.Size = new Size(W, H);
            pictureBox1.Size = new Size(W, H);
            pictureBox2.Size = new Size(W, H);
            pictureBox3.Size = new Size(W, H - 50);
            pictureBox4.Size = new Size(W, H);
            pictureBox5.Size = new Size(W, H);
            pictureBox0.BorderStyle = BorderStyle.Fixed3D;
            pictureBox1.BorderStyle = BorderStyle.Fixed3D;
            pictureBox2.BorderStyle = BorderStyle.Fixed3D;
            pictureBox3.BorderStyle = BorderStyle.Fixed3D;
            pictureBox4.BorderStyle = BorderStyle.Fixed3D;
            pictureBox5.BorderStyle = BorderStyle.Fixed3D;

            pictureBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox3.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            pictureBox5.Location = new Point(x_st + dx * 2, y_st + dy * 1);

            groupBox1.Location = new Point(x_st + dx * 0, y_st + dy * 1 - 80);
            int dd = 40;
            rb2.Location = new Point(rb1.Location.X + dd * 1, rb1.Location.Y);
            rb3.Location = new Point(rb1.Location.X + dd * 2, rb1.Location.Y);
            rb4.Location = new Point(rb1.Location.X + dd * 3, rb1.Location.Y);
            rb5.Location = new Point(rb1.Location.X + dd * 4, rb1.Location.Y);
            rb6.Location = new Point(rb1.Location.X + dd * 5, rb1.Location.Y);

            groupBox2.Location = new Point(x_st + dx * 0, y_st + dy * 2 - 110);
            groupBox3.Location = new Point(x_st + dx * 2, y_st + dy * 1 - 80);
            groupBox4.Location = new Point(x_st + dx * 1, y_st + dy * 1 - 80);

            bt_save.Location = new Point(x_st + dx * 3 - 50, y_st + dy * 0 + 0);

            richTextBox1.Location = new Point(x_st + dx * 3 - 50, y_st + dy * 0 + 50 + 50);

            //richTextBox1.Size = new Size(bt_exit.Right - richTextBox1.Location.X, this.Height - richTextBox1.Location.Y - 25);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //ClientSize = new Size(bt_exit.Right + 10, richTextBox1.Bottom + 80);    //自動表單邊界

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            bt_exit_setup();
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            bitmap1 = null;
            richTextBox1.Clear();
        }

        void save_image_to_drive()
        {
            if (bitmap1 != null)
            {
                string filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                string filename1 = filename + ".jpg";
                string filename2 = filename + ".bmp";
                string filename3 = filename + ".png";

                try
                {
                    bitmap1.Save(@filename1, ImageFormat.Jpeg);
                    bitmap1.Save(@filename2, ImageFormat.Bmp);
                    bitmap1.Save(@filename3, ImageFormat.Png);

                    richTextBox1.Text += "存檔成功\n";
                    richTextBox1.Text += "已存檔 : " + filename1 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename3 + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }
            else
                richTextBox1.Text += "無圖可存\n";
        }

        private void bt_save_Click(object sender, EventArgs e)
        {
            save_image_to_drive();
        }

        // Force all threads to end.
        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            Environment.Exit(0);
        }

        #region 萬花筒
        // Start drawing.
        private void pictureBox0_MouseDown(object sender, MouseEventArgs e)
        {
            NewPolyline = new List<Point>();
            Polylines.Add(NewPolyline);
            NewPolyline.Add(e.Location);
        }

        // Continue drawing.
        private void pictureBox0_MouseMove(object sender, MouseEventArgs e)
        {
            if (NewPolyline == null) return;
            NewPolyline.Add(e.Location);
            pictureBox0.Refresh();
        }

        // Stop drawing.
        private void pictureBox0_MouseUp(object sender, MouseEventArgs e)
        {
            if (NewPolyline == null) return;
            NewPolyline = null;
            pictureBox0.Refresh();
        }

        // Draw the polylines.
        private void pictureBox0_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Make a list of transformations, starting with the identity.
            List<Matrix> matrices = new List<Matrix>();
            matrices.Add(new Matrix());

            // Make transformation matrices for the selected style.
            int wid = pictureBox0.ClientSize.Width;
            int hgt = pictureBox0.ClientSize.Height;
            Rectangle src_rect = new Rectangle(0, 0, wid, hgt);
            if (rb1.Checked || rb3.Checked)
            {
                // Reflect across X axis.
                Point[] pts = { new Point(wid, 0), new Point(0, 0), new Point(wid, hgt) };
                Matrix mat = new Matrix(src_rect, pts);
                matrices.Add(mat);
            }
            if (rb2.Checked || rb3.Checked)
            {
                // Reflect across Y axis.
                Point[] pts = { new Point(0, hgt), new Point(wid, hgt), new Point(0, 0) };
                Matrix mat = new Matrix(src_rect, pts);
                matrices.Add(mat);
            }
            if (rb3.Checked)
            {
                // Reflect across X and Y axes.
                Point[] pts = { new Point(wid, hgt), new Point(0, hgt), new Point(wid, 0) };
                Matrix mat = new Matrix(src_rect, pts);
                matrices.Add(mat);
            }
            if (rb4.Checked)
            {
                // Rotate 180 degrees.
                Matrix mat = new Matrix();
                mat.RotateAt(180, new PointF(wid / 2, hgt / 2));
                matrices.Add(mat);
            }
            if (rb5.Checked)
            {
                // Rotate 90 degrees three times.
                for (int i = 1; i <= 3; i++)
                {
                    Matrix mat = new Matrix();
                    mat.RotateAt(i * 90, new PointF(wid / 2, hgt / 2));
                    matrices.Add(mat);
                }
            }
            if (rb6.Checked)
            {
                // Rotate 45 degrees seven times.
                for (int i = 1; i <= 7; i++)
                {
                    Matrix mat = new Matrix();
                    mat.RotateAt(i * 45, new PointF(wid / 2, hgt / 2));
                    matrices.Add(mat);
                }
            }

            // Loop through all of the transformations.
            foreach (Matrix mat in matrices)
            {
                e.Graphics.Transform = mat;
                foreach (List<Point> pline in Polylines)
                {
                    e.Graphics.DrawLines(Pens.Blue, pline.ToArray());
                }
            }
        }

        // Clear old polylines.
        private void button1_Click(object sender, EventArgs e)
        {
            Polylines = new List<List<Point>>();
            pictureBox0.Refresh();
        }
        #endregion 萬花筒

        #region PhiSpiral
        // Draw the bitmap.
        private void DrawPhiSpiralBitmap()
        {
            Bitmap bm;

            // Determine the first rectangle's orientation and dimensions.
            double phi = (1 + Math.Sqrt(5)) / 2;
            RectOrientations orientation;
            int client_wid = pictureBox3.ClientSize.Width;
            int client_hgt = pictureBox3.ClientSize.Height;
            double wid, hgt;                // The rectangle's size.
            if (client_wid > client_hgt)
            {
                // Horizontal rectangle.
                orientation = RectOrientations.RemoveLeft;
                if (client_wid / (double)client_hgt > phi)
                {
                    hgt = client_hgt;
                    wid = hgt * phi;
                }
                else
                {
                    wid = client_wid;
                    hgt = wid / phi;
                }
            }
            else
            {
                // Vertical rectangle.
                orientation = RectOrientations.RemoveTop;
                if (client_hgt / (double)client_wid > phi)
                {
                    wid = client_wid;
                    hgt = wid * phi;
                }
                else
                {
                    hgt = client_hgt;
                    wid = hgt / phi;
                }
            }

            // Allow a margin.
            wid *= 0.95f;
            hgt *= 0.95f;

            // Center it.
            double x = (client_wid - wid) / 2;
            double y = (client_hgt - hgt) / 2;

            // Make the Bitmap.
            bm = new Bitmap(client_wid, client_hgt);

            // Draw the rectangles.
            using (Graphics gr = Graphics.FromImage(bm))
            {
                // Draw the rectangles.
                gr.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
                List<PointF> points = new List<PointF>();
                DrawPhiRectanglesOnGraphics(gr, points, x, y, wid, hgt, orientation);

                // Draw the square spiral.
                if (chkSquareSpiral.Checked) gr.DrawLines(Pens.Green, points.ToArray());
                // Smoothed square spiral:
                //gr.DrawCurve(Pens.Green, points.ToArray());

                if (chkTrueSpiral.Checked && points.Count > 1)
                {
                    // Draw the true spiral.
                    PointF start = points[0];
                    PointF origin = points[points.Count - 1];
                    float dx = start.X - origin.X;
                    float dy = start.Y - origin.Y;
                    double radius = Math.Sqrt(dx * dx + dy * dy);

                    double theta = Math.Atan2(dy, dx);
                    const int num_slices = 1000;
                    double dtheta = Math.PI / 2 / num_slices;
                    double factor = 1 - (1 / phi) / num_slices * 0.78; //@
                    List<PointF> new_points = new List<PointF>();

                    // Repeat until dist is too small to see.
                    while (radius > 0.1)
                    {
                        PointF new_point = new PointF(
                            (float)(origin.X + radius * Math.Cos(theta)),
                            (float)(origin.Y + radius * Math.Sin(theta)));
                        new_points.Add(new_point);
                        theta += dtheta;
                        radius *= factor;
                    }
                    gr.DrawLines(Pens.Blue, new_points.ToArray());
                }
            }

            // Display the result.
            pictureBox3.Image = bm;
            pictureBox3.Refresh();
        }

        // Draw rectangles on a Graphics object.
        private void DrawPhiRectanglesOnGraphics(Graphics gr, List<PointF> points, double x, double y, double wid, double hgt, RectOrientations orientation)
        {
            if ((wid < 1) || (hgt < 1)) return;

            // Draw this rectangle.
            if (chkRectangles.Checked) gr.DrawRectangle(Pens.Blue,
                (float)x, (float)y, (float)wid, (float)hgt);

            if (chkCircularSpiral.Checked)
            {
                // Draw a circular arc from the spiral.
                RectangleF rect;
                switch (orientation)
                {
                    case RectOrientations.RemoveLeft:
                        rect = new RectangleF(
                            (float)x, (float)y, (float)(2 * hgt), (float)(2 * hgt));
                        gr.DrawArc(Pens.Red, rect, 180, 90);
                        break;
                    case RectOrientations.RemoveTop:
                        rect = new RectangleF(
                            (float)(x - wid), (float)y, (float)(2 * wid), (float)(2 * wid));
                        gr.DrawArc(Pens.Red, rect, -90, 90);
                        break;
                    case RectOrientations.RemoveRight:
                        rect = new RectangleF(
                            (float)(x + wid - 2 * hgt),
                            (float)(y - hgt), (float)(2 * hgt), (float)(2 * hgt));
                        gr.DrawArc(Pens.Red, rect, 0, 90);
                        break;
                    case RectOrientations.RemoveBottom:
                        rect = new RectangleF((float)x, (float)(y + hgt - 2 * wid),
                            (float)(2 * wid), (float)(2 * wid));
                        gr.DrawArc(Pens.Red, rect, 90, 90);
                        break;
                }
            }

            // Recursively draw the next rectangle.
            switch (orientation)
            {
                case RectOrientations.RemoveLeft:
                    points.Add(new PointF((float)x, (float)(y + hgt)));
                    x += hgt;
                    wid -= hgt;
                    orientation = RectOrientations.RemoveTop;
                    break;
                case RectOrientations.RemoveTop:
                    points.Add(new PointF((float)x, (float)y));
                    y += wid;
                    hgt -= wid;
                    orientation = RectOrientations.RemoveRight;
                    break;
                case RectOrientations.RemoveRight:
                    points.Add(new PointF((float)(x + wid), (float)y));
                    wid -= hgt;
                    orientation = RectOrientations.RemoveBottom;
                    break;
                case RectOrientations.RemoveBottom:
                    points.Add(new PointF((float)(x + wid), (float)(y + hgt)));
                    hgt -= wid;
                    orientation = RectOrientations.RemoveLeft;
                    break;
            }
            DrawPhiRectanglesOnGraphics(gr, points, x, y, wid, hgt, orientation);
        }

        private void Options_CheckedChanged(object sender, EventArgs e)
        {
            DrawPhiSpiralBitmap();
        }
        #endregion PhiSpiral

        #region spiral_of_theodorus

        // Draw.
        private void btnDraw_Click(object sender, EventArgs e)
        {
            // Get the spiral of Theodorus's points.
            int num_triangles = int.Parse(txtNumTriangles.Text);
            List<PointF> edge_points = FindTheodorusPoints(num_triangles);

            // Draw the spiral of Theodorus.
            pictureBox2.Image = DrawTheodorusSpiral(
                edge_points, pictureBox2.ClientSize,
                chkOutline.Checked, chkFill.Checked);
        }

        // Find points on the spiral of Theodorus.
        private List<PointF> FindTheodorusPoints(int num_triangles)
        {
            // Find the edge points.
            List<PointF> edge_points = new List<PointF>();

            // Add the first point.
            float theta = 0;
            float radius = 1;
            for (int i = 1; i <= num_triangles + 1; i++)
            {
                radius = (float)Math.Sqrt(i);
                edge_points.Add(new PointF(
                    radius * (float)Math.Cos(theta),
                    radius * (float)Math.Sin(theta)));
                theta -= (float)Math.Atan2(1, radius);
            }

            return edge_points;
        }

        // Draw the spiral of Theodorus.
        private Bitmap DrawTheodorusSpiral(List<PointF> edge_points,
            Size size, bool outline_triangles, bool fill_triangles)
        {
            // Make the bitmap and associated Graphics object.
            int wid = size.Width;
            int hgt = size.Height;
            Bitmap bm = new Bitmap(wid, hgt);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.SmoothingMode = SmoothingMode.AntiAlias;
                gr.Clear(Color.White);

                // Make brushes.
                Color[] colors = RainbowColors(255);
                Brush[] brushes = ColorsToBrushes(colors);

                // Scale and center.
                float xmin, xmax, ymin, ymax;
                GetBounds(edge_points, out xmin, out xmax, out ymin, out ymax);
                RectangleF drawing_rect = new RectangleF(
                    xmin, ymin, xmax - xmin, ymax - ymin);
                RectangleF target_rect = new RectangleF(
                    5, 5, wid - 10, hgt - 10);
                MapDrawing(gr, drawing_rect, target_rect, false);

                // Draw.
                using (Pen pen = new Pen(Color.Black, 0))
                {
                    int num_brushes = brushes.Length;
                    for (int i = edge_points.Count - 1; i > 0; i--)
                    {
                        PointF[] points =
                        {
                            new PointF(0, 0),
                            new PointF(edge_points[i].X, edge_points[i].Y),
                            new PointF(edge_points[i - 1].X, edge_points[i - 1].Y),
                        };
                        if (fill_triangles)
                            gr.FillPolygon(brushes[i % num_brushes], points);
                        if (outline_triangles)
                            gr.DrawPolygon(pen, points);
                    }
                }
            }

            return bm;
        }

        // Get the points' bounds.
        private void GetBounds(List<PointF> points,
            out float xmin, out float xmax,
            out float ymin, out float ymax)
        {
            // Find the bounds.
            xmin = points[0].X;
            xmax = xmin;
            ymin = points[0].Y;
            ymax = ymin;
            foreach (PointF point in points)
            {
                if (xmin > point.X) xmin = point.X;
                if (xmax < point.X) xmax = point.X;
                if (ymin > point.Y) ymin = point.Y;
                if (ymax < point.Y) ymax = point.Y;
            }
        }

        // Map a drawing coordinate rectangle to
        // a graphics object rectangle.
        // See http://csharphelper.com/blog/2014/11/scale-a-drawing-so-it-fits-a-target-area-in-c/
        private void MapDrawing(Graphics gr, RectangleF drawing_rect,
            RectangleF target_rect, bool stretch)
        {
            if ((target_rect.Width < 1) ||
                (target_rect.Height < 1)) return;

            gr.ResetTransform();

            // Center the drawing area at the origin.
            float drawing_cx = (drawing_rect.Left + drawing_rect.Right) / 2;
            float drawing_cy = (drawing_rect.Top + drawing_rect.Bottom) / 2;
            gr.TranslateTransform(-drawing_cx, -drawing_cy);

            // Scale.
            // Get scale factors for both directions.
            float scale_x = target_rect.Width / drawing_rect.Width;
            float scale_y = target_rect.Height / drawing_rect.Height;
            if (!stretch)
            {
                // To preserve the aspect ratio,
                // use the smaller scale factor.
                scale_x = Math.Min(scale_x, scale_y);
                scale_y = scale_x;
            }
            gr.ScaleTransform(scale_x, scale_y,
                System.Drawing.Drawing2D.MatrixOrder.Append);

            // Translate to center over the drawing area.
            float graphics_cx = (target_rect.Left + target_rect.Right) / 2;
            float graphics_cy = (target_rect.Top + target_rect.Bottom) / 2;
            gr.TranslateTransform(graphics_cx, graphics_cy,
                System.Drawing.Drawing2D.MatrixOrder.Append);
        }
        #endregion spiral_of_theodorus

        #region epitrochoid長短輻圓外旋輪線；外旋輪線

        private void button2_Click(object sender, EventArgs e)
        {
            if (timer_epitrochoid.Enabled)
            {
                Cursor = Cursors.Default;
                timer_epitrochoid.Enabled = false;
            }
            else
            {
                Cursor = Cursors.WaitCursor;

                // Make the points.
                a = float.Parse(txtA.Text);
                b = float.Parse(txtB.Text);
                h = float.Parse(txtH.Text);
                dt = float.Parse(txtDt.Text);
                MakeEpitrochoidPoints(a, b, h, dt);

                // Start drawing.
                MaxPointToDraw = 0;
                timer_epitrochoid.Enabled = true;
            }
        }

        // Draw the epitrochoid.
        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(pictureBox1.BackColor);
            if (Points == null) return;

            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Scale and center.
            float scale = Math.Min(
                pictureBox1.ClientSize.Width * 0.45f,
                pictureBox1.ClientSize.Height * 0.45f);
            e.Graphics.ScaleTransform(scale / (a + b + h), scale / (a + b + h));
            e.Graphics.TranslateTransform(
                pictureBox1.ClientSize.Width / 2,
                pictureBox1.ClientSize.Height / 2,
                MatrixOrder.Append);

            // Draw the circles.
            using (Pen black_pen = new Pen(Color.Black, 0))
            {
                // Inner circle.
                e.Graphics.DrawEllipse(black_pen, -a, -a, 2 * a, 2 * a);

                // Outer circle.
                float theta = Thetas[MaxPointToDraw];
                float cx = (float)((a + b) * Math.Cos(theta));
                float cy = (float)((a + b) * Math.Sin(theta));

                e.Graphics.DrawEllipse(black_pen, cx - b, cy - b, 2 * b, 2 * b);

                // The line segment.
                e.Graphics.DrawLine(black_pen, cx, cy, Points[MaxPointToDraw].X, Points[MaxPointToDraw].Y);
            }

            // Draw the curve.
            using (Pen white_pen = new Pen(Color.White, 0))
            {
                for (int i = 0; i < MaxPointToDraw; i++)
                {
                    e.Graphics.DrawLine(white_pen, Points[i], Points[i + 1]);
                }
            }
        }

        // Make the curve's points.
        private void MakeEpitrochoidPoints(float a, float b, float h, float dt)
        {
            // Calculate the stop value for t.
            float stop_t = (float)(b * 2 * Math.PI);

            // Find the points.
            List<PointF> point_list = new List<PointF>();
            List<float> theta_list = new List<float>();

            point_list.Add(new PointF(X(a, b, h, 0), Y(a, b, h, 0)));
            theta_list.Add(0);
            for (float t = dt; t <= stop_t; t += dt)
            {
                point_list.Add(new PointF(X(a, b, h, t), Y(a, b, h, t)));
                theta_list.Add(t);
            }
            point_list.Add(new PointF(X(a, b, h, 0), Y(a, b, h, 0)));
            theta_list.Add(0);

            Points = point_list.ToArray();
            Thetas = theta_list.ToArray();
        }

        // The parametric function X(t).
        private float X(float a, float b, float h, float t)
        {
            return (float)((a + b) * Math.Cos(t) - h * Math.Cos(t * (a + b) / b));
        }

        // The parametric function Y(t).
        private float Y(float a, float b, float h, float t)
        {
            return (float)((a + b) * Math.Sin(t) - h * Math.Sin(t * (a + b) / b));
        }

        // Draw another point.
        private void timer_epitrochoid_Tick(object sender, EventArgs e)
        {
            MaxPointToDraw++;
            if (MaxPointToDraw >= Points.Length - 1)
            {
                timer_epitrochoid.Enabled = false;
                Cursor = Cursors.Default;
            }
            pictureBox1.Refresh();
        }


        #endregion epitrochoid長短輻圓外旋輪線；外旋輪線

    }
}

