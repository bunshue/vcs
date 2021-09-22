using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing;

using System.Threading;

using AForge.Video;
using AForge.Video.DirectShow;  // Video Recording
using AForge.Vision.Motion;     // Motion detection
using AForge.Video.FFMPEG;

namespace vcs_WebCam_AForge1
{
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

                if (this.IsRecording == true)
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
                if (this.isResolutionSet == false)
                {
                    // this is run once to set the resolution for the VideoRecorder
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
            if (this.RecordOnMotion == true)
            {
                this.StartRecording(); // record if Autorecord is toggled
            }

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
            // the thread waits 3 seconds if there is no motion detected we stop the AutoRecord
            if ((this.forceRecord == false) && this.motionDetected == false)
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

            //ex : 第 1 台攝影機_2021-09-22_09-23-29.avi
            writer.Open("C:\\dddddddddd\\" + this.cameraName + String.Format("{0:_yyyy-MM-dd_hh-mm-ss}", DateTime.Now) + ".avi", this.Width, this.Height, 30);

            // as long as we're recording
            // we dequeue the BitMaps waiting in the Queue and write them to the file
            while (IsRecording == true)
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
            if (IsRecording == false)
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

