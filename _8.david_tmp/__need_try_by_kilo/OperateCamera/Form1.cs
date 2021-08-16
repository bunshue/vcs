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
        private FilterInfoCollection videoDevices;
        private VideoCaptureDevice videoSource;

        //开始录像
        private bool stopREC = true;
        private bool createNewFile = true;
        string videoPath = "";
        private VideoFileWriter videoWriter;
        int frameRate = 20; //默认帧率

        public Form1()
        {
            InitializeComponent();
            videoPath = Application.StartupPath + "\\videos\\";
            if (!Directory.Exists(videoPath))
            {
                Directory.CreateDirectory(videoPath);
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
        }

        private void btnConnect_Click(object sender, EventArgs e)
        {
            try
            {
                // 枚举所有视频输入设备
                videoDevices = new FilterInfoCollection(FilterCategory.VideoInputDevice);

                if (videoDevices.Count == 0)
                    throw new ApplicationException();

                foreach (FilterInfo device in videoDevices)
                {
                    richTextBox1.Text += "取得WebCam : " + device.Name + "\n";
                }
            }
            catch (ApplicationException)
            {
                richTextBox1.Text += "無 WebCam\n";
                videoDevices = null;
            }

            CameraConn();
        }

        //连接摄像头
        private void CameraConn()
        {
            VideoCaptureDevice videoSource = new VideoCaptureDevice(videoDevices[0].MonikerString);
            videoSource.DesiredFrameSize = new System.Drawing.Size(320, 240);
            videoSource.DesiredFrameRate = 1;

            videoSourcePlayer.VideoSource = videoSource;
            videoSourcePlayer.Start();
        }

        //关闭摄像头
        private void btnClose_Click(object sender, EventArgs e)
        {
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
            string fileFullPath = videoPath + "V1" + DateTime.Now.ToString("yyyy-MM-dd-HH-mm-ss"); ;

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
                    videoWriter = new VideoFileWriter();
                    //这里必须是全路径，否则会默认保存到程序运行根据录下了
                    videoWriter.Open(fileFullPath, image.Width, image.Height, frameRate, VideoCodec.MPEG4);
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
            //开始录像
            if (button1.Text == "开始录像")
            {
                stopREC = false;
                createNewFile = true;
                // frameRate = Convert.ToInt32(txtFrameRate.Text.Trim());
                button1.Text = "停止录像";
            }
            else if (button1.Text == "停止录像")
            {
                stopREC = true;
                button1.Text = "开始录像";
            }
        }
    }
}

