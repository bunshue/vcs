using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Diagnostics;

using System.Drawing.Imaging;   //for ImageFormat

using AForge.Video;
using AForge.Video.DirectShow;

namespace AForge_WebCam
{
    public partial class MainForm : Form
    {
        private Stopwatch stopWatch = null;

        // Class constructor
        public MainForm()
        {
            InitializeComponent();
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
            stopWatch = null;

            // start timer
            timer.Start();
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
            Graphics g = Graphics.FromImage(image);
            SolidBrush drawBrush = new SolidBrush(Color.Yellow);
            Font drawFont1 = new Font("Arial", 6, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);
            int x_st = 10;
            int y_st = 10;

            //在畫面的上方顯示時間
            string drawDate = DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss");
            g.DrawString(drawDate, drawFont1, drawBrush, x_st, y_st);
            drawBrush.Dispose();
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

                if (stopWatch == null)
                {
                    stopWatch = new Stopwatch();
                    stopWatch.Start();
                }
                else
                {
                    stopWatch.Stop();

                    float fps = 1000.0f * framesReceived / stopWatch.ElapsedMilliseconds;
                    this.Text = fps.ToString("F2") + " fps";

                    stopWatch.Reset();
                    stopWatch.Start();
                }
            }
        }

        // Open local video capture device
        private void button1_Click(object sender, EventArgs e)
        {
            VideoCaptureDeviceForm form = new VideoCaptureDeviceForm();

            if (form.ShowDialog(this) == DialogResult.OK)
            {
                // create video source
                VideoCaptureDevice Cam = form.VideoDevice;

                richTextBox1.Text += "VideoCapabilities.Length = " + Cam.VideoCapabilities.Length.ToString() + "\n";
                richTextBox1.Text += "FrameRate = " + Cam.VideoResolution.FrameRate.ToString() + "\n";

                // open it
                OpenVideoSource(Cam);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            CloseCurrentVideoSource();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (vsp.VideoSource == null)
            {
                richTextBox1.Text += "無圖可存\n";
                return;
            }

            try
            {
                Bitmap bitmap1 = vsp.GetCurrentVideoFrame();
                string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
                try
                {
                    //bitmap1.Save(@file1, ImageFormat.Jpeg);
                    bitmap1.Save(filename, ImageFormat.Bmp);
                    //bitmap1.Save(@file3, ImageFormat.Png);

                    //richTextBox1.Text += "已存檔 : " + file1 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename + "\n";
                    //richTextBox1.Text += "已存檔 : " + file3 + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }



            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息e01 : " + ex.Message + "\n";
            }

            
            
        }
    }
}
