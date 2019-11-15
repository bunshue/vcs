using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Mosaic
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\_case1\\pic1.jpg";

        Graphics g;
        Pen p;
        Bitmap bitmap1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bitmap1 = new Bitmap(filename);
            g = Graphics.FromImage(bitmap1);
            pictureBox1.Image = bitmap1;

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //馬賽克   TBD
            int block_size = 30;

            int i;
            int xx;
            int yy;
            int r_total = 0;
            int g_total = 0;
            int b_total = 0;
            byte rrr;
            byte ggg;
            byte bbb;

            for (yy = 0; yy < bitmap1.Height / 5; yy++)
            {
                for (xx = 0; xx < bitmap1.Width / 5; xx += 5)
                {
                    r_total = 0;
                    g_total = 0;
                    b_total = 0;

                    for (i = 0; i < block_size; i++)
                    {

                        rrr = bitmap1.GetPixel(xx + i, yy).R;
                        ggg = bitmap1.GetPixel(xx + i, yy).G;
                        bbb = bitmap1.GetPixel(xx + i, yy).B;
                        r_total += rrr;
                        g_total += ggg;
                        b_total += bbb;
                    }

                    Color zz = Color.FromArgb(255, (byte)(r_total / block_size), (byte)(g_total / block_size), (byte)(b_total / block_size));
                    for (i = 0; i < block_size; i++)
                    {
                        bitmap1.SetPixel(xx + i, yy, zz);
                    }
                }
            }

            pictureBox1.Image = bitmap1;

        }
    }
}
