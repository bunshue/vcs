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

        int awb_window_size = 100;     //AWB window size width, height
        int frame_cnt = 0;        //計算fps用

        double[,] rgb_data = new double[,] {
            {380,0.1741,0.0050,0.8209,0.00145,0.0000,0.0065 },
            {385,0.1740,0.0050,0.8210,0.0022,0.0001,0.0105 },
            {390,0.1738,0.0049,0.8213,0.0042,0.0001,0.0201 },
            {395,0.1736,0.0049,0.8215,0.0076,0.0002,0.0362 },
            {400,0.1733,0.0048,0.8219,0.0143,0.0004,0.0679 },
            {405,0.1730,0.0048,0.8222,0.0232,0.0006,0.1102 },
            {410,0.1726,0.0048,0.8226,0.0435,0.0012,0.2074 },
            {415,0.1721,0.0048,0.8231,0.0776,0.0022,0.3713 },
            {420,0.1714,0.0051,0.8235,0.1344,0.0040,0.6456 },
            {425,0.1703,0.0058,0.8239,0.2148,0.0073,1.0391 },
            {430,0.1689,0.0069,0.8242,0.2839,0.0116,1.3856 },
            {435,0.1669,0.0086,0.8245,0.3285,0.0168,1.6230 },
            {440,0.1644,0.0109,0.8247,0.3483,0.0230,1.7471 },
            {445,0.1611,0.0138,0.8251,0.3481,0.0298,1.7826 },
            {450,0.1566,0.0177,0.8257,0.3362,0.0380,1.7721 },
            {455,0.1510,0.0227,0.8263,0.3187,0.0480,1.7441 },
            {460,0.1440,0.0297,0.8263,0.2908,0.0600,1.6692 },
            {465,0.1355,0.0399,0.8246,0.2511,0.0739,1.5281 },
            {470,0.1241,0.0578,0.8181,0.1954,0.0910,1.2876 },
            {475,0.1096,0.0868,0.8036,0.1421,0.1126,1.0419 },
            {480,0.0913,0.1327,0.7760,0.0956,0.1390,0.8130 },
            {485,0.0687,0.2007,0.7306,0.0580,0.1693,0.6162 },
            {490,0.0454,0.2950,0.6596,0.0320,0.2080,0.4652 },
            {495,0.0235,0.4127,0.5638,0.0147,0.2586,0.3533 },
            {500,0.0082,0.5384,0.4534,0.0049,0.3230,0.2720 },
            {505,0.0039,0.6548,0.3413,0.0024,0.4073,0.2123 },
            {510,0.0139,0.7502,0.2359,0.0093,0.5030,0.1582 },
            {515,0.0389,0.8120,0.1491,0.0291,0.6082,0.1117 },
            {520,0.0743,0.8338,0.0919,0.0633,0.7100,0.0782 },
            {525,0.1142,0.8262,0.0596,0.1096,0.7932,0.0573 },
            {530,0.1547,0.8059,0.0394,0.1655,0.8620,0.0422 },
            {535,0.1929,0.7816,0.0255,0.2257,0.9149,0.0298 },
            {540,0.2296,0.7543,0.0161,0.2904,0.9540,0.0203 },
            {545,0.2658,0.7243,0.0099,0.3597,0.9803,0.0134 },
            {550,0.3016,0.6923,0.0061,0.4334,0.9950,0.0087 },
            {555,0.3373,0.6589,0.0038,0.5121,1.0000,0.0057 },
            {560,0.3731,0.6245,0.0024,0.5945,0.9950,0.0039 },
            {565,0.4087,0.5896,0.0017,0.6784,0.9786,0.0027 },
            {570,0.4441,0.5547,0.0012,0.7621,0.9520,0.0021 },
            {575,0.4788,0.5202,0.0010,0.8425,0.9154,0.0010 },
            {580,0.5125,0.4866,0.0009,0.9163,0.8700,0.0017 },
            {585,0.5448,0.4544,0.0008,0.9786,0.8163,0.0014 },
            {590,0.5752,0.4242,0.0006,1.0263,0.7570,0.0011 },
            {595,0.6029,0.3965,0.0006,1.0567,0.6949,0.0010 },
            {600,0.6270,0.3725,0.0005,1.0522,0.6130,0.0008 },
            {605,0.6482,0.3514,0.0004,1.0456,0.5668,0.0006 },
            {610,0.6658,0.3340,0.0002,1.0026,0.5030,0.0003 },
            {615,0.6801,0.3197,0.0002,0.9384,0.4412,0.0002 },
            {620,0.6915,0.3083,0.0002,0.8544,0.3810,0.0002 },
            {625,0.7006,0.2993,0.0001,0.7514,0.3210,0.0001 },
            {630,0.7079,0.2920,0.0001,0.6424,0.2650,0.0000 },
            {635,0.7140,0.2859,0.0001,0.5419,0.2170,0.0000 },
            {640,0.7219,0.2809,0.0001,0.4479,0.1750,0.0000 },
            {645,0.7230,0.2770,0.0000,0.3608,0.1382,0.0000 },
            {650,0.7260,0.2740,0.0000,0.2835,0.1070,0.0000 },
            {655,0.7283,0.2717,0.0000,0.2187,0.0816,0.0000 },
            {660,0.7300,0.2700,0.0000,0.1649,0.0610,0.0000 },
            {665,0.7311,0.2689,0.0000,0.1212,0.0446,0.0000 },
            {670,0.7320,0.2680,0.0000,0.0874,0.0320,0.0000 },
            {675,0.7327,0.2673,0.0000,0.0636,0.0232,0.0000 },
            {680,0.7334,0.2666,0.0000,0.0468,0.0170,0.0000 },
            {685,0.7340,0.2660,0.0000,0.0329,0.0119,0.0000 },
            {690,0.7344,0.2656,0.0000,0.0227,0.0082,0.0000 },
            {695,0.7346,0.2654,0.0000,0.0158,0.0057,0.0000 },
            {700,0.7347,0.2653,0.0000,0.0114,0.0041,0.0000 },
            {705,0.7347,0.2653,0.0000,0.0081,0.0029,0.0000 },
            {710,0.7347,0.2653,0.0000,0.0058,0.0021,0.0000 },
            {715,0.7347,0.2653,0.0000,0.0041,0.0015,0.0000 },
            {720,0.7347,0.2653,0.0000,0.0029,0.0010,0.0000 },
            {725,0.7347,0.2653,0.0000,0.0020,0.0007,0.0000 },
            {730,0.7347,0.2653,0.0000,0.0014,0.0005,0.0000 },
            {735,0.7347,0.2653,0.0000,0.0010,0.0004,0.0000 },
            {740,0.7347,0.2653,0.0000,0.0007,0.0002,0.0000 },
            {745,0.7347,0.2653,0.0000,0.0005,0.0002,0.0000 },
            {750,0.7347,0.2653,0.0000,0.0003,0.0001,0.0000 },
            {755,0.7347,0.2653,0.0000,0.0002,0.0001,0.0000 },
            {760,0.7347,0.2653,0.0000,0.0002,0.0001,0.0000 },
            {765,0.7347,0.2653,0.0000,0.0001,0.0000,0.0000 },
            {770,0.7347,0.2653,0.0000,0.0001,0.0000,0.0000 },
            {775,0.7347,0.2653,0.0000,0.0001,0.0000,0.0000 },
            {780,0.7347,0.2653,0.0000,0.0000,0.0000,0.0000 }
            };

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
                        pictureBox1.Location = new Point(50, 50);
                        this.FormBorderStyle = FormBorderStyle.FixedSingle;
                        this.WindowState = FormWindowState.Normal;
                        this.ClientSize = new Size(pictureBox1.Location.X + pictureBox1.Width + 50+300+50, pictureBox1.Location.Y + pictureBox1.Height + 50+300);
                        this.Location = new Point(100, 100);

                        richTextBox1.Size = new Size(300, 600);
                        richTextBox1.Location = new Point(pictureBox1.Location.X+pictureBox1.Width + 50, pictureBox1.Location.Y);

                        pictureBox2.Size = new Size(ww, hh/2);
                        pictureBox2.Location = new Point(pictureBox1.Location.X, pictureBox1.Location.Y + pictureBox1.Height + 50);
                    }
                }
            }
            else
            {
                //button12.Enabled = true;
                //richTextBox1.Text += "無影像裝置\n";
            }
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



            x_st = w / 2 - awb_window_size / 2;
            y_st = h / 2 - awb_window_size / 2;
            Pen p1 = new Pen(Color.Silver, 1);  //一般情況 中間大框框 為銀色
            gg.DrawRectangle(p1, x_st, y_st, awb_window_size, awb_window_size);   //畫中間那個大框框 200 X 200


            try
            {
                pictureBox1.Image = bm;
            }
            catch (Exception ex)
            {
                //richTextBox1.Text += "xxx錯誤訊息a : " + ex.Message + "\n";
            }

            frame_cnt++;
            if ((frame_cnt % 60) == 0)
            {
                drawSpectrum(bm);
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
            x_st = w / 2 - awb_window_size / 2;
            y_st = h / 2 - awb_window_size / 2;

            int[] data_array = new int[81];

            int total_cnt = 0;
            Color color;
            for (j = 0; j < awb_window_size; j++)
            {
                for (i = 0; i < awb_window_size; i++)
                {
                    total_cnt++;
                    color = bitmap1.GetPixel(x_st + i, y_st + j);

                    int wave_index = RGBToWavelength(color);
                    //richTextBox1.Text += "wavelength = " + wavelength.ToString() + "\n";


                    data_array[wave_index]++;
                }
            }

            for (i = 0; i < 81; i++)
            {
                richTextBox1.Text += data_array[i].ToString() + " ";

            }
            richTextBox1.Text += "\n";

            Graphics g = pictureBox2.CreateGraphics();
            //g.DrawRectangle(Pens.Red, 10, 10, 50, 50);

            int margin = 50;
            Pen redPen = new Pen(Color.Red, 4);
            Pen greenPen = new Pen(Color.Green, 3);
            Pen bluePen = new Pen(Color.Blue, 2);
            Pen yellowPen = new Pen(Color.Yellow, 1);
            Point[] curvePoints = new Point[81];    //一維陣列內有 256 個Point

            int W = pictureBox2.Width;
            int H = pictureBox2.Height;

            //畫紅色的分布
            for (i = 0; i < 81; i++)
            {
                //curvePoints[i].X = margin + 2 * i;
                curvePoints[i].X = 3 * i;
                //curvePoints[i].Y = H - (int)(data_array[i] * 1);
                //curvePoints[i].Y = data_array[i];
                curvePoints[i].Y = 2 * i;
            }
            // Draw lines between original points to screen.
            g.DrawLines(redPen, curvePoints);   //畫直線






        }

        int RGBToWavelength(Color color)
        {
            int wavelength = 0;
            int ROW = rgb_data.GetUpperBound(0) + 1;//獲取指定維度的上限，在 上一個1就是列數
            int COL = rgb_data.GetLength(1);//獲取指定維中的元 個數，這裡也就是列數了。（1表示的是第二維，0是第一維）
            int length = rgb_data.Length;//獲取整個二維陣列的長度，即所有元 的個數
            /*
            richTextBox1.Text += "ROW = " + ROW.ToString() + "\n";
            richTextBox1.Text += "COL = " + COL.ToString() + "\n";
            richTextBox1.Text += "length = " + length.ToString() + "\n";
            */

            double r = color.R;
            double g = color.G;
            double b = color.B;

            double x = 0;
            double y = 0;
            double z = 0;

            x = (0.490 * r + 0.310 * g + 0.200 * b) / (0.667 * r + 1.132 * g + 1.200 * b);
            y = (0.117 * r + 0.812 * g + 0.010 * b) / (0.667 * r + 1.132 * g + 1.200 * b);
            z = (0.000 * r + 0.010 * g + 0.990 * b) / (0.667 * r + 1.132 * g + 1.200 * b);

            /*
            richTextBox1.Text += "x = " + x.ToString() + "\n";
            richTextBox1.Text += "y = " + y.ToString() + "\n";
            richTextBox1.Text += "z = " + z.ToString() + "\n";
            */

            double abs_min = double.MaxValue;
            double abs = 0;
            int index = 0;
            int i;
            for (i = 0; i < ROW; i++)
            {
                abs = Math.Abs(rgb_data[i, 1] - x) + Math.Abs(rgb_data[i, 2] - y) + Math.Abs(rgb_data[i, 3] - z);
                if (abs < abs_min)
                {
                    abs_min = abs;
                    index = i;
                }
            }


            wavelength = (int)rgb_data[index, 0];
            //richTextBox1.Text += "index = " + index.ToString() + "\twavelength = " + rgb_data[index, 0].ToString() + "\n";

            return index;


            //return wavelength;
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

