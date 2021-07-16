using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;   //for StopWatch

using AForge.Video;
using AForge.Video.DirectShow;

//需要添加6個.dll, 參考/加入參考/瀏覽6檔

namespace vcs_WebCam_AForge0b
{
    public partial class Form1 : Form
    {
        FilterInfoCollection USBWebcams;
        AForge.Controls.VideoSourcePlayer vsp;
        Stopwatch sw;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            lb_fps.Text = "";
            lb_fps.Location = new Point(680, 20);
            button1.Location = new Point(800, 20);
            richTextBox1.Location = new Point(680, 60);
            USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice);
            if (USBWebcams.Count > 0)  // The quantity of WebCam must be more than 0.
            {
                vsp = new AForge.Controls.VideoSourcePlayer();
                this.Controls.Add(vsp);

                VideoCaptureDevice Cam = new VideoCaptureDevice(USBWebcams[0].MonikerString);
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

                vsp.Size = new Size(ww, hh);
                vsp.Location = new Point(20, 20);
                this.ClientSize = new Size(vsp.Size.Width + 250, vsp.Size.Height + 40);

                sw = new Stopwatch();
                sw.Start();
            }
            else
            {
                this.Text = "無影像裝置";
            }
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            vsp.SignalToStop();
            vsp.WaitForStop();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
            var bitmap = vsp.GetCurrentVideoFrame();
            bitmap.Save(filename, System.Drawing.Imaging.ImageFormat.Jpeg);
            richTextBox1.Text += "已存檔 : " + filename + "\n";
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (sw == null)
            {
                sw = new Stopwatch();
                sw.Start();
            }
            else
            {
                sw.Stop();

                IVideoSource ivs = vsp.VideoSource;
                int framesReceived1 = 0;

                // get number of frames for the last second
                if (ivs != null)
                {
                    framesReceived1 = ivs.FramesReceived;   //讀過資料後 會歸零

                    float fps = 1000.0f * framesReceived1 / sw.ElapsedMilliseconds;

                    lb_fps.Text = fps.ToString("F2") + " fps";

                    sw.Reset();
                    sw.Start();
                }
            }
        }
    }
}
