using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;
using System.Drawing.Imaging;   //for ImageFormat

using AForge.Video;             //需要添加這兩個.dll, 參考/右鍵/加入參考/瀏覽 此二檔 AForge.Video.dll和AForge.Video.DirectShow.dll
using AForge.Video.DirectShow;
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

namespace vcs_WebCam4_MotionDetection  // 標準 移動偵測
{
    public partial class Form1 : Form
    {
        private FilterInfoCollection USBWebcams = null;
        private VideoCaptureDevice Cam = null; // refrence to the actual VidioCaptureDevice (webcam)
        MotionDetector motion_detector;

        private const int BORDER = 10;

        bool flag_motion_detection = false;

        bool motionDetected = false; // was there any motion detected previously
        int calibrateAndResume = 0; // counter used delay/skip frames from being processed by the MotionDetector

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
            int W = 640;
            int H = 480;
            int x_st = BORDER;
            int y_st = BORDER;
            int dx = W + 50;
            int dy = H + 50;

            pictureBox1.Size = new Size(W, H);

            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_motion_detection.Location = new Point(x_st + W + BORDER, 10);
            richTextBox1.Size = new Size(250, H - 40);
            richTextBox1.Location = new Point(x_st + W + BORDER, 50);

            this.ClientSize = new Size(W + 250 + BORDER * 3, H + BORDER * 2);
        }

        void Init_WebcamSetup() //最小化WebCam設定
        {
            USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice); //實例化對象
            if (USBWebcams.Count > 0)
            {
                Cam = new VideoCaptureDevice(USBWebcams[0].MonikerString);//長名
                Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame); // defines which method to call when a new frame arrives

                this.pictureBox1.Paint += new PaintEventHandler(DrawMessage);

                //初始化motion detector
                motion_detector = new MotionDetector(new TwoFramesDifferenceDetector(), new MotionAreaHighlighting());
            }
            else
            {
                this.Text = "無影像裝置";
            }
        }

        private void DrawMessage(object sender, PaintEventArgs e)
        {
            using (Font f = new Font("Arial", 14, FontStyle.Bold))
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
            this.motionDetected = true;

            Thread.Sleep(10000); // the user is notified for 10 seconds
            calibrateAndResume = 0;
            this.motionDetected = false;
            Thread.Sleep(3000);
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
                //show_main_message("停止", S_OK, 20);
                Cam.Stop();  // WebCam stops capturing images.
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
