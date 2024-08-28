using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

using System.Threading;

using AForge.Video;
using AForge.Video.DirectShow;  // Video Recording

using AForge.Vision.Motion;     // Motion detection

namespace vcs_WebCam4_MotionDetection222
{
    public partial class MainForm : Form
    {
        CameraMonitor[] CamMonitor = new CameraMonitor[4];  //物件陣列

        private FilterInfoCollection USBWebcams = null;
        int webcam_count = 0;
        private const int BORDER = 30;

        bool flag_motion_detection = false;

        public MainForm()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //檢查錄影存檔的資料夾
            string Path = @"C:\dddddddddd";
            if (Directory.Exists(Path) == false)     //確認資料夾是否存在
            {
                Directory.CreateDirectory(Path);
                richTextBox1.Text += "已建立一個新資料夾: " + Path + "\n";
            }
            else
            {
                //richTextBox1.Text += "資料夾: " + Path + " 已存在，不用再建立\n";
            }

            USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice); //實例化對象

            webcam_count = USBWebcams.Count;

            int i;
            /*
            richTextBox1.Text += "找到 " + webcam_count.ToString() + " 台WebCam\n";

            richTextBox1.Text += "USBWebcams.Capacity : " + USBWebcams.Capacity.ToString() + "\n";
            richTextBox1.Text += "USBWebcams.Count : " + USBWebcams.Count.ToString() + "\n";

            for (i = 0; i < webcam_count; i++)
            {
                richTextBox1.Text += "第 " + (i + 1).ToString() + " 台WebCam:\n";
                richTextBox1.Text += "短名 : " + USBWebcams[i].Name + "\n";
                richTextBox1.Text += "長名 : " + USBWebcams[i].MonikerString + "\n";
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";
            */

            if (webcam_count > 0)
            {
                i = 0;
                string camera_name = USBWebcams[i].MonikerString;   //長名
                this.CamMonitor[i] = new CameraMonitor(pictureBox1, camera_name, "第 " + (i + 1).ToString() + " 台攝影機");

                /*
                richTextBox1.Text += "第 " + (i + 1).ToString() + " 台WebCam:\n";
                richTextBox1.Text += "短名 : " + USBWebcams[i].Name + "\n";
                richTextBox1.Text += "長名 : " + USBWebcams[i].MonikerString + "\n";
                */
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

            W = 120;
            H = 30;

            //W = 640;
            H = 480;
            button2.Location = new Point(1000, BORDER);

            richTextBox1.Size = new Size(200, 600);
            richTextBox1.Location = new Point(1000, 70);
        }

        private void MainForm_FormClosing(object sender, FormClosingEventArgs e)
        {
            //離開程式前, 關閉相機(錄影與播放)
            for (int i = 0; i < 4; i++)
            {
                try
                {
                    this.CamMonitor[i].StopCapture();
                }
                catch (Exception ex)
                {
                }
            }
        }

        private void toggleOption(int camIndex, int optionIndex, bool value)
        {
            switch (optionIndex)
            {
                case 0:
                    this.CamMonitor[camIndex].MotionDetection = value;
                    break;
                case 1:
                    //this.CamMonitor[camIndex].RecordOnMotion = value;
                    break;
                case 2:
                    //this.CamMonitor[camIndex].BeepOnMotion = value;
                    break;
            }
        }

        private void bt_motion_detection_Click(object sender, EventArgs e)
        {
            if (flag_motion_detection == false)
            {
                flag_motion_detection = true;

                this.toggleOption(0, 0, true);


            }
            else
            {
                flag_motion_detection = false;

                this.toggleOption(0, 0, false);
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "找到 " + webcam_count.ToString() + " 台WebCam\n";
            int i;
            i = 0;

            richTextBox1.Text += "第 " + (i + 1).ToString() + " 台WebCam:\n";
            richTextBox1.Text += "cameraName\t" + this.CamMonitor[i].cameraName.ToString() + "\n";
            richTextBox1.Text += "CamMonitor\t" + this.CamMonitor[i].ToString() + "\n";
        }


    }

    class CameraMonitor
    {
        PictureBox display;    // a refrence to the PictureBox on the MainForm
        private VideoCaptureDevice Cam = null; // refrence to the actual VidioCaptureDevice (webcam)
        public String cameraName; // string for display purposes
        MotionDetector md;

        public CameraMonitor(PictureBox display, string monikerString, String cameraName)
        {
            this.cameraName = cameraName;
            this.display = display;
            this.display.Paint += new PaintEventHandler(DrawMessage);

            md = new MotionDetector(new TwoFramesDifferenceDetector(), new MotionAreaHighlighting()); // creates the motion detector

            Cam = new VideoCaptureDevice(monikerString);
            Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame); // defines which method to call when a new frame arrives
            Cam.Start(); // starts the videoCapture
        }

        public void StopCapture()
        {
            if (this.Cam.IsRunning == true)
            {
                // we must stop the VideoCaptureDevice when done to free it so it can be used by other applications
                this.Cam.Stop();
            }
        }

        /*
         * the following method draws information on the PictureBox
         * (date / time / motion if detected / recording state ...)
         */
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
                }
                else
                {
                    str = DateTime.Now.ToString();
                    sb = new SolidBrush(Color.Green);
                }

                e.Graphics.DrawString(str, f, sb, new Point(10, 10));
            }
        }

        bool motionDetected = false; // was there any motion detected previously
        int calibrateAndResume = 0; // counter used delay/skip frames from being processed by the MotionDetector

        //自定義函數, 捕獲每一幀圖像並顯示
        void Cam_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            try
            {
                Bitmap bitmap1 = (Bitmap)eventArgs.Frame.Clone(); // get a copy of the BitMap from the VideoCaptureDevice
                if (this.isResolutionSet == false)
                {
                    this.Width = bitmap1.Width;
                    this.Height = bitmap1.Height;
                    this.isResolutionSet = true;
                }

                this.display.Image = (Bitmap)bitmap1.Clone(); // displays the current frame on the main form
                if ((this.MotionDetection == true) && (this.motionDetected == false))
                {
                    // if motion detection is enabled and there werent any previous motion detected
                    Bitmap bitmap2 = (Bitmap)bitmap1.Clone(); // clone the bits from the current frame

                    if (md.ProcessFrame(bitmap2) > 0.001) // feed the bits to the MD 
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
            catch (InvalidOperationException ex)
            {
            }
        }

        public bool MotionDetection = false;

        private void MotionReaction()
        {
            this.motionDetected = true;

            Thread.Sleep(10000); // the user is notified for 10 seconds
            calibrateAndResume = 0;
            this.motionDetected = false;
            Thread.Sleep(3000);
        }

        // output video resolution info
        bool isResolutionSet = false;
        int Width = 0;
        int Height = 0;

    }

}

