using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using AForge.Video;
using AForge.Video.DirectShow;

using System.Drawing.Imaging;

namespace vcs_WebCam7
{
    public partial class Form1 : Form
    {
        private FilterInfoCollection USBWebcams = null;
        public VideoCaptureDevice Cam = null;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            //button
            int W = 640;
            int H = 480;
            int x_st = 10;
            int y_st = 10;
            int dx = W + 10;
            int dy = H + 10;
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1 + 70);

            pictureBox1.Size = new Size(W, H);
            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);

            richTextBox1.Size = new Size(W, H / 2 - 40);
            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1330, 750);
            this.Text = "vcs_WebCam7";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            //Stop_Webcam();
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

        //最小化WebCam設定
        void Init_WebcamSetup()
        {
            USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice);
            if (USBWebcams.Count > 0)
            {
                Cam = new VideoCaptureDevice(USBWebcams[0].MonikerString);  //實例化對象
                Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);

                //新版AForge才支持以下功能
                //以下為WebCam訊息與調整視窗大小
                Cam.VideoResolution = Cam.VideoCapabilities[0];
                int ww = Cam.VideoCapabilities[0].FrameSize.Width;
                int hh = Cam.VideoCapabilities[0].FrameSize.Height;
                string webcam_name = USBWebcams[0].Name + " " + Cam.VideoCapabilities[0].FrameSize.Width.ToString() + " X " + Cam.VideoCapabilities[0].FrameSize.Height.ToString() + " @ " + Cam.VideoCapabilities[0].AverageFrameRate.ToString() + " Hz";
                //this.Text = webcam_name;
            }
            else
            {
                this.Text = "無影像裝置";
            }
        }

        void Start_Webcam()
        {
            if (Cam != null)
            {
                Cam.Start();   // WebCam starts capturing images.
            }
        }

        void Stop_Webcam()
        {
            if (Cam != null)
            {
                //show_main_message("停止", S_OK, 20);
                Cam.Stop();  // WebCam stops capturing images.
                Cam.SignalToStop();
                Cam.WaitForStop();
                while (Cam.IsRunning)
                {
                    Console.Write("等候相機關閉");
                }
                Cam = null;
            }
            pictureBox1.Image = null;
        }

        public Bitmap bm = null;
        //自定義函數, 捕獲每一幀圖像並顯示
        void Cam_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            try
            {
                pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();
                //pictureBox1.Image = bm;

                GC.Collect();       //回收資源
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息n : " + ex.Message + "\n";
            }
            GC.Collect();       //回收資源
        }

        private void button0_Click(object sender, EventArgs e)
        {
            Init_WebcamSetup();
            Start_Webcam();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Stop_Webcam();
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/



/*
Image ImgOrnek = (Image.FromFile(pic_filename) as Bitmap).Clone() as Image;
int width = ImgOrnek.Width;
int height = ImgOrnek.Height;
ImgOrnek.Dispose();
VideoFileWriter writer = new VideoFileWriter();
writer.Open(filename, width, height, this.Videofps, VideoCodec.MPEG4);

                image = (Bitmap)Image.FromFile("C:\\Users\\Halil\\Desktop\\newframes\\image" + i + ".jpg");
                writer.WriteVideoFrame(image);

//------------------------------------------------------------  # 60個

*/





