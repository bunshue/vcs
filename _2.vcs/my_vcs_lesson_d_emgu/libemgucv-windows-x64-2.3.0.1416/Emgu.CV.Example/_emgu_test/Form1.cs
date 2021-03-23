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
                cap.Dispose();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (cap != null) cap.FlipHorizontal = !cap.FlipHorizontal;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (cap != null) cap.FlipVertical = !cap.FlipVertical;
        }




        public void TestRun(Bitmap bitmap)
        {
            Image<Bgr, Byte> img = new Image<Bgr, Byte>(bitmap);
            //灰階
            Image<Gray, Byte> gray = img.Convert<Gray, Byte>().PyrDown().PyrUp();
            //二值化
            Image<Gray, Byte> gray1 = gray.ThresholdToZero(new Gray(100));
            //http://www.cnblogs.com/xrwang/archive/2010/03/03/ImageFeatureDetection.html.
            //Canny算子也可以用作边缘检测
            Image<Gray, Byte> gray2 = gray1.Canny(new Gray(150), new Gray(200));

            int iiW = bitmap.Width;
            int iiH = bitmap.Height;
            Bitmap image = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            using (Graphics g = Graphics.FromImage(image))
            {
                Rectangle rct1 = new Rectangle(new Point(0, 0), new Size(iiW / 2, iiH / 2));
                g.DrawImage(img.Bitmap, rct1, new Rectangle(new Point(0, 0), new Size(iiW, iiH)), GraphicsUnit.Pixel);
                g.DrawRectangle(new Pen(Color.Black), rct1);

                Rectangle rct2 = new Rectangle(new Point(0, iiW / 2), new Size(iiW / 2, iiH / 2));
                g.DrawImage(gray.Bitmap, rct2, new Rectangle(new Point(0, 0), new Size(iiW, iiH)), GraphicsUnit.Pixel);
                g.DrawRectangle(new Pen(Color.Black), rct2);

                Rectangle rct3 = new Rectangle(new Point(iiH / 2, 0), new Size(iiW / 2, iiH / 2));
                g.DrawImage(gray1.Bitmap, rct3, new Rectangle(new Point(0, 0), new Size(iiW, iiH)), GraphicsUnit.Pixel);
                g.DrawRectangle(new Pen(Color.Black), rct3);

                Rectangle rct4 = new Rectangle(new Point(iiH / 2, iiW / 2), new Size(iiW / 2, iiH / 2));

                g.DrawImage(gray2.Bitmap, rct4, new Rectangle(new Point(0, 0), new Size(iiW, iiH)), GraphicsUnit.Pixel);
                g.DrawRectangle(new Pen(Color.Black), rct4);
            }
            pictureBox1.Image = image;

        }
 

        private void button4_Click(object sender, EventArgs e)
        {
            Bitmap bmp = new Bitmap(@"C:\______test_files\picture1.jpg");
            TestRun(bmp);
        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {

        }
    }
}