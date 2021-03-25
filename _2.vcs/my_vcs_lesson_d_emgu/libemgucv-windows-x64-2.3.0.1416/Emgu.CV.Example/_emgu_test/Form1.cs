using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using Emgu.CV;
using Emgu.CV.UI;
using Emgu.CV.Structure;
using Emgu.CV.CvEnum;
using Emgu.Util;


namespace _emgu_test
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\picture1.jpg";
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

            pictureBox1.Image = frame.ToBitmap(); // 把畫面轉換成bitmap型態，在丟給pictureBox元件
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
            //Image方法
            Image<Bgr, Byte> img = new Image<Bgr, byte>(320, 240, new Bgr(100, 0, 255));

            //Matrix

            //Mat方法 
            //Matrix img2 = new Matrix(200, 400, DepthType.Cv8U, 3);
            //img2.SetTo(new Bgr(255, 0, 0).MCvScalar);

            //imageBox1.Image = img;

            pictureBox1.Image = img.ToBitmap();


            //Mat B = new Mat(3, 1, Emgu.CV.CvEnum.DepthType.Cv64F, 1);


        
        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        private void button10_Click(object sender, EventArgs e)
        {
        }
    }
}
