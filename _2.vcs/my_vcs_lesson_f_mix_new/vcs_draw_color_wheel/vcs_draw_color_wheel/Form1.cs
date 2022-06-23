using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_draw_color_wheel
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox1.ClientSize = new Size(512, 512);
            pictureBox1.BorderStyle = BorderStyle.Fixed3D;

        }

        private void button1_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = new Bitmap(512, 512);

            int w = 512;
            int h = 512;
            int cx = 512 / 2;
            int cy = 512 / 2;
            int r = 256;
            int rx = 0;
            int ry = 0;
            int gx = 0;
            int gy = 0;
            int bx = 0;
            int by = 0;

            rx = cx + (int)(r * Math.Cos(0 - Math.PI / 2));
            ry = cy + (int)(r * Math.Sin(0 - Math.PI / 2));
            gx = cx + (int)(r * Math.Cos(0 - Math.PI / 2 + Math.PI * 2 / 3));
            gy = cy + (int)(r * Math.Sin(0 - Math.PI / 2 + Math.PI * 2 / 3));
            bx = cx + (int)(r * Math.Cos(0 - Math.PI / 2 + Math.PI * 4 / 3));
            by = cy + (int)(r * Math.Sin(0 - Math.PI / 2 + Math.PI * 4 / 3));

            int i;
            int j;
            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {
                    int dist = get_distance(i, j, cx, cy);
                    int distr = get_distance(i, j, rx, ry);
                    int distg = get_distance(i, j, gx, gy);
                    int distb = get_distance(i, j, bx, by);
                    /*
                    if (dist < 256)
                    {
                        bitmap1.SetPixel(i, j, Color.FromArgb(dist, 0, 0, dist));
                    }
                    else
                    {
                        bitmap1.SetPixel(i, j, Color.White);
                    }
                    */

                    //if ((distr <= distg) && (distr <= distb))
                    {
                        if (dist < 256)
                        {
                            if (distr > 255)
                                distr = 255;
                            if (distg > 255)
                                distg = 255;
                            if (distb > 255)
                                distb = 255;

                            bitmap1.SetPixel(i, j, Color.FromArgb(255, 255 - distr, 255 - distg, 255 - distb));
                        }

                    }


                }
            }
            
            pictureBox1.Image = bitmap1;


            richTextBox1.Text += "cx = " + cx.ToString() + ", cy = " + cy.ToString() + "\n";
            richTextBox1.Text += "rx = " + rx.ToString() + ", ry = " + ry.ToString() + "\n";
            richTextBox1.Text += "gx = " + gx.ToString() + ", gy = " + gy.ToString() + "\n";
            richTextBox1.Text += "bx = " + bx.ToString() + ", by = " + by.ToString() + "\n";


        }

        //計算兩點的距離
        private int get_distance(int p1x,int p1y,int p2x, int p2y)
        {
            int dx = p1x - p2x;
            int dy = p1y - p2y;
            return (int)(Math.Sqrt(dx * dx + dy * dy));
        }

    }
}

