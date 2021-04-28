using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace my_plot
{
    public partial class Form1 : Form
    {
        int W = 0;
        int H = 0;
        int N = 30;
        Point[] pt_st;
        Point[] pt_sp;

        public Form1()
        {
            InitializeComponent();
        }


        private void Form1_Load(object sender, EventArgs e)
        {
            W = pictureBox1.Width;
            H = pictureBox1.Height;
            make_numbers();
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

        void make_numbers()
        {
            pt_st = new Point[N];
            pt_sp = new Point[N];

            int i;
            Random r = new Random();

            for (i = 0; i < N; i++)
            {
                pt_st[i].X = r.Next(W);
                pt_st[i].Y = r.Next(H);
            }

            int radius = 200;
            int theta = 0;
            bool flag_ok = false;
            for (i = 0; i < N; i++)
            {
                flag_ok = false;
                while (flag_ok == false)
                {
                    theta = r.Next(360);
                    pt_sp[i].X = pt_st[i].X + (int)(radius * cosd(theta));
                    pt_sp[i].Y = pt_st[i].Y + (int)(radius * sind(theta));
                    if ((pt_sp[i].X > 0) && (pt_sp[i].X < W) && (pt_sp[i].Y > 0) && (pt_sp[i].Y < H))
                    {
                        flag_ok = true;
                    }
                }
            }



            for (i = 0; i < N; i++)
            {
                richTextBox1.Text += pt_st[i].ToString() + "\n";
            }

            richTextBox1.Text += "\n\n";

            for (i = 0; i < N; i++)
            {
                richTextBox1.Text += pt_sp[i].ToString() + "\n";
            }




        }

        private void button1_Click(object sender, EventArgs e)
        {
            make_numbers();

            Graphics g = pictureBox1.CreateGraphics();
            g.Clear(Color.Pink);
            Pen p = new Pen(Color.Red, 3);
            int i;
            for (i = 0; i < N; i++)
            {
                g.DrawLine(p, pt_st[i], pt_sp[i]);

            }
        }
    }
}
