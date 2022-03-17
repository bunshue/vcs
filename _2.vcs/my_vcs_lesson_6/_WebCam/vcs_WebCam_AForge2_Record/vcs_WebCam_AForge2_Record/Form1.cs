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
using System.Diagnostics;   //for Stopwatch

using AForge.Video;
using AForge.Video.DirectShow;  // Video Recording
//using AForge.Video.FFMPEG;      //for VideoFileWriter

using System.Drawing.Drawing2D;

using System.Drawing.Imaging;   //for PixelFormat

namespace vcs_WebCam_AForge2_Record
{
    public partial class Form1 : Form
    {
        public FilterInfoCollection USBWebcams = null;
        public VideoCaptureDevice Cam = null;
        private bool flag_webcam_ok = false;    //判斷是否啟動webcam的旗標
        Stopwatch stopwatch;

        private const int BORDER = 10;

        private bool flag_recording = false;    //判斷是否啟動錄影的旗標, for 錄影1
        private bool flag_limit_recording_time = false;
        private string recording_filename = string.Empty;
        //VideoFileWriter writer = new VideoFileWriter();
        DateTime recording_time_st = DateTime.Now;

        int webcam_w = 0;
        int webcam_h = 0;
        //int webcam_fps = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            recording_filename = Application.StartupPath + "\\avi_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".avi";

            USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice);
            if (USBWebcams.Count > 0)  // The quantity of WebCam must be more than 0.
            {
                Cam = new VideoCaptureDevice(USBWebcams[0].MonikerString);  //實例化對象

                Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);
                Cam.Start();   // WebCam starts capturing images.

                //以下為WebCam訊息與調整視窗大小
                //Cam.VideoResolution = Cam.VideoCapabilities[0];
                string webcam_name = string.Empty;
                int ww = Cam.VideoCapabilities[0].FrameSize.Width;
                int hh = Cam.VideoCapabilities[0].FrameSize.Height;
                //webcam_name = USBWebcams[0].Name + " " + ww.ToString() + " X " + hh.ToString() + " @ " + Cam.VideoCapabilities[0].AverageFrameRate.ToString() + " Hz";
                webcam_name = USBWebcams[0].Name + " " + ww.ToString() + " X " + hh.ToString();
                this.Text = webcam_name;

                //有抓到WebCam, 重新設定pictureBox和vsp的大小和位置
                pictureBox1.Size = new Size(ww, hh);
                //pictureBox1.Location = new Point(BORDER, BORDER);

                stopwatch = new Stopwatch();
                stopwatch.Start();
                flag_webcam_ok = true;

                webcam_w = ww;
                webcam_h = hh;
                //webcam_fps = fps;
            }
            else
            {
                this.Text = "無影像裝置";
                flag_webcam_ok = false;

            }

        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
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

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        public Bitmap bm = null;
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
            frame_count++;
            //pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();
            bm = (Bitmap)eventArgs.Frame.Clone();

            g = Graphics.FromImage(bm);

            //顯示時間
            SolidBrush drawBrush;
            Font drawFont;
            string drawDate;
            //int x_st = 0;
            //int y_st = 0;

            drawDate = DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss");
            drawBrush = new SolidBrush(Color.Yellow);
            drawFont = new Font("Arial", 6, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);

            //在畫面的上方顯示時間
            g.DrawString(drawDate, drawFont, drawBrush, BORDER * 3, BORDER);

            if (flag_recording == true)
            {
                if (DateTime.Now.Millisecond > 500)
                {
                    //g.DrawString("錄影中", drawFont, new SolidBrush(Color.Red), BORDER+230, BORDER);
                    g.FillEllipse(Brushes.Red, 5, BORDER, 25, 25);
                }

                try
                {
                    //writer.WriteVideoFrame(bm);
                }
                catch (Exception ex)
                {
                    //richTextBox1.Text += "xxx錯誤訊息e01 : " + ex.Message + "\n";
                }
            }

            //bm.RotateFlip(RotateFlipType.RotateNoneFlipY);    //反轉
            pictureBox1.Image = bm;

            GC.Collect();       //回收資源
        }

        void show_item_location()
        {
            int x_st = BORDER;
            int y_st = BORDER;
            int dx = 140 + 50;
            int dy = 50 + 15;

            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);

            richTextBox1.Size = new Size(300, 670);
            richTextBox1.Location = new Point(x_st + dx * 4 + 100, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            lb_fps.Text = "";
            lb_fps.Location = new Point(750, 5);
        }


        void do_record()
        {
            if (flag_webcam_ok == false)    //如果webcam沒啟動
            {
                richTextBox1.Text += "無相機\n";
                return;
            }

            if (flag_recording == false)
            {
                //開啟錄影模式
                flag_recording = true;

                recording_filename = Application.StartupPath + "\\avi_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".avi";

                richTextBox1.Text += "filename : " + recording_filename + "\n";
                richTextBox1.Text += "Width : " + webcam_w.ToString() + "\n";
                richTextBox1.Text += "Height : " + webcam_h.ToString() + "\n";

                int fps = 30;
                //writer.Open(recording_filename, webcam_w, webcam_h, fps, VideoCodec.MPEG4);
                //writer.Open(recording_filename, webcam_w, webcam_h, fps, VideoCodec.WMV2);

                richTextBox1.Text += "錄影開始\t時間 : " + DateTime.Now.ToString() + "\n";
                recording_time_st = DateTime.Now;
            }
            else
            {
                richTextBox1.Text += "已在錄影\n";
            }
        }
        //錄影 ST
        private void bt_record_start_Click(object sender, EventArgs e)
        {
            flag_limit_recording_time = false;
            do_record();
        }

        //錄影 ST, 有限時
        private void bt_record_start2_Click(object sender, EventArgs e)
        {
            flag_limit_recording_time = true;
            do_record();
        }

        //錄影 SP
        private void bt_record_stop_Click(object sender, EventArgs e)
        {
            if (flag_recording == true)
            {
                //錄影完需將影像停止不然會出錯
                flag_recording = false;

                //writer.Close();

                richTextBox1.Text += "錄影結束\t時間 : " + DateTime.Now.ToString() + "\n";
                richTextBox1.Text += "錄影時間 :\t" + (DateTime.Now - recording_time_st).TotalSeconds.ToString("0.00") + " 秒\n";
                //richTextBox1.Text += "錄影時間 : " + (DateTime.Now - recording_time_st).ToString() + "\n\n";
                richTextBox1.Text += "檔案 :\t\t" + recording_filename + "\n\n";
                flag_limit_recording_time = false;
            }
            else
            {
                richTextBox1.Text += "並沒有在錄影\n";
            }
        }

        int min_old = 0;
        private void timer_fps_Tick(object sender, EventArgs e)
        {
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

                    if (flag_limit_recording_time == true)
                    {
                        if ((DateTime.Now - recording_time_st).TotalSeconds > 180)
                        {
                            flag_limit_recording_time = false;
                            bt_record_stop_Click(sender, e);
                        }
                    }
                }
            }
            else
            {
                lb_fps.Text = "";
            }
        }

    }
}

