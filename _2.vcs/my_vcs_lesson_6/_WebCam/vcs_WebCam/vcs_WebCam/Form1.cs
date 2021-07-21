using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat

using AForge.Video;             //需要添加這兩個.dll
using AForge.Video.DirectShow;

//參考
//【AForge.NET】C#上使用AForge.Net擷取視訊畫面
//https://ccw1986.blogspot.com/2013/01/ccaforgenetcapture-image.html

//AForge下載鏈結
//http://www.aforgenet.com/framework/downloads.html

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
        int timer_display_show_main_mesg_count = 0;
        int timer_display_show_main_mesg_count_target = 0;

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

            show_item_location();
            Init_WebcamSetup();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 210;
            dy = 42;

            groupBox1.Size = new Size(1120, 250);
            groupBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);

            pictureBox1.Size = new Size(640, 480);
            pictureBox1.Location = new Point(10, 270);

            richTextBox1.Size = new Size(300, 480);
            richTextBox1.Location = new Point(10 + 640 + 10, 270);

            y_st = 20;
            int w = 260;
            int h = 220;
            groupBox2.Size = new Size(w, h);
            groupBox3.Size = new Size(w, h);
            groupBox4.Size = new Size(w, h);
            groupBox5.Size = new Size(w, h);

            dx = w + 20;
            groupBox2.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            groupBox3.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            groupBox4.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            groupBox5.Location = new Point(x_st + dx * 3, y_st + dy * 0);

            //groupBox2
            x_st = 10;
            y_st = 20;
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
            x_st = 10;
            y_st = 20;
            dx = 210;
            dy = 30;
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
            x_st = 10;
            y_st = 20;
            dx = 80;
            dy = 50;
            bt_start.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_pause.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_stop.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt_refresh.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_snapshot.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            bt_exit.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            bt_info.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            bt_fullscreen.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            cb_show_time.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            cb_image_processing.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            cb_auto_save.Location = new Point(x_st + dx * 2, y_st + dy * 3);

            //groupBox5
            x_st = 10;
            y_st = 20;
            dx = 80;
            dy = 50;
            lb_main_mesg.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            lb_fps.Location = new Point(x_st + dx * 0, y_st + dy * 1);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            lb_main_mesg.Text = "";
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
                System.Environment.Exit(0);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
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

                        bool flag_use_first_non_virtual_camera = false;
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

                                if (flag_use_first_non_virtual_camera == false)
                                {
                                    //comboBox2.Items.Add(webcam_name);
                                }

                                richTextBox1.Text += webcam_name + "\n";

                                camera_capability.Add(new int[] { i, j });
                            }
                            flag_use_first_non_virtual_camera = true;
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
                bt_stop.Enabled = true;
                bt_refresh.Enabled = true;
                bt_snapshot.Enabled = true;
                bt_fullscreen.Enabled = true;
            }
            else
            {
                bt_start.Enabled = false;
                bt_pause.Enabled = false;
                bt_stop.Enabled = false;
                bt_refresh.Enabled = false;
                bt_snapshot.Enabled = false;
                bt_fullscreen.Enabled = false;
            }
            return;
        }

        void Start_Webcam()
        {
            richTextBox1.Text += "選擇相機 : " + camera_short_name[comboBox1.SelectedIndex] + "\n";
            richTextBox1.Text += "選擇能力 : " + comboBox2.SelectedIndex.ToString() + "\n";
            richTextBox1.Text += "選擇方向 : " + comboBox3.SelectedIndex.ToString() + "\t" + comboBox3.Text + "\n";

            Cam = new VideoCaptureDevice(camera_full_name[comboBox1.SelectedIndex]);    //實例化對象
            Cam.VideoResolution = Cam.VideoCapabilities[comboBox2.SelectedIndex];   //若有多個capabilities 可以更換, 真正設定顯示能力的地方
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

            //真正設定顯示能力的地方
            Cam.VideoResolution = Cam.VideoCapabilities[comboBox2.SelectedIndex];   //若有多個capabilities 可以更換

            //以下為WebCam訊息
            string webcam_name = string.Empty;
            int ww;
            int hh;
            ww = Cam.VideoCapabilities[comboBox2.SelectedIndex].FrameSize.Width;
            hh = Cam.VideoCapabilities[comboBox2.SelectedIndex].FrameSize.Height;
            webcam_name = camera_short_name[comboBox1.SelectedIndex] + " " + Cam.VideoCapabilities[comboBox2.SelectedIndex].FrameSize.Width.ToString() + " X " + Cam.VideoCapabilities[comboBox2.SelectedIndex].FrameSize.Height.ToString() + " @ " + Cam.VideoCapabilities[comboBox2.SelectedIndex].AverageFrameRate.ToString() + " Hz";
            this.Text = webcam_name;
            show_main_message(webcam_name, S_OK, 20);

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
        }

        public Bitmap bm = null;
        int frame_cnt = 0;          //每多少張做一個計算
        int frame_count = 0;        //計算fps用
        int frame_count_old = 0;    //計算fps用
        DateTime dt_old = DateTime.Now;

        //自定義函數, 捕獲每一幀圖像並顯示
        private void Cam_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            frame_count++;
            if (cb_show_time.Checked == false)      //直接顯示圖片
            {
                //pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();  //直接顯示圖片
                bm = (Bitmap)eventArgs.Frame.Clone();
                //bm.RotateFlip(RotateFlipType.RotateNoneFlipY);
                bm.RotateFlip(rotate_flip_type);                        //鏡射旋轉
                pictureBox1.Image = bm;

                GC.Collect();       //回收資源
            }
            else                //處理後再顯示圖片
            {
                //pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();  //直接顯示圖片
                bm = (Bitmap)eventArgs.Frame.Clone();
                //bm.RotateFlip(RotateFlipType.RotateNoneFlipY);
                bm.RotateFlip(rotate_flip_type);                        //鏡射旋轉

                Graphics g;
                g = Graphics.FromImage(bm);

                //顯示時間
                SolidBrush drawBrush;
                Font drawFont;
                string drawDate;
                int x_st = 0;
                int y_st = 0;

                drawDate = DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss");
                drawBrush = new SolidBrush(Color.Yellow);
                drawFont = new Font("Arial", 6, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);
                x_st = 10;
                y_st = 10;

                //在畫面的上方顯示時間
                g.DrawString(drawDate, drawFont, drawBrush, x_st, y_st);



                pictureBox1.Image = bm;

                GC.Collect();       //回收資源

            }

            if (cb_image_processing.Checked == true)
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
            if (camera_start == false)
            {
                camera_start = true;
                bt_start.Text = "停止";
                Start_Webcam();
            }
            else
            {
                camera_start = false;
                bt_start.Text = "啟動";
                Stop_Webcam();
            }
        }

        private void bt_pause_Click(object sender, EventArgs e)
        {
            show_main_message("暫停 TBD", S_OK, 20);
        }

        private void bt_stop_Click(object sender, EventArgs e)
        {
            camera_start = false;
            bt_start.Text = "啟動";
            Stop_Webcam();
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
            save_image_to_drive();
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
            show_main_message("全螢幕", S_OK, 20);
            groupBox1.Visible = false;
            richTextBox1.Visible = false;
            bt_clear.Visible = false;

            this.BackColor = Color.Black;
            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            //this.StartPosition = FormStartPosition.CenterScreen; //居中顯示

            this.pictureBox1.Size = new Size(1920, 1080);
            this.pictureBox1.Location = new Point(0, 0);
            //this.pictureBox1.Location = new Point((1920 - pictureBox1.Width) / 2, (1080 - pictureBox1.Height) / 2);
        }

        void show_main_message(string mesg, int number, int timeout)
        {
            lb_main_mesg.Text = mesg;
            //playSound(number);

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

                //bitmap1.Save(@file1, ImageFormat.Jpeg);
                bitmap1.Save(filename2, ImageFormat.Bmp);
                //bitmap1.Save(@file3, ImageFormat.Png);

                richTextBox1.Text += "存檔成功\n";
                //richTextBox1.Text += "已存檔 : " + file1 + "\n";
                richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                //richTextBox1.Text += "已存檔 : " + file3 + "\n";
                show_main_message("已存檔", S_OK, 10);
            }
            else
            {
                richTextBox1.Text += "無圖可存\n";
                show_main_message("無圖可存", S_OK, 20);
            }
        }
    }
}
