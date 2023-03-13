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
        //private VideoCaptureDevice videoSource;
        //开始录像
        private bool stopREC = true;
        private bool createNewFile = true;
        string videoPath = "";
        private VideoFileWriter videoWriter;
        private VideoFileWriter videoWriter1;
        int frameRate = 20; //默认帧率

        List<String> videos = new List<string>();

        public Form1()
        {
            InitializeComponent();
            videoPath = Application.StartupPath+"\\videos\\";
            if (!Directory.Exists(videoPath))
            {
                Directory.CreateDirectory(videoPath);
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            
            try
            {
                // 枚举所有视频输入设备
                videoDevices = new FilterInfoCollection(FilterCategory.VideoInputDevice);

                if (videoDevices.Count == 0)
                    throw new ApplicationException();

                foreach (FilterInfo device in videoDevices)
                {
                    tscbxCameras.Items.Add(device.Name);
                    videos.Add(device.Name);
                }

                tscbxCameras.SelectedIndex = 0;

            }
            catch (ApplicationException)
            {
                tscbxCameras.Items.Add("No local capture devices");
                videoDevices = null;
            }
        }

        private void btnConnect_Click(object sender, EventArgs e)
        {
            CameraConn();
           
        }
        //连接摄像头
        private void CameraConn()
        {
            for (int i = 0; i < videos.Count; i++)
            {
                if (i == 0)
                {
                    VideoCaptureDevice videoSource = new VideoCaptureDevice(videoDevices[i].MonikerString);
                    //videoSource.DesiredFrameSize = new System.Drawing.Size(320, 240);
                    //videoSource.DesiredFrameRate = 1;

                    videoSourcePlayer.VideoSource = videoSource;
                    videoSourcePlayer.Start();
                }
                else if (i == 1)
                {
                    VideoCaptureDevice videoSource1 = new VideoCaptureDevice(videoDevices[i].MonikerString);
                    //videoSource1.DesiredFrameSize = new System.Drawing.Size(320, 240);
                    //videoSource1.DesiredFrameRate = 1;

                    videoSourcePlayer1.VideoSource = videoSource1;
                    videoSourcePlayer1.Start();
                }
            }
        }


        //关闭摄像头
        private void btnClose_Click(object sender, EventArgs e)
        {
            videoSourcePlayer.SignalToStop();
            videoSourcePlayer.WaitForStop();

            videoSourcePlayer1.SignalToStop();
            videoSourcePlayer1.WaitForStop();
        }

        //主窗体关闭
        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            btnClose_Click(null, null);
        }

        //拍照
        private void Photograph_Click(object sender, EventArgs e)
        {
            try
            {
                if (videoSourcePlayer.IsRunning)
                {
                    BitmapSource bitmapSource = System.Windows.Interop.Imaging.CreateBitmapSourceFromHBitmap(
                                    videoSourcePlayer.GetCurrentVideoFrame().GetHbitmap(),
                                    IntPtr.Zero,
                                     Int32Rect.Empty,
                                    BitmapSizeOptions.FromEmptyOptions());
                    PngBitmapEncoder pE = new PngBitmapEncoder();
                    pE.Frames.Add(BitmapFrame.Create(bitmapSource));
                    string picName = GetImagePath() + "\\" + "xiaosy" + ".jpg";
                    if (File.Exists(picName))
                    {
                        File.Delete(picName);
                    }
                    using (Stream stream = File.Create(picName))
                    {
                        pE.Save(stream);
                    }
                    //拍照完成后关摄像头并刷新同时关窗体
                    if (videoSourcePlayer != null && videoSourcePlayer.IsRunning)
                    {
                        videoSourcePlayer.SignalToStop();
                        videoSourcePlayer.WaitForStop();
                    }
                    
                    this.Close();
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("摄像头异常：" + ex.Message);
            }
        }

        private string GetImagePath()
        {
            string personImgPath = Path.GetDirectoryName(AppDomain.CurrentDomain.BaseDirectory)
                         + Path.DirectorySeparatorChar.ToString() + "PersonImg";
            if (!Directory.Exists(personImgPath))
            {
                Directory.CreateDirectory(personImgPath);
            }

            return personImgPath;
        }

        private void videoSourcePlayer_NewFrame(object sender, ref System.Drawing.Bitmap image)
        {
            //录像
            Graphics g = Graphics.FromImage(image);
            SolidBrush drawBrush = new SolidBrush(Color.Yellow);

            Font drawFont = new Font("Arial", 6, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);
            int xPos = image.Width - (image.Width - 15);
            int yPos = 10;
            //写到屏幕上的时间
           string  drawDate = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");

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
            if (videos.Count == 0)
            {
                MessageBox.Show("请连接设备!");
                return;
            }
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

        private void videoSourcePlayer1_NewFrame(object sender, ref Bitmap image)
        {
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
            string fileFullPath = videoPath + "V2" + DateTime.Now.ToString("yyyy-MM-dd-HH-mm-ss"); ;

            if (stopREC)
            {
                stopREC = true;
                createNewFile = true;  //这里要设置为true表示要创建新文件
                if (videoWriter1 != null)
                    videoWriter1.Close();
            }
            else
            {
                //开始录像
                if (createNewFile)
                {
                    createNewFile = false;
                    if (videoWriter1 != null)
                    {
                        videoWriter1.Close();
                        videoWriter1.Dispose();
                    }
                    videoWriter1 = new VideoFileWriter();
                    //这里必须是全路径，否则会默认保存到程序运行根据录下了
                    videoWriter1.Open(fileFullPath, image.Width, image.Height, frameRate, VideoCodec.MPEG4);
                    videoWriter1.WriteVideoFrame(image);
                }
                else
                {
                    videoWriter1.WriteVideoFrame(image);
                }
            }
        }
        
    }
}
