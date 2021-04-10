using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.Threading;

using Emgu.CV;
using Emgu.CV.Structure;
using Emgu.Util;
using Emgu.CV.CvEnum;

namespace _EmguLoadImage
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\picture1.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "用OpenCV開啟一個圖檔\n";
            IntPtr inputImage = CvInvoke.cvLoadImage(filename, LOAD_IMAGE_TYPE.CV_LOAD_IMAGE_COLOR);
            CvInvoke.cvShowImage("IntPtr", inputImage);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "用OpenCV開啟一個圖檔\n";
            //EmguCV 影像格式 Image<Bgr, Byte>: a wrapper to IplImage of OpenCV
            Image<Bgr, Byte> inputImage = new Image<Bgr, byte>(filename);
            CvInvoke.cvShowImage("Image<Bgr, Byte>", inputImage);

            //same
            /*
            pictureBox1.Load(filename);
            Image<Bgr, Byte> inputImage2 = new Image<Bgr, Byte>((Bitmap)(pictureBox1.Image));
            CvInvoke.cvShowImage("Image<Bgr, Byte>", inputImage2);
            */
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "用OpenCV開啟一個圖檔，並轉成灰階影像格式\n";
            //EmguCV 影像格式 Image<Gray, Byte>: 宣告一個EmguCV灰階影像格式
            Image<Gray, Byte> inputImage = new Image<Gray, byte>(filename);     //彩色會自動轉灰階
            CvInvoke.cvShowImage("Image<Gray, Byte>", inputImage);
            //內建判斷, 直接自動將輸入彩色的照片轉成灰階

            //same
            /*
            pictureBox1.Load(filename);
            Image<Gray, Byte> inputImage2 = new Image<Gray, Byte>((Bitmap)(pictureBox1.Image));
            CvInvoke.cvShowImage("Image<Bgr, Byte>", inputImage2);
            */
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "將PictureBox.Image轉型Bitmpap丟給Image\n";
            //輸入PictureBox 讀入影像, 將PictureBox.Image轉型Bitmpap丟給Image<Bgr, Byte>
            pictureBox1.Load(filename);
            Image<Bgr, Byte> inputImage = new Image<Bgr, Byte>((Bitmap)(pictureBox1.Image));
            CvInvoke.cvShowImage("Image<Bgr, Byte>", inputImage);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "開啟一張空的影像(黑底), 大小為 640 X 480\n";
            Image<Gray, Byte> inputImage = new Image<Gray, byte>(new Size(640, 480));
            pictureBox1.Image = inputImage.ToBitmap();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "自己定義一塊影像大小和像素值, 大小為 640 X 480\n";
            Image<Bgr, Byte> inputImage = new Image<Bgr, byte>(640, 480, new Bgr(255, 0, 255)); //自定義顏色
            //Image<Bgr, Byte> inputImage2 = new Image<Bgr, byte>(new Size(640, 480));    //黑色

            pictureBox1.Image = inputImage.ToBitmap();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "利用Bitmap讀入一張圖片, 並傳給Image<Bgr, Byte>影像格式\n";
            Bitmap bmp = new Bitmap(filename);
            System.Drawing.Imaging.BitmapData bd;
            bd = bmp.LockBits(new Rectangle(0, 0, bmp.Width, bmp.Height),
                              System.Drawing.Imaging.ImageLockMode.ReadWrite,
                              System.Drawing.Imaging.PixelFormat.Format24bppRgb);
            Image<Bgr, Byte> inputImage = new Image<Bgr, Byte>(bd.Width, bd.Height, bd.Stride, bd.Scan0);
            pictureBox1.Image = inputImage.ToBitmap();
            bmp.UnlockBits(bd);
        }

        private void button8_Click(object sender, EventArgs e)
        {
            bool flag_increase = false;
            for (int j = 0; j < 10; j++)
            {
                for (int i = 0; i < 256; i++)
                {
                    Image<Gray, Byte> inputImage;
                    if (flag_increase == false)
                    {
                        inputImage = new Image<Gray, byte>(640, 480, new Gray(i));
                    }
                    else
                    {
                        inputImage = new Image<Gray, byte>(640, 480, new Gray(255 - i));
                    }
                    pictureBox1.Image = inputImage.ToBitmap();
                    Application.DoEvents();
                    Thread.Sleep(10);
                }
                flag_increase = !flag_increase;
            }
        }
    }
}
