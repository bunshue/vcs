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

namespace _EmguLoadImage0
{
    public partial class Form1 : Form
    {
        string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

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
            Image<Bgr, Byte> image = new Image<Bgr, byte>(filename);
            CvInvoke.cvShowImage("Image<Bgr, Byte>", image);

            //same
            /*
            pictureBox1.Load(filename);
            Image<Bgr, Byte> image2 = new Image<Bgr, Byte>((Bitmap)(pictureBox1.Image));
            CvInvoke.cvShowImage("Image<Bgr, Byte>", image2);
            */
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "用OpenCV開啟一個圖檔，並轉成灰階影像格式\n";
            //EmguCV 影像格式 Image<Gray, Byte>: 宣告一個EmguCV灰階影像格式
            Image<Gray, Byte> image = new Image<Gray, byte>(filename);     //彩色會自動轉灰階
            CvInvoke.cvShowImage("Image<Gray, Byte>", image);
            //內建判斷, 直接自動將輸入彩色的照片轉成灰階

            //same
            /*
            pictureBox1.Load(filename);
            Image<Gray, Byte> image2 = new Image<Gray, Byte>((Bitmap)(pictureBox1.Image));
            CvInvoke.cvShowImage("Image<Bgr, Byte>", image2);
            */
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "將PictureBox.Image轉型Bitmpap丟給Image\n";
            //輸入PictureBox 讀入影像, 將PictureBox.Image轉型Bitmpap丟給Image<Bgr, Byte>
            pictureBox1.Load(filename);
            Image<Bgr, Byte> image = new Image<Bgr, Byte>((Bitmap)(pictureBox1.Image));
            CvInvoke.cvShowImage("Image<Bgr, Byte>", image);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "開啟一張空的影像(黑底), 大小為 640 X 480\n";
            Image<Gray, Byte> image = new Image<Gray, byte>(new Size(640, 480));
            pictureBox1.Image = image.ToBitmap();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "自己定義一塊影像大小和像素值, 大小為 640 X 480\n";
            Image<Bgr, Byte> image = new Image<Bgr, byte>(640, 480, new Bgr(255, 0, 255)); //自定義顏色
            //Image<Bgr, Byte> image = new Image<Bgr, byte>(new Size(640, 480));    //黑色

            pictureBox1.Image = image.ToBitmap();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "利用Bitmap讀入一張圖片, 並傳給Image<Bgr, Byte>影像格式\n";
            Bitmap bmp = new Bitmap(filename);
            System.Drawing.Imaging.BitmapData bd;
            bd = bmp.LockBits(new Rectangle(0, 0, bmp.Width, bmp.Height),
                              System.Drawing.Imaging.ImageLockMode.ReadWrite,
                              System.Drawing.Imaging.PixelFormat.Format24bppRgb);
            Image<Bgr, Byte> image = new Image<Bgr, Byte>(bd.Width, bd.Height, bd.Stride, bd.Scan0);
            pictureBox1.Image = image.ToBitmap();
            bmp.UnlockBits(bd);
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //灰階0->255
            for (int i = 0; i < 256; i++)
            {
                Image<Gray, Byte> image = new Image<Gray, byte>(640, 480, new Gray(i));
                pictureBox1.Image = image.ToBitmap();
                this.Text = i.ToString();
                Application.DoEvents();
                Thread.Sleep(10);
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "用Image類別開啟一圖檔至picturebox\n";
            Image<Bgr, byte> img;
            img = new Image<Bgr, byte>(filename);
            //imageBox1.Image = img;
            pictureBox1.Image = img.ToBitmap();
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //各種Image類別處理
            Bitmap bitmap1 = new Bitmap(filename);
            TestRun(bitmap1);
        }

        public void TestRun(Bitmap bitmap)
        {
            int W = bitmap.Width;
            int H = bitmap.Height;
            Image<Bgr, Byte> img = new Image<Bgr, Byte>(bitmap);    //原圖
            Image<Gray, Byte> gray = img.Convert<Gray, Byte>().PyrDown().PyrUp();   //原圖轉灰階
            Image<Gray, Byte> gray1 = gray.ThresholdToZero(new Gray(100));      //灰階轉二值化
            //http://www.cnblogs.com/xrwang/archive/2010/03/03/ImageFeatureDetection.html.
            Image<Gray, Byte> gray2 = gray1.Canny(new Gray(150), new Gray(200));    //二值化轉Canny邊緣檢測

            Bitmap image = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            using (Graphics g = Graphics.FromImage(image))
            {
                Rectangle rct1 = new Rectangle(new Point(0, 0), new Size(W / 2, H / 2));
                g.DrawImage(img.Bitmap, rct1, new Rectangle(new Point(0, 0), new Size(W, H)), GraphicsUnit.Pixel);
                g.DrawRectangle(new Pen(Color.Black), rct1);

                Rectangle rct2 = new Rectangle(new Point(0, W / 2), new Size(W / 2, H / 2));
                g.DrawImage(gray.Bitmap, rct2, new Rectangle(new Point(0, 0), new Size(W, H)), GraphicsUnit.Pixel);
                g.DrawRectangle(new Pen(Color.Black), rct2);

                Rectangle rct3 = new Rectangle(new Point(H / 2, 0), new Size(W / 2, H / 2));
                g.DrawImage(gray1.Bitmap, rct3, new Rectangle(new Point(0, 0), new Size(W, H)), GraphicsUnit.Pixel);
                g.DrawRectangle(new Pen(Color.Black), rct3);

                Rectangle rct4 = new Rectangle(new Point(H / 2, W / 2), new Size(W / 2, H / 2));

                g.DrawImage(gray2.Bitmap, rct4, new Rectangle(new Point(0, 0), new Size(W, H)), GraphicsUnit.Pixel);
                g.DrawRectangle(new Pen(Color.Black), rct4);
            }
            pictureBox1.Image = image;
        }
    }
}
