using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

using Emgu.CV;
using Emgu.CV.Structure;

namespace vcs_WebCam_Emgu0k
{
    public partial class Form1 : Form
    {
        bool flag_webcam_ok = false;
        private Capture cap = null;
        private Capture cap2 = null;

        public Form1()
        {
            InitializeComponent();
        }

        void Application_Idle(object sender, EventArgs e)
        {
            Image<Bgr, Byte> image = cap.QueryFrame();
            pictureBox1.Image = image.ToBitmap();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (flag_webcam_ok == false)
            {
                richTextBox1.Text += "開啟Webcam ......\n";
                button1.Text = "關閉Webcam";
                flag_webcam_ok = true;

                cap = new Capture(0);   //預設使用第一台的webcam
                //cap = new Capture("C:\\______test_files\\aaaa.mp4");
                Application.Idle += new EventHandler(Application_Idle);
            }
            else
            {
                richTextBox1.Text += "關閉Webcam ......\n";
                button1.Text = "開啟Webcam";
                flag_webcam_ok = false;

                Application.Idle -= new EventHandler(Application_Idle);
                cap.Dispose();
            }
        }

        //截圖
        private void button2_Click(object sender, EventArgs e)
        {
            if (flag_webcam_ok == false)
            {
                richTextBox1.Text += "尚未開啟webcam\n";
                return;
            }

            richTextBox1.Text += "截圖\t\t";

            //  截圖  Query 攝影機的畫面
            Image<Bgr, Byte> image = cap.QueryFrame();

            string filename = Application.StartupPath + "\\image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

            try
            {
                image.Save(filename);   //儲存影像
                richTextBox1.Text += "已存檔 : " + filename + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
        }

        //離開
        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "離開 ......\n";

            if (flag_webcam_ok == true)
            {
                cap.Dispose();
            }

            Application.Exit();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (flag_webcam_ok == true)
            {
                double W;
                double H;
                double frame_count;
                double fps;

                W = cap.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FRAME_WIDTH);
                H = cap.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FRAME_HEIGHT);
                frame_count = cap.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FRAME_COUNT);
                fps = cap.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FPS);

                richTextBox1.Text += "FRAME_WIDTH = " + W.ToString() + "\n";
                richTextBox1.Text += "FRAME_HEIGHT = " + H.ToString() + "\n";
                richTextBox1.Text += "FRAME_COUNT = " + frame_count.ToString() + "\n";
                richTextBox1.Text += "FPS = " + fps.ToString() + "\n";
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            string filename = "F:\\Naval Legends Yamato  World of Warships.mp4";

            //Capture cap2 = null;
            cap2 = new Capture(filename);

            double W;
            double H;
            double frame_count;
            double fps;

            W = cap2.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FRAME_WIDTH);
            H = cap2.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FRAME_HEIGHT);
            frame_count = cap2.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FRAME_COUNT);
            fps = cap2.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FPS);

            richTextBox1.Text += "FRAME_WIDTH = " + W.ToString() + "\n";
            richTextBox1.Text += "FRAME_HEIGHT = " + H.ToString() + "\n";
            richTextBox1.Text += "FRAME_COUNT = " + frame_count.ToString() + "\n";
            richTextBox1.Text += "FPS = " + fps.ToString() + "\n";

            double sec = frame_count / fps;
            if (sec > 60)
                richTextBox1.Text += "duration = " + ((int)(sec / 60)).ToString() + " 分 " + (sec % 60).ToString() + " 秒\n";
            else
                richTextBox1.Text += "duration = " + sec.ToString() + " 秒\n";

            /*
            //test
            Image<Bgr, Byte> image = cap2.QueryFrame();
            pictureBox1.Image = image.ToBitmap();
            */


            filename = @"C:\______test_files\picture1.jpg";
            cap2 = new Capture(filename);

            W = cap2.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FRAME_WIDTH);
            H = cap2.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FRAME_HEIGHT);
            frame_count = cap2.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FRAME_COUNT);
            fps = cap2.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FPS);

            richTextBox1.Text += "FRAME_WIDTH = " + W.ToString() + "\n";
            richTextBox1.Text += "FRAME_HEIGHT = " + H.ToString() + "\n";
            richTextBox1.Text += "FRAME_COUNT = " + frame_count.ToString() + "\n";
            richTextBox1.Text += "FPS = " + fps.ToString() + "\n";

            Image<Bgr, Byte> image = cap2.QueryFrame();
            pictureBox1.Image = image.ToBitmap();

        }
    }
}
