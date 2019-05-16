using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Clock
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        Bitmap bmp;
        Graphics g;

        //int WIDTH = 150, HEIGHT = 150, secHAND = 70, minHAND = 55, hrHAND = 40;
        int WIDTH = 500, HEIGHT = 500;
        int secHAND = 70, minHAND = 55, hrHAND = 40;

        //center
        int cx, cy;

        private void Form1_Load(object sender, EventArgs e)
        {
            secHAND = 70 * WIDTH / 150;
            minHAND = 55 * WIDTH / 150;
            hrHAND = 40 * WIDTH / 150;

            pictureBox1.Size = new Size(WIDTH * 164 / 150, HEIGHT * 164 / 150);
            this.Size = new Size(WIDTH * 164 / 150 + 30, HEIGHT * 164 / 150 + 40);

            //create bitmap
            bmp = new Bitmap(WIDTH + 1, HEIGHT + 1);
            //center
            cx = WIDTH / 2;
            cy = HEIGHT / 2;
            timer1_Tick(sender, e);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            //create graphics
            g = Graphics.FromImage(bmp);


            //get time
            int ss = DateTime.Now.Second;
            int mm = DateTime.Now.Minute;
            int hh = DateTime.Now.Hour;

            int[] handCoord = new int[2];

            //clear
            g.Clear(Color.White);

            //draw circle
            g.DrawEllipse(new Pen(Color.Black, 1f), 0, 0, WIDTH, HEIGHT);

            //draw figure
            //g.DrawString("12", new Font("Arial", 12), Brushes.Black, new PointF(64, 1));
            //g.DrawString("3", new Font("Arial", 12), Brushes.Black, new PointF(138, 68));
            //g.DrawString("6", new Font("Arial", 12), Brushes.Black, new PointF(68, 133));
            //g.DrawString("9", new Font("Arial", 12), Brushes.Black, new PointF(0, 68));

            g.DrawString("12", new Font("Arial", 12), Brushes.Black, new PointF(64 * WIDTH / 150, 1 * HEIGHT / 150));
            g.DrawString("3", new Font("Arial", 12), Brushes.Black, new PointF(138 * WIDTH / 150, 68 * HEIGHT / 150));
            g.DrawString("6", new Font("Arial", 12), Brushes.Black, new PointF(68 * WIDTH / 150, 133 * HEIGHT / 150));
            g.DrawString("9", new Font("Arial", 12), Brushes.Black, new PointF(0 * WIDTH / 150, 68 * HEIGHT / 150));

            //second hand
            handCoord = msCoord(ss, secHAND);
            g.DrawLine(new Pen(Color.Red, 1f), new Point(cx, cy), new Point(handCoord[0], handCoord[1]));

            //minute hand
            handCoord = msCoord(mm, minHAND);
            g.DrawLine(new Pen(Color.Black, 2f), new Point(cx, cy), new Point(handCoord[0], handCoord[1]));

            //hour hand
            handCoord = hrCoord(hh % 12, mm, hrHAND);
            g.DrawLine(new Pen(Color.Gray, 3f), new Point(cx, cy), new Point(handCoord[0], handCoord[1]));

            //load bmp in picturebox1
            pictureBox1.Image = bmp;

            //disp time
            //this.Text = "Analog Clock -  " + hh + ":" + mm + ":" + ss;
            this.Text = "ims_Clock - " + hh + ":" + mm + ":" + ss;

            //dispose
            g.Dispose();


        }

        //coord for minute and second hand
        private int[] msCoord(int val, int hlen)
        {
            int[] coord = new int[2];
            val *= 6;   //each minute and second make 6 degree

            if (val >= 0 && val <= 180)
            {
                coord[0] = cx + (int)(hlen * Math.Sin(Math.PI * val / 180));
                coord[1] = cy - (int)(hlen * Math.Cos(Math.PI * val / 180));
            }
            else
            {
                coord[0] = cx - (int)(hlen * -Math.Sin(Math.PI * val / 180));
                coord[1] = cy - (int)(hlen * Math.Cos(Math.PI * val / 180));
            }
            return coord;
        }

        //coord for hour hand
        private int[] hrCoord(int hval, int mval, int hlen)
        {
            int[] coord = new int[2];

            //each hour makes 30 degree
            //each min makes 0.5 degree
            int val = (int)((hval * 30) + (mval * 0.5));

            if (val >= 0 && val <= 180)
            {
                coord[0] = cx + (int)(hlen * Math.Sin(Math.PI * val / 180));
                coord[1] = cy - (int)(hlen * Math.Cos(Math.PI * val / 180));
            }
            else
            {
                coord[0] = cx - (int)(hlen * -Math.Sin(Math.PI * val / 180));
                coord[1] = cy - (int)(hlen * Math.Cos(Math.PI * val / 180));
            }
            return coord;
        }

    }
}
