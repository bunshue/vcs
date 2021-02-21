#define FIG1        //for 畫蜂巢狀圖
//#define FIG34

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

namespace vcs_Draw9_Example9_vcsh
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;
        int W = 250;
        int H = 250;

        private const int Period = 21;
        // Initialize the colors.
        private Color[] Colors = new Color[]
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

        #region pictureBox_butterfly butterfly
        private const int period = 24;
        #endregion


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
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new System.Drawing.Point(0, 0);

            int x_st;
            int y_st;
            int dx;
            int dy;

            x_st = 10;
            y_st = 10;
            dx = W + 20;
            dy = H + 20;

            pictureBox_Chrysanthemum1.Size = new Size(W, H);
            pictureBox_Chrysanthemum2.Size = new Size(W, H);
            pictureBox_butterfly.Size = new Size(W, H);
            pictureBox_polar.Size = new Size(W, H);
            pictureBox_hex.Size = new Size(W, H);
            pictureBox_tri.Size = new Size(W, H);
            pictureBox7.Size = new Size(W, H);
            pictureBox8.Size = new Size(W, H);
            pictureBox9.Size = new Size(W, H);
            pictureBox10.Size = new Size(W, H);
            pictureBox11.Size = new Size(W, H);
            pictureBox12.Size = new Size(W, H);
            pictureBox13.Size = new Size(W, H);
            pictureBox14.Size = new Size(W, H);
            pictureBox15.Size = new Size(W, H);

            pictureBox_Chrysanthemum1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox_Chrysanthemum2.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox_butterfly.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox_polar.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            pictureBox_hex.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            pictureBox_tri.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox7.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            pictureBox8.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            pictureBox9.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            pictureBox10.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            pictureBox11.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            pictureBox12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            pictureBox13.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            pictureBox14.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            pictureBox15.Location = new Point(x_st + dx * 4, y_st + dy * 2);

            pictureBox_Chrysanthemum1.BackColor = Color.Black;
            pictureBox_Chrysanthemum2.BackColor = Color.Black;
            pictureBox_butterfly.BackColor = Color.Black;

            bt_save.Location = new Point(x_st + dx * 6 + 225, y_st + dy * 0 + 50);

            richTextBox1.Location = new Point(x_st + dx * 6 + 225 - 100, y_st + dy * 0 + 50 + 50);

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

        private void pictureBox_Chrysanthemum1_Paint(object sender, PaintEventArgs e)
        {
            // Scale and translate.
            const float ymax = -11;
            const float ymin = 11;
            const float hgt = ymin - ymax;
            const float wid = hgt;
            float scale = Math.Min(
                pictureBox_Chrysanthemum1.Size.Width / wid,
                pictureBox_Chrysanthemum1.Size.Height / hgt);
            e.Graphics.ScaleTransform(scale, scale);
            e.Graphics.TranslateTransform(
                pictureBox_Chrysanthemum1.Size.Width / 2,
                pictureBox_Chrysanthemum1.Size.Height / 2,
                System.Drawing.Drawing2D.MatrixOrder.Append);

            // Draw the curve.
            const long num_lines = 5000;

            // Generate the points.
            double t = 0;
            double r = 5 * (1 + Math.Sin(11 * t / 5))
                - 4 * Math.Pow(Math.Sin(17 * t / 3), 4)
                * Math.Pow(Math.Sin(2 * Math.Cos(3 * t) - 28 * t), 8);
            PointF pt1 = new PointF((float)(r * Math.Sin(t)), (float)(-r * Math.Cos(t)));

            using (Pen the_pen = new Pen(Color.Blue, 0))
            {
                for (int i = 0; i <= num_lines; i++)
                {
                    t = i * Period * Math.PI / num_lines;
                    r = 5 * (1 + Math.Sin(11 * t / 5))
                        - 4 * Math.Pow(Math.Sin(17 * t / 3), 4)
                        * Math.Pow(Math.Sin(2 * Math.Cos(3 * t) - 28 * t), 8);
                    PointF pt0 = pt1;
                    pt1 = new PointF((float)(r * Math.Sin(t)), (float)(r * Math.Cos(t)));
                    the_pen.Color = GetColor(t);
                    e.Graphics.DrawLine(the_pen, pt0, pt1);
                }
            }
        }

        // Return a color from the Colors array.
        private Color GetColor(double t)
        {
            int index = (int)(t / Math.PI);
            return Colors[index % Colors.Length];
        }

        private void pictureBox_Chrysanthemum2_Paint(object sender, PaintEventArgs e)
        {
            // Scale and translate.
            const float ymax = -11;
            const float ymin = 11;
            const float hgt = ymin - ymax;
            const float wid = hgt;
            float scale = Math.Min(
                pictureBox_Chrysanthemum2.Size.Width / wid,
                pictureBox_Chrysanthemum2.Size.Height / hgt);
            e.Graphics.ScaleTransform(scale, scale);
            e.Graphics.TranslateTransform(
                pictureBox_Chrysanthemum2.Size.Width / 2,
                pictureBox_Chrysanthemum2.Size.Height / 2,
                System.Drawing.Drawing2D.MatrixOrder.Append);

            // Draw the curve.
            const long num_lines = 5000;

            // Generate the points.
            double t = 0;
            double r = 5 * (1 + Math.Sin(11 * t / 5))
                - 4 * Math.Pow(Math.Sin(17 * t / 3), 4)
                * Math.Pow(Math.Sin(2 * Math.Cos(3 * t) - 28 * t), 8);
            PointF pt1 = new PointF((float)(r * Math.Sin(t)), (float)(-r * Math.Cos(t)));

            using (Pen the_pen = new Pen(Color.Blue, 0))
            {
                using (SolidBrush the_brush = new SolidBrush(Color.Blue))
                {
                    for (int i = 0; i <= num_lines; i++)
                    {
                        t = i * Period * Math.PI / num_lines;
                        r = 5 * (1 + Math.Sin(11 * t / 5))
                            - 4 * Math.Pow(Math.Sin(17 * t / 3), 4)
                            * Math.Pow(Math.Sin(2 * Math.Cos(3 * t) - 28 * t), 8);
                        PointF pt0 = pt1;
                        pt1 = new PointF((float)(r * Math.Sin(t)), (float)(r * Math.Cos(t)));
                        Color the_color = GetColor(t);

                        // Fill the triangle from this edge to the origin.
                        the_brush.Color = Color.FromArgb(64,
                            the_color.R, the_color.G, the_color.B);
                        PointF[] pts = { pt0, pt1, new PointF(0, 0) };
                        e.Graphics.FillPolygon(the_brush, pts);

                        // Draw the curve's outer edge.
                        the_pen.Color = the_color;
                        e.Graphics.DrawLine(the_pen, pt0, pt1);
                    }
                }
            }
        }




        #region pictureBox_butterfly butterfly

        // Draw the butterfly.
        private void pictureBox_butterfly_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            e.Graphics.Clear(this.pictureBox_butterfly.BackColor);

            // Scale and translate.
            RectangleF world_rect =
                new RectangleF(-4.0f, -4.4f, 8.0f, 7.3f);
            float cx = (world_rect.Left + world_rect.Right) / 2;
            float cy = (world_rect.Top + world_rect.Bottom) / 2;

            // Center the world coordinates at origin.
            e.Graphics.TranslateTransform(-cx, -cy);

            // Scale to fill the form.
            float scale = Math.Min(
                this.pictureBox_butterfly.ClientSize.Width / world_rect.Width,
                this.pictureBox_butterfly.ClientSize.Height / world_rect.Height);
            e.Graphics.ScaleTransform(scale, scale, MatrixOrder.Append);

            // Move the result to center on the form.
            e.Graphics.TranslateTransform(
                this.pictureBox_butterfly.ClientSize.Width / 2,
                this.pictureBox_butterfly.ClientSize.Height / 2, MatrixOrder.Append);

            // Generate the points.
            PointF pt0, pt1;
            double t = 0;
            double expr =
                Math.Exp(Math.Cos(t))
                - 2 * Math.Cos(4 * t)
                - Math.Pow(Math.Sin(t / 12), 5);
            pt1 = new PointF(
                (float)(Math.Sin(t) * expr),
                (float)(-Math.Cos(t) * expr));
            using (Pen the_pen = new Pen(Color.Blue, 0))
            {
                const long num_lines = 5000;
                for (long i = 0; i < num_lines; i++)
                {
                    t = i * period * Math.PI / num_lines;
                    expr =
                        Math.Exp(Math.Cos(t))
                        - 2 * Math.Cos(4 * t)
                        - Math.Pow(Math.Sin(t / 12), 5);
                    pt0 = pt1;
                    pt1 = new PointF(
                        (float)(Math.Sin(t) * expr),
                        (float)(-Math.Cos(t) * expr));
                    the_pen.Color = GetColor(t);
                    e.Graphics.DrawLine(the_pen, pt0, pt1);
                }
            }
        }
        #endregion

        // polar graph ST
        // Draw the graph.
        private void pictureBox_polar_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(Color.White);

            // Set up a transformation to map the region
            // -2.1 <= X <= 2.1, -2.1 <= Y <= 2.1 onto the  Bitmap.
            RectangleF rect = new RectangleF(-2.1f, -2.1f, 4.2f, 4.2f);
            PointF[] pts =
                    {
                        new PointF(0, H),
                        new PointF(W, H),
                        new PointF(0, 0),
                    };
            //e.Graphics
            e.Graphics.Transform = new Matrix(rect, pts);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            using (Pen thin_pen = new Pen(Color.Blue, 0))
            {
                // Draw the X and Y axes.
                thin_pen.Color = Color.Blue;
                e.Graphics.DrawLine(thin_pen, -2.1f, 0, 2.1f, 0);
                const float big_tick = 0.1f;
                const float small_tick = 0.05f;
                for (float x = (int)-2.1f; x <= 2.1f; x += 1)
                    e.Graphics.DrawLine(thin_pen, x, -small_tick, x, small_tick);
                for (float x = (int)-2.1f + 0.5f; x <= 2.1f; x += 1)
                    e.Graphics.DrawLine(thin_pen, x, -big_tick, x, big_tick);

                e.Graphics.DrawLine(thin_pen, 0, -2.1f, 0, 2.1f);
                for (float y = (int)-2.1f; y <= 2.1f; y += 1)
                    e.Graphics.DrawLine(thin_pen, -small_tick, y, small_tick, y);
                for (float y = (int)-2.1f + 0.5f; y <= 2.1f; y += 1)
                    e.Graphics.DrawLine(thin_pen, -big_tick, y, big_tick, y);

                // Draw the graph.
                DrawGraph(e.Graphics);
            }
        }

        // Draw the graph on a Bitmap.
        private void DrawGraph(Graphics gr)
        {
            // Generate the points.
            double t = 0;
            const double dt = Math.PI / 100.0;
            const double two_pi = 2 * Math.PI;
            List<PointF> points = new List<PointF>();
            while (t <= two_pi)
            {
                double r = 2 * Math.Sin(5 * t);
                float x = (float)(r * Math.Cos(t));
                float y = (float)(r * Math.Sin(t));
                points.Add(new PointF(x, y));
                t += dt;
            }

            // Draw the curve.
            using (Pen thin_pen = new Pen(Color.Red, 0))
            {
                gr.DrawPolygon(thin_pen, points.ToArray());
            }
        }
        // polar graph SP

        private void timer_change_Tick(object sender, EventArgs e)
        {
            redraw_all();

        }

        void redraw_all()
        {




        }



        //畫蜂巢狀圖 ST

        // The height of a hexagon.
        private const float HexHeight = 50;

        // Selected hexagons.
        private List<PointF> Hexagons = new List<PointF>();


#if FIG34
        // The selected search rectangle.
        // Used to draw Figures 3 and 4.
        private List<RectangleF> TestRects = new List<RectangleF>();
#endif

        // Redraw the grid.
        private void pictureBox_hex_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the selected hexagons.
            foreach (PointF point in Hexagons)
            {
                e.Graphics.FillPolygon(Brushes.LightBlue,
                    HexToPoints(HexHeight, point.X, point.Y));
            }

            // Draw the grid.
            DrawHexGrid(e.Graphics, Pens.Black,
                0, pictureBox_hex.ClientSize.Width,
                0, pictureBox_hex.ClientSize.Height,
                HexHeight);

#if FIG34
            // Draw the selected rectangles for Figures 3 and 4.
            using (Pen pen = new Pen(Color.Red, 3))
            {
                pen.DashStyle = DashStyle.Dash;
                foreach (RectangleF rect in TestRects)
                {
                    e.Graphics.DrawRectangle(pen, Rectangle.Round(rect));
                }
            }
#endif
        }

        // Draw a hexagonal grid for the indicated area.
        // (You might be able to draw the hexagons without
        // drawing any duplicate edges, but this is a lot easier.)
        private void DrawHexGrid(Graphics gr, Pen pen,
            float xmin, float xmax, float ymin, float ymax,
            float height)
        {
            // Loop until a hexagon won't fit.
            for (int row = 0; ; row++)
            {
                // Get the points for the row's first hexagon.
                PointF[] points = HexToPoints(height, row, 0);

                // If it doesn't fit, we're done.
                if (points[4].Y > ymax) break;

                // Draw the row.
                for (int col = 0; ; col++)
                {
                    // Get the points for the row's next hexagon.
                    points = HexToPoints(height, row, col);

                    // If it doesn't fit horizontally,
                    // we're done with this row.
                    if (points[3].X > xmax) break;

                    // If it fits vertically, draw it.
                    if (points[4].Y <= ymax)
                    {
                        gr.DrawPolygon(pen, points);

#if FIG1
                        // Label the hexagon (for Figure 1).
                        using (StringFormat sf = new StringFormat())
                        {
                            sf.Alignment = StringAlignment.Center;
                            sf.LineAlignment = StringAlignment.Center;
                            float x = (points[0].X + points[3].X) / 2;
                            float y = (points[1].Y + points[4].Y) / 2;
                            string label = "(" + row.ToString() + ", " +
                                col.ToString() + ")";
                            gr.DrawString(label, this.Font,
                                Brushes.Black, x, y, sf);
                        }
#endif
                    }
                }
            }
        }

        private void pictureBox_hex_Resize(object sender, EventArgs e)
        {
            pictureBox_hex.Refresh();
        }

        // Display the row and column under the mouse.
        private void pictureBox_hex_MouseMove(object sender, MouseEventArgs e)
        {
            int row, col;
            PointToHex(e.X, e.Y, HexHeight, out row, out col);
            this.Text = "(" + row + ", " + col + ")";
        }

        // Add the clicked hexagon to the Hexagons list.
        private void pictureBox_hex_MouseClick(object sender, MouseEventArgs e)
        {
            int row, col;
            PointToHex(e.X, e.Y, HexHeight, out row, out col);
            Hexagons.Add(new PointF(row, col));

#if FIG34
            // Used to draw Figures 3 and 4.
            PointF[] points = HexToPoints(HexHeight, row, col);
            TestRects.Add(new RectangleF(
                points[0].X, points[1].Y,
                0.75f * (points[3].X - points[0].X),
                points[4].Y - points[1].Y));
#endif

            pictureBox_hex.Refresh();
        }

        // Return the width of a hexagon.
        private float HexWidth(float height)
        {
            return (float)(4 * (height / 2 / Math.Sqrt(3)));
        }

        // Return the row and column of the hexagon at this point.
        private void PointToHex(float x, float y, float height,
            out int row, out int col)
        {
            // Find the test rectangle containing the point.
            float width = HexWidth(height);
            col = (int)(x / (width * 0.75f));

            if (col % 2 == 0)
                row = (int)(y / height);
            else
                row = (int)((y - height / 2) / height);

            // Find the test area.
            float testx = col * width * 0.75f;
            float testy = row * height;
            if (col % 2 == 1) testy += height / 2;

            // See if the point is above or
            // below the test hexagon on the left.
            bool is_above = false, is_below = false;
            float dx = x - testx;
            if (dx < width / 4)
            {
                float dy = y - (testy + height / 2);
                if (dx < 0.001)
                {
                    // The point is on the left edge of the test rectangle.
                    if (dy < 0) is_above = true;
                    if (dy > 0) is_below = true;
                }
                else if (dy < 0)
                {
                    // See if the point is above the test hexagon.
                    if (-dy / dx > Math.Sqrt(3)) is_above = true;
                }
                else
                {
                    // See if the point is below the test hexagon.
                    if (dy / dx > Math.Sqrt(3)) is_below = true;
                }
            }

            // Adjust the row and column if necessary.
            if (is_above)
            {
                if (col % 2 == 0) row--;
                col--;
            }
            else if (is_below)
            {
                if (col % 2 == 1) row++;
                col--;
            }
        }

        // Return the points that define the indicated hexagon.
        private PointF[] HexToPoints(float height, float row, float col)
        {
            // Start with the leftmost corner of the upper left hexagon.
            float width = HexWidth(height);
            float y = height / 2;
            float x = 0;

            // Move down the required number of rows.
            y += row * height;

            // If the column is odd, move down half a hex more.
            if (col % 2 == 1) y += height / 2;

            // Move over for the column number.
            x += col * (width * 0.75f);

            // Generate the points.
            return new PointF[]
                {
                    new PointF(x, y),
                    new PointF(x + width * 0.25f, y - height / 2),
                    new PointF(x + width * 0.75f, y - height / 2),
                    new PointF(x + width, y),
                    new PointF(x + width * 0.75f, y + height / 2),
                    new PointF(x + width * 0.25f, y + height / 2),
                };
        }
        //畫蜂巢狀圖 SP

        //畫三角巢狀圖 ST

        // The height of a triangle.
        private const float TriangleHeight = 50;

        // Selected triangles.
        private List<PointF> Triangles = new List<PointF>();

        // Redraw the grid.
        private void pictureBox_tri_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the selected triangles.
            foreach (PointF point in Triangles)
            {
                e.Graphics.FillPolygon(Brushes.LightBlue,
                    TriangleToPoints(TriangleHeight, point.X, point.Y));
            }

            // Draw the grid.
            DrawTriangularGrid(e.Graphics, Pens.Black,
                0, pictureBox_tri.ClientSize.Width,
                0, pictureBox_tri.ClientSize.Height,
                TriangleHeight);

            //// Used to draw Figure 1.
            //PointF[] tri_points = TriangleToPoints(TriangleHeight, 2, 1.5f);
            //using (Pen pen = new Pen(Color.Red, 3))
            //{
            //    pen.DashStyle = DashStyle.Dash;
            //    var xquery =
            //        from PointF point in tri_points
            //        select point.X;
            //    float x = xquery.Min();
            //    var yquery =
            //        from PointF point in tri_points
            //        select point.Y;
            //    float y = yquery.Min();
            //    e.Graphics.DrawRectangle(pen, x, y,
            //        TriangleWidth(TriangleHeight),
            //        TriangleHeight);
            //}
        }

        // Draw a triangular grid for the indicated area.
        private void DrawTriangularGrid(Graphics gr, Pen pen,
            float xmin, float xmax, float ymin, float ymax,
            float height)
        {
            float width = TriangleWidth(height);
            int row = 0;
            for (float y = 0; y <= ymax + width / 2; y += height)
            {
                float x = 0;
                if (row % 2 == 0) x = width / 2;

                PointF[] points =
                {
                    new PointF(x, y),
                    new PointF(x + width / 2, y + height),
                    new PointF(x - width / 2, y + height),
                };
                for (; x <= xmax; x += width)
                {
                    gr.DrawPolygon(pen, points);
                    points[0].X += width;
                    points[1].X += width;
                    points[2].X += width;
                }
                row++;
            }
        }

        private void pictureBox_tri_Resize(object sender, EventArgs e)
        {
            pictureBox_tri.Refresh();
        }

        // Display the row and column under the mouse.
        private void pictureBox_tri_MouseMove(object sender, MouseEventArgs e)
        {
            float row, col;
            PointToTriangle(e.X, e.Y, TriangleHeight, out row, out col);
            this.Text = "(" + row + ", " + col + ")";
        }

        // Add the clicked triangle to the Triangles list.
        private void pictureBox_tri_MouseClick(object sender, MouseEventArgs e)
        {
            float row, col;
            PointToTriangle(e.X, e.Y, TriangleHeight, out row, out col);
            Triangles.Add(new PointF(row, col));
            pictureBox_tri.Refresh();
        }

        // Return the width of a triangle.
        private float TriangleWidth(float height)
        {
            return (float)(2 * height / Math.Sqrt(3));
        }

        // Return the row and column of the triangle at this point.
        private void PointToTriangle(float x, float y, float height, out float row, out float col)
        {
            float width = TriangleWidth(height);
            row = (int)(y / height);
            col = (int)(x / width);

            float dy = (row + 1) * height - y;
            float dx = x - col * width;
            if (row % 2 == 1) dy = height - dy;
            if (dy > 1)
            {
                if (dx < width / 2)
                {
                    // Left half of triangle.
                    float ratio = dx / dy;
                    if (ratio < 1f / Math.Sqrt(3)) col -= 0.5f;
                }
                else
                {
                    // Right half of triangle.
                    float ratio = (width - dx) / dy;
                    if (ratio < 1f / Math.Sqrt(3)) col += 0.5f;
                }
            }
        }

        // Return the points that define the indicated triangle.
        private PointF[] TriangleToPoints(float height, float row, float col)
        {
            float width = TriangleWidth(height);
            float y = row * height;
            float x = (col + 0.5f) * width;

            // See if this triangle should be drawn
            // right-side up or upside down.
            bool whole_col = (Math.Abs(col - (int)col) < 0.1);
            bool rightside_up;
            if ((int)row % 2 == 0)
            {
                // Even row.
                rightside_up = whole_col;
            }
            else
            {
                // Odd row.
                rightside_up = !whole_col;
            }

            // Draw the triangle.
            if (rightside_up)
                return new PointF[]
                    {
                        new PointF(x, y),
                        new PointF(x + width / 2, y + height),
                        new PointF(x - width / 2, y + height),
                    };
            else
                return new PointF[]
                    {
                        new PointF(x, y + height),
                        new PointF(x + width / 2, y),
                        new PointF(x - width / 2, y),
                    };
        }
        
        //畫三角巢狀圖 SP

    }
}
