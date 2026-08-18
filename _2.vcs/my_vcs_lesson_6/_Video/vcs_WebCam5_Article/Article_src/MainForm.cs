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

using AForge.Vision.Motion; // Motion detection
using AForge.Video;              //
using AForge.Video.DirectShow;   // Video Recording
using AForge.Video.FFMPEG;

namespace WebcamSecurity
{
    public partial class MainForm : Form
    {
        // Refrence to cameraMonitors of all 4 cams
        WebCam[] CamMonitor = new WebCam[4];
        // Indexed arrays containing referces to the user interface components
        // so they can be easily accessed later on
        PictureBox[] DisplayReference = new PictureBox[4];
        GroupBox[] camPanels = new GroupBox[4];
        GroupBox[] camOptions = new GroupBox[4];

        string RecordingPath = @"D:\dddddddddd";

        public MainForm()
        {
            InitializeComponent();

            // linking the user interface componets to the arrays
            this.DisplayReference[0] = this.Display_Cam1;
            this.DisplayReference[1] = this.Display_Cam2;
            this.DisplayReference[2] = this.Display_Cam3;
            this.DisplayReference[3] = this.Display_Cam4;

            this.camPanels[0] = this.groupBox1;
            this.camPanels[1] = this.groupBox2;
            this.camPanels[2] = this.groupBox3;
            this.camPanels[3] = this.groupBox4;

            this.camOptions[0] = this.groupBox5;
            this.camOptions[1] = this.groupBox6;
            this.camOptions[2] = this.groupBox7;
            this.camOptions[3] = this.groupBox8;
            // we disable all the user controls (will be activated later when we load cameras)
            this.camPanels[0].Enabled = false;
            this.camPanels[1].Enabled = false;
            this.camPanels[2].Enabled = false;
            this.camPanels[3].Enabled = false;
            this.camOptions[0].Enabled = false;
            this.camOptions[1].Enabled = false;
            this.camOptions[2].Enabled = false;
            this.camOptions[3].Enabled = false;
        }

        // the FilterInfoCollection is where we get information about VideoCaptureDevices
        private FilterInfoCollection webcam;

        // When the form loads
        private void Form1_Load(object sender, EventArgs e)
        {
            // an instance of FilterInfoCollection is created to fetch available VideoCaptureDevices
            webcam = new FilterInfoCollection(FilterCategory.VideoInputDevice);
            // we create our CameraMonitors
            for (int i = 0; i < webcam.Count && i < 4; i++)
            {
                this.CamMonitor[i] = new WebCam(this.DisplayReference[i], webcam[i].MonikerString, "Camera" + (i + 1));
                // Enable the user controls coressponding to the CameraMonitor
                this.camPanels[i].Enabled = true;
                this.camOptions[i].Enabled = true;
            }

            // set the recording path to the exising CameraMonitors
            for (int i = 0; i < 4; i++)
            {
                this.CamMonitor[i].RecordingPath = RecordingPath;
            }
        }

        // this method will stop recording and running cameras 
        // also save the options to an xml file
        private void StopCameras(object sender, FormClosingEventArgs e)
        {
            for (int i = 0; i < 4; i++)
            {
                try
                {
                    this.CamMonitor[i].StopRecording();
                    this.CamMonitor[i].StopCapture();
                }
                catch (Exception ex) { }
            }
        }

        //6060

        // The Rest is User Interface EventHandling
        private void RecordButton1_Click(object sender, EventArgs e)
        {
            if (this.CamMonitor[0].IsRecording)
            {
                this.CamMonitor[0].StopRecording();
                this.CamMonitor[0].forceRecord = false;
                ((Button)sender).Text = "Record";
            }
            else
            {
                this.CamMonitor[0].StartRecording();
                this.CamMonitor[0].forceRecord = true;
                ((Button)sender).Text = "Stop";
            }
        }

        private void RecordButton2_Click(object sender, EventArgs e)
        {
            if (this.CamMonitor[1].IsRecording)
            {
                this.CamMonitor[1].StopRecording();
                this.CamMonitor[1].forceRecord = false;
                ((Button)sender).Text = "Record";
            }
            else
            {
                this.CamMonitor[1].StartRecording();
                this.CamMonitor[1].forceRecord = true;
                ((Button)sender).Text = "Stop";
            }
        }
        private void RecordButton3_Click(object sender, EventArgs e)
        {
            if (this.CamMonitor[2].IsRecording)
            {
                this.CamMonitor[2].StopRecording();
                this.CamMonitor[2].forceRecord = false;
                ((Button)sender).Text = "Record";
            }
            else
            {
                this.CamMonitor[2].StartRecording();
                this.CamMonitor[2].forceRecord = true;
                ((Button)sender).Text = "Stop";
            }
        }
        private void RecordButton4_Click(object sender, EventArgs e)
        {
            if (this.CamMonitor[3].IsRecording)
            {
                this.CamMonitor[3].StopRecording();
                this.CamMonitor[3].forceRecord = false;
                ((Button)sender).Text = "Record";
            }
            else
            {
                this.CamMonitor[3].StartRecording();
                this.CamMonitor[3].forceRecord = true;
                ((Button)sender).Text = "Stop";
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
                    this.CamMonitor[camIndex].RecordOnMotion = value;
                    break;
                case 2:
                    this.CamMonitor[camIndex].BeepOnMotion = value;
                    break;
            }
        }

        private void MotionDetection1_CheckedChanged(object sender, EventArgs e)
        {
            if (((CheckBox)sender).Checked)
            {
                this.toggleOption(0, 0, true);
            }
            else
            {
                this.toggleOption(0, 0, false);
            }
        }

        private void MotionDetection2_CheckedChanged(object sender, EventArgs e)
        {
            if (((CheckBox)sender).Checked)
            {
                this.toggleOption(1, 0, true);
            }
            else
            {
                this.toggleOption(1, 0, false);
            }
        }

        private void MotionDetection3_CheckedChanged(object sender, EventArgs e)
        {
            if (((CheckBox)sender).Checked)
            {
                this.toggleOption(2, 0, true);
            }
            else
            {
                this.toggleOption(2, 0, false);
            }
        }

        private void MotionDetection4_CheckedChanged(object sender, EventArgs e)
        {
            if (((CheckBox)sender).Checked)
            {
                this.toggleOption(3, 0, true);
            }
            else
            {
                this.toggleOption(3, 0, false);
            }
        }

        private void AutoRecord1_CheckedChanged(object sender, EventArgs e)
        {
            if (((CheckBox)sender).Checked)
            {
                this.toggleOption(0, 1, true);
            }
            else
            {
                this.toggleOption(0, 1, false);
            }
        }

        private void AutoRecord2_CheckedChanged(object sender, EventArgs e)
        {
            if (((CheckBox)sender).Checked)
            {
                this.toggleOption(1, 1, true);
            }
            else
            {
                this.toggleOption(1, 1, false);
            }
        }

        private void AutoRecord3_CheckedChanged(object sender, EventArgs e)
        {
            if (((CheckBox)sender).Checked)
            {
                this.toggleOption(2, 1, true);
            }
            else
            {
                this.toggleOption(2, 1, false);
            }
        }

        private void AutoRecord4_CheckedChanged(object sender, EventArgs e)
        {
            if (((CheckBox)sender).Checked)
            {
                this.toggleOption(3, 1, true);
            }
            else
            {
                this.toggleOption(3, 1, false);
            }
        }

        private void BeepOnMotionCheck1_CheckedChanged(object sender, EventArgs e)
        {
            if (((CheckBox)sender).Checked)
            {
                this.toggleOption(0, 2, true);
            }
            else
            {
                this.toggleOption(0, 2, false);
            }
        }

        private void BeepOnMotionCheck2_CheckedChanged(object sender, EventArgs e)
        {
            if (((CheckBox)sender).Checked)
            {
                this.toggleOption(1, 2, true);
            }
            else
            {
                this.toggleOption(1, 2, false);
            }
        }

        private void BeepOnMotionCheck3_CheckedChanged(object sender, EventArgs e)
        {
            if (((CheckBox)sender).Checked)
            {
                this.toggleOption(2, 2, true);
            }
            else
            {
                this.toggleOption(2, 2, false);
            }
        }

        private void BeepOnMotionCheck4_CheckedChanged(object sender, EventArgs e)
        {
            if (((CheckBox)sender).Checked)
            {
                this.toggleOption(3, 2, true);
            }
            else
            {
                this.toggleOption(3, 2, false);
            }
        }

        private void SetFocus(int camIndex)
        {
            switch (camIndex)
            {
                case 0:
                    this.splitContainer1.Panel1Collapsed = false;
                    this.splitContainer1.Panel2Collapsed = false;
                    this.splitContainer2.Panel1Collapsed = false;
                    this.splitContainer2.Panel2Collapsed = false;
                    this.splitContainer3.Panel1Collapsed = false;
                    this.splitContainer3.Panel2Collapsed = false;
                    break;
                case 1:
                    this.splitContainer1.Panel2Collapsed = true;
                    this.splitContainer2.Panel2Collapsed = true;
                    break;
                case 2:
                    this.splitContainer1.Panel2Collapsed = true;
                    this.splitContainer2.Panel1Collapsed = true;
                    break;
                case 3:
                    this.splitContainer1.Panel1Collapsed = true;
                    this.splitContainer3.Panel2Collapsed = true;
                    break;
                case 4:
                    this.splitContainer1.Panel1Collapsed = true;
                    this.splitContainer3.Panel1Collapsed = true;
                    break;

            }
        }

        private void buttonFocusCam1_Click(object sender, EventArgs e)
        {
            this.SetFocus(1);
        }

        private void buttonFocusCam2_Click(object sender, EventArgs e)
        {
            this.SetFocus(2);
        }

        private void buttonFocusCam3_Click(object sender, EventArgs e)
        {
            this.SetFocus(3);
        }

        private void buttonFocusCam4_Click(object sender, EventArgs e)
        {
            this.SetFocus(4);
        }

        private void buttonResetFocus_Click(object sender, EventArgs e)
        {
            this.SetFocus(0);
        }
    }



    class WebCam
    {
        PictureBox display;    // a refrence to the PictureBox on the MainForm
        private VideoCaptureDevice cam; // refrence to the actual VidioCaptureDevice (webcam)
        String cameraName; // string for display purposes
        MotionDetector md;
        public WebCam(PictureBox display, string monikerString, String cameraName)
        {
            this.cameraName = cameraName;
            this.display = display;
            this.display.Paint += new PaintEventHandler(DrawMessage);

            md = new MotionDetector(new TwoFramesDifferenceDetector(), new MotionAreaHighlighting()); // creates the motion detector

            cam = new VideoCaptureDevice(monikerString);
            cam.NewFrame += new NewFrameEventHandler(cam_NewFrame); // defines which method to call when a new frame arrives
            cam.Start(); // starts the videoCapture
        }



        public void StopCapture()
        {
            if (this.cam.IsRunning)
            {
                // we must stop the VideoCaptureDevice when done to free it so it can be used by other applications
                this.cam.Stop();
            }
        }

        /*
         * the following method draws information on the PictureBox
         * (date / time / motion if detected / recording state ...)
         */
        private void DrawMessage(object sender, PaintEventArgs e)
        {
            using (Font myFont = new Font("Tahoma", 10, FontStyle.Bold))
            {

                e.Graphics.DrawString(DateTime.Now.ToString() + ((this.motionDetected) ? " + Motion !" : ""), myFont, ((this.motionDetected) ? Brushes.Red : Brushes.Green), new Point(2, 2));
                if (this.IsRecording)
                {
                    if (this.showRecordMarkerCount > 10)
                    {
                        e.Graphics.DrawString("[RECORDING]", myFont, Brushes.Red, new Point(2, 14));

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

        void cam_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            try
            {
                Bitmap bit = (Bitmap)eventArgs.Frame.Clone(); // get a copy of the BitMap from the VideoCaptureDevice
                if (!this.isResolutionSet)
                {
                    // this is run once to set the resolution for the VideoRecorder
                    this.Width = bit.Width;
                    this.Height = bit.Height;
                    this.isResolutionSet = true;
                }
                this.display.Image = (Bitmap)bit.Clone(); // displays the current frame on the main form
                if (this.MotionDetection && !this.motionDetected)
                {
                    // if motion detection is enabled and there werent any previous motion detected
                    Bitmap bit2 = (Bitmap)bit.Clone(); // clone the bits from the current frame

                    if (md.ProcessFrame(bit2) > 0.001) // feed the bits to the MD 
                    {
                        if (this.calibrateAndResume > 3)
                        {
                            // if motion was detected in 3 subsequent frames
                            Thread th = new Thread(MotionReaction);
                            th.Start(); // start the motion reaction thread
                        }
                        else this.calibrateAndResume++;
                    }

                }
                if (IsRecording)
                {
                    // if recording is enabled we enqueue the current frame to be encoded to a video file
                    Graphics gr = Graphics.FromImage(bit);
                    Pen p = new Pen(Color.Red);
                    p.Width = 5.0f;
                    using (Font myFont = new Font("Tahoma", 10, FontStyle.Bold))
                    {
                        gr.DrawString(DateTime.Now.ToString(), myFont, Brushes.Red, new Point(2, 2));
                    }
                    frames.Enqueue((Bitmap)bit.Clone());
                }

            }
            catch (InvalidOperationException ex) { }
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
                // beep if BeepOnMotion is toggeled
                System.Console.Beep(400, 500);
                System.Console.Beep(800, 500);
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

        Queue<Bitmap> frames = new Queue<Bitmap>(); // Queue that stors frames to be written by the recorder thread
        public string RecordingPath = "recording"; // default recording path

        private void DoRecord()
        {
            // we set our VideoFileWriter as well as the file name, resolution and fps
            VideoFileWriter writer = new VideoFileWriter();
            writer.Open(RecordingPath + "\\" + this.cameraName + String.Format("{0:_dd-M-yyyy_hh-mm-ss}", DateTime.Now) + ".avi", this.Width, this.Height, 30);

            // as long as we're recording
            // we dequeue the BitMaps waiting in the Queue and write them to the file
            while (IsRecording)
            {
                if (frames.Count > 0)
                {
                    Bitmap bmp = frames.Dequeue();
                    writer.WriteVideoFrame(bmp);
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


