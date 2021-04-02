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
        Bitmap myBitmap;
        Image myImage;
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            openFileDialog1.Filter = "*.jpg,*.jpeg,*.bmp|*.jpg;*.jpeg;*.bmp";
            openFileDialog1.ShowDialog();
            myImage = System.Drawing.Image.FromFile(openFileDialog1.FileName);
            myBitmap = new Bitmap(myImage);
            this.BackgroundImage = myBitmap;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            try
            {
                myBitmap = new Bitmap(myImage);
                for (int i = 0; i < myBitmap.Width - 1; i++)
                {
                    for (int j = 0; j < myBitmap.Height - 1; j++)
                    {
                        Color Color1 = myBitmap.GetPixel(i, j);
                        Color Color2 = myBitmap.GetPixel(i + 1, j + 1);
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
                        myBitmap.SetPixel(i, j, Color.FromArgb(red, green, blue));
                    }
                }
                this.BackgroundImage = myBitmap;
            }
            catch { }
        }
    }
}