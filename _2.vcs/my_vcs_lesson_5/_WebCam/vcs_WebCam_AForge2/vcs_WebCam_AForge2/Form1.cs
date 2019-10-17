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

namespace vcs_WebCam_AForge2
{
    public partial class Form1 : Form
    {
        //參考
        //【AForge.NET】C#上使用AForge.Net擷取視訊畫面
        //https://ccw1986.blogspot.com/2013/01/ccaforgenetcapture-image.html

        //AForge下載鏈結
        //http://www.aforgenet.com/framework/downloads.html

        public FilterInfoCollection USBWebcams = null;
        public VideoCaptureDevice Cam = null;

        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE

        int timer_display_show_main_mesg_count = 0;
        int timer_display_show_main_mesg_count_target = 0;

        bool flag_show_time = true;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            lb_main_mesg.Text = "";
            this.pictureBox1.KeyDown += new KeyEventHandler(pictureBox1_KeyDown);
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            this.pictureBox1.Focus();

            //richTextBox1.Text += "重新抓取USB影像\t";
            USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice);
            if (USBWebcams.Count > 0)  // The quantity of WebCam must be more than 0.
            {
                //button12.Enabled = false;
                Cam = new VideoCaptureDevice(USBWebcams[0].MonikerString);  //實例化對象
                Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);
                Cam.Start();   // WebCam starts capturing images.
                //richTextBox1.Text += "有影像裝置\n";

                //lb_main_mesg.Text += 

                Cam.VideoResolution = Cam.VideoCapabilities[0];

                string webcam_name = string.Empty;

                int ww;
                int hh;
                ww = Cam.VideoCapabilities[0].FrameSize.Width;
                hh = Cam.VideoCapabilities[0].FrameSize.Height;

                webcam_name = USBWebcams[0].Name + " " + Cam.VideoCapabilities[0].FrameSize.Width.ToString() + " X " + Cam.VideoCapabilities[0].FrameSize.Height.ToString() + " @ " + Cam.VideoCapabilities[0].AverageFrameRate.ToString() + " Hz";
                //lb_main_mesg.Text = webcam_name;
                show_main_message(webcam_name, S_OK, 30);

                if (Screen.PrimaryScreen.Bounds.Width == 1920)
                {
                    if (ww >= Screen.PrimaryScreen.Bounds.Width)
                    {
                        pictureBox1.Size = new Size(1920, 1080);
                        pictureBox1.Location = new Point(0, 0);
                        this.FormBorderStyle = FormBorderStyle.None;
                        this.WindowState = FormWindowState.Maximized;
                        //this.Size = new Size(pictureBox1.Size.Width + 200, pictureBox1.Size.Height + 200);


                    }
                    else if (ww < Screen.PrimaryScreen.Bounds.Width)
                    {
                        pictureBox1.Size = new Size(ww, hh);
                        pictureBox1.Location = new Point(100, 100);
                        this.FormBorderStyle = FormBorderStyle.FixedSingle;
                        this.WindowState = FormWindowState.Normal;
                        this.Size = new Size(pictureBox1.Size.Width + 200, pictureBox1.Size.Height + 200);

                    }



                }

            }
            else
            {
                //button12.Enabled = true;
                //richTextBox1.Text += "無影像裝置\n";
            }

        }

        public Bitmap bm = null;
        //自定義函數, 捕獲每一幀圖像並顯示
        void Cam_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            //pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();
            bm = (Bitmap)eventArgs.Frame.Clone();
            bm.RotateFlip(RotateFlipType.RotateNoneFlipY);
            pictureBox1.Image = bm;

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

        void pictureBox1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.X)
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


                System.Environment.Exit(0);
            }
            else if (e.KeyCode == Keys.S)
            {
                this.pictureBox1.Focus();
                show_main_message("存檔中...", S_OK, 10);
                //delay(10);

                Bitmap bitmap1 = (Bitmap)pictureBox1.Image;

                if (bitmap1 != null)
                {
                    IntPtr pHdc;
                    Graphics g = Graphics.FromImage(bitmap1);
                    Pen p = new Pen(Color.Red, 1);
                    SolidBrush drawBrush = new SolidBrush(Color.Yellow);
                    Font drawFont = new Font("Arial", 6, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);
                    pHdc = g.GetHdc();

                    if (flag_show_time == true)
                    {   //顯示時間
                        int xPos = 10;
                        int yPos = 10;
                        string drawDate = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");

                        g.ReleaseHdc();
                        g.DrawString(drawDate, drawFont, drawBrush, xPos, yPos);
                    }
                    else
                    {
                        g.ReleaseHdc();
                    }
                    g.Dispose();

                    String filename = string.Empty;
                    filename = Application.StartupPath + "\\ims_image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");

                    //String file1 = file + ".jpg";
                    String filename2 = filename + ".bmp";
                    //String file3 = file + ".png";

                    //bitmap1.Save(@file1, ImageFormat.Jpeg);
                    bitmap1.Save(filename2, ImageFormat.Bmp);
                    //bitmap1.Save(@file3, ImageFormat.Png);

                    //richTextBox1.Text += "存檔成功\n";
                    //richTextBox1.Text += "已存檔 : " + file1 + "\n";
                    //richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                    //richTextBox1.Text += "已存檔 : " + file3 + "\n";
                    //show_main_message("已存檔BMP", S_OK, 30);
                }
                else
                {
                    //richTextBox1.Text += "無圖可存\n";
                    //show_main_message("無圖可存", S_FALSE, 30);
                }




            }
        }

        void show_main_message(string mesg, int number, int timeout)
        {
            lb_main_mesg.Text = mesg;
            //playSound(number);

            timer_display_show_main_mesg_count = 0;
            timer_display_show_main_mesg_count_target = timeout;   //timeout in 0.1 sec
            timer_display.Enabled = true;
        }

        private void timer_display_Tick(object sender, EventArgs e)
        {
            if (timer_display_show_main_mesg_count < timer_display_show_main_mesg_count_target)      //display main message timeout
            {
                timer_display_show_main_mesg_count++;
                if (timer_display_show_main_mesg_count >= timer_display_show_main_mesg_count_target)
                    lb_main_mesg.Text = "";
            }

        }



    }
}
