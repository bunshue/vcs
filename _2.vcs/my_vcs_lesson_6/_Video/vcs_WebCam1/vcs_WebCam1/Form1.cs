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

namespace vcs_WebCam1  //以此為準
{
    public partial class Form1 : Form
    {
        private FilterInfoCollection USBWebcams = null;
        private VideoCaptureDevice Cam = null;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //影像加上訊息
            pictureBox1.Paint += new PaintEventHandler(DrawMessage);

            Init_WebcamSetup();

            Start_Webcam();
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

        // 最小化WebCam設定
        void Init_WebcamSetup()
        {
            USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice);  // 實例化對象
            if (USBWebcams.Count > 0)
            {
                Cam = new VideoCaptureDevice(USBWebcams[0].MonikerString);  // 實例化對象, 長名
                Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);

                //新版AForge才支持以下功能
                //以下為WebCam訊息與調整視窗大小
                Cam.VideoResolution = Cam.VideoCapabilities[0];
                int ww = Cam.VideoCapabilities[0].FrameSize.Width;
                int hh = Cam.VideoCapabilities[0].FrameSize.Height;
                string webcam_name = USBWebcams[0].Name + " " + Cam.VideoCapabilities[0].FrameSize.Width.ToString() + " X " + Cam.VideoCapabilities[0].FrameSize.Height.ToString() + " @ " + Cam.VideoCapabilities[0].AverageFrameRate.ToString() + " Hz";
                this.Text = webcam_name;
            }
            else
            {
                this.Text = "無影像裝置";
            }
        }

        //影像加上訊息
        private void DrawMessage(object sender, PaintEventArgs e)
        {
            //顯示時間
            string drawDate = DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss");
            SolidBrush sb = new SolidBrush(Color.Green);
            Font f = new Font("Arial", 6, FontStyle.Bold, GraphicsUnit.Millimeter);
            e.Graphics.DrawString(drawDate, f, sb, new Point(10, 10));
        }

        public Bitmap bm = null;
        //自定義函數, 捕獲每一幀圖像並顯示
        void Cam_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            try
            {
                //pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();
                bm = (Bitmap)eventArgs.Frame.Clone();
                //bm.RotateFlip(RotateFlipType.RotateNoneFlipY);    //反轉
                pictureBox1.Image = bm;
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息n : " + ex.Message + "\n";
            }
            GC.Collect();       //回收資源
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
                Cam.Stop();
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
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個


// Stop_Webcam();

