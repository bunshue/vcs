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
            int i;
            int j;
            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {
                    double dist = Math.Sqrt((i - cx) * (i - cx) + (j - cy) * (j - cy));
                    if (dist < 256)
                    {
                        bitmap1.SetPixel(i, j, Color.FromArgb((int)dist, 0, 0, (int)dist));
                    }
                    else
                    {
                        bitmap1.SetPixel(i, j, Color.White);
                    }

                }
            }
            pictureBox1.Image = bitmap1;


        }
    }
}
