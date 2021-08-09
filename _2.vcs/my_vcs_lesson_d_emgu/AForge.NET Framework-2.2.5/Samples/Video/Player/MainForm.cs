using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;

using AForge.Video;
using AForge.Video.DirectShow;

namespace Player
{
    public partial class MainForm : Form
    {
        private Stopwatch stopwatch = null;

        // Class constructor
        public MainForm()
        {
            InitializeComponent();
        }

        private void MainForm_Load(object sender, EventArgs e)
        {

        }

        private void MainForm_FormClosing(object sender, FormClosingEventArgs e)
        {
            CloseCurrentVideoSource();
        }

        // Open video source
        private void OpenVideoSource(IVideoSource source)
        {
            // stop current video source
            CloseCurrentVideoSource();

            // start new video source
            vsp.VideoSource = source;
            vsp.Start();

            // reset stop watch
            stopwatch = null;

            // start timer
            timer.Start();

            if (source.IsRunning == true)
            {
                richTextBox1.Text += source.IsRunning.ToString() + "\n";
                richTextBox1.Text += source.Source.Length.ToString() + "\n";
                richTextBox1.Text += vsp.Size.ToString() + "\n";
                richTextBox1.Text += vsp.Width.ToString() + "\n";
                richTextBox1.Text += vsp.Height.ToString() + "\n";
            }
        }

        // Close video source if it is running
        private void CloseCurrentVideoSource()
        {
            if (vsp.VideoSource != null)
            {
                vsp.SignalToStop();

                // wait ~ 3 seconds
                for (int i = 0; i < 30; i++)
                {
                    if (!vsp.IsRunning)
                        break;
                    System.Threading.Thread.Sleep(100);
                }

                if (vsp.IsRunning)
                {
                    vsp.Stop();
                }

                vsp.VideoSource = null;
            }
        }

        // New frame received by the player
        private void vsp_NewFrame(object sender, ref Bitmap image)
        {
            //畫上目前的時間
            DateTime now = DateTime.Now;
            Graphics g = Graphics.FromImage(image);

            SolidBrush brush = new SolidBrush(Color.Red);
            g.DrawString(now.ToString(), this.Font, brush, new PointF(5, 5));
            brush.Dispose();

            g.Dispose();
        }

        // On timer event - gather statistics
        private void timer_Tick(object sender, EventArgs e)
        {
            IVideoSource videoSource = vsp.VideoSource;

            if (videoSource != null)
            {
                // get number of frames since the last timer tick
                int framesReceived = videoSource.FramesReceived;

                if (stopwatch == null)
                {
                    stopwatch = new Stopwatch();
                    stopwatch.Start();
                }
                else
                {
                    stopwatch.Stop();

                    float fps = 1000.0f * framesReceived / stopwatch.ElapsedMilliseconds;
                    fpsLabel.Text = fps.ToString("F2") + " fps";

                    stopwatch.Reset();
                    stopwatch.Start();
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //Local Video Capture Device
            VideoCaptureDeviceForm form = new VideoCaptureDeviceForm();

            if (form.ShowDialog(this) == DialogResult.OK)
            {
                // create video source
                VideoCaptureDevice videoSource = form.VideoDevice;

                // open it
                OpenVideoSource(videoSource);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //Open video file (using DirectShow)
            string filename = @"C:\______test_files\__RWa\_avi\enka.avi";
            {
                // create video source
                FileVideoSource fileSource = new FileVideoSource(filename);

                // open it
                OpenVideoSource(fileSource);
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //會不會是 無線網路監控IP Cam?

            //Open JPEG URL
            URLForm form = new URLForm();

            form.Description = "Enter URL of an updating JPEG from a web camera:";
            form.URLs = new string[]
				{
					"http://195.243.185.195/axis-cgi/jpg/image.cgi?camera=1",
				};

            if (form.ShowDialog(this) == DialogResult.OK)
            {
                // create video source
                JPEGStream jpegSource = new JPEGStream(form.URL);

                // open it
                OpenVideoSource(jpegSource);
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //會不會是 無線網路監控IP Cam?

            //Open MJPEG URL
            URLForm form = new URLForm();

            form.Description = "Enter URL of an MJPEG video stream:";
            form.URLs = new string[]
				{
					"http://195.243.185.195/axis-cgi/mjpg/video.cgi?camera=4",
					"http://195.243.185.195/axis-cgi/mjpg/video.cgi?camera=3",
				};

            if (form.ShowDialog(this) == DialogResult.OK)
            {
                // create video source
                MJPEGStream mjpegSource = new MJPEGStream(form.URL);

                // open it
                OpenVideoSource(mjpegSource);
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //Capture 1st display in the system
            OpenVideoSource(new ScreenCaptureStream(Screen.AllScreens[0].Bounds, 100));
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            this.Close();
        }



    }
}
