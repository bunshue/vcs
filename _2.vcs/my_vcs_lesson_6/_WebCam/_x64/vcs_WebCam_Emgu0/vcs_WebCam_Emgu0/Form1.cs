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
using Emgu.CV.CvEnum;
using Emgu.CV.UI;   //for ImageViewer

/*
using Emgu.Util;
using System.Threading;
*/

namespace vcs_WebCam_Emgu0
{
    public partial class Form1 : Form
    {
        private Capture cap = null;             //宣告一個Webcam物件
        private bool flag_webcam_ok = false;    //判斷是否啟動webcam的旗標

        private const int BORDER = 10;
        private const int W_groupBox1 = 640 * 2 + BORDER;
        private const int H_groupBox1 = 220;
        private const int W_pictureBox1 = 640;
        private const int H_pictureBox1 = 480;
        private const int W_richTextBox1 = 300;
        private const int H_richTextBox1 = 480;
        int WEBCAM_NO = 0;    //預設使用的webcam

        private bool flag_recording = false;    //判斷是否啟動錄影的旗標, for 錄影1
        private string recording_filename = string.Empty;
        VideoWriter vw;
        DateTime recording_time_st = DateTime.Now;
        int total_frame_count = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
            recording_filename = Application.StartupPath + "\\avi_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".avi";
        }

        void show_item_location()
        {
            int x_st = 670;
            int y_st = BORDER;
            int dx = 130;
            int dy = 45;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            bt_exit.Location = new Point(x_st + dx * 1, y_st + dy * 11);

            pictureBox1.Size = new Size(W_pictureBox1, H_pictureBox1);
            pictureBox1.Location = new Point(BORDER, BORDER);

            richTextBox1.Size = new Size(W_richTextBox1, H_richTextBox1);
            richTextBox1.Location = new Point(x_st + dx * 2 + 30, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            button0.Enabled = true;
            button1.Enabled = false;

            x_st = 10;
            y_st = BORDER * 2;
            dx = 130;
            dy = 45;

            button20.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button23.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            button24.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            button25.Location = new Point(x_st + dx * 5, y_st + dy * 0);

            lb_frame.Location = new Point(x_st + dx * 6 + 50, y_st + dy * 0 + 8);
            lb_frame.Text = "";
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            if (flag_recording == true) //錄影1
            {
                //錄影完需將影像停止不然會出錯
                flag_recording = false;
                vw.Dispose();
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

            //MCvFont font = new MCvFont(FONT.CV_FONT_HERSHEY_COMPLEX, 1.0, 1.0);
            //MCvFont font = new MCvFont(FONT.CV_FONT_HERSHEY_TRIPLEX, 0.5d, 0.5d);
            //MCvFont font = new MCvFont(FONT.CV_FONT_HERSHEY_PLAIN, 1.0, 1.0);
            //MCvFont font = new MCvFont(FONT.CV_FONT_HERSHEY_DUPLEX, 1d, 1d);
            //MCvFont font = new MCvFont(FONT.CV_FONT_HERSHEY_PLAIN, 3.0, 3.0);
            MCvFont font = new MCvFont(FONT.CV_FONT_HERSHEY_SIMPLEX, 0.5, 0.5);

            font.thickness = 1;

            if (flag_recording == true) //錄影1
            {
                if (DateTime.Now.Millisecond > 500)
                {
                    image.Draw(DateTime.Now.ToString() + "  Recording", ref font, new Point(20, 40), new Bgr(Color.Red));
                }
                vw.WriteFrame<Bgr, byte>(image); //將影格寫入影片中, 將每張圖片製作成影片
            }
            else
            {
                image.Draw(DateTime.Now.ToString(), ref font, new Point(20, 40), new Bgr(Color.Gold));
            }

            //Image<Bgr, Byte> image = cap.QueryFrame(); // Query WebCam 的畫面
            pictureBox1.Image = image.ToBitmap(); // 把畫面轉換成bitmap型態，再丟給pictureBox元件


            /*  其他處理
            pictureBox1.Image = image.Not().ToBitmap(); // 把畫面轉換成bitmap型態，再丟給pictureBox元件
            Image<Gray, Byte> grayFrame = image.Convert<Gray, Byte>();      //彩色轉灰階
            Image<Gray, Byte> smallGrayFrame = grayFrame.PyrDown();
            Image<Gray, Byte> smoothedGrayFrame = smallGrayFrame.PyrUp();
            Image<Gray, Byte> cannyFrame = smoothedGrayFrame.Canny(new Gray(100), new Gray(60));
            */
        }

        private void button0_Click(object sender, EventArgs e)
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
                        //cap = new Capture(@"C:\_git\vcs\_1.data\______test_files1\_video\i2c.avi");

                        if (cap == null)
                        {
                            richTextBox1.Text += "無相機\n";
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

                        //cap.SetCaptureProperty(CAP_PROP.CV_CAP_PROP_FRAME_WIDTH, 1280);
                        //cap.SetCaptureProperty(CAP_PROP.CV_CAP_PROP_FRAME_HEIGHT, 720);
                        //cap.SetCaptureProperty(CAP_PROP.CV_CAP_PROP_FPS, 30);



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


                        //cap.SetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FOURCC, CvInvoke.CV_FOURCC('M', 'J', 'P', 'G'));

                        Application.Idle += new EventHandler(Application_Idle); // 在Idle的event下，把畫面設定到pictureBox上

                        //cap.SetCaptureProperty(CAP_PROP.CV_CAP_PROP_BRIGHTNESS, 80);

                        double codec_double = cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FOURCC);
                        string s = new string(System.Text.Encoding.UTF8.GetString(BitConverter.GetBytes(Convert.ToUInt32(codec_double))).ToCharArray());


                        richTextBox1.Text += "Codec: " + codec_double.ToString() + "\n";
                        richTextBox1.Text += "Codec: " + s + "\n";




                        WEBCAM_NO = webcam_no;
                        flag_webcam_ok = true;
                        button0.Enabled = false;
                        button1.Enabled = true;
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
                richTextBox1.Text += "相機已開啟\n";
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (flag_webcam_ok == true)    //如果webcam已啟動
            {
                richTextBox1.Text += "關閉Webcam ......\n";
                flag_webcam_ok = false;
                pictureBox1.Image = null;
                Application.Idle -= new EventHandler(Application_Idle);
                cap.Dispose();
                cap = null;
                button0.Enabled = true;
                button1.Enabled = false;
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
                vw.Dispose();
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
            if (flag_webcam_ok == false)    //如果webcam沒啟動
            {
                richTextBox1.Text += "無相機\n";
                return;
            }

            //上下顛倒
            if (cap != null)
            {
                cap.FlipVertical = !cap.FlipVertical;
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (flag_webcam_ok == false)    //如果webcam沒啟動
            {
                richTextBox1.Text += "無相機\n";
                return;
            }

            //左右相反
            if (cap != null)
            {
                cap.FlipHorizontal = !cap.FlipHorizontal;
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (flag_webcam_ok == false)    //如果webcam沒啟動
            {
                richTextBox1.Text += "無相機\n";
                return;
            }

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

        //錄影 ST
        private void button5_Click(object sender, EventArgs e)
        {
            if (flag_webcam_ok == false)    //如果webcam沒啟動
            {
                richTextBox1.Text += "無相機\n";
                return;
            }

            if (flag_recording == false)
            {
                //開啟錄影模式
                flag_recording = true;

                recording_filename = Application.StartupPath + "\\avi_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".avi";

                richTextBox1.Text += "filename : " + recording_filename + "\n";
                richTextBox1.Text += "Width : " + cap.Width.ToString() + "\n";
                richTextBox1.Text += "Height : " + cap.Height.ToString() + "\n";

                //cap.Width 取得攝影機可支援的最大寬度
                //cap.Height 取得攝影機可支援的最大高度

                //未壓縮
                //public VideoWriter(string fileName, int compressionCode, int fps, int width, int height, bool isColor);
                //vw = new VideoWriter(recording_filename, 0, 10, cap.Width, cap.Height, true);  //一秒10張, 未壓縮, 應該是1秒10張bmp的圖疊合成一個檔案

                //int codec = CvInvoke.CV_FOURCC('P', 'I', 'M', '1');
                int codec = CvInvoke.CV_FOURCC('X', 'V', 'I', 'D');

                int fps = 30;
                int W = 640;
                int H = 480;

                //有壓縮
                //public VideoWriter(string fileName, int compressionCode, int fps, int width, int height, bool isColor);
                vw = new VideoWriter(recording_filename, codec, fps, W, H, true);   //一秒30張

                //XXXXXXXX
                //public VideoWriter(string fileName, int fps, int width, int height, bool isColor);
                //vw = new VideoWriter(recording_filename, fps, W, H, true);   //一秒30張

                richTextBox1.Text += "錄影開始\t時間 : " + DateTime.Now.ToString() + "\n";
                recording_time_st = DateTime.Now;
            }
            else
            {
                richTextBox1.Text += "已在錄影\n";
            }
        }

        //錄影 SP
        private void button6_Click(object sender, EventArgs e)
        {
            if (flag_recording == true)
            {
                //錄影完需將影像停止不然會出錯
                flag_recording = false;
                vw.Dispose();
                richTextBox1.Text += "錄影結束\t時間 : " + DateTime.Now.ToString() + "\n";
                richTextBox1.Text += "錄影時間 : " + (DateTime.Now - recording_time_st).TotalSeconds.ToString("0.00") + " 秒\n\n";
                //richTextBox1.Text += "錄影時間 : " + (DateTime.Now - recording_time_st).ToString() + "\n\n";
            }
            else
            {
                richTextBox1.Text += "並沒有在錄影\n";
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //錄製影像(有壓縮)
            cap = new Capture(WEBCAM_NO);   //預設使用的webcam
            //double fourcc = cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FOURCC);

            if (cap == null)
            {
                richTextBox1.Text += "無相機\n";
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
            Application.Idle -= Application_Idle;
        }

        private void button8_Click(object sender, EventArgs e)
        {
            if (cap == null)
            {
                richTextBox1.Text += "無相機\n";
                return;
            }

            Image<Bgr, Byte> image = cap.QueryFrame(); // Query WebCam 的畫面

            if (image != null)
            {
                CvInvoke.cvShowImage("使用cvShowImage抓一圖", image.Ptr);
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            CvInvoke.cvDestroyWindow("使用cvShowImage抓一圖");   //關閉剛剛開啟的CV視窗
        }

        private void button10_Click(object sender, EventArgs e)
        {

        }

        private void button11_Click(object sender, EventArgs e)
        {
        }

        private void button12_Click(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            Image<Bgr, Byte> image = cap.QueryFrame(); // Query WebCam 的畫面

            if (image != null)
            {


                pictureBox1.Image = image.ToBitmap(); // 把畫面轉換成bitmap型態，再丟給pictureBox元件
            }
            else
            {
                timer1.Enabled = false;

            }

        }

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button15_Click(object sender, EventArgs e)
        {

        }

        private void button16_Click(object sender, EventArgs e)
        {

        }

        private void button17_Click(object sender, EventArgs e)
        {
            using (Image<Bgr, Byte> image = new Image<Bgr, byte>(500, 200, new Bgr(255, 0, 0)))
            {
                MCvFont font = new MCvFont(FONT.CV_FONT_HERSHEY_COMPLEX, 1.0, 1.0);

                image.Draw("EMGU ImageViewer Test", ref font, new Point(10, 80), new Bgr(0, 255, 0));

                //Show the image using ImageViewer from Emgu.CV.UI
                ImageViewer viewer = new ImageViewer(image, "EMGU Test");
                viewer.ShowDialog();
            }
        }

        private void button18_Click(object sender, EventArgs e)
        {
            //cap.SetCaptureProperty(CAP_PROP.CV_CAP_PROP_FOURCC, 4);


            //double fourcc = cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FOURCC);
            //richTextBox1.Text += "4-character code of codec : " + fourcc.ToString() + "\n";

            //this->camRef.set(CV_CAP_PROP_FOURCC,CV_FOURCC('M','J','P','G'));

            //改變camera的設定

            //cap.SetCaptureProperty(CAP_PROP.CV_CAP_PROP_FRAME_WIDTH, 320);
            //cap.SetCaptureProperty(CAP_PROP.CV_CAP_PROP_FRAME_HEIGHT, 240);
            /*
            //取得目前所播放的幀數 對播放檔案才有用
            double frame_no = cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_POS_FRAMES);
            richTextBox1.Text += frame_no.ToString() + "\n";


            double time_index = cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_POS_MSEC);
            richTextBox1.Text += "Time: " + TimeSpan.FromMilliseconds(time_index).ToString().Substring(0, 8) + "\n";


            //跳至第100幀
            cap.SetCaptureProperty(CAP_PROP.CV_CAP_PROP_POS_FRAMES, 100);
            */

            /*
            double codec_double = cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FOURCC);
            string s = new string(System.Text.Encoding.UTF8.GetString(BitConverter.GetBytes(Convert.ToUInt32(codec_double))).ToCharArray());


            richTextBox1.Text += "Codec: " + codec_double.ToString() + "\n";
            richTextBox1.Text += "Codec: " + s + "\n\n";
            */




        }

        private void button19_Click(object sender, EventArgs e)
        {
            if (cap == null)
            {
                richTextBox1.Text += "無相機\n";
                return;
            }

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

            richTextBox1.Text += "info = \n";
            GetVideoInformation(cap);
        }

        private void GetVideoInformation(Capture cap)
        {
            //  information
            double W = cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FRAME_WIDTH);
            double H = cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FRAME_HEIGHT);
            double frame_count = cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FRAME_COUNT);
            double fps = cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FPS);

            richTextBox1.Text += "FRAME_WIDTH = " + W.ToString() + "\n";
            richTextBox1.Text += "FRAME_HEIGHT = " + H.ToString() + "\n";
            richTextBox1.Text += "FRAME_COUNT = " + frame_count.ToString() + "\n";
            richTextBox1.Text += "FPS = " + fps.ToString() + "\n";

            richTextBox1.Text += "CV_CAP_PROP_FORMAT = " + cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FORMAT).ToString() + "\n";
            richTextBox1.Text += "CV_CAP_PROP_MODE = " + cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_MODE).ToString() + "\n";
            richTextBox1.Text += "CV_CAP_PROP_CONVERT_RGB = " + cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_CONVERT_RGB).ToString() + "\n";
            richTextBox1.Text += "CV_CAP_PROP_MONOCROME = " + cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_MONOCROME).ToString() + "\n";
            richTextBox1.Text += "CV_CAP_PROP_FOURCC = " + cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FOURCC).ToString() + "\n";
            richTextBox1.Text += "CV_CAP_PROP_POS_FRAMES = " + cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_POS_FRAMES).ToString() + "\n";
            richTextBox1.Text += "CV_CAP_PROP_POS_AVI_RATIO = " + cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_POS_AVI_RATIO).ToString() + "\n";

            richTextBox1.Text += "CV_CAP_PROP_CONTRAST = " + (int)cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_CONTRAST) + "\n";
            richTextBox1.Text += "CV_CAP_PROP_BRIGHTNESS = " + (int)cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_BRIGHTNESS) + "\n";
            richTextBox1.Text += "CV_CAP_PROP_GAIN = " + (int)cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_GAIN) + "\n";

            richTextBox1.Text += "CV_CAP_PROP_BRIGHTNESS = " + cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_BRIGHTNESS) + "\n";
            richTextBox1.Text += "CV_CAP_PROP_CONTRAST = " + cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_CONTRAST) + "\n";
            richTextBox1.Text += "CV_CAP_PROP_SHARPNESS = " + cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_SHARPNESS) + "\n";
            richTextBox1.Text += "CV_CAP_PROP_SATURATION = " + cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_SATURATION) + "\n";
            richTextBox1.Text += "CV_CAP_PROP_WHITE_BALANCE_BLUE_U = " + cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_WHITE_BALANCE_BLUE_U) + "\n";
            richTextBox1.Text += "CV_CAP_PROP_WHITE_BALANCE_RED_V = " + cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_WHITE_BALANCE_RED_V) + "\n";
            richTextBox1.Text += "CV_CAP_PROP_HUE = " + cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_HUE) + "\n";
            richTextBox1.Text += "CV_CAP_PROP_GAIN = " + cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_GAIN) + "\n";
            richTextBox1.Text += "CV_CAP_PROP_GAMMA = " + cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_GAMMA) + "\n";

            double fourcc = cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FOURCC);
            richTextBox1.Text += "4-character code of codec : " + fourcc.ToString() + "\n";

            double brightness = cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_BRIGHTNESS);
            richTextBox1.Text += "brightness : " + brightness.ToString() + "\n";

            var codecDouble = cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FOURCC);
            //var codec = ConvertToStringCaptureProperty(codecDouble);


        }

        private void button20_Click(object sender, EventArgs e)
        {
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            //播放影片檔案
            //string filename = @"C:\_git\vcs\_1.data\______test_files1\_video\i2c.avi";

            //string filename = @"D:\內視鏡影片\院長平島徹朗が実際に胃内視鏡検査を受けました Full ver [720p].mp4";
            string filename = @"D:\aaaa.mp4";

            //Opens the movie file
            cap = new Capture(filename);

            richTextBox1.Text += "此影片檔案格式:\n";

            double W = cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FRAME_WIDTH);
            double H = cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FRAME_HEIGHT);
            double frame_count = cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FRAME_COUNT);
            double fps = cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FPS);

            richTextBox1.Text += "FRAME_WIDTH = " + W.ToString() + "\n";
            richTextBox1.Text += "FRAME_HEIGHT = " + H.ToString() + "\n";
            richTextBox1.Text += "FRAME_COUNT = " + frame_count.ToString() + "\n";
            richTextBox1.Text += "FPS = " + fps.ToString() + "\n";
            richTextBox1.Text += "影片長度 = " + (frame_count / fps).ToString() + " 秒\n";

            int FCapturePeriod = (int)(1000.0d / fps);
            richTextBox1.Text += "兩幀間距 = " + FCapturePeriod.ToString() + " msec\n";


            int FPS = (int)cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FPS);
            int frameCount = (int)cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FRAME_COUNT);

            //msec between frames
            int msec = (int)(1000 / FPS);

            richTextBox1.Text += "msec = " + msec.ToString() + "\n";

            if (fps > 0)
            {
                timer1.Interval = (int)Math.Ceiling((1000 / fps)) - 3;
            }
            else
            {
                fps = 25;
                timer1.Interval = 40;
            }

            timer1.Interval = msec;
            timer1.Enabled = true;

            double fourcc = cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FOURCC);
            richTextBox1.Text += "4-character code of codec : " + fourcc.ToString() + "\n";

            double brightness = cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_BRIGHTNESS);
            richTextBox1.Text += "brightness : " + brightness.ToString() + "\n";

            double totalFrameCount = cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FRAME_COUNT);
            //cap.ImageGrabbed += ProcessFrame;

            //Application.Idle += ProcessFrame;

            //timer.Start();
            //cap.ImageGrabbed += ProcessFrame;
            //if (timer.ElapsedMilliseconds == 1000) cap.Stop();


            //pictureBox1.Width = cap.Width;
            //pictureBox1.Height = cap.Height;


            //cap.SetCaptureProperty(CAP_PROP.CV_CAP_PROP_FPS, 5);
            //cap.ImageGrabbed += VideoCaptureInterface_ImageGrabbed;

            total_frame_count = (int)frame_count;
            trackBar1.Maximum = (int)frame_count;
        }

        void ProcessFrame(object sender, EventArgs e)
        {
            Image<Bgr, Byte> image = cap.QueryFrame(); // Query WebCam 的畫面
            /*
            //MCvFont font = new MCvFont(FONT.CV_FONT_HERSHEY_COMPLEX, 1.0, 1.0);
            //MCvFont font = new MCvFont(FONT.CV_FONT_HERSHEY_TRIPLEX, 0.5d, 0.5d);
            //MCvFont font = new MCvFont(FONT.CV_FONT_HERSHEY_PLAIN, 1.0, 1.0);
            //MCvFont font = new MCvFont(FONT.CV_FONT_HERSHEY_DUPLEX, 1d, 1d);
            //MCvFont font = new MCvFont(FONT.CV_FONT_HERSHEY_PLAIN, 3.0, 3.0);
            MCvFont font = new MCvFont(FONT.CV_FONT_HERSHEY_SIMPLEX, 0.5, 0.5);

            font.thickness = 1;

            if (flag_recording == true) //錄影1
            {
                if (DateTime.Now.Millisecond > 500)
                {
                    image.Draw(DateTime.Now.ToString() + "  Recording", ref font, new Point(20, 40), new Bgr(Color.Red));
                }
                vw.WriteFrame<Bgr, byte>(image); //將影格寫入影片中, 將每張圖片製作成影片
            }
            else
            {
                image.Draw(DateTime.Now.ToString(), ref font, new Point(20, 40), new Bgr(Color.Gold));
            }
            */
            //Image<Bgr, Byte> image = cap.QueryFrame(); // Query WebCam 的畫面
            pictureBox1.Image = image.ToBitmap(); // 把畫面轉換成bitmap型態，再丟給pictureBox元件


            /*  其他處理
            pictureBox1.Image = image.Not().ToBitmap(); // 把畫面轉換成bitmap型態，再丟給pictureBox元件
            Image<Gray, Byte> grayFrame = image.Convert<Gray, Byte>();      //彩色轉灰階
            Image<Gray, Byte> smallGrayFrame = grayFrame.PyrDown();
            Image<Gray, Byte> smoothedGrayFrame = smallGrayFrame.PyrUp();
            Image<Gray, Byte> cannyFrame = smoothedGrayFrame.Canny(new Gray(100), new Gray(60));
            */
        }

        private void button21_Click(object sender, EventArgs e)
        {
            //快進
            double frame_count = cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FRAME_COUNT);
            double frame_number = cap.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_POS_FRAMES);

            richTextBox1.Text += "Total = " + frame_count.ToString() + "\n";
            richTextBox1.Text += "Current = " + frame_number.ToString() + "\n";

            double new_number = frame_count / 2;

            cap.SetCaptureProperty(CAP_PROP.CV_CAP_PROP_POS_FRAMES, new_number);

            //richTextBox1.Text += "Current = " + frame_number.ToString() + "\n";



            //_capture.SetCaptureProperty(CAP_PROP.CV_CAP_PROP_POS_FRAMES, frameNumber);


        }

        private void button22_Click(object sender, EventArgs e)
        {

        }

        private void button23_Click(object sender, EventArgs e)
        {

        }

        private void button24_Click(object sender, EventArgs e)
        {

        }

        private void button25_Click(object sender, EventArgs e)
        {

        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            //richTextBox1.Text += trackBar1.Value.ToString() + " ";

        }

        private void trackBar1_MouseDown(object sender, MouseEventArgs e)
        {

        }

        private void trackBar1_MouseMove(object sender, MouseEventArgs e)
        {
            lb_frame.Text = trackBar1.Value.ToString() + " / " + total_frame_count.ToString();

        }

        private void trackBar1_MouseUp(object sender, MouseEventArgs e)
        {
            if (cap == null)
            {
                return;

            }
            //int new_position = trackBar1.Value;

            //richTextBox1.Text += new_position.ToString() + "  " + ((double)new_position / total_frame_count).ToString("p") + "  ";


            cap.SetCaptureProperty(CAP_PROP.CV_CAP_PROP_POS_FRAMES, 300);


        }
    }
}

