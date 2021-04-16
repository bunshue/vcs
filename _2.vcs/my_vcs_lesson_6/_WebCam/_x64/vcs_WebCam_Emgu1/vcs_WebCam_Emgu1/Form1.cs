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

namespace vcs_WebCam_Emgu1
{
    public partial class Form1 : Form
    {
        private Capture cap = null;             //宣告一個Webcam物件
        private bool flag_webcam_ok = false;    //判斷是否啟動webcam的旗標
        private bool flag_recording = false;    //判斷是否啟動錄影的旗標
        VideoWriter video;

        private bool flag_interrupt_mode = true;    //true : 中斷模式, false : 輪詢模式
        Timer timer1;   //準備給輪詢模式用

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //宣告Timer 1秒執行一次
            timer1 = new Timer();
            timer1.Interval = 1000;
            timer1.Tick += new EventHandler(TimerEventProcessor);
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
                video.WriteFrame<Bgr, byte>(image); //將影格寫入影片中
            }
        }

        private void TimerEventProcessor(object sender, EventArgs e)
        {
            Image<Bgr, Byte> image = cap.QueryFrame(); // Query WebCam 的畫面
            pictureBox1.Image = image.ToBitmap(); // 把畫面轉換成bitmap型態，再丟給pictureBox元件

            //錄影模式
            if (flag_recording == true)
            {
                video.WriteFrame<Bgr, byte>(image); //將影格寫入影片中
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (flag_webcam_ok == false)    //如果webcam沒啟動
            {
                try
                {
                    richTextBox1.Text += "開啟Webcam ......\n";
                    button1.Text = "關閉Webcam";
                    flag_webcam_ok = true;

                    cap = new Capture(0);   //預設使用第一台的webcam
                    //cap = new Capture("C:\\______test_files\\__RW\\_avi\\\i2c.avi");

                    //cap.FlipHorizontal = true;  //左右相反
                    //cap.FlipVertical = true;    //上下顛倒

                    richTextBox1.Text += "W = " + cap.Width.ToString() + ", ";
                    richTextBox1.Text += "H = " + cap.Height.ToString() + "\n";

                    if (flag_interrupt_mode == true)
                    {
                        Application.Idle += new EventHandler(Application_Idle); // 在Idle的event下，把畫面設定到pictureBox上
                    }
                    else
                    {
                        timer1.Start();
                    }

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
                catch (NullReferenceException excpt)
                {
                    MessageBox.Show(excpt.Message);
                }
            }
            else
            {
                richTextBox1.Text += "關閉Webcam ......\n";
                button1.Text = "開啟Webcam";
                flag_webcam_ok = false;
                pictureBox1.Image = null;

                if (flag_interrupt_mode == true)
                {
                    Application.Idle -= new EventHandler(Application_Idle);
                }
                else
                {
                    timer1.Stop();
                }
                cap.Dispose();
                cap = null;
            }
        }

        //關閉程式
        private void bt_exit_Click(object sender, EventArgs e)
        {
            //停止錄影
            if (flag_recording == true)
            {
                //錄影完需將影像停止不然會出錯
                flag_recording = false;
                video.Dispose();
                richTextBox1.Text += "停止錄影\n";
                if (flag_interrupt_mode == true)
                {
                    Application.Idle -= Application_Idle;
                }
                else
                {
                    timer1.Stop();
                }
            }

            if (cap != null)
            {
                cap.Dispose();
            }
            Application.Exit();
        }

        //基本
        //---------------------------------------------------------------------------------------------------------------------------
        //進階

        private void button2_Click(object sender, EventArgs e)
        {
            //上下顛倒
            if (cap != null)
            {
                cap.FlipVertical = !cap.FlipVertical;
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //左右相反
            if (cap != null)
            {
                cap.FlipHorizontal = !cap.FlipHorizontal;
            }
        }

        //截圖
        private void button4_Click(object sender, EventArgs e)
        {
            if (cap != null)
            {
                // Bitmap -> Image
                Image<Bgr, Byte> image = cap.QueryFrame(); // Query WebCam 的畫面

                //儲存路徑
                string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

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
        }

        private void button5_Click(object sender, EventArgs e)
        {
            if (cap == null)
                return;

            //錄影
            if (button5.Text == "錄影")
            {
                button5.Text = "停止錄影";

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
            }
            else
            {
                button5.Text = "錄影";
                //停止錄影
                if (flag_recording == true)
                {
                    //錄影完需將影像停止不然會出錯
                    flag_recording = false;
                    video.Dispose();
                    richTextBox1.Text += "停止錄影\n";
                }
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            if (cap == null)
                return;

            // Bitmap -> Image
            Image<Bgr, Byte> image = cap.QueryFrame(); // Query WebCam 的畫面

            richTextBox1.Text += "Size = " + image.Size.ToString() + "\n";
            richTextBox1.Text += "Width = " + image.Width.ToString() + "\n";
            richTextBox1.Text += "Height = " + image.Height.ToString() + "\n";
            richTextBox1.Text += "Rows = " + image.Rows.ToString() + "\n";
            richTextBox1.Text += "Cols = " + image.Cols.ToString() + "\n";
            richTextBox1.Text += "Bytes.Rank = " + image.Bytes.Rank.ToString() + "\n";
            richTextBox1.Text += "Bytes.Length = " + image.Bytes.Length.ToString() + "\n";
            //richTextBox1.Text += "W = " + image.Data.Length.ToString() + "\n";
            //richTextBox1.Text += "W = " + image.Data.Rank.ToString() + "\n";

            richTextBox1.Text += "NumberOfChannels = " + image.NumberOfChannels.ToString() + "\n";
            richTextBox1.Text += "ROI = " + image.ROI.ToString() + "\n";

        }
    }
}
