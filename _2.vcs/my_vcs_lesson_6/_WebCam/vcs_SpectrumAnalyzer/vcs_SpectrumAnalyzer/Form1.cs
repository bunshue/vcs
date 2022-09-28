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

namespace vcs_SpectrumAnalyzer
{
    public partial class Form1 : Form
    {
        bool flag_show_time = true;     //顯示時間
        bool flag_fullscreen = false;

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

        int spectrum_window_size_width = 640;    //AWB window size width
        int spectrum_window_size_height = 10;   //AWB window size height
        int frame_cnt = 0;        //計算fps用

        bool flag_show_data = false;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //C# 跨 Thread 存取 UI
            //Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效	same
            Control.CheckForIllegalCrossThreadCalls = false;//忽略跨執行緒錯誤

            this.pictureBox1.MouseDoubleClick += new MouseEventHandler(pictureBox1_MouseDoubleClick);
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
                        pictureBox1.Location = new Point(20, 10);

                        this.FormBorderStyle = FormBorderStyle.FixedSingle;
                        this.WindowState = FormWindowState.Normal;
                        this.ClientSize = new Size(pictureBox1.Location.X + pictureBox1.Width + 50+300+50, pictureBox1.Location.Y + pictureBox1.Height + 50+300+200);
                        this.Location = new Point(100, 10);

                        richTextBox1.Size = new Size(300, 600);
                        richTextBox1.Location = new Point(pictureBox1.Location.X+pictureBox1.Width + 50, pictureBox1.Location.Y);

                        pictureBox2.Size = new Size(ww, hh);
                        pictureBox2.Location = new Point(pictureBox1.Location.X, pictureBox1.Location.Y + pictureBox1.Height + 20);
                    }
                }
            }
            else
            {
                //button12.Enabled = true;
                //richTextBox1.Text += "無影像裝置\n";
            }
            //do_spectrum_test();
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

            /*
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
            */

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

            x_st = w / 2 - spectrum_window_size_width / 2;
            y_st = h / 2 - spectrum_window_size_height / 2;
            Pen p1 = new Pen(Color.Silver, 1);  //一般情況 中間大框框 為銀色
            gg.DrawRectangle(p1, x_st, y_st, spectrum_window_size_width, spectrum_window_size_height);   //畫中間那個大框框

            try
            {
                pictureBox1.Image = bm;
            }
            catch (Exception ex)
            {
                //richTextBox1.Text += "xxx錯誤訊息a : " + ex.Message + "\n";
            }

            frame_cnt++;
            this.Text = frame_cnt.ToString();
            if ((frame_cnt % 30) == 0)
            {
                Bitmap bmp = (Bitmap)eventArgs.Frame.Clone();

                if ((frame_cnt % 300) == 0)
                {
                    //flag_show_data = true;
                }
                drawSpectrum(bmp);
            }
            GC.Collect();       //回收資源

        }

        void drawSpectrum(Bitmap bitmap1)
        {
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

            //richTextBox1.Text += "A";
            int i;
            int j;
            int x_st = 0;
            int y_st = 0;
            x_st = w / 2 - spectrum_window_size_width / 2;
            y_st = h / 2 - spectrum_window_size_height / 2;

            int[] hue_array = new int[spectrum_window_size_width];
            float[] wavelength_array = new float[spectrum_window_size_width];
            Color[] color_array = new Color[spectrum_window_size_width];

            Color color;
            for (i = 0; i < spectrum_window_size_width; i++)
            {
                //for (j = 0; j < spectrum_window_size_height; j++)
                {
                    j = spectrum_window_size_height / 2;
                    color = bitmap1.GetPixel(x_st + i, y_st + j);

                    hue_array[i] = (int)color.GetHue();



                }


                //應該要做到每個直行要平均

            }
            //richTextBox1.Text += "\n";

            //richTextBox1.Text += "hue_array.Length = " + hue_array.Length.ToString() + "\n";

            //Graphics g = pictureBox2.CreateGraphics();
            //g.DrawRectangle(Pens.Red, 10, 10, 50, 50);

            int margin = 50;
            Pen redPen = new Pen(Color.Red, 2);
            Pen greenPen = new Pen(Color.Green, 3);
            Pen bluePen = new Pen(Color.Blue, 2);
            Pen yellowPen = new Pen(Color.Yellow, 1);
            Pen grayPen = new Pen(Color.Gray, 1);
            Point[] curvePoints1 = new Point[spectrum_window_size_width];    //一維陣列
            Point[] curvePoints2 = new Point[spectrum_window_size_width];    //一維陣列

            int W = pictureBox2.Width;
            int H = pictureBox2.Height;

            Bitmap bitmap2 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap2);

            for (i = 0; i < hue_array.Length; i++)
            {
                curvePoints1[i].X = i;
                curvePoints1[i].Y = H - (int)(hue_array[i] * 1);

                float wavelength = 0;
                do_spectrum_test0(hue_array[i], out wavelength, out color);
                //richTextBox1.Text += "hue = " + hue.ToString() + ",\t" + wavelength.ToString() + ",\t" + color.ToString() + "\n";

                wavelength = (wavelength - 300) * 6 / 5;

                wavelength_array[i] = wavelength;
                color_array[i] = color;

                curvePoints2[i].X = i;
                curvePoints2[i].Y = H - (int)(wavelength_array[i]);
            }

            //g.DrawLines(redPen, curvePoints1);   //畫直線
            g.DrawLines(grayPen, curvePoints2);   //畫直線


            for (i = 0; i < hue_array.Length; i++)
            {
                //float wavelength = 0;
                //do_spectrum_test0(hue_array[i], out wavelength, out color);

                SolidBrush b = new SolidBrush(color_array[i]);
                //g.FillRectangle(b, curvePoints2[i].X, curvePoints2[i].Y, 1, 3);

                g.FillRectangle(b, curvePoints2[i].X, curvePoints2[i].Y, 1, H - curvePoints2[i].Y);

            }



            if (flag_show_data == true)
            {
                flag_show_data = false;

                richTextBox1.Text += "hue_array.Length = " + hue_array.Length.ToString() + "\n";

                richTextBox1.Text += "hue\n";
                for (i = 0; i < hue_array.Length; i++)
                {
                    richTextBox1.Text += hue_array[i].ToString();
                    if ((i % 24) == 23)
                        richTextBox1.Text += "\n";
                    else
                        richTextBox1.Text += " ";
                }
                richTextBox1.Text += "\n";

                richTextBox1.Text += "wavelength\n";
                for (i = 0; i < hue_array.Length; i++)
                {
                    richTextBox1.Text += wavelength_array[i].ToString();
                    if ((i % 24) == 23)
                        richTextBox1.Text += "\n";
                    else
                        richTextBox1.Text += " ";
                }
                richTextBox1.Text += "\n";

                richTextBox1.Text += "color\n";
                for (i = 0; i < hue_array.Length; i++)
                {
                    richTextBox1.Text +=color_array[i].ToString();
                    if ((i % 24) == 23)
                        richTextBox1.Text += "\n";
                    else
                        richTextBox1.Text += " ";
                }
                richTextBox1.Text += "\n";




            }



            pictureBox2.Image = bitmap2;

        }

        void do_spectrum_test()
        {
            float hue = 0;
            float wavelength = 0;
            Color color = Color.Red;
            for (hue = 0; hue <= 360; hue += 10)
            {
                do_spectrum_test0(hue, out wavelength, out color);
                richTextBox1.Text += "hue = " + hue.ToString() + ",\t" + wavelength.ToString() + ",\t" + color.ToString() + "\n";


            }

        }

        /*
紫色 	380–450nm	127 0 127 	300度
藍色 	450–475nm	0 0 255		240
青色 	476–495nm	0 255 255	180
綠色 	495–570nm	0 255 0		120
黃色 	570–590nm	255 255 0	60
橙色 	590–620nm	255 128 0	30
紅色 	620–750nm	255 0 0		0
         */
        void do_spectrum_test0(float hue, out float wavelength, out Color color)
        {
            if (hue < 15)
            {
                //紅色
                color = Color.FromArgb(255, 255, 0, 0);
                wavelength = 750 - (750 - 620) * (hue - 0) / (15 - 0);
            }
            else if (hue < 45)
            {
                //橙色
                color = Color.FromArgb(255, 255, 128, 0);
                wavelength = 620 - (620 - 590) * (hue - 15) / (45 - 15);
            }
            else if (hue < 90)
            {
                //黃色
                color = Color.FromArgb(255, 255, 255, 0);
                wavelength = 590 - (590 - 570) * (hue - 45) / (90 - 45);
            }
            else if (hue < 150)
            {
                //綠色
                color = Color.FromArgb(255, 0, 255, 0);
                wavelength = 570 - (570 - 495) * (hue - 90) / (150 - 90);
            }
            else if (hue < 210)
            {
                //青色
                color = Color.FromArgb(255, 0, 255, 255);
                wavelength = 495 - (495 - 475) * (hue - 150) / (210 - 150);
            }
            else if (hue < 270)
            {
                //藍色
                color = Color.FromArgb(255, 0, 0, 255);
                wavelength = 475 - (475 - 450) * (hue - 210) / (270 - 210);
            }
            else if (hue < 360)
            {
                //紫色
                color = Color.FromArgb(255, 128, 0, 128);
                wavelength = 450 - (450 - 380) * (hue - 270) / (360 - 270);
            }
            else
            {
                richTextBox1.Text += "XXXX";
                //黑色
                color = Color.FromArgb(255, 0, 0, 0);
                wavelength = 800;
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

        private void pictureBox1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            if (flag_fullscreen == false)
            {
                flag_fullscreen = true;
                show_main_message("全螢幕", S_OK, 20);
                //groupBox1.Visible = false;
                //richTextBox1.Visible = false;
                //bt_clear.Visible = false;

                this.BackColor = Color.Black;
                //最大化螢幕
                this.FormBorderStyle = FormBorderStyle.None;
                this.WindowState = FormWindowState.Maximized;
                //this.StartPosition = FormStartPosition.CenterScreen; //居中顯示

                pictureBox1.Size = new Size(1920, 1080);
                pictureBox1.Location = new Point(0, 0);
                pictureBox1.Focus();
            }
            else
            {
                flag_fullscreen = false;
                show_main_message("復原", S_OK, 20);
                /*
                groupBox1.Visible = true;
                if (debug_mode == true)
                {
                    richTextBox1.Visible = true;
                    bt_clear.Visible = true;
                }
                */
                this.BackColor = System.Drawing.SystemColors.ControlLight;
                //最大化螢幕
                this.FormBorderStyle = FormBorderStyle.Sizable;
                this.WindowState = FormWindowState.Normal;

                int ww;
                int hh;
                ww = Cam.VideoCapabilities[0].FrameSize.Width;
                hh = Cam.VideoCapabilities[0].FrameSize.Height;
                pictureBox1.Size = new Size(ww, hh);
                pictureBox1.Location = new Point(140, 60);
                this.FormBorderStyle = FormBorderStyle.FixedSingle;
                this.WindowState = FormWindowState.Normal;
                this.ClientSize = new Size(pictureBox1.Location.X + pictureBox1.Width + 50, pictureBox1.Location.Y + pictureBox1.Height + 50);

                //this.StartPosition = FormStartPosition.CenterScreen; //居中顯示

                //pictureBox1.Size = new Size(W_pictureBox1, H_pictureBox1);
                //pictureBox1.Location = new Point(BORDER, BORDER + H_groupBox1 + BORDER);
                pictureBox1.Focus();
            }
        }

    }
}

