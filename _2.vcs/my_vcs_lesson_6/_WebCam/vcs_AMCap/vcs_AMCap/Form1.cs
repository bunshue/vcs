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

namespace vcs_AMCap
{
    public partial class Form1 : Form
    {
        bool flag_show_time = true;     //顯示時間
        bool flag_show_grid = true;     //顯示格線
        bool flag_invert = false;        //反相, SC700需要反相
        bool flag_auto_save = false;    //自動存檔

        //參考
        //【AForge.NET】C#上使用AForge.Net擷取視訊畫面
        //https://ccw1986.blogspot.com/2013/01/ccaforgenetcapture-image.html

        //AForge下載鏈結
        //http://www.aforgenet.com/framework/downloads.html

        //參考/右鍵/加入參考/瀏覽AForge.Video.dll和AForge.Video.DirectShow.dll

        public FilterInfoCollection USBWebcams = null;
        public VideoCaptureDevice Cam = null;

        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE

        int timer_display_show_main_mesg_count = 0;
        int timer_display_show_main_mesg_count_target = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            if (flag_show_time == true)
                checkBox1.Checked = true;
            else
                checkBox1.Checked = false;
            if (flag_show_grid == true)
                checkBox2.Checked = true;
            else
                checkBox2.Checked = false;
            if (flag_invert == true)
                checkBox3.Checked = true;
            else
                checkBox3.Checked = false;
            if (flag_auto_save == true)
            {
                checkBox4.Checked = true;
                timer_auto_save.Enabled = true;
                numericUpDown_time.Visible = true;
            }
            else
            {
                checkBox4.Checked = false;
                timer_auto_save.Enabled = false;
                numericUpDown_time.Visible = false;
            }

            lb_main_mesg.Text = "";

            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            this.pictureBox1.Focus();

            //richTextBox1.Text += "重新抓取USB影像\t";
            USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice);
            if (USBWebcams.Count > 0)  // The quantity of WebCam must be more than 0.
            {
                //button12.Enabled = false;
                Cam = new VideoCaptureDevice(USBWebcams[0].MonikerString);  //實例化對象
                Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);
                Cam.Start();   // WebCam starts capturing images.
                //richTextBox1.Text += "有影像裝置\n";

                //lb_main_mesg.Text += 

                Cam.VideoResolution = Cam.VideoCapabilities[0];

                string webcam_name = string.Empty;

                int ww;
                int hh;
                ww = Cam.VideoCapabilities[0].FrameSize.Width;
                hh = Cam.VideoCapabilities[0].FrameSize.Height;

                webcam_name = USBWebcams[0].Name + " " + Cam.VideoCapabilities[0].FrameSize.Width.ToString() + " X " + Cam.VideoCapabilities[0].FrameSize.Height.ToString() + " @ " + Cam.VideoCapabilities[0].AverageFrameRate.ToString() + " Hz";
                this.Text = webcam_name;

                if (Screen.PrimaryScreen.Bounds.Width == 1920)
                {
                    if (ww >= Screen.PrimaryScreen.Bounds.Width)
                    {
                        pictureBox1.Size = new Size(1920, 1080);
                        pictureBox1.Location = new Point(0, 0);
                        this.FormBorderStyle = FormBorderStyle.None;
                        this.WindowState = FormWindowState.Maximized;
                        //this.Size = new Size(pictureBox1.Size.Width + 200, pictureBox1.Size.Height + 200);
                        show_main_message(webcam_name, S_OK, 30);
                    }
                    else if (ww < Screen.PrimaryScreen.Bounds.Width)
                    {
                        pictureBox1.Size = new Size(ww, hh);
                        pictureBox1.Location = new Point(140, 60);
                        this.FormBorderStyle = FormBorderStyle.FixedSingle;
                        this.WindowState = FormWindowState.Normal;
                        this.ClientSize = new Size(pictureBox1.Location.X + pictureBox1.Width + 50, pictureBox1.Location.Y + pictureBox1.Height + 50);
                    }
                }
            }
            else
            {
                //button12.Enabled = true;
                //richTextBox1.Text += "無影像裝置\n";
            }
        }

        //寫字的功能, 畫框的功能
        Graphics gg;
        SolidBrush drawBrush;
        Font drawFont1;
        //Font drawFont2;
        Font drawFont3;
        string drawDate;

        public Bitmap bm = null;
        //自定義函數, 捕獲每一幀圖像並顯示
        void Cam_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            try
            {
                //pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();
                bm = (Bitmap)eventArgs.Frame.Clone();
                //pictureBox1.Image = bm;
            }
            catch (Exception ex)
            {
                //richTextBox1.Text += "xxx錯誤訊息n : " + ex.Message + "\n";
            }

            if (flag_invert == true)
                bm.RotateFlip(RotateFlipType.RotateNoneFlipY);

            gg = Graphics.FromImage(bm);

            int w;
            int h;
            try
            {
                w = bm.Width;
                h = bm.Height;
            }
            catch (Exception ex)
            {
                //richTextBox1.Text += "xxx錯誤訊息m : " + ex.Message + "\n";
                GC.Collect();       //回收資源
                return;
            }

            if (flag_show_grid == true)
            {   //顯示格線
                int i;
                int j;

                j = 0;
                if (rb_3X3.Checked == true)
                {
                    j = 3;
                }
                else if (rb_4X4.Checked == true)
                {
                    j = 4;
                }
                else if (rb_5X5.Checked == true)
                {
                    j = 5;
                }
                else
                {
                    j = 4;
                }

                if (j >= 2)
                {
                    for (i = 1; i <= (j - 1); i++)
                    {
                        gg.DrawLine(new Pen(Color.Silver, 1), w * i / j, 0, w * i / j, h);
                        gg.DrawLine(new Pen(Color.Silver, 1), 0, h * i / j, w, h * i / j);
                    }
                }


            }

            int x_st = 0;
            int y_st = 0;


            if (flag_show_time == true)
            {   //顯示時間
                drawDate = DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss");
                drawBrush = new SolidBrush(Color.Yellow);
                drawFont1 = new Font("Arial", 6, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);
                //drawFont2 = new Font("Arial", 4, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);
                drawFont3 = new Font("Arial", 3, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);
                x_st = 10;
                y_st = 10;
                gg.DrawString(drawDate, drawFont1, drawBrush, x_st, y_st);
            }


            try
            {
                pictureBox1.Image = bm;
            }
            catch (Exception ex)
            {
                //richTextBox1.Text += "xxx錯誤訊息a : " + ex.Message + "\n";
            }

            GC.Collect();       //回收資源

        }

        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
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

        void show_main_message(string mesg, int number, int timeout)
        {
            lb_main_mesg.Text = mesg;
            //playSound(number);

            timer_display_show_main_mesg_count = 0;
            timer_display_show_main_mesg_count_target = timeout;   //timeout in 0.1 sec
            timer_display.Enabled = true;
        }

        private void timer_display_Tick(object sender, EventArgs e)
        {
            if (timer_display_show_main_mesg_count < timer_display_show_main_mesg_count_target)      //display main message timeout
            {
                timer_display_show_main_mesg_count++;
                if (timer_display_show_main_mesg_count >= timer_display_show_main_mesg_count_target)
                {
                    lb_main_mesg.Text = "";
                }
            }

        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox1.Checked == true)
                flag_show_time = true;
            else
                flag_show_time = false;
        }

        private void checkBox2_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox2.Checked == true)
            {
                flag_show_grid = true;
                rb_3X3.Visible = true;
                rb_4X4.Visible = true;
                rb_5X5.Visible = true;
            }
            else
            {
                flag_show_grid = false;
                rb_3X3.Visible = false;
                rb_4X4.Visible = false;
                rb_5X5.Visible = false;
            }
        }

        private void checkBox3_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox3.Checked == true)
                flag_invert = true;
            else
                flag_invert = false;
        }

        private void checkBox4_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox4.Checked == true)
            {
                flag_auto_save = true;
                timer_auto_save.Enabled = true;
                numericUpDown_time.Visible = true;
            }
            else
            {
                flag_auto_save = false;
                timer_auto_save.Enabled = false;
                numericUpDown_time.Visible = false;
            }
        }

        private void timer_auto_save_Tick(object sender, EventArgs e)
        {
            save_image_file();
        }

        private void timer_focus_Tick(object sender, EventArgs e)
        {
            this.pictureBox1.Focus();
        }

        void save_image_file()
        {
            this.pictureBox1.Focus();
            //show_main_message("存檔中...", S_OK, 10);
            //delay(10);

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
                    string drawDate = DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss");

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

                try
                {
                    //bitmap1.Save(@file1, ImageFormat.Jpeg);
                    bitmap1.Save(filename2, ImageFormat.Bmp);
                    //bitmap1.Save(@file3, ImageFormat.Png);

                    //richTextBox1.Text += "存檔成功\n";
                    //richTextBox1.Text += "已存檔 : " + file1 + "\n";
                    //richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                    //richTextBox1.Text += "已存檔 : " + file3 + "\n";
                    show_main_message("已存檔 BMP", S_OK, 10);
                }
                catch (Exception ex)
                {
                    //richTextBox1.Text += "xxx錯誤訊息b : " + ex.Message + "\n";
                    //show_main_message1("存檔失敗", S_OK, 30);
                    //show_main_message2("存檔失敗 : " + ex.Message, S_OK, 30);
                }

            }
            else
            {
                //richTextBox1.Text += "無圖可存\n";
                //show_main_message("無圖可存", S_FALSE, 30);
            }
            return;
        }

        private void numericUpDown_time_ValueChanged(object sender, EventArgs e)
        {
            timer_auto_save.Interval = (int)numericUpDown_time.Value * 1000;
        }
    }
}

