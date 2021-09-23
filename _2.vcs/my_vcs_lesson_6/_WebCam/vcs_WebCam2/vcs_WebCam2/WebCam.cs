using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Windows.Forms;
using System.Drawing;

using System.Threading;

using AForge.Video;
using AForge.Video.DirectShow;

namespace vcs_WebCam2
{
    class WebCam
    {
        PictureBox display;    // a refrence to the PictureBox on the MainForm
        private VideoCaptureDevice Cam = null; // refrence to the actual VidioCaptureDevice (webcam)
        public String cameraName; // string for display purposes

        public WebCam(PictureBox display, string monikerString, String cameraName)
        {
            this.cameraName = cameraName;
            this.display = display;
            this.display.Paint += new PaintEventHandler(DrawMessage);

            Cam = new VideoCaptureDevice(monikerString);
            Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame); // defines which method to call when a new frame arrives
            Cam.Start(); // starts the videoCapture
        }

        public void StopCapture()
        {
            if (this.Cam.IsRunning == true)
            {
                // we must stop the VideoCaptureDevice when done to free it so it can be used by other applications
                this.Cam.Stop();
            }
        }

        private void DrawMessage(object sender, PaintEventArgs e)
        {
            using (Font f = new Font("Arial", 14, FontStyle.Bold))
            {
                string str = DateTime.Now.ToString();
                SolidBrush sb = new SolidBrush(Color.Green);

                e.Graphics.DrawString(str, f, sb, new Point(10, 10));
            }
        }

        //自定義函數, 捕獲每一幀圖像並顯示
        void Cam_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            try
            {
                Bitmap bitmap1 = (Bitmap)eventArgs.Frame.Clone(); // get a copy of the BitMap from the VideoCaptureDevice
                if (this.isResolutionSet == false)
                {
                    // this is run once to set the resolution for the VideoRecorder
                    this.Width = bitmap1.Width;
                    this.Height = bitmap1.Height;
                    this.isResolutionSet = true;
                }

                this.display.Image = (Bitmap)bitmap1.Clone(); // displays the current frame on the main form

            }
            catch (InvalidOperationException ex)
            {
            }
        }

        // output video resolution info
        bool isResolutionSet = false;
        int Width = 0;
        int Height = 0;
    }
}

