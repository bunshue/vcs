using System;
using System.IO;
using System.Linq;
using System.Text;
using WebCam_Capture;
using System.Collections.Generic;

namespace vcs_WebCam_Capture
{
    //Design by Pongsakorn Poosankam
    class WebCam
    {
        private WebCamCapture webcam;
        private System.Windows.Forms.PictureBox _FrameImage;
        private int FrameNumber = 30;
        public void InitializeWebCam(ref System.Windows.Forms.PictureBox ImageControl, ref System.Windows.Forms.RichTextBox rtb)
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
            _FrameImage = ImageControl;
        }

        void webcam_ImageCaptured(object source, WebcamEventArgs e)
        {
            _FrameImage.Image = e.WebCamImage;
        }

        public void Start()
        {
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
            webcam.Config();
        }

        public void AdvanceSetting()
        {
            webcam.Config2();
        }
    }
}
