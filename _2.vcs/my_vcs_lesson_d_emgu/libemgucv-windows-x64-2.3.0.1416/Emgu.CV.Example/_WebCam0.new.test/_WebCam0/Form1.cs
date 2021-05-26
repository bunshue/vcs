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

namespace _WebCam0
{
    public partial class Form1 : Form
    {
        private Capture cap = null;             //宣告一個Webcam物件
        private bool flag_webcam_ok = false;    //判斷是否啟動webcam的旗標

        public Form1()
        {
            InitializeComponent();
        }

        void Application_Idle(object sender, EventArgs e)
        {
            Image<Bgr, Byte> image = cap.QueryFrame(); // Query WebCam 的畫面
            pictureBox1.Image = image.Not().ToBitmap(); // 把畫面轉換成bitmap型態，再丟給pictureBox元件

            /*  其他處理
            Image<Gray, Byte> grayFrame = image.Convert<Gray, Byte>();      //彩色轉灰階
            Image<Gray, Byte> smallGrayFrame = grayFrame.PyrDown();
            Image<Gray, Byte> smoothedGrayFrame = smallGrayFrame.PyrUp();
            Image<Gray, Byte> cannyFrame = smoothedGrayFrame.Canny(new Gray(100), new Gray(60));
            */
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (flag_webcam_ok == false)    //如果webcam沒啟動
            {
                try
                {
                    richTextBox1.Text += "開啟Webcam ......\n";
                    button1.Text = "關閉Webcam";
                    flag_webcam_ok = true;

                    cap = new Capture(0);   //預設使用第一台的webcam
                    //cap = new Capture("C:\\______test_files\\__RW\\_avi\\\i2c.avi");

                    //cap.FlipHorizontal = true;  //左右相反
                    //cap.FlipVertical = true;    //上下顛倒

                    richTextBox1.Text += "W = " + cap.Width.ToString() + ", ";
                    richTextBox1.Text += "H = " + cap.Height.ToString() + "\n";

                    Application.Idle += new EventHandler(Application_Idle); // 在Idle的event下，把畫面設定到pictureBox上

                    //  information
                    double W;
                    double H;
                    double frame_count;
                    double fps;
                    W = cap.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FRAME_WIDTH);
                    H = cap.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FRAME_HEIGHT);
                    frame_count = cap.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FRAME_COUNT);
                    fps = cap.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FPS);

                    richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";
                    richTextBox1.Text += "frame_count = " + frame_count.ToString() + "\n";
                    richTextBox1.Text += "fps = " + fps.ToString() + "\n";
                }
                catch (NullReferenceException excpt)
                {
                    MessageBox.Show(excpt.Message);
                }
            }
            else
            {
                richTextBox1.Text += "關閉Webcam ......\n";
                button1.Text = "開啟Webcam";
                flag_webcam_ok = false;
                pictureBox1.Image = null;
                Application.Idle -= new EventHandler(Application_Idle);
                cap.Dispose();
                cap = null;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (flag_webcam_ok == false)    //如果webcam沒啟動
                return;

            Image<Bgr, Byte> image = cap.QueryFrame(); // Query WebCam 的畫面


            richTextBox1.Text += "W = " + image.Width.ToString() + ", H = " + image.Height.ToString() + "\n";
            int i;
            int j;
            Bgr color = image[640 / 2, 480 / 2];


            Byte blue;
            Byte green;
            Byte red;


            //for (j = 100; j < 120; j++)
            {
                for (i = 0; i < 10; i++)
                {
                    /*
                    //richTextBox1.Text += image[0, i].Red.ToString() + " ";
                    //image[0, i].Red = 0;
                    //image[0, i, j] = color;
                    blue = image.Data[10, 10, 0];
                    green = image.Data[10, 10, 1];
                    red = image.Data[10, 10, 2];
                    */

                    //richTextBox1.Text += blue.ToString() + " " + green.ToString() + " " + red.ToString() + "|";

                }
            }

            pictureBox2.Image = image.ToBitmap(); // 把畫面轉換成bitmap型態，再丟給pictureBox元件



        }
    }
}
