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

namespace vcs_webcam_1
{
    public partial class Form1 : Form
    {
        //全區域變數宣告
        //攝影機的變量
        private Capture cap;
        //判斷是否啟動webcam的frame旗標
        private bool _captureInProgress = false;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //預設使用第一台的webcam
            cap = new Capture(0);
            //cap = new Capture("D:\\aaaa.mp4");
            richTextBox1.Text += "Width = " + cap.Width.ToString() + "\n";
            richTextBox1.Text += "Height = " + cap.Height.ToString() + "\n";
            richTextBox1.Text += "FRAME_COUNT = " + cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FRAME_COUNT).ToString() + "\n";
            richTextBox1.Text += "FPS = " + cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FPS).ToString() + "\n";
            richTextBox1.Text += "FORMAT = " + cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FORMAT) + "\n";

        }


        void Application_Idle(object sender, EventArgs e)
        {
            Image<Bgr, Byte> frame = cap.QueryFrame();
            pictureBox1.Image = frame.ToBitmap();
        }

        //啟動webcam
        private void button1_Click(object sender, EventArgs e)
        {
            //如果webcam沒啟動
            if (cap == null)
            {
                try
                {
                    //打開預設的webcam
                    cap = new Capture();
                }
                catch (NullReferenceException excpt)
                {
                    MessageBox.Show(excpt.Message);
                }
            }

            //webcam啟動
            if (cap != null)
            {
                //frame啟動
                if (_captureInProgress)
                { //stop the capture
                    _captureInProgress = false;
                    button1.Text = "開始";
                    Application.Idle -= Application_Idle;
                }
                //frame關閉
                else
                {
                    //start the capture
                    _captureInProgress = true;
                    button1.Text = "結束";
                    Application.Idle += Application_Idle;
                }
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
            Image<Bgr, byte> temp = cap.QueryFrame();

            SaveFileDialog SaveFileDialog1 = new SaveFileDialog();
            SaveFileDialog1.FileName = DateTime.Now.ToString("yyyyMMddhhmmss");
            SaveFileDialog1.Filter = "Image Files(*.avi)|*.avi|All files (*.*)|*.*";
            if (SaveFileDialog1.ShowDialog() == DialogResult.OK)
            {
                MessageBox.Show("開始錄製，按ESC結束錄製");
            }

            VideoWriter video = new VideoWriter(SaveFileDialog1.FileName, CvInvoke.CV_FOURCC('X', 'V', 'I', 'D'), 20, 800, 600, true);

            while (temp != null)
            {
                CvInvoke.cvShowImage("camera", temp.Ptr);
                temp = cap.QueryFrame();
                int c = CvInvoke.cvWaitKey(20);
                video.WriteFrame<Bgr, byte>(temp);
                if (c == 27) break;
            }
            video.Dispose();
            CvInvoke.cvDestroyWindow("camera");

            //錄影完需將影像停止不然會出錯
            _captureInProgress = false;
            button1.Text = "開始";
            Application.Idle -= Application_Idle;
        }

        //關閉程式
        private void button3_Click(object sender, EventArgs e)
        {
            cap.Dispose();
            Application.Exit();

        }

        private void button4_Click(object sender, EventArgs e)
        {
            Image<Bgr, Byte> frame = cap.QueryFrame();
            //Image<Bgr, Byte> detected = faceDetection(frame);
            //确定保存路径
            SaveFileDialog SaveFileDialog1 = new SaveFileDialog();
            SaveFileDialog1.FileName = DateTime.Now.ToString("yyyyMMddhhmmss");
            SaveFileDialog1.Filter = "Image Files(*.JPG;*.GIF)|*.JPG;*.GIF|All files (*.*)|*.*";
            if (SaveFileDialog1.ShowDialog() == DialogResult.OK)
            {
                frame.Save(SaveFileDialog1.FileName); //保存
            }

        }



    }
}
