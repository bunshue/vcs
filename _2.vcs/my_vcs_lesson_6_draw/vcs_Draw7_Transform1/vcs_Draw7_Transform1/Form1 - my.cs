using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;         //for Matrix

namespace vcs_Draw7_Transform1
{
    public partial class Form1 : Form
    {
        int N = 10;
        int M = 0;
        Point[] data;

        int x_max;
        int x_min;
        int y_max;
        int y_min;
        public Form1()
        {
            InitializeComponent();
        }

        
        private void Form1_Load(object sender, EventArgs e)
        {
            M = N * 2 + 1;
            data = new Point[M];    //一維陣列內有 M 個Point
            int i;
            for (i = -N; i <= N; i++)
            {
                data[N + i].X = i + 10;
                //data[i].Y = 100 + (int)(100 * sind(i));
                data[N + i].Y = i * i * i / 5;
            }

            x_max=data[0].X;
            x_min=data[0].X;
            y_max=data[0].Y;
            y_min=data[0].Y;

            for (i = 0; i < M; i++)
            {
                if (data[i].X < x_min)
                    x_min = data[i].X;
                else if (data[i].X > x_max)
                    x_max = data[i].X;
                if (data[i].Y < y_min)
                    y_min = data[i].Y;
                else if (data[i].Y > y_max)
                    y_max = data[i].Y;
            }
            richTextBox1.Text += "x_min =" + x_min.ToString() + "\n";
            richTextBox1.Text += "x_max =" + x_max.ToString() + "\n";
            richTextBox1.Text += "y_min =" + y_min.ToString() + "\n";
            richTextBox1.Text += "y_max =" + y_max.ToString() + "\n";
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
            richTextBox1.Text += "畫x^3/5, x=-10:1:10 沒有transform，只能顯示x,y皆為正值的部分，1:1比例\n";
            Graphics g = this.pictureBox1.CreateGraphics();

            // Create pens.
            Pen redPen = new Pen(Color.Red, 1);
            Pen blackPen = new Pen(Color.Black, 1);
            Pen greenPen = new Pen(Color.Green, 1);

            g.DrawRectangle(redPen, x_min, y_min, x_max, y_max - y_min);    //原資料標記

            // Draw lines between original points to screen.
            g.DrawLines(greenPen, data);   //畫直線

            // Draw curve to screen.
            //g.DrawCurve(greenPen, data); //畫曲線
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "畫x^3/5, x=-10:1:10 有transform，可以顯示全圖\n";
            Graphics g = this.pictureBox1.CreateGraphics();

            // Create pens.
            Pen redPen = new Pen(Color.Red, 1);
            Pen blackPen = new Pen(Color.Black, 1);
            Pen bluePen = new Pen(Color.Blue, 1);

            g.DrawRectangle(redPen, x_min, y_min, x_max, y_max - y_min);    //原資料標記

            #region 做transform
            // Scale to fit the data.
            RectangleF rect = new RectangleF(x_min, y_min, x_max, y_max - y_min);

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

            Point pt1;
            Point pt2;
            pt1 = new Point(x_min, (y_min + y_max) / 2);
            pt2 = new Point(x_max, (y_min + y_max) / 2);
            g.DrawLine(blackPen, pt1, pt2);

            pt1 = new Point((x_min + x_max) / 2, y_min);
            pt2 = new Point((x_min + x_max) / 2, y_max);
            g.DrawLine(blackPen, pt1, pt2);

            // Draw lines between original points to screen.
            g.DrawLines(bluePen, data);   //畫直線

            // Draw curve to screen.
            //g.DrawCurve(bluePen, data); //畫曲線
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "畫x^3/5, x=-10:1:10 有transform，可以顯示全圖 到中間 邊界10%\n";
            Graphics g = this.pictureBox1.CreateGraphics();

            // Create pens.
            Pen redPen = new Pen(Color.Red, 1);
            Pen blackPen = new Pen(Color.Black, 1);
            Pen bluePen = new Pen(Color.Blue, 1);

            g.DrawRectangle(redPen, x_min, y_min, x_max, y_max - y_min);    //原資料標記

            #region 做transform
            // Scale to fit the data.
            RectangleF rect = new RectangleF(x_min, y_min, x_max, y_max - y_min);

            richTextBox1.Text += "rect w = " + rect.Width.ToString() + ", h = " + rect.Height.ToString() + "\n";
            int w = pictureBox1.ClientSize.Width;
            int h = pictureBox1.ClientSize.Height;
            int x_st = w / 10;
            int y_st = h / 10;
            int w2 = w * 8 / 10;
            int h2 = h * 8 / 10;
            PointF[] pts = 
                {
                    new PointF(x_st, y_st+h2),
                    new PointF(x_st+w2, y_st+h2),
                    new PointF(x_st, y_st),
                };

            richTextBox1.Text += "pts w = " + pictureBox1.ClientSize.Width.ToString() + ", h = " + pictureBox1.ClientSize.Height.ToString() + "\n";

            g.Transform = new Matrix(rect, pts);
            #endregion

            // Draw lines between original points to screen.
            g.DrawLines(bluePen, data);   //畫直線

            // Draw curve to screen.
            //g.DrawCurve(bluePen, data); //畫曲線

        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            pictureBox1.Image = null;
        }
    }
}
