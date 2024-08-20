using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;   //for ImageFormat
using System.Diagnostics;       //for Process
using System.Runtime.InteropServices;   //for dll

using System.Threading;

using AForge.Video;
using AForge.Video.DirectShow;  // Video Recording
using AForge.Video.FFMPEG;      //for VideoFileWriter

//使用Thread 錄影

namespace vcs_WebCam_AForge2_Record2
{
    public partial class Form1 : Form
    {
        private FilterInfoCollection USBWebcams = null;
        CameraMonitor CamMonitor;
        private bool flag_recording = false;    //判斷是否啟動錄影的旗標
        private string recording_filename = string.Empty;
        DateTime recording_time_st = DateTime.Now;

        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE
        private const int BORDER = 10;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice); //實例化對象

            if (USBWebcams.Count > 0)
            {
                string camera_name = USBWebcams[0].MonikerString;   //長名
                this.CamMonitor = new CameraMonitor(pictureBox1, camera_name, "第 1 台攝影機");
            }
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            //離開程式前, 關閉相機(錄影與播放)
            try
            {
                this.CamMonitor.StopRecording();
                this.CamMonitor.StopCapture();
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息e01 : " + ex.Message + "\n";
            }
        }

        void show_item_location()
        {
            int W = 640;
            int H = 480;
            int x_st = BORDER;
            int y_st = BORDER;
            int dx = 140 + 50;
            int dy = 50 + 15;

            pictureBox1.Size = new Size(W, H);
            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox1.Image = vcs_WebCam_AForge2_Record2.Properties.Resources.ims_logo_720x480;

            richTextBox1.Size = new Size(300, 560);
            richTextBox1.Location = new Point(x_st + dx * 3 + 90, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            groupBox1.Size = new Size(380, 70);
            groupBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0 + H + BORDER);

            bt_record_stop.Enabled = false;
            this.Size = new Size(1000, 620);
            x_st = 10;
            y_st = 20;
            dx = 90;
            dy = 28;
            dy = 40;

            bt_record_start.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_record_stop.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_exit.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            richTextBox1.BringToFront();
            bt_clear.BringToFront();
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //錄影 ST
        private void bt_record_start_Click(object sender, EventArgs e)
        {
            /*
            if (flag_webcam_ok == false)    //如果webcam沒啟動
            {
                richTextBox1.Text += "無相機\n";
                return;
            }
            */

            if (flag_recording == false)
            {
                //開啟錄影模式
                flag_recording = true;

                recording_filename = Application.StartupPath + "\\avi_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".avi";

                richTextBox1.Text += "filename : " + recording_filename + "\n";
                //richTextBox1.Text += "Width : " + webcam_w.ToString() + "\n";
                //richTextBox1.Text += "Height : " + webcam_h.ToString() + "\n";

                this.CamMonitor.RecordingFilename = recording_filename;
                this.CamMonitor.StartRecording();

                richTextBox1.Text += "檔案 :\t\t" + this.CamMonitor.RecordingFilename + "\n\n";
                richTextBox1.Text += "錄影開始\t時間 : " + DateTime.Now.ToString() + "\n";
                recording_time_st = DateTime.Now;
                bt_record_start.Enabled = false;
                bt_record_stop.Enabled = true;
            }
            else
            {
                richTextBox1.Text += "已在錄影\n";
            }
        }

        //錄影 SP
        private void bt_record_stop_Click(object sender, EventArgs e)
        {
            if (flag_recording == true)
            {
                //錄影完需將影像停止不然會出錯
                flag_recording = false;

                this.CamMonitor.StopRecording();

                richTextBox1.Text += "錄影結束\t時間 : " + DateTime.Now.ToString() + "\n";
                richTextBox1.Text += "錄影時間 :\t" + (DateTime.Now - recording_time_st).TotalSeconds.ToString("0.00") + " 秒\n";
                //richTextBox1.Text += "錄影時間 : " + (DateTime.Now - recording_time_st).ToString() + "\n\n";
                richTextBox1.Text += "檔案 :\t\t" + this.CamMonitor.RecordingFilename + "\n\n";
                bt_record_start.Enabled = true;
                bt_record_stop.Enabled = false;
            }
            else
            {
                richTextBox1.Text += "並沒有在錄影\n";
            }
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }

    class CameraMonitor
    {
        PictureBox display;    // a refrence to the PictureBox on the MainForm
        private VideoCaptureDevice Cam = null; // refrence to the actual VidioCaptureDevice (webcam)
        public String cameraName; // string for display purposes
        VideoFileWriter writer2 = new VideoFileWriter();

        public CameraMonitor(PictureBox display, string monikerString, String cameraName)
        {
            this.cameraName = cameraName;
            this.display = display;
            this.display.Paint += new PaintEventHandler(DrawMessage);

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
                string str = DateTime.Now.ToString();
                SolidBrush sb = new SolidBrush(Color.Green);

                e.Graphics.DrawString(str, f, sb, new Point(10, 10));

                if (flag_recording == true)
                {
                    if (DateTime.Now.Millisecond < 500)
                    {
                        int ww = 22;
                        e.Graphics.FillEllipse(Brushes.Red, 640 - BORDER - ww, BORDER + 4, ww, ww);
                    }
                }
            }
        }

        private const int BORDER = 10;
        public Bitmap bitmap1 = null;
        DateTime dt_old = DateTime.Now;

        //自定義函數, 捕獲每一幀圖像並顯示
        void Cam_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            try
            {
                bitmap1 = (Bitmap)eventArgs.Frame.Clone(); // get a copy of the BitMap from the VideoCaptureDevice
                if (this.isResolutionSet == false)
                {
                    // this is run once to set the resolution for the VideoRecorder
                    this.Width = bitmap1.Width;
                    this.Height = bitmap1.Height;
                    this.isResolutionSet = true;
                }

                this.display.Image = (Bitmap)bitmap1.Clone(); // displays the current frame on the main form

                string str = DateTime.Now.ToString();
                SolidBrush sb = new SolidBrush(Color.Green);
                Font f = new Font("Arial", 14, FontStyle.Bold);

                Graphics g = Graphics.FromImage(bitmap1);
                g.DrawString(str, f, sb, new Point(10, 10));

                if (flag_recording == true)
                {
                    frames.Enqueue((Bitmap)bitmap1.Clone());
                }
                GC.Collect();       //回收資源
            }
            catch (InvalidOperationException ex)
            {
                Console.WriteLine("xxx錯誤訊息e02 : " + ex.Message);
            }
        }

        // output video resolution info
        bool isResolutionSet = false;
        int Width = 0;
        int Height = 0;

        private bool flag_recording = false;    //判斷是否啟動錄影的旗標

        public string RecordingFilename = "aaaaa.avi";

        Queue<Bitmap> frames = new Queue<Bitmap>(); // Queue that stores frames to be written by the recorder thread

        private void DoRecord()
        {
            // we set our VideoFileWriter as well as the file name, resolution and fps
            VideoFileWriter writer1 = new VideoFileWriter();

            writer1.Open(RecordingFilename, this.Width, this.Height, 30);

            // as long as we're recording
            // we dequeue the BitMaps waiting in the Queue and write them to the file
            while (flag_recording == true)
            {
                if (frames.Count > 0)
                {
                    try
                    {
                        Bitmap bitmap1 = frames.Dequeue();
                        writer1.WriteVideoFrame(bitmap1);
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine("xxx錯誤訊息e03 : " + ex.Message);
                    }
                }
            }
            writer1.Close();
        }

        public void StartRecording()
        {
            if (flag_recording == false)
            {
                // if were not already recording we start the recording thread
                flag_recording = true;
                Thread th = new Thread(DoRecord);
                th.Start();
            }
        }

        public void StopRecording()
        {
            flag_recording = false;
        }
    }
}
