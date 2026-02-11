using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

using System.Diagnostics;       //for StopWatch
using System.Drawing.Imaging;   //for ImageFormat

using AForge.Video;             //需要添加這兩個.dll, 參考/加入參考/瀏覽此二檔
using AForge.Video.DirectShow;
//using AForge.Video.FFMPEG;


//使用Aforge的VideoSourcePlayer, 在要再多添加4個.dll

/*
Aforge.Net 安裝路徑設定
Solution Explorer(方案總管) => References(參考)(右鍵) => Add Reference(加入參考) => AForge.Net的Release資料夾
加入AForge.Video.dll、AForge.Video.DirectShow.dll
*/

namespace vcs_WebCam_AForge_VideoSourcePlayer2
{
    public partial class Form1 : Form
    {
        //參考
        //【AForge.NET】C#上使用AForge.Net擷取視訊畫面
        //https://ccw1986.blogspot.com/2013/01/ccaforgenetcapture-image.html

        //AForge下載鏈結
        //http://www.aforgenet.com/framework/downloads.html

        private FilterInfoCollection videoDevices;
        private AForge.Controls.VideoSourcePlayer videoSourcePlayer;

        public FilterInfoCollection USBWebcams = null;
        public VideoCaptureDevice Cam = null;

        AForge.Controls.VideoSourcePlayer vsp;
        Stopwatch stopwatch;

        private const int BORDER = 10;

        //开始录像
        private bool stopREC = true;
        private bool createNewFile = true;
        string videoPath = "";
        //private VideoFileWriter videoWriter;
        //private VideoFileWriter videoWriter1;
        int frameRate = 20; //默认帧率

        List<String> videos = new List<string>();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            videoPath = Application.StartupPath + "\\videos\\";
            if (!Directory.Exists(videoPath))
            {
                Directory.CreateDirectory(videoPath);
            }


            this.Size = new Size(1300, 800);
            richTextBox1.Size = new Size(300, 760);
            richTextBox1.Location = new Point(980, 0);

            try
            {
                // 枚举所有视频输入设备
                videoDevices = new FilterInfoCollection(FilterCategory.VideoInputDevice);

                if (videoDevices.Count == 0)
                {
                    throw new ApplicationException();
                }

                foreach (FilterInfo device in videoDevices)
                {
                    richTextBox1.Text += device.Name + "\n";

                    //tscbxCameras.Items.Add(device.Name);
                    //videos.Add(device.Name);
                }
                //tscbxCameras.SelectedIndex = 0;
            }
            catch (ApplicationException)
            {
                richTextBox1.Text += "無WebCam設備\n";
                videoDevices = null;
            }
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            videoSourcePlayer.SignalToStop();
            videoSourcePlayer.WaitForStop();

        }

        private void button0_Click(object sender, EventArgs e)
        {
            videoSourcePlayer = new AForge.Controls.VideoSourcePlayer();
            videoSourcePlayer.Size = new Size(640, 480);
            videoSourcePlayer.Location = new Point(250, 10);
            //videoSourcePlayer.NewFrame += new AForge.Controls.VideoSourcePlayer.NewFrameHandler(videoSourcePlayer_NewFrame);
            this.Controls.Add(videoSourcePlayer);

            int i = 0;
            VideoCaptureDevice videoSource = new VideoCaptureDevice(videoDevices[i].MonikerString);
            //videoSource.DesiredFrameSize = new System.Drawing.Size(320, 240);
            //videoSource.DesiredFrameRate = 1;

            videoSourcePlayer.VideoSource = videoSource;
            videoSourcePlayer.Start();

        }

        private void button1_Click(object sender, EventArgs e)
        {

        }
    }
}
