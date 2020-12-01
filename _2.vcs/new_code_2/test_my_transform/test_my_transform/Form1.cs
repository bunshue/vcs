using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace test_my_transform
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

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            W = pictureBox1.Width;
            H = pictureBox1.Height;
        }

        void MakeData()
        {
            x.Clear();
            y.Clear();
            ymax = 0;
            ymin = 0;

            xmin = -20;
            xmax = 20;
            float i;
            //原始x y資料
            double yy;
            for (i = xmin; i <= xmax; i += 0.1f)
            {
                x.Add(i);
                //yy = sind(i);
                if (i == 0)
                    yy = 1;
                else
                    yy = (float)(Math.Sin(i) / i);
                if (Math.Abs(yy) < 0.0001)
                    yy = 0;
                y.Add(yy);     //y = sind(x)   x=-180:1:180
            }
        }

        void DrawData()
        {
            int i;

            xmargin = pictureBox1.Size.Width * xmargin_perncent / 100;
            ymargin = pictureBox1.Size.Height * ymargin_perncent / 100;

            //找出最大和最小的y
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
                //richTextBox1.Text += x[i].ToString() + "\t" + y[i].ToString() + "\n";
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
                g.DrawLine(new Pen(Color.Black, 3), xmin, H - (0 - ymin * yratio), (xmax - xmin) * xratio, H - (0 - ymin * yratio));
                g.DrawLine(new Pen(Color.Black, 3), (0 - xmin) * xratio, 0, (0 - xmin) * xratio, H);

            }
            */
        }

        private void button1_Click(object sender, EventArgs e)
        {
            MakeData();
            DrawData();


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



    }
}
