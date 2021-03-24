//----------------------------------------------------------------------------
//  Copyright (C) 2004-2011 by EMGU. All rights reserved.       
//----------------------------------------------------------------------------

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using Emgu.CV;
using Emgu.CV.Structure;
using Emgu.Util;

namespace _emgu_test
{
    public partial class Form1 : Form
    {
        private Capture cap = null;             // Webcam物件
        private bool flag_webcam_ok = false;    //判斷是否啟動webcam的旗標

        public Form1()
        {
            InitializeComponent();
        }

        private void ProcessFrame(object sender, EventArgs arg)
        {
            Image<Bgr, Byte> frame = cap.QueryFrame();

            Image<Gray, Byte> grayFrame = frame.Convert<Gray, Byte>();
            Image<Gray, Byte> smallGrayFrame = grayFrame.PyrDown();
            Image<Gray, Byte> smoothedGrayFrame = smallGrayFrame.PyrUp();
            Image<Gray, Byte> cannyFrame = smoothedGrayFrame.Canny(new Gray(100), new Gray(60));

            //captureImageBox.Image = frame;
            //grayscaleImageBox.Image = grayFrame;
            //smoothedGrayscaleImageBox.Image = smoothedGrayFrame;
            //cannyImageBox.Image = cannyFrame;

            pictureBox1.Image = cannyFrame.ToBitmap(); // 把畫面轉換成bitmap型態，在丟給pictureBox元件
        }

        private void button1_Click(object sender, EventArgs e)
        {
            #region if capture is not created, create it now
            if (cap == null)
            {
                try
                {
                    cap = new Capture();
                }
                catch (NullReferenceException excpt)
                {
                    MessageBox.Show(excpt.Message);
                }
            }
            #endregion

            if (cap != null)
            {
                if (flag_webcam_ok)
                {  //stop the capture
                    button1.Text = "Start Capture";
                    Application.Idle -= ProcessFrame;
                }
                else
                {
                    //start the capture
                    button1.Text = "Stop";
                    Application.Idle += ProcessFrame;
                }

                flag_webcam_ok = !flag_webcam_ok;
            }
        }

        private void ReleaseData()
        {
            if (cap != null)
            {
                cap.Dispose();
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (cap != null)
            {
                cap.FlipHorizontal = !cap.FlipHorizontal;
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (cap != null)
            {
                cap.FlipVertical = !cap.FlipVertical;
            }
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

        private void button4_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = new Bitmap(@"C:\______test_files\picture1.jpg");
            TestRun(bitmap1);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";

            //EmguCV 影像格式 Image<Bgr, Byte>: a wrapper to IplImage of OpenCV
            Image<Bgr, Byte> inputImage = new Image<Bgr, byte>(filename);
            CvInvoke.cvShowImage("Image<Bgr, Byte>", inputImage);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";

            //3. EmguCV 影像格式 Image<Gray, Byte>: 宣告一個EmguCV灰階影像格式

            Image<Gray, Byte> inputImage = new Image<Gray, byte>(filename);
            CvInvoke.cvShowImage("Image<Gray, Byte>", inputImage);

            //內建判斷, 直接自動將輸入彩色的照片轉成灰階

        }

        private void button7_Click(object sender, EventArgs e)
        {
            //輸入PictureBox 讀入影像, 將PictureBox.Image轉型Bitmpap丟給Image<Bgr, Byte>

            string filename = @"C:\______test_files\picture1.jpg";

            pictureBox1.Load(filename);
            Image<Bgr, Byte> inputImage = new Image<Bgr, Byte>((Bitmap)(pictureBox1.Image));
            CvInvoke.cvShowImage("Image<Bgr, Byte>", inputImage);
        }

        private void button8_Click(object sender, EventArgs e)
        {
             //開啟一張空的影像(黑底), 大小為640X480

            Image<Gray, Byte> inputImage = new Image<Gray, byte>(new Size(640, 480));
            pictureBox1.Image = inputImage.ToBitmap();
        }

        private void button9_Click(object sender, EventArgs e)
        {
            // 自己定義一塊影像大小和像素值
            Image<Bgr, Byte> inputImage = new Image<Bgr, byte>(640, 480, new Bgr(255, 0, 255));
            pictureBox1.Image = inputImage.ToBitmap();
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //利用Bitmap讀入一張圖片, 並傳給Image<Bgr, Byte>影像格式

            string filename = @"C:\______test_files\picture1.jpg";

            Bitmap bmp = new Bitmap(filename);
            System.Drawing.Imaging.BitmapData bd;
            bd = bmp.LockBits(new Rectangle(0, 0, bmp.Width, bmp.Height),
                              System.Drawing.Imaging.ImageLockMode.ReadWrite,
                              System.Drawing.Imaging.PixelFormat.Format24bppRgb);
            Image<Bgr, Byte> inputImage = new Image<Bgr, Byte>(bd.Width, bd.Height, bd.Stride, bd.Scan0);
            pictureBox1.Image = inputImage.ToBitmap();
            bmp.UnlockBits(bd);

        }
    }
}
