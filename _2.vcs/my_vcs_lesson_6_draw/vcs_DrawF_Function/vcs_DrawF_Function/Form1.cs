using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace vcs_DrawF_Function
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            float A;
            float B;
            float C;
            float D;
            float E;

            // Calculate Polynomial(x)  Polynomial(x) = ax^4+bx^3+cx^2+dx+e
            A = 0;
            B = 0;
            C = 1;
            D = 0;
            E = 0;

            // Get the X coordinate bounds.
            float xmin = -10;
            float xmax = 10;
            float ymin = 100;
            float ymax = 0;

            float x_tick = 1;

            // Get points for the negative root on the left.
            List<PointF> points = new List<PointF>();
            float xmid1 = xmax;

            for (float x = xmin; x <= xmax; x += x_tick)
            {
                //float y = G1(x, A, B, C, D, E, F, -1f);
                float y = Polynomial(x, A, B, C, D, E);
                if (!IsNumber(y))
                {
                    xmid1 = x - 1;
                    break;
                }
                points.Add(new PointF(x, y));
            }

            int len = points.Count;
            richTextBox1.Text += "len = " + len.ToString() + "\n";

            for (int i = 0; i < len; i++)
            {
                if (points[i].Y > ymax)
                    ymax = points[i].Y;
                else if (points[i].Y < ymin)
                    ymin = points[i].Y;
                //richTextBox1.Text += "i = " + i.ToString() + "\tx = " + points[i].X.ToString() + "\ty = " + points[i].Y.ToString() + "\n";
            }
            richTextBox1.Text += "ymax = " + ymax.ToString() + "\n";
            richTextBox1.Text += "ymin = " + ymin.ToString() + "\n";

            int x_ratio = 1;
            int y_ratio = 1;
            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;

            x_ratio = (int)(W / (xmax - xmin));
            richTextBox1.Text += "x_ratio = " + x_ratio.ToString() + "\n";
            //x_ratio -= 10;    //to see the boundary

            y_ratio = (int)(H / (ymax - ymin));
            richTextBox1.Text += "y_ratio = " + y_ratio.ToString() + "\n";

            Bitmap bitmap1 = new Bitmap(W, H);
            using (Graphics g = Graphics.FromImage(bitmap1))
            {
                g.Clear(Color.White);
                g.SmoothingMode = SmoothingMode.AntiAlias;

                // Draw the curves.
                using (Pen thick_pen = new Pen(Color.Red, 2))
                {
                    for (int i = 0; i < len; i++)
                    {
                        points[i] = new PointF((points[i].X + 10) * x_ratio, H - (points[i].Y) * y_ratio);
                    }

                    thick_pen.Color = Color.Red;
                    if (points.Count > 1)
                        g.DrawLines(thick_pen, points.ToArray());
                }
            }
            // Display the result.
            pictureBox1.Image = bitmap1;
        }

        // Return true if the number is not infinity or NaN.
        private bool IsNumber(float number)
        {
            return !(float.IsNaN(number) || float.IsInfinity(number));
        }

        // Calculate Polynomial(x)  Polynomial(x) = ax^4+bx^3+cx^2+dx+e
        private float Polynomial(float x, float A, float B, float C, float D, float E)
        {
            float result;
            result = A * x * x * x * x + B * x * x * x + C * x * x + D * x + E;
            return result;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            MakeGraph();
        }

        // Make the graph.
        private void MakeGraph()
        {
            // The bounds to draw.
            float xmin = -20;
            float xmax = 20;
            float ymin = -5;
            float ymax = 12;

            // Make the Bitmap.
            int wid = pictureBox1.ClientSize.Width;
            int hgt = pictureBox1.ClientSize.Height;
            Bitmap bm = new Bitmap(wid, hgt);
            using (Graphics g = Graphics.FromImage(bm))
            {
                g.Clear(Color.White);
                g.SmoothingMode = SmoothingMode.AntiAlias;

                // Transform to map the graph bounds to the Bitmap.
                RectangleF rect = new RectangleF(xmin, ymin, xmax - xmin, ymax - ymin);
                PointF[] pts = 
                {
                    new PointF(0, hgt),
                    new PointF(wid, hgt),
                    new PointF(0, 0),
                };
                g.Transform = new Matrix(rect, pts);

                // Draw the graph.
                using (Pen graph_pen = new Pen(Color.Blue, 0))
                {
                    // Draw the axes.
                    g.DrawLine(graph_pen, xmin, 0, xmax, 0);
                    g.DrawLine(graph_pen, 0, ymin, 0, ymax);
                    for (int x = (int)xmin; x <= xmax; x++)
                    {
                        g.DrawLine(graph_pen, x, -0.1f, x, 0.1f);
                    }
                    for (int y = (int)ymin; y <= ymax; y++)
                    {
                        g.DrawLine(graph_pen, -0.1f, y, 0.1f, y);
                    }
                    graph_pen.Color = Color.Red;

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
                            if (points.Count == 0) valid_point = true;
                            else
                            {
                                float dy = y - points[points.Count - 1].Y;
                                if (Math.Abs(dy / dx) < 1000) valid_point = true;
                            }
                            if (valid_point) points.Add(new PointF(x, y));
                        }
                        catch
                        {
                        }

                        // If the new point is invalid, draw
                        // the points in the latest batch.
                        if (!valid_point)
                        {
                            if (points.Count > 1) g.DrawLines(graph_pen, points.ToArray());
                            points.Clear();
                        }

                    }

                    // Draw the last batch of points.
                    if (points.Count > 1) g.DrawLines(graph_pen, points.ToArray());
                }
            }

            // Display the result.
            pictureBox1.Image = bm;
        }

        // The function to graph.
        private float F(float x)
        {
            //return (float)((1 / x + 1 / (x + 1) - 2 * x * x) / 10);
            //return x;
            //return (float)Math.Sin(x);
            return (float)(10 * Math.Sin(x) / x);
        }

        //XY平面
        private void button3_Click(object sender, EventArgs e)
        {
            Graphics g;
            Pen p;
            SolidBrush sb;
            Bitmap bitmap1;

            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;

            //----開新的Bitmap----
            bitmap1 = new Bitmap(W, H);
            //----使用上面的Bitmap畫圖----
            g = Graphics.FromImage(bitmap1);


            p = new Pen(Color.Red, 10);     // 設定畫筆為紅色、粗細為 10 點。
            sb = new SolidBrush(Color.Blue);

            g.Clear(Color.White);


            float ratio_x, ratio_y;
            float w, h;
            float x0, x1, y0, y1;

            //----畫筆顏色----
            p = new Pen(Color.Black);
            sb = new SolidBrush(p.Color);
            //----取得picturebox寬度與高度----
            w = pictureBox1.Width;
            h = pictureBox1.Height;
            //----是否有上一次的圖片，如果有就清除----
            if (pictureBox1.Image != null)
                pictureBox1.Image = null;
            //if (bitmap1 != null)
            //  bitmap1.Dispose();
            //----轉換使用者輸入的資料----
            x0 = (float)10;
            y0 = (float)10;
            x1 = (float)-5;
            y1 = (float)-9;
            //----計算放大倍率----
            ratio_x = (w - 50) / 20;
            ratio_y = (h - 50) / 20;
            //----開新的Bitmap----
            bitmap1 = new Bitmap((int)w, (int)h);
            //----使用上面的Bitmap畫圖----
            g = Graphics.FromImage(bitmap1);
            //----清除Bitmap為某顏色----
            g.Clear(Color.White);
            //----更改原點位置----
            g.TranslateTransform(pictureBox1.Width / 2, pictureBox1.Height / 2);
            //----畫坐標軸----
            g.DrawLine(p, -1000, 0, 1000, 0);//x軸
            g.DrawLine(p, 0, -1000, 0, 1000);//y軸
            g.DrawString("X", this.Font, sb, w / 2 - 20, 20);
            g.DrawString("Y", this.Font, sb, 20, -h / 2);
            g.DrawLine(p, w / 2, 0, w / 2 - 10, 5);//x軸箭頭
            g.DrawLine(p, w / 2, 0, w / 2 - 10, -5);
            g.DrawLine(p, 0, -h / 2, 5, -h / 2 + 10);//y軸箭頭
            g.DrawLine(p, 0, -h / 2, -5, -h / 2 + 10);
            for (int i = -10; i <= 10; i++)//畫X Y軸座標位置
            {
                g.DrawLine(p, i * ratio_x, -5, i * ratio_x, 5);
                g.DrawString(i.ToString().PadLeft(2, ' '), this.Font, sb, i * ratio_x - 9, 10);
                g.DrawLine(p, -5, i * ratio_y, 5, i * ratio_y);
                if (i != 0)
                    g.DrawString(i.ToString(), this.Font, sb, 15, i * ratio_y - 8);
            }
            //----換顏色----
            p = new Pen(Color.Red);
            sb = new SolidBrush(p.Color);
            //----畫線----
            g.DrawLine(p, x0 * ratio_x, -y0 * ratio_y, x1 * ratio_x, -y1 * ratio_y);
            //----畫兩點----
            g.FillEllipse(sb, new RectangleF(x0 * ratio_x - 2.5f, -y0 * ratio_y - 2.5f, 5, 5));
            g.FillEllipse(sb, new RectangleF(x1 * ratio_x - 2.5f, -y1 * ratio_y - 2.5f, 5, 5));
            //----釋放Graphics資源----
            //g.Dispose();
            //----將Bitmap顯示在Picture上
            g.ResetTransform();
            pictureBox1.Image = bitmap1;


        }

    }
}
