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
        int N = 360;
        Point[] data;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            data = new Point[N];    //一維陣列內有 N 個Point
            int i;
            for (i = 0; i < N; i++)
            {
                data[i].X = i;
                data[i].Y = 100 + (int)(100 * sind(i));
            }
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
            richTextBox1.Text += "畫 y=100+100*sind(x), x=0:1:360 沒有transform\n";

            // Create pens.
            Pen greenPen = new Pen(Color.Green, 2);
            Graphics g = this.pictureBox1.CreateGraphics();

            // Draw lines between original points to screen.
            g.DrawLines(greenPen, data);   //畫直線

            // Draw curve to screen.
            //g.DrawCurve(greenPen, data); //畫曲線
        }

        private void button2_Click(object sender, EventArgs e)
        {
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

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            pictureBox1.Image = null;
                
        }
    }
}
