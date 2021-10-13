using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for BitmapData
using System.Runtime.InteropServices;   //for Marshal

namespace vcs_ImageProcessingE
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";
            Image img = Image.FromFile(filename);
            pictureBox1.Image = img;


        }

        private void button1_Click(object sender, EventArgs e)
        {
            //灰階圖片處理1_Bitmap類


            //從pictureBox取得Bitmap
            Bitmap bitmap1 = (Bitmap)pictureBox1.Image;

            //提取像素法
            //使用的是GDI+中的Bitmap.GetPixel和Bitmap.SetPixel方法。

            if (bitmap1 != null)
            {
                Bitmap newbitmap = bitmap1.Clone() as Bitmap;
                Color pixel;
                int ret;
                for (int x = 0; x < newbitmap.Width; x++)
                {
                    for (int y = 0; y < newbitmap.Height; y++)
                    {
                        pixel = newbitmap.GetPixel(x, y);
                        ret = (int)(pixel.R * 0.299 + pixel.G * 0.587 + pixel.B * 0.114);
                        newbitmap.SetPixel(x, y, Color.FromArgb(ret, ret, ret));
                    }
                }
                pictureBox1.Image = newbitmap.Clone() as Image;
            }




        }

        private void button2_Click(object sender, EventArgs e)
        {
            //灰階圖片處理2_BitmapData類

            //從pictureBox取得Bitmap
            Bitmap bitmap1 = (Bitmap)pictureBox1.Image;


            //內存法

            //內存法是把圖像數據直接復制到內存中，這樣程序的運行速度就能大大提高了。

            if (bitmap1 != null)
            {
                Bitmap newbitmap = bitmap1.Clone() as Bitmap;
                Rectangle rect = new Rectangle(0, 0, newbitmap.Width, newbitmap.Height);
                BitmapData bmpdata = newbitmap.LockBits(rect, ImageLockMode.ReadWrite, newbitmap.PixelFormat);
                IntPtr ptr = bmpdata.Scan0;

                int bytes = newbitmap.Width * newbitmap.Height * 3;
                byte[] rgbvalues = new byte[bytes];

                Marshal.Copy(ptr, rgbvalues, 0, bytes);

                double colortemp = 0;
                for (int i = 0; i < rgbvalues.Length; i += 3)
                {
                    colortemp = rgbvalues[i + 2] * 0.299 + rgbvalues[i + 1] * 0.587 + rgbvalues[i] * 0.114;
                    rgbvalues[i] = rgbvalues[i + 1] = rgbvalues[i + 2] = (byte)colortemp;
                }

                Marshal.Copy(rgbvalues, 0, ptr, bytes);

                newbitmap.UnlockBits(bmpdata);
                pictureBox1.Image = newbitmap.Clone() as Image;
            }
        }
    }
}
