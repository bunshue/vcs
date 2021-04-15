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

namespace vcs_WebCam_Emgu1
{
    public partial class Form1 : Form
    {
        private Capture cap = null;             //宣告一個Webcam物件
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
            if (cap != null)
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
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (cap != null)
            {
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

        //截圖
        private void button4_Click(object sender, EventArgs e)
        {
            if (cap != null)
            {
                Image<Bgr, Byte> image = cap.QueryFrame(); // Query WebCam 的畫面

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
        }

        private void button5_Click(object sender, EventArgs e)
        {
            // Bitmap -> Image
            Image<Bgr, Byte> image = cap.QueryFrame(); // Query WebCam 的畫面

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
            //停止錄影
            if (flag_recording == true)
            {
                //錄影完需將影像停止不然會出錯
                flag_recording = false;
                video.Dispose();
                richTextBox1.Text += "停止錄影\n";
                Application.Idle -= Application_Idle;
            }
            cap.Dispose();
            Application.Exit();
        }
    }
}
