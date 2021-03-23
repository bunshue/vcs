using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using Emgu.CV;
using Emgu.CV.Structure;
using Emgu.Util;
using Emgu.CV.CvEnum;

using System.Threading;

namespace vcs_WebCam_Emgu3k
{
    public partial class Form1 : Form
    {
        private Capture cap = null;             // Webcam物件
        private bool flag_webcam_ok = false;    //判斷是否啟動webcam的旗標

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            cap = new Capture(0);   //預設使用第一台的webcam
            //cap = new Capture("D:\\aaaa.mp4");
            richTextBox1.Text += "Width = " + cap.Width.ToString() + "\n";
            richTextBox1.Text += "Height = " + cap.Height.ToString() + "\n";
            richTextBox1.Text += "FRAME_COUNT = " + cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FRAME_COUNT).ToString() + "\n";
            richTextBox1.Text += "FPS = " + cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FPS).ToString() + "\n";
            richTextBox1.Text += "FORMAT = " + cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FORMAT) + "\n";
        }

        void Application_Idle(object sender, EventArgs e)
        {
            Image<Bgr, Byte> image = cap.QueryFrame(); // Query WebCam 的畫面
            pictureBox1.Image = image.ToBitmap();           // 把畫面轉換成bitmap型態，在丟給pictureBox元件
        }

        //啟動webcam
        private void button1_Click(object sender, EventArgs e)
        {
            //如果webcam沒啟動
            if (cap == null)
            {
                try
                {
                    //打開預設的webcam
                    cap = new Capture();
                }
                catch (NullReferenceException excpt)
                {
                    MessageBox.Show(excpt.Message);
                }
            }

            if (cap != null)    //webcam啟動
            {
                if (flag_webcam_ok == false)
                {
                    //啟動
                    flag_webcam_ok = true;
                    button1.Text = "關閉";
                    Application.Idle += Application_Idle;
                }
                else
                {
                    //關閉
                    flag_webcam_ok = false;
                    button1.Text = "開啟";
                    Application.Idle -= Application_Idle;
                }
            }
        }

        //錄製影像
        private void button2_Click(object sender, EventArgs e)
        {
            cap = new Capture();
            double fourcc = cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FOURCC);

            if (cap == null)
            {
                MessageBox.Show("can't find a camera", "error");
            }
            Image<Bgr, Byte> image = cap.QueryFrame(); // Query WebCam 的畫面

            SaveFileDialog SaveFileDialog1 = new SaveFileDialog();
            SaveFileDialog1.FileName = DateTime.Now.ToString("yyyyMMddhhmmss");
            SaveFileDialog1.Filter = "Image Files(*.avi)|*.avi|All files (*.*)|*.*";
            if (SaveFileDialog1.ShowDialog() == DialogResult.OK)
            {
                MessageBox.Show("開始錄製，按ESC結束錄製");
            }

            VideoWriter video = new VideoWriter(SaveFileDialog1.FileName, CvInvoke.CV_FOURCC('X', 'V', 'I', 'D'), 20, 800, 600, true);

            while (image != null)
            {
                CvInvoke.cvShowImage("camera", image.Ptr);
                image = cap.QueryFrame(); // Query WebCam 的畫面
                int c = CvInvoke.cvWaitKey(20);
                video.WriteFrame<Bgr, byte>(image);
                if (c == 27) break;
            }
            video.Dispose();
            CvInvoke.cvDestroyWindow("camera");

            //錄影完需將影像停止不然會出錯
            flag_webcam_ok = false;
            button1.Text = "開始";
            Application.Idle -= Application_Idle;
        }

        //關閉程式
        private void button3_Click(object sender, EventArgs e)
        {
            cap.Dispose();
            Application.Exit();
        }

        //截圖
        private void button4_Click(object sender, EventArgs e)
        {
            Image<Bgr, Byte> image = cap.QueryFrame(); // Query WebCam 的畫面

            string filename = Application.StartupPath + "\\image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

            try
            {
                image.Save(filename);
                richTextBox1.Text += "已存檔 : " + filename + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
        }
    }
}
