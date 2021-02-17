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

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            W = pictureBox1.Width;
            H = pictureBox1.Height;
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        void MakeData()
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
                //yy = sind(i)+0.6;
                yy = sind(i);
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

        void DrawData1()
        {
            int i;

            xmargin = pictureBox1.Size.Width * xmargin_perncent / 100;
            ymargin = pictureBox1.Size.Height * ymargin_perncent / 100;

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
            g.DrawRectangle(new Pen(Color.Red, 1), 0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1);
            g.DrawRectangle(new Pen(Color.Red, 1), xmargin, ymargin, pictureBox1.Width - xmargin * 2 - 1, pictureBox1.Height - ymargin * 2 - 1);


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

        void DrawData2()
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
            Bitmap bm = new Bitmap(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.SmoothingMode = SmoothingMode.AntiAlias;

                // Scale to fit the data.
                //RectangleF rect = new RectangleF((float)x_min, (float)y_min, (float)x_max, (float)y_max);

                RectangleF rect = new RectangleF(0, 0, 100, 50);
                gr.DrawRectangle(new Pen(Color.Red, 0), (float)x_min, (float)y_min, (float)x_max, (float)y_max);

                //gr.DrawString("A", new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(20, 20));

                PointF[] pts = 
                {
                    new PointF(0, pictureBox1.ClientSize.Height),
                    new PointF(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height),
                    new PointF(0, 0),
                };
                //gr.DrawRectangle(new Pen(Color.Green, 10), 0, 0, pic.ClientSize.Width, pic.ClientSize.Height);

                //gr.DrawString("A", new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(30, 30));

                gr.Transform = new Matrix(rect, pts);

                //DrawLines 直接使用 List
                List<PointF> points = new List<PointF>();

                int i;
                for (i = 0; i < x.Count; i++)
                {
                    points.Add(new PointF((float)x[i], (float)y[i]));
                }
                //gr.DrawLines(new Pen(Color.Red, 0), points.ToArray());

                gr.DrawLine(new Pen(Color.Red, 2), 0, 0, 100, 50);
                gr.DrawRectangle(new Pen(Color.Red, 1), 0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1);
                gr.DrawRectangle(new Pen(Color.Red, 5), 0, 0, 100, 50);

                pictureBox1.Image = bm;


            }


            return;


            /*
            int i;

            xmargin = pictureBox1.Size.Width * xmargin_perncent / 100;
            ymargin = pictureBox1.Size.Height * ymargin_perncent / 100;

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


            richTextBox1.Text += "原始x y資料\n";
            for (i = 0; i < x.Count; i++)
            {
                richTextBox1.Text += x[i].ToString() + "\t" + y[i].ToString() + "\n";
            }
            richTextBox1.Text += "\n";



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
            g.DrawRectangle(new Pen(Color.Red, 1), 0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1);
            g.DrawRectangle(new Pen(Color.Red, 1), xmargin, ymargin, pictureBox1.Width - xmargin * 2 - 1, pictureBox1.Height - ymargin * 2 - 1);


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
            */

            /*
            //把XY資料印出來
            richTextBox1.Text += "X\tY\n";
            for (i = 0; i < points.Count; i++)
            {
                richTextBox1.Text += points[i].X.ToString() + "\t" + points[i].Y.ToString() + "\n";
            }
            richTextBox1.Text += "\n";
            */

            /*
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
            */
                /*  輔助線 正中間
                g.DrawLine(new Pen(Color.Pink, 1), 0, H / 2, W, H / 2);
                g.DrawLine(new Pen(Color.Pink, 1), W / 2, 0, W / 2, H);
                */
            /*
            }

            if (flag_draw_title == true)
            {
                float x_st = W / 2 - 80;
                float y_st = ymargin / 5;
                g.DrawString(title, new Font("標楷體", 15), new SolidBrush(Color.Green), new PointF(x_st, y_st));
            }
            */
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
            MakeData();
            DrawData1();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //使用Transform畫正弦波
            MakeData();
            DrawData2();
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }



    }
}
