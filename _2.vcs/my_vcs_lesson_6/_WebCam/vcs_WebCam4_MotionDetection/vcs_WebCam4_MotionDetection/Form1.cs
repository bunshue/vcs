using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using AForge.Video;             //需要添加這兩個.dll, 參考/加入參考/瀏覽此二檔
using AForge.Video.DirectShow;  // Video Recording
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

namespace vcs_WebCam4_MotionDetection
{
    public partial class Form1 : Form
    {
        private FilterInfoCollection USBWebcams = null;

        private const int BORDER = 10;
        private const int W_pictureBox1 = 640;
        private const int H_pictureBox1 = 480;
        private const int W_richTextBox1 = 300;
        private const int H_richTextBox1 = 480 - 60;

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

            pictureBox1.Size = new Size(W_pictureBox1, H_pictureBox1);
            pictureBox1.Location = new Point(BORDER, BORDER);

            richTextBox1.Size = new Size(W_richTextBox1, H_richTextBox1);
            richTextBox1.Location = new Point(BORDER + W_pictureBox1 + BORDER, BORDER + BORDER + 50);
            bt_motion_detection.Location = new Point(BORDER + W_pictureBox1 + BORDER, BORDER + BORDER);

            int w = BORDER + W_pictureBox1 + BORDER + W_richTextBox1 + BORDER;
            int h = BORDER + H_pictureBox1 + BORDER;
            this.ClientSize = new Size(w, h);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void Init_WebcamSetup()
        {
            USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice); //實例化對象
            if (USBWebcams.Count > 0)
            {
                string camera_name = USBWebcams[0].MonikerString;   //長名
                //this.CamMonitor = new CameraMonitor(pictureBox1, camera_name, "第 1 台攝影機");
                //flag_webcam_ok = true;
            }
        }
    }
}

