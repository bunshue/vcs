using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;
using System.Drawing.Imaging;

namespace BassoRelievo
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\picture1.jpg";

        Bitmap bitmap1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bitmap1 = new Bitmap(filename);
            pictureBox1.Image = bitmap1;
        }

        Bitmap BassoRelievo(Bitmap bmp)
        {
            try
            {
                for (int i = 0; i < bmp.Width - 1; i++)
                {
                    for (int j = 0; j < bmp.Height - 1; j++)
                    {
                        Color Color1 = bmp.GetPixel(i, j);
                        Color Color2 = bmp.GetPixel(i + 1, j + 1);
                        int red = Math.Abs(Color1.R - Color2.R + 128);
                        int green = Math.Abs(Color1.G - Color2.G + 128);
                        int blue = Math.Abs(Color1.B - Color2.B + 128);
                        //顏色處理
                        if (red > 255) red = 255;
                        if (red < 0) red = 0;

                        if (green > 255) green = 255;
                        if (green < 0) green = 0;

                        if (blue > 255) blue = 255;
                        if (blue < 0) blue = 0;
                        bmp.SetPixel(i, j, Color.FromArgb(red, green, blue));
                    }
                }
            }
            catch { }

            return bmp;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            bitmap1 = new Bitmap(filename);
            pictureBox1.Image = BassoRelievo(bitmap1);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            bitmap1 = new Bitmap(filename);
            pictureBox1.Image = bitmap1;
        }
    }
}
