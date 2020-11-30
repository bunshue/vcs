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
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {

            Graphics g = pictureBox1.CreateGraphics();
            g.DrawRectangle(new Pen(Color.Red, 1), 0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1);

            int xmin;
            int xmax;
            float ymin;
            float ymax;
            int xmargin;
            float ymargin;
            float xratio;
            float yratio;

            int W = pictureBox1.Width;
            int H = pictureBox1.Height;

            xmin = -180;
            xmax = 180;
            ymin = -1;
            ymax = 1;
            xmargin = 10;
            ymargin = 10;

            g.DrawRectangle(new Pen(Color.Red, 1), xmargin, ymargin, pictureBox1.Width - xmargin * 2 - 1, pictureBox1.Height - ymargin * 2 - 1);

            xratio = (float)((W - xmargin * 2) / (float)(xmax - xmin));     //2 倍
            yratio = (float)((H - ymargin * 2) / (float)(ymax - ymin));     //180 倍

            richTextBox1.Text += "xratio = " + xratio.ToString() + "\n";
            richTextBox1.Text += "yratio = " + yratio.ToString() + "\n";

            List<double> x = new List<double>();
            List<double> y = new List<double>();

            int i;
            //原始x y資料
            for (i = xmin; i <= xmax; i+=3)
            {
                x.Add(i);
                y.Add(sind(i));
            }

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
                richTextBox1.Text += x[i].ToString() + "\t" + y[i].ToString() + "\n";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "放大x y資料\n";
            for (i = 0; i < x.Count; i++)
            {
                x[i] = x[i] * xratio;
                y[i] = y[i] * yratio;
                richTextBox1.Text += x[i].ToString() + "\t" + y[i].ToString() + "\n";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "y反相\n";
            for (i = 0; i < x.Count; i++)
            {
                y[i] = H - y[i];
                richTextBox1.Text += x[i].ToString() + "\t" + y[i].ToString() + "\n";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "加margin\n";
            for (i = 0; i < x.Count; i++)
            {
                x[i] = x[i] + xmargin;
                y[i] = y[i] - ymargin;
                richTextBox1.Text += x[i].ToString() + "\t" + y[i].ToString() + "\n";
            }
            richTextBox1.Text += "\n";

            //DrawLines 直接使用 List
            List<PointF> points = new List<PointF>();

            for (i = 0; i < x.Count; i++)
            {
                //points.Add(new PointF((float)(x[i] * xratio), H - (float)(y[i] * yratio)-H/2));
                //points.Add(new PointF((float)(x[i] * 1 - xmin), H - (float)(y[i] * yratio - ymin) - H / 2));
                //points.Add(new PointF((float)((x[i] - xmin) * xratio), (float)((y[i] - ymin) * 1)));
                points.Add(new PointF((float)x[i], (float)y[i]));
            }
            g.DrawLines(new Pen(Color.Red, 3), points.ToArray());

            richTextBox1.Text += "X\tY\n";
            for (i = 0; i < points.Count; i++)
            {
                richTextBox1.Text += points[i].X.ToString() + "\t" + points[i].Y.ToString() + "\n";
            }
            richTextBox1.Text += "\n";
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
