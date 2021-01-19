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
                DataValues[i] = rnd.Next(MIN_VALUE + 5, MAX_VALUE - 5);

            //pictureBox4 的中心
            CenterPoint = new PointF(
                this.pictureBox4.ClientSize.Width / 2,
                this.pictureBox4.ClientSize.Height / 2);

            draw_random_pixel_image();
            draw_random_circles();          //pictureBox13
            draw_Apollonian_Gasket();       //pictureBox14
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

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
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
            pictureBox8.Size = new Size(W, H);
            pictureBox9.Size = new Size(W, H);
            pictureBox10.Size = new Size(W, H * 9 / 10);
            pictureBox_random_pixel_image.Size = new Size(W, H);
            pictureBox12.Size = new Size(W, H);
            pictureBox13.Size = new Size(W, H);
            pictureBox14.Size = new Size(W, H);
            pictureBox15.Size = new Size(W, H);
            pictureBox16.Size = new Size(W, H);
            pictureBox17.Size = new Size(W, H);
            pictureBox18.Size = new Size(W, H);
            pictureBox19.Size = new Size(W, H);
            pictureBox20.Size = new Size(W, H);
            pictureBox21.Size = new Size(W, H);
            pictureBox22.Size = new Size(W, H);
            pictureBox23.Size = new Size(W, H);
            pictureBox_rainbow.Size = new Size(W, H * 2 / 3);

            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox3.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox4.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            checkBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0 + H - 30);
            pictureBox5.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            pictureBox_histogram.Location = new Point(x_st + dx * 5, y_st + dy * 0);

            pictureBox_age.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox8.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            pictureBox9.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            pictureBox10.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            pictureBox_random_pixel_image.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            pictureBox12.Location = new Point(x_st + dx * 5, y_st + dy * 1);

            pictureBox13.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            pictureBox14.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            groupBox1.Location = new Point(x_st + dx * 1 + 10, y_st + dy * 3 - 30);
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
            pictureBox23.Location = new Point(x_st + dx * 4, y_st + dy * 3);
            pictureBox_rainbow.Location = new Point(x_st + dx * 5, y_st + dy * 3);
            groupBox2.Location = new Point(x_st + dx * 5, y_st + dy * 3 + 180);

            bt_save.Location = new Point(x_st + dx * 6, y_st + dy * 0);
            bt_exit.Location = new Point(x_st + dx * 6 + 120, y_st + dy * 0);
            richTextBox1.Location = new Point(x_st + dx * 6, y_st + dy * 0 + 50);

            richTextBox1.Size = new Size(bt_exit.Right - richTextBox1.Location.X, this.Height - richTextBox1.Location.Y - 25);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //ClientSize = new Size(bt_exit.Right + 10, richTextBox1.Bottom + 80);    //自動表單邊界
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

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
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

        private void pictureBox8_Paint(object sender, PaintEventArgs e)
        {

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
                    bmp.SetPixel(x, y, Color.FromArgb(a, r, g, b));
                }
            }

            //load bmp in pictureBox_random_pixel_image
            pictureBox_random_pixel_image.Image = bmp;
        }

        void draw_random_circles()
        {
            Bitmap bm = new Bitmap(pictureBox13.ClientSize.Width, pictureBox13.ClientSize.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.Clear(Color.Silver);

                Random rnd = new Random();
                int max_r = Math.Min(pictureBox13.ClientRectangle.Width, pictureBox13.ClientRectangle.Height) / 3;
                int min_r = max_r / 4;
                for (int i = 0; i < 15; i++)
                {
                    int r = rnd.Next(min_r, max_r);
                    int x = rnd.Next(min_r, pictureBox13.ClientRectangle.Width - min_r);
                    int y = rnd.Next(min_r, pictureBox13.ClientRectangle.Height - min_r);
                    gr.DrawEllipse(Pens.Black, x - r, y - r, 2 * r, 2 * r);
                }
            }
            pictureBox13.Image = bm;
        }

        // Apollonian Gasket ST
        void draw_Apollonian_Gasket()
        {
            int width = Math.Min(pictureBox14.ClientSize.Width, pictureBox14.ClientSize.Height);
            pictureBox14.Image = FindApollonianPacking(width);
        }

        // Find the Apollonian packing.
        private Bitmap FindApollonianPacking(int width)
        {
            Bitmap bm = new Bitmap(width, width);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.SmoothingMode = SmoothingMode.AntiAlias;
                if (rb1.Checked == true)
                    gr.Clear(Color.LightGreen);
                else
                    gr.Clear(Color.Black);

                // Create the three central tangent circles.
                float radius = width * 0.225f;
                float x = width / 2;
                float gasket_height = 2 * (float)(radius + 2 * radius / Math.Sqrt(3));
                float y = (width - gasket_height) / 2 + radius;
                Circle circle0 = new Circle(x, y, radius);

                // Draw a box around the gasket. (For debugging.)
                //gr.DrawRectangle(Pens.Orange,
                //    x - gasket_height / 2,
                //    y - radius,
                //    gasket_height,
                //    gasket_height);

                x -= radius;
                y += (float)(radius * Math.Sqrt(3));
                Circle circle1 = new Circle(x, y, radius);
                x += 2 * radius;
                Circle circle2 = new Circle(x, y, radius);

                if (rb1.Checked == true)
                {
                    // Draw the three central circles.
                    circle0.Draw(gr, Pens.Blue);
                    circle1.Draw(gr, Pens.Blue);
                    circle2.Draw(gr, Pens.Blue);
                }

                // Find the circle that contains them all.
                Circle big_circle = FindApollonianCircle(circle0, circle1, circle2, -1, -1, -1);
                if (rb1.Checked == true)
                {
                    big_circle.Draw(gr, Pens.Blue);
                }
                else
                {
                    // Draw the big circle.
                    using (Brush the_brush = new SolidBrush(RandomColor()))
                    {
                        big_circle.Draw(gr, the_brush);
                    }

                    // Draw the three central circles.
                    using (Brush the_brush = new SolidBrush(RandomColor()))
                    {
                        circle0.Draw(gr, the_brush);
                    }
                    using (Brush the_brush = new SolidBrush(RandomColor()))
                    {
                        circle1.Draw(gr, the_brush);
                    }
                    using (Brush the_brush = new SolidBrush(RandomColor()))
                    {
                        circle2.Draw(gr, the_brush);
                    }
                }

                // Set level to smaller values such as 3 to see partially drawn gaskets.
                int level = 10000;

                // Find the central circle.
                FindCircleOutsideAll(level, gr, circle0, circle1, circle2);

                // Find circles tangent to the big circle.
                FindCircleOutsideTwo(level, gr, circle0, circle1, big_circle);
                FindCircleOutsideTwo(level, gr, circle1, circle2, big_circle);
                FindCircleOutsideTwo(level, gr, circle2, circle0, big_circle);
            }
            return bm;
        }

        // Draw a circle tangent to these three circles and that is outside all three.
        private void FindCircleOutsideAll(int level, Graphics gr, Circle circle0, Circle circle1, Circle circle2)
        {
            Circle new_circle = FindApollonianCircle(circle0, circle1, circle2, 1, 1, 1);
            if (new_circle == null) return;
            if (new_circle.Radius < 0.1) return;

            if (rb1.Checked == true)
            {
                new_circle.Draw(gr, Pens.Blue);
            }
            else
            {
                using (Brush the_brush = new SolidBrush(RandomColor()))
                {
                    new_circle.Draw(gr, the_brush);
                }
            }

            if (--level > 0)
            {
                FindCircleOutsideAll(level, gr, circle0, circle1, new_circle);
                FindCircleOutsideAll(level, gr, circle0, circle2, new_circle);
                FindCircleOutsideAll(level, gr, circle1, circle2, new_circle);
            }
        }

        // Draw a circle tangent to these three circles and that is outside two of them.
        private void FindCircleOutsideTwo(int level, Graphics gr, Circle circle0, Circle circle1, Circle circle_contains)
        {
            Circle new_circle = FindApollonianCircle(circle0, circle1, circle_contains, 1, 1, -1);
            if (new_circle == null) return;
            if (new_circle.Radius < 0.1) return;

            if (rb1.Checked == true)
            {
                new_circle.Draw(gr, Pens.Blue);
            }
            else
            {
                using (Brush the_brush = new SolidBrush(RandomColor()))
                {
                    new_circle.Draw(gr, the_brush);
                }
            }

            if (--level > 0)
            {
                FindCircleOutsideTwo(level, gr, new_circle, circle0, circle_contains);
                FindCircleOutsideTwo(level, gr, new_circle, circle1, circle_contains);
                FindCircleOutsideAll(level, gr, circle0, circle1, new_circle);
            }
        }

        // Find the circles that touch each of the three input circles.
        private Circle[] FindApollonianCircles(Circle[] given_circles)
        {
            // Make a list for results.
            List<Circle> solution_circles = new List<Circle>();

            // Loop over all of the signs.
            foreach (int s0 in new int[] { -1, 1 })
            {
                foreach (int s1 in new int[] { -1, 1 })
                {
                    foreach (int s2 in new int[] { -1, 1 })
                    {
                        Circle new_circle = FindApollonianCircle(
                            given_circles[0], given_circles[1], given_circles[2],
                            s0, s1, s2);
                        if (new_circle != null) solution_circles.Add(new_circle);
                    }
                }
            }

            // Return the results.
            return solution_circles.ToArray();
        }

        // Find a solution to Apollonius' problem.
        // For discussion and method, see:
        //    http://mathworld.wolfram.com/ApolloniusProblem.html
        //    http://en.wikipedia.org/wiki/Problem_of_Apollonius#Algebraic_solutions
        // For most of a Java code implementation, see:
        //    http://www.diku.dk/hjemmesider/ansatte/rfonseca/implementations/apollonius.html
        private Circle FindApollonianCircle(Circle c1, Circle c2, Circle c3, int s1, int s2, int s3)
        {
            // Make sure c2 doesn't have the same X or Y coordinate as the others.
            const float tiny = 0.0001f;
            if ((Math.Abs(c2.Center.X - c1.Center.X) < tiny) ||
                (Math.Abs(c2.Center.Y - c1.Center.Y) < tiny))
            {
                Circle temp_circle = c2;
                c2 = c3;
                c3 = temp_circle;
                int temp_s = s2;
                s2 = s3;
                s3 = temp_s;
            }
            if ((Math.Abs(c2.Center.X - c3.Center.X) < tiny) ||
                (Math.Abs(c2.Center.Y - c3.Center.Y) < tiny))
            {
                Circle temp_circle = c2;
                c2 = c1;
                c1 = temp_circle;
                int temp_s = s2;
                s2 = s1;
                s1 = temp_s;
            }

            Debug.Assert(
                (c2.Center.X != c1.Center.X) && (c2.Center.Y != c1.Center.Y) &&
                (c2.Center.X != c3.Center.X) && (c2.Center.Y != c3.Center.Y),
                "Cannot find points without matching coordinates.");

            float x1 = c1.Center.X;
            float y1 = c1.Center.Y;
            float r1 = c1.Radius;
            float x2 = c2.Center.X;
            float y2 = c2.Center.Y;
            float r2 = c2.Radius;
            float x3 = c3.Center.X;
            float y3 = c3.Center.Y;
            float r3 = c3.Radius;

            float v11 = 2 * x2 - 2 * x1;
            float v12 = 2 * y2 - 2 * y1;
            float v13 = x1 * x1 - x2 * x2 + y1 * y1 - y2 * y2 - r1 * r1 + r2 * r2;
            float v14 = 2 * s2 * r2 - 2 * s1 * r1;

            float v21 = 2 * x3 - 2 * x2;
            float v22 = 2 * y3 - 2 * y2;
            float v23 = x2 * x2 - x3 * x3 + y2 * y2 - y3 * y3 - r2 * r2 + r3 * r3;
            float v24 = 2 * s3 * r3 - 2 * s2 * r2;

            float w12 = v12 / v11;
            float w13 = v13 / v11;
            float w14 = v14 / v11;

            float w22 = v22 / v21 - w12;
            float w23 = v23 / v21 - w13;
            float w24 = v24 / v21 - w14;

            float P = -w23 / w22;
            float Q = w24 / w22;
            float M = -w12 * P - w13;
            float N = w14 - w12 * Q;

            float a = N * N + Q * Q - 1;
            float b = 2 * M * N - 2 * N * x1 + 2 * P * Q - 2 * Q * y1 + 2 * s1 * r1;
            float c = x1 * x1 + M * M - 2 * M * x1 + P * P + y1 * y1 - 2 * P * y1 - r1 * r1;

            // Find roots of a quadratic equation
            double[] solutions = QuadraticSolutions(a, b, c);
            if (solutions.Length < 1) return null;
            float rs = (float)solutions[0];
            float xs = M + N * rs;
            float ys = P + Q * rs;

            Debug.Assert(!float.IsNaN(rs) && !float.IsNaN(xs) && !float.IsNaN(ys),
                "Error finding Apollonian circle.");

            if (rb1.Checked == false)
            {
                if (float.IsInfinity(xs) || float.IsInfinity(ys) || float.IsInfinity(rs)) return null;
            }
            if ((Math.Abs(xs) < tiny) || (Math.Abs(ys) < tiny) || (Math.Abs(rs) < tiny)) return null;
            return new Circle(xs, ys, rs);
        }

        // Return solutions to a quadratic equation.
        private double[] QuadraticSolutions(double a, double b, double c)
        {
            const double tiny = 0.000001;
            double discriminant = b * b - 4 * a * c;

            // See if there are no real solutions.
            if (discriminant < 0)
            {
                return new double[] { };
            }

            // See if there is one solution.
            if (discriminant < tiny)
            {
                return new double[] { -b / (2 * a) };
            }

            // There are two solutions.
            return new double[]
            {
                (-b + Math.Sqrt(discriminant)) / (2 * a),
                (-b - Math.Sqrt(discriminant)) / (2 * a),
            };
        }

        // Return a random color.
        private Random rand = new Random();
        private Color[] Colors =
        {
            Color.Red,
            Color.Green,
            Color.Blue,
            Color.Lime,
            Color.Orange,
            Color.Fuchsia,
            Color.Yellow,
            Color.LightGreen,
            Color.LightBlue,
            Color.Cyan,
        };

        private Color RandomColor()
        {
            return Colors[rand.Next(0, Colors.Length)];
        }

        // Apollonian Gasket SP

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
            draw_random_circles();          //pictureBox13
            draw_Apollonian_Gasket();       //pictureBox14
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

        
        // 畫星形 ST
        private void pictureBox22_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            PointF[] pts = StarPoints(5, this.pictureBox22.ClientRectangle);
            e.Graphics.DrawPolygon(Pens.Blue, pts);
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
            nudSkip.Maximum = (int)(((int)nudPoints.Value - 1) / 2.0);
            pictureBox23.Refresh();
        }
        private void nudSkip_ValueChanged(object sender, EventArgs e)
        {
            pictureBox23.Refresh();
        }

        // Draw the star.
        private void pictureBox23_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the star.
            DrawStar(e.Graphics, Pens.Red, Brushes.Yellow,
                (int)nudPoints.Value, (int)nudSkip.Value, pictureBox23.ClientRectangle);
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


    }
}
