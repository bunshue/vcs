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
using AForge.Video.FFMPEG;

namespace vcs_WebCam5_Article
{
    public partial class MainForm : Form
    {
        WebCam CamMonitor;

        private FilterInfoCollection USBWebcams = null;
        int webcam_count = 0;

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
            richTextBox1.Text += "找到 " + webcam_count.ToString() + " 台WebCam\n";

            int i;
            /*

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
                CamMonitor = new WebCam(pictureBox1, camera_name, "第1台攝影機");

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
            int x_st = 10;
            int y_st = 10;
            int dx = W + 50;
            int dy = H + 50;

            pictureBox1.Size = new Size(W, H);

            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);

            W = 120;
            H = 30;
            button1.Size = new Size(W, H);

            //W = 640;
            H = 480;
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 0 + H + 10);
            button2.Location = new Point(1000, 10);

            richTextBox1.Size = new Size(200, 600);
            richTextBox1.Location = new Point(1000, 50);
        }

        private void MainForm_FormClosing(object sender, FormClosingEventArgs e)
        {
            //離開程式前, 關閉相機(錄影與播放)
            for (int i = 0; i < 4; i++)
            {
                try
                {
                    CamMonitor.StopRecording();
                    CamMonitor.StopCapture();
                }
                catch (Exception ex)
                {
                }
            }
        }

        // The Rest is User Interface EventHandling
        private void button1_Click(object sender, EventArgs e)
        {
            if (CamMonitor.IsRecording)
            {
                CamMonitor.StopRecording();
                CamMonitor.forceRecord = false;
                ((Button)sender).Text = "Record";
            }
            else
            {
                CamMonitor.StartRecording();
                CamMonitor.forceRecord = true;
                ((Button)sender).Text = "Stop";
            }
        }

        private void toggleOption(int optionIndex, bool value)
        {
            switch (optionIndex)
            {
                case 0:
                    CamMonitor.MotionDetection = value;
                    break;
                case 1:
                    CamMonitor.RecordOnMotion = value;
                    break;
                case 2:
                    CamMonitor.BeepOnMotion = value;
                    break;
            }
        }

        private void MotionDetection1_CheckedChanged(object sender, EventArgs e)
        {
            if (((CheckBox)sender).Checked)
            {
                this.toggleOption(0, true);
            }
            else
            {
                this.toggleOption(0, false);
            }
        }

        private void AutoRecord1_CheckedChanged(object sender, EventArgs e)
        {
            if (((CheckBox)sender).Checked)
            {
                this.toggleOption(1, true);
            }
            else
            {
                this.toggleOption(1, false);
            }
        }

        private void BeepOnMotionCheck1_CheckedChanged(object sender, EventArgs e)
        {
            if (((CheckBox)sender).Checked)
            {
                this.toggleOption(2, true);
            }
            else
            {
                this.toggleOption(2, false);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
        }
    }

    class WebCam
    {
        PictureBox display;    // a refrence to the PictureBox on the MainForm
        private VideoCaptureDevice Cam = null; // refrence to the actual VidioCaptureDevice (webcam)
        public String cameraName; // string for display purposes
        MotionDetector md;

        public WebCam(PictureBox display, string monikerString, String cameraName)
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
            if (this.Cam.IsRunning)
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

                if (this.IsRecording)
                {
                    if (this.showRecordMarkerCount > 10)
                    {
                        e.Graphics.DrawString("錄影中", f, Brushes.Red, new Point(2, 14));

                        if (this.showRecordMarkerCount == 20)
                        {
                            this.showRecordMarkerCount = 0;
                        }
                    }
                    this.showRecordMarkerCount++;
                }
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
                if (!this.isResolutionSet)
                {
                    // this is run once to set the resolution for the VideoRecorder
                    this.Width = bitmap1.Width;
                    this.Height = bitmap1.Height;
                    this.isResolutionSet = true;
                }
                this.display.Image = (Bitmap)bitmap1.Clone(); // displays the current frame on the main form

                if (this.MotionDetection && !this.motionDetected)
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

                if (IsRecording)
                {
                    // if recording is enabled we enqueue the current frame to be encoded to a video file
                    Graphics g = Graphics.FromImage(bitmap1);
                    Pen p = new Pen(Color.Red);
                    p.Width = 5.0f;
                    using (Font f = new Font("Tahoma", 10, FontStyle.Bold))
                    {
                        g.DrawString(DateTime.Now.ToString(), f, Brushes.Red, new Point(2, 2));
                    }
                    frames.Enqueue((Bitmap)bitmap1.Clone());
                }
            }
            catch (InvalidOperationException ex)
            {
            }
        }

        // different option toggles
        public bool RecordOnMotion = false;
        public bool BeepOnMotion = false;
        public bool MotionDetection = false;
        public bool forceRecord = false;

        private void MotionReaction()
        {
            this.motionDetected = true;
            if (this.RecordOnMotion)
            {
                this.StartRecording(); // record if Autorecord is toggled
            }

            if (this.BeepOnMotion)
            {
                //偵測到移動
            }

            Thread.Sleep(10000); // the user is notified for 10 seconds
            calibrateAndResume = 0;
            this.motionDetected = false;
            Thread.Sleep(3000);
            // the thread waits 3 seconds if there is no motion detected we stop the AutoRecord
            if (!this.forceRecord && this.motionDetected == false)
            {
                this.StopRecording();
            }
        }

        // output video resolution info
        bool isResolutionSet = false;
        int Width = 0;
        int Height = 0;

        public bool IsRecording = false; // recording flag

        Queue<Bitmap> frames = new Queue<Bitmap>(); // Queue that stores frames to be written by the recorder thread

        private void DoRecord()
        {
            // we set our VideoFileWriter as well as the file name, resolution and fps
            VideoFileWriter writer = new VideoFileWriter();
            writer.Open("C:\\dddddddddd\\" + this.cameraName + String.Format("{0:_dd-M-yyyy_hh-mm-ss}", DateTime.Now) + ".avi", this.Width, this.Height, 30);

            // as long as we're recording
            // we dequeue the BitMaps waiting in the Queue and write them to the file
            while (IsRecording)
            {
                if (frames.Count > 0)
                {
                    Bitmap bitmap1 = frames.Dequeue();
                    writer.WriteVideoFrame(bitmap1);
                }
            }
            writer.Close();
        }

        int showRecordMarkerCount = 0; // used to display message on the main form
        public void StartRecording()
        {
            if (!IsRecording)
            {
                // if were not already recording we start the recording thread
                this.IsRecording = true;
                Thread th = new Thread(DoRecord);
                th.Start();
            }
        }

        // stops recording
        public void StopRecording()
        {
            this.IsRecording = false;
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

