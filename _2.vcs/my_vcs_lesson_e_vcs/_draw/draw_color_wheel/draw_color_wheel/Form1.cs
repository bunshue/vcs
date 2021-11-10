using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace draw_color_wheel
{
    public partial class Form1 : Form
    {
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

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            Graphics g = this.pictureBox1.CreateGraphics();
            g.Clear(Color.White);

            int i = 0;
            int j = 0;
            int R = 0;
            int G = 0;
            int B = 0;
            int color_r_st;
            int color_r_sp;
            int color_g_st;
            int color_g_sp;
            int color_b_st;
            int color_b_sp;

            int cx = 200;
            int cy = 200;
            int r = 200;

            for (i = 0; i < 360; i += 1)
            {
                if (i < 60)
                {
                    color_r_st = 255;
                    color_g_st = 0;
                    color_b_st = 0;
                    color_r_sp = 255;
                    color_g_sp = 255;
                    color_b_sp = 0;
                }
                else if (i < 120)
                {
                    color_r_st = 255;
                    color_g_st = 255;
                    color_b_st = 0;
                    color_r_sp = 0;
                    color_g_sp = 255;
                    color_b_sp = 0;
                }
                else if (i < 180)
                {
                    color_r_st = 0;
                    color_g_st = 255;
                    color_b_st = 0;
                    color_r_sp = 0;
                    color_g_sp = 255;
                    color_b_sp = 255;
                }
                else if (i < 240)
                {
                    color_r_st = 0;
                    color_g_st = 255;
                    color_b_st = 255;
                    color_r_sp = 0;
                    color_g_sp = 0;
                    color_b_sp = 255;
                }
                else if (i < 300)
                {
                    color_r_st = 0;
                    color_g_st = 0;
                    color_b_st = 255;
                    color_r_sp = 255;
                    color_g_sp = 0;
                    color_b_sp = 255;
                }
                else
                {
                    color_r_st = 255;
                    color_g_st = 0;
                    color_b_st = 255;
                    color_r_sp = 255;
                    color_g_sp = 0;
                    color_b_sp = 0;
                }
                if (color_r_st == color_r_sp)
                {
                    R = color_r_st;
                }
                else
                {
                    j = i % 60;
                    R = color_r_st + (j * (color_r_sp - color_r_st) / 60);
                }
                if (color_g_st == color_g_sp)
                {
                    G = color_g_st;
                }
                else
                {
                    j = i % 60;
                    G = color_g_st + (j * (color_g_sp - color_g_st) / 60);
                }
                if (color_b_st == color_b_sp)
                {
                    B = color_b_st;
                }
                else
                {
                    j = i % 60;
                    B = color_b_st + (j * (color_b_sp - color_b_st) / 60);
                }

                Pen p = new Pen(Color.FromArgb(255, R, G, B), 2);

                g.DrawLine(p, cx, cy, cx + r * (float)cosd(i), cy + r * (float)sind(i));



                richTextBox1.Text += "i = " + i.ToString() + ", R = " + R.ToString() + ", G = " + G.ToString() + ", B = " + B.ToString() + "\n";
            }




        }
    }
}
