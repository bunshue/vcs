using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using AForge.Video;
using AForge.Video.DirectShow;

using System.Drawing.Imaging;

namespace vcs_WebCam6
{
    public partial class Form1 : Form
    {
        private FilterInfoCollection USBWebcams = null;
        public VideoCaptureDevice Cam = null;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            pictureBox2.SizeMode = PictureBoxSizeMode.Zoom;
        }

        void show_item_location()
        {
            //button
            int W = 640;
            int H = 480;
            int x_st = 10;
            int y_st = 10;
            int dx = W + 10;
            int dy = H + 10;
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1 + 70);
            lb_zoom.Location = new Point(x_st + dx * 0, y_st + dy * 1 + 140);
            bt_plus.Location = new Point(x_st + dx * 0 + 210, y_st + dy * 1);
            bt_minus.Location = new Point(x_st + dx * 0 + 210, y_st + dy * 1 + 70);
            bt_plus.BackgroundImageLayout = ImageLayout.Zoom;
            bt_minus.BackgroundImageLayout = ImageLayout.Zoom;
            bt_plus.BackgroundImage = Properties.Resources.plus;
            bt_minus.BackgroundImage = Properties.Resources.minus;

            pictureBox1.Size = new Size(W, H);
            pictureBox2.Size = new Size(W, H);
            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 1, y_st + dy * 0);

            richTextBox1.Size = new Size(W, H / 2 - 40);
            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1330, 750);
            this.Text = "vcs_WebCam6";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            //Stop_Webcam();
            if (Cam != null)
            {
                if (Cam.IsRunning)  // When Form1 closes itself, WebCam must stop, too.
                {
                    Cam.Stop();   // WebCam stops capturing images.
                    Cam.SignalToStop();
                    Cam.WaitForStop();
                }
            }
        }

        //最小化WebCam設定
        void Init_WebcamSetup()
        {
            USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice);
            if (USBWebcams.Count > 0)
            {
                Cam = new VideoCaptureDevice(USBWebcams[0].MonikerString);  //實例化對象
                Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);

                //新版AForge才支持以下功能
                //以下為WebCam訊息與調整視窗大小
                Cam.VideoResolution = Cam.VideoCapabilities[0];
                int ww = Cam.VideoCapabilities[0].FrameSize.Width;
                int hh = Cam.VideoCapabilities[0].FrameSize.Height;
                string webcam_name = USBWebcams[0].Name + " " + Cam.VideoCapabilities[0].FrameSize.Width.ToString() + " X " + Cam.VideoCapabilities[0].FrameSize.Height.ToString() + " @ " + Cam.VideoCapabilities[0].AverageFrameRate.ToString() + " Hz";
                //this.Text = webcam_name;
            }
            else
            {
                this.Text = "無影像裝置";
            }
        }

        void Start_Webcam()
        {
            if (Cam != null)
            {
                Cam.Start();   // WebCam starts capturing images.
            }
        }

        void Stop_Webcam()
        {
            if (Cam != null)
            {
                //show_main_message("停止", S_OK, 20);
                Cam.Stop();  // WebCam stops capturing images.
                Cam.SignalToStop();
                Cam.WaitForStop();
                while (Cam.IsRunning)
                {
                    Console.Write("等候相機關閉");
                }
                Cam = null;
            }
            pictureBox1.Image = null;
        }

        int cx = 0;
        int cy = 0;
        int R = 100;
        public Bitmap bm = null;
        //自定義函數, 捕獲每一幀圖像並顯示
        void Cam_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            try
            {
                pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();
                //pictureBox1.Image = bm;

                /*
                if (flag_pictureBox1_MouseHover == true)
                {
                    pictureBox2.BackColor = Color.Red;

                    RectangleF rect = new RectangleF(cx, cy, R, R);
                    pictureBox2.Image = bm.Clone(rect, PixelFormat.Format32bppArgb);
                }
                else
                {
                    pictureBox2.BackColor = Color.Green;
                }
                */

                int w = 640;
                int h = 480;

                //設定要抓取的區域
                //RectangleF rect = new RectangleF(zoom_step * zoom_cnt / 2, zoom_step * zoom_cnt * 3 / 4 / 2, w - zoom_step * zoom_cnt, h - zoom_step * zoom_cnt * 3 / 4);
                //RectangleF rect = new RectangleF(zoom_step * zoom_cnt / 2 + zoom_step * (btn_right_cnt - btn_left_cnt) / 2, zoom_step * zoom_cnt * 3 / 4 / 2, w - zoom_step * zoom_cnt, h - zoom_step * zoom_cnt * 3 / 4);
                RectangleF rect = new RectangleF(zoom_step * zoom_cnt / 2 + zoom_step * btn_right_left_cnt / 2,
                                                 (zoom_step * zoom_cnt / 2 + zoom_step * btn_down_up_cnt / 2) * 3 / 4,
                                                 w - zoom_step * zoom_cnt, h - zoom_step * zoom_cnt * 3 / 4);

                try
                {
                    bm = (Bitmap)eventArgs.Frame.Clone();
                    //bm.RotateFlip(RotateFlipType.RotateNoneFlipY);    //反轉

                    //將處理之後的圖片貼出來
                    pictureBox2.Image = bm.Clone(rect, PixelFormat.Format32bppArgb);
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "xxx錯誤訊息e12 : " + ex.Message + "\n";
                }
                GC.Collect();       //回收資源


            }
            catch (Exception ex)
            {
                //richTextBox1.Text += "xxx錯誤訊息n : " + ex.Message + "\n";
            }
            GC.Collect();       //回收資源
        }

        private void button0_Click(object sender, EventArgs e)
        {
            Init_WebcamSetup();
            Start_Webcam();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Stop_Webcam();
        }

        bool flag_pictureBox1_MouseHover = false;
        private void pictureBox1_MouseHover(object sender, EventArgs e)
        {
            flag_pictureBox1_MouseHover = true;
        }

        private void pictureBox1_MouseLeave(object sender, EventArgs e)
        {
            flag_pictureBox1_MouseHover = false;
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            cx = e.X;
            cy = e.Y;
            //this.Text = "(" + e.X.ToString() + ", " + e.Y.ToString() + ")";  // 相對於pictureBox1原點的位置
            //this.Text += "(" + MousePosition.X.ToString() + ", " + MousePosition.Y.ToString() + ")";  // 相對於視窗原點的位置
            //this.Text += "(" + Cursor.Position.X.ToString() + ", " + Cursor.Position.Y.ToString() + ")";  // 相對於視窗原點的位置
        }

        int zoom_cnt = 0;
        int zoom_cnt_max = 15;
        int zoom_step = 40;
        int usb_camera_width = 640;
        int usb_camera_height = 480;

        int btn_down_up_cnt = 0;
        int btn_right_left_cnt = 0;
        int flag_right_left_cnt = 0;
        int flag_down_up_cnt = 0;
        int flag_right_left_point_cnt = 0;
        int flag_down_up_point_cnt = 0;

        private void bt_plus_Click(object sender, EventArgs e)
        {
            if (zoom_cnt < zoom_cnt_max)
            {
                zoom_cnt++;
                //pictureBox1.Size = new Size(pictureBox1.Size.Width + zoom_step, pictureBox1.Size.Height + zoom_step * 3 / 4);
                //pictureBox1.Size = new Size(pictureBox1.Size.Width, pictureBox1.Size.Height);
                //pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;

                int w = usb_camera_width;
                int h = usb_camera_height;
                richTextBox1.Text += "zoom_cnt = " + zoom_cnt.ToString() + "\tx_st = " + (zoom_step * zoom_cnt / 2).ToString() + "\ty_st = " + (zoom_step * zoom_cnt / 2 * 3 / 4).ToString()
                    + "\tW = " + (w - zoom_step * zoom_cnt).ToString() + "\tH = " + (h - zoom_step * zoom_cnt * 3 / 4).ToString() + "\n";

                float ratio;
                ratio = 640 / (float)(w - zoom_step * zoom_cnt);
                lb_zoom.Text = ratio.ToString("#0.00") + " X";
            }
            else
            {
                richTextBox1.Text += "已達最大放大倍率\n";
            }
        }

        private void bt_minus_Click(object sender, EventArgs e)
        {
            if (zoom_cnt > 0)
            {
                int w = usb_camera_width;
                int h = usb_camera_height;
                int x_st = zoom_step * zoom_cnt / 2 + zoom_step * btn_right_left_cnt / 2;
                int y_st = (zoom_step * zoom_cnt / 2 + zoom_step * btn_down_up_cnt / 2) * 3 / 4;
                int W = w - zoom_step * zoom_cnt;
                int H = h - zoom_step * zoom_cnt * 3 / 4;
                //richTextBox1.Text += "原抓取位置 x_st = " + x_st.ToString() + " y_st = " + y_st.ToString() + " W = " + W.ToString() + " H = " + H.ToString() + "\n";

                int x_st_next = zoom_step * (zoom_cnt - 1) / 2 + zoom_step * btn_right_left_cnt / 2;
                int y_st_next = (zoom_step * (zoom_cnt - 1) / 2 + zoom_step * btn_down_up_cnt / 2) * 3 / 4;
                int W2 = w - zoom_step * (zoom_cnt - 1) + x_st_next;
                int H2 = h - zoom_step * (zoom_cnt - 1) * 3 / 4 + y_st_next;

                //richTextBox1.Text += "x_st_next = " + x_st_next.ToString() + " y_st_next = " + y_st_next.ToString() + "\n";
                if (x_st_next < 0)
                {
                    richTextBox1.Text += "已到左邊界, 不動作left, 回走, 向右一步\n";
                    btn_right_left_cnt++;
                }
                if (y_st_next < 0)
                {
                    richTextBox1.Text += "已到上邊界, 不動作up, 回走, 向下一步\n";
                    btn_down_up_cnt++;
                }
                if (W2 > 640)
                {
                    richTextBox1.Text += "已到右邊界, 不動作right, 回走, 向左一步\n";
                    btn_right_left_cnt--;
                }
                if (H2 > 480)
                {
                    richTextBox1.Text += "已到下邊界, 不動作down, 回走, 向上一步\n";
                    btn_down_up_cnt--;
                }

                {
                    zoom_cnt--;
                    x_st = zoom_step * zoom_cnt / 2 + zoom_step * btn_right_left_cnt / 2;
                    y_st = (zoom_step * zoom_cnt / 2 + zoom_step * btn_down_up_cnt / 2) * 3 / 4;
                    W = w - zoom_step * zoom_cnt;
                    H = h - zoom_step * zoom_cnt * 3 / 4;
                    //richTextBox1.Text += "後抓取位置 x_st = " + x_st.ToString() + " y_st = " + y_st.ToString() + " W = " + W.ToString() + " H = " + H.ToString() + "\n";
                }

                //pictureBox1.Size = new Size(pictureBox1.Size.Width - zoom_step, pictureBox1.Size.Height - zoom_step * 3 / 4);
                //pictureBox1.Size = new Size(pictureBox1.Size.Width, pictureBox1.Size.Height);
                //pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;

                //int w = usb_camera_width;
                //int h = usb_camera_height;

                /*
                richTextBox1.Text += "zoom_cnt = " + zoom_cnt.ToString() + "\tx_st = " + (zoom_step * zoom_cnt / 2).ToString() + "\ty_st = " + (zoom_step * zoom_cnt / 2 * 3 / 4).ToString()
                    + "\tW = " + (w - zoom_step * zoom_cnt).ToString() + "\tH = " + (h - zoom_step * zoom_cnt * 3 / 4).ToString() + "\n";
                */
                float ratio;
                ratio = 640 / (float)(w - zoom_step * zoom_cnt);
                lb_zoom.Text = ratio.ToString("#0.00") + " X";
            }
            else
            {
                richTextBox1.Text += "已達最小放大倍率\n";
            }
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個
