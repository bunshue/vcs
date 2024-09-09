using System;
using System.IO;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using WebCam_Capture;
using System.Collections.Generic;

namespace vcs_WebCam_Capture
{
    //Design by Pongsakorn Poosankam
    class WebCam
    {
        private WebCamCapture webcam;
        private PictureBox pictureBox1;
        private int FrameNumber = 30;
        public void InitializeWebCam(ref PictureBox pbx, ref RichTextBox rtb)
        {
            webcam = new WebCamCapture();

            rtb.Text += "Name : " + webcam.Name.ToString() + "\n";
            rtb.Text += "ProductName : " + webcam.ProductName.ToString() + "\n";
            rtb.Text += "CompanyName : " + webcam.CompanyName.ToString() + "\n";

            rtb.Text += "CaptureWidth : " + webcam.CaptureWidth.ToString() + "\n";
            rtb.Text += "CaptureHeight : " + webcam.CaptureHeight.ToString() + "\n";
            rtb.Text += "Size : " + webcam.Size.ToString() + "\n";
            rtb.Text += "Width : " + webcam.Width.ToString() + "\n";
            rtb.Text += "Height : " + webcam.Height.ToString() + "\n";

            webcam.FrameNumber = ((ulong)(0ul));
            webcam.TimeToCapture_milliseconds = FrameNumber;
            webcam.ImageCaptured += new WebCamCapture.WebCamEventHandler(webcam_ImageCaptured);
            pictureBox1 = pbx;
        }

        void webcam_ImageCaptured(object source, WebcamEventArgs e)
        {
            pictureBox1.Image = e.WebCamImage;
        }

        public void Start()
        {
            Console.WriteLine("webcam start");
            webcam.TimeToCapture_milliseconds = FrameNumber;
            webcam.Start(0);
        }

        public void Stop()
        {
            webcam.Stop();
        }

        public void Continue()
        {
            // change the capture time frame
            webcam.TimeToCapture_milliseconds = FrameNumber;

            // resume the video capture from the stop
            webcam.Start(this.webcam.FrameNumber);
        }

        public void ResolutionSetting()
        {
            Console.WriteLine("webcam config");
            webcam.Config();
        }

        public void AdvanceSetting()
        {
            webcam.Config2();
        }

        public void Info()
        {
            Console.WriteLine("webcam ifno");
            //webcam.Info();

            Console.WriteLine("webcam W " + webcam.CaptureWidth.ToString());
            Console.WriteLine("webcam H " + webcam.CaptureHeight.ToString());
            Console.WriteLine("webcam N " + webcam.FrameNumber.ToString());
            Console.WriteLine("webcam T " + webcam.TimeToCapture_milliseconds.ToString());
        }

    }
}


/*
        public int CaptureHeight { get; set; }
        public int CaptureWidth { get; set; }
        public ulong FrameNumber { get; set; }
        public int TimeToCapture_milliseconds { get; set; }
*/
