using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using AForge.Video;             //需要添加這兩個.dll
using AForge.Video.DirectShow;

namespace vcs_WebCam0
{
    public partial class Form1 : Form
    {
        //參考
        //【AForge.NET】C#上使用AForge.Net擷取視訊畫面
        //https://ccw1986.blogspot.com/2013/01/ccaforgenetcapture-image.html

        //AForge下載鏈結
        //http://www.aforgenet.com/framework/downloads.html

        //參考/右鍵/加入參考/瀏覽AForge.Video.dll和AForge.Video.DirectShow.dll


        private FilterInfoCollection USBWebcams = null;

        private const int BORDER = 10;
        private const int W = 640;
        private const int H = 480;
        private const int W_richTextBox1 = W/2;
        private const int H_richTextBox1 = H - 50;

        //int webcam_count = 0;
        
        //public FilterInfoCollection USBWebcams = null;
        public VideoCaptureDevice Cam = null;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            Stop_Webcam();
        }

        void show_item_location()
        {
            pictureBox1.Size = new Size(W, H);
            pictureBox1.Location = new Point(BORDER, BORDER);

            richTextBox1.Location = new Point(BORDER+W+BORDER, BORDER + 50);
            richTextBox1.Size = new Size(W_richTextBox1, H_richTextBox1);

            int dx = 80;
            button1.Location = new Point(BORDER + W + BORDER + dx * 0, BORDER);
            button2.Location = new Point(BORDER + W + BORDER + dx * 1, BORDER);
            button3.Location = new Point(BORDER + W + BORDER + dx * 2, BORDER);
            lb_fps.Location = new Point(BORDER + W + BORDER + dx * 3, BORDER+BORDER/2);

            this.Text = "";
            this.ClientSize = new Size(BORDER + W + BORDER + W/2 + BORDER, BORDER + H + BORDER);
        }

        void Init_WebcamSetup()
        {
            //richTextBox1.Text += "重新抓取USB影像\t";
            USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice);
            if (USBWebcams.Count > 0)  // The quantity of WebCam must be more than 0.
            {
                //button12.Enabled = false;
                Cam = new VideoCaptureDevice(USBWebcams[0].MonikerString);  //實例化對象
                Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);
                //richTextBox1.Text += "有影像裝置\n";

                Cam.VideoResolution = Cam.VideoCapabilities[0];

                string webcam_name = string.Empty;

                /*
                int ww;
                int hh;
                ww = Cam.VideoCapabilities[0].FrameSize.Width;
                hh = Cam.VideoCapabilities[0].FrameSize.Height;

                webcam_name = USBWebcams[0].Name + " " + Cam.VideoCapabilities[0].FrameSize.Width.ToString() + " X " + Cam.VideoCapabilities[0].FrameSize.Height.ToString() + " @ " + Cam.VideoCapabilities[0].AverageFrameRate.ToString() + " Hz";
                this.Text = webcam_name;

                pictureBox1.Size = new Size(ww, hh);
                pictureBox1.Location = new Point(50, 50);
                this.ClientSize = new Size(pictureBox1.Location.X + pictureBox1.Width + 50, pictureBox1.Location.Y + pictureBox1.Height + 50);
                */
            }
            else
            {
                this.Text = "無影像裝置\n";
            }
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
                //show_main_message("停止", S_OK, 20);
                Cam.Stop();  // WebCam stops capturing images.
                Cam.SignalToStop();
                Cam.WaitForStop();
                while (Cam.IsRunning)
                {
                    Console.Write("等候相機關閉");
                }
                Cam = null;
            }
        }

        int frame_count = 0;        //計算fps用
        int frame_count_old = 0;    //計算fps用
        DateTime dt_old = DateTime.Now;

        public Bitmap bm = null;
        //自定義函數, 捕獲每一幀圖像並顯示
        void Cam_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            frame_count++;
            try
            {
                //pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();
                bm = (Bitmap)eventArgs.Frame.Clone();
                //pictureBox1.Image = bm;
            }
            catch (Exception ex)
            {
                //richTextBox1.Text += "xxx錯誤訊息n : " + ex.Message + "\n";
            }

            Graphics g = Graphics.FromImage(bm);

            int w;
            int h;
            try
            {
                w = bm.Width;
                h = bm.Height;
            }
            catch (Exception ex)
            {
                //richTextBox1.Text += "xxx錯誤訊息m : " + ex.Message + "\n";
                GC.Collect();       //回收資源
                return;
            }

            //顯示時間
            string drawDate = DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss");
            SolidBrush sb = new SolidBrush(Color.Yellow);
            Font f = new Font("Arial", 6, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);
            int x_st = 10;
            int y_st = 10;
            g.DrawString(drawDate, f, sb, x_st, y_st);

            try
            {
                pictureBox1.Image = bm;
            }
            catch (Exception ex)
            {
                //richTextBox1.Text += "xxx錯誤訊息a : " + ex.Message + "\n";
            }
            GC.Collect();       //回收資源
        }

        private void timer_clock_Tick(object sender, EventArgs e)
        {
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
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Init_WebcamSetup();
            Start_Webcam();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Stop_Webcam();
        }

        private void button3_Click(object sender, EventArgs e)
        {

        }
    }
}

