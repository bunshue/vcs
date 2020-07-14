using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Draw8
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
