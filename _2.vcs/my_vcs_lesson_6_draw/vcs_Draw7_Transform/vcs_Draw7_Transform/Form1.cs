using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //SmoothingMode

namespace vcs_Draw7_Transform
{
    public partial class Form1 : Form
    {
        List<double> x = new List<double>();
        List<double> y = new List<double>();

        int xmin;
        int xmax;
        float ymin;
        float ymax;
        float xmargin_perncent = 5;
        float ymargin_perncent = 5;
        float xmargin;
        float ymargin;
        float xratio;
        float yratio;

        int W;
        int H;

        bool flag_draw_axis = true;
        bool flag_draw_title = true;
        //bool flag_draw_xylabel = true;
        //bool flag_draw_xytick = true;

        string title = "My VCS Test";

        Point[] Points = new Point[8];    //一維陣列內有 8 個Point

        int N = 360;
        Point[] data;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            W = pictureBox1.ClientSize.Width;
            H = pictureBox1.ClientSize.Height;
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            data = new Point[N];    //一維陣列內有 N 個Point
            int i;
            for (i = 0; i < N; i++)
            {
                data[i].X = i;
                data[i].Y = 100 + (int)(100 * sind(i));
            }
        }

        void MakeData1a()
        {
            richTextBox1.Text += "製作資料\n";
            richTextBox1.Text += "x=-180:5:180;\n";
            richTextBox1.Text += "y=sind(x)+0.6;\n";

            x.Clear();
            y.Clear();
            ymax = 0;
            ymin = 0;

            xmin = -180;
            xmax = 180;
            float i;
            //原始x y資料
            double yy;
            for (i = xmin; i <= xmax; i += 5f)
            {
                x.Add(i);

                yy = sind(i) + 0.6;

                /*
                if (i == 0)
                    yy = 1;
                else
                    yy = (float)(Math.Sin(i) / i);
                */
                if (Math.Abs(yy) < 0.0001)
                    yy = 0;
                y.Add(yy);     //y = sind(x)   x=-180:1:180
            }
        }

        void MakeData1b()
        {
            richTextBox1.Text += "製作資料\n";
            richTextBox1.Text += "x=-180:5:180;\n";
            richTextBox1.Text += "y=sind(x)+0.6;\n";

            x.Clear();
            y.Clear();
            ymax = 0;
            ymin = 0;

            xmin = -180;
            xmax = 180;
            float i;
            //原始x y資料
            double yy;
            for (i = xmin; i <= xmax; i += 5f)
            {
                //x.Add(i);
                x.Add(i + 180);
                //yy = sind(i)+0.6;
                //yy = sind(i);
                yy = sind(i) * 50 + 50;
                /*
                if (i == 0)
                    yy = 1;
                else
                    yy = (float)(Math.Sin(i) / i);
                */
                if (Math.Abs(yy) < 0.0001)
                    yy = 0;
                y.Add(yy);     //y = sind(x)   x=-180:1:180
            }
        }

        void DrawData1a()
        {
            int i;

            xmargin = W * xmargin_perncent / 100;
            ymargin = H * ymargin_perncent / 100;

            //找出最大與最小的y
            ymax = (float)y[0];
            ymin = (float)y[0];
            for (i = 0; i < x.Count; i++)
            {
                if (y[i] > ymax)
                    ymax = (float)y[i];
                if (y[i] < ymin)
                    ymin = (float)y[i];
            }
            richTextBox1.Text += "找到 最大y = " + ymax.ToString() + "\t 最小y = " + ymin.ToString() + "\n";

            xratio = (float)((W - xmargin * 2) / (float)(xmax - xmin));     //2 倍
            yratio = (float)((H - ymargin * 2) / (float)(ymax - ymin));     //180 倍

            richTextBox1.Text += "xratio = " + xratio.ToString() + "\n";
            richTextBox1.Text += "yratio = " + yratio.ToString() + "\n";

            /*
            richTextBox1.Text += "原始x y資料\n";
            for (i = 0; i < x.Count; i++)
            {
                richTextBox1.Text += x[i].ToString() + "\t" + y[i].ToString() + "\n";
            }
            richTextBox1.Text += "\n";
            */


            richTextBox1.Text += "平移x y資料\n";
            for (i = 0; i < x.Count; i++)
            {
                x[i] = x[i] - xmin;
                y[i] = y[i] - ymin;
                //richTextBox1.Text += x[i].ToString() + "\t" + y[i].ToString() + "\n";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "放大x y資料\n";
            for (i = 0; i < x.Count; i++)
            {
                x[i] = x[i] * xratio;
                y[i] = y[i] * yratio;
                //richTextBox1.Text += x[i].ToString() + "\t" + y[i].ToString() + "\n";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "y反相\n";
            for (i = 0; i < x.Count; i++)
            {
                y[i] = H - y[i];
                //richTextBox1.Text += x[i].ToString() + "\t" + y[i].ToString() + "\n";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "加margin\n";
            for (i = 0; i < x.Count; i++)
            {
                x[i] = x[i] + xmargin;
                y[i] = y[i] - ymargin;
                //richTextBox1.Text += x[i].ToString() + "\t" + y[i].ToString() + "\n";
            }
            richTextBox1.Text += "\n";



            Graphics g = pictureBox1.CreateGraphics();
            g.Clear(Color.White);
            g.DrawRectangle(new Pen(Color.Red, 1), 0, 0, W - 1, H - 1);
            g.DrawRectangle(new Pen(Color.Red, 1), xmargin, ymargin, W - xmargin * 2 - 1, H - ymargin * 2 - 1);


            //DrawLines 直接使用 List
            List<PointF> points = new List<PointF>();

            //int i;
            for (i = 0; i < x.Count; i++)
            {
                //points.Add(new PointF((float)(x[i] * xratio), H - (float)(y[i] * yratio)-H/2));
                //points.Add(new PointF((float)(x[i] * 1 - xmin), H - (float)(y[i] * yratio - ymin) - H / 2));
                //points.Add(new PointF((float)((x[i] - xmin) * xratio), (float)((y[i] - ymin) * 1)));
                points.Add(new PointF((float)x[i], (float)y[i]));
            }
            g.DrawLines(new Pen(Color.Red, 3), points.ToArray());

            /*
            //把XY資料印出來
            richTextBox1.Text += "X\tY\n";
            for (i = 0; i < points.Count; i++)
            {
                richTextBox1.Text += points[i].X.ToString() + "\t" + points[i].Y.ToString() + "\n";
            }
            richTextBox1.Text += "\n";
            */

            if (flag_draw_axis == true)
            {
                // Create pen.
                Pen p = new Pen(Color.Black, 3);

                float x1;
                float y1;
                float x2;
                float y2;
                PointF p1;
                PointF p2;

                //x軸
                x1 = xmargin;
                y1 = H - (0 - ymin * yratio) - ymargin;
                x2 = W - xmargin;
                y2 = H - (0 - ymin * yratio) - ymargin;
                p1 = new PointF(x1, y1);
                p2 = new PointF(x2, y2);

                g.DrawLine(p, p1, p2);

                //y軸
                x1 = (0 - xmin) * xratio + xmargin;
                y1 = ymargin;
                x2 = (0 - xmin) * xratio + xmargin;
                y2 = H - ymargin;
                p1 = new PointF(x1, y1);
                p2 = new PointF(x2, y2);

                g.DrawLine(p, p1, p2);

                /*  輔助線 正中間
                g.DrawLine(new Pen(Color.Pink, 1), 0, H / 2, W, H / 2);
                g.DrawLine(new Pen(Color.Pink, 1), W / 2, 0, W / 2, H);
                */

            }

            if (flag_draw_title == true)
            {
                float x_st = W / 2 - 80;
                float y_st = ymargin / 5;
                g.DrawString(title, new Font("標楷體", 15), new SolidBrush(Color.Green), new PointF(x_st, y_st));
            }
        }

        void DrawData1b()
        {
            double x_max = x.Max();
            double x_min = x.Min();
            double y_max = y.Max();
            double y_min = y.Min();

            richTextBox1.Text += "x_min = " + x_min.ToString() + "\n";
            richTextBox1.Text += "x_max = " + x_max.ToString() + "\n";
            richTextBox1.Text += "y_min = " + y_min.ToString() + "\n";
            richTextBox1.Text += "y_max = " + y_max.ToString() + "\n";

            // Make a Bitmap.
            Bitmap bitmap1 = new Bitmap(W, H);
            using (Graphics g = Graphics.FromImage(bitmap1))
            {
                g.SmoothingMode = SmoothingMode.AntiAlias;
                g.Clear(Color.White);

                // Create pens.
                Pen redPen = new Pen(Color.Red, 0);     //線寬大於0會讓轉換後線變粗
                Pen bluePen = new Pen(Color.Blue, 0);

                //DrawLines 直接使用 List
                List<PointF> points = new List<PointF>();

                int i;
                for (i = 0; i < x.Count; i++)
                {
                    points.Add(new PointF((float)x[i], (float)y[i]));
                }
                g.DrawLines(redPen, points.ToArray());

                float dx = (float)x_min;
                float dy = (float)y_min;
                float w = (float)(x_max - x_min);
                float h = (float)(y_max - y_min);

                // Scale to fit the data.
                RectangleF rect = new RectangleF(dx, dy, w, h);

                //RectangleF rect = new RectangleF(0, 0, 100, 50);
                g.DrawRectangle(new Pen(Color.Red, 5), dx, dy, w, h);

                //g.DrawString("A", new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(20, 20));

                // Draw lines between original points to screen.
                //g.DrawLines(bluePen, Points);   //畫直線
                g.DrawString("文字", new Font("標楷體", 10), new SolidBrush(Color.Blue), new PointF(30, 20));

                //準備Transform

                int w2;
                int h2;
                int dx2;
                int dy2;

                w2 = W * 8 / 10;
                h2 = H * 8 / 10;
                dx2 = W * 1 / 10;
                dy2 = H * 1 / 10;

                PointF[] pts = 
                {
                    new PointF(dx2, dy2+h2),
                    new PointF(dx2+w2, dy2+h2),
                    new PointF(dx2, dy2),
                };
                g.DrawRectangle(new Pen(Color.Green, 5), dx2, dy2, w2 - 1, h2 - 1);
                //g.DrawRectangle(new Pen(Color.Red, 0), dx1, dy1, w1, h1);
                //g.DrawRectangle(new Pen(Color.Red, 1), 0, 0, Points[7].X, Points[7].Y);

                g.Transform = new Matrix(rect, pts);

                //g.DrawRectangle(new Pen(Color.Red, 0), dx1, dy1, w1, h1);
                //g.DrawRectangle(new Pen(Color.Red, 1), 0, 0, Points[7].X, Points[7].Y);

                g.Transform = new Matrix(rect, pts);

                g.DrawLines(redPen, points.ToArray());  //畫直線
                g.DrawString("文字", new Font("標楷體", 10), new SolidBrush(Color.Red), new PointF(30, 20));

                pictureBox1.Image = bitmap1;
            }
            return;
        }

        private double rad(double d)
        {
            return d * Math.PI / 180.0;
        }

        private double sind(double d)
        {
            return Math.Sin(d * Math.PI / 180.0);
        }

        private double cosd(double d)
        {
            return Math.Cos(d * Math.PI / 180.0);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //不使用Transform畫正弦波
            MakeData1a();
            DrawData1a();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //使用Transform畫正弦波
            MakeData1b();
            DrawData1b();
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void MakeData2()
        {
            richTextBox1.Text += "製作資料\n";
            // Make data
            Points[0].X = 0;
            Points[0].Y = 0;
            Points[1].X = 1;
            Points[1].Y = 1;
            Points[2].X = 2;
            Points[2].Y = 0;
            Points[3].X = 3;
            Points[3].Y = 2;
            Points[4].X = 4;
            Points[4].Y = 1;
            Points[5].X = 5;
            Points[5].Y = 3;
            Points[6].X = 6;
            Points[6].Y = 2;
            Points[7].X = 7;
            Points[7].Y = 4;

            int i;
            for (i = 0; i < 8; i++)
            {
                Points[i].X = 10 * Points[i].X;
                Points[i].Y = 40 * Points[i].Y;
            }
        }

        void DrawData2()
        {
            // Make a Bitmap.
            Bitmap bitmap1 = new Bitmap(W, H);
            using (Graphics g = Graphics.FromImage(bitmap1))
            {
                g.SmoothingMode = SmoothingMode.AntiAlias;
                g.Clear(Color.White);

                // Create pens.
                Pen redPen = new Pen(Color.Red, 2);     //線寬大於0會讓轉換後線變粗
                Pen bluePen = new Pen(Color.Blue, 2);

                // Draw lines between original points to screen.
                //g.DrawLines(bluePen, Points);   //畫直線
                g.DrawCurve(bluePen, Points);   //畫曲線
                g.DrawString("轉換前10", new Font("標楷體", 10), new SolidBrush(Color.Blue), new PointF(22, 20));

                //準備Transform
                int w1;
                int h1;
                int dx1;
                int dy1;

                w1 = Points[7].X * 10 / 10;
                h1 = Points[7].Y * 10 / 10;
                dx1 = Points[7].X * 0 / 10;
                dy1 = Points[7].Y * 0 / 10;

                RectangleF rect = new RectangleF(dx1, dy1, w1, h1);
                g.DrawRectangle(new Pen(Color.Red, 0), dx1, dy1, w1, h1);

                int w2;
                int h2;
                int dx2;
                int dy2;

                w2 = W * 8 / 10;
                h2 = H * 8 / 10;
                dx2 = W * 1 / 10;
                dy2 = H * 1 / 10;

                PointF[] pts = 
                {
                    new PointF(dx2, dy2+h2),
                    new PointF(dx2+w2, dy2+h2),
                    new PointF(dx2, dy2),
                };
                g.DrawRectangle(new Pen(Color.Green, 5), dx2, dy2, w2 - 1, h2 - 1);
                g.DrawRectangle(new Pen(Color.Red, 0), dx1, dy1, w1, h1);
                //g.DrawRectangle(new Pen(Color.Red, 1), 0, 0, Points[7].X, Points[7].Y);

                g.Transform = new Matrix(rect, pts);

                //g.DrawLines(redPen, Points);   //畫直線
                g.DrawCurve(redPen, Points);   //畫曲線
                g.DrawString("轉換後10", new Font("標楷體", 10), new SolidBrush(Color.Red), new PointF(22, 20));

                g.ResetTransform();
                g.DrawString("恢復轉換後10", new Font("標楷體", 10), new SolidBrush(Color.Red), new PointF(100, 20));

                pictureBox1.Image = bitmap1;
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            MakeData2();
            DrawData2();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //畫sin, 無transform
            richTextBox1.Text += "畫 y=100+100*sind(x), x=0:1:360 沒有transform\n";

            // Create pens.
            Pen greenPen = new Pen(Color.Green, 2);
            Graphics g = this.pictureBox1.CreateGraphics();

            // Draw lines between original points to screen.
            g.DrawLines(greenPen, data);   //畫直線

            // Draw curve to screen.
            //g.DrawCurve(greenPen, data); //畫曲線


        }

        private void button5_Click(object sender, EventArgs e)
        {
            //畫sin, 有transform
            richTextBox1.Text += "畫 y=sind(x), x=0:1:360 有transform\n";
            // Create pens.
            Pen redPen = new Pen(Color.Red, 3);
            Graphics g = this.pictureBox1.CreateGraphics();


            #region 做transform
            int x_max = 360;
            int x_min = 0;
            int y_max = 0;
            int y_min = 200;

            int i;
            for (i = 0; i < N; i++)
            {
                //data[i].X = i;
                //data[i].Y = 100 + (int)(100 * sind(i));
                if (data[i].Y > y_max)
                    y_max = data[i].Y;
                if (data[i].Y < y_min)
                    y_min = data[i].Y;
            }

            // Scale to fit the data.
            RectangleF rect = new RectangleF(x_min, y_min, x_max, y_max - y_min);

            g.DrawRectangle(redPen, x_min, y_min, x_max, y_max - y_min);

            richTextBox1.Text += "rect w = " + rect.Width.ToString() + ", h = " + rect.Height.ToString() + "\n";
            PointF[] pts = 
                {
                    new PointF(0, pictureBox1.ClientSize.Height),
                    new PointF(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height),
                    new PointF(0, 0),
                };

            richTextBox1.Text += "pts w = " + pictureBox1.ClientSize.Width.ToString() + ", h = " + pictureBox1.ClientSize.Height.ToString() + "\n";

            g.Transform = new Matrix(rect, pts);
            #endregion

            // Draw lines between original points to screen.
            g.DrawLines(redPen, data);   //畫直線

            // Draw curve to screen.
            //g.DrawCurve(redPen, data); //畫曲線
        }

        private void button6_Click(object sender, EventArgs e)
        {
            Pen redPen = new Pen(Color.Red, 3);
            Graphics g = this.pictureBox1.CreateGraphics();

            g.SmoothingMode = SmoothingMode.AntiAlias;      // Draw smoothly.

            richTextBox1.Text += "左: 原圖放大平移\n";
            //原圖在 (-1,-1) w = 2 h = 2
            //重置轉換
            g.ResetTransform();

            //x方向放大200倍 y方向放大100倍, 變成 (-200,-100), w = 400, h = 200
            g.ScaleTransform(200, 100);

            //平移 水平向右移200 垂直向下移200 
            g.TranslateTransform(200, 200, MatrixOrder.Append);

            // Draw.
            DrawChart(g);


            richTextBox1.Text += "右上: 原圖放大平移\n";
            //原圖在 (-1,-1) w = 2 h = 2
            //轉換到 (300,10) w = 150 h = 100  //放大又平移
            float x_st = 500f;
            float y_st = 10f;
            int w = 150;
            int h = 100;

            RectangleF from_rect = new RectangleF(-1, -1, 2, 2);
            PointF[] to_points =
            {
                new PointF(x_st, y_st),    // Upper left.
                new PointF(x_st+w, y_st),    // Upper right.
                new PointF(x_st, y_st+h),   // Lower left.
            };
            Matrix map_matrix = new Matrix(from_rect, to_points);
            g.Transform = map_matrix;
            // Draw.
            DrawChart(g);


            richTextBox1.Text += "右中: 原圖放大平移 且歪曲50\n";
            //原圖在 (-1,-1) w = 2 h = 2
            //轉換到 (400,120) w = 180 h = 100  //放大又平移 且 歪曲50
            x_st = 500f;
            y_st = 120f;
            w = 180;
            h = 100;

            from_rect = new RectangleF(-1, -1, 2, 2);
            to_points = new PointF[]
            {
                new PointF(x_st, y_st),    // Upper left.
                new PointF(x_st+w, y_st),   // Upper right.
                new PointF(x_st-50, y_st+h),    // Lower left.
            };
            map_matrix = new Matrix(from_rect, to_points);
            g.Transform = map_matrix;
            // Draw.
            DrawChart(g);


            richTextBox1.Text += "右下: 原圖放大平移 且 Y軸反相\n";
            //反相畫圖  Y軸反相
            //原圖在 (-1,-1) w = 2 h = 2
            //轉換到 (100,450) w = 100 h = 100  //放大又平移 且 Y軸反相

            x_st = 500f;
            y_st = 330f;
            w = 100;
            h = 100;

            from_rect = new RectangleF(-1, -1, 2, 2);
            to_points = new PointF[]
            {
                new PointF(x_st, y_st),   // Upper left.
                new PointF(x_st+w, y_st),   // Upper right.
                new PointF(x_st, y_st-h),   // Lower left.
            };
            map_matrix = new Matrix(from_rect, to_points);
            g.Transform = map_matrix;
            // Draw.
            DrawChart(g);
        }

        //把圖畫在(-1,-1) w = 2 h = 2
        private void DrawChart(Graphics g)
        {
            using (Pen black_pen = new Pen(Color.Black, 0))
            {
                g.DrawLine(black_pen, -1, 1, 1, 1);     //畫出X軸
                g.DrawLine(black_pen, -1, 1, -1, -1);   //畫出y軸

                using (Pen p = new Pen(Color.Red, 0))
                {
                    p.EndCap = LineCap.ArrowAnchor;

                    g.DrawLines(p, new PointF[]
                    {
                    new PointF(-1,1),
                    new PointF(-0.7f,-0.3f),
                    new PointF(-0.4f,0.2f),
                    new PointF(0.1f,0f),
                    new PointF(0.4f,0.3f),
                    new PointF(0.7f,-0.8f)
                    }
                    );
                }
            }
        }
    }
}
