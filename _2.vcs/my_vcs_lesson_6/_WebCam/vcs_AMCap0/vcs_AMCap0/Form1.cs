using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat

using AForge.Video;             //需要添加這兩個.dll
using AForge.Video.DirectShow;

namespace vcs_AMCap0
{
    public partial class Form1 : Form
    {
        //參考
        //【AForge.NET】C#上使用AForge.Net擷取視訊畫面
        //https://ccw1986.blogspot.com/2013/01/ccaforgenetcapture-image.html

        //AForge下載鏈結
        //http://www.aforgenet.com/framework/downloads.html

        //參考/右鍵/加入參考/瀏覽AForge.Video.dll和AForge.Video.DirectShow.dll

        public FilterInfoCollection USBWebcams = null;
        public VideoCaptureDevice Cam = null;

        private const int BORDER = 10;
        private const int W_pictureBox1 = 640;
        private const int H_pictureBox1 = 480;
        private const int W_groupBox1 = W_pictureBox1;
        private const int H_groupBox1 = 60;
        private const int W_richTextBox1 = 360;
        private const int H_richTextBox1 = H_pictureBox1 + H_groupBox1 + BORDER;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
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

        void Init_WebcamSetup()
        {
            //richTextBox1.Text += "重新抓取USB影像\t";
            USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice);
            if (USBWebcams.Count > 0)  // The quantity of WebCam must be more than 0.
            {
                Cam = new VideoCaptureDevice(USBWebcams[0].MonikerString);  //實例化對象
                Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);
                //richTextBox1.Text += "有影像裝置\n";

                Cam.VideoResolution = Cam.VideoCapabilities[0];

                string webcam_name = string.Empty;

                int ww;
                int hh;
                ww = Cam.VideoCapabilities[0].FrameSize.Width;
                hh = Cam.VideoCapabilities[0].FrameSize.Height;

                webcam_name = USBWebcams[0].Name + " " + Cam.VideoCapabilities[0].FrameSize.Width.ToString() + " X " + Cam.VideoCapabilities[0].FrameSize.Height.ToString() + " @ " + Cam.VideoCapabilities[0].AverageFrameRate.ToString() + " Hz";
                this.Text = webcam_name;
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
            pictureBox1.Image = null;
        }

        public Bitmap bm = null;
        //自定義函數, 捕獲每一幀圖像並顯示
        void Cam_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            try
            {
                //pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();
                bm = (Bitmap)eventArgs.Frame.Clone();

                pictureBox1.Image = bm;
            }
            catch (Exception ex)
            {
                this.Text += "xxx錯誤訊息n : " + ex.Message + "\n";
            }
            GC.Collect();       //回收資源
        }

        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            if (Cam != null)
            {
                if (Cam.IsRunning)  // When Form1 closes itself, WebCam must stop, too.
                {
                    Cam.Stop();   // WebCam stops capturing images.
                    Cam.SignalToStop();
                    Cam.WaitForStop();
                }
            }
        }

        void save_image_file()
        {
            this.pictureBox1.Focus();

            Bitmap bitmap1 = (Bitmap)pictureBox1.Image;

            if (bitmap1 != null)
            {
                IntPtr pHdc;
                Graphics g = Graphics.FromImage(bitmap1);
                Pen p = new Pen(Color.Red, 1);
                SolidBrush drawBrush = new SolidBrush(Color.Yellow);
                Font drawFont = new Font("Arial", 6, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);
                pHdc = g.GetHdc();

                g.ReleaseHdc();
                g.Dispose();

                String filename = string.Empty;
                filename = Application.StartupPath + "\\ims_image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");

                String filename2 = filename + ".bmp";

                try
                {
                    bitmap1.Save(filename2, ImageFormat.Bmp);
                    //richTextBox1.Text += "存檔成功\n";
                    //richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                }
                catch (Exception ex)
                {
                    this.Text += "xxx錯誤訊息b : " + ex.Message + "\n";
                }
            }
            else
            {
                //richTextBox1.Text += "無圖可存\n";
            }
            return;
        }

        private void button0_Click(object sender, EventArgs e)
        {
            Init_WebcamSetup();
            Start_Webcam();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Stop_Webcam();
        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {
            save_image_file();
        }
    }
}
