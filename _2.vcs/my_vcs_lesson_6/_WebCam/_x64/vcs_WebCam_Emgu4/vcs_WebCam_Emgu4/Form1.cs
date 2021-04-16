using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using Emgu.CV;
using Emgu.CV.Structure;

namespace vcs_WebCam_Emgu4
{
    public partial class Form1 : Form
    {
        private Capture cap = null;             //宣告一個Webcam物件
        private Capture cap2 = null;
        private bool flag_webcam_ok = false;    //判斷是否啟動webcam的旗標

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

                                                                        void Application_Idle(object sender, EventArgs e)
                                                                        {
                                                                            Image<Bgr, Byte> image = cap.QueryFrame(); // Query WebCam 的畫面
                                                                            pictureBox1.Image = image.ToBitmap(); // 把畫面轉換成bitmap型態，再丟給pictureBox元件
                                                                        }

                                                                        private void button1_Click(object sender, EventArgs e)
                                                                        {
                                                                            if (flag_webcam_ok == false)
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
                                                                            else
                                                                            {
                                                                                richTextBox1.Text += "關閉Webcam ......\n";
                                                                                button1.Text = "開啟Webcam";
                                                                                flag_webcam_ok = false;
                                                                                pictureBox1.Image = null;

                                                                                Application.Idle -= new EventHandler(Application_Idle);
                                                                                cap.Dispose();
                                                                            }
                                                                        }


        private void button5_Click(object sender, EventArgs e)
        {
            //不 OK

            //string filename = "F:\\Naval Legends Yamato  World of Warships.mp4";
            //string filename = "C:\\______test_files\\胃カメラによる上部消化管検査 [720p].mp4";
            string filename = @"C:\______test_files\__RW\_avi\i2c.avi";

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

        //關閉程式
        private void bt_exit_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "離開 ......\n";

            if (flag_webcam_ok == true)
            {
                cap.Dispose();
                Application.Idle -= Application_Idle;
            }
            Application.Exit();
        }
    }
}

