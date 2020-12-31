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

// Add a reference to PresentationCore.     //要用.NET Framework4及加入參考PresentationCore
using System.Windows.Media.Media3D;

namespace vcs_Draw9_Example6_vcsh_math
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
            // Reduce flicker.
            DoubleBuffered = true;

            show_item_location();

            MakeData(F1);
            DrawLevelCurves(pictureBox1);

            MakeData(F2);
            DrawLevelCurves(pictureBox2);

            MakeData(F3);
            DrawLevelCurves(pictureBox3);

            MakeData(F4);
            DrawLevelCurves(pictureBox4);

            DrawHeart();
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

            bt_save.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_exit.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 1);

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
            pictureBox7.Size = new Size(W, H);
            pictureBox8.Size = new Size(W, H);
            pictureBox9.Size = new Size(W, H);

            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox3.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            pictureBox4.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox5.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            pictureBox6.Location = new Point(x_st + dx * 2, y_st + dy * 1);

            pictureBox7.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            pictureBox8.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            pictureBox9.Location = new Point(x_st + dx * 2, y_st + dy * 2);

            richTextBox1.Size = new Size(bt_exit.Right - richTextBox1.Location.X, this.Height - richTextBox1.Location.Y - 25);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            ClientSize = new Size(bt_exit.Right + 10, richTextBox1.Bottom + 10);    //自動表單邊界
        }


        #region 畫前四圖曲線
        //for pictureBox1~4
        //1. Bowl: z = x^2 + (y*2)^2 - 200
        //2. Monkey saddle: x * (x^2 - 3 * y^2)
        //3. Crossed trough: x^2 * y^2 - 30000
        //4. Hemisphere: Sqrt(400 - (x^2 + y^2))

        // The function delegate.
        private delegate double FofXY2(double x, double y);

        // The data.
        private const int Xmax = 10;
        private Point3D[,] Values;
        private double Zmin = double.MaxValue;
        private double Zmax = double.MinValue;

        // Make the data.
        private void MakeData(FofXY2 func)
        {
            // Make data.
            Values = new Point3D[2 * Xmax + 1, 2 * Xmax + 1];

            Zmin = double.MaxValue;
            Zmax = double.MinValue;
            for (int x = -Xmax; x <= Xmax; x++)
            {
                for (int y = -Xmax; y <= Xmax; y++)
                {
                    double z = func(x, y);

                    // Make the new point.
                    Values[x + Xmax, y + Xmax] = new Point3D(x, y, z);

                    // Update the min and max values.
                    if (Zmin > z) Zmin = z;
                    if (Zmax < z) Zmax = z;
                }
            }

            // Console.WriteLine(zmin.ToString() + " <= z <= " + zmax.ToString());
        }

        // Draw level curves for the function.
        private void DrawLevelCurves(PictureBox pbx)
        {
            // Make the Bitmap.
            Bitmap bm = new Bitmap(pbx.ClientSize.Width, pbx.ClientSize.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                // Clear.
                gr.Clear(Color.White);
                gr.ScaleTransform(
                    bm.Width / Xmax / 2,
                    -bm.Height / Xmax / 2,
                    System.Drawing.Drawing2D.MatrixOrder.Append);
                gr.TranslateTransform(bm.Width * 0.5f, bm.Height * 0.5f,
                    System.Drawing.Drawing2D.MatrixOrder.Append);

                // Draw axes.
                using (Pen axis_pen = new Pen(Color.LightGray, 0))
                {
                    gr.DrawLine(axis_pen, -Xmax, 0, Xmax, 0);
                    gr.DrawLine(axis_pen, 0, -Xmax, 0, Xmax);
                    for (int i = -Xmax; i <= Xmax; i++)
                    {
                        gr.DrawLine(axis_pen, i, -0.1f, i, 0.1f);
                        gr.DrawLine(axis_pen, -0.1f, i, 0.1f, i);
                    }
                }

                // Draw level curves.
                double dz = (Zmax - Zmin) / 20;
                for (double z = Zmin; z <= Zmax; z += dz)
                {
                    // Draw this level curve;
                    DrawLevelCurve(gr, Values, z);
                }
            } // using gr.

            // Display the result.
            pbx.Image = bm;
        }

        // Draw this level curve.
        private void DrawLevelCurve(Graphics gr, Point3D[,] values, double z)
        {
            using (Pen thin_pen = new Pen(Color.Black, 0))
            {
                if (z > 0)
                {
                    thin_pen.Color = Color.Blue;
                }
                else if (z < 0)
                {
                    thin_pen.Color = Color.Red;
                }

                for (int x = 0; x < values.GetUpperBound(0); x++)
                {
                    for (int y = 0; y < values.GetUpperBound(1); y++)
                    {
                        // Intersect this triangle with the level plane.
                        DrawPlaneTriangleIntersections(
                            gr, thin_pen,
                            new Point3D(0, 0, z),
                            new Vector3D(0, 0, 1),
                            values[x, y],
                            values[x, y + 1],
                            values[x + 1, y + 1]);

                        // Intersect this triangle with the level plane.
                        DrawPlaneTriangleIntersections(
                            gr, thin_pen,
                            new Point3D(0, 0, z),
                            new Vector3D(0, 0, 1),
                            values[x, y],
                            values[x + 1, y + 1],
                            values[x + 1, y]);
                    }
                }
            }
        }

        // Draw the line segment of intersection
        // between a triangle and a plane.
        private void DrawPlaneTriangleIntersections(
            Graphics gr, Pen pen,
            Point3D p0, Vector3D N,
            Point3D p1, Point3D p2, Point3D p3)
        {
            List<Point3D> points = new List<Point3D>();
            IntersectPlaneAndTriangle(
                points, p0, N, p1, p2, p3);
            if (points.Count == 2)
            {
                // The triangle intersects the plane.
                gr.DrawLine(pen,
                    (float)points[0].X, (float)points[0].Y,
                    (float)points[1].X, (float)points[1].Y);
            }
            if (points.Count > 2)
            {
                gr.DrawLine(pen,
                    (float)points[0].X, (float)points[0].Y,
                    (float)points[2].X, (float)points[2].Y);
                gr.DrawLine(pen,
                    (float)points[1].X, (float)points[1].Y,
                    (float)points[2].X, (float)points[2].Y);
            }
        }

        // Return the line segment of intersection
        // between a triangle and a plane.
        private void IntersectPlaneAndTriangle(
            List<Point3D> points,
            Point3D p0, Vector3D N,
            Point3D p1, Point3D p2, Point3D p3)
        {
            // Find points of intersection between
            // the triangle's edges and the plane.
            IntersectPlaneAndSegment(points, p0, N, p1, p2);
            IntersectPlaneAndSegment(points, p0, N, p2, p3);
            IntersectPlaneAndSegment(points, p0, N, p3, p1);
        }

        // If the plane and line segment intersect, add the
        // points of intersection to points and return true.
        //
        // The equation of the plane is:
        //      N dot (p - p0) = 0
        //
        // The equation of the line is:
        //      p1 + t * <p2 - p1> where 0 <= t <= 1
        //
        // The plane and line intersect where:
        //      t = [N dot <p0 - p1>] / [N dot <p2 - p1>]
        private void IntersectPlaneAndSegment(List<Point3D> points,
            Point3D p0, Vector3D N,
            Point3D p1, Point3D p2)
        {
            // Get the denominator. If it's 0, the plane and line are parallel.
            Vector3D v12 = p2 - p1;
            double denominator = Vector3D.DotProduct(N, v12);
            if (Math.Abs(denominator) < -0.0001) return;

            // Get the numerator.
            Vector3D v10 = p0 - p1;
            double numerator = Vector3D.DotProduct(N, v10);

            // Calculate t and see if the segment intersects the plane.
            double t = numerator / denominator;
            if ((t >= 0) && (t <= 1))
            {
                // The segment intersects the plane at p1 + t * v12.
                points.Add(p1 + t * v12);
            }
        }

        // The functions.
        // Bowl.
        private double F1(double x, double y)
        {
            return x * x + (y * 2) * (y * 2) - 600;
        }

        // Monkey saddle.
        private double F2(double x, double y)
        {
            return x * (x * x - 3 * y * y);
        }

        // Crossed trough.
        private double F3(double x, double y)
        {
            return x * x * y * y - 30000;
        }

        // Hemisphere.
        private double F4(double x, double y)
        {
            return Math.Sqrt(400 - (x * x + y * y));
        }
        #endregion

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

        void DrawHeart()
        {
            // Plot the equations.
            // Make the Bitmap.
            Bitmap bm = new Bitmap(pictureBox4.ClientSize.Width, pictureBox4.ClientSize.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                // Clear.
                gr.Clear(Color.White);

                Rectangle rect = new Rectangle(-2, -2, 4, 4);
                Point[] pts = new Point[] 
                { 
                    new Point(0, pictureBox4.ClientSize.Height),
                    new Point(pictureBox4.ClientSize.Width, pictureBox4.ClientSize.Height), 
                    new Point(0, 0)
                };
                gr.Transform = new Matrix(rect, pts);

                // Draw axes.
                using (Pen axis_pen = new Pen(Color.Gray, 0))
                {
                    gr.DrawLine(axis_pen, -2, 0, 2, 0);
                    gr.DrawLine(axis_pen, 0, -2, 0, 2);
                    for (int i = -2; i <= 2; i++)
                    {
                        gr.DrawLine(axis_pen, i, -0.1f, i, 0.1f);
                        gr.DrawLine(axis_pen, -0.1f, i, 0.1f, i);
                    }
                }

                // Graph the equations.
                float dx = 2f / bm.Width;
                float dy = 2f / bm.Height;
                PlotFunction(gr, HeartFunc, dx, dy);
            } // using gr.

            // Display the result.
            pictureBox5.Image = bm;
        }

        private delegate float FofXY(float x, float y);

        // Plot a function.
        private void PlotFunction(Graphics gr, FofXY func, float dx, float dy)
        {
            // Plot the function.
            using (Pen thin_pen = new Pen(Color.Black, 0))
            {
                // Horizontal comparisons.
                for (float x = -2f; x <= 2f; x += dx)
                {
                    float last_y = func(x, -2f);
                    for (float y = -2f + dy; y <= 2f; y += dy)
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
                for (float y = -2f + dy; y <= 2f; y += dy)
                {
                    float last_x = func(-2f, y);
                    for (float x = -2f; x <= 2f; x += dx)
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

        // The function.
        private float HeartFunc(float x, float y)
        {
            /*
            //Heart type 1
            double a = x * x;
            double b = y - Math.Pow(x * x, (double)1 / 3);
            return (float)(a + b * b - 1);
            */

            //Heart type 2
            double a = x * x;
            double b = 5.0 * y / 4.0 - Math.Sqrt(Math.Abs(x));
            return (float)(a * a + b * b - 1);
        }





    }
}
