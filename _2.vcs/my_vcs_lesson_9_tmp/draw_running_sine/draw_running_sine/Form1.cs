using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace draw_running_sine
{
    public partial class Form1 : Form
    {
        Bitmap bmp;
        Pen p;
        Graphics g;

        int t;


        int WIDTH = 720, HEIGHT = 300, AMPLITUDE = 150;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //create Bitmap
            bmp = new Bitmap(pictureBox1.Size.Width, pictureBox1.Size.Height);

            //background color
            //this.BackColor = Color.Black;

            //center
            //cx = WIDTH / 2;
            //cy = HEIGHT / 2;

            //initial degree of HAND
            //u = 0;

            //timer1.Enabled = true;
            t = 0;
            DrawXY();
            DrawYLine();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            //pen
            p = new Pen(Color.Green, 1f);

            //graphics
            g = Graphics.FromImage(bmp);

            int xx;
            int yy;

            xx = t;
            yy = HEIGHT - (int)(AMPLITUDE * Math.Sin(Math.PI * t / 180)) - AMPLITUDE;


            g.DrawEllipse(new Pen(Color.Red, 1f), xx, yy, 1, 1);

            //load bitmap in picturebox1
            pictureBox1.Image = bmp;


            //dispose
            p.Dispose();
            g.Dispose();

            t += 3;
            if (t >= 720)
                timer1.Enabled = false;

        }

        private void button1_Click(object sender, EventArgs e)
        {
            bmp = null;
            bmp = new Bitmap(pictureBox1.Size.Width, pictureBox1.Size.Height);
            pictureBox1.Image = null;
            t = 0;
            DrawXY();
            DrawYLine();
            timer1.Enabled = true;
        }

        private void DrawXY()//画X轴Y轴
        {
            //graphics
            g = Graphics.FromImage(bmp);
            System.Drawing.Point px1 = new System.Drawing.Point(this.pictureBox1.Width * 10 / 100, this.pictureBox1.Height * 90 / 100);
            System.Drawing.Point px2 = new System.Drawing.Point(this.pictureBox1.Width * 90 / 100, this.pictureBox1.Height * 90 / 100);
            g.DrawLine(new Pen(Brushes.Black, 5), px1, px2);
            System.Drawing.Point py1 = new System.Drawing.Point(this.pictureBox1.Width * 10 / 100, this.pictureBox1.Height * 90 / 100);
            System.Drawing.Point py2 = new System.Drawing.Point(this.pictureBox1.Width * 10 / 100, this.pictureBox1.Height * 10 / 100);
            g.DrawLine(new Pen(Brushes.Black, 5), py1, py2);
            g.Dispose();
        }

        private void DrawYLine()    //画X轴刻度
        {
            //graphics
            g = Graphics.FromImage(bmp);
            for (int i = 1; i < 9; i++)
            {
                System.Drawing.Point py1 = new System.Drawing.Point(100 * i, this.pictureBox1.Height - 5);
                System.Drawing.Point py2 = new System.Drawing.Point(100 * i, this.pictureBox1.Height);
                g.DrawLine(new Pen(Brushes.Red, 1), py1, py2);
            }
            g.Dispose();
        }


    }
}
