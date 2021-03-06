// #define SAVE_FRAMES
#define USE_CASE1
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for CompositingQuality, SmoothingMode
using System.Drawing.Imaging;   //for ImageFormat
using System.Drawing.Text;      //for TextRenderingHint

using System.Diagnostics;       //for Debug

namespace vcs_Draw9_Example8_vcsh
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;
        int W = 250;
        int H = 250;

        // True if it is X's turn.
        private bool XsTurn = true;

        // A 2-D array holding the squares.
        private Label[,] Squares;

        //for histogram
        private const int MIN_VALUE = 0;
        private const int MAX_VALUE = 100;
        private float[] DataValues = new float[10];
        private Matrix Transformation;


        //for age
        // The mean and standard deviation data.
        private const int MinAge = 6;
        private float[] Means = { 62, 56, 43, 42, 39, 36, 32, 31, };
        private float[] StdDevs = { 15, 9, 8, 8, 7, 5, 5, 6, };

        // Some test points.
        private PointF[] TestPoints =
        {
            new PointF(6, 58),
            new PointF(7, 63),
            new PointF(9, 55),
            new PointF(11, 39),
            new PointF(13, 29),
        };

        //pictureBox4 的中心
        // Select the ellipse's center point.
        private PointF CenterPoint;


        //pictureBox10 眼睛
        // A thick pen.
        private Pen ThickPen = new Pen(Color.Black, 3);

        // The previous mouse location.
        private Point OldMousePos = new Point(-1, -1);

        // 畫派圖，可以偵測位置 ST    pictureBox17
        // The pie chart's center.
        private Point EllipseCenter;

        // The pie chart's drawing area.
        private Rectangle EllipseRect;

        // The ellipse's X and Y radii.
        private float EllipseRx, EllipseRy;

        // The slices' ending angles in degrees.
        // The first angle is 0 and marks the start of the first slice.
        private float[] Angles = { 0, 45, 80, 110, 130, 170, 220, 245, 300, 360 };

        // The slices' colors.
        private Brush[] ChartBrushes =
        {
            Brushes.Red, Brushes.LightGreen, Brushes.LightBlue,
            Brushes.Yellow, Brushes.Orange, Brushes.White,
            Brushes.Cyan, Brushes.Pink, Brushes.Black,
        };
        // 畫派圖，可以偵測位置 SP

        // 畫動態派圖 ST
        // Represents a pie slice.
        private struct Slice : IComparable
        {
            public Brush TopBrush, SideBrush;
            public Pen TopPen;
            public float StartAngle, SweepAngle, ExplodeDistance;
            public float ZDistance
            {
                get
                {
                    // Right half of the ellipse.
                    if (StartAngle <= 90)
                    {
                        if (StartAngle + SweepAngle > 90)
                        {
                            // It spans the bottom of the
                            // ellipse so should be last.
                            return 181;
                        }
                        return 90 + StartAngle + SweepAngle;
                    }

                    // Left half of the ellipse.
                    return 270 - StartAngle;
                }
            }

            #region IComparable Members

            // Compare by ZDistance.
            public int CompareTo(object obj)
            {
                Slice other = (Slice)obj;
                return ZDistance.CompareTo(other.ZDistance);
            }

            #endregion
        }

        // Colors.
        private Color[] TopColors =
        {
            Color.FromArgb(255, 128, 128),
            Color.FromArgb(128, 255, 128),
            Color.Red,
            Color.FromArgb(128, 128, 255),
            Color.Orange,
            Color.FromArgb(255, 255, 128),
            Color.Blue,
            Color.FromArgb(128, 255, 255),
            Color.FromArgb(255, 128, 255),
            Color.Yellow,
        };
        private Brush[] TopBrushes;
        private Pen[] TopPens;
        private Brush[] SideBrushes;

        // The data values.
        private float[] Values = new float[10];

        // The slice data.
        Slice[] Slices;

        int explode_pie1 = 2;
        int explode_pie2 = 7;
        // 畫動態派圖 SP

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            ResizeRedraw = true;
            DoubleBuffered = true;

            // Reduce flicker.
            DoubleBuffered = true;

            show_item_location();
            DrawHistogram();

            // Initialize the 2-D array holding the squares.
            Squares = new Label[,]
            {
                { lblSquare00, lblSquare01, lblSquare02},
                { lblSquare10, lblSquare11, lblSquare12},
                { lblSquare20, lblSquare21, lblSquare22},
            };

            DrawRose();
            DrawGraph(MinAge, Means, StdDevs);  //age

            //for histogram
            Random rnd = new Random();
            // Create data.
            for (int i = 0; i < DataValues.Length; i++)
            {
                DataValues[i] = rnd.Next(MIN_VALUE + 5, MAX_VALUE - 5);
            }

            //pictureBox4 的中心
            CenterPoint = new PointF(this.pictureBox4.ClientSize.Width / 2, this.pictureBox4.ClientSize.Height / 2);

            draw_random_pixel_image();
            draw_smiley();                  //pictureBox15
            draw_polygon_pathgradientbrush();   //pictureBox18
            load_move_ball();               //pictureBox19

            // 畫派圖，可以偵測位置 ST    pictureBox17
            // Initialize the pie chart data.
            const int margin = 10;
            int wid = pictureBox17.ClientSize.Width - 2 * margin;
            int hgt = pictureBox17.ClientSize.Height - 2 * margin;
            EllipseRect = new Rectangle(margin, margin, wid, hgt);
            EllipseRx = wid / 2;
            EllipseRy = hgt / 2;
            EllipseCenter = new Point(pictureBox17.ClientSize.Width / 2, pictureBox17.ClientSize.Height / 2);
            // 畫派圖，可以偵測位置 SP

            // 畫動態派圖 ST
            // Make some random data.
            DoubleBuffered = true;
            ResizeRedraw = true;

            // Make the random data.
            Random rand = new Random();
            for (int i = 0; i < Values.Length; i++)
            {
                Values[i] = rand.Next(1, 5);
            }

            // Make the pens and brushes.
            TopBrushes = new Brush[TopColors.Length];
            SideBrushes = new Brush[TopColors.Length];
            TopPens = new Pen[TopColors.Length];
            for (int i = 0; i < TopColors.Length; i++)
            {
                TopBrushes[i] = new SolidBrush(TopColors[i]);
                TopPens[i] = new Pen(TopColors[i]);
                Color side_color = Color.FromArgb(
                    TopColors[i].R / 2,
                    TopColors[i].G / 2,
                    TopColors[i].B / 2);
                SideBrushes[i] = new SolidBrush(side_color);
            }

            // Calculate slice drawing information.
            Slices = new Slice[Values.Length];
            float total = Values.Sum();
            float start_angle = -90;
            for (int i = 0; i < Values.Length; i++)
            {
                Slices[i].TopBrush = TopBrushes[i % TopBrushes.Length];
                Slices[i].TopPen = TopPens[i % TopPens.Length];
                Slices[i].SideBrush = SideBrushes[i % SideBrushes.Length];

                Slices[i].StartAngle = start_angle;
                Slices[i].SweepAngle = 360f * Values[i] / total;

                start_angle += Slices[i].SweepAngle;
            }

            // Sort by ZDistance.
            Array.Sort(Slices);


            ExplodeDistance = 0;
            timer_pie.Enabled = true;   //Start Pie exploding


            // 畫動態派圖 SP

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            bt_exit_setup();
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

            pictureBox1.Size = new Size(W, H);
            pictureBox2.Size = new Size(W, H);
            pictureBox3.Size = new Size(W, H);
            pictureBox4.Size = new Size(W, H - 40);
            pictureBox5.Size = new Size(W, H);
            pictureBox_histogram.Size = new Size(W, H);
            pictureBox_age.Size = new Size(W, H);
            pictureBox_color_wheel1.Size = new Size(W, H);
            pictureBox_color_wheel2.Size = new Size(W, H);
            pictureBox10.Size = new Size(W, H * 9 / 10);
            pictureBox_random_pixel_image.Size = new Size(W, H);
            pictureBox_arrow.Size = new Size(W, H);
            pictureBox_hilbert_curve.Size = new Size(W, H);
            pictureBox_sierpinski_curve.Size = new Size(W, H);
            pictureBox15.Size = new Size(W, H);
            pictureBox16.Size = new Size(W, H);
            pictureBox17.Size = new Size(W, H);
            pictureBox18.Size = new Size(W, H);
            pictureBox19.Size = new Size(W, H);
            pictureBox20.Size = new Size(W, H);
            pictureBox21.Size = new Size(W, H);
            pictureBox22.Size = new Size(W, H);
            pictureBox_pie.Size = new Size(W, H);
            pictureBox_rainbow.Size = new Size(W, H * 2 / 3);

            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox3.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox4.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            checkBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0 + H - 30);
            pictureBox5.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            pictureBox_histogram.Location = new Point(x_st + dx * 5, y_st + dy * 0);

            pictureBox_age.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox_color_wheel1.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            pictureBox_color_wheel2.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            pictureBox10.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            pictureBox_random_pixel_image.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            pictureBox_arrow.Location = new Point(x_st + dx * 5, y_st + dy * 1);

            pictureBox_hilbert_curve.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            pictureBox_hilbert_curve.BackColor = Color.Pink;
            pictureBox_sierpinski_curve.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            pictureBox15.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            pictureBox16.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            pictureBox17.Location = new Point(x_st + dx * 4, y_st + dy * 2);
            label1.Location = new Point(x_st + dx * 4+10, y_st + dy * 2+10);
            label1.Text = "";
            pictureBox18.Location = new Point(x_st + dx * 5, y_st + dy * 2);

            pictureBox19.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            pictureBox20.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            pictureBox21.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            pictureBox22.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            pictureBox_pie.Location = new Point(x_st + dx * 4, y_st + dy * 3);
            pictureBox_rainbow.Location = new Point(x_st + dx * 5, y_st + dy * 3);

            bt_save.Location = new Point(x_st + dx * 6 + 225, y_st + dy * 0 + 50);

            richTextBox1.Location = new Point(x_st + dx * 6 + 225-100, y_st + dy * 0 + 50+50);

            //richTextBox1.Size = new Size(bt_exit.Right - richTextBox1.Location.X, this.Height - richTextBox1.Location.Y - 25);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //ClientSize = new Size(bt_exit.Right + 10, richTextBox1.Bottom + 80);    //自動表單邊界

            pictureBox_color_wheel1.BackColor = Color.Red;
            pictureBox_color_wheel2.BackColor = Color.Green;

            //最大化螢幕
            //this.FormBorderStyle = FormBorderStyle.None;
            //this.WindowState = FormWindowState.Maximized;
            //bt_exit_setup();
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

        void DrawHistogram()
        {
            // Make some data.
            // Make an array to hold counts for values
            // between 2 and 12 with indexes between 0 and 10.
            int[] counts = new int[11];

            // Make the values.
            Random rand = new Random();
            for (int i = 0; i < 1000; i++)
            {
                // Roll two 6-sided dice.
                int new_value = rand.Next(1, 7) + rand.Next(1, 7);
                int index = new_value - 2;
                counts[index]++;
            }

            // Make a simple histogram.
            Label[] labels = { lbl2, lbl3, lbl4, lbl5, lbl6,
                lbl7, lbl8, lbl9, lbl10, lbl11, lbl12 };
            MakeHistogram(labels, counts);
        }

        // Display the values.
        private void MakeHistogram(Label[] labels, int[] values)
        {
            // Calculate a scale so the largest
            // value fits nicely on the form.
            int available_height = labels[0].Bottom - 5;
            int max = values.Max();
            float scale = available_height / (float)max;

            for (int i = 0; i < labels.Length; i++)
            {
                int height = (int)(scale * values[i]);
                labels[i].Top = labels[i].Bottom - height;
                labels[i].Height = height;
            }
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {

        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
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

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
        }

        // A square was clicked.
        private void lblSquare_Click(object sender, EventArgs e)
        {
            // Get the label clicked.
            Label lbl = sender as Label;

            // If the square is already taken, do nothing.
            if (lbl.Text != "") return;

            // Take it for the current player.
            if (XsTurn)
            {
                lbl.Text = "X";
            }
            else
            {
                lbl.Text = "O";
            }
            XsTurn = !XsTurn;
        }

        // Clear all squares.
        private void bt_ox_clear_Click(object sender, EventArgs e)
        {
            foreach (Label label in Squares)
                label.Text = "";
        }

        void DrawRose()
        {
            float A = 2.0f;
            int n = 3;
            int d = 4;

            // Make the Bitmap and associated Graphics object.
            Bitmap bm = new Bitmap(W, H);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.Clear(Color.White);
                gr.SmoothingMode = SmoothingMode.AntiAlias;

                // Set up a transformation to map the region
                // x/y = A +/- 0.1 onto the Bitmap.
                RectangleF rect = new RectangleF(
                    -A - 0.1f, -A - 0.1f, 2 * A + 0.2f, 2 * A + 0.2f);
                PointF[] pts =
                {
                    new PointF(0, bm.Height),
                    new PointF(bm.Width, bm.Height),
                    new PointF(0, 0),
                };
                gr.Transform = new Matrix(rect, pts);

                // Draw the curve.
                DrawCurve(gr, A, n, d);

                // Draw the axes.
                DrawAxes(gr, rect.Right);

                // Display the result and size the form to fit.
                pictureBox5.Image = bm;
                pictureBox5.SizeMode = PictureBoxSizeMode.AutoSize;
            }

        }

        private void DrawAxes(Graphics gr, float wxmax)
        {
            int xmax = (int)wxmax;
            using (Pen pen = new Pen(Color.Black, 0))
            {
                // Draw the X and Y axes.
                gr.DrawLine(pen, -wxmax, 0, wxmax, 0);
                gr.DrawLine(pen, 0, -wxmax, 0, wxmax);

                float tic = 0.1f;
                for (int x = -xmax; x <= xmax; x++)
                {
                    gr.DrawLine(pen, x, -tic, x, tic);
                    gr.DrawLine(pen, -tic, x, tic, x);
                }
            }
        }

        // Draw the curve.
        // n and d should be relatively prime.
        private void DrawCurve(Graphics gr, float A, int n, int d)
        {
            const int num_points = 1000;

            // Period is Pi * d if n and d are both odd. 2 * Pi * d otherwise.
            double period = Math.PI * d;
            if ((n % 2 == 0) || (d % 2 == 0)) period *= 2;

            double dtheta = period / num_points;
            List<PointF> points = new List<PointF>();
            double k = (double)n / d;
            for (int i = 0; i < num_points; i++)
            {
                double theta = i * dtheta;
                double r = A * Math.Cos(k * theta);
                float x = (float)(r * Math.Cos(theta));
                float y = (float)(r * Math.Sin(theta));

                points.Add(new PointF(x, y));
            }

            gr.FillPolygon(Brushes.LightBlue, points.ToArray());

            // Draw the curve.
            using (Pen pen = new Pen(Color.Red, 0))
            {
                gr.DrawLines(pen, points.ToArray());
            }
        }

        #region pictureBox3齒輪運轉圖

        // The angle used as the gears' origins.
        private float StartAngle = 0;
#if SAVE_FRAMES
        private float dStartAngle = (float)(Math.PI / 45);
#else
        private float dStartAngle = (float)(Math.PI / 180);
#endif


#if USE_CASE1
        // Draw the gear.
        private void pictureBox3_Paint(object sender, PaintEventArgs e)
        {
            // Draw smoothly.
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            const float radius = 50;
            const float tooth_length = 10;
            float x = pictureBox3.ClientSize.Width / 2 - radius - tooth_length - 1;
            float y = pictureBox3.ClientSize.Height / 3;
            DrawGear(StartAngle, e.Graphics, Brushes.Black, Brushes.LightBlue, Pens.Blue, new PointF(x, y),
                radius, tooth_length, 10, 5, true);

            x += 2 * radius + tooth_length + 2;
            DrawGear(-StartAngle, e.Graphics, Brushes.Black, Brushes.LightGreen, Pens.Green, new PointF(x, y),
                radius, tooth_length, 10, 5, false);

            y += 2f * radius + tooth_length + 2;
            DrawGear(StartAngle, e.Graphics, Brushes.Black, Brushes.Pink, Pens.Red, new PointF(x, y),
                radius, tooth_length, 10, 5, true);
        }
#else
        // Draw the gears.
        private void pictureBox3_Paint(object sender, PaintEventArgs e)
        {
            // Draw smoothly.
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            const float axel_radius = 5;
            const float radius = 50;
            const float tooth_length = 10;
            const int num_teeth = 10;
            const float green_ratio = 1.5f;
            const int num_green_teeth = (int)(num_teeth * green_ratio);
            float x = pictureBox3.ClientSize.Width / 2 - radius - tooth_length - 1;
            float y = pictureBox3.ClientSize.Height / 3;
            DrawGear(StartAngle, e.Graphics,
                Brushes.Black, Brushes.LightBlue,
                Pens.Blue, new PointF(x, y), radius,
                tooth_length, num_teeth, axel_radius, true);

            // Make the green gear 1.5 times as big (so it has 15 teeth).
            const float green_radius = (int)(radius * 1.5f);
            float green_angle = -StartAngle / 1.5f;
            x += radius + green_radius + tooth_length + 2;
            DrawGear(green_angle, e.Graphics,
                Brushes.Black, Brushes.LightGreen,
                Pens.Green, new PointF(x, y), green_radius,
                tooth_length, num_green_teeth, axel_radius, true);

            // Offset pink gear by half of one tooth.
            float pink_angle = (float)(StartAngle - 360 / num_teeth);
            y += radius + green_radius + tooth_length + 2;
            DrawGear(pink_angle, e.Graphics,
                Brushes.Black, Brushes.Pink,
                Pens.Red, new PointF(x, y), radius,
                tooth_length, num_teeth, axel_radius, true);
        }
#endif
        // Draw a gear.
        private void DrawGear(float start_angle, Graphics gr, Brush axle_brush, Brush gear_brush, Pen gear_pen, PointF center, float radius, float tooth_length, int num_teeth, float axle_radius, bool start_with_tooth)
        {
            float dtheta = (float)(Math.PI / num_teeth);
            float dtheta_degrees = (float)(dtheta * 180 / Math.PI);     // dtheta in degrees.

            const float chamfer = 2;
            float tooth_width = radius * dtheta - chamfer;
            float alpha = tooth_width / (radius + tooth_length);
            float alpha_degrees = (float)(alpha * 180 / Math.PI);
            float phi = (dtheta - alpha) / 2;

            // Set theta for the beginning of the first tooth.
            float theta = start_angle;
            if (start_with_tooth) theta += dtheta / 2;
            else theta -= dtheta / 2;

            // Make rectangles to represent the gear's inner and outer arcs.
            RectangleF inner_rect = new RectangleF(
                center.X - radius, center.Y - radius,
                2 * radius, 2 * radius);
            RectangleF outer_rect = new RectangleF(
                center.X - radius - tooth_length, center.Y - radius - tooth_length,
                2 * (radius + tooth_length), 2 * (radius + tooth_length));

            // Make a path representing the gear.
            GraphicsPath path = new GraphicsPath();
            for (int i = 0; i < num_teeth; i++)
            {
                // Move across the gap between teeth.
                float degrees = (float)(theta * 180 / Math.PI);
                path.AddArc(inner_rect, degrees, dtheta_degrees);
                theta += dtheta;

                // Move across the tooth's outer edge.
                degrees = (float)((theta + phi) * 180 / Math.PI);
                path.AddArc(outer_rect, degrees, alpha_degrees);
                theta += dtheta;
            }

            path.CloseFigure();

            // Draw the gear.
            gr.FillPath(gear_brush, path);
            gr.DrawPath(gear_pen, path);
            gr.FillEllipse(axle_brush,
                center.X - axle_radius, center.Y - axle_radius,
                2 * axle_radius, 2 * axle_radius);
        }

        // Increment the gears' start angle and redraw.
        private void timer_gear_Tick(object sender, EventArgs e)
        {
            StartAngle += dStartAngle;
            pictureBox3.Refresh();

#if SAVE_FRAMES
            if (frame_num < 9)
            {
                Bitmap bm = GetControlImage(this);
                bm.Save("Frame" + frame_num.ToString() + ".png",
                    System.Drawing.Imaging.ImageFormat.Png);
                frame_num++;
            }
#endif
        }

#if SAVE_FRAMES
        private int frame_num = 0;

        // Return a Bitmap holding an image of the control.
        private Bitmap GetControlImage(Control ctl)
        {
            Bitmap bm = new Bitmap(ctl.Width, ctl.Height);
            ctl.DrawToBitmap(bm, new Rectangle(0, 0, ctl.Width, ctl.Height));
            return bm;
        }
#endif
        #endregion

        #region pictureBox_histogram 柱狀圖

        // Draw the histogram.
        private void pictureBox_histogram_Paint(object sender, PaintEventArgs e)
        {
            DrawHistogram(e.Graphics, pictureBox_histogram.BackColor, DataValues, pictureBox_histogram.ClientSize.Width, pictureBox_histogram.ClientSize.Height);

            Font f = new Font("Comic Sans MS", 15);
            e.Graphics.DrawString("點選柱狀圖", f, new SolidBrush(Color.Red), 5, 5);
        }

        // Redraw.
        private void pictureBox_histogram_Resize(object sender, EventArgs e)
        {
            pictureBox_histogram.Refresh();
        }

        // Draw a histogram.
        private void DrawHistogram(Graphics gr, Color back_color, float[] values, int width, int height)
        {
            Color[] Colors = new Color[] {
                Color.Red, Color.LightGreen, Color.Blue,
                Color.Pink, Color.Green, Color.LightBlue,
                Color.Orange, Color.Yellow, Color.Purple
            };

            gr.Clear(back_color);

            // Make a transformation to the PictureBox.
            RectangleF data_bounds = new RectangleF(0, 0, values.Length, MAX_VALUE);
            PointF[] points =
            {
                new PointF(0, height),
                new PointF(width, height),
                new PointF(0, 0)
            };
            Transformation = new Matrix(data_bounds, points);
            gr.Transform = Transformation;

            // Draw the histogram.
            using (Pen thin_pen = new Pen(Color.Black, 0))
            {
                for (int i = 0; i < values.Length; i++)
                {
                    RectangleF rect = new RectangleF(i, 0, 1, values[i]);
                    using (Brush the_brush = new SolidBrush(Colors[i % Colors.Length]))
                    {
                        gr.FillRectangle(the_brush, rect);
                        gr.DrawRectangle(thin_pen, rect.X, rect.Y, rect.Width, rect.Height);
                    }
                }
            }

            gr.ResetTransform();
            gr.DrawRectangle(Pens.Black, 0, 0, width - 1, height - 1);
        }

        // Display the value clicked.
        private void pictureBox_histogram_MouseDown(object sender, MouseEventArgs e)
        {
            // Determine which data value was clicked.
            float bar_wid = pictureBox_histogram.ClientSize.Width / (int)DataValues.Length;
            int i = (int)(e.X / bar_wid);
            richTextBox1.Text += "點選第 " + (i + 1).ToString() + " 項, 數值: " + DataValues[i] + "\n";
        }

        // Record the mouse position.
        private string TipText;
        private void pictureBox_histogram_MouseMove(object sender, MouseEventArgs e)
        {
            if (Transformation == null)
            {
                richTextBox1.Text += "XXXXXXXXXXXX\n";  //Transformationg尚未初始化
                return;
            }
            // Determine which data value is under the mouse.
            float bar_wid = pictureBox_histogram.ClientSize.Width / (int)DataValues.Length;
            int bar_number = (int)(e.X / bar_wid);
            if (bar_number >= DataValues.Length) return;

            // Get the coordinates of the top of the bar.
            PointF[] points = { new PointF(0, DataValues[bar_number]) };
            Transformation.TransformPoints(points);

            // See if the mouse is over the bar and not the space above it.
            string tip = "";
            if (e.Y >= points[0].Y)
            {
                tip = "點選第 " + (bar_number + 1).ToString() + " 項, 數值: " + DataValues[bar_number];
            }

            // Update the tooltip if it has changed.
            if (TipText != tip)
            {
                TipText = tip;
                toolTip_histogram.SetToolTip(pictureBox_histogram, tip);
            }
        }

        #endregion

        #region pictureBox_age

        // Draw the graph.
        private void DrawGraph(int min_age, float[] means, float[] stddevs)
        {
            int max_age = min_age + means.Length - 1;

            // Get the minimum and maximum values.
            const float max_dev = 2.5f;
            float min_value = means[0] - max_dev * stddevs[0];
            float max_value = means[0] + max_dev * stddevs[0];
            for (int i = 0; i < means.Length; i++)
            {
                if (min_value > means[i] - max_dev * stddevs[i])
                    min_value = means[i] - max_dev * stddevs[i];
                if (max_value < means[i] + max_dev * stddevs[i])
                    max_value = means[i] + max_dev * stddevs[i];
            }
            if (min_value > 0) min_value = 0;

            float hgt = 1.2f * (max_value - min_value);
            float middle = (max_value + min_value) / 2f;
            min_value = middle - hgt / 2f;
            max_value = middle + hgt / 2f;

            // Make a transformation for drawing.
            RectangleF world = new RectangleF(
                min_age - 1f, min_value,
                max_age - min_age + 1.5f, max_value - min_value);
            PointF[] device_points =
            {
                new PointF(0, pictureBox_age.ClientSize.Height),
                new PointF(pictureBox_age.ClientSize.Width, pictureBox_age.ClientSize.Height),
                new PointF(0, 0),
            };
            Matrix transform = new Matrix(world, device_points);

            Bitmap bm = new Bitmap(
                pictureBox_age.ClientSize.Width,
                pictureBox_age.ClientSize.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                using (Pen pen = new Pen(Color.Red, 0))
                {
                    gr.SmoothingMode = SmoothingMode.AntiAlias;
                    gr.Transform = transform;

                    // Draw the standard deviation envelopes.
                    using (SolidBrush brush = new SolidBrush(Color.FromArgb(255, 128, 128)))
                    {
                        pen.Color = brush.Color;
                        DrawEnvelope(gr, min_age, means, stddevs,
                            2.5f, brush, pen);
                    }
                    using (SolidBrush brush = new SolidBrush(Color.FromArgb(255, 255, 128)))
                    {
                        pen.Color = brush.Color;
                        DrawEnvelope(gr, min_age, means, stddevs,
                            1.5f, brush, pen);
                    }
                    using (SolidBrush brush = new SolidBrush(Color.FromArgb(128, 255, 128)))
                    {
                        pen.Color = brush.Color;
                        DrawEnvelope(gr, min_age, means, stddevs,
                            0.5f, brush, pen);
                    }

                    // Draw the curve.
                    List<PointF> points = new List<PointF>();
                    for (int i = 0; i < means.Length; i++)
                        points.Add(new PointF(i + min_age, means[i]));
                    pen.Color = Color.Black;
                    gr.DrawLines(pen, points.ToArray());

                    // Draw and label the axes.
                    pen.Color = Color.Black;
                    using (Font font = new Font("Arial", 8))
                    {
                        gr.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;
                        using (StringFormat sf = new StringFormat())
                        {
                            sf.Alignment = StringAlignment.Center;
                            sf.LineAlignment = StringAlignment.Near;

                            // Draw the X axis.
                            // Draw the axis.
                            gr.DrawLine(pen, min_age, 0, max_age, 0);

                            // Draw the tick marks.
                            for (int x = min_age; x <= max_age; x++)
                                gr.DrawLine(pen, x, 0, x, max_value);

                            // Label the ages.
                            List<PointF> tick_points = new List<PointF>();
                            List<string> tick_labels = new List<string>();
                            PointF[] label_points_array;
                            for (int x = min_age; x <= max_age; x++)
                            {
                                tick_points.Add(new PointF(x, 0));
                                tick_labels.Add(x.ToString());
                            }
                            label_points_array = tick_points.ToArray();
                            transform.TransformPoints(label_points_array);
                            gr.Transform = new Matrix();
                            for (int i = 0; i < label_points_array.Length; i++)
                            {
                                gr.DrawString(tick_labels[i], font,
                                    Brushes.Black, label_points_array[i], sf);
                            }

                            // Draw the Y axis.
                            // Draw the axis.
                            gr.Transform = transform;
                            gr.DrawLine(pen, 0, min_value, 0, max_value);

                            // Draw the tick marks.
                            int start_y = 10;
                            int stop_y = 10 * (int)(max_value / 10f);
                            int num_y = stop_y - start_y + 1;
                            for (int y = start_y; y <= stop_y; y += 10)
                                gr.DrawLine(pen, min_age - 0.15f, y, min_age + 0.15f, y);

                            // Label the Y axis.
                            sf.Alignment = StringAlignment.Far;
                            sf.LineAlignment = StringAlignment.Center;

                            tick_points.Clear();
                            tick_labels.Clear();
                            for (int y = start_y; y <= stop_y; y += 10)
                            {
                                tick_points.Add(new PointF(min_age - 0.2f, y));
                                tick_labels.Add(y.ToString());
                            }
                            label_points_array = tick_points.ToArray();
                            transform.TransformPoints(label_points_array);

                            gr.Transform = new Matrix();
                            for (int y = 0; y < label_points_array.Length; y++)
                            {
                                gr.DrawString(tick_labels[y], font,
                                    Brushes.Black, label_points_array[y], sf);
                            }
                        } // StringFormat
                    } // Font

                    // Plot test points.
                    transform.TransformPoints(TestPoints);
                    gr.Transform = new Matrix();
                    foreach (PointF point in TestPoints)
                    {
                        gr.FillRectangle(Brushes.Red,
                            point.X - 3, point.Y - 3, 6, 6);
                    }
                } // Pen
            } // Graphics

            pictureBox_age.Image = bm;
        }

        // Draw an envelope for dev_mult times the standard deviations.
        private void DrawEnvelope(Graphics gr, int min_age,
            float[] means, float[] stddevs,
            float dev_mult, Brush brush, Pen pen)
        {
            List<PointF> points = new List<PointF>();
            for (int i = 0; i < means.Length; i++)
                points.Add(new PointF(i + min_age, means[i] + dev_mult * stddevs[i]));
            for (int i = means.Length - 1; i >= 0; i--)
                points.Add(new PointF(i + min_age, means[i] - dev_mult * stddevs[i]));

            gr.FillPolygon(brush, points.ToArray());
            gr.DrawPolygon(pen, points.ToArray());
        }

        #endregion

        private void pictureBox4_MouseMove(object sender, MouseEventArgs e)
        {
            CenterPoint = e.Location;
            this.pictureBox4.Refresh();
        }

        // Draw the elliptical gradient background.
        private void pictureBox4_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Make a GraphicsPath to represent the ellipse.
            Rectangle rect = new Rectangle(
                10, 10,
                this.pictureBox4.ClientSize.Width - 20,
                this.pictureBox4.ClientSize.Height - 20);
            GraphicsPath path = new GraphicsPath();
            path.AddEllipse(rect);

            // Make a PathGradientBrush from the path.
            using (PathGradientBrush br = new PathGradientBrush(path))
            {
                if (checkBox1.Checked == true)
                    br.CenterPoint = CenterPoint;
                br.CenterColor = Color.Blue;
                br.SurroundColors = new Color[] { this.pictureBox4.BackColor };
                e.Graphics.FillEllipse(br, rect);
            }
        }

        // See if the mouse has moved.
        private void timer_eyes_Tick(object sender, EventArgs e)
        {
            // See if the cursor has moved.
            Point new_pos = Control.MousePosition;
            if (new_pos.Equals(OldMousePos)) return;
            OldMousePos = new_pos;

            // Redraw.
            //this.pictureBox10.Invalidate(); //with flicker
            this.pictureBox10.Refresh();  //no flicker
        }

        private void pictureBox10_Paint(object sender, PaintEventArgs e)
        {
            DrawEyes(e.Graphics);
        }

        // Draw the eyes.
        private void DrawEyes(Graphics gr)
        {
            // Convert the cursor position into form units.
            Point local_pos = this.pictureBox10.PointToClient(OldMousePos);

            // Calculate the size of the eye.
            int hgt = (int)(this.pictureBox10.ClientSize.Height * 0.9);
            int wid = (int)(this.pictureBox10.ClientSize.Width * 0.45);

            // Find the positions of the eyes.
            int y = (this.pictureBox10.ClientSize.Height - hgt) / 2;
            int x1 = (int)((this.pictureBox10.ClientSize.Width - wid * 2) / 3);
            int x2 = wid + 2 * x1;

            // Create a Bitmap on which to draw.
            gr.SmoothingMode = SmoothingMode.AntiAlias;
            gr.Clear(this.pictureBox10.BackColor);

            // Draw the eyes.
            DrawEye(gr, local_pos, x1, y, wid, hgt);
            DrawEye(gr, local_pos, x2, y, wid, hgt);
        }

        // Draw an eye here.
        private void DrawEye(Graphics gr, Point local_pos, int x1, int y1, int wid, int hgt)
        {
            // Draw the outside.
            gr.FillEllipse(Brushes.White, x1, y1, wid, hgt);
            gr.DrawEllipse(ThickPen, x1, y1, wid, hgt);

            // Find the center of the eye.
            int cx = x1 + wid / 2;
            int cy = y1 + hgt / 2;

            // Get the unit vector pointing towards the mouse position.
            double dx = local_pos.X - cx;
            double dy = local_pos.Y - cy;
            double dist = Math.Sqrt(dx * dx + dy * dy);
            dx /= dist;
            dy /= dist;

            // This point is 1/4 of the way
            // from the center to the edge of the eye.
            double px = cx + dx * wid / 4;
            double py = cy + dy * hgt / 4;

            // Draw an ellipse 1/2 the size of the eye
            // centered at (px, py).
            gr.FillEllipse(Brushes.Blue, (int)(px - wid / 4),
                (int)(py - hgt / 4), wid / 2, hgt / 2);
        }

        void draw_random_pixel_image()
        {
            pictureBox_random_pixel_image.BackColor = Color.Pink;
            int width = pictureBox_random_pixel_image.ClientSize.Width;
            int height = pictureBox_random_pixel_image.ClientSize.Height;

            //bitmap
            Bitmap bmp = new Bitmap(width, height);

            //random number
            Random rand = new Random();

            //create random pixels
            for (int y = 0; y < height; y++)
            {
                for (int x = 0; x < width; x++)
                {
                    //generate random ARGB value
                    int a = rand.Next(256);
                    int r = rand.Next(256);
                    int g = rand.Next(256);
                    int b = rand.Next(256);

                    //set ARGB value
                    if (y < height * 1 / 3)
                        bmp.SetPixel(x, y, Color.FromArgb(50, r, g, b));    //上
                    else if (y < height * 2 / 3)
                        bmp.SetPixel(x, y, Color.FromArgb(a, r, g, b));     //中
                    else
                        bmp.SetPixel(x, y, Color.FromArgb(255, r, g, b));   //下
                }
            }

            //load bmp in pictureBox_random_pixel_image
            pictureBox_random_pixel_image.Image = bmp;
        }

        // 畫Smiley ST
        private delegate float FofXY(float x, float y);

        // Plot the equations.
        void draw_smiley()
        {
            // Make the Bitmap.
            Bitmap bm = new Bitmap(pictureBox15.ClientSize.Width, pictureBox15.ClientSize.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                // Clear.
                gr.Clear(Color.White);
                gr.ScaleTransform(24f, -24f, System.Drawing.Drawing2D.MatrixOrder.Append);
                gr.TranslateTransform(bm.Width * 0.5f, bm.Height * 0.5f,
                    System.Drawing.Drawing2D.MatrixOrder.Append);

                // Draw axes.
                using (Pen axis_pen = new Pen(Color.Blue, 0))
                {
                    gr.DrawLine(axis_pen, -6, 0, 6, 0);
                    gr.DrawLine(axis_pen, 0, -6, 0, 6);
                    for (int i = -6; i <= 6; i++)
                    {
                        gr.DrawLine(axis_pen, i, -0.1f, i, 0.1f);
                        gr.DrawLine(axis_pen, -0.1f, i, 0.1f, i);
                    }
                }

                // Graph the equations.
                float dx = 2f / bm.Width;
                float dy = 2f / bm.Height;
                PlotFunction(gr, F1, -6, -6, 6, 6, dx, dy);
                PlotFunction(gr, F2, -6, -6, 6, 6, dx, dy);
            } // using gr.

            // Display the result.
            pictureBox15.Image = bm;
        }

        // Plot a function.
        private void PlotFunction(Graphics gr, FofXY func,
            float xmin, float ymin, float xmax, float ymax,
            float dx, float dy)
        {
            // Plot the function.
            using (Pen thin_pen = new Pen(Color.Black, 0))
            {
                // Horizontal comparisons.
                for (float x = xmin; x <= xmax; x += dx)
                {
                    float last_y = func(x, ymin);
                    for (float y = ymin + dy; y <= ymax; y += dy)
                    {
                        float next_y = func(x, y);
                        if (
                            ((last_y <= 0f) && (next_y >= 0f)) ||
                            ((last_y >= 0f) && (next_y <= 0f))
                           )
                        {
                            // Plot this point.
                            gr.DrawLine(thin_pen, x, y - dy, x, y);
                        }
                        last_y = next_y;
                    }
                } // Horizontal comparisons.

                // Vertical comparisons.
                for (float y = ymin + dy; y <= ymax; y += dy)
                {
                    float last_x = func(xmin, y);
                    for (float x = xmin + dx; x <= xmax; x += dx)
                    {
                        float next_x = func(x, y);
                        if (
                            ((last_x <= 0f) && (next_x >= 0f)) ||
                            ((last_x >= 0f) && (next_x <= 0f))
                           )
                        {
                            // Plot this point.
                            gr.DrawLine(thin_pen, x - dx, y, x, y);
                        }
                        last_x = next_x;
                    }
                } // Vertical comparisons.
            } // using thin_pen.
        }

        // Calculate:
        //   [x^2 + y^2 - 225] *
        //   [x^2 + y^2 - 10000] *
        //   [(x - 45)^2 + (y - 35)^2 - 225] *
        //   [(x + 45)^2 + (y - 35)^2 - 225]
        private float F1(float x, float y)
        {
            // Flip y to make the image appear right side up.
            return
                (x * x + y * y - 25f) *
                (x * x + y * y - 1f) *
                ((x - 2.5f) * (x - 2.5f) + (y - 2.0f) * (y - 2.0f) - 1f) *
                ((x + 2.5f) * (x + 2.5f) + (y - 2.0f) * (y - 2.0f) - 1f);
        }

        // Calculate:
        //   y + Sqrt(16 - x^2)
        private float F2(float x, float y)
        {
            return (float)(y + Math.Sqrt(12.25f - x * x));
        }
        // 畫Smiley SP

        // 畫星形，可以偵測位置 ST
        // The polygon's points.
        Point[] Points = 
        {
            new Point(133,  14),
            new Point( 44, 228),
            new Point(255,  83),
            new Point( 16,  74),
            new Point(214, 246),
        };

        // Draw the polygon.
        private void pictureBox16_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            e.Graphics.FillPolygon(Brushes.Yellow, Points);
            e.Graphics.DrawPolygon(Pens.Red, Points);
            Font f = new Font("Comic Sans MS", 12);
            e.Graphics.DrawString("偵測滑鼠位置", f, new SolidBrush(Color.Red), 5, 5);
        }

        // Set the cursor depending on whether the mouse is over the polygon.
        private void pictureBox16_MouseMove(object sender, MouseEventArgs e)
        {
            Cursor new_cursor;
            if (PointIsInPolygon(Points, e.Location))
                new_cursor = Cursors.Cross;
            else new_cursor = Cursors.Default;

            // Update the cursor.
            if (this.Cursor != new_cursor) this.Cursor = new_cursor;
        }

        // Return true if the point is inside the polygon.
        private bool PointIsInPolygon(Point[] polygon, Point target_point)
        {
            // Make a GraphicsPath containing the polygon.
            GraphicsPath path = new GraphicsPath();
            path.AddPolygon(polygon);

            // See if the point is inside the path.
            return path.IsVisible(target_point);
        }
        // 畫星形，可以偵測位置 SP

        // 畫派圖，可以偵測位置 ST    pictureBox17
        // Draw the pie slices.
        private void pictureBox17_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            e.Graphics.FillEllipse(Brushes.Blue, EllipseRect);
            for (int i = 1; i < Angles.Length; i++)
            {
                e.Graphics.FillPie(ChartBrushes[i - 1],
                    EllipseRect, Angles[i], Angles[i - 1] - Angles[i]);
            }
            e.Graphics.DrawEllipse(Pens.Blue, EllipseRect);
        }

        // Display the number of the slice under the mouse.
        private void pictureBox17_MouseMove(object sender, MouseEventArgs e)
        {
            // Get the slice number.
            int slice_number = GetSliceNumber(EllipseRect, Angles, e.Location);

            // Display the slice number.
            if (slice_number == -1)
                label1.Text = "";
            else
                label1.Text = slice_number.ToString() + "\n";
        }

        // Return the slice number or -1 if the 
        // mouse isn't over a slice.
        private int GetSliceNumber(Rectangle rect, float[] angles, Point point)
        {
            // Get the position relative to the ellipse's center.
            float rx = rect.Width / 2;
            float ry = rect.Height / 2;
            float cx = rect.X + rx;
            float cy = rect.Y + ry;
            float dx = point.X - cx;
            float dy = point.Y - cy;
            float value =
                dx * dx / rx / rx +
                dy * dy / ry / ry;

            // See if the mouse is at the center.
            if (value < 0.0001) return -1;

            // See if the point is outside of the ellipse.
            if (value > 1) return -1;

            // The point is inside the ellipse.
            // Get the angle.
            double angle = Math.Atan2(dy, dx);
            if (angle < 0) angle += 2 * Math.PI;

            // Convert the angle into degrees.
            angle = angle * 180 / Math.PI;

            // Get the slice number.
            for (int i = 0; i < Angles.Length - 1; i++)
                if (angle <= Angles[i + 1]) return i;

            throw new Exception("Cannot find angle " + angle);
        }
        // 畫派圖，可以偵測位置 SP


        void draw_polygon_pathgradientbrush()
        {
            pictureBox18.Refresh();


        }


        private void timer_change_draw_figure_Tick(object sender, EventArgs e)
        {

        }

        // Fill a polygon with a PathGradientBrush.
        private void pictureBox18_Paint(object sender, PaintEventArgs e)
        {
            // Make the points for a hexagon.
            PointF[] pts = new PointF[6];
            int cx = (int)(this.pictureBox18.ClientSize.Width / 2);
            int cy = (int)(this.pictureBox18.ClientSize.Height / 2);
            double theta = 0;
            double dtheta = 2 * Math.PI / 6;
            for (int i = 0; i < pts.Length; i++)
            {
                pts[i].X = (int)(cx + cx * Math.Cos(theta));
                pts[i].Y = (int)(cy + cy * Math.Sin(theta));
                theta += dtheta;
            }

            // Make a path gradient brush.
            using (PathGradientBrush path_brush = new PathGradientBrush(pts))
            {
                // Define the center and surround colors.
                path_brush.CenterColor = Color.White;
                path_brush.SurroundColors = new Color[] { Color.Red, Color.Yellow, Color.Lime, Color.Cyan, Color.Blue, Color.Magenta };

                // Fill the hexagon.
                e.Graphics.FillPolygon(path_brush, pts);
            }
            // Outline the hexagon.
            e.Graphics.DrawPolygon(Pens.Black, pts);
        }


        // Some drawing parameters.
        private BallSprite[] Sprites;

        void load_move_ball()
        {
            // Make random balls.
            Random rand = new Random();
            const int num_balls = 10;
            Sprites = new BallSprite[num_balls];
            for (int i = 0; i < num_balls; i++)
            {
                Sprites[i] = new BallSprite(10, 40, pictureBox19.ClientSize.Width, pictureBox19.ClientSize.Height, 2, 10);
            }

            // Save the form's size.
            //FormSize = ClientSize;

            // Use double buffering to reduce flicker.
            this.SetStyle(
                ControlStyles.AllPaintingInWmPaint |
                ControlStyles.UserPaint |
                ControlStyles.DoubleBuffer,
                true);
            this.UpdateStyles();
        }

        // Move the balls and refresh.
        private void timer_move_ball_Tick(object sender, EventArgs e)
        {
            foreach (BallSprite sprite in Sprites)
                sprite.Move();
            Refresh();
        }

        // Redraw.
        private void pictureBox19_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            e.Graphics.Clear(BackColor);
            foreach (BallSprite sprite in Sprites)
                sprite.Draw(e.Graphics);

        }

        // Force all threads to end.
        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            Environment.Exit(0);
        }



        // Draw rainbow colors on the form.
        private void pictureBox_rainbow_Paint(object sender, PaintEventArgs e)
        {
            int wid = this.pictureBox_rainbow.ClientSize.Width;
            int hgt = this.pictureBox_rainbow.ClientSize.Height;
            int hgt2 = (int)(hgt / 2);
            for (int x = 0; x < wid; x++)
            {
                using (Pen the_pen = new Pen(MapRainbowColor(x, 0, wid)))
                {
                    e.Graphics.DrawLine(the_pen, x, 0, x, hgt2);
                }
                using (Pen the_pen = new Pen(MapRainbowColor(x, wid, 0)))
                {
                    e.Graphics.DrawLine(the_pen, x, hgt2, x, hgt);
                }
            }

        }


        // Map a value to a rainbow color.
        private Color MapRainbowColor(float value, float red_value, float blue_value)
        {
            // Convert into a value between 0 and 1023.
            int int_value = (int)(1023 * (value - red_value) / (blue_value - red_value));

            // Map different color bands.
            if (int_value < 256)
            {
                // Red to yellow. (255, 0, 0) to (255, 255, 0).
                return Color.FromArgb(255, int_value, 0);
            }
            else if (int_value < 512)
            {
                // Yellow to green. (255, 255, 0) to (0, 255, 0).
                int_value -= 256;
                return Color.FromArgb(255 - int_value, 255, 0);
            }
            else if (int_value < 768)
            {
                // Green to aqua. (0, 255, 0) to (0, 255, 255).
                int_value -= 512;
                return Color.FromArgb(0, 255, int_value);
            }
            else
            {
                // Aqua to blue. (0, 255, 255) to (0, 0, 255).
                int_value -= 768;
                return Color.FromArgb(0, 255 - int_value, 255);
            }
        }

        // 兩種 Color Wheel ST
        // Draw a color wheel in the indicated area.
        private void DrawColorWheel1(Graphics gr, Color outline_color, int xmin, int ymin, int wid, int hgt)
        {
            Rectangle rect = new Rectangle(xmin, ymin, wid, hgt);
            GraphicsPath wheel_path = new GraphicsPath();
            wheel_path.AddEllipse(rect);
            wheel_path.Flatten();

            int num_pts = (wheel_path.PointCount - 1) / 3;
            Color[] surround_colors = new Color[wheel_path.PointCount];
            float r = 255, g = 0, b = 0;
            float dr, dg, db;
            dr = -255 / num_pts;
            db = 255 / num_pts;
            for (int i = 0; i < num_pts; i++)
            {
                surround_colors[i] = Color.FromArgb(255, (int)r, (int)g, (int)b);
                r += dr;
                b += db;
            }

            r = 0; g = 0; b = 255;
            dg = 255 / num_pts;
            db = -255 / num_pts;
            for (int i = num_pts; i < 2 * num_pts; i++)
            {
                surround_colors[i] = Color.FromArgb(255, (int)r, (int)g, (int)b);
                g += dg;
                b += db;
            }

            r = 0; g = 255; b = 0;
            dr = 255 / (wheel_path.PointCount - 2 * num_pts);
            dg = -255 / (wheel_path.PointCount - 2 * num_pts);
            for (int i = 2 * num_pts; i < wheel_path.PointCount; i++)
            {
                surround_colors[i] = Color.FromArgb(255, (int)r, (int)g, (int)b);
                r += dr;
                g += dg;
            }

            using (PathGradientBrush path_brush = new PathGradientBrush(wheel_path))
            {
                path_brush.CenterColor = Color.White;
                path_brush.SurroundColors = surround_colors;

                gr.FillPath(path_brush, wheel_path);

                // It looks better if we outline the wheel.
                using (Pen thick_pen = new Pen(outline_color, 2))
                {
                    gr.DrawPath(thick_pen, wheel_path);
                }
            }

            //// Uncomment the following to draw the path's points.
            //for (int i = 0; i < wheel_path.PointCount; i++)
            //{
            //    gr.FillEllipse(Brushes.Black,
            //        wheel_path.PathPoints[i].X - 2,
            //        wheel_path.PathPoints[i].Y - 2,
            //        4, 4);
            //}
        }

        // Draw a color wheel.
        private void pictureBox_color_wheel1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            DrawColorWheel1(e.Graphics, this.pictureBox_color_wheel1.BackColor, 10, 10, this.pictureBox_color_wheel1.ClientSize.Width - 20, this.pictureBox_color_wheel1.ClientSize.Height - 20);
        }


        // Draw a color wheel in the indicated area.
        private void DrawColorWheel2(Graphics gr, Color outline_color,
            int xmin, int ymin, int wid, int hgt)
        {
            Rectangle rect = new Rectangle(xmin, ymin, wid, hgt);
            GraphicsPath wheel_path = new GraphicsPath();
            wheel_path.AddEllipse(rect);
            wheel_path.Flatten();

            float num_pts = (wheel_path.PointCount - 1) / 6;
            Color[] surround_colors = new Color[wheel_path.PointCount];

            int index = 0;
            InterpolateColors(surround_colors, ref index,
                1 * num_pts, 255, 255, 0, 0, 255, 255, 0, 255);
            InterpolateColors(surround_colors, ref index,
                2 * num_pts, 255, 255, 0, 255, 255, 0, 0, 255);
            InterpolateColors(surround_colors, ref index,
                3 * num_pts, 255, 0, 0, 255, 255, 0, 255, 255);
            InterpolateColors(surround_colors, ref index,
                4 * num_pts, 255, 0, 255, 255, 255, 0, 255, 0);
            InterpolateColors(surround_colors, ref index,
                5 * num_pts, 255, 0, 255, 0, 255, 255, 255, 0);
            InterpolateColors(surround_colors, ref index,
                wheel_path.PointCount, 255, 255, 255, 0, 255, 255, 0, 0);

            using (PathGradientBrush path_brush =
                new PathGradientBrush(wheel_path))
            {
                path_brush.CenterColor = Color.White;
                path_brush.SurroundColors = surround_colors;

                gr.FillPath(path_brush, wheel_path);

                // It looks better if we outline the wheel.
                using (Pen thick_pen = new Pen(outline_color, 2))
                {
                    gr.DrawPath(thick_pen, wheel_path);
                }
            }

            //// Uncomment the following to draw the path's points.
            //for (int i = 0; i < wheel_path.PointCount; i++)
            //{
            //    gr.FillEllipse(Brushes.Black,
            //        wheel_path.PathPoints[i].X - 2,
            //        wheel_path.PathPoints[i].Y - 2,
            //        4, 4);
            //}
        }

        // Fill in colors interpolating between the from and to values.
        private void InterpolateColors(Color[] surround_colors,
            ref int index, float stop_pt,
            int from_a, int from_r, int from_g, int from_b,
            int to_a, int to_r, int to_g, int to_b)
        {
            int num_pts = (int)stop_pt - index;
            float a = from_a, r = from_r, g = from_g, b = from_b;
            float da = (to_a - from_a) / (num_pts - 1);
            float dr = (to_r - from_r) / (num_pts - 1);
            float dg = (to_g - from_g) / (num_pts - 1);
            float db = (to_b - from_b) / (num_pts - 1);

            for (int i = 0; i < num_pts; i++)
            {
                surround_colors[index++] =
                    Color.FromArgb((int)a, (int)r, (int)g, (int)b);
                a += da;
                r += dr;
                g += dg;
                b += db;
            }
        }



        // Draw a color wheel.
        private void pictureBox_color_wheel2_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            DrawColorWheel2(e.Graphics, this.pictureBox_color_wheel2.BackColor, 10, 10, this.pictureBox_color_wheel2.ClientSize.Width - 20, this.pictureBox_color_wheel2.ClientSize.Height - 20);
        }

        // 兩種 Color Wheel SP

        //畫各種箭頭 ST

        // The end point style.
        private enum EndpointStyle
        {
            None,
            ArrowHead,
            Fletching
        }

        // Draw arrow heads or tails for the
        // segment from p1 to p2.
        private void DrawArrow(Graphics gr, Pen pen, PointF p1, PointF p2,
            float length, EndpointStyle style1, EndpointStyle style2)
        {
            // Draw the shaft.
            gr.DrawLine(pen, p1, p2);

            // Find the arrow shaft unit vector.
            float vx = p2.X - p1.X;
            float vy = p2.Y - p1.Y;
            float dist = (float)Math.Sqrt(vx * vx + vy * vy);
            vx /= dist;
            vy /= dist;

            // Draw the start.
            if (style1 == EndpointStyle.ArrowHead)
            {
                DrawArrowhead(gr, pen, p1, -vx, -vy, length);
            }
            else if (style1 == EndpointStyle.Fletching)
            {
                DrawArrowhead(gr, pen, p1, vx, vy, length);
            }

            // Draw the end.
            if (style2 == EndpointStyle.ArrowHead)
            {
                DrawArrowhead(gr, pen, p2, vx, vy, length);
            }
            else if (style2 == EndpointStyle.Fletching)
            {
                DrawArrowhead(gr, pen, p2, -vx, -vy, length);
            }
        }

        // Draw an arrowhead at the given point
        // in the normalized direction <nx, ny>.
        private void DrawArrowhead(Graphics gr, Pen pen,
            PointF p, float nx, float ny, float length)
        {
            float ax = length * (-ny - nx);
            float ay = length * (nx - ny);
            PointF[] points =
            {
                new PointF(p.X + ax, p.Y + ay),
                p,
                new PointF(p.X - ay, p.Y + ax)
            };
            gr.DrawLines(pen, points);
        }

        // Draw some arrows.
        private void pictureBox_arrow_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
            int x1 = 20;
            int x2 = 200;

            using (Pen thick_pen = new Pen(Color.Blue, 3))
            {
                int y = 20;
                DrawArrow(e.Graphics, thick_pen,
                    new PointF(x1, y), new PointF(x2, y), 10,
                    EndpointStyle.Fletching,
                    EndpointStyle.ArrowHead);
                y += 30;
                DrawArrow(e.Graphics, thick_pen,
                    new PointF(x1, y), new PointF(x2, y), 10,
                    EndpointStyle.ArrowHead,
                    EndpointStyle.ArrowHead);
                y += 30;
                DrawArrow(e.Graphics, thick_pen,
                    new PointF(x1, y), new PointF(x2, y), 10,
                    EndpointStyle.ArrowHead,
                    EndpointStyle.Fletching);
                y += 30;
                DrawArrow(e.Graphics, thick_pen,
                    new PointF(x1, y), new PointF(x2, y), 10,
                    EndpointStyle.Fletching,
                    EndpointStyle.Fletching);
            }
        }

        //畫各種箭頭 SP


        int hilbert_curve_depth = 2;
        int sierpinski_curve_depth = 2;


        private void timer_change_Tick(object sender, EventArgs e)
        {
            draw_hilbert_curve();
            hilbert_curve_depth++;
            if (hilbert_curve_depth > 6)
                hilbert_curve_depth = 2;

            draw_sierpinski_curve();
            sierpinski_curve_depth++;
            if (sierpinski_curve_depth > 6)
                sierpinski_curve_depth = 2;
        }

        #region Hilbert Curve
        private float LastX, LastY;
        private Bitmap HilbertImage;

        void draw_hilbert_curve()
        {
            Application.DoEvents();

            // Get the parameters.
            float total_length, start_x, start_y, start_length;

            // See how big we can make the curve.
            if (pictureBox_hilbert_curve.ClientSize.Height < pictureBox_hilbert_curve.ClientSize.Width)
            {
                total_length = (float)(0.9 * pictureBox_hilbert_curve.ClientSize.Height);
            }
            else
            {
                total_length = (float)(0.9 * pictureBox_hilbert_curve.ClientSize.Width);
            }

            start_x = (pictureBox_hilbert_curve.ClientSize.Width - total_length) / 2;
            start_y = (pictureBox_hilbert_curve.ClientSize.Height - total_length) / 2;

            // Compute the side length for this level.
            start_length = (float)(total_length / (Math.Pow(2, hilbert_curve_depth) - 1));

            HilbertImage = new Bitmap(pictureBox_hilbert_curve.ClientSize.Width, pictureBox_hilbert_curve.ClientSize.Height);
            pictureBox_hilbert_curve.Image = HilbertImage;

            using (Graphics gr = Graphics.FromImage(HilbertImage))
            {
                // Draw the curve.
                gr.Clear(pictureBox_hilbert_curve.BackColor);
                LastX = (int)start_x;
                LastY = (int)start_y;
                Hilbert(gr, hilbert_curve_depth, start_length, 0);
            }
        }

        // Draw a Hilbert curve.
        private void Hilbert(Graphics gr, int depth, float dx, float dy)
        {
            if (depth > 1) Hilbert(gr, depth - 1, dy, dx);
            DrawRelative(gr, dx, dy);
            if (depth > 1) Hilbert(gr, depth - 1, dx, dy);
            DrawRelative(gr, dy, dx);
            if (depth > 1) Hilbert(gr, depth - 1, dx, dy);
            DrawRelative(gr, -dx, -dy);
            if (depth > 1) Hilbert(gr, depth - 1, -dy, -dx);
        }

        // Draw the line (LastX, LastY)-(LastX + dx, LastY + dy) and
        // update LastX = LastX + dx, LastY = LastY + dy.
        private void DrawRelative(Graphics gr, float dx, float dy)
        {
            gr.DrawLine(Pens.Black, LastX, LastY, LastX + dx, LastY + dy);
            LastX = LastX + dx;
            LastY = LastY + dy;
        }

        #endregion Hilbert Curve



        #region Sierpinski Curve
        private Bitmap m_Bm;

        void draw_sierpinski_curve()
        {
            Application.DoEvents();

            // See if we should refresh as we draw.

            m_Bm = new Bitmap(pictureBox_sierpinski_curve.ClientSize.Width, pictureBox_sierpinski_curve.ClientSize.Height);
            pictureBox_sierpinski_curve.Image = m_Bm;

            using (Graphics gr = Graphics.FromImage(m_Bm))
            {
                // Draw the curve.
                gr.Clear(pictureBox_sierpinski_curve.BackColor);

                float dx = (float)(m_Bm.Width / Math.Pow(2, sierpinski_curve_depth - 1) / 8);
                float dy = (float)(m_Bm.Height / Math.Pow(2, sierpinski_curve_depth - 1) / 8);
                Sierpinski(gr, sierpinski_curve_depth, dx, dy);
            }

            // Display the result.
            pictureBox_sierpinski_curve.Refresh();
        }

        // Draw a Sierpinski curve.
        private void Sierpinski(Graphics gr, int depth, float dx, float dy)
        {
            float x = 2 * dx;
            float y = dy;

            SierpA(gr, depth, dx, dy, ref x, ref y);
            DrawRel(gr, ref x, ref y, dx, dy);
            SierpB(gr, depth, dx, dy, ref x, ref y);
            DrawRel(gr, ref x, ref y, -dx, dy);
            SierpC(gr, depth, dx, dy, ref x, ref y);
            DrawRel(gr, ref x, ref y, -dx, -dy);
            SierpD(gr, depth, dx, dy, ref x, ref y);
            DrawRel(gr, ref x, ref y, dx, -dy);

            pictureBox_sierpinski_curve.Refresh();
        }

        // Draw right across the top.
        private void SierpA(Graphics gr, float depth, float dx, float dy, ref float x, ref float y)
        {
            if (depth > 0)
            {
                depth--;

                SierpA(gr, depth, dx, dy, ref x, ref y);
                DrawRel(gr, ref x, ref y, dx, dy);
                SierpB(gr, depth, dx, dy, ref x, ref y);
                DrawRel(gr, ref x, ref y, 2 * dx, 0);
                SierpD(gr, depth, dx, dy, ref x, ref y);
                DrawRel(gr, ref x, ref y, dx, -dy);
                SierpA(gr, depth, dx, dy, ref x, ref y);
            }
        }

        // Draw down on the right.
        private void SierpB(Graphics gr, float depth, float dx, float dy, ref float x, ref float y)
        {
            if (depth > 0)
            {
                depth--;
                SierpB(gr, depth, dx, dy, ref x, ref y);
                DrawRel(gr, ref x, ref y, -dx, dy);
                SierpC(gr, depth, dx, dy, ref x, ref y);
                DrawRel(gr, ref x, ref y, 0, 2 * dy);
                SierpA(gr, depth, dx, dy, ref x, ref y);
                DrawRel(gr, ref x, ref y, dx, dy);
                SierpB(gr, depth, dx, dy, ref x, ref y);
            }
        }

        // Draw left across the bottom.
        private void SierpC(Graphics gr, float depth, float dx, float dy, ref float x, ref float y)
        {
            if (depth > 0)
            {
                depth--;
                SierpC(gr, depth, dx, dy, ref x, ref y);
                DrawRel(gr, ref x, ref y, -dx, -dy);
                SierpD(gr, depth, dx, dy, ref x, ref y);
                DrawRel(gr, ref x, ref y, -2 * dx, 0);
                SierpB(gr, depth, dx, dy, ref x, ref y);
                DrawRel(gr, ref x, ref y, -dx, dy);
                SierpC(gr, depth, dx, dy, ref x, ref y);
            }
        }

        // Draw up along the left.
        private void SierpD(Graphics gr, float depth, float dx, float dy, ref float x, ref float y)
        {
            if (depth > 0)
            {
                depth--;
                SierpD(gr, depth, dx, dy, ref x, ref y);
                DrawRel(gr, ref x, ref y, dx, -dy);
                SierpA(gr, depth, dx, dy, ref x, ref y);
                DrawRel(gr, ref x, ref y, 0, -2 * dy);
                SierpC(gr, depth, dx, dy, ref x, ref y);
                DrawRel(gr, ref x, ref y, -dx, -dy);
                SierpD(gr, depth, dx, dy, ref x, ref y);
            }
        }

        // Draw a line between (x, y) and (x + dx, y + dy).
        // Update x and y.
        private void DrawRel(Graphics gr, ref float x, ref float y, float dx, float dy)
        {
            gr.DrawLine(Pens.Black, x, y, x + dx, y + dy);
            x += dx;
            y += dy;
        }
        #endregion Sierpinski Curve


        // 畫動態派圖 ST        
        private void pictureBox_pie_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            PointF offset_3d = new PointF(0, 20);
            RectangleF rect = new RectangleF(40, 30,
                pictureBox_pie.ClientSize.Width - 80 - offset_3d.X,
                pictureBox_pie.ClientSize.Height - 60 - offset_3d.Y);

            // Set explode distances for slices 2 and 7.
            Slices[explode_pie1].ExplodeDistance = ExplodeDistance;
            Slices[explode_pie2].ExplodeDistance = ExplodeDistance;

            // Draw the pie slices in sorted order.
            foreach (Slice slice in Slices)
            {
                PieSlice3D(e.Graphics,
                    slice.TopBrush, slice.TopPen, slice.SideBrush,
                    offset_3d, slice.ExplodeDistance, rect,
                    slice.StartAngle, slice.SweepAngle);
            }
        }

        // Draw a 3-D pie slice.
        private void PieSlice3D(Graphics gr, Brush top_brush, Pen top_pen, Brush side_brush, PointF offset_3d, float explode_distance, RectangleF rect, float start_angle, float sweep_angle)
        {
            // Calculate the explode offset.
            double explode_angle = (start_angle + sweep_angle / 2f) * Math.PI / 180f;
            float dx = explode_distance * (float)Math.Cos(explode_angle);
            float dy = explode_distance * (float)Math.Sin(explode_angle);

            // Create the top of the side.
            RectangleF top_rect = new RectangleF(
                rect.X + dx, rect.Y + dy,
                rect.Width, rect.Height);
            GraphicsPath path = new GraphicsPath();
            path.AddPie(top_rect, start_angle, sweep_angle);

            // Create the bottom of the side.
            RectangleF bottom_rect = new RectangleF(
                top_rect.X + offset_3d.X,
                top_rect.Y + offset_3d.Y,
                rect.Width, rect.Height);
            path.AddPie(bottom_rect, start_angle, sweep_angle);

            // Convert the GraphicsPath into a list of points.
            path.Flatten();
            PointF[] path_points = path.PathPoints;
            List<PointF> points_list = new List<PointF>(path_points);

            // Make a convex hull.
            List<PointF> hull_points = Geometry.MakeConvexHull(points_list);

            // Fill the convex hull.
            gr.FillPolygon(side_brush, hull_points.ToArray());

            // Draw the top.
            gr.FillPie(top_brush, top_rect, start_angle, sweep_angle);
            gr.DrawPie(top_pen, top_rect, start_angle, sweep_angle);
        }

        // The distance we have exploded so far.
        private float ExplodeDistance = 0;

        // The maximum distance we will explode.
        private float MaxExplodeDistance = 30;

        // The change in explode distance per tick.
        private float DeltaExplodeDistance = 2;

        int wait_time = 0;
        // Continue exploding.
        private void timer_pie_Tick(object sender, EventArgs e)
        {
            if (wait_time == 0)
            {
                pictureBox_pie.Refresh();

                ExplodeDistance += DeltaExplodeDistance;
            }

            if (ExplodeDistance > MaxExplodeDistance)
            {
                wait_time++;
                if (wait_time > 100)
                {
                    wait_time = 0;
                    ExplodeDistance = 0;

                    pictureBox_pie.Refresh();

                    Random rand = new Random();

                    explode_pie1 = rand.Next(10);
                    explode_pie2 = rand.Next(10);

                    while (explode_pie2 == explode_pie1)
                    {
                        explode_pie2 = rand.Next(10);
                    }
                }
            }
        }

        // 畫動態派圖 SP



    }
}
