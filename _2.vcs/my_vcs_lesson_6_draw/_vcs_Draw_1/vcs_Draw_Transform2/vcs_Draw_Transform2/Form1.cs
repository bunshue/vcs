using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;
using System.Drawing.Drawing2D; //SmoothingMode, Matrix

//平移縮放旋轉

namespace vcs_Draw_Transform2
{
    public partial class Form1 : Form
    {
        Bitmap bitmap1;
        Graphics g;
        SolidBrush sb1 = new SolidBrush(Color.Red);
        SolidBrush sb2 = new SolidBrush(Color.Green);
        SolidBrush sb3 = new SolidBrush(Color.Blue);

        //string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6_draw\data\tiger.jpg";  // 100 X 100
        //string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6_draw\data\smile.jpg";  // 200 X 200
        //string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6_draw\data\peony.bmp";  // 200 X 200

        //string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
        string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6_draw\data\volkswagen.png";
        Bitmap bmp;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            reset_pictureBox();

            bmp = new Bitmap(filename);
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 10;
            dy = 60 + 5;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            pictureBox1.Size = new Size(820, 880);
            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt_reset.Location = new Point(pictureBox1.Location.X + pictureBox1.Size.Width - bt_reset.Size.Width, pictureBox1.Location.Y);

            richTextBox1.Size = new Size(300, 880);
            richTextBox1.Location = new Point(x_st + dx * 6, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1600, 940);
            this.Text = "vcs_Draw_Transform2";

            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((1920 - this.Size.Width) / 2, (1080 - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_reset_Click(object sender, EventArgs e)
        {
            reset_pictureBox();
        }

        void reset_pictureBox()
        {
            pictureBox1.Size = new Size(820, 880);
            bitmap1 = new Bitmap(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height);
            g = Graphics.FromImage(bitmap1);
            g.ResetTransform();  // 重置轉換, 恢復
            g.SmoothingMode = SmoothingMode.AntiAlias;
            g.Clear(Color.White);
            draw_grid(g);
            pictureBox1.Image = bitmap1;
        }

        int angle = 0;
        private void button0_Click(object sender, EventArgs e)
        {
            reset_pictureBox();

            //旋轉
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            angle += 30;
            Bitmap bitmap1 = new Bitmap(filename);
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            Bitmap bitmap2 = new Bitmap(W, H);

            Graphics g = Graphics.FromImage(bitmap2);

            Matrix mx = new Matrix();
            //mx.Rotate(30);//以左上角為圓心順時鐘旋轉角度
            mx.RotateAt(angle, new PointF(W / 2, H / 2));//以(cx,cy)為圓心順時鐘旋轉角度
            g.Transform = mx;

            g.DrawImage(bitmap1, new Rectangle(0, 0, W, H));

            g.Dispose();

            pictureBox1.Image = bitmap2;
        }

        //畫Sinc ST
        private void button1_Click(object sender, EventArgs e)
        {
            reset_pictureBox();

            //畫Sinc
            MakeGraph();
        }
        // Make the graph.
        private void MakeGraph()
        {
            g.SmoothingMode = SmoothingMode.AntiAlias;

            // Transform to map the graph bounds to the Bitmap.
            // The bounds to draw.
            float xmin = -20;
            float xmax = 20;
            float ymin = -5;
            float ymax = 12;
            RectangleF rect = new RectangleF(xmin, ymin, xmax - xmin, ymax - ymin);

            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;
            PointF[] pts = 
            {
                new PointF(0, H),
                new PointF(W, H),
                new PointF(0, 0),
            };
            g.Transform = new Matrix(rect, pts);

            // Draw the graph.
            Pen p = new Pen(Color.Blue, 0);
            // Draw the axes.
            g.DrawLine(p, xmin, 0, xmax, 0);
            g.DrawLine(p, 0, ymin, 0, ymax);
            for (int x = (int)xmin; x <= xmax; x++)
            {
                g.DrawLine(p, x, -0.1f, x, 0.1f);
            }
            for (int y = (int)ymin; y <= ymax; y++)
            {
                g.DrawLine(p, -0.1f, y, 0.1f, y);
            }
            p.Color = Color.Red;

            // See how big 1 pixel is horizontally.
            Matrix inverse = g.Transform;
            inverse.Invert();
            PointF[] pixel_pts =
            {
                new PointF(0, 0),
                new PointF(1, 0)
            };
            inverse.TransformPoints(pixel_pts);
            float dx = pixel_pts[1].X - pixel_pts[0].X;
            dx /= 2;

            // Loop over x values to generate points.
            List<PointF> points = new List<PointF>();
            for (float x = xmin; x <= xmax; x += dx)
            {
                bool valid_point = false;
                try
                {
                    // Get the next point.
                    float y = F(x);

                    // If the slope is reasonable, this is a valid point.
                    if (points.Count == 0)
                    {
                        valid_point = true;
                    }
                    else
                    {
                        float dy = y - points[points.Count - 1].Y;
                        if (Math.Abs(dy / dx) < 1000)
                        {
                            valid_point = true;
                        }
                    }
                    if (valid_point)
                    {
                        points.Add(new PointF(x, y));
                    }
                }
                catch
                {
                }

                // If the new point is invalid, draw
                // the points in the latest batch.
                if (!valid_point)
                {
                    if (points.Count > 1)
                    {
                        g.DrawLines(p, points.ToArray());
                    }
                    points.Clear();
                }
            }

            // Draw the last batch of points.
            if (points.Count > 1)
            {
                g.DrawLines(p, points.ToArray());
            }

            pictureBox1.Image = bitmap1;
        }

        // The function to graph.
        private float F(float x)
        {
            //return (float)((1 / x + 1 / (x + 1) - 2 * x * x) / 10);
            //return x;
            //return (float)Math.Sin(x);
            return (float)(10 * Math.Sin(x) / x);
        }
        //畫Sinc SP

        private void button2_Click(object sender, EventArgs e)
        {
            reset_pictureBox();
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
            //Matrix 測試
            //矩陣的定義
            Matrix myMatrix1 = new Matrix();  // 第一種方式
            Matrix myMatrix2 = new Matrix(1, 2, 4, 5, 7, 8); // 第二種方式

            float m11 = myMatrix2.Elements[0];
            float m12 = myMatrix2.Elements[1];
            float m21 = myMatrix2.Elements[2];
            float m22 = myMatrix2.Elements[3];
            float dx = myMatrix2.Elements[4];
            float dy = myMatrix2.Elements[5];

            float dx2 = myMatrix2.OffsetX;
            float dy2 = myMatrix2.OffsetY;


            Rectangle rect = new Rectangle(0, 0, 100, 100);
            Point[] pt = new Point[3] { new Point(0, 0), new Point(100, 0), new Point(0, 100) };
            Matrix myMatrix3 = new Matrix(rect, pt); // 第三種方式

            RectangleF rect2 = new Rectangle(0, 0, 100, 100);
            PointF[] pt2 = new PointF[3] { new PointF(0, 0), new PointF(100, 0), new PointF(0, 100) };
            Matrix myMatrix4 = new Matrix(rect2, pt2); // 第四種方式

            //e.Graphics.Transform = myMatrix1;

            //矩陣的相乘的順序
            Matrix A = new Matrix(0, 1, -1, 0, 0, 0);
            Matrix B = new Matrix(1, 0, 0, 1, 1, 0);

            A.Multiply(B);  // A = B x A
            //A.Multiply(B, MatrixOrder.Prepend); // A = B x A
            //A.Multiply(B, MatrixOrder.Append);  // A = A x B




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

        void draw_grid(Graphics g)
        {
            int W = this.pictureBox1.Width;
            int H = this.pictureBox1.Height;
            int i;
            int j;

            for (i = 0; i <= W; i += 100)
            {
                g.DrawLine(Pens.Gray, i, 0, i, H);
            }
            for (j = 0; j <= H; j += 100)
            {
                g.DrawLine(Pens.Gray, 0, j, W, j);
            }
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            pictureBox1.Invalidate();
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



