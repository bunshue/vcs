using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;

using AForge.Video;             //需要添加這兩個.dll, 參考/加入參考/瀏覽此二檔
using AForge.Video.DirectShow;  // Video Recording
//using AForge.Video.FFMPEG;      //for VideoFileWriter
using AForge.Vision.Motion;     // Motion detection

/*
參考
【AForge.NET】C#上使用AForge.Net擷取視訊畫面
https://ccw1986.blogspot.com/2013/01/ccaforgenetcapture-image.html

AForge下載鏈結
http://www.aforgenet.com/framework/downloads.html

Aforge.Net 安裝路徑設定
Solution Explorer(方案總管) => References(參考)(右鍵) => Add Reference(加入參考) => AForge.Net的Release資料夾
加入AForge.Video.dll、AForge.Video.DirectShow.dll

移動偵測 需要 參考/加入參考/選取以下3個dll
AForge.dll
AForge.Imaging.dll
AForge.Vision.dll
 */

namespace vcs_WebCam4_MotionDetection
{
    public partial class Form1 : Form
    {
        private FilterInfoCollection USBWebcams = null;
        private VideoCaptureDevice Cam = null;
        MotionDetector motion_detector;

        private const int BORDER = 10;
        private const int W_pictureBox1 = 640;
        private const int H_pictureBox1 = 480;
        private const int W_richTextBox1 = 300;
        private const int H_richTextBox1 = 480 - 60;

        bool flag_motion_detection = false;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            Init_WebcamSetup();
            Start_Webcam();
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            //Stop_Webcam();
            if (Cam != null)
            {
                if (Cam.IsRunning)  // When Form1 closes itself, WebCam must stop, too.
                {
                    Cam.Stop();   // WebCam stops capturing images.
                    Cam.SignalToStop();
                    Cam.WaitForStop();
                }
            }
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            pictureBox1.Size = new Size(W_pictureBox1, H_pictureBox1);
            pictureBox1.Location = new Point(BORDER, BORDER);

            richTextBox1.Size = new Size(W_richTextBox1, H_richTextBox1);
            richTextBox1.Location = new Point(BORDER + W_pictureBox1 + BORDER, BORDER + BORDER + 50);
            bt_motion_detection.Location = new Point(BORDER + W_pictureBox1 + BORDER, BORDER + BORDER);

            int w = BORDER + W_pictureBox1 + BORDER + W_richTextBox1 + BORDER;
            int h = BORDER + H_pictureBox1 + BORDER;
            this.ClientSize = new Size(w, h);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void Init_WebcamSetup()
        {
            USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice); //實例化對象
            if (USBWebcams.Count > 0)
            {
                string camera_name = USBWebcams[0].MonikerString;   //長名
                //this.CamMonitor = new CameraMonitor(pictureBox1, camera_name, "第 1 台攝影機");
                //flag_webcam_ok = true;
            }

            USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice); //實例化對象
            if (USBWebcams.Count > 0)  // The quantity of WebCam must be more than 0.
            {
                Cam = new VideoCaptureDevice(USBWebcams[0].MonikerString);  //實例化對象

                Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);
                Cam.Start();   // WebCam starts capturing images.

                motion_detector = new MotionDetector(new TwoFramesDifferenceDetector(), new MotionAreaHighlighting()); // creates the motion detector

                /*
                //以下為WebCam訊息與調整視窗大小
                Cam.VideoResolution = Cam.VideoCapabilities[0];
                string webcam_name = string.Empty;
                int ww;
                int hh;
                ww = Cam.VideoCapabilities[0].FrameSize.Width;
                hh = Cam.VideoCapabilities[0].FrameSize.Height;
                webcam_name = USBWebcams[0].Name + " " + Cam.VideoCapabilities[0].FrameSize.Width.ToString() + " X " + Cam.VideoCapabilities[0].FrameSize.Height.ToString() + " @ " + Cam.VideoCapabilities[0].AverageFrameRate.ToString() + " Hz";
                this.Text = webcam_name;
                //有抓到WebCam, 重新設定pictureBox的大小和位置
                pictureBox1.Size = new Size(ww, hh);
                pictureBox1.Location = new Point(BORDER, BORDER);
                */
            }
            else
            {
                this.Text = "無影像裝置";
            }
        }

        bool motionDetected = false;

        // different option toggles
        public bool RecordOnMotion = false;
        public bool BeepOnMotion = false;
        public bool MotionDetection = false;
        public bool forceRecord = false;

        private void MotionReaction()
        {
            this.motionDetected = true;

            if (this.BeepOnMotion == true)
            {
                // beep if BeepOnMotion is toggeled
                System.Console.Beep(400, 500);
                System.Console.Beep(800, 500);
            }

            Thread.Sleep(10000); // the user is notified for 10 seconds
            calibrateAndResume = 0;
            this.motionDetected = false;
            Thread.Sleep(3000);
        }

        int calibrateAndResume = 0; // counter used delay/skip frames from being processed by the MotionDetector

        public Bitmap bm = null;
        //自定義函數, 捕獲每一幀圖像並顯示
        void Cam_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            //pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();
            bm = (Bitmap)eventArgs.Frame.Clone();
            //bm.RotateFlip(RotateFlipType.RotateNoneFlipY);    //反轉
            pictureBox1.Image = bm;

            if (flag_motion_detection == true)
            {
                // if motion detection is enabled and there werent any previous motion detected
                Bitmap bitmap2 = (Bitmap)bm.Clone(); // clone the bits from the current frame

                if (motion_detector.ProcessFrame(bitmap2) > 0.001) // feed the bits to the MD 
                {
                    if (this.calibrateAndResume > 3)
                    {
                        // if motion was detected in 3 subsequent frames
                        Thread th = new Thread(MotionReaction);
                        th.Start(); // start the motion reaction thread
                    }
                    else
                    {
                        this.calibrateAndResume++;
                    }
                }

            }

            GC.Collect();       //回收資源
        }

        private void bt_motion_detection_Click(object sender, EventArgs e)
        {
            if (flag_motion_detection == false)
            {
                flag_motion_detection = true;
                richTextBox1.Text += "啟動 移動偵測\n";
                bt_motion_detection.Text = "停止 移動偵測";
            }
            else
            {
                flag_motion_detection = false;
                richTextBox1.Text += "停止 移動偵測\n";
                bt_motion_detection.Text = "啟動 移動偵測";
            }
        }
    }
}

