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
using Emgu.CV.CvEnum;

namespace vcs_WebCam_Emgu0
{
    public partial class Form1 : Form
    {
        // Webcam物件
        private Capture cap = null;
        //判斷是否啟動webcam的frame旗標
        private bool _captureInProgress = false;

        bool _isRecording = false;
        string _fileName;
        Timer _timer;
        VideoWriter video;

        public Form1()
        {
            InitializeComponent();

            //宣告Timer 0.1秒執行一次
            _timer = new Timer();
            _timer.Interval = 100;
            _timer.Tick += new EventHandler(TimerEventProcessor);
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void TimerEventProcessor(object sender, EventArgs e)
        {
            Image<Bgr, Byte> frame = cap.QueryFrame(); // Query 攝影機的畫面

            pictureBox1.Image = frame.ToBitmap(); // 把畫面轉換成bitmap型態，在丟給pictureBox元件

            //錄影模式
            if (_isRecording == true)
            {
                //將影格寫入影片中
                video.WriteFrame<Bgr, byte>(frame);
            }
        }

        /// <summary>
        /// 開啟攝影機
        /// </summary>
        private void openWebCam()
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
        }

        private void button1_Click(object sender, EventArgs e)
        {
            openWebCam();

            //webcam啟動
            if (cap != null)
            {
                //frame啟動
                if (_captureInProgress == true)
                {
                    //stop the capture
                    _captureInProgress = false;
                    button1.Text = "開啟";
                    _timer.Stop();
                }
                //frame關閉
                else
                {
                    //start the capture
                    _captureInProgress = true;
                    button1.Text = "關閉";
                    _timer.Start();
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            openWebCam();

            _timer.Start();

            _fileName = Application.StartupPath + "\\avi_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".avi";

            richTextBox1.Text += "filename : " + _fileName + "\n";
            richTextBox1.Text += "Width : " + cap.Width.ToString() + "\n";
            richTextBox1.Text += "Height : " + cap.Height.ToString() + "\n";

            //cap.Width 取得攝影機可支援的最大寬度
            //cap.Height 取得攝影機可支援的最大高度
            video = new VideoWriter(_fileName, 0, 10, cap.Width, cap.Height, true);

            //開啟錄影模式
            _isRecording = true;

            richTextBox1.Text += "開始錄影\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //錄影完需將影像停止不然會出錯
            _isRecording = false;
            video.Dispose();

            richTextBox1.Text += "停止錄影\n";
        }

        //拍攝照片
        private void button4_Click(object sender, EventArgs e)
        {
            openWebCam();

            // Query 攝影機的畫面
            Image<Bgr, Byte> image = cap.QueryFrame();

            //儲存路徑
            string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

            //儲存影像
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

        private void button5_Click(object sender, EventArgs e)
        {
            // Query 攝影機的畫面
            // Bitmap -> Image
            Image<Bgr, Byte> image = cap.QueryFrame();

            /*
            //儲存路徑
            string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

            //儲存影像
            try
            {
                image.Save(filename);
                richTextBox1.Text += "已存檔 : " + filename + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
            */

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

            int i;
            for (i = 0; i < 300; i++)
            {
                //richTextBox1.Text += image[i].ToString() + " ";
                //richTextBox1.Text += image.Data[100, 100, 0].ToString("X2") + " ";
                //richTextBox1.Text += image.Data[10, 10, 1].ToString() + " ";

            }
            richTextBox1.Text += "\n";


            /*
            image.Save("file1.bmp");

            //Image(RGB) -> Image(Gray)
            Image<Gray, Byte> gimage = image.Convert<Gray, Byte>();
            gimage.Save("file2.bmp");
            */

            /*
            //灰階轉回彩色
            Image<Rgb, Byte> newimage = gimage.Convert<Rgb, Byte>();
            newimage.Save("file3.bmp");


            //Image -> Bitmap
            Bitmap result = image.ToBitmap();
            result.Save("file4.bmp");
            */



        }


        /*
        public void TestRun(Bitmap bitmap)
        {
            int W = bitmap.Width;
            int H = bitmap.Height;

            Image<Bgr, Byte> img = new Image<Bgr, Byte>(bitmap);
            //灰階
            Image<Gray, Byte> gray = img.Convert<Gray, Byte>().PyrDown().PyrUp();
        */
            /*
                                    //二值化
                                    Image<Gray, Byte> gray1 = gray.ThresholdToZero(new Gray(Settings.ThresholdToZero));
                                    //http://www.cnblogs.com/xrwang/archive/2010/03/03/ImageFeatureDetection.html.
                                    //Canny算子也可以用作边缘检测
                                    Image<Gray, Byte> gray2 = gray1.Canny(new Gray(Settings.LowThresh), new Gray(Settings.HighThresh));
             */

        /*
            Bitmap image = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            using (Graphics g = Graphics.FromImage(image))
            {
                Rectangle rct1 = new Rectangle(new Point(0, 0), new Size(W / 2, H / 2));
                g.DrawImage(img.Bitmap, rct1, new Rectangle(new Point(0, 0), new Size(W, H)), GraphicsUnit.Pixel);
                g.DrawRectangle(new Pen(Color.Black), rct1);

                Rectangle rct2 = new Rectangle(new Point(0, W / 2), new Size(W / 2, H / 2));
                g.DrawImage(gray.Bitmap, rct2, new Rectangle(new Point(0, 0), new Size(W, H)), GraphicsUnit.Pixel);
                g.DrawRectangle(new Pen(Color.Black), rct2);
        */
                /*
                               Rectangle rct3 = new Rectangle(new Point(H / 2, 0), new Size(W / 2, H / 2));
                               g.DrawImage(gray1.Bitmap, rct3, new Rectangle(new Point(0, 0), new Size(W, H)), GraphicsUnit.Pixel);
                               g.DrawRectangle(new Pen(Color.Black), rct3);
 
                               Rectangle rct4 = new Rectangle(new Point(H / 2, W / 2), new Size(W / 2, H / 2));
 
                               g.DrawImage(gray2.Bitmap, rct4, new Rectangle(new Point(0, 0), new Size(W, H)), GraphicsUnit.Pixel);
                               g.DrawRectangle(new Pen(Color.Black), rct4);
               */
        /*
            }
            pictureBox1.Image = image;

        }
        */

        private void button6_Click(object sender, EventArgs e)
        {
            //Bitmap bmp = new Bitmap(@"C:\______test_files\picture1.jpg");

            //TestRun(bmp);


        }

        private void button7_Click(object sender, EventArgs e)
        {
            //Image<Gray, int> inputImage = new Image<Gray, byte>(new Size(640, 480));
            //pictureBox1.Image = inputImage.ToBitmap();

        }
 


    }
}
