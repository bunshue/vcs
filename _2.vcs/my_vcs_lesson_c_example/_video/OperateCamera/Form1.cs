using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing.Imaging;
using System.Text;
using System.Windows;
using System.Windows.Forms;

using System.IO;
using System.Windows.Media.Imaging;

using AForge;
using AForge.Controls;
using AForge.Video;
using AForge.Video.DirectShow;
using AForge.Video.FFMPEG;

using Size = System.Drawing.Size;
using System.Drawing;

namespace OperateCamera
{
    public partial class Form1 : Form
    {
        public FilterInfoCollection USBWebcams = null;
        public VideoCaptureDevice Cam = null;

        //开始录像
        private bool stopREC = true;
        private bool createNewFile = true;
        private VideoFileWriter videoWriter;

        string fileFullPath = string.Empty;

        bool flag_recording = false;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //创建文件路径
            string fileFullPath = Application.StartupPath + "\\V1" + DateTime.Now.ToString("yyyy-MM-dd-HH-mm-ss");

            richTextBox1.Text += "開啟檔案 : " + fileFullPath + "\n";

            /*
            videoWriter = new VideoFileWriter();    //無法執行此行

            //这里必须是全路径，否则会默认保存到程序运行根据录下了
            videoWriter.Open(fileFullPath, 640, 480, 30, VideoCodec.MPEG4);
            */


        }

        private void btnConnect_Click(object sender, EventArgs e)
        {
            try
            {
                // 枚举所有视频输入设备
                USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice);

                if (USBWebcams.Count == 0)
                    throw new ApplicationException();

                foreach (FilterInfo device in USBWebcams)
                {
                    richTextBox1.Text += "取得WebCam : " + device.Name + "\n";
                }
            }
            catch (ApplicationException)
            {
                richTextBox1.Text += "無 WebCam\n";
                USBWebcams = null;
            }

            CameraConn();
        }

        //连接摄像头
        private void CameraConn()
        {
            Cam = new VideoCaptureDevice(USBWebcams[0].MonikerString);  //實例化對象

            Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);
            Cam.Start();   // WebCam starts capturing images.



            Cam.DesiredFrameSize = new System.Drawing.Size(320, 240);
            Cam.DesiredFrameRate = 1;

            videoSourcePlayer.VideoSource = Cam;
            videoSourcePlayer.Start();
        }

        //关闭摄像头
        private void btnClose_Click(object sender, EventArgs e)
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

            videoSourcePlayer.SignalToStop();
            videoSourcePlayer.WaitForStop();
        }

        //主窗体关闭
        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            btnClose_Click(null, null);
        }

        private void videoSourcePlayer_NewFrame(object sender, ref System.Drawing.Bitmap image)
        {
            richTextBox1.Text += "a";
            //录像
            Graphics g = Graphics.FromImage(image);
            SolidBrush drawBrush = new SolidBrush(Color.Yellow);

            Font drawFont = new Font("Arial", 6, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);
            int xPos = image.Width - (image.Width - 15);
            int yPos = 10;
            //写到屏幕上的时间
            string drawDate = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");

            g.DrawString(drawDate, drawFont, drawBrush, xPos, yPos);

            ////创建文件路径
            //string fileFullPath = videoPath + "V1" + DateTime.Now.ToString("yyyy-MM-dd-HH-mm-ss");

            if (stopREC)
            {
                stopREC = true;
                createNewFile = true;  //这里要设置为true表示要创建新文件
                if (videoWriter != null)
                    videoWriter.Close();
            }
            else
            {
                //开始录像
                if (createNewFile)
                {

                    createNewFile = false;
                    if (videoWriter != null)
                    {
                        videoWriter.Close();
                        videoWriter.Dispose();
                    }
                    richTextBox1.Text += "開啟檔案 : " + fileFullPath + "\n";

                    videoWriter = new VideoFileWriter();
                    //这里必须是全路径，否则会默认保存到程序运行根据录下了
                    videoWriter.Open(fileFullPath, image.Width, image.Height, 30, VideoCodec.MPEG4);
                    videoWriter.WriteVideoFrame(image);
                }
                else
                {
                    videoWriter.WriteVideoFrame(image);
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (flag_recording == false)
            {
                flag_recording = true;
                stopREC = false;
                createNewFile = true;
                button1.Text = "停止錄影";
            }
            else
            {
                flag_recording = false;
                stopREC = true;
                button1.Text = "開始錄影";


                flag_recording = false;
                if (videoWriter != null)
                {
                    videoWriter.Close();
                    videoWriter.Dispose();
                }


            }
        }

        public Bitmap bmp = null;
        //自定義函數, 捕獲每一幀圖像並顯示
        void Cam_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            //pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();
            bmp = (Bitmap)eventArgs.Frame.Clone();

            bmp = (Bitmap)eventArgs.Frame.Clone();

            //bmp.RotateFlip(RotateFlipType.RotateNoneFlipY);    //反轉
            Graphics g = Graphics.FromImage(bmp);
            SolidBrush drawBrush = new SolidBrush(Color.Yellow);

            Font drawFont = new Font("Arial", 6, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);
            int xPos = bmp.Width - (bmp.Width - 15);
            int yPos = 10;
            //写到屏幕上的时间
            string drawDate = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");

            g.DrawString(drawDate, drawFont, drawBrush, xPos, yPos);


            /*  準備中
            if (stopREC)
            {
                stopREC = true;
                createNewFile = true;  //这里要设置为true表示要创建新文件
                if (videoWriter != null)
                    videoWriter.Close();
            }
            else
            {
                //开始录像
                if (createNewFile)
                {

                    createNewFile = false;
                    if (videoWriter != null)
                    {
                        videoWriter.Close();
                        videoWriter.Dispose();
                    }
                    richTextBox1.Text += "開啟檔案 : " + fileFullPath + "\n";

                    videoWriter = new VideoFileWriter();
                    //这里必须是全路径，否则会默认保存到程序运行根据录下了
                    videoWriter.Open(fileFullPath, bmp.Width, bmp.Height, 30, VideoCodec.MPEG4);
                    videoWriter.WriteVideoFrame(bmp);
                }
                else
                {
                    videoWriter.WriteVideoFrame(bmp);
                }
            }
            */

            pictureBox1.Image = bmp;

            GC.Collect();       //回收資源





        }

        private void button2_Click(object sender, EventArgs e)
        {
            //string fileFullPath = videoPath + "V1" + DateTime.Now.ToString("yyyy-MM-dd-HH-mm-ss");

            /*
            if (videoWriter != null)
            {
                videoWriter.Close();
                videoWriter.Dispose();
            }
            */

            //videoWriter = new VideoFileWriter();

            //videoWriter.Open(fileFullPath, 640, 480, 30, VideoCodec.MPEG4);
            //videoWriter.WriteVideoFrame(image);

            //videoWriter.Close();
            //videoWriter.Dispose();
        }
    }
}
