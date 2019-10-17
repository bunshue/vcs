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

namespace vcs_WebCam_AForge1
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
        RotateFlipType rotate_flip_type = RotateFlipType.RotateNoneFlipNone;
        bool flag_show_time = true;

        public Form1()
        {
            InitializeComponent();
            comboBox1.SelectedIndex = 0;
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

        //自定義函數, 捕獲每一幀圖像並顯示
        private void Cam_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            //pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();
            bm = (Bitmap)eventArgs.Frame.Clone();
            //bm.RotateFlip(RotateFlipType.RotateNoneFlipY);
            bm.RotateFlip(rotate_flip_type);
            pictureBox1.Image = bm;

            GC.Collect();       //回收資源
        }

        int camera_start = 0;
        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                if (camera_start == 0)
                {
                    camera_start = 1;
                    button1.Text = "關閉Webcam";
                    //Cam.VideoResolution = Cam.VideoCapabilities[0];   //若有多個capabilities 或許可以換
                    Cam.Start();   // WebCam starts capturing images.
                }
                else
                {
                    camera_start = 0;
                    button1.Text = "開啟Webcam";
                    Cam.Stop();  // WebCam stops capturing images.
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        //窗口關閉事件
        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            try
            {
                if (Cam != null)
                {
                    //關閉WebCam
                    if (Cam.IsRunning)  // When Form1 closes itself, WebCam must stop, too.
                    {
                        Cam.Stop();   // WebCam stops capturing images.
                        Cam.SignalToStop();
                        Cam.WaitForStop();
                    }
                }
                System.Environment.Exit(0);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }


        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            richTextBox1.Text += "選了" + comboBox1.SelectedIndex.ToString() + "\n";
            switch (comboBox1.SelectedIndex)
            {
                case 0: rotate_flip_type = RotateFlipType.RotateNoneFlipNone; break;
                case 1: rotate_flip_type = RotateFlipType.RotateNoneFlipX; break;
                case 2: rotate_flip_type = RotateFlipType.RotateNoneFlipY; break;
                case 3: rotate_flip_type = RotateFlipType.RotateNoneFlipXY; break;
                case 4: rotate_flip_type = RotateFlipType.Rotate90FlipNone; break;
                case 5: rotate_flip_type = RotateFlipType.Rotate90FlipX; break;
                case 6: rotate_flip_type = RotateFlipType.Rotate90FlipY; break;
                case 7: rotate_flip_type = RotateFlipType.Rotate90FlipXY; break;
                case 8: rotate_flip_type = RotateFlipType.Rotate180FlipNone; break;
                case 9: rotate_flip_type = RotateFlipType.Rotate180FlipX; break;
                case 10: rotate_flip_type = RotateFlipType.Rotate180FlipY; break;
                case 11: rotate_flip_type = RotateFlipType.Rotate180FlipXY; break;
                case 12: rotate_flip_type = RotateFlipType.Rotate270FlipNone; break;
                case 13: rotate_flip_type = RotateFlipType.Rotate270FlipX; break;
                case 14: rotate_flip_type = RotateFlipType.Rotate270FlipY; break;
                case 15: rotate_flip_type = RotateFlipType.Rotate270FlipXY; break;
                default: rotate_flip_type = RotateFlipType.RotateNoneFlipNone; break;
            }

            richTextBox1.Text += "選了" + rotate_flip_type.ToString() + "\n";

        }

        private void button2_Click(object sender, EventArgs e)
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

                richTextBox1.Text += "存檔成功\n";
                //richTextBox1.Text += "已存檔 : " + file1 + "\n";
                richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                //richTextBox1.Text += "已存檔 : " + file3 + "\n";
            }
            else
            {
                richTextBox1.Text += "無圖可存\n";
            }

        }



    }
}
