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

            //button
            x_st = 800;
            y_st = 10;
            dx = 140;
            dy = 55;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button2.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            button3.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button5.Location = new Point(x_st + dx * 2, y_st + dy * 1);

            button6.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button7.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button8.Location = new Point(x_st + dx * 2, y_st + dy * 2);

            button9.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button11.Location = new Point(x_st + dx * 2, y_st + dy * 3);

            button12.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button14.Location = new Point(x_st + dx * 2, y_st + dy * 4);

            button15.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button17.Location = new Point(x_st + dx * 2, y_st + dy * 5);

            button18.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 6);

            bt_save.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            bt_exit.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            richTextBox1.Size = new Size(richTextBox1.Size.Width, this.Height - richTextBox1.Location.Y - 25);

            x_st = 10;
            y_st = 10;
            dx = W + 10;
            dy = H + 10;

            pictureBox1.Size = new Size(W, H);
            pictureBox2.Size = new Size(W, H);
            pictureBox3.Size = new Size(W, H);
            pictureBox4.Size = new Size(W, H);
            pictureBox5.Size = new Size(W, H);
            pictureBox6.Size = new Size(W, H);
            pictureBox7.Size = new Size(W * 5 / 2, H);

            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox3.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            pictureBox4.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox5.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            pictureBox6.Location = new Point(x_st + dx * 2, y_st + dy * 1);

            pictureBox7.Location = new Point(x_st + dx * 0, y_st + dy * 2);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            ClientSize = new Size(button2.Right + 10, richTextBox1.Bottom + 10);    //自動表單邊界
        }

        private void button0_Click(object sender, EventArgs e)
        {
        }

        private void button1_Click(object sender, EventArgs e)
        {
        }

        private void button2_Click(object sender, EventArgs e)
        {
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        private void button10_Click(object sender, EventArgs e)
        {
        }

        private void button11_Click(object sender, EventArgs e)
        {
        }

        private void button12_Click(object sender, EventArgs e)
        {
        }

        private void button13_Click(object sender, EventArgs e)
        {
        }

        private void button14_Click(object sender, EventArgs e)
        {
        }

        private void button15_Click(object sender, EventArgs e)
        {
        }

        private void button16_Click(object sender, EventArgs e)
        {
        }

        private void button17_Click(object sender, EventArgs e)
        {
        }

        private void button18_Click(object sender, EventArgs e)
        {
        }

        private void button19_Click(object sender, EventArgs e)
        {
        }

        private void button20_Click(object sender, EventArgs e)
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

        // The image used for the graph.
        private Bitmap GraphImage;

        // Graph.
        private void btnGraph_Click(object sender, EventArgs e)
        {
            GraphImage = new Bitmap(
                pictureBox7.ClientSize.Width,
                pictureBox7.ClientSize.Height);
            using (Graphics gr = Graphics.FromImage(GraphImage))
            {
                gr.Clear(Color.White);
                gr.SmoothingMode = SmoothingMode.AntiAlias;

                using (Pen thin_pen = new Pen(Color.Purple, 0))
                {
                    // Get the bounds.
                    double xmin = double.Parse(txtXmin.Text) * Math.PI;
                    double xmax = double.Parse(txtXmax.Text) * Math.PI;
                    double ymin = double.Parse(txtYmin.Text);
                    double ymax = double.Parse(txtYmax.Text);

                    // Scale to make the area fit the PictureBox.
                    RectangleF world_coords = new RectangleF(
                        (float)xmin, (float)ymax,
                        (float)(xmax - xmin),
                        (float)(ymin - ymax));
                    PointF[] device_coords =
                    {
                        new PointF(0, 0),
                        new PointF(pictureBox7.ClientSize.Width, 0),
                        new PointF(0, pictureBox7.ClientSize.Height),
                    };
                    gr.Transform = new Matrix(world_coords, device_coords);

                    // Draw the X-axis.
                    // Start at the multiple of Pi < xmin.
                    double start_x = Math.PI * ((int)(xmin - 1));
                    gr.DrawLine(thin_pen, (float)xmin, 0, (float)xmax, 0);
                    float dy = (float)((ymax - ymin) / 30.0);
                    for (double x = start_x; x <= xmax; x += Math.PI)
                    {
                        gr.DrawLine(thin_pen, (float)x, -2 * dy, (float)x, 2 * dy);
                    }
                    for (double x = start_x + Math.PI / 2.0; x <= xmax; x += Math.PI)
                    {
                        gr.DrawLine(thin_pen, (float)x, -dy, (float)x, dy);
                    }

                    // Draw the Y-axis.
                    // Start at the multiple of 1 < ymin.
                    double start_y = (int)ymin - 1;
                    gr.DrawLine(thin_pen, 0, (float)ymin, 0, (float)ymax);
                    float dx = (float)((xmax - xmin) / 60.0);
                    for (double y = start_y; y <= ymax; y += 1.0)
                    {
                        gr.DrawLine(thin_pen, -2 * dx, (float)y, 2 * dx, (float)y);
                    }
                    for (double y = start_y + 0.5; y <= ymax; y += 1.0)
                    {
                        gr.DrawLine(thin_pen, -dx, (float)y, dx, (float)y);
                    }

                    // Draw vertical asymptotes.
                    thin_pen.DashPattern = new float[] { 5, 5 };
                    for (double x = start_x + Math.PI / 2.0; x <= xmax; x += Math.PI)
                    {
                        gr.DrawLine(thin_pen, (float)x, (float)ymin, (float)x, (float)ymax);
                    }

                    // Draw horizontal limits for sine and cosine.
                    gr.DrawLine(thin_pen, (float)xmin, 1, (float)xmax, 1);
                    gr.DrawLine(thin_pen, (float)xmin, -1, (float)xmax, -1);
                    thin_pen.DashStyle = DashStyle.Solid;

                    // See how big a pixel is before scaling.
                    Matrix inverse = gr.Transform;
                    inverse.Invert();
                    PointF[] pixel_pts =
                    {
                        new PointF(0, 0),
                        new PointF(1, 0),
                    };
                    inverse.TransformPoints(pixel_pts);
                    dx = pixel_pts[1].X - pixel_pts[0].X;

                    // Sine.
                    List<PointF> sine_points = new List<PointF>();
                    for (float x = (float)xmin; x <= xmax; x += dx)
                    {
                        sine_points.Add(new PointF(x, (float)Math.Sin(x)));
                    }
                    thin_pen.Color = Color.Red;
                    gr.DrawLines(thin_pen, sine_points.ToArray());

                    // Cosine.
                    List<PointF> cosine_points = new List<PointF>();
                    for (float x = (float)xmin; x <= xmax; x += dx)
                    {
                        cosine_points.Add(new PointF(x, (float)Math.Cos(x)));
                    }
                    thin_pen.Color = Color.Green;
                    gr.DrawLines(thin_pen, cosine_points.ToArray());

                    // Tangent.
                    List<PointF> tangent_points = new List<PointF>();
                    double old_value = Math.Tan(xmin);
                    thin_pen.Color = Color.Blue;
                    for (float x = (float)xmin; x <= xmax; x += dx)
                    {
                        // See if we're at a discontinuity.
                        double new_value = Math.Tan(x);
                        if ((Math.Abs(new_value - old_value) > 10) &&
                            (Math.Sign(new_value) != Math.Sign(old_value)))
                        {
                            if (tangent_points.Count > 1)
                                gr.DrawLines(thin_pen, tangent_points.ToArray());
                            tangent_points = new List<PointF>();
                        }
                        else
                        {
                            tangent_points.Add(new PointF(x, (float)Math.Tan(x)));
                        }
                    }
                    if (tangent_points.Count > 1)
                        gr.DrawLines(thin_pen, tangent_points.ToArray());
                }
            }

            // Display the result.
            pictureBox7.Image = GraphImage;


        }

        // Draw an arrow normally and rotated around a point.
        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the basic arrow.
            DrawArrow(Pens.Blue, e.Graphics);

            // Draw the point of rotation.
            Point center = new Point(50, 70);
            e.Graphics.FillEllipse(Brushes.Red, center.X - 3, center.Y - 3, 6, 6);

            // Rotate 30 degrees around the point.
            e.Graphics.Transform = RotateAroundPoint(30, center);

            // Draw the arrow rotated.
            DrawArrow(Pens.Green, e.Graphics);
        }

        // Draw an arrow.
        private void DrawArrow(Pen pen, Graphics gr)
        {
            Point[] pts = 
            {
                new Point( 50,  50),
                new Point(150,  50),
                new Point(150,  20),
                new Point(200,  70),
                new Point(150, 120),
                new Point(150,  90),
                new Point( 50,  90)
            };
            gr.DrawPolygon(pen, pts);
        }

        // Return a rotation matrix to rotate around a point.
        private Matrix RotateAroundPoint(float angle, Point center)
        {
            // Translate the point to the origin.
            Matrix result = new Matrix();
            result.RotateAt(angle, center);
            return result;
        }

        private void pictureBox4_Paint(object sender, PaintEventArgs e)
        {

        }


    }
}
