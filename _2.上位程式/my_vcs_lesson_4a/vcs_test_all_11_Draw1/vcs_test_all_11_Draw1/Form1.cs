using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_test_all_11_Draw1
{
    public partial class Form1 : Form
    {
        Graphics g;
        public Form1()
        {
            InitializeComponent();
            g = panel1.CreateGraphics();
        }

        int flag_Draw_circle = 0;
        int flag_Draw_line = 0;
        int flag_Draw_picture = 0;
        float x_old = -1;
        float y_old = -1;

        private void button1_Click(object sender, EventArgs e)
        {
            Pen bluePen = new Pen(Color.Blue, 3);// Create pens.

            Point point1a = new Point(0, 0);
            Point point2a = new Point(600, 400);
            g.DrawLine(bluePen, point1a, point2a);     // Draw line to screen.

            Point point3a = new Point(300, 400);
            Point point4a = new Point(600, 0);
            g.DrawLine(bluePen, point3a, point4a);     // Draw line to screen.
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Pen redPen = new Pen(Color.Red, 3); // Create pens.

            // Create points that define curve.
            Point point0 = new Point(0, 400);
            Point point1 = new Point(50, 350);
            Point point2 = new Point(100, 400);
            Point point3 = new Point(150, 250);
            Point point4 = new Point(200, 200);
            Point point5 = new Point(250, 150);
            Point point6 = new Point(300, 100);
            Point point7 = new Point(350, 50);
            Point point8 = new Point(400, 0);
            Point point9 = new Point(450, 200);
            Point point10 = new Point(500, 400);
            Point point11 = new Point(550, 300);
            Point point12 = new Point(600, 100);

            Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12};

            g.DrawLines(redPen, curvePoints);   //畫直線

        }

        private void button3_Click(object sender, EventArgs e)
        {
            g.Clear(BackColor);     //清除整個繪圖介面，並使用指定的背景色彩填滿它。
        }

        private void DrawXY()//画X轴Y轴
        {
            Point px1 = new Point(0, this.panel1.Height);
            Point px2 = new Point(this.panel1.Width, this.panel1.Height);
            g.DrawLine(new Pen(Brushes.Black, 5), px1, px2);
            Point py1 = new Point(0, this.panel1.Height);
            Point py2 = new Point(0, 0);
            g.DrawLine(new Pen(Brushes.Black, 5), py1, py2);
        }

        private void DrawXLine()    //画X轴平行线
        {
            for (int i = 1; i < 9; i++)
            {
                Point px1 = new Point(0, this.panel1.Height - i * 50);
                Point px2 = new Point(this.panel1.Width, this.panel1.Height - i * 50);
                g.DrawLine(new Pen(Brushes.Black, 1), px1, px2);
            }
        }
        private void DrawYLine()    //画X轴刻度
        {
            for (int i = 1; i < 9; i++)
            {
                Point py1 = new Point(100 * i, this.panel1.Height - 5);
                Point py2 = new Point(100 * i, this.panel1.Height);
                g.DrawLine(new Pen(Brushes.Red, 1), py1, py2);
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            DrawXY();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            DrawXLine();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            DrawYLine();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            Pen greenPen = new Pen(Color.Green, 3); // Create pens.

            // Create points that define curve.
            Point point0 = new Point(0, 400);
            Point point1 = new Point(50, 350);
            Point point2 = new Point(100, 400);
            Point point3 = new Point(150, 250);
            Point point4 = new Point(200, 200);
            Point point5 = new Point(250, 150);
            Point point6 = new Point(300, 100);
            Point point7 = new Point(350, 50);
            Point point8 = new Point(400, 0);
            Point point9 = new Point(450, 200);
            Point point10 = new Point(500, 400);
            Point point11 = new Point(550, 300);
            Point point12 = new Point(600, 100);

            Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12 };

            g.DrawCurve(greenPen, curvePoints); //畫曲線

        }

        private void button8_Click(object sender, EventArgs e)
        {
            //在指定位置畫上一圖
            // Create image.
            //Image newImage = Image.FromFile("calculator.png");
            Image newImage = Resource1.doraemon;

            // Create coordinates for upper-left corner of image.
            int x = 50;
            int y = 50;

            // Draw image to screen.
            g.DrawImage(newImage, x, y);
        }

        private void button9_Click(object sender, EventArgs e)
        {
            // Create string to draw.
            String drawString = "測試文字";

            // Create font and brush.
            Font drawFont = new Font("Arial", 16);
            SolidBrush drawBrush = new SolidBrush(Color.Black);

            // Create point for upper-left corner of drawing.
            PointF drawPoint = new PointF(150.0F, 150.0F);

            // Draw string to screen.
            g.DrawString(drawString, drawFont, drawBrush, drawPoint);
        }

        private void button10_Click(object sender, EventArgs e)
        {
            // Create pen.
            Pen blackPen = new Pen(Color.Black, 3);

            // Create location and size of ellipse.
            float x = 300F;
            float y = 200F;
            float width = 200.0F;
            float height = 100.0F;

            // Draw ellipse to screen.
            g.DrawEllipse(blackPen, x, y, width, height);
        }

        private void button11_Click(object sender, EventArgs e)
        {
            // Create pen.
            Pen blackPen = new Pen(Color.Black, 3);

            // Create location and size of ellipse.
            float x = 300F;
            float y = 200F;
            float width = 200.0F;
            float height =200.0F;

            // Draw ellipse to screen.
            g.DrawEllipse(blackPen, x, y, width, height);
        }

        private void button12_Click(object sender, EventArgs e)
        {
            // Create pen.
            Pen blackPen = new Pen(Color.Black, 3);

            // Create location and size of ellipse.
            float x = 300F;
            float y = 200F;
            float r = 200F;
            float xx = x-r;
            float yy = y-r;
            float width = r*2;
            float height = r*2;

            // Draw ellipse to screen.
            g.DrawEllipse(blackPen, xx, yy, width, height);
        }

        private void panel1_MouseClick(object sender, MouseEventArgs e)
        {
            if ((flag_Draw_circle == 0) && (flag_Draw_line == 0) && (flag_Draw_picture == 0))
                return;

            if ((flag_Draw_circle == 0) || (flag_Draw_line == 0))
                DrawLineCircle(e.X, e.Y, 10);

            if (flag_Draw_picture == 1)
                DrawPicture(e.X, e.Y);
        }

        private void DrawPicture(float x, float y)
        {
            //在指定位置畫上一圖
            // Create image.
            Image newImage = Resource1.doraemon;

            // Draw image to screen.
            g.DrawImage(newImage, x, y);
        }

        private void DrawLineCircle(float x, float y, float r)
        {
            // Create pen.
            Pen redPen = new Pen(Color.Red, 3);
            Pen bluePen = new Pen(Color.Blue, 3);

            // Create location and size of ellipse.
            float xx = x - r;
            float yy = y - r;
            float width = r * 2;
            float height = r * 2;

            if (flag_Draw_circle == 1)
            {
                // Draw ellipse to screen.
                g.DrawEllipse(redPen, xx, yy, width, height);
            }

            if (flag_Draw_line == 1)
            {
                if (x_old != -1)
                {
                    Point point1a = new Point((int)x_old, (int)y_old);
                    Point point2a = new Point((int)x, (int)y);
                    g.DrawLine(bluePen, point1a, point2a);     // Draw line to screen.
                }
                x_old = x;
                y_old = y;
            }
        }

        private void panel1_MouseMove(object sender, MouseEventArgs e)
        {
            label2.Text = e.X + " : " + e.Y;
        }

        private void button13_Click(object sender, EventArgs e)
        {
            double[] xx = new double[20];
            double[] yy = new double[20];

            for(int i=0;i<20;i++)
            {
                xx[i] = i*30;
                yy[i] = Math.Sin(i)*200+200;
                //yy[i] = 100;
            }

            Pen redPen = new Pen(Color.Red, 3); // Create pens.

            // Create points that define curve.
            Point point0 = new Point((int)xx[0], panel1.Height - (int)yy[0]);
            Point point1 = new Point((int)xx[1], panel1.Height - (int)yy[1]);
            Point point2 = new Point((int)xx[2], panel1.Height - (int)yy[2]);
            Point point3 = new Point((int)xx[3], panel1.Height - (int)yy[3]);
            Point point4 = new Point((int)xx[4], panel1.Height - (int)yy[4]);
            Point point5 = new Point((int)xx[5], panel1.Height - (int)yy[5]);
            Point point6 = new Point((int)xx[6], panel1.Height - (int)yy[6]);
            Point point7 = new Point((int)xx[7], panel1.Height - (int)yy[7]);
            Point point8 = new Point((int)xx[8], panel1.Height - (int)yy[8]);
            Point point9 = new Point((int)xx[9], panel1.Height - (int)yy[9]);
            Point point10 = new Point((int)xx[10], panel1.Height - (int)yy[10]);
            Point point11 = new Point((int)xx[11], panel1.Height - (int)yy[11]);
            Point point12 = new Point((int)xx[12], panel1.Height - (int)yy[12]);
            Point point13 = new Point((int)xx[13], panel1.Height - (int)yy[13]);
            Point point14 = new Point((int)xx[14], panel1.Height - (int)yy[14]);
            Point point15 = new Point((int)xx[15], panel1.Height - (int)yy[15]);
            Point point16 = new Point((int)xx[16], panel1.Height - (int)yy[16]);
            Point point17 = new Point((int)xx[17], panel1.Height - (int)yy[17]);
            Point point18 = new Point((int)xx[18], panel1.Height - (int)yy[18]);
            Point point19 = new Point((int)xx[19], panel1.Height - (int)yy[19]);

            Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14, point15, point16, point17, point18, point19 };

            g.DrawLines(redPen, curvePoints);   //畫直線
        }

        private void button14_Click(object sender, EventArgs e)
        {
            double[] xx = new double[20];
            double[] yy = new double[20];

            for (int i = 0; i < 20; i++)
            {
                xx[i] = i * 30;
                yy[i] = Math.Sin(i) * 200 + 200;
                //yy[i] = 100;
            }

            Pen greenPen = new Pen(Color.Green, 3); // Create pens.

            // Create points that define curve.
            Point point0 = new Point((int)xx[0], panel1.Height - (int)yy[0]);
            Point point1 = new Point((int)xx[1], panel1.Height - (int)yy[1]);
            Point point2 = new Point((int)xx[2], panel1.Height - (int)yy[2]);
            Point point3 = new Point((int)xx[3], panel1.Height - (int)yy[3]);
            Point point4 = new Point((int)xx[4], panel1.Height - (int)yy[4]);
            Point point5 = new Point((int)xx[5], panel1.Height - (int)yy[5]);
            Point point6 = new Point((int)xx[6], panel1.Height - (int)yy[6]);
            Point point7 = new Point((int)xx[7], panel1.Height - (int)yy[7]);
            Point point8 = new Point((int)xx[8], panel1.Height - (int)yy[8]);
            Point point9 = new Point((int)xx[9], panel1.Height - (int)yy[9]);
            Point point10 = new Point((int)xx[10], panel1.Height - (int)yy[10]);
            Point point11 = new Point((int)xx[11], panel1.Height - (int)yy[11]);
            Point point12 = new Point((int)xx[12], panel1.Height - (int)yy[12]);
            Point point13 = new Point((int)xx[13], panel1.Height - (int)yy[13]);
            Point point14 = new Point((int)xx[14], panel1.Height - (int)yy[14]);
            Point point15 = new Point((int)xx[15], panel1.Height - (int)yy[15]);
            Point point16 = new Point((int)xx[16], panel1.Height - (int)yy[16]);
            Point point17 = new Point((int)xx[17], panel1.Height - (int)yy[17]);
            Point point18 = new Point((int)xx[18], panel1.Height - (int)yy[18]);
            Point point19 = new Point((int)xx[19], panel1.Height - (int)yy[19]);

            Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14, point15, point16, point17, point18, point19 };

            g.DrawCurve(greenPen, curvePoints); //畫曲線

        }

        private void button15_Click(object sender, EventArgs e)
        {
            if (flag_Draw_circle == 0)
            {
                button15.BackColor = Color.Red;
                flag_Draw_circle = 1;
            }
            else
            {
                button15.BackColor = Color.Green;
                flag_Draw_circle = 0;
            }
        }

        private void button16_Click(object sender, EventArgs e)
        {
            if (flag_Draw_line == 0)
            {
                button16.BackColor = Color.Red;
                flag_Draw_line = 1;
            }
            else
            {
                button16.BackColor = Color.Green;
                flag_Draw_line = 0;
            }
        }

        private void button17_Click(object sender, EventArgs e)
        {
            if (flag_Draw_picture == 0)
            {
                button17.BackColor = Color.Red;
                flag_Draw_picture = 1;
            }
            else
            {
                button17.BackColor = Color.Green;
                flag_Draw_picture = 0;
            }
        }
    }
}
