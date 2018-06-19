using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_test_all_11_Draw2
{
    public partial class Form1 : Form
    {
        Graphics g;
        public Form1()
        {
            InitializeComponent();
            g = panel1.CreateGraphics();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int[] x = { 0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600 };
            int[] y = { 200, 295, 368, 399, 381, 319, 228, 129, 48, 4, 8, 58, 144, 243, 331, 387, 397, 359, 282, 184, 91 };
            Bitmap bitM = new Bitmap(this.panel1.Width, this.panel1.Height);
            //MessageBox.Show("Width = " + this.panel1.Width + "  Height = " + this.panel1.Height);
            Graphics g = Graphics.FromImage(bitM);
            g.Clear(Color.WhiteSmoke);
            Point[] points = new Point[21];
            Random r = new Random();
            for (int i = 0; i < 21; i++)
            {
                points[i].X = x[i];
                points[i].Y = y[i];
            }
            g.DrawLines(new Pen(Color.FromArgb(r.Next(1, 255), r.Next(1, 255), r.Next(1, 255))), points);  //繪製折線 
            this.panel1.BackgroundImage = bitM;

        }

        private void button2_Click(object sender, EventArgs e)
        {
            int[] x = { 0, 40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560, 600 };
            int[] y = { 200, 328, 396, 373, 268, 131, 26, 3, 71, 200, 328, 396, 373, 268, 131, 26 };

            for (int i = 0; i < 10; i++)
            {
                Application.DoEvents();
                for (int j = 0; j < 20; j++)
                    System.Threading.Thread.Sleep(1);

                g.DrawLine(Pens.Red, new Point(x[i], 400 - y[i]), new Point(x[i + 1], 400 - y[i + 1]));
            }
            MessageBox.Show("OK");

        }

        private void button4_Click(object sender, EventArgs e)
        {
            // Create pen.
            Pen blackPen = new Pen(Color.Black, 3);
            // Create location and size of ellipse.

            float x = 0.0F;
            float y = 0.0F;
            float width = 400.0F;
            float height = 200.0F;

            //都是以左上角為基準

            //畫橢圓
            g.DrawEllipse(blackPen, x, y, width, height);

            //畫圓
            g.DrawEllipse(Pens.Blue, x, y, 50, 50);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            // Draw line to screen.
            g.DrawLine(Pens.Red, new Point(0, 0), new Point(400, 0));
            g.DrawLine(Pens.Green, new Point(0, 0), new Point(400, 200));
            g.DrawLine(Pens.Blue, new Point(0, 0), new Point(0, 200));
            g.DrawLine(Pens.Black, new Point(0, 0), new Point(400, 200));
            g.DrawLine(Pens.Red, new Point(400, 0), new Point(400, 200));
            g.DrawLine(Pens.Red, new Point(0, 200), new Point(400, 200));
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //法一
            g.Clear(BackColor);             //清除畫板

            //法二
            //g.Clear(panel1.BackColor);      //清除畫板
        }

        private void button5_Click(object sender, EventArgs e)
        {
            int[] x = new int[10];
            double[] y = new double[10];
            int[] yy = new int[10];
            //int x[10] = 0;
            //float y[10] = 0;
            for (int i = 0; i < 10; i++)
            {
                x[i] = i * 40;
                y[i] = Math.Sin(x[i] * Math.PI / 180) * 200 + 200;
                yy[i] = (int)y[i];
                richTextBox1.Text += x[i].ToString() + "\t" + y[i].ToString() + "\n";
            }

            Pen greenPen = new Pen(Color.Green, 3); // Create pens.

            // Create points that define curve.
            Point point0 = new Point(x[0], yy[0]);
            Point point1 = new Point(x[1], yy[1]);
            Point point2 = new Point(x[2], yy[2]);
            Point point3 = new Point(x[3], yy[3]);
            Point point4 = new Point(x[4], yy[4]);
            Point point5 = new Point(x[5], yy[5]);
            Point point6 = new Point(x[6], yy[6]);
            Point point7 = new Point(x[7], yy[7]);
            Point point8 = new Point(x[8], yy[8]);
            Point point9 = new Point(x[9], yy[9]);

            Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9 };

            g.DrawCurve(greenPen, curvePoints); //畫曲線
            g.DrawLines(greenPen, curvePoints);   //畫直線
        }

        private void button7_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button12_Click(object sender, EventArgs e)
        {
            g.DrawString("這是一組同心圓", this.Font, Brushes.Black, 10, 20);
            Pen p1 = new Pen(Color.Red);
            Pen p2 = new Pen(Color.Purple);
            Pen p3 = new Pen(Color.Blue);
            Pen p4 = new Pen(Color.Green);
            g.DrawEllipse(p1, 120 - 80, 120 - 80, 80 * 2, 80 * 2);
            g.DrawEllipse(p2, 120 - 60, 120 - 60, 60 * 2, 60 * 2);
            g.DrawEllipse(p3, 120 - 40, 120 - 40, 40 * 2, 40 * 2);
            g.DrawEllipse(p4, 120 - 20, 120 - 20, 20 * 2, 20 * 2);
        }
    }
}
