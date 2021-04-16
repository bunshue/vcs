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
using Emgu.Util;
using Emgu.CV.CvEnum;

using System.Threading;

namespace vcs_WebCam_Emgu3
{
    public partial class Form1 : Form
    {
        private Capture cap = null;             //宣告一個Webcam物件
        private bool flag_webcam_ok = false;    //判斷是否啟動webcam的旗標

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
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

        //錄製影像
        private void button2_Click(object sender, EventArgs e)
        {
            cap = new Capture();
            double fourcc = cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FOURCC);

            if (cap == null)
            {
                MessageBox.Show("can't find a camera", "error");
            }
            Image<Bgr, Byte> image = cap.QueryFrame(); // Query WebCam 的畫面

            SaveFileDialog SaveFileDialog1 = new SaveFileDialog();
            SaveFileDialog1.FileName = DateTime.Now.ToString("yyyyMMddhhmmss");
            SaveFileDialog1.Filter = "Image Files(*.avi)|*.avi|All files (*.*)|*.*";
            if (SaveFileDialog1.ShowDialog() == DialogResult.OK)
            {
                MessageBox.Show("開始錄製，按ESC結束錄製");
            }

            VideoWriter video = new VideoWriter(SaveFileDialog1.FileName, CvInvoke.CV_FOURCC('X', 'V', 'I', 'D'), 20, 800, 600, true);

            while (image != null)
            {
                CvInvoke.cvShowImage("camera", image.Ptr);
                image = cap.QueryFrame(); // Query WebCam 的畫面
                int c = CvInvoke.cvWaitKey(20);
                video.WriteFrame<Bgr, byte>(image);
                if (c == 27) break;
            }
            video.Dispose();
            CvInvoke.cvDestroyWindow("camera");

            //錄影完需將影像停止不然會出錯
            flag_webcam_ok = false;
            button1.Text = "開始";
            Application.Idle -= Application_Idle;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //關閉程式
            if (cap != null)
            {
                cap.Dispose();
            }
            Application.Exit();
        }
    }
}
