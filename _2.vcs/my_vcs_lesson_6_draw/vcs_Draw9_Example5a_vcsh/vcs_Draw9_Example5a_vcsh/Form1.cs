#define CORNER_WALKS
// #define CORNER_WALKS2

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

using System.Diagnostics;

namespace vcs_Draw9_Example5a_vcsh
{
    public partial class Form1 : Form
    {
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

        #region pickover_attractor
        // The plane we should project on.
        private enum Plane
        {
            XY,
            YZ,
            XZ,
        }
        private Plane SelectedPlane;

        // The Bitmap and Graphics object.
        private Bitmap bm;
        private Graphics gr;

        // Drawing size variables.
        private int wid, hgt;
        private double xoff, yoff, zoff, xscale, yscale, zscale;

        // Drawing parameters.
        private double A, B, C, D, E, X0, Y0, Z0;

        // The colors.
        Color BgColor, FgColor;

        #endregion pickover_attractor

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
            DrawPhiSpiralBitmap();
            this.ResizeRedraw = true;

            #region pickover_attractor
            // Start with the first plane selected.
            cboPlane.SelectedIndex = 0;
            SelectedPlane = Plane.XY;
            #endregion pickover_attractor
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
            dx = W + 30;
            dy = H + 80;

            pictureBox0.Size = new Size(W, H);
            pictureBox1.Size = new Size(W, H);
            pictureBox2.Size = new Size(W, H);
            pictureBox3.Size = new Size(W, H - 50);
            pictureBox4.Size = new Size(W, H - 50);
            pictureBox5.Size = new Size(W, H - 50);
            pictureBox6.Size = new Size(W, H - 100);
            pictureBox7.Size = new Size(W, H - 100);
            pictureBox0.BorderStyle = BorderStyle.Fixed3D;
            pictureBox1.BorderStyle = BorderStyle.Fixed3D;
            pictureBox2.BorderStyle = BorderStyle.Fixed3D;
            pictureBox3.BorderStyle = BorderStyle.Fixed3D;
            pictureBox4.BorderStyle = BorderStyle.Fixed3D;
            pictureBox5.BorderStyle = BorderStyle.Fixed3D;
            pictureBox6.BorderStyle = BorderStyle.Fixed3D;
            pictureBox7.BorderStyle = BorderStyle.Fixed3D;

            pictureBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox3.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            pictureBox4.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox5.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            pictureBox6.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            pictureBox7.Location = new Point(x_st + dx * 3, y_st + dy * 1);

            groupBox0.Location = new Point(x_st + dx * 0, y_st + dy * 1 - 80);
            int dd = 40;
            rb2.Location = new Point(rb1.Location.X + dd * 1, rb1.Location.Y);
            rb3.Location = new Point(rb1.Location.X + dd * 2, rb1.Location.Y);
            rb4.Location = new Point(rb1.Location.X + dd * 3, rb1.Location.Y);
            rb5.Location = new Point(rb1.Location.X + dd * 4, rb1.Location.Y);
            rb6.Location = new Point(rb1.Location.X + dd * 5, rb1.Location.Y);
            groupBox1.Location = new Point(x_st + dx * 1, y_st + dy * 1 - 80);
            groupBox2.Location = new Point(x_st + dx * 2, y_st + dy * 1 - 80);
            groupBox3.Location = new Point(x_st + dx * 3, y_st + dy * 1 - 110);

            groupBox4.Location = new Point(x_st + dx * 0, y_st + dy * 2 - 120);
            groupBox5.Location = new Point(x_st + dx * 1, y_st + dy * 2 - 120);
            groupBox6.Location = new Point(x_st + dx * 2, y_st + dy * 2 - 160);

            lblResults.Text = "";
            lblWalkNum2.Text = "";

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


        private void ColorSample_Click(object sender, EventArgs e)
        {
            // Let the user pick a new color.
            Label lbl = sender as Label;
            colorDialog1.Color = lbl.BackColor;
            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                lbl.BackColor = colorDialog1.Color;
            }
        }

        // Start or stop drawing.
        bool Running = false;
        private void btnStart_Click(object sender, EventArgs e)
        {
            if (Running)
            {
                Running = false;
                btnStart.Text = "Stopped";
            }
            else
            {
                Running = true;
                btnStart.Text = "Stop";
                DrawCurve();
                btnStart.Text = "Go";
            }
        }

        // Draw the curve.
        private void DrawCurve()
        {
            // Get the parameters and otherwise get ready.
            Prepare();

            // Start drawing.
            double x = X0, y = Y0, z = Z0;
            while (Running)
            {
                // Plot a bunch of points.
                for (int i = 1; i <= 1000; i++)
                {
                    // Move to the next point.
                    double x2 = Math.Sin(A * y) - z * Math.Cos(B * x);
                    double y2 = z * Math.Sin(C * x) - Math.Cos(D * y);
                    z = Math.Sin(x);
                    x = x2;
                    y = y2;

                    // Plot the point.
                    switch (SelectedPlane)
                    {
                        case Plane.XY:
                            bm.SetPixel((int)(x * xscale + xoff), (int)(y * yscale + yoff), FgColor);
                            break;
                        case Plane.YZ:
                            bm.SetPixel((int)(y * yscale + yoff), (int)(z * zscale + zoff), FgColor);
                            break;
                        case Plane.XZ:
                            bm.SetPixel((int)(x * xscale + xoff), (int)(z * zscale + zoff), FgColor);
                            break;
                    }
                }

                // Refresh.
                pictureBox4.Refresh();

                // Check events to see if the user clicked Stop.
                Application.DoEvents();
            }
        }

        // Get ready to draw.
        private void Prepare()
        {
            pictureBox4.Size = new Size(W, H - 50);

            // Get the colors.
            BgColor = lblBackColor.BackColor;
            FgColor = lblForeColor.BackColor;

            // Make the Bitmap and Graphics object.
            wid = pictureBox4.ClientSize.Width;
            hgt = pictureBox4.ClientSize.Height;
            bm = new Bitmap(wid, hgt);
            gr = Graphics.FromImage(bm);
            gr.Clear(BgColor);
            pictureBox4.Image = bm;

            // Calculate scaling parameters.
            const double XMIN = -2.1;
            const double XMAX = 2.1;
            const double YMIN = -2.1;
            const double YMAX = 2.1;
            const double ZMIN = -1.2;
            const double ZMAX = 1.2;
            SelectedPlane = (Plane)cboPlane.SelectedIndex;
            switch (SelectedPlane)
            {
                case Plane.XY:
                    xoff = wid / 2;
                    yoff = hgt / 2;
                    xscale = wid / (XMAX - XMIN);
                    yscale = hgt / (YMAX - YMIN);
                    break;
                case Plane.YZ:
                    yoff = wid / 2;
                    zoff = hgt / 2;
                    yscale = wid / (YMAX - YMIN);
                    zscale = hgt / (ZMAX - ZMIN);
                    break;
                case Plane.XZ:
                    xoff = wid / 2;
                    zoff = hgt / 2;
                    xscale = wid / (XMAX - XMIN);
                    zscale = hgt / (ZMAX - ZMIN);
                    break;
            }

            // Get the parameters.
            if (double.TryParse(txtA.Text, out A)) A = 2.0;
            if (double.TryParse(txtB.Text, out B)) B = 0.5;
            if (double.TryParse(txtC.Text, out C)) C = -0.6;
            if (double.TryParse(txtD.Text, out D)) D = -2.5;
            if (double.TryParse(txtE.Text, out E)) E = 1.0;
            if (double.TryParse(txtX0.Text, out X0)) X0 = 0.0;
            if (double.TryParse(txtY0.Text, out Y0)) Y0 = 0.0;
            if (double.TryParse(txtZ0.Text, out Z0)) Z0 = 0.0;
        }

        // Adjust for the new size.
        private void pictureBox4_Resize(object sender, EventArgs e)
        {
            Prepare();
        }




        #region queue_breadth_first_tree
        // Hold branch information.
        private class BranchInfo
        {
            public float X, Y, Theta, Length;
            public int Depth;
            public BranchInfo(float x, float y, float theta, float length, int depth)
            {
                X = x;
                Y = y;
                Theta = theta;
                Length = length;
                Depth = depth;
            }
        }

        // Draw a binary tree.
        private void DrawTree(Graphics gr, Pen pen,
            int max_depth, float x, float y, float max_length,
            float initial_theta, float length_scale, float dtheta)
        {
            // Add the trunk to a queue.
            Queue<BranchInfo> branches = new Queue<BranchInfo>();
            branches.Enqueue(new BranchInfo(x, y, initial_theta, max_length, max_depth));

            // Process branches until the queue is empty.
            while (branches.Count > 0)
            {
                // Draw the next branch.
                BranchInfo branch = branches.Dequeue();

                // Set the pen's color depending on the depth.
                if (branch.Depth == 1) pen.Color = Color.Red;
                else
                {
                    int g = 255 * (max_depth - branch.Depth) / max_depth;
                    int r = 139 * (branch.Depth - 3) / max_depth;
                    if (r < 0) r = 0;
                    int b = 0;
                    pen.Color = Color.FromArgb(r, g, b);
                }

                // Set the pen's thickness depending on the depth.
                int thickness = 10 * branch.Depth / max_depth;
                if (thickness < 0) thickness = 0;
                pen.Width = thickness;

                // See where this branch should end.
                float x1 = (float)(branch.X + branch.Length * Math.Cos(branch.Theta));
                float y1 = (float)(branch.Y + branch.Length * Math.Sin(branch.Theta));

                // Draw the branch.
                gr.DrawLine(pen, branch.X, branch.Y, x1, y1);

                // If branch.depth > 1, add child branches to the queue.
                if (branch.Depth > 1)
                {
                    branches.Enqueue(new BranchInfo(x1, y1,
                        branch.Theta + dtheta, branch.Length * length_scale, branch.Depth - 1));
                    branches.Enqueue(new BranchInfo(x1, y1,
                        branch.Theta - dtheta, branch.Length * length_scale, branch.Depth - 1));
                }
            }
        }

        // Draw the tree.
        private void pictureBox5_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(pictureBox5.BackColor);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            try
            {
                float root_x = pictureBox5.ClientSize.Width / 2;
                float root_y = pictureBox5.ClientSize.Height - 4;
                float length_scale = float.Parse(txtLengthScale.Text);
                float dtheta = (float)(Math.PI / 180.0 * (double)nudDtheta.Value);
                using (Pen the_pen = new Pen(Color.Black))
                {
                    DrawTree(e.Graphics, the_pen,
                        (int)nudDepth.Value, root_x, root_y,
                        (int)nudLength.Value, (float)(-Math.PI / 2), length_scale,
                        dtheta);
                }
            }
            catch
            {
            }
        }

        private void pictureBox5_Resize(object sender, EventArgs e)
        {
            // Redraw.
            pictureBox5.Refresh();
        }

        private void parameter_ValueChanged(object sender, EventArgs e)
        {
            // Redraw.
            pictureBox5.Refresh();
        }

        private void nud_KeyUp(object sender, KeyEventArgs e)
        {
            // Redraw.
            pictureBox5.Refresh();

        }
        #endregion queue_breadth_first_tree


        #region self_avoiding_corner_walk
        private List<List<Point>> Walks = null;
        private int WalkWidth, WalkHeight;

        private IEnumerator<List<Point>> Walker = null;
        private int WalkNumber = 0;

        private void btnGenerate_Click(object sender, EventArgs e)
        {
            lblResults.Text = "Working...";
            lblWalkNum.Text = "";
            btnGenerate.Enabled = false;
            trkWalk.Visible = false;
            pictureBox6.Image = null;
            Cursor = Cursors.WaitCursor;
            Application.DoEvents();

            // Find the walks.
            WalkWidth = int.Parse(txtWidth.Text);
            WalkHeight = int.Parse(txtHeight.Text);
            Stopwatch watch = new Stopwatch();
            watch.Start();
            Walks = FindWalks(WalkWidth, WalkHeight);
            watch.Stop();

            string noun = (Walks.Count == 1 ? " walk " : " walks ");
            lblResults.Text = "Found " +
                Walks.Count.ToString() + noun + "in " +
                watch.Elapsed.TotalSeconds.ToString("0.00") +
                " seconds";

            // Display the first walk.
            if (Walks.Count > 0)
            {
                DisplayWalk(0);
                if (Walks.Count > 1)
                {
                    trkWalk.Maximum = Walks.Count - 1;
                    trkWalk.Value = 0;
                    trkWalk.Visible = true;
                }
            }

            btnGenerate.Enabled = true;
            Cursor = Cursors.Default;


            if (btnGenerate.Text == "Generate")
            {
                // Start generating walks.
                btnGenerate.Text = "Stop";
                pictureBox7.Image = null;

                WalkWidth = int.Parse(txtWidth.Text);
                WalkHeight = int.Parse(txtHeight.Text);
                IEnumerable<List<Point>> walks = FindWalks2(WalkWidth, WalkHeight);
                Walker = walks.GetEnumerator();
                WalkNumber = 1;

                tmrShowWalk.Enabled = true;
            }
            else
            {
                // Stop generating walks.
                btnGenerate.Text = "Generate";
                Walker = null;
            }

        }

        // Generate all self-avoiding walks.
        private List<List<Point>> FindWalks(int width, int height)
        {
            List<List<Point>> walks = new List<List<Point>>();

            // Make an array to show where we have been.
            bool[,] visited = new bool[width + 1, height + 1];

            // Get the number of points we need to visit.
            int num_points = (width + 1) * (height + 1);

            // Start the walk at (0, 0).
            Stack<Point> current_walk = new Stack<Point>();
            current_walk.Push(new Point(0, 0));
            visited[0, 0] = true;

            // Search for walks.
            FindWalks(num_points, walks, current_walk,
                0, 0, width, height, visited);
            return walks;
        }

        // Extend the walk that is at (current_x, current_y).
        private void FindWalks(int num_points,
            List<List<Point>> walks, Stack<Point> current_walk,
            int current_x, int current_y,
            int width, int height, bool[,] visited)
        {
            // If we have visited every position, and the
            // last point is in the lower right corner,
            // then this is a complete walk.
            if (current_walk.Count == num_points)
            {
#if CORNER_WALKS
                if ((current_x == width) && (current_y == height))
                    walks.Add(current_walk.ToList());
#else
                walks.Add(current_walk.ToList());
#endif

                if (walks.Count % 1000 == 0)
                {
                    lblResults.Text = "... " +
                        walks.Count.ToString() + " ...";
                    Application.DoEvents();
                }
            }
            else
            {
                // Try the possible moves.
                Point[] next_points = new Point[]
                {
                    new Point(current_x - 1, current_y),
                    new Point(current_x + 1, current_y),
                    new Point(current_x, current_y - 1),
                    new Point(current_x, current_y + 1),
                };
                foreach (Point point in next_points)
                {
                    if (point.X < 0) continue;
                    if (point.X > width) continue;
                    if (point.Y < 0) continue;
                    if (point.Y > height) continue;
                    if (visited[point.X, point.Y]) continue;

                    // Try visiting this point.
                    visited[point.X, point.Y] = true;
                    current_walk.Push(point);

                    FindWalks(num_points, walks, current_walk,
                        point.X, point.Y, width, height, visited);

                    // We're done visiting this point.
                    visited[point.X, point.Y] = false;
                    current_walk.Pop();
                }
            }
        }

        // Display the selected walk.
        private void trkWalk_Scroll(object sender, EventArgs e)
        {
            DisplayWalk(trkWalk.Value);
        }
        private void DisplayWalk(int walk_num)
        {
            lblWalkNum.Text = "Walk " + walk_num.ToString();
            using (Pen pen = new Pen(Color.Blue, 2))
            {
                Bitmap bm = DrawWalk(Walks[walk_num],
                    WalkWidth, WalkHeight,
                    pictureBox6.ClientSize.Width,
                    pictureBox6.ClientSize.Height,
                    Color.White, Brushes.Green, pen);
                pictureBox6.Image = bm;
            }
        }

        // Draw a walk.
        private Bitmap DrawWalk(List<Point> walk,
            int width, int height, int bm_width, int bm_height,
            Color bg_color, Brush dot_brush, Pen pen)
        {
            Bitmap bm = new Bitmap(bm_width, bm_height);

            // See how big to make each row and column.
            float scale_x = bm_width / (width + 2);
            float scale_y = bm_height / (height + 2);
            float scale = Math.Min(scale_x, scale_y);
            float offset_x = (bm_width - scale * width) / 2;
            float offset_y = (bm_height - scale * height) / 2;
            float dot_r = scale_x * 0.1f;
            float dot_w = 2 * dot_r;

            // Draw the walk.
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.SmoothingMode = SmoothingMode.AntiAlias;
                gr.Clear(bg_color);

                // Draw a grid of dots.
                for (int x = 0; x <= width; x++)
                {
                    for (int y = 0; y <= height; y++)
                    {
                        gr.FillEllipse(dot_brush,
                            offset_x + x * scale - dot_r,
                            offset_y + y * scale - dot_r,
                            dot_w, dot_w);
                    }
                }

                // Draw the walk.
                if (walk.Count > 1)
                {
                    List<PointF> points = new List<PointF>();
                    foreach (Point point in walk.ToArray())
                    {
                        points.Add(new PointF(
                            offset_x + point.X * scale,
                            offset_y + point.Y * scale));
                    }
                    gr.DrawLines(pen, points.ToArray());
                }
            }

            return bm;
        }

        // Generate all self-avoiding walks.
        private IEnumerable<List<Point>> FindWalks2(int width, int height)
        {
            // Make an array to show where we have been.
            bool[,] visited = new bool[width + 1, height + 1];

            // Get the number of points we need to visit.
            int num_points = (width + 1) * (height + 1);

            // Start the walk at (0, 0).
            Stack<Point> current_walk = new Stack<Point>();
            current_walk.Push(new Point(0, 0));
            visited[0, 0] = true;

            // Search for walks.
            return FindWalks2(num_points, current_walk,
                0, 0, width, height, visited);
        }

        // Extend the walk that is at (current_x, current_y).
        private IEnumerable<List<Point>> FindWalks2(int num_points,
            Stack<Point> current_walk,
            int current_x, int current_y,
            int width, int height, bool[,] visited)
        {
            // If we have visited every position, and the
            // last point is in the lower right corner,
            // then this is a complete walk.
            if (current_walk.Count == num_points)
            {
#if CORNER_WALKS2
                if ((current_x == width) && (current_y == height))
                    yield return current_walk.ToList();
#else
                yield return current_walk.ToList();
#endif
            }
            else
            {
                // Try the possible moves.
                Point[] next_points = new Point[]
                {
                    new Point(current_x - 1, current_y),
                    new Point(current_x + 1, current_y),
                    new Point(current_x, current_y - 1),
                    new Point(current_x, current_y + 1),
                };

                // Try the moves.
                foreach (Point point in next_points)
                {
                    if (point.X < 0) continue;
                    if (point.X > width) continue;
                    if (point.Y < 0) continue;
                    if (point.Y > height) continue;
                    if (visited[point.X, point.Y]) continue;

                    // Try visiting this point.
                    visited[point.X, point.Y] = true;
                    current_walk.Push(point);

                    foreach (List<Point> walk in FindWalks2(num_points, current_walk,
                        point.X, point.Y, width, height, visited))
                        yield return walk;

                    // We're done visiting this point.
                    visited[point.X, point.Y] = false;
                    current_walk.Pop();
                }
            }
        }

        private void DisplayNextWalk()
        {
            lblWalkNum2.Text = "Walk " + WalkNumber.ToString();
            WalkNumber++;

            if (!Walker.MoveNext())
            {
                btnGenerate.Text = "Generate";
                Walker = null;
            }
            else
            {
                using (Pen pen = new Pen(Color.Blue, 2))
                {
                    List<Point> walk = Walker.Current;
                    Bitmap bm = DrawWalk(walk,
                        WalkWidth, WalkHeight,
                        pictureBox7.ClientSize.Width,
                        pictureBox7.ClientSize.Height,
                        Color.White, Brushes.Green, pen);
                    pictureBox7.Image = bm;
                }
            }
        }

        /*
        // Draw a walk.
        private Bitmap DrawWalk(List<Point> walk,
            int width, int height, int bm_width, int bm_height,
            Color bg_color, Brush dot_brush, Pen pen)
        {
            Bitmap bm = new Bitmap(bm_width, bm_height);

            // See how big to make each row and column.
            float scale_x = bm_width / (width + 2);
            float scale_y = bm_height / (height + 2);
            float scale = Math.Min(scale_x, scale_y);
            float offset_x = (bm_width - scale * width) / 2;
            float offset_y = (bm_height - scale * height) / 2;
            float dot_r = scale_x * 0.1f;
            float dot_w = 2 * dot_r;

            // Draw the walk.
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.SmoothingMode = SmoothingMode.AntiAlias;
                gr.Clear(bg_color);

                // Draw a grid of dots.
                for (int x = 0; x <= width; x++)
                {
                    for (int y = 0; y <= height; y++)
                    {
                        gr.FillEllipse(dot_brush,
                            offset_x + x * scale - dot_r,
                            offset_y + y * scale - dot_r,
                            dot_w, dot_w);
                    }
                }

                // Draw the walk.
                if (walk.Count > 1)
                {
                    List<PointF> points = new List<PointF>();
                    foreach (Point point in walk.ToArray())
                    {
                        points.Add(new PointF(
                            offset_x + point.X * scale,
                            offset_y + point.Y * scale));
                    }
                    gr.DrawLines(pen, points.ToArray());
                }
            }
            return bm;
        }
        */

        // Generate and display the next walk.
        private void tmrShowWalk_Tick(object sender, EventArgs e)
        {
            if (Walker == null)
                tmrShowWalk.Enabled = false;
            else
                DisplayNextWalk();
        }

        private void scrSpeed_Scroll(object sender, ScrollEventArgs e)
        {
            tmrShowWalk.Interval = 1000 / scrSpeed.Value;
        }

        #endregion self_avoiding_corner_walk
    }
}
