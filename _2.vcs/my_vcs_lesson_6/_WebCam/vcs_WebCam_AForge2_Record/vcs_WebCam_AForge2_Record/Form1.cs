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
using AForge.Video.FFMPEG;

namespace vcs_WebCam_AForge2_Record
{
    public partial class Form1 : Form
    {
        private string recording_filename = string.Empty;
        DateTime recording_time_st = DateTime.Now;
        private bool flag_recording1 = false;    //判斷是否啟動錄影的旗標, for 錄影1, 使用Thread
        private bool flag_recording2 = false;    //判斷是否啟動錄影的旗標, for 錄影2, 不使用Thread

        CameraMonitor CamMonitor;

        private FilterInfoCollection USBWebcams = null;
        int webcam_count = 0;
        private const int BORDER = 30;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

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
                this.CamMonitor = new CameraMonitor(pictureBox1, camera_name, "第 " + (i + 1).ToString() + " 台攝影機");

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
            int dx = 140 + 50;
            int dy = 50 + 15;

            pictureBox1.Size = new Size(W, H);
            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);

            richTextBox1.Size = new Size(300, 600);
            richTextBox1.Location = new Point(x_st + dx * 4 + 70, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            button2.Enabled = false;
            button4.Enabled = false;
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            //離開程式前, 關閉相機(錄影與播放)
            try
            {
                this.CamMonitor.StopRecording1();
                this.CamMonitor.StopRecording2();
                this.CamMonitor.StopCapture();
            }
            catch (Exception ex)
            {
            }

        }

        //錄影 ST, 使用thread
        private void button1_Click(object sender, EventArgs e)
        {
            /*
            if (flag_webcam_ok == false)    //如果webcam沒啟動
            {
                richTextBox1.Text += "無相機\n";
                return;
            }
            */

            if (flag_recording1 == false)
            {
                //開啟錄影模式
                flag_recording1 = true;

                recording_filename = Application.StartupPath + "\\avi_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".avi";

                richTextBox1.Text += "filename : " + recording_filename + "\n";
                //richTextBox1.Text += "Width : " + webcam_w.ToString() + "\n";
                //richTextBox1.Text += "Height : " + webcam_h.ToString() + "\n";

                this.CamMonitor.RecordingFilename = recording_filename;
                this.CamMonitor.StartRecording1();

                richTextBox1.Text += "檔案 :\t\t" + this.CamMonitor.RecordingFilename + "\n\n";
                richTextBox1.Text += "錄影開始\t時間 : " + DateTime.Now.ToString() + "\n";
                recording_time_st = DateTime.Now;
                groupBox2.Enabled = false;
                button1.Enabled = false;
                button2.Enabled = true;
            }
            else
            {
                richTextBox1.Text += "已在錄影\n";
            }
        }

        //錄影 SP, 使用Thread
        private void button2_Click(object sender, EventArgs e)
        {
            if (flag_recording1 == true)
            {
                //錄影完需將影像停止不然會出錯
                flag_recording1 = false;

                this.CamMonitor.StopRecording1();

                richTextBox1.Text += "錄影結束\t時間 : " + DateTime.Now.ToString() + "\n";
                richTextBox1.Text += "錄影時間 :\t" + (DateTime.Now - recording_time_st).TotalSeconds.ToString("0.00") + " 秒\n";
                //richTextBox1.Text += "錄影時間 : " + (DateTime.Now - recording_time_st).ToString() + "\n\n";
                richTextBox1.Text += "檔案 :\t\t" + this.CamMonitor.RecordingFilename + "\n\n";
                groupBox2.Enabled = true;
                button1.Enabled = true;
                button2.Enabled = false;
            }
            else
            {
                richTextBox1.Text += "並沒有在錄影\n";
            }
        }

        //錄影 ST, 不使用thread
        private void button3_Click(object sender, EventArgs e)
        {
            /*
            if (flag_webcam_ok == false)    //如果webcam沒啟動
            {
                richTextBox1.Text += "無相機\n";
                return;
            }
            */

            if (flag_recording2 == false)
            {
                //開啟錄影模式
                flag_recording2 = true;

                recording_filename = Application.StartupPath + "\\avi_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".avi";

                richTextBox1.Text += "filename : " + recording_filename + "\n";
                //richTextBox1.Text += "Width : " + webcam_w.ToString() + "\n";
                //richTextBox1.Text += "Height : " + webcam_h.ToString() + "\n";

                this.CamMonitor.RecordingFilename = recording_filename;
                this.CamMonitor.StartRecording2();

                richTextBox1.Text += "檔案 :\t\t" + this.CamMonitor.RecordingFilename + "\n\n";
                richTextBox1.Text += "錄影開始\t時間 : " + DateTime.Now.ToString() + "\n";
                recording_time_st = DateTime.Now;
                groupBox1.Enabled = false;
                button3.Enabled = false;
                button4.Enabled = true;
            }
            else
            {
                richTextBox1.Text += "已在錄影\n";
            }
        }

        //錄影 SP, 不使用Thread
        private void button4_Click(object sender, EventArgs e)
        {
            if (flag_recording2 == true)
            {
                //錄影完需將影像停止不然會出錯
                flag_recording2 = false;

                this.CamMonitor.StopRecording2();

                richTextBox1.Text += "錄影結束\t時間 : " + DateTime.Now.ToString() + "\n";
                richTextBox1.Text += "錄影時間 :\t" + (DateTime.Now - recording_time_st).TotalSeconds.ToString("0.00") + " 秒\n";
                //richTextBox1.Text += "錄影時間 : " + (DateTime.Now - recording_time_st).ToString() + "\n\n";
                richTextBox1.Text += "檔案 :\t\t" + this.CamMonitor.RecordingFilename + "\n\n";
                groupBox1.Enabled = true;
                button3.Enabled = true;
                button4.Enabled = false;
            }
            else
            {
                richTextBox1.Text += "並沒有在錄影\n";
            }
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

                if ((flag_recording1 == true) || (flag_recording2 == true))
                {
                    if (DateTime.Now.Millisecond < 500)
                    {
                        e.Graphics.DrawString("錄影中", f, Brushes.Red, new Point(240, 10));
                    }
                }
            }
        }

        private const int BORDER = 10;
        public Bitmap bitmap1 = null;
        //int frame_cnt = 0;          //每多少張做一個計算
        int frame_count = 0;        //計算fps用
        int frame_count_old = 0;    //計算fps用
        DateTime dt_old = DateTime.Now;

        Graphics g;
        //SolidBrush drawBrush;
        //Font drawFont1;

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

                if (flag_recording1 == true)    //使用thread
                {
                    frames.Enqueue((Bitmap)bitmap1.Clone());
                }

                if (flag_recording2 == true)
                {
                    try
                    {
                        writer2.WriteVideoFrame(bitmap1);
                    }
                    catch (Exception ex)
                    {
                    }
                }
                GC.Collect();       //回收資源
            }
            catch (InvalidOperationException ex)
            {
            }
        }

        // output video resolution info
        bool isResolutionSet = false;
        int Width = 0;
        int Height = 0;

        private bool flag_recording1 = false;    //判斷是否啟動錄影的旗標, for 錄影1, 使用Thread
        private bool flag_recording2 = false;    //判斷是否啟動錄影的旗標, for 錄影2, 不使用Thread

        public string RecordingFilename = "aaaaa.avi";

        Queue<Bitmap> frames = new Queue<Bitmap>(); // Queue that stores frames to be written by the recorder thread

        private void DoRecord()
        {
            // we set our VideoFileWriter as well as the file name, resolution and fps
            VideoFileWriter writer1 = new VideoFileWriter();

            writer1.Open(RecordingFilename, this.Width, this.Height, 30);

            // as long as we're recording
            // we dequeue the BitMaps waiting in the Queue and write them to the file
            while (flag_recording1 == true)
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
                    }
                }
            }
            writer1.Close();
        }

        public void StartRecording1()
        {
            if (flag_recording1 == false)
            {
                // if were not already recording we start the recording thread
                flag_recording1 = true;
                Thread th = new Thread(DoRecord);
                th.Start();
            }
        }

        // stops recording
        public void StopRecording1()
        {
            flag_recording1 = false;
        }

        public void StartRecording2()
        {
            if (flag_recording2 == false)
            {
                flag_recording2 = true;
                writer2.Open(RecordingFilename, this.Width, this.Height, 30);
            }
        }

        public void StopRecording2()
        {
            flag_recording2 = false;
            writer2.Close();
        }
    }
}

