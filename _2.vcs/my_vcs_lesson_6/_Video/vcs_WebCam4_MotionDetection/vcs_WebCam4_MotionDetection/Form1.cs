using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;

using AForge.Video;  // 需要添加這兩個.dll, 參考/右鍵/加入參考/瀏覽 此二檔 AForge.Video.dll和AForge.Video.DirectShow.dll
using AForge.Video.DirectShow;
using AForge.Vision.Motion;  // Motion detection

namespace vcs_WebCam4_MotionDetection  // 標準 移動偵測
{
    public partial class Form1 : Form
    {
        private FilterInfoCollection USBWebcams = null;
        private VideoCaptureDevice Cam = null;

        MotionDetector motion_detector;
        bool flag_motion_detection = false;
        bool motionDetected = false; // was there any motion detected previously
        int calibrateAndResume = 0; // counter used delay/skip frames from being processed by the MotionDetector

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //C# 跨 Thread 存取 UI
            //Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效	same
            Control.CheckForIllegalCrossThreadCalls = false;//忽略跨執行緒錯誤

            //影像加上訊息
            pictureBox1.Paint += new PaintEventHandler(DrawMessage);

            Init_WebcamSetup();

            Start_Webcam();
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

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

        // 最小化WebCam設定
        void Init_WebcamSetup()
        {
            USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice);  // 實例化對象
            if (USBWebcams.Count > 0)
            {
                Cam = new VideoCaptureDevice(USBWebcams[0].MonikerString);  // 實例化對象, 長名
                Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);

                //初始化motion detector
                motion_detector = new MotionDetector(new TwoFramesDifferenceDetector(), new MotionAreaHighlighting());
            }
            else
            {
                this.Text = "無影像裝置";
            }
        }

        //影像加上訊息
        private void DrawMessage(object sender, PaintEventArgs e)
        {
            using (Font f = new Font("Arial", 18, FontStyle.Bold))
            {
                string str = string.Empty;
                SolidBrush sb;
                if (this.motionDetected == true)
                {
                    str = DateTime.Now.ToString() + " 移動偵測";
                    sb = new SolidBrush(Color.Red);
                    e.Graphics.DrawRectangle(new Pen(Color.Red, 10), 5, 5, 640 - 10, 480 - 10);
                }
                else
                {
                    str = DateTime.Now.ToString();
                    sb = new SolidBrush(Color.Green);
                }
                e.Graphics.DrawString(str, f, sb, new Point(10, 10));
            }
        }

        //自定義函數, 捕獲每一幀圖像並顯示
        void Cam_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            Bitmap bitmap1 = (Bitmap)eventArgs.Frame.Clone(); // get a copy of the BitMap from the VideoCaptureDevice
            pictureBox1.Image = (Bitmap)bitmap1.Clone(); // displays the current frame on the main form

            //做移動偵測
            if ((this.flag_motion_detection == true) && (this.motionDetected == false))
            {
                // if motion detection is enabled and there werent any previous motion detected
                Bitmap bitmap2 = (Bitmap)bitmap1.Clone(); // clone the bits from the current frame

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
        }

        private void MotionReaction()
        {
            richTextBox1.Text += "偵測到移動 警示5秒\n";

            this.motionDetected = true;

            Thread.Sleep(5000); // 警示 5 秒

            calibrateAndResume = 0;
            this.motionDetected = false;
        }

        void Start_Webcam()
        {
            if (Cam != null)
            {
                Cam.Start();   // WebCam starts capturing images.
            }
        }

        void Stop_Webcam()
        {
            if (Cam != null)
            {
                Cam.Stop();
                Cam.SignalToStop();
                Cam.WaitForStop();
                while (Cam.IsRunning)
                {
                    Console.Write("等候相機關閉");
                }
                Cam = null;
            }
            pictureBox1.Image = null;
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

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個


// Stop_Webcam();

