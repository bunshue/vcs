using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//參考/加入參考  CV UI Util

//加入/現有項目 core231 highgui231 並設為有更新時才複製

//壓縮影像錄影, 需要再添加:  opencv_ffmpeg_64.dll

/*
把*.csproj
    <PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'Debug|x86' ">
    <PlatformTarget>x86</PlatformTarget>
改
    <PlatformTarget>x64</PlatformTarget>
*/

using Emgu.CV;
using Emgu.CV.Structure;
/*
using Emgu.Util;
using Emgu.CV.CvEnum;
using System.Threading;
*/

namespace vcs_WebCam_Emgu0
{
    public partial class Form1 : Form
    {
        private Capture cap = null;             //宣告一個Webcam物件
        private bool flag_webcam_ok = false;    //判斷是否啟動webcam的旗標

        private bool flag_recording = false;    //判斷是否啟動錄影的旗標, for 錄影1
        VideoWriter video;

        private const int BORDER = 10;
        private const int W_groupBox1 = 640 * 2 + BORDER;
        private const int H_groupBox1 = 220;
        private const int W_pictureBox1 = 640;
        private const int H_pictureBox1 = 480;
        private const int W_richTextBox1 = 640;
        private const int H_richTextBox1 = 480;

        int WEBCAM_NO = 0;    //預設使用的webcam

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            pictureBox1.Size = new Size(W_pictureBox1, H_pictureBox1);
            pictureBox1.Location = new Point(BORDER, BORDER);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            if (flag_recording == true) //錄影1
            {
                //錄影完需將影像停止不然會出錯
                flag_recording = false;
                video.Dispose();
                richTextBox1.Text += "停止錄影\n";
            }
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void Application_Idle(object sender, EventArgs e)
        {
            Image<Bgr, Byte> image = cap.QueryFrame(); // Query WebCam 的畫面
            pictureBox1.Image = image.ToBitmap(); // 把畫面轉換成bitmap型態，再丟給pictureBox元件

            /*  其他處理
            pictureBox1.Image = image.Not().ToBitmap(); // 把畫面轉換成bitmap型態，再丟給pictureBox元件
            Image<Gray, Byte> grayFrame = image.Convert<Gray, Byte>();      //彩色轉灰階
            Image<Gray, Byte> smallGrayFrame = grayFrame.PyrDown();
            Image<Gray, Byte> smoothedGrayFrame = smallGrayFrame.PyrUp();
            Image<Gray, Byte> cannyFrame = smoothedGrayFrame.Canny(new Gray(100), new Gray(60));
            */

            //錄影模式
            if (flag_recording == true) //錄影1
            {
                video.WriteFrame<Bgr, byte>(image); //將影格寫入影片中
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (flag_webcam_ok == false)    //如果webcam沒啟動
            {
                int webcam_no = 0;
                while (true)
                {
                    try
                    {
                        richTextBox1.Text += "開啟Webcam ......try webcam_no = " + webcam_no.ToString() + "\n";

                        cap = new Capture(webcam_no);   //預設使用的webcam
                        //cap = new Capture("C:\\______test_files\\__RW\\_avi\\\i2c.avi");

                        if (cap == null)
                        {
                            richTextBox1.Text += "空的\n";
                            webcam_no++;

                            if (webcam_no > 5)
                            {
                                richTextBox1.Text += "找不到了, 放棄\n";
                                break;
                            }
                            else
                            {
                                continue;
                            }
                        }

                        richTextBox1.Text += "W = " + cap.Width.ToString() + ", ";
                        richTextBox1.Text += "H = " + cap.Height.ToString() + "\n";

                        if (webcam_no > 5)
                        {
                            richTextBox1.Text += "找不到了, 放棄\n";
                            break;
                        }

                        if (cap.Width == 1920)
                        {
                            richTextBox1.Text += "跳過\n";
                            webcam_no++;
                            continue;
                        }


                        //cap.FlipHorizontal = true;  //左右相反
                        //cap.FlipVertical = true;    //上下顛倒


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

                        richTextBox1.Text += "FRAME_WIDTH = " + W.ToString() + "\n";
                        richTextBox1.Text += "FRAME_HEIGHT = " + H.ToString() + "\n";
                        richTextBox1.Text += "FRAME_COUNT = " + frame_count.ToString() + "\n";
                        richTextBox1.Text += "FPS = " + fps.ToString() + "\n";

                        richTextBox1.Text += "CV_CAP_PROP_FORMAT = " + cap.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FORMAT).ToString() + "\n";
                        richTextBox1.Text += "CV_CAP_PROP_MODE = " + cap.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_MODE).ToString() + "\n";
                        richTextBox1.Text += "CV_CAP_PROP_CONVERT_RGB = " + cap.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_CONVERT_RGB).ToString() + "\n";
                        richTextBox1.Text += "CV_CAP_PROP_MONOCROME = " + cap.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_MONOCROME).ToString() + "\n";
                        richTextBox1.Text += "CV_CAP_PROP_FOURCC = " + cap.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FOURCC).ToString() + "\n";
                        richTextBox1.Text += "CV_CAP_PROP_POS_FRAMES = " + cap.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_POS_FRAMES).ToString() + "\n";
                        richTextBox1.Text += "CV_CAP_PROP_POS_AVI_RATIO = " + cap.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_POS_AVI_RATIO).ToString() + "\n";

                        button1.Text = "關閉Webcam";
                        WEBCAM_NO = webcam_no;
                        flag_webcam_ok = true;
                        break;


                    }
                    catch (NullReferenceException excpt)
                    {
                        MessageBox.Show(excpt.Message);
                    }
                }
            }
            else
            {
                richTextBox1.Text += "關閉Webcam ......\n";
                button1.Text = "開啟Webcam";
                flag_webcam_ok = false;
                pictureBox1.Image = null;
                Application.Idle -= new EventHandler(Application_Idle);
                cap.Dispose();
                cap = null;
            }
        }

        //關閉程式
        private void bt_exit_Click(object sender, EventArgs e)
        {
            //停止錄影
            if (flag_recording == true) //錄影1
            {
                //錄影完需將影像停止不然會出錯
                flag_recording = false;
                video.Dispose();
                richTextBox1.Text += "停止錄影\n";
            }

            if (cap != null)
            {
                cap.Dispose();
                Application.Idle -= Application_Idle;
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

        private void button4_Click(object sender, EventArgs e)
        {
            if (flag_webcam_ok == false)    //如果webcam沒啟動
                return;

            //截圖
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

        //錄影1
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
                video = new VideoWriter(filename, 0, 10, cap.Width, cap.Height, true);  //一秒10張, 未壓縮, 應該是1秒10張bmp的圖疊合成一個檔案

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

        private void bt_info_Click(object sender, EventArgs e)
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

        private void button6_Click(object sender, EventArgs e)
        {
            //錄製影像(有壓縮)
            cap = new Capture(WEBCAM_NO);   //預設使用的webcam
            //double fourcc = cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FOURCC);

            if (cap == null)
            {
                MessageBox.Show("找不到攝影機", "error");
            }
            Image<Bgr, Byte> image = cap.QueryFrame(); // Query WebCam 的畫面

            string filename = Application.StartupPath + "\\avi_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".avi";

            VideoWriter video = new VideoWriter(filename, CvInvoke.CV_FOURCC('X', 'V', 'I', 'D'), 30, 640, 480, true);

            while (image != null)
            {
                CvInvoke.cvShowImage("錄製影像, 按ESC停止錄影", image.Ptr);
                image = cap.QueryFrame(); // Query WebCam 的畫面
                video.WriteFrame<Bgr, byte>(image); //將每張圖片製作成影片

                int c = CvInvoke.cvWaitKey(20);
                //遇到事件停止錄影
                if (c == 27)
                    break;
            }
            video.Dispose();
            CvInvoke.cvDestroyWindow("錄製影像, 按ESC停止錄影"); //關閉剛剛開啟的CV視窗

            //錄影完需將影像停止不然會出錯
            flag_webcam_ok = false;
            button1.Text = "開始";
            Application.Idle -= Application_Idle;
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //圖片轉影片
            Image<Bgr, Byte> img;

            string filenamej;

            string filename = Application.StartupPath + "\\avi_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".avi";

            VideoWriter video = new VideoWriter(filename, CvInvoke.CV_FOURCC('X', 'V', 'I', 'D'), 1, 640, 480, true);

            filenamej = @"C:\______test_files\_pic\id_card_01.jpg";
            pictureBox1.Image = Image.FromFile(filenamej);
            img = new Image<Bgr, byte>(filenamej);
            video.WriteFrame<Bgr, byte>(img); //將每張圖片製作成影片
            Application.DoEvents();
            System.Threading.Thread.Sleep(1000);

            filenamej = @"C:\______test_files\_pic\id_card_02.jpg";
            pictureBox1.Image = Image.FromFile(filenamej);
            img = new Image<Bgr, byte>(filenamej);
            video.WriteFrame<Bgr, byte>(img); //將每張圖片製作成影片
            Application.DoEvents();
            System.Threading.Thread.Sleep(1000);

            filenamej = @"C:\______test_files\_pic\id_card_03.jpg";
            pictureBox1.Image = Image.FromFile(filenamej);
            img = new Image<Bgr, byte>(filenamej);
            video.WriteFrame<Bgr, byte>(img); //將每張圖片製作成影片
            Application.DoEvents();
            System.Threading.Thread.Sleep(1000);

            filenamej = @"C:\______test_files\_pic\id_card_04.jpg";
            pictureBox1.Image = Image.FromFile(filenamej);
            img = new Image<Bgr, byte>(filenamej);
            video.WriteFrame<Bgr, byte>(img); //將每張圖片製作成影片
            Application.DoEvents();
            System.Threading.Thread.Sleep(1000);

            filenamej = @"C:\______test_files\_pic\id_card_05.jpg";
            pictureBox1.Image = Image.FromFile(filenamej);
            img = new Image<Bgr, byte>(filenamej);
            video.WriteFrame<Bgr, byte>(img); //將每張圖片製作成影片
            Application.DoEvents();
            System.Threading.Thread.Sleep(1000);

            video.Dispose();

            richTextBox1.Text += "圖片轉影片, 完成\n";
        }
    }
}

