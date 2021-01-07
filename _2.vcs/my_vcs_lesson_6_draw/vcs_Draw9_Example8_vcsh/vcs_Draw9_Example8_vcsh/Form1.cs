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

            //最大化螢幕
            //this.FormBorderStyle = FormBorderStyle.None;
            //this.WindowState = FormWindowState.Maximized;
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
            dx = W + 30;
            dy = H + 30;

            pictureBox1.Size = new Size(W, H);
            pictureBox2.Size = new Size(W, H);
            pictureBox3.Size = new Size(W, H);
            pictureBox4.Size = new Size(W, H - 40);
            pictureBox5.Size = new Size(W, H);
            pictureBox_histogram.Size = new Size(W, H);
            pictureBox_age.Size = new Size(W, H);
            pictureBox8.Size = new Size(W * 2 + 10, H);
            pictureBox10.Size = new Size(W, H * 9 / 10);
            pictureBox11.Size = new Size(W, H);
            pictureBox12.Size = new Size(W, H);
            pictureBox13.Size = new Size(W, H);
            pictureBox14.Size = new Size(W, H);
            pictureBox15.Size = new Size(W, H);

            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox3.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox4.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            checkBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0 + H - 30);
            pictureBox5.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            pictureBox_histogram.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox_age.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            pictureBox8.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            pictureBox10.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            pictureBox11.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            pictureBox12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            pictureBox13.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            pictureBox14.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            pictureBox15.Location = new Point(x_st + dx * 4, y_st + dy * 2);

            bt_save.Location = new Point(x_st + dx * 5+150, y_st + dy * 0);
            bt_exit.Location = new Point(x_st + dx * 5+300, y_st + dy * 0);
            richTextBox1.Location = new Point(x_st + dx * 5, y_st + dy * 0 + 50);

            richTextBox1.Size = new Size(bt_exit.Right - richTextBox1.Location.X, this.Height - richTextBox1.Location.Y - 25);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            ClientSize = new Size(bt_exit.Right + 10, richTextBox1.Bottom + 80);    //自動表單邊界
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
            e.Graphics.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;

            using (Font the_font = new Font("Comic Sans MS", 20))
            {

                int x_st = 10;
                int y_st = 220;
                int dx;

                dx = 40;
                DrawRotatedTextAt(e.Graphics, -90, "January", x_st, y_st, the_font, Brushes.Red);
                x_st += dx;
                DrawRotatedTextAt(e.Graphics, -90, "February", x_st, y_st, the_font, Brushes.Red);
                x_st += dx;
                DrawRotatedTextAt(e.Graphics, -90, "March", x_st, y_st, the_font, Brushes.Red);
                x_st += dx;
                DrawRotatedTextAt(e.Graphics, -90, "April", x_st, y_st, the_font, Brushes.Red);
                x_st += dx;
                DrawRotatedTextAt(e.Graphics, -90, "May", x_st, y_st, the_font, Brushes.Red);
                x_st += dx;
                DrawRotatedTextAt(e.Graphics, -90, "June", x_st, y_st, the_font, Brushes.Red);
                x_st += dx;
                DrawRotatedTextAt(e.Graphics, -90, "July", x_st, y_st, the_font, Brushes.Red);
                x_st += dx;
                DrawRotatedTextAt(e.Graphics, -90, "August", x_st, y_st, the_font, Brushes.Red);
                x_st += dx;
                DrawRotatedTextAt(e.Graphics, -90, "September", x_st, y_st, the_font, Brushes.Red);
                x_st += dx;
                DrawRotatedTextAt(e.Graphics, -90, "October", x_st, y_st, the_font, Brushes.Red);
                x_st += dx;
                DrawRotatedTextAt(e.Graphics, -90, "November", x_st, y_st, the_font, Brushes.Red);
                x_st += dx;
                DrawRotatedTextAt(e.Graphics, -90, "December", x_st, y_st, the_font, Brushes.Red);
            }

        }

        // Draw a rotated string at a particular position.
        private void DrawRotatedTextAt(Graphics gr, float angle, string txt, int x, int y, Font the_font, Brush the_brush)
        {
            // Save the graphics state.
            GraphicsState state = gr.Save();
            gr.ResetTransform();

            // Rotate.
            gr.RotateTransform(angle);

            // Translate to desired position. Be sure to append
            // the rotation so it occurs after the rotation.
            gr.TranslateTransform(x, y, MatrixOrder.Append);

            // Draw the text at the origin.
            gr.DrawString(txt, the_font, the_brush, 0, 0);

            // Restore the graphics state.
            gr.Restore(state);
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




    }
}
