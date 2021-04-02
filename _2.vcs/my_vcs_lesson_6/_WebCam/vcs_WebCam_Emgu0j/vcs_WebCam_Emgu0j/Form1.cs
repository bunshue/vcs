using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
//需引用的Emgu
using Emgu.CV;
using Emgu.CV.Structure;
using Emgu.Util;
using System.Threading;
using Emgu.CV.CvEnum;

namespace vcs_WebCam_Emgu0j
{
    public partial class Form1 : Form
    {
        //攝影機的變量
        private Capture _capture;
        //判斷是否啟動webcam的frame旗標
        private bool _captureInProgress = false;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            _capture = new Capture(0);
        }

        void Application_Idle(object sender, EventArgs e)
        {
            Image<Bgr, Byte> frame = _capture.QueryFrame();
            pictureBox1.Image = frame.ToBitmap();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //如果webcam沒啟動
            if (_capture == null)
            {
                try
                {
                    //打開預設的webcam
                    _capture = new Capture();
                }
                catch (NullReferenceException excpt)
                {
                    MessageBox.Show(excpt.Message);
                }
            }

            //webcam啟動
            if (_capture != null)
            {
                //frame啟動
                if (_captureInProgress)
                {  //stop the capture
                    _captureInProgress = false;
                    button1.Text = "開始";
                    Application.Idle -= Application_Idle;
                }
                //frame關閉
                else
                {
                    //start the capture
                    _captureInProgress = true;
                    button1.Text = "结束";
                    Application.Idle += Application_Idle;
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            _capture = new Capture();
            if (_capture == null)
            {
                MessageBox.Show("can't find a camera", "error");
            }

            Image<Bgr, byte> temp = _capture.QueryFrame();

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
                temp = _capture.QueryFrame();
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

        private void button3_Click(object sender, EventArgs e)
        {
            _capture.Dispose();
            Application.Exit();
        }
    }
}
