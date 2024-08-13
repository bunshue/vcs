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

using AForge.Video;
using AForge.Video.DirectShow;  // Video Recording
using AForge.Video.FFMPEG;      //for VideoFileWriter

//不使用Thread 錄影

namespace vcs_WebCam_AForge2_Record3
{
    public partial class Form1 : Form
    {
        private FilterInfoCollection USBWebcams = null;
        CameraMonitor CamMonitor;
        private bool flag_recording = false;    //判斷是否啟動錄影的旗標


        private string recording_filename = string.Empty;
        DateTime recording_time_st = DateTime.Now;

        int webcam_count = 0;

        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE
        private const int BORDER = 10;

        int timer_display_show_main_mesg_count = 0;
        int timer_display_show_main_mesg_count_target = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //C# 跨 Thread 存取 UI
            Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效

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

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            //離開程式前, 關閉相機(錄影與播放)
            try
            {
                this.CamMonitor.StopRecording2();
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
            pictureBox1.Image = vcs_WebCam_AForge2_Record3.Properties.Resources.ims_logo_720x480;

            richTextBox1.Size = new Size(300, 690);
            richTextBox1.Location = new Point(x_st + dx * 3 + 90, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            groupBox1.Size = new Size(250, 200);
            groupBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0 + H + BORDER);
            groupBox2.Size = new Size(380, 200);
            groupBox2.Location = new Point(x_st + dx * 0 + 250 + BORDER, y_st + dy * 0 + H + BORDER);

            bt_record_stop.Enabled = false;
            this.Size = new Size(1000, 750);
            x_st = 10;
            y_st = 20;
            dx = 90;
            dy = 28;
            comboBox1.Size = new Size(220, 40);
            comboBox2.Size = new Size(220, 40);
            comboBox3.Size = new Size(220, 40);
            label1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            comboBox1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            label2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            comboBox2.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            label3.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            comboBox3.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            dy = 40;

            bt_start.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_stop.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_refresh.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt_exit.Location = new Point(x_st + dx * 3, y_st + dy * 0);

            bt_snapshot.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_record_start.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            bt_record_stop.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            lb_fps.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            lb_fps.Text = "";
            lb_main_mesg.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            lb_main_mesg.Text = "";
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
                this.CamMonitor.StartRecording2();

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

                this.CamMonitor.StopRecording2();

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

        int min_old = 0;
        private void timer_fps_Tick(object sender, EventArgs e)
        {
            /*
            if (flag_webcam_ok == true)
            {
                DateTime dt = DateTime.Now;
                lb_fps.Text = (((frame_count - frame_count_old) * 1000) / ((TimeSpan)(dt - dt_old)).TotalMilliseconds).ToString("F2") + " fps";
                dt_old = dt;
                frame_count_old = frame_count;

                if (flag_recording == true)
                {
                    int min = (int)((DateTime.Now - recording_time_st).TotalMinutes);
                    if ((min > 0) && (min != min_old))
                    {
                        richTextBox1.Text += "已錄影 " + min.ToString() + " 分\n";
                        min_old = min;
                    }
            }
            else
            {
                lb_fps.Text = "";
            }
            */
        }

        bool camera_start = false;
        private void bt_start_Click(object sender, EventArgs e)
        {
            camera_start = true;
            //Start_Webcam();
            bt_start.Enabled = false;
            bt_stop.Enabled = true;
            //bt_record.Enabled = true;
        }

        private void bt_stop_Click(object sender, EventArgs e)
        {

        }

        private void bt_refresh_Click(object sender, EventArgs e)
        {

        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            show_main_message("離開", S_OK, 20);
            Application.Exit();
        }

        private void bt_snapshot_Click(object sender, EventArgs e)
        {
            save_image_to_drive();
        }

        void save_image_to_drive()
        {
            show_main_message("截圖", S_OK, 20);

            Bitmap bitmap1 = (Bitmap)pictureBox1.Image;

            if (bitmap1 != null)
            {
                String filename = string.Empty;
                filename = Application.StartupPath + "\\ims_image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");

                //String file1 = file + ".jpg";
                String filename2 = filename + ".bmp";
                //String file3 = file + ".png";
                try
                {
                    //bitmap1.Save(@file1, ImageFormat.Jpeg);
                    bitmap1.Save(filename2, ImageFormat.Bmp);
                    //bitmap1.Save(@file3, ImageFormat.Png);

                    richTextBox1.Text += "存檔成功\n";
                    //richTextBox1.Text += "已存檔 : " + file1 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                    //richTextBox1.Text += "已存檔 : " + file3 + "\n";
                    show_main_message("已存檔", S_OK, 10);
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "xxx錯誤訊息b : " + ex.Message + "\n";
                    show_main_message("存檔失敗", S_OK, 30);
                }
            }
            else
            {
                richTextBox1.Text += "無圖可存\n";
                show_main_message("無圖可存", S_OK, 20);
            }
        }

        void show_main_message(string mesg, int number, int timeout)
        {
            lb_main_mesg.Text = mesg;

            timer_display_show_main_mesg_count = 0;
            timer_display_show_main_mesg_count_target = timeout;   //timeout in 0.1 sec
            timer_display.Enabled = true;
        }

        private void timer_display_Tick(object sender, EventArgs e)
        {
            if (timer_display_show_main_mesg_count < timer_display_show_main_mesg_count_target)      //display main message timeout
            {
                timer_display_show_main_mesg_count++;
                if (timer_display_show_main_mesg_count >= timer_display_show_main_mesg_count_target)
                    lb_main_mesg.Text = "";
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

                if (flag_recording == true)
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

                string str = DateTime.Now.ToString();
                SolidBrush sb = new SolidBrush(Color.Green);
                Font f = new Font("Arial", 14, FontStyle.Bold);

                Graphics g = Graphics.FromImage(bitmap1);
                g.DrawString(str, f, sb, new Point(10, 10));

                if (flag_recording == true)
                {
                    try
                    {
                        writer2.WriteVideoFrame(bitmap1);
                    }
                    catch (Exception ex)
                    {
                        //richTextBox1.Text += "xxx錯誤訊息e02 : " + ex.Message + "\n";
                    }
                }
                GC.Collect();       //回收資源
            }
            catch (InvalidOperationException ex)
            {
                //richTextBox1.Text += "xxx錯誤訊息e03 : " + ex.Message + "\n";
            }
        }

        // output video resolution info
        bool isResolutionSet = false;
        int Width = 0;
        int Height = 0;

        private bool flag_recording = false;    //判斷是否啟動錄影的旗標, for 錄影

        public string RecordingFilename = "aaaaa.avi";

        private void DoRecord()
        {
            // we set our VideoFileWriter as well as the file name, resolution and fps
            VideoFileWriter writer1 = new VideoFileWriter();

            writer1.Open(RecordingFilename, this.Width, this.Height, 30);

            writer1.Close();
        }

        public void StartRecording2()
        {
            if (flag_recording == false)
            {
                flag_recording = true;
                writer2.Open(RecordingFilename, this.Width, this.Height, 30);
            }
        }

        public void StopRecording2()
        {
            flag_recording = false;
            writer2.Close();
        }
    }
}

