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

namespace vcs_WebCam_AForge1
{
    public partial class Form1 : Form
    {
        //參考
        //【AForge.NET】C#上使用AForge.Net擷取視訊畫面
        //https://ccw1986.blogspot.com/2013/01/ccaforgenetcapture-image.html

        //AForge下載鏈結
        //http://www.aforgenet.com/framework/downloads.html

        public FilterInfoCollection USBWebcams = null;
        public VideoCaptureDevice Cam = null;
        RotateFlipType rotate_flip_type = RotateFlipType.RotateNoneFlipNone;
        bool flag_show_time = true;

        List<string> camera_short_name = new List<string>();      //一維List for string
        List<string> camera_full_name = new List<string>();      //一維List for string
        List<int[]> camera_capability = new List<int[]>();  //二維List for int

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
            Init_WebcamSetup();
        }

        void show_item_location()
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void Init_WebcamSetup()     //讀出目前相機資訊 存在各list, comboBox1~3和richTextBox1裏
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

                richTextBox1.Text += "USBWebcams.Capacity : " + USBWebcams.Capacity.ToString() + "\n";
                richTextBox1.Text += "USBWebcams.Count : " + USBWebcams.Count.ToString() + "\n";

                int webcam_count = USBWebcams.Count;
                richTextBox1.Text += "找到 " + webcam_count.ToString() + " 台WebCam\n";

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
                        richTextBox1.Text += "第 " + (i + 1).ToString() + " 台WebCam:\n";
                        richTextBox1.Text += "短名 : " + USBWebcams[i].Name + "\n";

                        Cam = new VideoCaptureDevice(USBWebcams[i].MonikerString);  //實例化對象

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

                if (webcam_count > 0)  //有相機存在
                {
                    button1.Enabled = true;
                    Cam = new VideoCaptureDevice(USBWebcams[0].MonikerString);  //實例化對象
                    ///---绑定事件
                    Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);

                    richTextBox1.Text += "Cam.Source = " + Cam.Source + "\n";
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
                        //comboBox2.Items.Add(video_capability);
                    }
                    comboBox2.SelectedIndex = 0;

                    //真正設定顯示能力的地方
                    if (videoCapabilities.Count() > 0)
                    {
                        Cam.VideoResolution = Cam.VideoCapabilities.Last(); //若有多個capabilities 可以更換, 真正設定顯示能力的地方

                        //可能寫法
                        //var videoCapabilities2 = Cam.VideoCapabilities;
                        //Cam.VideoResolution = videoCapabilities2[10];

                        //可能寫法
                        //Cam.VideoResolution = Cam.VideoCapabilities[4];
                        //Cam.VideoResolution = Cam.VideoCapabilities[comboBox2.SelectedIndex];   //若有多個capabilities 可以更換
                    }

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
                }
                else
                {
                    button1.Enabled = false;
                    richTextBox1.Text += "無影像裝置\n";
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
            return;
        }

        void Start_Webcam()
        {
            richTextBox1.Text += "選擇相機 : " + camera_short_name[comboBox1.SelectedIndex] + "\n";
            richTextBox1.Text += "選擇能力 : " + comboBox2.SelectedIndex.ToString() + "\n";
            richTextBox1.Text += "選擇方向 : " + comboBox3.SelectedIndex.ToString() + "\t" + comboBox3.Text + "\n";

            Cam = new VideoCaptureDevice(camera_full_name[comboBox1.SelectedIndex]);  //實例化對象
            Cam.VideoResolution = Cam.VideoCapabilities[comboBox2.SelectedIndex];   //若有多個capabilities 可以更換, 真正設定顯示能力的地方
            Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);

            Cam.Start();   // WebCam starts capturing images.
        }

        void Stop_Webcam()
        {
            Cam.Stop();  // WebCam stops capturing images.
            Cam.SignalToStop();
            Cam.WaitForStop();
            while (Cam.IsRunning)
            {
            }
            Cam = null;
        }

        public Bitmap bm = null;

        //自定義函數, 捕獲每一幀圖像並顯示
        private void Cam_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            //pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();
            bm = (Bitmap)eventArgs.Frame.Clone();
            //bm.RotateFlip(RotateFlipType.RotateNoneFlipY);
            bm.RotateFlip(rotate_flip_type);
            pictureBox1.Image = bm;

            GC.Collect();       //回收資源
        }

        int camera_start = 0;
        private void button1_Click(object sender, EventArgs e)
        {
            if (camera_start == 0)
            {
                camera_start = 1;
                button1.Text = "關閉Webcam";
                Start_Webcam();

            }
            else
            {
                camera_start = 0;
                button1.Text = "開啟Webcam";
                Stop_Webcam();
            }
        }

        //窗口關閉事件
        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
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

        private void button2_Click(object sender, EventArgs e)
        {
            this.pictureBox1.Focus();

            Bitmap bitmap1 = (Bitmap)pictureBox1.Image;

            if (bitmap1 != null)
            {
                IntPtr pHdc;
                Graphics g = Graphics.FromImage(bitmap1);
                Pen p = new Pen(Color.Red, 1);
                SolidBrush drawBrush = new SolidBrush(Color.Yellow);
                Font drawFont = new Font("Arial", 6, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);
                pHdc = g.GetHdc();

                if (flag_show_time == true)
                {   //顯示時間
                    int xPos = 10;
                    int yPos = 10;
                    string drawDate = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");

                    g.ReleaseHdc();
                    g.DrawString(drawDate, drawFont, drawBrush, xPos, yPos);
                }
                else
                {
                    g.ReleaseHdc();
                }
                g.Dispose();

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
            }
            else
            {
                richTextBox1.Text += "無圖可存\n";
            }
        }

        //重抓WebCam, 只有關了再開
        private void button3_Click(object sender, EventArgs e)
        {
            camera_start = 0;

            Stop_Webcam();

            System.Threading.Thread.Sleep(1000);

            camera_start = 1;
            button1.Text = "關閉Webcam";

            Start_Webcam();


        }

        private void button4_Click(object sender, EventArgs e)
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

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
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
    }
}
