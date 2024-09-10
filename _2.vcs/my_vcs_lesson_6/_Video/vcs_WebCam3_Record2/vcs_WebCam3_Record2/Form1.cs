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

using AForge.Video;             //需要添加這兩個.dll, 參考/加入參考/瀏覽此二檔
using AForge.Video.DirectShow;  // Video Recording
using AForge.Video.FFMPEG;      //for VideoFileWriter

namespace vcs_WebCam3_Record2
{
    public partial class Form1 : Form
    {
        private FilterInfoCollection USBWebcams = null;
        private VideoCaptureDevice Cam = null;

        private bool flag_webcam_start = false;    //判斷是否啟動webcam的旗標
        private bool flag_recording = false;    //判斷是否啟動錄影的旗標

        int webcam_count = 0;

        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE
        private const int BORDER = 10;

        private string recording_filename = "XXXXXXX.avi";
        VideoFileWriter writer = new VideoFileWriter();
        DateTime recording_time_st = DateTime.Now;

        int timer_display_show_main_mesg_count = 0;
        int timer_display_show_main_mesg_count_target = 0;

        int webcam_w = 0;
        int webcam_h = 0;
        int webcam_fps = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
            //bt_start_Click(sender, e);
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            //離開程式前, 關閉相機(錄影與播放)
            ///先關閉錄影  再關閉播放

            if (flag_recording == true)
            {
                try
                {
                    bt_record_stop_Click(sender, e);
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "xxx錯誤訊息e01 : " + ex.Message + "\n";
                }
            }

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
            int dx = 140 + 50;
            int dy = 50 + 15;

            pictureBox1.Size = new Size(W, H);
            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox1.Image = vcs_WebCam3_Record2.Properties.Resources.ims_logo_720x480;

            richTextBox1.Size = new Size(300, 690);
            richTextBox1.Location = new Point(x_st + dx * 3 + 90, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            groupBox1.Size = new Size(640, 200);
            groupBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0 + H + BORDER);

            bt_record_stop.Enabled = false;
            this.Size = new Size(1000, 750);
            x_st = 10;
            y_st = 20;
            dx = 70 + 8;
            dy = 28;
            dy = 40 + 6;

            bt_start.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_stop.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_refresh.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt_exit.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_snapshot.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            bt_record_start.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            bt_record_stop.Location = new Point(x_st + dx * 6, y_st + dy * 0);

            lb_fps.Location = new Point(x_st + dx * 5 + 40, y_st + dy * 1);
            lb_fps.Text = "";
            lb_main_mesg.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            lb_main_mesg.Text = "";

            richTextBox1.BringToFront();
            bt_clear.BringToFront();

            bt_start.Enabled = true;
            bt_stop.Enabled = false;
            bt_refresh.Enabled = false;
            bt_exit.Enabled = true;
            bt_snapshot.Enabled = false;
            bt_record_start.Enabled = false;
            bt_record_stop.Enabled = false;
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //delay 10000 約 10秒
        //C# 不lag的延遲時間
        private void delay(int delay_milliseconds)
        {
            delay_milliseconds *= 2;
            DateTime time_before = DateTime.Now;
            while (((TimeSpan)(DateTime.Now - time_before)).TotalMilliseconds < delay_milliseconds)
            {
                Application.DoEvents();
            }
        }

        void Init_WebcamSetup() //最小化WebCam設定
        {
            try
            {
                USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice); //實例化對象
                webcam_count = USBWebcams.Count;
                if (webcam_count > 0)
                {
                    Cam = new VideoCaptureDevice(USBWebcams[0].MonikerString);  //實例化對象
                    Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);

                    //真正設定顯示能力的地方  Fail
                    //Cam.VideoResolution = Cam.VideoCapabilities[0];   //若有多個capabilities 可以更換

                    //richTextBox1.Text += "目前因為AF版本問題, 只能使用預設顯示能力\n";

                    /*
                    richTextBox1.Text += "DesiredFrameRate : " + Cam.DesiredFrameRate + "\n";
                    richTextBox1.Text += "DesiredFrameSize : " + Cam.DesiredFrameSize + "\n";
                    richTextBox1.Text += "VideoCapabilities : " + Cam.VideoCapabilities + "\n";
                    richTextBox1.Text += "顯示能力 VideoCapabilities.Length " + Cam.VideoCapabilities.Length.ToString() + "\n";
                    */

                    webcam_w = Cam.VideoCapabilities[0].FrameSize.Width;
                    webcam_h = Cam.VideoCapabilities[0].FrameSize.Height;
                    webcam_fps = Cam.VideoCapabilities[0].FrameRate;

                    //以下為WebCam訊息與調整視窗大小
                    //Cam.VideoResolution = Cam.VideoCapabilities[0];
                    string webcam_name = string.Empty;
                    //int ww = Cam.VideoCapabilities[0].FrameSize.Width;
                    int ww = webcam_w;
                    //int hh = Cam.VideoCapabilities[0].FrameSize.Height;
                    int hh = webcam_h;
                    //webcam_name = USBWebcams[0].Name + " " + ww.ToString() + " X " + hh.ToString() + " @ " + Cam.VideoCapabilities[0].AverageFrameRate.ToString() + " Hz";
                    //webcam_name = USBWebcams[0].Name + " " + ww.ToString() + " X " + hh.ToString();
                    webcam_name = "camera";
                    //richTextBox1.Text += "webcam_name = " + webcam_name + "\n";
                    //richTextBox1.Text += "webcam_name = " + webcam_name + "\n";
                    //richTextBox1.Text += "webcam_name = " + webcam_name + "\n";
                    this.Text = webcam_name;

                    //有抓到WebCam, 重新設定pictureBox和vsp的大小和位置
                    pictureBox1.Size = new Size(ww, hh);
                    //pictureBox1.Location = new Point(BORDER, BORDER);

                    webcam_w = ww;
                    webcam_h = hh;
                    //webcam_fps = fps;

                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }

            if (webcam_count > 0)  //有相機存在
            {
                bt_start.Enabled = true;
                bt_refresh.Enabled = true;
                bt_snapshot.Enabled = true;
            }
            else
            {
                bt_start.Enabled = false;
                bt_refresh.Enabled = false;
                bt_snapshot.Enabled = false;
            }
            bt_stop.Enabled = false;
            bt_record_start.Enabled = false;
            bt_record_stop.Enabled = false;
            return;
        }

        void Start_Webcam()
        {
            if (Cam != null)
            {
                Cam.Start();   // WebCam starts capturing images.
                flag_webcam_start = true;

                bt_start.Enabled = false;
                bt_stop.Enabled = true;
                bt_snapshot.Enabled = true;
                bt_record_start.Enabled = true;
                bt_record_stop.Enabled = false;

            }
            else
            {
                this.Text = "無影像裝置";
                flag_webcam_start = false;
            }
        }

        void Stop_Webcam()
        {
            if (Cam != null)
            {
                show_main_message("停止", S_OK, 20);
                Cam.Stop();  // WebCam stops capturing images.
                Cam.SignalToStop();
                Cam.WaitForStop();
                while (Cam.IsRunning)
                {
                }
                Cam = null;
            }
            pictureBox1.Image = vcs_WebCam3_Record2.Properties.Resources.ims_logo_720x480;
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

            try
            {
                bm = (Bitmap)eventArgs.Frame.Clone();
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息e04 : " + ex.Message + "\n";
            }

            g = Graphics.FromImage(bm);

            //顯示時間
            SolidBrush drawBrush;
            Font drawFont;
            string drawDate;

            drawDate = DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss");
            drawBrush = new SolidBrush(Color.Yellow);
            drawFont = new Font("Arial", 8, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);

            //在畫面的上方顯示時間
            g.DrawString(drawDate, drawFont, drawBrush, BORDER * 3, BORDER);

            if (flag_recording == true)
            {
                try
                {
                    writer.WriteVideoFrame(bm);
                }
                catch (Exception ex)
                {
                    Console.WriteLine("xxx錯誤訊息e01a : " + ex.Message);
                }
            }

            if (flag_recording == true)
            {
                TimeSpan diff = DateTime.Now - recording_time_st;
                int ms = diff.Milliseconds;
                if (ms < 500)
                {
                    int ww = 22;
                    try
                    {
                        g.FillEllipse(Brushes.Red, 640 - BORDER - ww, BORDER + 4, ww, ww);
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine("xxx錯誤訊息e01b : " + ex.Message);
                    }
                }
            }

            try
            {
                //bm.RotateFlip(RotateFlipType.RotateNoneFlipY);    //反轉
                pictureBox1.Image = bm;
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息e05 : " + ex.Message + "\n";
            }
            GC.Collect();       //回收資源
            return;
        }

        void do_record()
        {
            if (flag_webcam_start == false)    //如果webcam沒啟動
            {
                richTextBox1.Text += "無相機 / 相機未啟動\n";
                return;
            }

            if (flag_recording == false)
            {
                //開啟錄影模式
                recording_time_st = DateTime.Now;
                //int fps = webcam_fps;
                int fps = 30;   //16.79

                recording_filename = Application.StartupPath + "\\avi_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".avi";

                richTextBox1.Text += "\n開始錄影, 檔案 : " + recording_filename + "\n";
                richTextBox1.Text += "格式 : " + webcam_w.ToString() + " X " + webcam_h.ToString() + " @ " + fps.ToString() + " Hz\n";
                richTextBox1.Text += "時間 : " + recording_time_st.ToString() + "\n";

                //writer.Open(recording_filename, webcam_w, webcam_h, fps, VideoCodec.MPEG4);
                //writer.Open(recording_filename, webcam_w, webcam_h, fps, VideoCodec.WMV2); //容量較大
                writer.Open(recording_filename, webcam_w, webcam_h, fps, (VideoCodec)0);
                /*
                Default = -1,
                MPEG4 = 0,
                WMV1 = 1,
                WMV2 = 2,
                MSMPEG4v2 = 3,
                MSMPEG4v3 = 4,
                H263P = 5,
                FLV1 = 6,
                MPEG2 = 7,
                Raw = 8,
                //(VideoCodec)3;
                */
            }
            else
            {
                richTextBox1.Text += "已在錄影\n";
            }
        }

        //錄影 ST
        private void bt_record_start_Click(object sender, EventArgs e)
        {
            if (flag_webcam_start == false)    //如果webcam沒啟動
            {
                show_main_message("無相機 / 相機未啟動, 無錄影", S_OK, 20);
                return;
            }

            if (flag_recording == false)
            {
                //開啟錄影模式
                do_record();
                flag_recording = true;

                richTextBox1.Text += "錄影開始, 時間 : " + DateTime.Now.ToString() + "\n";
                recording_time_st = DateTime.Now;
                bt_record_start.Enabled = false;
                bt_record_stop.Enabled = true;
                bt_stop.Enabled = false;
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
                bt_record_stop.Text = "停止錄影";
                bt_record_stop.BackColor = Color.Red;

                //錄影完需將影像停止不然會出錯
                flag_recording = false;

                delay(250);//0.5秒

                writer.Close();

                richTextBox1.Text += "錄影結束, 時間 : " + DateTime.Now.ToString() + "\n";
                richTextBox1.Text += "錄影時間 : " + (DateTime.Now - recording_time_st).TotalSeconds.ToString("0.00") + " 秒\n";
                richTextBox1.Text += "錄影時間 : " + (DateTime.Now - recording_time_st).ToString() + "\n";
                richTextBox1.Text += "檔案 : " + recording_filename + "\n\n";

                bt_record_start.Enabled = true;
                bt_record_stop.Enabled = false;
                bt_stop.Enabled = true;

                bt_record_stop.Text = "錄影 SP";
                bt_record_stop.BackColor = SystemColors.ControlLight;
            }
            else
            {
                richTextBox1.Text += "並沒有在錄影\n";
            }
        }

        int min_old = 0;
        private void timer_fps_Tick(object sender, EventArgs e)
        {
            //一般播放顯示fps
            if (flag_webcam_start == true)
            {
                DateTime dt = DateTime.Now;
                lb_fps.Text = (((frame_count - frame_count_old) * 1000) / ((TimeSpan)(dt - dt_old)).TotalMilliseconds).ToString("F2") + " fps";
                dt_old = dt;
                frame_count_old = frame_count;
            }
            else
            {
                lb_fps.Text = "";
            }

            //錄影
            if (flag_recording == true)
            {
                int min = (int)((DateTime.Now - recording_time_st).TotalMinutes);
                if ((min > 0) && (min != min_old))
                {
                    richTextBox1.Text += "已錄影 " + min.ToString() + " 分\n";
                    min_old = min;
                }
            }
        }

        private void bt_start_Click(object sender, EventArgs e)
        {
            show_main_message("啟動", S_OK, 20);

            Init_WebcamSetup();
            Start_Webcam();

            if (flag_webcam_start == false)    //如果webcam沒啟動
            {
                show_main_message("相機啟動失敗", S_OK, 20);
                return;
            }
            bt_start.Enabled = false;
            bt_stop.Enabled = true;
            //bt_record.Enabled = true;
        }

        private void bt_stop_Click(object sender, EventArgs e)
        {
            flag_webcam_start = false;
            Stop_Webcam();

            bt_start.Enabled = true;
            bt_stop.Enabled = false;
            bt_refresh.Enabled = false;
            bt_exit.Enabled = true;
            bt_snapshot.Enabled = false;
            bt_record_start.Enabled = false;
            bt_record_stop.Enabled = false;
        }

        //重抓WebCam, 只有關了再開
        private void bt_refresh_Click(object sender, EventArgs e)
        {
            show_main_message("重抓", S_OK, 20);

            Stop_Webcam();

            System.Threading.Thread.Sleep(100);

            Init_WebcamSetup();

            show_main_message("啟動", S_OK, 20);
            Start_Webcam();
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            show_main_message("離開", S_OK, 20);
            bt_record_stop_Click(sender, e);
            Application.Exit();

            /*
            show_main_message("測試自動錄影", S_OK, 20);
            test_auto_record();
            */
        }

        private void bt_snapshot_Click(object sender, EventArgs e)
        {
            if (flag_webcam_start == false)    //如果webcam沒啟動
            {
                show_main_message("相機未啟動, 無存圖", S_OK, 20);
                return;
            }
            save_image_to_drive();
        }

        void save_image_to_drive()
        {
            show_main_message("截圖", S_OK, 20);

            Bitmap bitmap1 = (Bitmap)pictureBox1.Image;

            if (bitmap1 != null)
            {
                String filename = string.Empty;

                filename = Application.StartupPath + "\\image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");

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

        void test_auto_record()
        {
            if (flag_webcam_start == false)    //如果webcam沒啟動
            {
                show_main_message("相機未啟動, 無錄影", S_OK, 20);
                return;
            }

            for (int codec = 0; codec <= 8; codec++)
            {
                //開啟錄影模式
                flag_recording = true;
                recording_time_st = DateTime.Now;
                int fps = webcam_fps;

                //recording_filename = Application.StartupPath + "\\avi_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".avi";
                recording_filename = Application.StartupPath + "\\avi_test_mode_" + codec.ToString() + ".avi";

                richTextBox1.Text += "\n開始錄影, 檔案 : " + recording_filename + "\n";
                richTextBox1.Text += "格式 : " + webcam_w.ToString() + " X " + webcam_h.ToString() + " @ " + fps.ToString() + " Hz\n";
                richTextBox1.Text += "時間 : " + recording_time_st.ToString() + "\n";

                //writer.Open(recording_filename, webcam_w, webcam_h, fps, VideoCodec.MPEG4);
                //writer.Open(recording_filename, webcam_w, webcam_h, fps, VideoCodec.WMV2); //容量較大
                writer.Open(recording_filename, webcam_w, webcam_h, fps, (VideoCodec)codec);
                /*
                Default = -1,
                MPEG4 = 0,
                WMV1 = 1,
                WMV2 = 2,
                MSMPEG4v2 = 3,
                MSMPEG4v3 = 4,
                H263P = 5,
                FLV1 = 6,
                MPEG2 = 7,
                Raw = 8,

                //(VideoCodec)3;
                */

                while (true)
                {
                    richTextBox1.Text += "XXXX";
                    break;
                    delay(100);
                }
            }
        }
    }
}
