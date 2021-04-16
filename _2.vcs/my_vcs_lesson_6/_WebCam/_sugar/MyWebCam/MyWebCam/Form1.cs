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
using Emgu.CV.CvEnum;


namespace MyWebCam
{
    public partial class Form1 : Form
    {
        // Webcam物件
        private Capture cap = null;                
        //判斷是否啟動webcam的frame旗標
        private bool _captureInProgress = false;

        bool _isRecording = false;
        string _movieDirectory = @"d:\Test\movies\";
        string _fileName;
        Timer _timer;
        VideoWriter video;

        public Form1()
        {
            InitializeComponent();

            //宣告Timer 0.1秒執行一次
            _timer = new Timer();
            _timer.Interval = 100;
            _timer.Tick += new EventHandler(TimerEventProcessor);
        }

        private void TimerEventProcessor(object sender, EventArgs e)
        {
            Image<Bgr, Byte> frame = cap.QueryFrame(); // Query 攝影機的畫面

            pictureBox1.Image = frame.ToBitmap(); // 把畫面轉換成bitmap型態，在丟給pictureBox元件

            //錄影模式
            if (_isRecording)
            {
                //將影格寫入影片中
                video.WriteFrame<Bgr, byte>(frame);
            }
        }


        private void button1_Click(object sender, EventArgs e)
        {
            openWebCam();

            //webcam啟動
            if (cap != null)
            {
                //frame啟動
                if (_captureInProgress)
                {
                    //stop the capture
                    _captureInProgress = false;
                    button1.Text = "開啟";
                    _timer.Stop();
                }
                //frame關閉
                else
                {
                    //start the capture
                    _captureInProgress = true;
                    button1.Text = "關閉";
                    _timer.Start();
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
                openWebCam();

                _timer.Start();

                _fileName = string.Format("{0}{1}{2}", _movieDirectory, DateTime.Now.ToString("yyyyMMddHmmss"), ".avi");

                //cap.Width 取得攝影機可支援的最大寬度
                //cap.Height 取得攝影機可支援的最大高度
                video = new VideoWriter(_fileName, 0, 10, cap.Width, cap.Height, true);

                //開啟錄影模式
                _isRecording = true;

        }

        private void button3_Click(object sender, EventArgs e)
        {            
            //錄影完需將影像停止不然會出錯
            _isRecording = false;
            video.Dispose();

        }

        /// <summary>
        /// 開啟攝影機
        /// </summary>
        private void openWebCam()
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
        
        }

    }
}
