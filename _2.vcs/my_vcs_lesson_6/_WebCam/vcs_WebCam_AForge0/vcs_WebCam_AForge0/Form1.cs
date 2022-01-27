using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;       //for StopWatch
using System.Drawing.Imaging;   //for ImageFormat

using AForge.Video;             //需要添加這兩個.dll, 參考/加入參考/瀏覽此二檔
using AForge.Video.DirectShow;

//使用Aforge的VideoSourcePlayer, 在要再多添加4個.dll

/*
Aforge.Net 安裝路徑設定
Solution Explorer(方案總管) => References(參考)(右鍵) => Add Reference(加入參考) => AForge.Net的Release資料夾
加入AForge.Video.dll、AForge.Video.DirectShow.dll
*/

namespace vcs_WebCam_AForge0
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

        AForge.Controls.VideoSourcePlayer vsp;
        Stopwatch stopwatch;

        private const int BORDER = 30;

        public Form1()
        {
            InitializeComponent();
        }

        void show_item_location()
        {
            richTextBox1.Location = new Point(BORDER, BORDER + 480 + BORDER);
            richTextBox1.Size = new Size(640 * 2 + BORDER, 200);

            this.ClientSize = new Size(BORDER + 640 + BORDER + 640 + BORDER, BORDER + 480 + BORDER + 200 + BORDER);

            lb_fps.Text = "";
            lb_fps.Location = new Point(BORDER + 640 + BORDER + 640 + BORDER - 130, 5);

            pictureBox1.Size = new Size(640, 480);
            pictureBox1.Location = new Point(BORDER, BORDER);

            vsp.Size = new Size(640, 480);
            vsp.Location = new Point(BORDER + 640 + BORDER, BORDER);
            button1.Location = new Point(vsp.Location.X + vsp.Size.Width - button1.Size.Width, vsp.Location.Y);
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            vsp = new AForge.Controls.VideoSourcePlayer();
            this.Controls.Add(vsp);

            show_item_location();

            USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice);
            if (USBWebcams.Count > 0)  // The quantity of WebCam must be more than 0.
            {
                Cam = new VideoCaptureDevice(USBWebcams[0].MonikerString);  //實例化對象

                Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);
                Cam.Start();   // WebCam starts capturing images.

                vsp.VideoSource = Cam;
                vsp.Start();

                //以下為WebCam訊息與調整視窗大小
                Cam.VideoResolution = Cam.VideoCapabilities[0];
                string webcam_name = string.Empty;
                int ww;
                int hh;
                ww = Cam.VideoCapabilities[0].FrameSize.Width;
                hh = Cam.VideoCapabilities[0].FrameSize.Height;
                webcam_name = USBWebcams[0].Name + " " + Cam.VideoCapabilities[0].FrameSize.Width.ToString() + " X " + Cam.VideoCapabilities[0].FrameSize.Height.ToString() + " @ " + Cam.VideoCapabilities[0].AverageFrameRate.ToString() + " Hz";
                this.Text = webcam_name;

                //有抓到WebCam, 重新設定pictureBox和vsp的大小和位置
                pictureBox1.Size = new Size(ww, hh);
                pictureBox1.Location = new Point(BORDER, BORDER);
                vsp.Size = new Size(ww, hh);
                vsp.Location = new Point(BORDER + ww + BORDER, BORDER);
                button1.Location = new Point(vsp.Location.X + vsp.Size.Width - button1.Size.Width, vsp.Location.Y);

                stopwatch = new Stopwatch();
                stopwatch.Start();
            }
            else
            {
                this.Text = "無影像裝置";
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
            vsp.SignalToStop();
            vsp.WaitForStop();
        }

        public Bitmap bm = null;
        //自定義函數, 捕獲每一幀圖像並顯示
        void Cam_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            //pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();
            bm = (Bitmap)eventArgs.Frame.Clone();
            //bm.RotateFlip(RotateFlipType.RotateNoneFlipY);    //反轉
            pictureBox1.Image = bm;

            GC.Collect();       //回收資源
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (stopwatch == null)
            {
                stopwatch = new Stopwatch();
                stopwatch.Start();
            }
            else
            {
                stopwatch.Stop();

                IVideoSource ivs = vsp.VideoSource;
                int framesReceived1 = 0;

                // get number of frames for the last second
                if (ivs != null)
                {
                    framesReceived1 = ivs.FramesReceived;   //讀過資料後 會歸零

                    float fps = 1000.0f * framesReceived1 / stopwatch.ElapsedMilliseconds;

                    lb_fps.Text = fps.ToString("F2") + " fps";

                    stopwatch.Reset();
                    stopwatch.Start();
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
            var bitmap = vsp.GetCurrentVideoFrame();
            bitmap.Save(filename, System.Drawing.Imaging.ImageFormat.Jpeg);
            richTextBox1.Text += "已存檔 : " + filename + "\n";
        }
    }
}
