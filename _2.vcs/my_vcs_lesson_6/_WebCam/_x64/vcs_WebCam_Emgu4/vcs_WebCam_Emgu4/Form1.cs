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

namespace vcs_WebCam_Emgu4
{
    public partial class Form1 : Form
    {
        private Capture cap = null;             //宣告一個Webcam物件
        private Capture cap2 = null;
        private bool flag_webcam_ok = false;    //判斷是否啟動webcam的旗標

        bool flag_recording = false;
        VideoWriter video;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void Application_Idle(object sender, EventArgs e)
        {
            Image<Bgr, Byte> image = cap.QueryFrame(); // Query WebCam 的畫面
            pictureBox1.Image = image.ToBitmap(); // 把畫面轉換成bitmap型態，再丟給pictureBox元件

            //錄影模式
            if (flag_recording == true)
            {
                //將影格寫入影片中
                video.WriteFrame<Bgr, byte>(image);
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (flag_webcam_ok == false)
            {
                richTextBox1.Text += "開啟Webcam ......\n";
                button1.Text = "關閉Webcam";
                flag_webcam_ok = true;

                cap = new Capture(0);   //預設使用第一台的webcam
                //cap = new Capture("C:\\______test_files\\__RW\\_avi\\\i2c.avi");
                Application.Idle += new EventHandler(Application_Idle); // 在Idle的event下，把畫面設定到pictureBox上

                //  information
                double W;
                double H;
                double frame_count;
                double fps;
                W = cap.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FRAME_WIDTH);
                H = cap.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FRAME_HEIGHT);
                frame_count = cap.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FRAME_COUNT);
                fps = cap.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FPS);

                richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";
                richTextBox1.Text += "frame_count = " + frame_count.ToString() + "\n";
                richTextBox1.Text += "fps = " + fps.ToString() + "\n";
            }
            else
            {
                richTextBox1.Text += "關閉Webcam ......\n";
                button1.Text = "開啟Webcam";
                flag_webcam_ok = false;
                pictureBox1.Image = null;

                Application.Idle -= new EventHandler(Application_Idle);
                cap.Dispose();
            }
        }

        //錄影
        private void button2_Click(object sender, EventArgs e)
        {
            string filename = Application.StartupPath + "\\avi_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".avi";

            richTextBox1.Text += "filename : " + filename + "\n";
            richTextBox1.Text += "Width : " + cap.Width.ToString() + "\n";
            richTextBox1.Text += "Height : " + cap.Height.ToString() + "\n";

            //cap.Width 取得攝影機可支援的最大寬度
            //cap.Height 取得攝影機可支援的最大高度
            video = new VideoWriter(filename, 0, 10, cap.Width, cap.Height, true);

            //開啟錄影模式
            flag_recording = true;

            richTextBox1.Text += "開始錄影\n";
            Application.Idle += Application_Idle;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //停止錄影
            if (flag_recording == true)
            {
                //錄影完需將影像停止不然會出錯
                flag_recording = false;
                video.Dispose();
                richTextBox1.Text += "停止錄影\n";
                Application.Idle -= Application_Idle;
            }
        }

        //截圖
        private void button4_Click(object sender, EventArgs e)
        {
            if (flag_webcam_ok == false)
            {
                richTextBox1.Text += "尚未開啟webcam\n";
                return;
            }

            richTextBox1.Text += "截圖\t\t";

            //  截圖  Query 攝影機的畫面
            Image<Bgr, Byte> image = cap.QueryFrame();

            string filename = Application.StartupPath + "\\image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

            try
            {
                image.Save(filename);   //儲存影像
                richTextBox1.Text += "已存檔 : " + filename + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }

        }

        private void button5_Click(object sender, EventArgs e)
        {
            //不 OK

            //string filename = "F:\\Naval Legends Yamato  World of Warships.mp4";
            //string filename = "C:\\______test_files\\胃カメラによる上部消化管検査 [720p].mp4";
            string filename = @"C:\______test_files\__RW\_avi\i2c.avi";

            //Capture cap2 = null;
            cap2 = new Capture(filename);

            double W;
            double H;
            double frame_count;
            double fps;

            W = cap2.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FRAME_WIDTH);
            H = cap2.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FRAME_HEIGHT);
            frame_count = cap2.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FRAME_COUNT);
            fps = cap2.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FPS);

            richTextBox1.Text += "FRAME_WIDTH = " + W.ToString() + "\n";
            richTextBox1.Text += "FRAME_HEIGHT = " + H.ToString() + "\n";
            richTextBox1.Text += "FRAME_COUNT = " + frame_count.ToString() + "\n";
            richTextBox1.Text += "FPS = " + fps.ToString() + "\n";

            double sec = frame_count / fps;
            if (sec > 60)
                richTextBox1.Text += "duration = " + ((int)(sec / 60)).ToString() + " 分 " + (sec % 60).ToString() + " 秒\n";
            else
                richTextBox1.Text += "duration = " + sec.ToString() + " 秒\n";

            /*
            //test
            Image<Bgr, Byte> image = cap2.QueryFrame();
            pictureBox1.Image = image.ToBitmap();
            */


            filename = @"C:\______test_files\picture1.jpg";
            cap2 = new Capture(filename);

            W = cap2.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FRAME_WIDTH);
            H = cap2.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FRAME_HEIGHT);
            frame_count = cap2.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FRAME_COUNT);
            fps = cap2.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FPS);

            richTextBox1.Text += "FRAME_WIDTH = " + W.ToString() + "\n";
            richTextBox1.Text += "FRAME_HEIGHT = " + H.ToString() + "\n";
            richTextBox1.Text += "FRAME_COUNT = " + frame_count.ToString() + "\n";
            richTextBox1.Text += "FPS = " + fps.ToString() + "\n";

            Image<Bgr, Byte> image = cap2.QueryFrame();
            pictureBox1.Image = image.ToBitmap();

        }

        private void button7_Click(object sender, EventArgs e)
        {
            //Image<Gray, int> inputImage = new Image<Gray, byte>(new Size(640, 480));
            //pictureBox1.Image = inputImage.ToBitmap();




            //string filename = @"C:\______test_files\pic_256X100.jpg";
            string filename = @"C:\______test_files\pic_256X100b.bmp";

            //Load the Image
            Image<Bgr, Byte> img1 = new Image<Bgr, byte>(filename);

            //Display the Image
            pictureBox1.Image = img1.ToBitmap();

            int W = img1.Bitmap.Width;
            int H = img1.Bitmap.Height;
            int len = img1.Bytes.Length;


            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";
            richTextBox1.Text += "Length = " + len.ToString() + "\n";
            richTextBox1.Text += "W = " + img1.Size.Width.ToString() + ", H = " + img1.Size.Height.ToString() + "\n";
            richTextBox1.Text += "W = " + img1.Width.ToString() + ", H = " + img1.Height.ToString() + "\n";
            richTextBox1.Text += "cols = " + img1.Cols.ToString() + ", rows = " + img1.Rows.ToString() + "\n";

            int i;
            for (i = 0; i < img1.Bytes.Length / 100; i++)
            {
                richTextBox1.Text += img1.Bytes[i].ToString() + " ";
            }


            //不能直接修改數值 ?!?!
            for (i = 0; i < 500; i++)
            {
                //img1.Bytes[i] = (byte)(((int)img1.Bytes[i] + (int)img1.Bytes[i + 1] + (int)img1.Bytes[i + 2]) / 3);
                img1.Bytes[i] = 0;
            }


            pictureBox1.Image = img1.ToBitmap();

            richTextBox1.Text += "\n\n";

            for (i = 0; i < img1.Bytes.Length / 100; i++)
            {
                richTextBox1.Text += img1.Bytes[i].ToString() + " ";
            }



            /*
            Image<Bgr, Byte> img2 = img1.Flip(Emgu.CV.CvEnum.FLIP.HORIZONTAL);
            pictureBox2.Image = img2.ToBitmap();

            Image<Bgr, Byte> img3 = img1.Flip(Emgu.CV.CvEnum.FLIP.VERTICAL);
            pictureBox3.Image = img3.ToBitmap();

            Image<Bgr, Byte> img4 = img1.Flip(Emgu.CV.CvEnum.FLIP.HORIZONTAL).Flip(Emgu.CV.CvEnum.FLIP.VERTICAL);
            pictureBox4.Image = img4.ToBitmap();
            */

        }

        private void button6_Click(object sender, EventArgs e)
        {
            if (flag_webcam_ok == true)
            {
                double W;
                double H;
                double frame_count;
                double fps;

                W = cap.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FRAME_WIDTH);
                H = cap.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FRAME_HEIGHT);
                frame_count = cap.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FRAME_COUNT);
                fps = cap.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FPS);

                richTextBox1.Text += "FRAME_WIDTH = " + W.ToString() + "\n";
                richTextBox1.Text += "FRAME_HEIGHT = " + H.ToString() + "\n";
                richTextBox1.Text += "FRAME_COUNT = " + frame_count.ToString() + "\n";
                richTextBox1.Text += "FPS = " + fps.ToString() + "\n";
            }
        }

        //上下顛倒
        private void button8_Click(object sender, EventArgs e)
        {
            if (cap != null)
            {
                cap.FlipVertical = !cap.FlipVertical;
            }
        }

        //左右相反
        private void button9_Click(object sender, EventArgs e)
        {
            if (cap != null)
            {
                cap.FlipHorizontal = !cap.FlipHorizontal;
            }
        }

        //關閉程式
        private void bt_exit_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "離開 ......\n";

            if (flag_webcam_ok == true)
            {
                cap.Dispose();
                Application.Idle -= Application_Idle;
            }

            //停止錄影
            if (flag_recording == true)
            {
                //錄影完需將影像停止不然會出錯
                flag_recording = false;
                video.Dispose();
                richTextBox1.Text += "停止錄影\n";
                Application.Idle -= Application_Idle;
            }
            Application.Exit();
        }
    }
}
