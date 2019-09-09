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

namespace vcs_WebCam_AForge
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

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            try
            {
                ///---实例化对象
                USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice);
                richTextBox1.Text += "WebCam數目 : " + USBWebcams.Count.ToString() + "\n";

                ///---摄像头数量大于0
                if (USBWebcams.Count > 0)  // The quantity of WebCam must be more than 0.
                {
                    richTextBox1.Text += "WebCam Name : " + USBWebcams[0].Name + "\n";
                    richTextBox1.Text += "WebCam MonikerString Length : " + USBWebcams[0].MonikerString.Length.ToString() + "\n";

                    button1.Enabled = true;
                    ///---实例化对象
                    Cam = new VideoCaptureDevice(USBWebcams[0].MonikerString);
                    ///---绑定事件
                    Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);

                    richTextBox1.Text += "Length " + Cam.Source.Length.ToString() + "\n";
                    richTextBox1.Text += "Length " + Cam.VideoCapabilities.Length.ToString() + "\n";
                }
                else
                {
                    ///--没有摄像头
                    button1.Enabled = false;
                    richTextBox1.Text += "無影像裝置\n";
                }
               
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }


        }

        public Bitmap bm = null;

        ///------自定义函数
        private void Cam_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            //原本的寫法 會有問題
            pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();

            /*
            //在摄像头捕获到每一帧图像后，做好系统资源回收。
            bm = (Bitmap)eventArgs.Frame.Clone();
            pictureBox1.Image = bm;
            ///-----!!!!!!!!!!!!!! 注意，解决我的内存问题的代码就是下面的这一行
            ///---回收资源
            GC.Collect();
            ///---throw new NotImplementedException();
            */
        }

        int camera_start = 0;
        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                if (camera_start == 0)
                {
                    camera_start = 1;
                    button1.Text = "Stop";
                    //Cam.VideoResolution = Cam.VideoCapabilities[0];   //若有多個capabilities 或許可以換
                    Cam.Start();   // WebCam starts capturing images.
                }
                else
                {
                    camera_start = 0;
                    button1.Text = "Start";
                    Cam.Stop();  // WebCam stops capturing images.
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        ///---窗口关闭事件
        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            try
            {
                if (Cam != null)
                {
                    ///---关闭摄像头
                    if (Cam.IsRunning)  // When Form1 closes itself, WebCam must stop, too.
                    {
                        Cam.Stop();   // WebCam stops capturing images.
                    }
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }


        }



    }
}
