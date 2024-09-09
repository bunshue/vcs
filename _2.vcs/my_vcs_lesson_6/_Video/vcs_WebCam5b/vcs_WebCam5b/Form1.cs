using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;

using AForge.Video;
using AForge.Video.DirectShow;

namespace vcs_WebCam5b
{
    public partial class Form1 : Form
    {
        WebCam webcam;

        private FilterInfoCollection USBWebcams = null;

        private const int BORDER = 10;
        private const int W_pictureBox1 = 640;
        private const int H_pictureBox1 = 480;
        private const int W_groupBox1 = W_pictureBox1;
        private const int H_groupBox1 = 60;
        private const int W_richTextBox1 = 360;
        private const int H_richTextBox1 = H_pictureBox1 + H_groupBox1 + BORDER;

        int webcam_count = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            //離開程式前, 關閉相機
            try
            {
                this.webcam.StopCapture();
            }
            catch (Exception ex)
            {
            }
        }

        void show_item_location()
        {
            pictureBox1.Size = new Size(W_pictureBox1, H_pictureBox1);
            pictureBox1.Location = new Point(BORDER, BORDER);

            richTextBox1.Location = new Point(BORDER + W_pictureBox1 + BORDER, BORDER);
            richTextBox1.Size = new Size(W_richTextBox1, H_richTextBox1);

            int dx = 80;
            int offset_y = 3;
            button0.Location = new Point(BORDER + dx * 0, BORDER + offset_y);
            button1.Location = new Point(BORDER + dx * 1, BORDER + offset_y);
            button2.Location = new Point(BORDER + dx * 2, BORDER + offset_y);
            button3.Location = new Point(BORDER + dx * 3, BORDER + offset_y);
            lb_fps.Location = new Point(BORDER + dx * 4, BORDER + BORDER);

            groupBox1.Size = new Size(W_groupBox1, H_groupBox1);
            groupBox1.Location = new Point(BORDER + dx * 0, BORDER + H_pictureBox1 + BORDER);

            this.Text = "";
            this.ClientSize = new Size(BORDER + W_pictureBox1 + BORDER + W_richTextBox1 + BORDER, BORDER + H_pictureBox1 + BORDER + H_groupBox1 + BORDER);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //ST

            USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice); //實例化對象

            webcam_count = USBWebcams.Count;

            int i;
            /*
            richTextBox1.Text += "找到 " + webcam_count.ToString() + " 台WebCam\n";

            richTextBox1.Text += "USBWebcams.Capacity : " + USBWebcams.Capacity.ToString() + "\n";
            richTextBox1.Text += "USBWebcams.Count : " + USBWebcams.Count.ToString() + "\n";

            for (i = 0; i < webcam_count; i++)
            {
                richTextBox1.Text += "第 " + (i + 1).ToString() + " 台WebCam:\n";
                richTextBox1.Text += "短名 : " + USBWebcams[i].Name + "\n";
                richTextBox1.Text += "長名 : " + USBWebcams[i].MonikerString + "\n";
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";
            */

            if (webcam_count > 0)
            {
                i = 0;
                string camera_name = USBWebcams[i].MonikerString;   //長名
                this.webcam = new WebCam(pictureBox1, camera_name, "第 " + (i + 1).ToString() + " 台攝影機");
                this.Text = USBWebcams[i].Name;

                /*
                richTextBox1.Text += "第 " + (i + 1).ToString() + " 台WebCam:\n";
                richTextBox1.Text += "短名 : " + USBWebcams[i].Name + "\n";
                richTextBox1.Text += "長名 : " + USBWebcams[i].MonikerString + "\n";
                */
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //SP
            try
            {
                this.webcam.StopCapture();
                this.Text = "";
            }
            catch (Exception ex)
            {
            }
            pictureBox1.Image = null;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (this.webcam != null)
            {
                richTextBox1.Text += "找到 " + webcam_count.ToString() + " 台WebCam\n";
                int i = 0;
                richTextBox1.Text += "第 " + (i + 1).ToString() + " 台WebCam:\n";
                richTextBox1.Text += "cameraName\t" + this.webcam.cameraName.ToString() + "\n";
                richTextBox1.Text += "CamMonitor\t" + this.webcam.ToString() + "\n";
            }
            else
            {
                richTextBox1.Text += "尚未開啟WebCam\n";
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void timer_clock_Tick(object sender, EventArgs e)
        {
            /*
            if (Cam != null)
            {
                if (Cam.IsRunning == true)
                {
                    DateTime dt = DateTime.Now;
                    lb_fps.Text = (((frame_count - frame_count_old) * 1000) / ((TimeSpan)(dt - dt_old)).TotalMilliseconds).ToString("F2") + " fps";
                    dt_old = dt;
                    frame_count_old = frame_count;
                }
                else
                {
                    lb_fps.Text = "";
                }
            }
            */
        }

    }

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
