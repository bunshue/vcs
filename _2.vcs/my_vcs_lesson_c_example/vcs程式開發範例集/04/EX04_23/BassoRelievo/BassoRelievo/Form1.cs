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
        Image image;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            image = System.Drawing.Image.FromFile(filename);
            bitmap1 = new Bitmap(image);
            this.BackgroundImage = bitmap1;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            try
            {
                bitmap1 = new Bitmap(image);
                for (int i = 0; i < bitmap1.Width - 1; i++)
                {
                    for (int j = 0; j < bitmap1.Height - 1; j++)
                    {
                        Color Color1 = bitmap1.GetPixel(i, j);
                        Color Color2 = bitmap1.GetPixel(i + 1, j + 1);
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
                        bitmap1.SetPixel(i, j, Color.FromArgb(red, green, blue));
                    }
                }
                this.BackgroundImage = bitmap1;
            }
            catch { }
        }
    }
}