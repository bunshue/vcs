using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;
using System.Drawing.Imaging;   //for ImageFormat

using AForge.Video;
using AForge.Video.DirectShow;

/*
增加 VideoSourcePlayer 工具

工具箱/右鍵/選擇項目/瀏覽/選 AForge.Controls.dll
*/

namespace vcs_AForge_WebCam
{
    public partial class Form1 : Form
    {
        private Stopwatch stopwatch = null;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
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
            timer1.Start();
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
        private void timer1_Tick(object sender, EventArgs e)
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
                    this.Text = fps.ToString("F2") + " fps";

                    stopwatch.Reset();
                    stopwatch.Start();
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //開啟WebCam

            VideoCaptureDeviceForm form = new VideoCaptureDeviceForm();

            if (form.ShowDialog(this) == DialogResult.OK)
            {
                // create video source
                VideoCaptureDevice Cam = form.VideoDevice;

                //message ST
                richTextBox1.Text += "VideoCapabilities.Length = " + Cam.VideoCapabilities.Length.ToString() + "\n";
                richTextBox1.Text += "FrameRate = " + Cam.VideoResolution.FrameRate.ToString() + "\n";

                richTextBox1.Text += "VideoDeviceMoniker = " + form.VideoDeviceMoniker + "\n";

                Size cs = form.CaptureSize;
                richTextBox1.Text += "CaptureSize W = " + cs.Width.ToString() + ", H = " + cs.Height.ToString() + "\n";

                bool con1 = form.ConfigureSnapshots;
                richTextBox1.Text += "ConfigureSnapshots = " + con1.ToString() + "\n";
                if (con1 == true)
                {
                    Size ss = form.SnapshotSize;

                    richTextBox1.Text += "SnapshotSize W = " + ss.Width.ToString() + ", H = " + ss.Height.ToString() + "\n";
                }

                VideoInput vi = form.VideoInput;
                richTextBox1.Text += "Index " + vi.Index.ToString() + "\n";
                richTextBox1.Text += "Type " + vi.Type.ToString() + "\n";
                //message SP

                // open it
                OpenVideoSource(Cam);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //關閉WebCam

            CloseCurrentVideoSource();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //截圖
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
