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
using AForge.Video.DirectShow;
//using AForge.Video.FFMPEG;      //for VideoFileWriter

using AForge.Vision.Motion;     // Motion detection
/*
移動偵測 需要 參考/加入參考/選取以下3個dll
AForge.dll
AForge.Imaging.dll
AForge.Vision.dll
*/

//參考
//【AForge.NET】C#上使用AForge.Net擷取視訊畫面
//https://ccw1986.blogspot.com/2013/01/ccaforgenetcapture-image.html

//AForge下載鏈結
//http://www.aforgenet.com/framework/downloads.html

/*
Aforge.Net 安裝路徑設定
Solution Explorer(方案總管) => References(參考)(右鍵) => Add Reference(加入參考) => AForge.Net的Release資料夾
加入AForge.Video.dll、AForge.Video.DirectShow.dll
*/

namespace vcs_WebCam
{
    public partial class Form1 : Form
    {
        public FilterInfoCollection USBWebcams = null;
        public VideoCaptureDevice Cam = null;
        RotateFlipType rotate_flip_type = RotateFlipType.RotateNoneFlipNone;

        List<string> camera_short_name = new List<string>();      //一維List for string
        List<string> camera_full_name = new List<string>();      //一維List for string
        List<int[]> camera_capability = new List<int[]>();  //二維List for int

        int webcam_count = 0;

        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE
        private const int BORDER = 10;

        private const int W_groupBox1 = 640 * 2 + BORDER;
        private const int H_groupBox1 = 220;
        private const int W_pictureBox1 = 640;
        private const int H_pictureBox1 = 480;
        private const int W_richTextBox1 = 640;
        private const int H_richTextBox1 = 480;

        int timer_display_show_main_mesg_count = 0;
        int timer_display_show_main_mesg_count_target = 0;

        bool flag_fullscreen = false;
        bool flag_show_time = true;     //顯示時間
        bool flag_show_grid = true;     //顯示格線
        bool flag_invert = false;        //反相, SC700需要反相
        bool flag_auto_save = false;    //自動存檔

        int webcam_w = 0;
        int webcam_h = 0;
        int webcam_fps = 0;

        bool debug_mode = true;

        bool flag_motion_detection = false;
        MotionDetector motion_detector;

        public struct RGB
        {
            private byte _r;
            private byte _g;
            private byte _b;

            public RGB(byte r, byte g, byte b)
            {
                this._r = r;
                this._g = g;
                this._b = b;
            }

            public byte R
            {
                get { return this._r; }
                set { this._r = value; }
            }

            public byte G
            {
                get { return this._g; }
                set { this._g = value; }
            }

            public byte B
            {
                get { return this._b; }
                set { this._b = value; }
            }

            public bool Equals(RGB rgb)
            {
                return (this.R == rgb.R) && (this.G == rgb.G) && (this.B == rgb.B);
            }
        }

        public struct YUV
        {
            private double _y;
            private double _u;
            private double _v;

            public YUV(double y, double u, double v)
            {
                this._y = y;
                this._u = u;
                this._v = v;
            }

            public double Y
            {
                get { return this._y; }
                set { this._y = value; }
            }

            public double U
            {
                get { return this._u; }
                set { this._u = value; }
            }

            public double V
            {
                get { return this._v; }
                set { this._v = value; }
            }

            public bool Equals(YUV yuv)
            {
                return (this.Y == yuv.Y) && (this.U == yuv.U) && (this.V == yuv.V);
            }
        }

        public static YUV RGBToYUV(RGB rgb)
        {
            double y = rgb.R * .299000 + rgb.G * .587000 + rgb.B * .114000;
            double u = rgb.R * -.168736 + rgb.G * -.331264 + rgb.B * .500000 + 128;
            double v = rgb.R * .500000 + rgb.G * -.418688 + rgb.B * -.081312 + 128;

            return new YUV(y, u, v);
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //C# 跨 Thread 存取 UI
            Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效

            pictureBox1.KeyDown += new KeyEventHandler(pictureBox1_KeyDown);
            this.ActiveControl = pictureBox1;//选中pictureBox1，不然没法触发事件

            show_item_location();
            Init_WebcamSetup();

            //初始化motion detector
            motion_detector = new MotionDetector(new TwoFramesDifferenceDetector(), new MotionAreaHighlighting());

            pictureBox1.Image = vcs_WebCam.Properties.Resources.chicken;
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            groupBox1.Size = new Size(W_groupBox1, H_groupBox1);
            groupBox1.Location = new Point(BORDER, BORDER);

            pictureBox1.Size = new Size(W_pictureBox1, H_pictureBox1);
            pictureBox1.Location = new Point(BORDER, BORDER + H_groupBox1 + BORDER);

            richTextBox1.Size = new Size(W_richTextBox1, H_richTextBox1);
            richTextBox1.Location = new Point(BORDER + W_pictureBox1 + BORDER, BORDER + H_groupBox1 + BORDER);

            int w = BORDER + W_groupBox1 + BORDER;
            int h = BORDER + H_groupBox1 + BORDER + H_pictureBox1 + BORDER;
            this.ClientSize = new Size(w, h);

            int W = Screen.PrimaryScreen.WorkingArea.Width;
            int H = Screen.PrimaryScreen.WorkingArea.Height;

            this.Location = new Point((W - w) / 2, (H - h) / 2);    //置中顯示

            w = (W_groupBox1 - BORDER * 5 - 100) / 4;
            h = 190;
            groupBox2.Size = new Size(w, h);
            groupBox3.Size = new Size(w, h);
            groupBox4.Size = new Size(w + 100, h);
            groupBox5.Size = new Size(w, h);

            //button
            x_st = BORDER;
            y_st = BORDER;

            dx = w + BORDER;
            dy = 42;
            y_st = BORDER * 2;

            if (debug_mode == true)
            {
                groupBox2.Location = new Point(x_st + dx * 0, y_st + dy * 0);
                groupBox3.Location = new Point(x_st + dx * 1, y_st + dy * 0);
                groupBox4.Location = new Point(x_st + dx * 2, y_st + dy * 0);
                groupBox5.Location = new Point(x_st + dx * 3 + 100, y_st + dy * 0);
            }
            else
            {
                groupBox2.Visible = false;
                groupBox3.Location = new Point(x_st + dx * 0, y_st + dy * 0);
                groupBox4.Location = new Point(x_st + dx * 1, y_st + dy * 0);
                groupBox5.Location = new Point(x_st + dx * 2 + 100, y_st + dy * 0);
                groupBox5.Size = new Size(w + 250, h);
                richTextBox1.Visible = false;
                bt_record.Visible = false;
                bt_clear.Visible = false;
                cb_image_processing.Visible = false;
                cb_auto_save.Visible = false;
                cb_show_grid.Visible = false;
                rb1.Visible = false;
                rb2.Visible = false;
                rb3.Visible = false;
            }

            //groupBox2
            x_st = BORDER;
            y_st = BORDER * 2;
            dx = 80;
            dy = 30;
            checkBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            checkBox2.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            checkBox3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            radioButton1.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            radioButton2.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            checkBox1.Enabled = false;
            checkBox2.Enabled = false;
            radioButton1.Enabled = false;
            radioButton2.Enabled = false;

            //groupBox3
            x_st = BORDER;
            y_st = BORDER * 2;
            dx = 210;
            dy = 26;
            label1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            label2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            label3.Location = new Point(x_st + dx * 0, y_st + dy * 4);

            comboBox1.Size = new Size(230, 30);
            comboBox2.Size = new Size(230, 30);
            comboBox3.Size = new Size(230, 30);
            comboBox1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            comboBox2.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            comboBox3.Location = new Point(x_st + dx * 0, y_st + dy * 5);

            //groupBox4
            x_st = BORDER;
            y_st = BORDER * 2;
            dx = 80;
            dy = 40;
            bt_start.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_pause.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_stop.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt_record.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_refresh.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_snapshot.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            bt_motion_detection.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            bt_exit.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            bt_info.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            bt_fullscreen.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            bt_help.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            bt_open_folder.Location = new Point(x_st + dx * 4 - 20, y_st + dy * 2 + 20);
            bt_open_folder.BackgroundImage = Properties.Resources.folder_open;

            cb_show_time.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            cb_image_processing.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            cb_auto_save.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            cb_show_grid.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            cb_rgb.Location = new Point(x_st + dx * 0, y_st + dy * 3 + 25);
            cb_corner.Location = new Point(x_st + dx * 1, y_st + dy * 3 + 25);

            rb1.Location = new Point(x_st + dx * 2, y_st + dy * 3 + 25);
            rb2.Location = new Point(x_st + dx * 2 + 30, y_st + dy * 3 + 25);
            rb3.Location = new Point(x_st + dx * 2 + 60, y_st + dy * 3 + 25);

            rb_3X3.Location = new Point(x_st + dx * 3 + 45, y_st + dy * 3 - 20);
            rb_4X4.Location = new Point(x_st + dx * 3 + 45, y_st + dy * 3);
            rb_5X5.Location = new Point(x_st + dx * 3 + 45, y_st + dy * 3 + 20);

            rb_3X3.Visible = false;
            rb_4X4.Visible = false;
            rb_5X5.Visible = false;

            //groupBox5
            x_st = BORDER;
            y_st = BORDER * 2;
            dx = 80;
            dy = 50;
            lb_main_mesg.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            lb_fps.Location = new Point(x_st + dx * 0, y_st + dy * 1);


            x_st = BORDER;
            y_st = 120;
            dx = 55;
            dy = 30;

            lb_rgb_r.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            lb_rgb_g.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            lb_rgb_b.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            lb_yuv_y.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            lb_yuv_u.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            lb_yuv_v.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            panel1.Location = new Point(x_st + dx * 3 + 10, y_st + dy * 0);



            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            lb_main_mesg.Text = "";

            bt_start.Enabled = true;
            bt_stop.Enabled = false;
            bt_record.Enabled = false;
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //窗口關閉事件
        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            try
            {
                if (Cam != null)
                {
                    //關閉WebCam
                    if (Cam.IsRunning)  // When Form1 closes itself, WebCam must stop, too.
                    {
                        Cam.Stop();   // WebCam stops capturing images.
                        Cam.SignalToStop();
                        Cam.WaitForStop();
                        while (Cam.IsRunning)
                        {
                        }
                        Cam = null;
                    }
                }
                //System.Environment.Exit(0);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }

            //C# 強制關閉 Process
            Process.GetCurrentProcess().Kill();

            Application.Exit();
        }

        void Init_WebcamSetup()         //讀出目前相機資訊 存在各list, comboBox1~3和richTextBox1裏
        {
            camera_short_name.Clear();
            camera_full_name.Clear();
            camera_capability.Clear();
            comboBox1.Items.Clear();
            comboBox2.Items.Clear();
            comboBox3.SelectedIndex = 0;

            try
            {
                USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice); //實例化對象
                webcam_count = USBWebcams.Count;
                richTextBox1.Text += "找到 " + webcam_count.ToString() + " 台WebCam\n";

                richTextBox1.Text += "USBWebcams.Capacity : " + USBWebcams.Capacity.ToString() + "\n";
                richTextBox1.Text += "USBWebcams.Count : " + USBWebcams.Count.ToString() + "\n";

                int i = 0;
                foreach (FilterInfo vidDevice in USBWebcams)
                {
                    richTextBox1.Text += "第 " + (i + 1).ToString() + " 台WebCam:\n";
                    richTextBox1.Text += "短名 : " + vidDevice.Name + "\n";
                    richTextBox1.Text += "長名 : " + vidDevice.MonikerString + "\n";
                    richTextBox1.Text += "\n";
                    i++;
                }

                /* same
                for (i = 0; i < webcam_count; i++)
                {
                    richTextBox1.Text += "第 " + (i + 1).ToString() + " 台WebCam:\n";
                    richTextBox1.Text += "短名 : " + USBWebcams[i].Name + "\n";
                    richTextBox1.Text += "長名 : " + USBWebcams[i].MonikerString + "\n";
                    richTextBox1.Text += "\n";
                }
                richTextBox1.Text += "\n";
                */

                //抓出並顯示所有顯示能力
                if (webcam_count > 0)  // The quantity of WebCam must be more than 0.
                {
                    for (i = 0; i < webcam_count; i++)
                    {
                        Cam = new VideoCaptureDevice(USBWebcams[i].MonikerString);  //實例化對象

                        richTextBox1.Text += "第 " + (i + 1).ToString() + " 台WebCam:\n";
                        richTextBox1.Text += "短名 : " + USBWebcams[i].Name + "\n";
                        richTextBox1.Text += "ProvideSnapshots = " + Cam.ProvideSnapshots.ToString() + "\n";
                        if (Cam.ProvideSnapshots == true)
                        {
                            richTextBox1.Text += "Snapshot len = " + Cam.SnapshotCapabilities.Length.ToString() + "\n";
                            richTextBox1.Text += "Snapshot W = " + Cam.SnapshotResolution.FrameSize.Width.ToString() + "\n";
                            richTextBox1.Text += "Snapshot H = " + Cam.SnapshotResolution.FrameSize.Height.ToString() + "\n";
                            richTextBox1.Text += "Snapshot FR = " + Cam.SnapshotResolution.MaximumFrameRate.ToString() + "\n";
                        }
                        richTextBox1.Text += "顯示能力 VideoCapabilities.Length " + Cam.VideoCapabilities.Length.ToString() + "\n";
                        var videoCapabilities = Cam.VideoCapabilities;
                        foreach (var video in videoCapabilities)
                        {
                            /*
                            richTextBox1.Text += "預覽分辨率 : " + video.FrameSize.Width.ToString() + " X " + video.FrameSize.Height.ToString() + "\n";
                            richTextBox1.Text += "AverageFrameRate : " + video.AverageFrameRate.ToString() + "\n";
                            richTextBox1.Text += "BitCount : " + video.BitCount.ToString() + "\n";
                            richTextBox1.Text += "MaximumFrameRate : " + video.MaximumFrameRate.ToString() + "\n";
                            string video_capability = video.FrameSize.Width.ToString() + " X " + video.FrameSize.Height.ToString() + " @ " + video.AverageFrameRate.ToString() + " Hz";
                            //comboBox2.Items.Add(video_capability);
                            */
                        }

                        string webcam_name;
                        if (USBWebcams[i].Name.Contains("Virtual"))
                        {
                            richTextBox1.Text += "跳過 Virtual\n";
                            webcam_name = (i + 1).ToString() + ". " + USBWebcams[i].Name;
                        }
                        else
                        {
                            camera_short_name.Add(USBWebcams[i].Name);
                            camera_full_name.Add(USBWebcams[i].MonikerString);

                            comboBox1.Items.Add(USBWebcams[i].Name);

                            int j;

                            for (j = 0; j < Cam.VideoCapabilities.Length; j++)
                            {
                                /*
                                richTextBox1.Text += "FR1 = " + Cam.VideoCapabilities[j].AverageFrameRate.ToString() + "\n";
                                //richTextBox1.Text += "FR1 = " + Cam.VideoCapabilities[j].FrameRate.ToString();
                                richTextBox1.Text += "W = " + Cam.VideoCapabilities[j].FrameSize.Width.ToString() + "\n";
                                richTextBox1.Text += "H = " + Cam.VideoCapabilities[j].FrameSize.Height.ToString() + "\n";
                                */
                                /*
                                richTextBox1.Text += "BitCount = " + Cam.VideoCapabilities[j].BitCount.ToString() + "\n";
                                richTextBox1.Text += "FR_max = " + Cam.VideoCapabilities[j].MaximumFrameRate.ToString() + "\n";
                                richTextBox1.Text += "ProvideSnapshots = " + Cam.ProvideSnapshots.ToString() + "\n";
                                if (Cam.ProvideSnapshots == true)
                                {
                                    richTextBox1.Text += "Snapshot len = " + Cam.SnapshotCapabilities.Length.ToString() + "\n";
                                    richTextBox1.Text += "Snapshot W = " + Cam.SnapshotResolution.FrameSize.Width.ToString() + "\n";
                                    richTextBox1.Text += "Snapshot H = " + Cam.SnapshotResolution.FrameSize.Height.ToString() + "\n";
                                    richTextBox1.Text += "Snapshot FR = " + Cam.SnapshotResolution.MaximumFrameRate.ToString() + "\n";
                                }
                                richTextBox1.Text += "Cam.Source = " + Cam.Source.ToString() + "\n";
                                richTextBox1.Text += "Cam.Source.Length = " + Cam.Source.Length.ToString() + "\n";
                                richTextBox1.Text += "FrameRate = " + Cam.VideoResolution.FrameRate.ToString() + "\n";    //old
                                richTextBox1.Text += "FrameSize.W = " + Cam.VideoResolution.FrameSize.Width.ToString() + "\n";
                                richTextBox1.Text += "FrameSize.H = " + Cam.VideoResolution.FrameSize.Height.ToString() + "\n";
                                */

                                webcam_name = (i + 1).ToString() + ". " + USBWebcams[i].Name + " "
                                    + Cam.VideoCapabilities[j].FrameSize.Width.ToString() + " X " + Cam.VideoCapabilities[j].FrameSize.Height.ToString()
                                    + " @ " + Cam.VideoCapabilities[j].AverageFrameRate.ToString() + " Hz";

                                richTextBox1.Text += webcam_name + "\n";

                                camera_capability.Add(new int[] { i, j });
                            }
                        }
                        richTextBox1.Text += "\n\n";
                    }
                    if (comboBox1.Items.Count > 0)
                        comboBox1.SelectedIndex = 0;

                    if (comboBox2.Items.Count > 0)
                        comboBox2.SelectedIndex = 0;
                }

                /*  reserved
                 * 
                    richTextBox1.Text += "aaaa SnapshotCapabilities.Length " + Cam.SnapshotCapabilities.Length.ToString() + "\n";
                    var snapVabalities = Cam.SnapshotCapabilities;
                    foreach (var snap in snapVabalities)
                    {
                        richTextBox1.Text += "Snapshot分辨率->" + snap.FrameSize.Width.ToString() + "*" + snap.FrameSize.Height.ToString() + "\n";
                        richTextBox1.Text += "Snapshot AverageFrameRate : " + snap.AverageFrameRate.ToString() + "\n";
                        richTextBox1.Text += "Snapshot BitCount : " + snap.BitCount.ToString() + "\n";
                        richTextBox1.Text += "Snapshot MaximumFrameRate : " + snap.MaximumFrameRate.ToString() + "\n";
                    }
                    //選擇Snapshot分辨率
                    if (snapVabalities.Count() > 0)
                    {
                        Cam.SnapshotResolution = Cam.SnapshotCapabilities.Last();
                    }

                    int len;
                    len = Cam.VideoCapabilities.Length;
                    for (i = 0; i < len; i++)
                    {
                        richTextBox1.Text += "BitCount = " + Cam.VideoCapabilities[i].BitCount.ToString() + "\t";
                        richTextBox1.Text += "MaximumFrameRate = " + Cam.VideoCapabilities[i].MaximumFrameRate.ToString() + "\t";
                        richTextBox1.Text += "fps = " + Cam.VideoCapabilities[i].AverageFrameRate.ToString() + "\t";
                        richTextBox1.Text += "W = " + Cam.VideoCapabilities[i].FrameSize.Width.ToString() + "\t";
                        richTextBox1.Text += "H = " + Cam.VideoCapabilities[i].FrameSize.Height.ToString() + "\n";
                    }
                */
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }

            if (webcam_count > 0)  //有相機存在
            {
                bt_start.Enabled = true;
                bt_pause.Enabled = true;
                bt_refresh.Enabled = true;
                bt_snapshot.Enabled = true;
                bt_fullscreen.Enabled = true;
            }
            else
            {
                bt_start.Enabled = false;
                bt_pause.Enabled = false;
                bt_refresh.Enabled = false;
                bt_snapshot.Enabled = false;
                bt_fullscreen.Enabled = false;
            }
            bt_stop.Enabled = false;
            bt_record.Enabled = false;

            return;
        }

        void Start_Webcam()
        {
            richTextBox1.Text += "選擇相機 : " + camera_short_name[comboBox1.SelectedIndex] + "\n";
            richTextBox1.Text += "選擇能力 : " + comboBox2.SelectedIndex.ToString() + "\n";
            richTextBox1.Text += "選擇方向 : " + comboBox3.SelectedIndex.ToString() + "\t" + comboBox3.Text + "\n";

            Cam = new VideoCaptureDevice(camera_full_name[comboBox1.SelectedIndex]);    //實例化對象

            //真正設定顯示能力的地方
            Cam.VideoResolution = Cam.VideoCapabilities[comboBox2.SelectedIndex];   //若有多個capabilities 可以更換

            Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);                 //綁定事件

            /* 以下為WebCam訊息
            richTextBox1.Text += "Cam.Source = " + Cam.Source + "\n";   //就是camera fullname
            richTextBox1.Text += "Cam.Source.Length " + Cam.Source.Length.ToString() + "\n";
            richTextBox1.Text += "VideoCapabilities.Length " + Cam.VideoCapabilities.Length.ToString() + "\n";
            var videoCapabilities = Cam.VideoCapabilities;
            foreach (var video in videoCapabilities)
            {
                richTextBox1.Text += "預覽分辨率 : " + video.FrameSize.Width.ToString() + " X " + video.FrameSize.Height.ToString() + "\n";
                richTextBox1.Text += "AverageFrameRate : " + video.AverageFrameRate.ToString() + "\n";
                richTextBox1.Text += "BitCount : " + video.BitCount.ToString() + "\n";
                richTextBox1.Text += "MaximumFrameRate : " + video.MaximumFrameRate.ToString() + "\n";
                string video_capability = video.FrameSize.Width.ToString() + " X " + video.FrameSize.Height.ToString() + " @ " + video.AverageFrameRate.ToString() + " Hz";
                richTextBox1.Text += video_capability + "\n";
            }
            */

            //以下為WebCam訊息
            string webcam_name = string.Empty;
            int ww = Cam.VideoCapabilities[comboBox2.SelectedIndex].FrameSize.Width;
            int hh = Cam.VideoCapabilities[comboBox2.SelectedIndex].FrameSize.Height;
            int fps = Cam.VideoCapabilities[comboBox2.SelectedIndex].AverageFrameRate;

            webcam_name = camera_short_name[comboBox1.SelectedIndex] + " "
                + ww.ToString() + " X "
                + hh.ToString() + " @ "
                + fps.ToString() + " Hz";
            this.Text = webcam_name;
            show_main_message(webcam_name, S_OK, 20);

            webcam_w = ww;
            webcam_h = hh;
            webcam_fps = fps;

            Cam.Start();   // WebCam starts capturing images.
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
            pictureBox1.Image = vcs_WebCam.Properties.Resources.chicken;
        }

        public Bitmap bm = null;
        int frame_cnt = 0;          //每多少張做一個計算
        int frame_count = 0;        //計算fps用
        int frame_count_old = 0;    //計算fps用
        DateTime dt_old = DateTime.Now;

        Graphics g;
        //SolidBrush drawBrush;
        Font drawFont1;

        int[] saturation_array = new int[81];
        int[] saturation_deny_array = new int[81];

        int awb_x = 0;
        int awb_y = 0;


        //自定義函數, 捕獲每一幀圖像並顯示
        private void Cam_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            frame_count++;
            if ((cb_show_time.Checked == false) && (cb_image_processing.Checked == false))      //直接顯示圖片
            {
                //pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();  //直接顯示圖片, 不能做任何處理
                bm = (Bitmap)eventArgs.Frame.Clone();
                //bm.RotateFlip(RotateFlipType.RotateNoneFlipY);
                bm.RotateFlip(rotate_flip_type);                        //鏡射旋轉
                //pictureBox1.Image = bm;

                GC.Collect();       //回收資源

                if (cb_corner.Checked == true)
                {
                    Graphics g;
                    try
                    {
                        g = Graphics.FromImage(bm);
                    }
                    catch (Exception ex)
                    {
                        GC.Collect();       //回收資源
                        return;
                    }

                    SolidBrush sb = new SolidBrush(Color.Black);
                    Point[] points = new Point[3];
                    int dd = 90;
                    points[0] = new Point(0, 0);
                    points[1] = new Point(dd, 0);
                    points[2] = new Point(0, dd);
                    g.FillPolygon(sb, points);
                    points[0] = new Point(640 - dd, 0);
                    points[1] = new Point(640, 0);
                    points[2] = new Point(640, dd);
                    g.FillPolygon(sb, points);
                    points[0] = new Point(0, 480);
                    points[1] = new Point(0, 480 - dd);
                    points[2] = new Point(dd, 480);
                    g.FillPolygon(sb, points);
                    points[0] = new Point(640 - dd, 480);
                    points[1] = new Point(640, 480);
                    points[2] = new Point(640, 480 - dd);
                    g.FillPolygon(sb, points);
                }

                if (flag_motion_detection == true)
                {
                    //Bitmap bitmap1 = (Bitmap)eventArgs.Frame.Clone(); // get a copy of the BitMap from the VideoCaptureDevice
                    Bitmap bitmap1 = (Bitmap)bm.Clone(); // get a copy of the BitMap from the VideoCaptureDevice
                    Bitmap bitmap2 = (Bitmap)bitmap1.Clone(); // clone the bits from the current frame

                    if (motion_detector.ProcessFrame(bitmap2) > 0.001) // feed the bits to the MD
                    {
                        this.Text = "移動";
                        Graphics g = Graphics.FromImage(bitmap1);
                        g.DrawRectangle(new Pen(Color.Red, 10), 0, 0, bitmap1.Width - 5, bitmap1.Height - 5);

                        pictureBox1.Image = bitmap1;
                    }
                    else
                    {
                        this.Text = "無移動";
                        pictureBox1.Image = bm;
                    }
                }
                else
                {
                    pictureBox1.Image = bm;

                }
            }
            else                //處理後再顯示圖片
            {
                //pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();  //直接顯示圖片
                bm = (Bitmap)eventArgs.Frame.Clone();
                //bm.RotateFlip(RotateFlipType.RotateNoneFlipY);
                bm.RotateFlip(rotate_flip_type);                        //鏡射旋轉

                g = Graphics.FromImage(bm);

                //畫截角
                if (cb_corner.Checked == true)
                {
                    SolidBrush sb = new SolidBrush(Color.Black);
                    Point[] points = new Point[3];
                    int dd = 90;
                    points[0] = new Point(0, 0);
                    points[1] = new Point(dd, 0);
                    points[2] = new Point(0, dd);
                    g.FillPolygon(sb, points);
                    points[0] = new Point(640 - dd, 0);
                    points[1] = new Point(640, 0);
                    points[2] = new Point(640, dd);
                    g.FillPolygon(sb, points);
                    points[0] = new Point(0, 480);
                    points[1] = new Point(0, 480 - dd);
                    points[2] = new Point(dd, 480);
                    g.FillPolygon(sb, points);
                    points[0] = new Point(640 - dd, 480);
                    points[1] = new Point(640, 480);
                    points[2] = new Point(640, 480 - dd);
                    g.FillPolygon(sb, points);
                }

                //顯示時間
                SolidBrush drawBrush;
                Font drawFont;
                string drawDate;
                int x_st = 0;
                int y_st = 0;

                if (cb_show_time.Checked == true)
                {
                    drawDate = DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss");
                    drawBrush = new SolidBrush(Color.Yellow);
                    drawFont = new Font("Arial", 6, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);

                    //在畫面的上方顯示時間
                    g.DrawString(drawDate, drawFont, drawBrush, BORDER, BORDER);
                }

                if (cb_image_processing.Checked == true)
                {
                    if (rb1.Checked == true)    //亮度
                    {
                        frame_cnt++;
                        if ((frame_cnt % 30) == 0)
                        {
                            //Bitmap bitmap1 = (Bitmap)pictureBox1.Image;
                            Bitmap bitmap1 = (Bitmap)eventArgs.Frame.Clone();   //重新抓圖, 以免拿到上面寫過字的圖
                            //bitmap1.RotateFlip(RotateFlipType.RotateNoneFlipX);

                            int WW = bitmap1.Width;
                            int HH = bitmap1.Height;
                            int i;
                            int j;
                            Color pt;
                            int ww = WW;
                            int hh = HH;
                            int total_Y = 0;

                            for (j = 0; j < hh; j++)
                            {
                                for (i = 0; i < ww; i++)
                                {
                                    pt = bitmap1.GetPixel(0 + i, 0 + j);

                                    RGB pp = new RGB(pt.R, pt.G, pt.B);
                                    YUV yyy = new YUV();
                                    yyy = RGBToYUV(pp);
                                    total_Y += (int)yyy.Y;
                                }
                            }

                            GC.Collect();       //回收資源
                            lb_main_mesg.Text = "亮度 : " + (total_Y / (ww * hh)).ToString();

                            /*  存圖備查
                            String filename = string.Empty;
                            filename = Application.StartupPath + "\\ims_image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");

                            //String file1 = file + ".jpg";
                            String filename2 = filename + ".bmp";
                            //String file3 = file + ".png";

                            //bitmap1.Save(@file1, ImageFormat.Jpeg);
                            bitmap1.Save(filename2, ImageFormat.Bmp);
                            //bitmap1.Save(@file3, ImageFormat.Png);
                            */
                        }
                    }
                    else if (rb2.Checked == true)   //做圖
                    {
                        bm = (Bitmap)eventArgs.Frame.Clone();
                        g = Graphics.FromImage(bm);

                        int i;
                        int j;
                        int A;
                        int R;
                        int G;
                        int B;

                        //int x_st = 0;
                        //int y_st = 0;


                        int W = bm.Width;
                        int H = bm.Height;
                        int center_x = W / 2;
                        int center_y = H / 2;

                        int awb_block = 32;     //AWB block size width, height
                        int awb_search_size = 256 + 32;   //256X256


                        x_st = center_x - awb_search_size / 2;
                        y_st = center_y - awb_search_size / 2;

                        for (i = 0; i <= (awb_search_size / awb_block); i++)
                        {
                            g.DrawLine(new Pen(Color.Red, 1), x_st, y_st + awb_block * i, x_st + awb_search_size - 1, y_st + awb_block * i);
                            g.DrawLine(new Pen(Color.Red, 1), x_st + awb_block * i, y_st, x_st + awb_block * i, y_st + awb_search_size - 1);
                        }

                        for (i = 0; i < saturation_array.Length; i++)
                        {
                            saturation_array[i] = 0;
                        }

                        int upper_bound = 255;
                        for (j = y_st; j < (y_st + awb_search_size); j++)
                        {
                            for (i = x_st; i < (x_st + awb_search_size); i++)
                            {
                                Color pp = bm.GetPixel(i, j);

                                A = pp.A;
                                R = pp.R;
                                G = pp.G;
                                B = pp.B;

                                if ((R >= upper_bound) && (G >= upper_bound) && (B >= upper_bound))
                                {
                                    saturation_array[((i - x_st) / awb_block) + (((j - y_st) / awb_block)) * (awb_search_size / awb_block)]++;

                                }
                            }
                        }

                        SolidBrush semiTransBrush = new SolidBrush(Color.FromArgb(40, 0, 255, 0));
                        SolidBrush semiTransBrushRed = new SolidBrush(Color.FromArgb(40, 255, 0, 0));
                        //richTextBox1.Text += "\nresult:\n";

                        int ii = 0;
                        int jj = 0;
                        int xx;
                        int yy;

                        for (i = 0; i < saturation_array.Length; i++)
                        {
                            //richTextBox1.Text += "saturation_array[" + i.ToString() + "] = " + saturation_array[i].ToString() + "\n";
                            if (saturation_array[i] <= 40)
                            {
                                if (saturation_deny_array[i] == 1)
                                {
                                    xx = (i % (awb_search_size / awb_block));
                                    yy = (i / (awb_search_size / awb_block));

                                    g.FillRectangle(semiTransBrushRed, new Rectangle(x_st + awb_block * xx, y_st + awb_block * yy, awb_block, awb_block));
                                }
                                else
                                {
                                    xx = (i % (awb_search_size / awb_block));
                                    yy = (i / (awb_search_size / awb_block));

                                    g.FillRectangle(semiTransBrush, new Rectangle(x_st + awb_block * xx, y_st + awb_block * yy, awb_block, awb_block));
                                }
                            }
                        }
                        semiTransBrush = new SolidBrush(Color.FromArgb(60, 255, 0, 0));
                        //g.FillRectangle(semiTransBrush, new Rectangle(x_st + awb_block * ii, y_st + awb_block * jj, awb_block, awb_block));
                        //g.DrawRectangle(new Pen(Color.Red, 3), new Rectangle(x_st + awb_block * ii + 3, y_st + awb_block * jj + 3, awb_block - 6, awb_block - 6));
                        g.DrawRectangle(new Pen(Color.Red, 1), new Rectangle(x_st + awb_block * ii + 2, y_st + awb_block * jj + 2, awb_block - 4, awb_block - 4));

                        drawBrush = new SolidBrush(Color.Red);
                        drawFont1 = new Font("Arial", 16, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);

                        x_st = 200;
                        y_st = 20;
                        //g.DrawString(tmp, drawFont1, drawBrush, x_st, y_st);

                        x_st = 580;
                        y_st = 390 - 100 + 30;

                        g.DrawRectangle(new Pen(Color.Red, 1), new Rectangle(x_st, y_st, 50, 25));
                        g.DrawRectangle(new Pen(Color.Red, 1), new Rectangle(x_st, y_st + 25, 50, 40));

                        //upper_bound
                        drawBrush = new SolidBrush(Color.Red);
                        drawFont1 = new Font("Arial", 6, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);
                        g.DrawString(upper_bound.ToString(), drawFont1, drawBrush, x_st, y_st);

                        g.DrawString(saturation_array[awb_x + awb_y * 9].ToString(), drawFont1, drawBrush, x_st + 8, y_st + 30);
                    }
                    else if (rb3.Checked == true)   //TBD
                    {

                    }
                    else
                    {

                    }
                }

                pictureBox1.Image = bm;

                GC.Collect();       //回收資源
            }
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            comboBox3.SelectedIndex = 0;
            comboBox2.Items.Clear();
            int i = comboBox1.SelectedIndex;
            richTextBox1.Text += "你選了 : " + i.ToString() + "  相機\n";
            VideoCaptureDevice Cam_tmp = null;
            Cam_tmp = new VideoCaptureDevice(USBWebcams[i].MonikerString);  //實例化對象

            string webcam_name;
            if (USBWebcams[i].Name.Contains("Virtual"))
            {
                richTextBox1.Text += "跳過 Virtual\n";
                webcam_name = (i + 1).ToString() + ". " + USBWebcams[i].Name;
            }
            else
            {
                int j;

                for (j = 0; j < Cam_tmp.VideoCapabilities.Length; j++)
                {
                    /*
                    richTextBox1.Text += "FR1 = " + Cam_tmp.VideoCapabilities[j].AverageFrameRate.ToString() + "\n";
                    //richTextBox1.Text += "FR1 = " + Cam_tmp.VideoCapabilities[j].FrameRate.ToString();
                    richTextBox1.Text += "W = " + Cam_tmp.VideoCapabilities[j].FrameSize.Width.ToString() + "\n";
                    richTextBox1.Text += "H = " + Cam_tmp.VideoCapabilities[j].FrameSize.Height.ToString() + "\n";
                    */
                    /*
                    richTextBox1.Text += "BitCount = " + Cam_tmp.VideoCapabilities[j].BitCount.ToString() + "\n";
                    richTextBox1.Text += "FR_max = " + Cam_tmp.VideoCapabilities[j].MaximumFrameRate.ToString() + "\n";
                    richTextBox1.Text += "ProvideSnapshots = " + Cam_tmp.ProvideSnapshots.ToString() + "\n";
                    if (Cam_tmp.ProvideSnapshots == true)
                    {
                    richTextBox1.Text += "Snapshot len = " + Cam_tmp.SnapshotCapabilities.Length.ToString() + "\n";
                    richTextBox1.Text += "Snapshot W = " + Cam_tmp.SnapshotResolution.FrameSize.Width.ToString() + "\n";
                    richTextBox1.Text += "Snapshot H = " + Cam_tmp.SnapshotResolution.FrameSize.Height.ToString() + "\n";
                    richTextBox1.Text += "Snapshot FR = " + Cam_tmp.SnapshotResolution.MaximumFrameRate.ToString() + "\n";
                    }
                    richTextBox1.Text += "Cam_tmp.Source = " + Cam_tmp.Source.ToString() + "\n";
                    richTextBox1.Text += "Cam_tmp.Source.Length = " + Cam_tmp.Source.Length.ToString() + "\n";
                    richTextBox1.Text += "FrameRate = " + Cam_tmp.VideoResolution.FrameRate.ToString() + "\n";    //old
                    richTextBox1.Text += "FrameSize.W = " + Cam_tmp.VideoResolution.FrameSize.Width.ToString() + "\n";
                    richTextBox1.Text += "FrameSize.H = " + Cam_tmp.VideoResolution.FrameSize.Height.ToString() + "\n";
                    */

                    webcam_name = Cam_tmp.VideoCapabilities[j].FrameSize.Width.ToString() + " X " + Cam_tmp.VideoCapabilities[j].FrameSize.Height.ToString()
                    + " @ " + Cam_tmp.VideoCapabilities[j].AverageFrameRate.ToString() + " Hz";

                    comboBox2.Items.Add(webcam_name);

                    richTextBox1.Text += webcam_name + "\n";
                }
            }
            if (comboBox2.Items.Count > 0)
                comboBox2.SelectedIndex = 0;
        }

        private void comboBox3_SelectedIndexChanged(object sender, EventArgs e)
        {
            richTextBox1.Text += "選了" + comboBox3.SelectedIndex.ToString() + "\n";
            switch (comboBox3.SelectedIndex)
            {
                case 0: rotate_flip_type = RotateFlipType.RotateNoneFlipNone; break;
                case 1: rotate_flip_type = RotateFlipType.RotateNoneFlipX; break;
                case 2: rotate_flip_type = RotateFlipType.RotateNoneFlipY; break;
                case 3: rotate_flip_type = RotateFlipType.RotateNoneFlipXY; break;
                case 4: rotate_flip_type = RotateFlipType.Rotate90FlipNone; break;
                case 5: rotate_flip_type = RotateFlipType.Rotate90FlipX; break;
                case 6: rotate_flip_type = RotateFlipType.Rotate90FlipY; break;
                case 7: rotate_flip_type = RotateFlipType.Rotate90FlipXY; break;
                case 8: rotate_flip_type = RotateFlipType.Rotate180FlipNone; break;
                case 9: rotate_flip_type = RotateFlipType.Rotate180FlipX; break;
                case 10: rotate_flip_type = RotateFlipType.Rotate180FlipY; break;
                case 11: rotate_flip_type = RotateFlipType.Rotate180FlipXY; break;
                case 12: rotate_flip_type = RotateFlipType.Rotate270FlipNone; break;
                case 13: rotate_flip_type = RotateFlipType.Rotate270FlipX; break;
                case 14: rotate_flip_type = RotateFlipType.Rotate270FlipY; break;
                case 15: rotate_flip_type = RotateFlipType.Rotate270FlipXY; break;
                default: rotate_flip_type = RotateFlipType.RotateNoneFlipNone; break;
            }
            richTextBox1.Text += "選了" + rotate_flip_type.ToString() + "\n";
        }

        bool camera_start = false;
        private void bt_start_Click(object sender, EventArgs e)
        {
            camera_start = true;
            Start_Webcam();
            bt_start.Enabled = false;
            bt_stop.Enabled = true;
            bt_record.Enabled = true;
        }

        private void bt_pause_Click(object sender, EventArgs e)
        {
            show_main_message("暫停 TBD", S_OK, 20);
        }

        private void bt_stop_Click(object sender, EventArgs e)
        {
            camera_start = false;
            Stop_Webcam();
            bt_start.Enabled = true;
            bt_stop.Enabled = false;
            bt_record.Enabled = false;
        }

        //重抓WebCam, 只有關了再開
        private void bt_refresh_Click(object sender, EventArgs e)
        {
            show_main_message("重抓", S_OK, 20);

            camera_start = false;

            Stop_Webcam();

            System.Threading.Thread.Sleep(100);

            camera_start = true;
            bt_start.Text = "停止";

            Start_Webcam();
        }

        private void bt_snapshot_Click(object sender, EventArgs e)
        {
            //save_image_to_drive();
            save_image_to_drive30();
        }

        private void bt_motion_detection_Click(object sender, EventArgs e)
        {
            if (flag_motion_detection == false)
            {
                flag_motion_detection = true;
                bt_motion_detection.Text = "移動偵測";

            }
            else
            {
                flag_motion_detection = false;
                bt_motion_detection.Text = "停止移動偵測";
            }
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            show_main_message("離開", S_OK, 20);
            Application.Exit();
        }

        private void bt_info_Click(object sender, EventArgs e)
        {
            int i;
            int j;

            richTextBox1.Text += "短名\n";
            for (i = 0; i < camera_short_name.Count; i++)
            {
                richTextBox1.Text += camera_short_name[i] + "\n";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "長名\n";
            for (i = 0; i < camera_full_name.Count; i++)
            {
                richTextBox1.Text += camera_full_name[i] + "\n";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "所有顯示能力\n";
            for (i = 0; i < camera_capability.Count; i++)
            {
                for (j = 0; j < 2; j++)
                {
                    richTextBox1.Text += camera_capability[i][j].ToString() + "\t";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";


            richTextBox1.Text += "USBWebcams.Count : " + USBWebcams.Count.ToString() + "\n";


            int webcam_count = USBWebcams.Count;
            richTextBox1.Text += "找到 " + webcam_count.ToString() + " 台WebCam\n";

            for (i = 0; i < webcam_count; i++)
            {
                richTextBox1.Text += "第 " + (i + 1).ToString() + " 台WebCam:\n";
                richTextBox1.Text += "短名 : " + USBWebcams[i].Name + "\n";
                richTextBox1.Text += "長名 : " + USBWebcams[i].MonikerString + "\n";
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";
        }

        private void bt_fullscreen_Click(object sender, EventArgs e)
        {
            if (flag_fullscreen == false)
            {
                flag_fullscreen = true;
                show_main_message("全螢幕", S_OK, 20);
                groupBox1.Visible = false;
                richTextBox1.Visible = false;
                bt_clear.Visible = false;

                this.BackColor = Color.Black;
                //最大化螢幕
                this.FormBorderStyle = FormBorderStyle.None;
                this.WindowState = FormWindowState.Maximized;
                //this.StartPosition = FormStartPosition.CenterScreen; //居中顯示

                pictureBox1.Size = new Size(1920, 1080);
                pictureBox1.Location = new Point(0, 0);
                pictureBox1.Focus();
            }
            else
            {
                flag_fullscreen = false;
                show_main_message("復原", S_OK, 20);
                groupBox1.Visible = true;
                if (debug_mode == true)
                {
                    richTextBox1.Visible = true;
                    bt_clear.Visible = true;
                }

                this.BackColor = System.Drawing.SystemColors.ControlLight;
                //最大化螢幕
                this.FormBorderStyle = FormBorderStyle.Sizable;
                this.WindowState = FormWindowState.Normal;
                //this.StartPosition = FormStartPosition.CenterScreen; //居中顯示

                pictureBox1.Size = new Size(W_pictureBox1, H_pictureBox1);
                pictureBox1.Location = new Point(BORDER, BORDER + H_groupBox1 + BORDER);
                pictureBox1.Focus();
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

        private void timer_clock_Tick(object sender, EventArgs e)
        {
            if (camera_start == true)
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
        }

        private void timer_auto_save_Tick(object sender, EventArgs e)
        {
            save_image_to_drive();
        }

        private void checkBox3_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox3.Checked == true)
            {
                richTextBox1.Visible = true;
                bt_clear.Visible = true;
            }
            else
            {
                richTextBox1.Visible = false;
                bt_clear.Visible = false;
            }
        }

        private void cb_auto_save_CheckedChanged(object sender, EventArgs e)
        {
            if (cb_auto_save.Checked == true)
            {
                timer_auto_save.Enabled = true;
            }
            else
            {
                timer_auto_save.Enabled = false;
            }
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

        void save_image_to_drive30()
        {
            show_main_message("截圖30", S_OK, 20);

            Bitmap bitmap1 = (Bitmap)pictureBox1.Image;

            //int W = bitmap1.Width;
            //int H = bitmap1.Height;
            //Bitmap bitmap_all = (Bitmap)pictureBox1.Image;

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            int i;
            int j;
            int k;
            Color pt;
            int total_pictures = 5;

            double[, ,] total_RGB = new double[W, H, 3];
            Bitmap bitmap_average = new Bitmap(W, H);

            for (k = 0; k < total_pictures; k++)
            {
                bitmap1 = (Bitmap)pictureBox1.Image;
                bitmap1.Save("picture" + k.ToString() + ".bmp", ImageFormat.Bmp);

                for (j = 0; j < H; j++)
                {
                    for (i = 0; i < W; i++)
                    {
                        pt = bitmap1.GetPixel(i, j);

                        double R = (double)pt.R;
                        double G = (double)pt.G;
                        double B = (double)pt.B;

                        total_RGB[i, j, 0] += R;
                        total_RGB[i, j, 1] += G;
                        total_RGB[i, j, 2] += B;

                        //bitmap_average.SetPixel(i, j, Color.FromArgb(pt.R, pt.G, pt.B));

                        if ((i == 320) && (j == 240))
                        {
                            richTextBox1.Text += "pt = " + pt.ToString() + "\n";
                            richTextBox1.Text += "R = " + R.ToString() + "\n";
                            richTextBox1.Text += "G = " + G.ToString() + "\n";
                            richTextBox1.Text += "B = " + B.ToString() + "\n";
                            richTextBox1.Text += "RR = " + total_RGB[i, j, 0].ToString() + "\n";
                            richTextBox1.Text += "GG = " + total_RGB[i, j, 1].ToString() + "\n";
                            richTextBox1.Text += "BB = " + total_RGB[i, j, 2].ToString() + "\n";
                        }
                    }
                }
                System.Threading.Thread.Sleep(200);
                Application.DoEvents();
            }


            richTextBox1.Text += "W = " + W.ToString() + "\n";
            richTextBox1.Text += "H = " + H.ToString() + "\n";
            
            for (j = 0; j < H; j++)
            {
                for (i = 0; i < W; i++)
                {

                    bitmap_average.SetPixel(i, j, Color.FromArgb(255, (byte)(total_RGB[i, j, 0] / total_pictures), (byte)(total_RGB[i, j, 1] / total_pictures), (byte)(total_RGB[i, j, 2] / total_pictures)));

                    if ((i == 320) && (j == 240))
                    {
                        richTextBox1.Text += "R = " + (total_RGB[i, j, 0] / total_pictures).ToString() + "\n";
                        richTextBox1.Text += "G = " + (total_RGB[i, j, 1] / total_pictures).ToString() + "\n";
                        richTextBox1.Text += "B = " + (total_RGB[i, j, 2] / total_pictures).ToString() + "\n";
                    }


                }
            }


            if (bitmap_average != null)
            {
                String filename = string.Empty;
                filename = Application.StartupPath + "\\ims_image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");

                //String file1 = file + ".jpg";
                String filename2 = filename + ".bmp";
                //String file3 = file + ".png";
                try
                {
                    //bitmap_average.Save(@file1, ImageFormat.Jpeg);
                    bitmap_average.Save(filename2, ImageFormat.Bmp);
                    //bitmap_average.Save(@file3, ImageFormat.Png);

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

        void pictureBox1_KeyDown(object sender, KeyEventArgs e)
        {
            switch (e.KeyCode)   //根據e.KeyCode分別執行
            {
                case Keys.Escape:
                    if (flag_fullscreen == true)
                    {
                        flag_fullscreen = false;
                        show_main_message("復原", S_OK, 20);
                        groupBox1.Visible = true;
                        richTextBox1.Visible = true;
                        bt_clear.Visible = true;

                        this.BackColor = System.Drawing.SystemColors.ControlLight;
                        //最大化螢幕
                        this.FormBorderStyle = FormBorderStyle.Sizable;
                        this.WindowState = FormWindowState.Normal;
                        //this.StartPosition = FormStartPosition.CenterScreen; //居中顯示

                        pictureBox1.Size = new Size(W_pictureBox1, H_pictureBox1);
                        pictureBox1.Location = new Point(BORDER, BORDER + H_groupBox1 + BORDER);
                        pictureBox1.Focus();
                    }
                    break;
                case Keys.X:
                    show_main_message("離開", S_OK, 20);
                    MessageBox.Show("版權沒有，歡迎散發", "WebCam");
                    Application.Exit();
                    break;
                case Keys.G:

                    break;
                case Keys.S:
                    save_image_to_drive();
                    break;
                case Keys.W:

                    break;
                case Keys.Space:

                    break;
                case Keys.Up:

                    break;
                case Keys.Down:

                    break;
                default:
                    //MessageBox.Show("x, KeyCode: " + e.KeyCode.ToString());
                    break;
            }
        }

        private void bt_help_Click(object sender, EventArgs e)
        {
            string message = string.Empty;
            message += "按 S 鍵 截圖\n";
            message += "按 ESC 鍵 離開全螢幕\n\n";
            message += "按 X 鍵 離開程式\n";
            MessageBox.Show(message, "WebCam操作說明");
        }

        private void bt_open_folder_Click(object sender, EventArgs e)
        {
            //開啟檔案總管
            Process.Start(Application.StartupPath);
        }

        private void pictureBox1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            if (flag_fullscreen == false)
            {
                flag_fullscreen = true;
                show_main_message("全螢幕", S_OK, 20);
                groupBox1.Visible = false;
                richTextBox1.Visible = false;
                bt_clear.Visible = false;

                this.BackColor = Color.Black;
                //最大化螢幕
                this.FormBorderStyle = FormBorderStyle.None;
                this.WindowState = FormWindowState.Maximized;
                //this.StartPosition = FormStartPosition.CenterScreen; //居中顯示

                pictureBox1.Size = new Size(1920, 1080);
                pictureBox1.Location = new Point(0, 0);
                pictureBox1.Focus();
            }
            else
            {
                flag_fullscreen = false;
                show_main_message("復原", S_OK, 20);
                groupBox1.Visible = true;
                if (debug_mode == true)
                {
                    richTextBox1.Visible = true;
                    bt_clear.Visible = true;
                }

                this.BackColor = System.Drawing.SystemColors.ControlLight;
                //最大化螢幕
                this.FormBorderStyle = FormBorderStyle.Sizable;
                this.WindowState = FormWindowState.Normal;
                //this.StartPosition = FormStartPosition.CenterScreen; //居中顯示

                pictureBox1.Size = new Size(W_pictureBox1, H_pictureBox1);
                pictureBox1.Location = new Point(BORDER, BORDER + H_groupBox1 + BORDER);
                pictureBox1.Focus();
            }
        }

        private void rb_processing_CheckedChanged(object sender, EventArgs e)
        {
            if (rb1.Checked == true)
            {
                show_main_message("亮度", S_OK, 30);
                timer_qr_code.Enabled = false;
            }
            else if (rb2.Checked == true)
            {
                show_main_message("畫圖", S_OK, 30);
                timer_qr_code.Enabled = false;
            }
            else if (rb3.Checked == true)
            {
                show_main_message("QR Code", S_OK, 30);
                timer_qr_code.Enabled = true;
            }
            else
            {
                timer_qr_code.Enabled = false;
                show_main_message("", S_OK, 30);
            }
        }

        private void timer_qr_code_Tick(object sender, EventArgs e)
        {
            if (camera_start == false)
                return;

            if (cb_image_processing.Checked == false)
                return;

            //  存圖用以後來解讀其中的資料
            string filename = Application.StartupPath + "\\image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
            Bitmap bmp = pictureBox1.Image as Bitmap;
            bmp.Save(filename, ImageFormat.Jpeg);
            //richTextBox1.Text += "pictureBox1存圖，存檔檔名：" + filename + "\n";

            Bitmap bitmap = null;
            //宣告 QRCode Reader 物件
            ZXing.IBarcodeReader reader = new ZXing.BarcodeReader();

            //讀取要解碼的圖片
            FileStream fs = new FileStream(filename, FileMode.Open);
            Byte[] data = new Byte[fs.Length];
            // 把檔案讀取到位元組陣列
            fs.Read(data, 0, data.Length);
            fs.Close();
            // 實例化一個記憶體資料流 MemoryStream，將位元組陣列放入
            MemoryStream ms = new MemoryStream(data);
            // 將記憶體資料流的資料放到 BitMap的物件中
            bitmap = (Bitmap)Image.FromStream(ms);

            //pictureBox2.Image = bitmap;       //將圖片顯示於 PictureBox 中

            //進行解碼的動作
            ZXing.Result result = reader.Decode(bitmap);

            if (result != null)
            {   //如果有成功解讀，則顯示文字
                richTextBox1.Text += "OK ";
                richTextBox1.Text += result.Text;
            }
            else
            {
                richTextBox1.Text += "解不出來 ";
            }
        }

        private void cb_show_grid_CheckedChanged(object sender, EventArgs e)
        {
            if (cb_show_grid.Checked == true)
            {
                flag_show_grid = true;
                rb_3X3.Visible = true;
                rb_4X4.Visible = true;
                rb_5X5.Visible = true;
            }
            else
            {
                flag_show_grid = false;
                rb_3X3.Visible = false;
                rb_4X4.Visible = false;
                rb_5X5.Visible = false;
            }
        }

        private void bt_record_Click(object sender, EventArgs e)
        {
            string filename = "test0.avi";
            int W = 640;
            int H = 480;
            //int frameRate = 25;
            if (File.Exists(filename) == true)
            {
                File.Delete(filename);
            }

            richTextBox1.Text += "W = " + webcam_w.ToString() + "\n";
            richTextBox1.Text += "H = " + webcam_h.ToString() + "\n";
            richTextBox1.Text += "F = " + webcam_fps.ToString() + "\n";

            richTextBox1.Text += "目前 AForge.Video.FFMPEG.dll 在 Sugar 上還不能用\n";
            //VideoFileWriter writer = new VideoFileWriter();

            //writer.Open(filename, webcam_w, webcam_h, webcam_fps, VideoCodec.MPEG4);
        }




        [DllImport("gdi32.dll")]
        static public extern uint GetPixel(IntPtr hDC, int XPos, int YPos);
        [DllImport("gdi32.dll")]
        static public extern IntPtr CreateDC(string driverName, string deviceName, string output, IntPtr lpinitData);
        [DllImport("gdi32.dll")]
        static public extern bool DeleteDC(IntPtr DC);
        static public byte GetRValue(uint color)
        {
            return (byte)color;
        }
        static public byte GetGValue(uint color)
        {
            return ((byte)(((short)(color)) >> 8));
        }
        static public byte GetBValue(uint color)
        {
            return ((byte)((color) >> 16));
        }
        static public byte GetAValue(uint color)
        {
            return ((byte)((color) >> 24));
        }

        public Color GetColor(Point screenPoint)
        {
            IntPtr displayDC = CreateDC("DISPLAY", null, null, IntPtr.Zero);
            uint colorref = GetPixel(displayDC, screenPoint.X, screenPoint.Y);
            DeleteDC(displayDC);
            byte Red = GetRValue(colorref);
            byte Green = GetGValue(colorref);
            byte Blue = GetBValue(colorref);
            return Color.FromArgb(Red, Green, Blue);
        }

        int cccc = 0;
        int total_RGB_R_old = -1;
        int total_RGB_G_old = -1;
        int total_RGB_B_old = -1;



        private void timer_rgb_Tick(object sender, EventArgs e)
        {
            if (cb_rgb.Checked == false)
                return;

            richTextBox1.Text += "x";

            Point pt = new Point(Control.MousePosition.X, Control.MousePosition.Y);
            Color cl = GetColor(pt);
            panel1.BackColor = cl;
            lb_rgb_r.Text = cl.R.ToString();
            lb_rgb_g.Text = cl.G.ToString();
            lb_rgb_b.Text = cl.B.ToString();

            RGB pp = new RGB(cl.R, cl.G, cl.B);
            YUV yyy = new YUV();
            yyy = RGBToYUV(pp);
            lb_yuv_y.Text = ((int)yyy.Y).ToString();
            lb_yuv_u.Text = ((int)yyy.U).ToString();
            lb_yuv_v.Text = ((int)yyy.V).ToString();
        }

        private void cb_rgb_CheckedChanged(object sender, EventArgs e)
        {
            if (cb_rgb.Checked == true)
            {
                timer_rgb.Enabled = true;
                lb_rgb_r.Visible = true;
                lb_rgb_g.Visible = true;
                lb_rgb_b.Visible = true;
                lb_yuv_y.Visible = true;
                lb_yuv_u.Visible = true;
                lb_yuv_v.Visible = true;
                panel1.Visible = true;
            }
            else
            {
                timer_rgb.Enabled = false;
                lb_rgb_r.Visible = false;
                lb_rgb_g.Visible = false;
                lb_rgb_b.Visible = false;
                lb_yuv_y.Visible = false;
                lb_yuv_u.Visible = false;
                lb_yuv_v.Visible = false;
                panel1.Visible = false;
            }
        }
    }
}
