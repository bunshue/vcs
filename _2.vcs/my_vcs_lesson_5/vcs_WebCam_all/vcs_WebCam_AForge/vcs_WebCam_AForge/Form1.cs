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

namespace vcs_WebCam_AForge
{
    public partial class Form1 : Form
    {

        //參考
        //【AForge.NET】C#上使用AForge.Net擷取視訊畫面
        //https://ccw1986.blogspot.com/2013/01/ccaforgenetcapture-image.html
        public FilterInfoCollection USBWebcams = null;
        public VideoCaptureDevice Cam = null;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice);
            if (USBWebcams.Count > 0)  // The quantity of WebCam must be more than 0.
            {
                button1.Enabled = true;
                Cam = new VideoCaptureDevice(USBWebcams[0].MonikerString);
                //Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);
                Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);
            }
            else
            {
                button1.Enabled = false;
                richTextBox1.Text += "無影像裝置\n";
            }

        }

        void Cam_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();
        }

        int camera_start = 0;
        private void button1_Click(object sender, EventArgs e)
        {
            if (camera_start == 0)
            {
                camera_start = 1;
                button1.Text = "Stop";
                Cam.Start();   // WebCam starts capturing images.
            }
            else
            {
                camera_start = 0;
                button1.Text = "Start";
                Cam.Stop();  // WebCam stops capturing images.
            }


        }

        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            if (Cam != null)
            {
                if (Cam.IsRunning)  // When Form1 closes itself, WebCam must stop, too.
                {
                    Cam.Stop();   // WebCam stops capturing images.
                }
            }

        }


    }
}
