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
        int H = 230;

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


        //畫triangle_puzzle_solution ST
        // The points.
        private PointF[] Points;

        // The solutions.
        private List<int[]> Solutions;

        // The solution we should display.
        private int CurrentSolution = 100;
        //畫triangle_puzzle_solution SP


        //畫find_squares_colored ST
        // The points.
        private PointF[] Points2;

        // The solutions.
        private List<int[]> Solutions2;

        // The solutions' side lengths.
        private List<int> SideLengths;

        // The solution we should display.
        private int CurrentSolution2 = 100;

        // Colors used to draw the squares.
        private Color[] Colors2 = { Color.Red, Color.Green, Color.Blue, };
        //畫find_squares_colored SP

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            draw_circle_connection();       //pictureBox_circle
            draw_some_random_circles();     //pictureBox_floodfill

            draw_triangle_puzzle_solution();

            draw_find_squares_colored();
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
            dx = W + 20;
            dy = H + 40;

            pictureBox_Chrysanthemum1.Size = new Size(W, H);
            pictureBox_Chrysanthemum2.Size = new Size(W, H);
            pictureBox_butterfly.Size = new Size(W, H);
            pictureBox_polar.Size = new Size(W, H);
            pictureBox_hex.Size = new Size(W, H);
            pictureBox_tri.Size = new Size(W, H);
            pictureBox_circle.Size = new Size(W, H);
            pictureBox_star1.Size = new Size(W, H);
            pictureBox_star2.Size = new Size(W, H);
            pictureBox_star3.Size = new Size(W, H);
            pictureBox_floodfill.Size = new Size(W, H);
            pictureBox12.Size = new Size(W, H);
            pictureBox13.Size = new Size(W, H);
            pictureBox14.Size = new Size(W, H);
            pictureBox15.Size = new Size(W, H);
            pictureBox_triangle_puzzle_solution.Size = new Size(W, H);
            pictureBox_find_squares_colored.Size = new Size(W, H);
            pictureBox18.Size = new Size(W, H);
            pictureBox19.Size = new Size(W, H);
            pictureBox20.Size = new Size(W, H);

            pictureBox_Chrysanthemum1.BorderStyle = BorderStyle.Fixed3D;
            pictureBox_Chrysanthemum2.BorderStyle = BorderStyle.Fixed3D;
            pictureBox_butterfly.BorderStyle = BorderStyle.Fixed3D;
            pictureBox_polar.BorderStyle = BorderStyle.Fixed3D;
            pictureBox_hex.BorderStyle = BorderStyle.Fixed3D;
            pictureBox_tri.BorderStyle = BorderStyle.Fixed3D;
            pictureBox_circle.BorderStyle = BorderStyle.Fixed3D;
            pictureBox_star1.BorderStyle = BorderStyle.Fixed3D;
            pictureBox_star2.BorderStyle = BorderStyle.Fixed3D;
            pictureBox_star3.BorderStyle = BorderStyle.Fixed3D;
            pictureBox_floodfill.BorderStyle = BorderStyle.Fixed3D;
            pictureBox12.BorderStyle = BorderStyle.Fixed3D;
            pictureBox13.BorderStyle = BorderStyle.Fixed3D;
            pictureBox14.BorderStyle = BorderStyle.Fixed3D;
            pictureBox15.BorderStyle = BorderStyle.Fixed3D;
            pictureBox_triangle_puzzle_solution.BorderStyle = BorderStyle.Fixed3D;
            pictureBox_find_squares_colored.BorderStyle = BorderStyle.Fixed3D;
            pictureBox18.BorderStyle = BorderStyle.Fixed3D;
            pictureBox19.BorderStyle = BorderStyle.Fixed3D;
            pictureBox20.BorderStyle = BorderStyle.Fixed3D;

            pictureBox_Chrysanthemum1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox_Chrysanthemum2.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox_butterfly.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox_polar.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            pictureBox_hex.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            label5.Location = new Point(x_st + dx * 4, y_st + dy * 0 - 25);
            label5.Text = "點選位置填滿顏色";
            pictureBox_tri.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            label6.Location = new Point(x_st + dx * 0, y_st + dy * 1 - 25);
            label6.Text = "點選位置填滿顏色";
            pictureBox_circle.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            pictureBox_star1.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            pictureBox_star2.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            pictureBox_star3.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            pictureBox_floodfill.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            label11.Location = new Point(x_st + dx * 0, y_st + dy * 2 - 25);
            label11.Text = "點選位置填滿顏色";

            pictureBox12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            pictureBox13.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            pictureBox14.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            pictureBox15.Location = new Point(x_st + dx * 4, y_st + dy * 2);
            pictureBox_triangle_puzzle_solution.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 3 - 25);
            button2.Location = new Point(x_st + dx * 0 + 90, y_st + dy * 3 - 25);
            label16.Location = new Point(x_st + dx * 0 + 90 + 90, y_st + dy * 3 - 25);
            label16.Text = "";

            pictureBox_find_squares_colored.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button3.Location = new Point(x_st + dx * 1, y_st + dy * 3 - 25);
            button4.Location = new Point(x_st + dx * 1 + 90, y_st + dy * 3 - 25);
            label17.Location = new Point(x_st + dx * 1 + 90 + 90, y_st + dy * 3 - 25);
            label17.Text = "";
            pictureBox18.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            pictureBox19.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            pictureBox20.Location = new Point(x_st + dx * 4, y_st + dy * 3);

            pictureBox_Chrysanthemum1.BackColor = Color.Black;
            pictureBox_Chrysanthemum2.BackColor = Color.Black;
            pictureBox_butterfly.BackColor = Color.Black;

            groupBox2.Location = new Point(x_st + dx * 5 - 40, y_st + dy * 1);

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
            int W = this.pictureBox_butterfly.ClientSize.Width;
            int H = this.pictureBox_butterfly.ClientSize.Height;

            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            e.Graphics.Clear(this.pictureBox_butterfly.BackColor);

            // Scale and translate.
            RectangleF world_rect = new RectangleF(-4.0f, -4.4f, 8.0f, 7.3f);
            float cx = (world_rect.Left + world_rect.Right) / 2;
            float cy = (world_rect.Top + world_rect.Bottom) / 2;

            // Center the world coordinates at origin.
            e.Graphics.TranslateTransform(-cx, -cy);

            // Scale to fill the form.
            float scale = Math.Min(W / world_rect.Width, H / world_rect.Height);
            e.Graphics.ScaleTransform(scale, scale, MatrixOrder.Append);

            // Move the result to center on the form.
            e.Graphics.TranslateTransform(W / 2, H / 2, MatrixOrder.Append);

            // Generate the points.
            PointF pt0, pt1;
            double t = 0;
            double expr = Math.Exp(Math.Cos(t)) - 2 * Math.Cos(4 * t) - Math.Pow(Math.Sin(t / 12), 5);
            pt1 = new PointF((float)(Math.Sin(t) * expr), (float)(-Math.Cos(t) * expr));
            using (Pen the_pen = new Pen(Color.Blue, 0))
            {
                const long num_lines = 5000;
                for (long i = 0; i < num_lines; i++)
                {
                    t = i * period * Math.PI / num_lines;
                    expr = Math.Exp(Math.Cos(t)) - 2 * Math.Cos(4 * t) - Math.Pow(Math.Sin(t / 12), 5);
                    pt0 = pt1;
                    pt1 = new PointF((float)(Math.Sin(t) * expr), (float)(-Math.Cos(t) * expr));
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



        void draw_circle_connection()   //pictureBox_circle
        {
            pictureBox_circle.Image = DrawPattern(pictureBox_circle.ClientSize.Width, pictureBox_circle.ClientSize.Height);
        }

        // Draw the pattern.
        private Bitmap DrawPattern(int wid, int hgt)
        {
            Bitmap bm = new Bitmap(wid, hgt);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.SmoothingMode = SmoothingMode.AntiAlias;

                float margin = 10;
                float diameter1 = (hgt - margin) / 5f;
                float diameter2 = (wid - margin) / (float)(1 + 2 * Math.Sqrt(3));
                float diameter = Math.Min(diameter1, diameter2);

                float radius = diameter / 2f;
                float cx = wid / 2f;
                float cy = hgt / 2f;

                // Find the center circle's center.
                List<PointF> centers = new List<PointF>();
                centers.Add(new PointF(cx, cy));

                // Add the other circles.
                for (int ring_num = 0; ring_num < 2; ring_num++)
                {
                    float ring_radius = diameter * (ring_num + 1);
                    double theta = Math.PI / 2.0;
                    double dtheta = Math.PI / 3.0;
                    for (int i = 0; i < 6; i++)
                    {
                        double x = cx + ring_radius * Math.Cos(theta);
                        double y = cy + ring_radius * Math.Sin(theta);
                        centers.Add(new PointF((float)x, (float)y));
                        theta += dtheta;
                    }
                }

                // Fill and outline the circles.
                foreach (PointF center in centers)
                {
                    float x = center.X - radius;
                    float y = center.Y - radius;
                    gr.FillEllipse(Brushes.LightBlue, x, y, diameter, diameter);
                    gr.DrawEllipse(Pens.Blue, x, y, diameter, diameter);
                }

                // Connect the circle centers.
                int num_circles = centers.Count;
                for (int i = 0; i < num_circles; i++)
                {
                    for (int j = i + 1; j < num_circles; j++)
                    {
                        gr.DrawLine(Pens.Blue, centers[i], centers[j]);
                    }
                }
            }

            return bm;
        }


        // Draw the indicated star in the rectangle.
        private void DrawStar2(Graphics gr, Pen the_pen, Brush the_brush, int num_points, int skip, Rectangle rect)
        {
            // Get the star's points.
            PointF[] star_points = MakeStarPoints(-Math.PI / 2, num_points, skip, rect);

            // Draw the star.
            gr.FillPolygon(the_brush, star_points);
            gr.DrawPolygon(the_pen, star_points);
        }

        // Draw with a compound pen.
        private void pictureBox_star1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            using (Pen the_pen = new Pen(Color.Blue, 20))
            {
                the_pen.CompoundArray = new float[] { 0.0f, 0.1f, 0.2f, 0.8f, 0.9f, 1.0f };

                // Draw the star.
                Rectangle rect = new Rectangle(35, 40, this.pictureBox_star1.ClientSize.Width - 70, this.pictureBox_star1.ClientSize.Height - 50);
                DrawStar2(e.Graphics, the_pen, Brushes.White, 5, 2, rect);
            }
        }

        // 畫星形 ST
        private void pictureBox_star2_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            PointF[] pts = StarPoints(5, this.pictureBox_star2.ClientRectangle);
            e.Graphics.DrawPolygon(Pens.Blue, pts);
        }

        // Draw the star.
        private void pictureBox_star3_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the star.
            DrawStar(e.Graphics, Pens.Red, Brushes.Yellow, (int)nudPoints.Value, (int)nudSkip.Value, this.pictureBox_star3.ClientRectangle);
        }

        // Return PointFs to define a star.
        private PointF[] StarPoints(int num_points, Rectangle bounds)
        {
            // Make room for the points.
            PointF[] pts = new PointF[num_points];

            double rx = bounds.Width / 2;
            double ry = bounds.Height / 2;
            double cx = bounds.X + rx;
            double cy = bounds.Y + ry;

            // Start at the top.
            double theta = -Math.PI / 2;
            double dtheta = 4 * Math.PI / num_points;
            for (int i = 0; i < num_points; i++)
            {
                pts[i] = new PointF(
                    (float)(cx + rx * Math.Cos(theta)),
                    (float)(cy + ry * Math.Sin(theta)));
                theta += dtheta;
            }
            return pts;
        }

        // 畫星形 SP

        // 畫星形2 ST
        // For information on star polygons, see:
        // http://en.wikipedia.org/wiki/Star_polygon
        // Redraw the star with the new parameters.
        private void nudPoints_ValueChanged(object sender, EventArgs e)
        {
            //nudSkip.Maximum = (int)(((int)nudPoints.Value - 1) / 2.0);
            this.pictureBox_star3.Refresh();
        }
        private void nudSkip_ValueChanged(object sender, EventArgs e)
        {
            this.pictureBox_star3.Refresh();
        }

        // Draw the indicated star in the rectangle.
        private void DrawStar(Graphics gr, Pen the_pen, Brush the_brush, int num_points, int skip, Rectangle rect)
        {
            // Get the star's points.
            PointF[] star_points = MakeStarPoints(-Math.PI / 2, num_points, skip, rect);

            // Draw the star.
            gr.FillPolygon(the_brush, star_points);
            gr.DrawPolygon(the_pen, star_points);
        }

        // Generate the points for a star.
        private PointF[] MakeStarPoints(double start_theta, int num_points, int skip, Rectangle rect)
        {
            double theta, dtheta;
            PointF[] result;
            float rx = rect.Width / 2f;
            float ry = rect.Height / 2f;
            float cx = rect.X + rx;
            float cy = rect.Y + ry;

            // If this is a polygon, don't bother with concave points.
            if (skip == 1)
            {
                result = new PointF[num_points];
                theta = start_theta;
                dtheta = 2 * Math.PI / num_points;
                for (int i = 0; i < num_points; i++)
                {
                    result[i] = new PointF(
                        (float)(cx + rx * Math.Cos(theta)),
                        (float)(cy + ry * Math.Sin(theta)));
                    theta += dtheta;
                }
                return result;
            }

            // Find the radius for the concave vertices.
            double concave_radius = CalculateConcaveRadius(num_points, skip);

            // Make the points.
            result = new PointF[2 * num_points];
            theta = start_theta;
            dtheta = Math.PI / num_points;
            for (int i = 0; i < num_points; i++)
            {
                result[2 * i] = new PointF(
                    (float)(cx + rx * Math.Cos(theta)),
                    (float)(cy + ry * Math.Sin(theta)));
                theta += dtheta;
                result[2 * i + 1] = new PointF(
                    (float)(cx + rx * Math.Cos(theta) * concave_radius),
                    (float)(cy + ry * Math.Sin(theta) * concave_radius));
                theta += dtheta;
            }
            return result;
        }

        // Calculate the inner star radius.
        private double CalculateConcaveRadius(int num_points, int skip)
        {
            // For really small numbers of points.
            if (num_points < 5) return 0.33f;

            // Calculate angles to key points.
            double dtheta = 2 * Math.PI / num_points;
            double theta00 = -Math.PI / 2;
            double theta01 = theta00 + dtheta * skip;
            double theta10 = theta00 + dtheta;
            double theta11 = theta10 - dtheta * skip;

            // Find the key points.
            PointF pt00 = new PointF(
                (float)Math.Cos(theta00),
                (float)Math.Sin(theta00));
            PointF pt01 = new PointF(
                (float)Math.Cos(theta01),
                (float)Math.Sin(theta01));
            PointF pt10 = new PointF(
                (float)Math.Cos(theta10),
                (float)Math.Sin(theta10));
            PointF pt11 = new PointF(
                (float)Math.Cos(theta11),
                (float)Math.Sin(theta11));

            // See where the segments connecting the points intersect.
            bool lines_intersect, segments_intersect;
            PointF intersection, close_p1, close_p2;
            FindIntersection(pt00, pt01, pt10, pt11,
                out lines_intersect, out segments_intersect,
                out intersection, out close_p1, out close_p2);

            // Calculate the distance between the
            // point of intersection and the center.
            return Math.Sqrt(
                intersection.X * intersection.X +
                intersection.Y * intersection.Y);
        }

        // Find the point of intersection between
        // the lines p1 --> p2 and p3 --> p4.
        private void FindIntersection(
            PointF p1, PointF p2, PointF p3, PointF p4,
            out bool lines_intersect, out bool segments_intersect,
            out PointF intersection,
            out PointF close_p1, out PointF close_p2)
        {
            // Get the segments' parameters.
            float dx12 = p2.X - p1.X;
            float dy12 = p2.Y - p1.Y;
            float dx34 = p4.X - p3.X;
            float dy34 = p4.Y - p3.Y;

            // Solve for t1 and t2
            float denominator = (dy12 * dx34 - dx12 * dy34);

            float t1 =
                ((p1.X - p3.X) * dy34 + (p3.Y - p1.Y) * dx34)
                    / denominator;
            if (float.IsInfinity(t1))
            {
                // The lines are parallel (or close enough to it).
                lines_intersect = false;
                segments_intersect = false;
                intersection = new PointF(float.NaN, float.NaN);
                close_p1 = new PointF(float.NaN, float.NaN);
                close_p2 = new PointF(float.NaN, float.NaN);
                return;
            }
            lines_intersect = true;

            float t2 =
                ((p3.X - p1.X) * dy12 + (p1.Y - p3.Y) * dx12)
                    / -denominator;

            // Find the point of intersection.
            intersection = new PointF(p1.X + dx12 * t1, p1.Y + dy12 * t1);

            // The segments intersect if t1 and t2 are between 0 and 1.
            segments_intersect =
                ((t1 >= 0) && (t1 <= 1) &&
                 (t2 >= 0) && (t2 <= 1));

            // Find the closest points on the segments.
            if (t1 < 0)
            {
                t1 = 0;
            }
            else if (t1 > 1)
            {
                t1 = 1;
            }

            if (t2 < 0)
            {
                t2 = 0;
            }
            else if (t2 > 1)
            {
                t2 = 1;
            }

            close_p1 = new PointF(p1.X + dx12 * t1, p1.Y + dy12 * t1);
            close_p2 = new PointF(p3.X + dx34 * t2, p3.Y + dy34 * t2);
        }

        // 畫星形2 SP

        //畫floodfill ST
        // The background image.
        private Bitmap bm_floodfill;
        private Bitmap32 bm32_floodfill;

        void draw_some_random_circles()     // Make some random circles.
        {
            int W = this.pictureBox_floodfill.ClientSize.Width;
            int H = this.pictureBox_floodfill.ClientSize.Height;

            bm_floodfill = new Bitmap(W, H);
            using (Graphics gr = Graphics.FromImage(bm_floodfill))
            {
                gr.Clear(Color.Silver);

                Random rnd = new Random();
                int max_r = Math.Min(W, H) / 3;
                int min_r = max_r / 4;
                for (int i = 0; i < 15; i++)
                {
                    int r = rnd.Next(min_r, max_r);
                    int x = rnd.Next(min_r, W - min_r);
                    int y = rnd.Next(min_r, H - min_r);
                    gr.DrawEllipse(Pens.Black, x - r, y - r, 2 * r, 2 * r);
                }
            }

            bm32_floodfill = new Bitmap32(bm_floodfill);
            this.pictureBox_floodfill.Image = bm_floodfill;
        }

        // Initialize the colors.
        private Color[] colors = 
        {
            Color.Red,
            Color.Orange,
            Color.Yellow,
            Color.Lime,
            Color.Cyan,
            Color.Blue,
            Color.Green,
            Color.Blue,
            Color.LightBlue,
            Color.LightGreen,
            Color.White
        };
        private Random random = new Random();
        private Color RandomColor()
        {
            return colors[random.Next(0, colors.Length)];
        }

        // Flood the clicked point with a random color.
        private void pictureBox_floodfill_MouseClick(object sender, MouseEventArgs e)
        {
            // Skip it if it's a black pixel.
            Color old_color = bm_floodfill.GetPixel(e.X, e.Y);
            if ((old_color.R == 0) && (old_color.G == 0) && (old_color.B == 0))
            {
                return;
            }

            // Flood at the pixel.
            bm32_floodfill.LockBitmap();
            //this.Text = "(" + e.X.ToString() + ", " + e.Y.ToString() + ")";
            bm32_floodfill.FloodFill(e.X, e.Y, RandomColor());
            bm32_floodfill.UnlockBitmap();
            Refresh();
            this.pictureBox_floodfill.Refresh();
        }

        //畫floodfill SP


        //畫triangle_puzzle_solution ST
        void draw_triangle_puzzle_solution()
        {
            // Define the points and solutions.
            label16.Text = "";

            DoubleBuffered = true;

            // Define the points.
            float dy = this.pictureBox_triangle_puzzle_solution.ClientSize.Height / 4;
            float dx = (float)(dy / Math.Sqrt(3));
            float top_x = this.pictureBox_triangle_puzzle_solution.ClientSize.Width / 2;
            float top_y = -dy / 2;
            Points = new PointF[]
                {
                    new PointF(top_x - dx, top_y + dy),
                    new PointF(top_x + dx, top_y + dy),
                    new PointF(top_x - 2 * dx, top_y + 2 * dy),
                    new PointF(top_x - 0 * dx, top_y + 2 * dy),
                    new PointF(top_x + 2 * dx, top_y + 2 * dy),
                    new PointF(top_x - 3 * dx, top_y + 3 * dy),
                    new PointF(top_x - 1 * dx, top_y + 3 * dy),
                    new PointF(top_x + 1 * dx, top_y + 3 * dy),
                    new PointF(top_x + 3 * dx, top_y + 3 * dy),
                    new PointF(top_x - 2 * dx, top_y + 4 * dy),
                    new PointF(top_x - 0 * dx, top_y + 4 * dy),
                    new PointF(top_x + 2 * dx, top_y + 4 * dy),
                };

            // Define the solutions.
            Solutions = new List<int[]>();
            Solutions.Add(new int[] { 0, 2, 3 });
            Solutions.Add(new int[] { 0, 3, 1 });
            Solutions.Add(new int[] { 1, 3, 4 });
            Solutions.Add(new int[] { 2, 5, 6 });
            Solutions.Add(new int[] { 2, 6, 3 });
            Solutions.Add(new int[] { 3, 6, 7 });
            Solutions.Add(new int[] { 3, 7, 4 });
            Solutions.Add(new int[] { 4, 7, 8 });
            Solutions.Add(new int[] { 5, 9, 6 });
            Solutions.Add(new int[] { 6, 9, 10 });
            Solutions.Add(new int[] { 6, 10, 7 });
            Solutions.Add(new int[] { 7, 10, 11 });
            Solutions.Add(new int[] { 7, 11, 8 });

            Solutions.Add(new int[] { 0, 5, 7 });
            Solutions.Add(new int[] { 1, 6, 8 });
            Solutions.Add(new int[] { 3, 9, 11 });
            Solutions.Add(new int[] { 10, 2, 4 });

            Solutions.Add(new int[] { 5, 10, 3 });
            Solutions.Add(new int[] { 2, 7, 1 });
            Solutions.Add(new int[] { 6, 11, 4 });
            Solutions.Add(new int[] { 8, 3, 10 });
            Solutions.Add(new int[] { 4, 6, 0 });
            Solutions.Add(new int[] { 7, 9, 2 });

            Solutions.Add(new int[] { 0, 9, 8 });
            Solutions.Add(new int[] { 1, 5, 11 });
        }

        // Draw a solution.
        private void DrawSolution(Graphics gr, int solution_num)
        {
            if (solution_num >= Solutions.Count)
            {
                return;
            }

            // Get the right color for this solution.
            Pen the_pen;
            if (solution_num < 13) the_pen = Pens.Red;
            else if (solution_num < 17) the_pen = Pens.Green;
            else if (solution_num < 23) the_pen = Pens.Purple;
            else the_pen = Pens.Orange;

            // Make a list of the points in this solution.
            List<PointF> pts = new List<PointF>();
            foreach (int i in Solutions[solution_num]) pts.Add(Points[i]);
            gr.DrawPolygon(the_pen, pts.ToArray());
        }

        // Draw the circles and any triangles currently defined.
        private void pictureBox_triangle_puzzle_solution_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the points.
            const float radius = 5;
            foreach (PointF pt in Points)
            {
                e.Graphics.FillEllipse(Brushes.Blue,
                    pt.X - radius, pt.Y - radius,
                    2 * radius, 2 * radius);
            }

            // Draw the current solution.
            if (CurrentSolution < 0)
            {
                // Draw all solutions.
                for (int i = 0; i < Solutions.Count; i++)
                {
                    DrawSolution(e.Graphics, i);
                }
                label16.Text = Solutions.Count.ToString();
            }
            else
            {
                // Draw the current solution.
                DrawSolution(e.Graphics, CurrentSolution);
                if (CurrentSolution < Solutions.Count)
                {
                    label16.Text = (CurrentSolution + 1).ToString();
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // Start showing solutions.
            // Start at the first solution.
            CurrentSolution = 0;

            // Start the timer.
            timer_triangle_puzzle_solution.Enabled = true;

            // Redraw.
            Refresh();
            this.pictureBox_triangle_puzzle_solution.Refresh();

        }

        private void button2_Click(object sender, EventArgs e)
        {
            // Show all of the solutions.
            CurrentSolution = -1;
            timer_triangle_puzzle_solution.Enabled = false;
            //btnShowSolutions.Enabled = true;
            Refresh();
            this.pictureBox_triangle_puzzle_solution.Refresh();
        }

        // Show the next solution.
        private void timer_triangle_puzzle_solution_Tick(object sender, EventArgs e)
        {
            // Increment CurrentSolution. If the result is greater than the
            // last solution's index, disable the timer.
            CurrentSolution++;
            timer_triangle_puzzle_solution.Enabled = (CurrentSolution < Solutions.Count);
            this.Text = CurrentSolution.ToString() + " " + timer_triangle_puzzle_solution.Enabled.ToString();

            // If we're done drawing, enable the button.
            //btnShowSolutions.Enabled = (!timer_triangle_puzzle_solution.Enabled);

            // Redraw.
            Refresh();
            this.pictureBox_triangle_puzzle_solution.Refresh();
        }



        //畫triangle_puzzle_solution SP



        //畫find_squares_colored ST

        void draw_find_squares_colored()
        {
            // Define the points and solutions.
            DoubleBuffered = true;
            int W = pictureBox_find_squares_colored.ClientSize.Width;
            int H = pictureBox_find_squares_colored.ClientSize.Height;

            // Define the points.
            float dx = Math.Min(W, H) / 4;
            float dy = dx;
            float x0 = (W - 3 * dx) / 2;
            float y0 = (H - 3 * dy) / 2;
            Points2 = new PointF[]
            {
                new PointF(x0 + dx, y0),
                new PointF(x0 + 2 * dx, y0),
                new PointF(x0, y0 + dy),
                new PointF(x0 + dx, y0 + dy),
                new PointF(x0 + 2 * dx, y0 + dy),
                new PointF(x0 + 3 * dx, y0 + dy),
                new PointF(x0, y0 + 2 * dy),
                new PointF(x0 + dx, y0 + 2 * dy),
                new PointF(x0 + 2 * dx, y0 + 2 * dy),
                new PointF(x0 + 3 * dx, y0 + 2 * dy),
                new PointF(x0 + dx, y0 + 3 * dy),
                new PointF(x0 + 2 * dx, y0 + 3 * dy),
            };

            // Define the solutions and side lengths.
            Solutions2 = new List<int[]>();
            SideLengths = new List<int>();

            // Find the solutions.
            FindSolutions();
        }

        // Find the solutions.
        private void FindSolutions()
        {
            for (int i = 0; i < Points2.Length - 3; i++)
            {
                for (int j = i + 1; j < Points2.Length - 2; j++)
                {
                    for (int k = j + 1; k < Points2.Length - 1; k++)
                    {
                        for (int m = k + 1; m < Points2.Length; m++)
                        {
                            // See if these points make a square.
                            int[] square_points = GetSquarePoints(i, j, k, m);
                            if (square_points != null)
                            {
                                Solutions2.Add(square_points);

                                // Save the side length.
                                int side_length =
                                    (int)PointFDistance(Points2[i], Points2[j]);
                                if (!SideLengths.Contains(side_length))
                                    SideLengths.Add(side_length);
                            }
                        }
                    }
                }
            }
        }

        // If these points make up a square, return an array holding
        // them in an order that makes a square.
        // If the points don't make up a square, return null.
        private int[] GetSquarePoints(int i, int j, int k, int m)
        {
            // A small value for equality testing.
            const double tiny = 0.001;

            // Store all but the first index in an array.
            int[] indexes = { j, k, m };

            // Get the distances from point i to the others.
            float[] distances =
            {
                PointFDistance(Points2[i], Points2[j]),
                PointFDistance(Points2[i], Points2[k]),
                PointFDistance(Points2[i], Points2[m]),
            };

            // Sort the distances and the corresponding indexes.
            Array.Sort(distances, indexes);

            // If the two smaller distances are not roughly
            // the same (the side length), then this isn't a square.
            if (Math.Abs(distances[0] - distances[1]) > tiny) return null;

            // If the longer distance isn't roughly Sqr(2) times
            // the side length (the diagonal length), then this isn't a square.
            float diagonal_length = (float)(Math.Sqrt(2) * distances[0]);
            if (Math.Abs(distances[2] - diagonal_length) > tiny) return null;

            // See if the distance between the farther point and
            // the two closer points is roughly the side length.
            float distance1 = PointFDistance(Points2[indexes[2]], Points2[indexes[0]]);
            if (Math.Abs(distances[0] - distance1) > tiny) return null;
            float distance2 = PointFDistance(Points2[indexes[2]], Points2[indexes[1]]);
            if (Math.Abs(distances[0] - distance2) > tiny) return null;

            // It's a square!
            return new int[] { i, indexes[0], indexes[2], indexes[1] };
        }

        // Return the distance between two PointFs.
        private float PointFDistance(PointF point1, PointF point2)
        {
            float dx = point1.X - point2.X;
            float dy = point1.Y - point2.Y;
            return (float)Math.Sqrt(dx * dx + dy * dy);
        }

        // Draw a solution.
        private void DrawSolution2(Graphics gr, int solution_num)
        {
            if (solution_num >= Solutions2.Count)
            {
                return;
            }

            // Make a list of the points in this solution.
            List<PointF> pts = new List<PointF>();
            foreach (int i in Solutions2[solution_num])
            {
                pts.Add(Points2[i]);
            }

            // Get the side length.
            int side_length = (int)PointFDistance(pts[0], pts[1]);
            int index = SideLengths.IndexOf(side_length);

            // Make an appropriately colored brush and pen.
            Color fill_color = Color.FromArgb(64,
                Colors2[index].R,
                Colors2[index].G,
                Colors2[index].B);
            using (Brush brush = new SolidBrush(fill_color))
            {
                gr.FillPolygon(brush, pts.ToArray());
            }

            using (Pen pen = new Pen(Colors2[index], 0))
            {
                gr.DrawPolygon(pen, pts.ToArray());
            }
        }



        // Show the next solution.
        private void timer_find_squares_colored_Tick(object sender, EventArgs e)
        {
            // Increment CurrentSolution. If the result is greater than the
            // last solution's index, disable the timer.
            CurrentSolution2++;
            timer_find_squares_colored.Enabled = (CurrentSolution2 < Solutions2.Count);

            // If we're done drawing, enable the button.
            if (!timer_find_squares_colored.Enabled)
            {
                button1.Enabled = true;
                label17.Text = "";
            }

            // Redraw.
            Refresh();
        }

        // Start showing solutions.
        private void button3_Click(object sender, EventArgs e)
        {
            // Start at the first solution.
            CurrentSolution2 = 0;

            // Start the timer.
            timer_find_squares_colored.Enabled = true;

            // Redraw.
            Refresh();
        }

        // Show all of the solutions.
        private void button4_Click(object sender, EventArgs e)
        {
            CurrentSolution2 = -1;
            timer_find_squares_colored.Enabled = false;

            // Display the number of solutions.
            label17.Text = "square " + Solutions2.Count.ToString();

            // Redraw.
            Refresh();
        }

        // Draw the circles and any squares currently defined.
        private void pictureBox_find_squares_colored_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the points.
            const float radius = 5;
            foreach (PointF pt in Points2)
            {
                e.Graphics.FillEllipse(Brushes.Blue,
                    pt.X - radius, pt.Y - radius,
                    2 * radius, 2 * radius);
            }

            // Draw the current solution.
            if (CurrentSolution2 < 0)
            {
                // Draw all solutions.
                for (int i = 0; i < Solutions2.Count; i++)
                {
                    DrawSolution2(e.Graphics, i);
                }
            }
            else
            {
                // Draw the current solution.
                DrawSolution2(e.Graphics, CurrentSolution2);
                if (CurrentSolution2 < Solutions2.Count)
                {
                    label17.Text = "square " + (CurrentSolution2 + 1).ToString();
                }
            }
        }




        //畫find_squares_colored SP






    }
}
