using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Draw_Wave
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {

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

        int x_st = 0;
        int y_st = 0;
        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            int W = 1024;
            int H = 256;
            int i;

            // Create pens.
            Pen redPen = new Pen(Color.Red, 4);
            Point[] curvePoints = new Point[W];    //一維陣列內有 W 個Point

            //畫紅色的分布
            for (i = 0; i < W; i++)
            {
                y_st = 256 * 1 - (int)(128 * (sind(x_st + i) + 1));
                //curvePoints[i].X = x_st;
                //curvePoints[i].Y = y_st;
                //richTextBox1.Text += y_st.ToString() + " ";
                //curvePoints[i].Y = 2 * i;

                if (y_st > 255)
                    y_st = 255;
                else if (y_st < 0)
                    y_st = 0;
                Pen p = new Pen(Color.Red, 1);
                p.Color = Color.FromArgb(y_st, y_st, y_st);
                e.Graphics.DrawLine(p, i, 0, i, 256);
            }
            //e.Graphics.DrawLines(redPen, curvePoints);   //畫直線
            x_st -= 5;

            for (i = 0; i < W; i++)
            {
                //richTextBox1.Text += c


            }

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            pictureBox1.Invalidate();
        }
    }
}
