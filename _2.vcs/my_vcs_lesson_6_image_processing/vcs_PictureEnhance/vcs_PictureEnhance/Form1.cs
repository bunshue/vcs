using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;

namespace vcs_PictureEnhance
{
    public partial class Form1 : Form
    {
        string filename1 = @"C:\______test_files\color1.bmp";
        string filename2 = @"C:\______test_files\color2.bmp";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox2.Image = Image.FromFile(filename1);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename1);	//Bitmap.FromFile出來的是Image格式
            Graphics g = Graphics.FromImage(bitmap1);
            //g.Clear(Color.White);

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";

            int x_st = W / 8;
            int y_st = H / 8;
            int w = W * 3 / 4;
            int h = H * 3 / 4;

            /*
            x_st = 1;
            y_st = 1;
            w = 20;
            h = 20;
            */

            int i;
            int j;

            Color pt;


            int total_R = 0;
            int total_G = 0;
            int total_B = 0;
            int R_max = 0;
            int R_min = 255;
            int G_max = 0;
            int G_min = 255;
            int B_max = 0;
            int B_min = 255;

            total_R = 0;
            total_G = 0;
            total_B = 0;
            R_max = 0;
            R_min = 255;
            G_max = 0;
            G_min = 255;
            B_max = 0;
            B_min = 255;

            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {
                    pt = bitmap1.GetPixel(x_st + i, y_st + j);
                    total_R += pt.R;
                    total_G += pt.G;
                    total_B += pt.B;

                    if (R_max < pt.R)
                        R_max = pt.R;
                    if (G_max < pt.G)
                        G_max = pt.G;
                    if (B_max < pt.B)
                        B_max = pt.B;
                    if (R_min > pt.R)
                        R_min = pt.R;
                    if (G_min > pt.G)
                        G_min = pt.G;
                    if (B_min > pt.B)
                        B_min = pt.B;
                }
            }

            richTextBox1.Text += "R1 = " + ((float)total_R / (w * h)).ToString("F2") + "\n";
            richTextBox1.Text += "G1 = " + ((float)total_G / (w * h)).ToString("F2") + "\n";
            richTextBox1.Text += "B1 = " + ((float)total_B / (w * h)).ToString("F2") + "\n";

            float R1 = ((float)total_R / (w * h));
            float G1 = ((float)total_G / (w * h));
            float B1 = ((float)total_B / (w * h));
            richTextBox1.Text += "(" + R1.ToString() + ", " + G1.ToString() + ", " + B1.ToString() + ")";

            richTextBox1.Text += "R_max = " + R_max.ToString() + "\tR_min = " + R_min.ToString() + "\n";
            richTextBox1.Text += "G_max = " + G_max.ToString() + "\tG_min = " + G_min.ToString() + "\n";
            richTextBox1.Text += "B_max = " + B_max.ToString() + "\tB_min = " + B_min.ToString() + "\n";




            int diff_R = R_max - R_min;
            int diff_G = G_max - G_min;
            int diff_B = B_max - B_min;

            if (diff_R == 0)
                diff_R = 1;
            if (diff_G == 0)
                diff_G = 1;
            if (diff_B == 0)
                diff_B = 1;

            float ratio_R = 255 / (float)diff_R;
            float ratio_G = 255 / (float)diff_G;
            float ratio_B = 255 / (float)diff_B;


            richTextBox1.Text += "ratio_R = " + ratio_R.ToString("F2") + "\n";
            richTextBox1.Text += "ratio_G = " + ratio_G.ToString("F2") + "\n";
            richTextBox1.Text += "ratio_B = " + ratio_B.ToString("F2") + "\n";


            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {
                    pt = bitmap1.GetPixel(x_st + i, y_st + j);

                    int R_new = (int)((pt.R - R_min) * ratio_R);
                    int G_new = (int)((pt.G - G_min) * ratio_G);
                    int B_new = (int)((pt.B - B_min) * ratio_B);


                    bitmap1.SetPixel(x_st + i, y_st + j, Color.FromArgb(255, R_new, G_new, B_new));

                }
            }



            total_R = 0;
            total_G = 0;
            total_B = 0;
            R_max = 0;
            R_min = 255;
            G_max = 0;
            G_min = 255;
            B_max = 0;
            B_min = 255;

            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {
                    pt = bitmap1.GetPixel(x_st + i, y_st + j);
                    total_R += pt.R;
                    total_G += pt.G;
                    total_B += pt.B;

                    if (R_max < pt.R)
                        R_max = pt.R;
                    if (G_max < pt.G)
                        G_max = pt.G;
                    if (B_max < pt.B)
                        B_max = pt.B;
                    if (R_min > pt.R)
                        R_min = pt.R;
                    if (G_min > pt.G)
                        G_min = pt.G;
                    if (B_min > pt.B)
                        B_min = pt.B;
                }
            }

            richTextBox1.Text += "R1 = " + ((float)total_R / (w * h)).ToString("F2") + "\n";
            richTextBox1.Text += "G1 = " + ((float)total_G / (w * h)).ToString("F2") + "\n";
            richTextBox1.Text += "B1 = " + ((float)total_B / (w * h)).ToString("F2") + "\n";


            richTextBox1.Text += "R_max = " + R_max.ToString() + "\tR_min = " + R_min.ToString() + "\n";
            richTextBox1.Text += "G_max = " + G_max.ToString() + "\tG_min = " + G_min.ToString() + "\n";
            richTextBox1.Text += "B_max = " + B_max.ToString() + "\tB_min = " + B_min.ToString() + "\n";



            pictureBox1.Image = bitmap1;
        }
    }
}
