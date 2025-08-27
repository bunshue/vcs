using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat
using System.Drawing.Drawing2D; //for DashStyle
using System.Diagnostics;       //for StopWatch
using System.Runtime.InteropServices;   //for dll

using AForge.Video;             //需要添加這兩個.dll, 參考/加入參考/瀏覽此二檔
using AForge.Video.DirectShow;

//使用Aforge的VideoSourcePlayer, 在要再多添加4個.dll

/*
Aforge.Net 安裝路徑設定
Solution Explorer(方案總管) => References(參考)(右鍵) => Add Reference(加入參考) => AForge.Net的Release資料夾
加入AForge.Video.dll、AForge.Video.DirectShow.dll
*/

namespace vcs_ColorHistogram
{
    public partial class Form1 : Form
    {
        bool flag_webcam_mode = false;

        //參考
        //【AForge.NET】C#上使用AForge.Net擷取視訊畫面
        //https://ccw1986.blogspot.com/2013/01/ccaforgenetcapture-image.html

        //AForge下載鏈結
        //http://www.aforgenet.com/framework/downloads.html

        public FilterInfoCollection USBWebcams = null;
        public VideoCaptureDevice Cam = null;

        Stopwatch stopwatch;

        private const int BORDER = 0;

        //string filename = @"D:\_git\vcs\_1.data\______test_files1\ims_image_20230921_155302.bmp";
        string filename = @"D:\_git\vcs\_1.data\______test_files1\ims01.bmp";
        //string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
        //string filename = "pic_original2.bmp";

        public Point firstPoint = new Point(0, 0);  //鼠標第一點 
        public Point secondPoint = new Point(0, 0);  //鼠標第二點 
        public bool begin = false;   //是否開始畫矩形 
        Graphics g1;

        private int W = 0;  //原圖的寬
        private int H = 0;  //原圖的高
        private int w = 0;  //擷取圖的寬
        private int h = 0;  //擷取圖的高

        int x_st = 0;
        int y_st = 0;
        int x_sp = 0;
        int y_sp = 0;

        Image image;
        int[] yuv_data_y = new int[256];
        int[] yuv_data_u = new int[256];
        int[] yuv_data_v = new int[256];
        int[] rgb_data_r = new int[256];
        int[] rgb_data_g = new int[256];
        int[] rgb_data_b = new int[256];

        int max = 255;
        int min = 0;
        int brightness = 128;
        int brightness_old = 128;
        int contrast = 128;
        int contrast_old = 128;

        bool flag_no_update_crop_picture = false;

        private Bitmap bitmap0 = null;  //原圖
        private Bitmap bitmap1 = null;  //處理後的圖 或 處理結果

        //private int W = 0;  //原圖的寬
        //private int H = 0;  //原圖的高
        //private int w = 0;  //擷取圖的寬
        //private int h = 0;  //擷取圖的高
        //int x_st = 0;   //擷取開始x
        //int y_st = 0;   //擷取開始y

        //量測範圍
        int measure_x_st = 50;
        int measure_y_st = 50;
        int measure_w = 640 - 100;
        int measure_h = 480 - 100;

        private int brightness_max = 0;
        private int brightness_min = 0;
        private int brightness_avg = 0;
        private double brightness_sd = 0;
        private float brightness_ratio = 0;
        private int brightness_max_mod = 0;
        private int brightness_min_mod = 0;
        private float brightness_ratio_mod = 0;

        //int[] yuv_data_y = new int[256];

        public struct RGB
        {
            private byte _r;
            private byte _g;
            private byte _b;

            public RGB(byte r, byte g, byte b)
            {
                this._r = r;
                this._g = g;
                this._b = b;
            }

            public byte R
            {
                get { return this._r; }
                set { this._r = value; }
            }

            public byte G
            {
                get { return this._g; }
                set { this._g = value; }
            }

            public byte B
            {
                get { return this._b; }
                set { this._b = value; }
            }

            public bool Equals(RGB rgb)
            {
                return (this.R == rgb.R) && (this.G == rgb.G) && (this.B == rgb.B);
            }
        }

        public struct YUV
        {
            private double _y;
            private double _u;
            private double _v;

            public YUV(double y, double u, double v)
            {
                this._y = y;
                this._u = u;
                this._v = v;
            }

            public double Y
            {
                get { return this._y; }
                set { this._y = value; }
            }

            public double U
            {
                get { return this._u; }
                set { this._u = value; }
            }

            public double V
            {
                get { return this._v; }
                set { this._v = value; }
            }

            public bool Equals(YUV yuv)
            {
                return (this.Y == yuv.Y) && (this.U == yuv.U) && (this.V == yuv.V);
            }
        }

        public static YUV RGBToYUV(RGB rgb)
        {
            double y = rgb.R * .299000 + rgb.G * .587000 + rgb.B * .114000;
            double u = rgb.R * -.168736 + rgb.G * -.331264 + rgb.B * .500000 + 128;
            double v = rgb.R * .500000 + rgb.G * -.418688 + rgb.B * -.081312 + 128;

            return new YUV(y, u, v);
        }

        public static RGB YUVToRGB(YUV yuv)
        {
            double r = yuv.Y + 1.4075 * (yuv.V - 128);
            double g = yuv.Y - 0.3455 * (yuv.U - 128) - (0.7169 * (yuv.V - 128));
            double b = yuv.Y + 1.7790 * (yuv.U - 128);
            if (r > 255)
                r = 255;
            if (g > 255)
                g = 255;
            if (b > 255)
                b = 255;
            if (r < 0)
                r = 0;
            if (g < 0)
                g = 0;
            if (b < 0)
                b = 0;

            return new RGB((byte)r, (byte)g, (byte)b);
        }

        void get_brigheness_data(Bitmap bmp, int x_st, int y_st, int w, int h)
        {
            richTextBox1.Text += "x_st = " + x_st.ToString() + "\ty_st = " + y_st.ToString() + "\tw = " + w.ToString() + "\th = " + h.ToString() + "\n";
            yuv_data_y = new int[256];

            int i;
            int j;
            Color pt;
            int total_points = 0;
            double total_brightness = 0;

            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {
                    pt = bmp.GetPixel(x_st + i, y_st + j);

                    RGB pp = new RGB(pt.R, pt.G, pt.B);
                    YUV yyy = new YUV();
                    yyy = RGBToYUV(pp);

                    total_brightness += yyy.Y;

                    int y = (int)Math.Round(yyy.Y); //四捨五入

                    if (y > 255)
                        y = 255;
                    if (y < 0)
                        y = 0;

                    yuv_data_y[y]++;
                    total_points++;

                    /*
                    if (j == 10)
                    {
                        richTextBox1.Text += y.ToString() + " ";
                        if ((i % 16) == 15)
                        {
                            richTextBox1.Text += "\n";
                        }
                    }
                    */
                }
                //richTextBox1.Text += "\n";
            }
            //richTextBox1.Text += "\n";
            richTextBox1.Text += "共有 " + total_points.ToString() + " 個點\n";
            richTextBox1.Text += "總亮度 " + total_brightness.ToString() + "\n";
            richTextBox1.Text += "平均亮度 " + (total_brightness / total_points).ToString() + "\n";
        }

        void measure_brightness(Bitmap bmp)
        {
            //量測範圍
            x_st = SelectionRectangle.X;
            y_st = SelectionRectangle.Y;
            w = SelectionRectangle.Width;
            h = SelectionRectangle.Height;

            //量測原圖 bmp
            get_brigheness_data(bmp, x_st, y_st, w, h);

            int i;
            int most = 0;
            int brightness_st = 0;
            int brightness_sp = 0;
            int total_points = 0;
            double total_brightness = 0;
            for (i = 0; i < 256; i++)
            {
                total_points += yuv_data_y[i];
                total_brightness += i * yuv_data_y[i];
                //richTextBox1.Text += yuv_data_y[i].ToString() + " ";
                if (yuv_data_y[i] > most)
                    most = yuv_data_y[i];
                /*
                if (yuv_data_y[i] == 0)
                    yuv_data_y[i] = 5;
                */
                if ((yuv_data_y[i] > 0) && (brightness_st == 0))
                {
                    brightness_st = i;
                }
                if (yuv_data_y[i] > 0)
                {
                    brightness_sp = i;
                }
            }

            richTextBox1.Text += "\n最多 " + most.ToString() + "\n";
            richTextBox1.Text += "亮度範圍 : " + brightness_st.ToString() + " 到 " + brightness_sp.ToString() + "\n";
            richTextBox1.Text += "亮差 : " + (brightness_sp - brightness_st).ToString() + "\n";

            richTextBox1.Text += "共有 " + total_points.ToString() + " 個點\n";
            richTextBox1.Text += "總亮度 " + total_brightness.ToString() + "\n";
            richTextBox1.Text += "平均亮度 " + (total_brightness / total_points).ToString() + "\n";

            //一維陣列用法：
            double[] sd_num = new double[total_points];

            int index = 0;
            int j = 0;
            Color pt;

            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {
                    pt = bmp.GetPixel(x_st + i, y_st + j);

                    RGB pp = new RGB(pt.R, pt.G, pt.B);
                    YUV yyy = new YUV();
                    yyy = RGBToYUV(pp);

                    sd_num[index] = yyy.Y;
                    index++;
                }
            }

            double sd = SD(sd_num);
            //richTextBox1.Text += "標準差 " + sd.ToString("F2") + "\n";
            brightness_sd = sd;

            int average_brightness = (int)Math.Round(total_brightness / total_points); //四捨五入
            //richTextBox1.Text += "平均亮度 " + average_brightness.ToString() + "\n";
            brightness_avg = average_brightness;

            int ww = 480 * 2 - 10;
            int hh1 = 300;
            int hh2 = 256;
            Bitmap bmp4 = new Bitmap(ww, hh1 * 2 + 100);
            Graphics g4 = Graphics.FromImage(bmp4);
            g4.Clear(Color.Pink);
            Pen p = new Pen(Color.Blue, 2);

            double ratio = 0;
            ratio = (double)hh2 / most;
            richTextBox1.Text += "ratio = " + ratio.ToString() + "\n";

            for (i = 0; i < 256; i++)
            {
                g4.FillRectangle(Brushes.Red, i * 2, hh2 - (float)(yuv_data_y[i] * ratio), 2, (float)(yuv_data_y[i] * ratio));
            }

            g4.DrawRectangle(p, 0 + 1, 0 + 1, ww - 2, hh1 - 2);
            g4.DrawRectangle(p, 0 + 1, 0 + 1, ww - 2, hh2 - 2);

            p = new Pen(Color.Yellow, 3);
            g4.DrawLine(p, average_brightness * 2, 0, average_brightness * 2, hh2 - 2);
            g4.DrawLine(p, brightness_st * 2, 0, brightness_st * 2, hh2 - 2);
            g4.DrawLine(p, brightness_sp * 2, 0, brightness_sp * 2, hh2 - 2);

            Brush b = new SolidBrush(Color.FromArgb(33, Color.RoyalBlue.R, Color.RoyalBlue.G, Color.RoyalBlue.B));

            g4.FillRectangle(b, min * 2, 0, (max - min) * 2, hh1);

            Font f = new Font("標楷體", 20);

            if ((min >= 0) && (min <= 103))
            {
                g4.DrawString(min.ToString(), f, new SolidBrush(Color.Blue), new PointF(min * 2, hh2));
            }
            else if (min < 0)
            {
                g4.DrawString(min.ToString(), f, new SolidBrush(Color.Blue), new PointF(0, hh2));
            }
            else
            {
                g4.DrawString(min.ToString(), f, new SolidBrush(Color.Blue), new PointF(103 * 2, hh2));
            }

            if ((max <= 255) && (max >= 152))
            {
                g4.DrawString(max.ToString(), f, new SolidBrush(Color.Blue), new PointF(max * 2 - 50, hh2));

                g4.DrawString(brightness_st.ToString(), f, new SolidBrush(Color.Yellow), new PointF(brightness_st * 2 - 25, hh2));
                g4.DrawString(brightness_sp.ToString(), f, new SolidBrush(Color.Yellow), new PointF(brightness_sp * 2 - 25, hh2));
                g4.DrawString(average_brightness.ToString(), f, new SolidBrush(Color.Yellow), new PointF(average_brightness * 2 - 25, hh2));
            }
            else if (max > 255)
            {
                g4.DrawString(max.ToString(), f, new SolidBrush(Color.Blue), new PointF(512 - 50, hh2));
            }
            else
            {
                g4.DrawString(max.ToString(), f, new SolidBrush(Color.Blue), new PointF(152 * 2 - 50, hh2));
            }

            int y_min = 0;
            int y_max = 0;
            FindYMaxYMin(yuv_data_y, out y_min, out y_max);
            //richTextBox1.Text += "M = " + y_max.ToString() + "\t" + "m = " + y_min.ToString() + "\n";

            int dy = 22;
            g4.DrawString("Max = " + y_max.ToString(), new Font("標楷體", 18), new SolidBrush(Color.Navy), 512, 10 + dy * 0);
            g4.DrawString("min = " + y_min.ToString(), new Font("標楷體", 18), new SolidBrush(Color.Navy), 512, 10 + dy * 1);
            g4.DrawString("most = " + most.ToString(), new Font("標楷體", 18), new SolidBrush(Color.Navy), 512, 10 + dy * 2);
            g4.DrawString("最亮 : " + brightness_sp.ToString(), new Font("標楷體", 18), new SolidBrush(Color.Navy), 512, 10 + dy * 3);
            g4.DrawString("最暗 : " + brightness_st.ToString(), new Font("標楷體", 18), new SolidBrush(Color.Navy), 512, 10 + dy * 4);
            g4.DrawString("亮差 : " + (brightness_sp - brightness_st).ToString(), new Font("標楷體", 18), new SolidBrush(Color.Navy), 512, 10 + dy * 5);
            g4.DrawString("平均 : " + average_brightness.ToString(), new Font("標楷體", 18), new SolidBrush(Color.Navy), 512, 10 + dy * 6);
            g4.DrawString("SD : " + sd.ToString("F2"), new Font("標楷體", 18), new SolidBrush(Color.Navy), 512, 10 + dy * 7);

            float rr_sp = 2.0f;
            //bool flag_modify_boundary_sp = true;
            if ((brightness_sp - average_brightness) < sd * rr_sp)
            {
                g4.DrawString("YMax太近", new Font("標楷體", 18), new SolidBrush(Color.Navy), 512, 10 + dy * 8);
                //flag_modify_boundary_sp = false;
            }

            float rr_st = 3.0f;
            //bool flag_modify_boundary_st = true;
            if ((average_brightness - brightness_st) < sd * rr_st)
            {
                g4.DrawString("YMin太近", new Font("標楷體", 18), new SolidBrush(Color.Navy), 512 + 100, 10 + dy * 8);
                //flag_modify_boundary_st = false;
            }

            g4.DrawString(((int)Math.Round((average_brightness - sd * rr_st))).ToString() + " " +
                average_brightness.ToString() + " " +
                ((int)Math.Round((average_brightness + sd * rr_sp))).ToString(), new Font("標楷體", 18), new SolidBrush(Color.Navy), 512, 10 + dy * 9);

            /*
            if ((flag_modify_boundary_sp == false) || (cb_modify.Checked == false))
            {
                g4.DrawString("亮場未調整", new Font("標楷體", 13), new SolidBrush(Color.Red), 512 + 105, 10 + dy * 10);
            }

            if ((flag_modify_boundary_st == false) || (cb_modify.Checked == false))
            {
                g4.DrawString("暗場未調整", new Font("標楷體", 13), new SolidBrush(Color.Red), 512, 10 + dy * 10);
            }
            */

            int boundary_st = (int)Math.Round(average_brightness - sd * rr_st);
            int boundary_sp = (int)Math.Round(average_brightness + sd * rr_sp);

            b = new SolidBrush(Color.FromArgb(30, Color.Lime.R, Color.Lime.G, Color.Lime.B));
            g4.FillRectangle(b, boundary_st * 2, 0 + 0, (boundary_sp - boundary_st) * 2, hh2 - 0 - 0);
            g4.DrawRectangle(Pens.Lime, boundary_st * 2, 0 + 0, (boundary_sp - boundary_st) * 2, hh2 - 0 - 0);
            //g4.DrawLine(Pens.Lime, boundary_st * 2, 0, boundary_st * 2, hh2);
            //g4.DrawLine(Pens.Lime, boundary_sp * 2, 0, boundary_sp * 2, hh2);

            int width = 40;
            b = new SolidBrush(Color.FromArgb(30, Color.Lime.R, Color.Lime.G, Color.Lime.B));
            g4.FillRectangle(b, 750, 0, width, 256);
            g4.FillRectangle(b, 800, 0, width, 256);
            g4.FillRectangle(b, 850, 0, width, 256);

            g4.DrawRectangle(Pens.Red, 750, hh2 - brightness_sp, width, brightness_sp - brightness_st);

            //richTextBox1.Text += "brightness data :\n";
            //printArrayData(yuv_data_y);
            int mm = yuv_data_y.Max();
            //richTextBox1.Text += "mm = " + mm.ToString() + "\n";
            float rr = mm / (float)width;
            for (i = 0; i < 256; i++)
            {
                g4.DrawLine(Pens.Red, 750, hh2 - i, 750 + (int)(yuv_data_y[i] / rr), hh2 - i);
            }

            Point[] curvePoints = new Point[256];    //一維陣列內有 256 個Point
            for (i = 0; i < 256; i++)
            {
                curvePoints[i].X = 750 + (int)(yuv_data_y[i] / rr);
                curvePoints[i].Y = hh2 - i;
            }
            // Draw lines between original points to screen.
            g4.DrawLines(Pens.Yellow, curvePoints);   //畫直線
            // Draw curve to screen.
            //g4.DrawCurve(Pens.Yellow, curvePoints); //畫曲線

            //再把標準差範圍畫出來

            richTextBox1.Text += "brightness_st = " + brightness_st.ToString() + "\n";
            richTextBox1.Text += "brightness_sp = " + brightness_sp.ToString() + "\n";
            richTextBox1.Text += "brightness_min = " + brightness_min.ToString() + "\n";
            richTextBox1.Text += "brightness_max = " + brightness_max.ToString() + "\n";
            richTextBox1.Text += "brightness_avg = " + brightness_avg.ToString() + "\n";
            richTextBox1.Text += "brightness_sd = " + brightness_sd.ToString() + "\n";
            richTextBox1.Text += "brightness_ratio = " + brightness_ratio.ToString("F2") + "\n";

            richTextBox1.Text += "brightness_min_mod = " + brightness_min_mod.ToString() + "\n";
            richTextBox1.Text += "brightness_max_mod = " + brightness_max_mod.ToString() + "\n";
            richTextBox1.Text += "brightness_ratio_mod = " + brightness_ratio_mod.ToString("F2") + "\n";

            g4.DrawRectangle(Pens.Red, 800, hh2 - brightness_max_mod, width, brightness_max_mod - brightness_min_mod);
            g4.DrawLine(Pens.Red, 800, hh2 - brightness_avg, 800 + width, hh2 - brightness_avg);

            pictureBox1.Image = bmp4;
        }

        void FindYMaxYMin(int[] array, out int y_min, out int y_max)
        {
            int i;
            int len = array.Length;
            y_min = int.MaxValue;
            y_max = int.MinValue;
            for (i = 0; i < len; i++)
            {
                if (y_min > array[i])
                {
                    y_min = array[i];
                }
                if (y_max < array[i])
                {
                    y_max = array[i];
                }
            }
        }

        /// <summary> 
        /// 標準差(StandardDifference) 
        /// </summary> 
        /// <param name="val"></param> 
        /// <returns></returns> 
        public double SD(double[] a)
        {
            int len;
            double avg;
            double sd;
            int i;

            len = a.Length;
            avg = a.Average();
            if (len <= 1)
            {
                sd = 0;
                richTextBox1.Text += "SD = " + sd.ToString() + "\n";
                return sd;
            }

            richTextBox1.Text += "len = " + len.ToString() + "\n";
            richTextBox1.Text += "average = " + avg.ToString() + "\n";
            sd = 0;
            for (i = 0; i < len; i++)
            {
                sd += Math.Pow((a[i] - avg), 2);
            }
            sd /= (len - 1);
            sd = Math.Sqrt(sd);

            return sd;
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            filename = @"D:\_git\vcs\_1.data\______test_files1\ims01.bmp"; //stomach
            tb_filename.Text = filename;

            show_item_location();

            bitmap0 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            pictureBox0.Image = bitmap0;

            W = bitmap0.Width;
            H = bitmap0.Height;

            nud_x_st.ValueChanged += new EventHandler(select_crop_area);
            nud_y_st.ValueChanged += new EventHandler(select_crop_area);
            nud_w.ValueChanged += new EventHandler(select_crop_area);
            nud_h.ValueChanged += new EventHandler(select_crop_area);

            rb_selection1.CheckedChanged += new EventHandler(rb_selection_CheckedChanged);
            rb_selection2.CheckedChanged += new EventHandler(rb_selection_CheckedChanged);
            rb_selection3.CheckedChanged += new EventHandler(rb_selection_CheckedChanged);

            //量測範圍
            measure_x_st = 50;
            measure_y_st = 50;
            measure_w = W - 50 * 2;
            measure_h = H - 50 * 2;
            nud_x_st.Value = measure_x_st;
            nud_y_st.Value = measure_y_st;
            nud_w.Value = measure_w;
            nud_h.Value = measure_h;

            if (flag_webcam_mode == true)
            {
                USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice);
                if (USBWebcams.Count > 0)  // The quantity of WebCam must be more than 0.
                {
                    Cam = new VideoCaptureDevice(USBWebcams[0].MonikerString);  //實例化對象

                    Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);
                    Cam.Start();   // WebCam starts capturing images.

                    //以下為WebCam訊息與調整視窗大小
                    Cam.VideoResolution = Cam.VideoCapabilities[0];
                    string webcam_name = string.Empty;
                    int ww;
                    int hh;
                    ww = Cam.VideoCapabilities[0].FrameSize.Width;
                    hh = Cam.VideoCapabilities[0].FrameSize.Height;
                    webcam_name = USBWebcams[0].Name + " " + Cam.VideoCapabilities[0].FrameSize.Width.ToString() + " X " + Cam.VideoCapabilities[0].FrameSize.Height.ToString() + " @ " + Cam.VideoCapabilities[0].AverageFrameRate.ToString() + " Hz";
                    this.Text = webcam_name;

                    //有抓到WebCam, 重新設定pictureBox和vsp的大小和位置
                    pictureBox0.Size = new Size(ww, hh);
                    pictureBox0.Location = new Point(BORDER, BORDER);

                    stopwatch = new Stopwatch();
                    stopwatch.Start();

                    timer1.Enabled = true;
                }
                else
                {
                    this.Text = "無影像裝置";
                }
            }
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
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

        public Bitmap bm = null;
        //自定義函數, 捕獲每一幀圖像並顯示
        Graphics g;

        void Cam_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            try
            {
                //pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();
                bm = (Bitmap)eventArgs.Frame.Clone();
                //bm.RotateFlip(RotateFlipType.RotateNoneFlipX);
                //pictureBox1.Image = bm;
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息e06 : " + ex.Message + "\n";
                GC.Collect();       //回收資源
                return;
            }

            try
            {
                bm = draw_selectionArea(bm, SelectionRectangle);    //畫紅框
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息e07 : " + ex.Message + "\n";
                GC.Collect();       //回收資源
                return;
            }

            pictureBox0.Image = bm;

            GC.Collect();       //回收資源
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
                }
                Cam = null;
            }
        }

        private Rectangle SelectionRectangle = new Rectangle(new Point(0, 0), new Size(0, 0));    //用來保存截圖的矩形

        // Return a Rectangle with these points as corners.
        private Rectangle MakeRectangle(int x0, int y0, int x1, int y1)
        {
            return new Rectangle(Math.Min(x0, x1), Math.Min(y0, y1), Math.Abs(x0 - x1), Math.Abs(y0 - y1));
        }

        private Rectangle MakeRectangle(Point pt1, Point pt2)
        {
            return new Rectangle(Math.Min(pt1.X, pt2.X), Math.Min(pt1.Y, pt2.Y), Math.Abs(pt1.X - pt2.X), Math.Abs(pt1.Y - pt2.Y));
        }

        private void select_crop_area(object sender, EventArgs e)
        {
            int x_st = (int)nud_x_st.Value;
            int y_st = (int)nud_y_st.Value;
            int w = (int)nud_w.Value;
            int h = (int)nud_h.Value;

            /*
            measure_x_st = x_st;
            measure_y_st = y_st;
            measure_w = w;
            measure_h = h;
            */

            SelectionRectangle = MakeRectangle(x_st, y_st, x_st + w, y_st + h);

            if ((SelectionRectangle.X < 0) || (SelectionRectangle.X >= W))
                return;
            if ((SelectionRectangle.Y < 0) || (SelectionRectangle.Y >= H))
                return;
            if ((SelectionRectangle.Width <= 0) || (SelectionRectangle.Width > W))
                return;
            if ((SelectionRectangle.Height <= 0) || (SelectionRectangle.Height > H))
                return;
            if (((SelectionRectangle.X + SelectionRectangle.Width) > W) || ((SelectionRectangle.Y + SelectionRectangle.Height) > H))
                return;

            if (flag_webcam_mode == false)
            {
                draw_selectionBox();
            }
        }

        private void rb_selection_CheckedChanged(object sender, EventArgs e)
        {
            //量測範圍

            if (rb_selection1.Checked == true)
            {
                richTextBox1.Text += "大\n";
                measure_x_st = 50;
                measure_y_st = 50;
                measure_w = W - measure_x_st * 2;
                measure_h = H - measure_y_st * 2;
            }
            else if (rb_selection2.Checked == true)
            {
                richTextBox1.Text += "中\n";
                measure_w = 180;
                measure_h = 180;
                measure_x_st = (int)((W - measure_w) / 2);
                measure_y_st = (int)((H - measure_h) / 2);
            }
            else if (rb_selection3.Checked == true)
            {
                richTextBox1.Text += "小\n";
                measure_w = 100;
                measure_h = 100;
                measure_x_st = (int)((W - measure_w) / 2);
                measure_y_st = (int)((H - measure_h) / 2);
            }
            else
            {
                richTextBox1.Text += "XXXXXXXXXXXXXXXXXXXXXXX\n";

            }
            nud_x_st.Value = measure_x_st;
            nud_y_st.Value = measure_y_st;
            nud_w.Value = measure_w;
            nud_h.Value = measure_h;
        }

        void draw_selectionBox()
        {
            //畫紅框 需要重新讀取圖片
            filename = tb_filename.Text;
            bitmap0 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式

            //畫紅框
            bitmap0 = draw_selectionArea(bitmap0, SelectionRectangle);  //畫紅框

            pictureBox0.Image = bitmap0;
        }

        Bitmap draw_selectionArea(Bitmap bmp, Rectangle rectangle)
        {
            Graphics g = Graphics.FromImage(bmp);
            Pen pen = new Pen(Color.Red, 3);
            pen.DashStyle = DashStyle.Dash;
            g.DrawRectangle(pen, rectangle.X - 4, rectangle.Y - 4, rectangle.Width + 8, rectangle.Height + 8);
            g.Dispose();
            return bmp;
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            int W = 640;
            int H = 480;

            pictureBox0.Size = new Size(W, H);
            //pictureBox1.Size = new Size(W, H);
            pictureBox1.Size = new Size(512 * 2 + 240, 1000);
            richTextBox1.Size = new Size(W, H - 100);

            x_st = 0;
            y_st = 0;
            dx = W;
            dy = H;

            pictureBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox1.Location = new Point(x_st + dx * 1 + 10, y_st + dy * 0 + 10);
            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 1);

            x_st = 20;
            y_st = -80;
            dx = 100;
            tb_filename.Size = new Size(620, 50);
            tb_filename.Location = new Point(x_st + dx * 0, y_st + dy * 2 - 15);

            groupBox_control.Size = new Size(360, 170);
            groupBox_control.Location = new Point(x_st + dx * 0, y_st + dy * 2 + 20);
            groupBox_selection.Size = new Size(250, 170);
            groupBox_selection.Location = new Point(x_st + dx * 4 - 30, y_st + dy * 2 + 20);
            groupBox_color.Size = new Size(290, 64);
            groupBox_color.Location = new Point(x_st + dx * 6 + 30, y_st + dy * 2 + 130);

            hScrollBar1.Size = new Size(200, 22);
            hScrollBar1.Location = new Point(x_st + dx * 9 + 40, y_st + dy * 2 + 130);
            hScrollBar2.Size = new Size(200, 22);
            hScrollBar2.Location = new Point(x_st + dx * 9 + 40, y_st + dy * 2 + 130+23);
            hScrollBar3.Size = new Size(200, 22);
            hScrollBar3.Location = new Point(x_st + dx * 9 + 40, y_st + dy * 2 + 130+46);

            //button
            x_st = 20;
            y_st = 20;
            dx = 80 + 10;
            dy = 40 + 10;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button5.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button7.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button8.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            bt_open_picture.Location = new Point(x_st + dx * 3, y_st + dy * 0 + 5);
            bt_open_picture.BackgroundImage = vcs_ColorHistogram.Properties.Resources.open_folder;
            bt_save_picture.Location = new Point(x_st + dx * 3, y_st + dy * 1 + 30 - 5);
            bt_save_picture.BackgroundImage = vcs_ColorHistogram.Properties.Resources.save;

            dx = 60;
            dy = 36;
            lb_x_st.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            lb_y_st.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            lb_w.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            lb_h.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            nud_x_st.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            nud_y_st.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            nud_w.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            nud_h.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            rb_selection1.Location = new Point(x_st + dx * 2 + 30, y_st + dy * 0);
            rb_selection2.Location = new Point(x_st + dx * 2 + 30, y_st + dy * 1);
            rb_selection3.Location = new Point(x_st + dx * 2 + 30, y_st + dy * 2);

            x_st = 10;
            y_st = 8;
            dx = 55;
            dy = 24;

            lb_rgb_r.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            lb_rgb_g.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            lb_rgb_b.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            lb_yuv_y.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            lb_yuv_u.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            lb_yuv_v.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            panel1.Size = new Size(100, 50);
            panel1.Location = new Point(x_st + dx * 3 + 10, y_st + dy * 0 + 3);

            //控件位置
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
            bt_clear.BringToFront();

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            //this.Size = new Size(1300, 1080);

            //離開按鈕的寫法
            bt_exit_setup();
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void do_channel_conversion()
        {
            //Channel 交換

            //讀取圖檔
            //原圖
            bitmap0 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            //準備要放資料的位圖
            bitmap1 = new Bitmap(bitmap0.Width, bitmap0.Height);

            /* 畫色塊 為了做驗證比較好用
            Graphics g = Graphics.FromImage(bitmap1);

            g.FillRectangle(new SolidBrush(Color.Red), 50, 100, 50, 50);
            g.FillRectangle(new SolidBrush(Color.Lime), 50, 100+70, 50, 50);
            g.FillRectangle(new SolidBrush(Color.Blue), 50, 100+140, 50, 50);
            */

            int i;
            int j;
            Color pt;
            int W = bitmap0.Width;
            int H = bitmap0.Height;

            for (j = 0; j < H; j++)
            {
                for (i = 0; i < W; i++)
                {
                    pt = bitmap0.GetPixel(i, j);

                    RGB pp = new RGB(pt.R, pt.G, pt.B);

                    byte r = pp.R;
                    byte g = pp.G;
                    byte b = pp.B;

                    Color cc = Color.FromArgb(255, g, b, b);

                    bitmap1.SetPixel(i, j, cc);
                }
            }

            pictureBox0.Image = bitmap0;    //原圖
            pictureBox1.Image = bitmap1;    //處理後的圖
        }

        void measure_brightness0(PictureBox pbox_source)
        {
            yuv_data_y = new int[256];
            yuv_data_u = new int[256];
            yuv_data_v = new int[256];
            rgb_data_r = new int[256];
            rgb_data_g = new int[256];
            rgb_data_b = new int[256];

            //量測範圍
            measure_x_st = (int)nud_x_st.Value;
            measure_y_st = (int)nud_y_st.Value;
            measure_w = (int)nud_w.Value;
            measure_h = (int)nud_h.Value;
            x_st = measure_x_st;
            y_st = measure_y_st;
            w = measure_w;
            h = measure_h;

            //把圖複製出來 量測資料用
            Bitmap bmp = (Bitmap)pbox_source.Image;

            //開始量測圖的資料
            int W = bmp.Width;
            int H = bmp.Height;
            //richTextBox1.Text += "圖片大小 : W = " + W.ToString() + ", H = " + H.ToString() + "\n";
            //richTextBox1.Text += "量測範圍 : x_st = " + x_st.ToString() + ", y_st = " + y_st.ToString() + ", w = " + w.ToString() + ", h = " + h.ToString() + "\n";

            int i;
            int j;
            int total_points = 0;

            for (j = y_st; j < (y_st + h); j++)
            {
                for (i = x_st; i < (x_st + w); i++)
                {
                    Color pt = bmp.GetPixel(i, j);
                    rgb_data_r[pt.R]++;
                    rgb_data_g[pt.G]++;
                    rgb_data_b[pt.B]++;

                    RGB pp = new RGB(pt.R, pt.G, pt.B);
                    YUV yyy = new YUV();
                    yyy = RGBToYUV(pp);
                    yuv_data_y[(int)yyy.Y]++;
                    yuv_data_u[(int)yyy.U]++;
                    yuv_data_v[(int)yyy.V]++;

                    total_points++;
                }
            }

            // 若有 純色 存在, 可能數字會很大, 會讓畫圖效果變差
            //一律忽視最亮和最暗的數值
            //yuv_data_y[0] = 0;
            //yuv_data_y[255] = 0;

            richTextBox1.Text += "共量測 " + total_points.ToString() + " 個點\n";
        }

        Bitmap draw_color_histogram0(Bitmap bmp, int[] color_data, Color color, int x_offset, int y_offset, string message)
        {
            int ww = 512;
            int hh1 = 300;
            int hh2 = 256;

            Graphics g1 = Graphics.FromImage(bmp);

            int i;
            int most = 0;
            int most_index = 0;
            int total_points = 0;
            int total_values = 0;

            for (i = 0; i < 256; i++)
            {
                total_points += color_data[i];
                total_values += color_data[i] * i;
                //richTextBox1.Text += color_data[i].ToString() + " ";
                if (color_data[i] > most)
                {
                    most = color_data[i];
                    most_index = i;
                }
                if (color_data[i] == 0)
                    color_data[i] = 5;
            }
            richTextBox1.Text += "最多 " + most.ToString() + "\t出現在 " + most_index.ToString() + "\n";
            richTextBox1.Text += "總點數 : " + total_points.ToString() + "\n";
            richTextBox1.Text += "總和 : " + total_values.ToString() + "\n";
            richTextBox1.Text += "平均 : " + ((double)total_values / total_points).ToString("F4") + "\n";

            Pen p = new Pen(Color.Blue, 2);
            Brush b = new SolidBrush(Color.FromArgb(33, Color.RoyalBlue.R, Color.RoyalBlue.G, Color.RoyalBlue.B));
            Brush br = new SolidBrush(color);
            double ratio = 0;
            Font f = new Font("標楷體", 20);

            p = new Pen(Color.Blue, 2);
            ratio = (double)hh2 / most;
            richTextBox1.Text += "ratio = " + ratio.ToString() + "\n";

            for (i = 0; i < 256; i++)
            {
                g1.FillRectangle(br, x_offset + i * 2, y_offset + hh2 - (float)(color_data[i] * ratio), 2, (float)(color_data[i] * ratio));
            }

            //畫連線
            Point[] curvePoints = new Point[256];    //一維陣列內有 256 個Point
            for (i = 0; i < 256; i++)
            {
                curvePoints[i].X = x_offset + i * 2;
                curvePoints[i].Y = y_offset + hh2 - (int)(color_data[i] * ratio);
            }
            g1.DrawCurve(new Pen(Color.Cyan, 3), curvePoints); //畫曲線

            g1.DrawRectangle(p, x_offset + 0 + 1, y_offset + 0 + 1, ww - 2, hh1 - 2);
            g1.DrawRectangle(p, x_offset + 0 + 1, y_offset + 0 + 1, ww - 2, hh2 - 2);

            b = new SolidBrush(Color.FromArgb(33, Color.RoyalBlue.R, Color.RoyalBlue.G, Color.RoyalBlue.B));
            g1.FillRectangle(b, x_offset + min * 2, y_offset + 0, (max - min) * 2, hh1);

            p = new Pen(color, 3);
            g1.DrawLine(p, x_offset + min * 2, y_offset + hh2, x_offset + max * 2, y_offset + 0);

            //richTextBox1.Text += "max = " + max.ToString() + "\n";
            //richTextBox1.Text += "min = " + min.ToString() + "\n";

            f = new Font("標楷體", 16);

            int draw_max = max;
            int draw_min = min;
            int draw_most_index = most_index;
            if ((message == "U") || (message == "V"))
            {
                draw_max = max - 128;
                draw_min = min - 128;
                draw_most_index = most_index - 128;

                //多畫一個0
                g1.DrawLine(p, x_offset + 128 * 2, y_offset + hh2 + 15, x_offset + 128 * 2, y_offset + hh2 - 15);
                g1.DrawString("0", f, new SolidBrush(Color.Blue), new PointF(x_offset + 128 * 2, y_offset + hh2));
            }

            if ((min >= 0) && (min <= 103))
            {
                g1.DrawString(draw_min.ToString(), f, new SolidBrush(Color.Blue), new PointF(x_offset + min * 2, y_offset + hh2));
            }
            else if (min < 0)
            {
                g1.DrawString(draw_min.ToString(), f, new SolidBrush(Color.Blue), new PointF(x_offset + 0, y_offset + hh2));
            }
            else
            {
                g1.DrawString(draw_min.ToString(), f, new SolidBrush(Color.Blue), new PointF(x_offset + 103 * 2, y_offset + hh2));
            }
            if ((max <= 255) && (max >= 152))
            {
                g1.DrawString(draw_max.ToString(), f, new SolidBrush(Color.Blue), new PointF(x_offset + max * 2 - 50, y_offset + hh2));
            }
            else if (max > 255)
            {
                g1.DrawString(draw_max.ToString(), f, new SolidBrush(Color.Blue), new PointF(x_offset + 512 - 50, y_offset + hh2));
            }
            else
            {
                g1.DrawString(draw_max.ToString(), f, new SolidBrush(Color.Blue), new PointF(x_offset + 152 * 2 - 50, y_offset + hh2));
            }

            //標出最大值
            richTextBox1.Text += "最多 " + most.ToString() + "\t出現在 " + most_index.ToString() + "\n";
            int linewidth = 5;
            if ((most_index < 5) || (most_index > 250))
                linewidth = 30;
            if (color == Color.Red)
            {
                if (most_index < 220)
                    g1.DrawString(most.ToString(), f, new SolidBrush(Color.Blue), new PointF(x_offset + most_index * 2 + 15, y_offset + 20));
                else
                    g1.DrawString(most.ToString(), f, new SolidBrush(Color.Blue), new PointF(x_offset + most_index * 2 - 110, y_offset + 20));
                p = new Pen(Color.Blue, linewidth);
                g1.DrawLine(p, x_offset + most_index * 2, y_offset + 0, x_offset + most_index * 2, y_offset + hh2);

                g1.DrawString(draw_most_index.ToString(), f, new SolidBrush(Color.Blue), new PointF(x_offset + most_index * 2 - 16, y_offset + hh2 + 16));
            }
            else
            {
                if (most_index < 220)
                    g1.DrawString(most.ToString(), f, new SolidBrush(Color.Red), new PointF(x_offset + most_index * 2 + 15, y_offset + 20));
                else
                    g1.DrawString(most.ToString(), f, new SolidBrush(Color.Red), new PointF(x_offset + most_index * 2 - 110, y_offset + 20));
                p = new Pen(Color.Red, linewidth);
                g1.DrawLine(p, x_offset + most_index * 2, y_offset + 0, x_offset + most_index * 2, y_offset + hh2);

                g1.DrawString(draw_most_index.ToString(), f, new SolidBrush(Color.Red), new PointF(x_offset + most_index * 2 - 16, y_offset + hh2 + 16));
            }

            g1.DrawString(message, f, new SolidBrush(Color.Red), new PointF(x_offset + 10, y_offset + 40));

            double offset = 0.0;
            if ((message == "U") || (message == "V"))
            {
                offset = -128.0;
            }
            g1.DrawString((((double)total_values / total_points) + offset).ToString("F2"), f, new SolidBrush(Color.Red), new PointF(x_offset + 10, y_offset + 70));

            return bmp;
        }

        void do_measure_brightness_all()
        {
            clear_all_pictures();

            measure_brightness_all(pictureBox0, pictureBox1);
        }

        void measure_brightness_all(PictureBox pbox_source, PictureBox pbox_destination)
        {
            richTextBox1.Text += "\n\n圖片 : " + filename + "\n";
            if (pbox_source.Image == null)
            {
                richTextBox1.Text += pbox_source.Name + " 無影像, 離開\n";
                return;
            }
            measure_brightness0(pbox_source);

            draw_color_histogram_all(pbox_destination);
        }

        void draw_color_histogram_all(PictureBox pbox)
        {
            int BORDER = 20;
            int x_st = BORDER;
            int y_st = BORDER;
            int dx = 512 + BORDER;
            int dy = 300 + BORDER;

            int ww = 512 * 2 + 100 + 100;
            int hh = 1000;
            bitmap1 = new Bitmap(ww, hh);

            Color color = Color.Red;
            int[] color_data = rgb_data_r;
            pbox.Image = draw_color_histogram0(bitmap1, color_data, color, x_st + dx * 0, y_st + dy * 0, "R");

            color = Color.Green;
            color_data = rgb_data_g;
            pbox.Image = draw_color_histogram0(bitmap1, color_data, color, x_st + dx * 0, y_st + dy * 1, "G");

            color = Color.Blue;
            color_data = rgb_data_b;
            pbox.Image = draw_color_histogram0(bitmap1, color_data, color, x_st + dx * 0, y_st + dy * 2, "B");

            color = Color.Yellow;
            color_data = yuv_data_y;
            pbox.Image = draw_color_histogram0(bitmap1, color_data, color, x_st + dx * 1, y_st + dy * 0, "Y");

            color = Color.Green;
            color_data = yuv_data_u;
            pbox.Image = draw_color_histogram0(bitmap1, color_data, color, x_st + dx * 1, y_st + dy * 1, "U");

            color = Color.Blue;
            color_data = yuv_data_v;
            pbox.Image = draw_color_histogram0(bitmap1, color_data, color, x_st + dx * 1, y_st + dy * 2, "V");
        }

        void do_select_picture(object sender, EventArgs e)
        {
            Stop_Webcam();
            OpenFileDialog openFileDialog1 = new OpenFileDialog();
            openFileDialog1.Title = "開啟圖片";
            openFileDialog1.FileName = "";
            openFileDialog1.Filter = "jpg (*.jpg)|*.jpg|bmp (*.bmp)|*.bmp|png (*.png)|*.png";	//限定檔案格式
            openFileDialog1.FilterIndex = 2;
            //openFileDialog1.RestoreDirectory = false;
            openFileDialog1.InitialDirectory = @"D:\_git\vcs\_1.data\______test_files6\白紙,亮度1";
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                clear_all_pictures();
                richTextBox1.Text += "4 get filename : " + openFileDialog1.FileName + "\n";
                tb_filename.Text = openFileDialog1.FileName;

                bitmap0 = (Bitmap)Image.FromFile(openFileDialog1.FileName);	//Image.FromFile出來的是Image格式
                pictureBox0.Image = bitmap0;

                W = bitmap0.Width;
                H = bitmap0.Height;

                //量測範圍
                measure_x_st = 50;
                measure_y_st = 50;
                measure_w = W - 50 * 2;
                measure_h = H - 50 * 2;

                nud_x_st.Value = measure_x_st;
                nud_y_st.Value = measure_y_st;
                nud_w.Value = measure_w;
                nud_h.Value = measure_h;

                rb_selection1.Checked = true;
                rb_selection2.Checked = false;
                rb_selection3.Checked = false;

                select_crop_area(sender, e);

                richTextBox1.Text += "開啟圖片完成\n";
            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";
                Start_Webcam();
            }
        }

        void do_save_picture(object sender, EventArgs e)
        {
            if (bitmap1 != null)
            {
                string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

                try
                {
                    bitmap1.Save(filename, ImageFormat.Bmp);

                    richTextBox1.Text += "存檔成功\n";
                    richTextBox1.Text += "已存檔 : " + filename + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "xxx錯誤訊息e40 : " + ex.Message + "\n";
                }
            }
            else
            {
                richTextBox1.Text += "無圖可存\n";
            }
            return;
        }

        void clear_all_pictures()
        {
            pictureBox1.Image = null;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            do_measure_brightness_all();
        }

        [DllImport("gdi32.dll")]
        static public extern uint GetPixel(IntPtr hDC, int XPos, int YPos);
        [DllImport("gdi32.dll")]
        static public extern IntPtr CreateDC(string driverName, string deviceName, string output, IntPtr lpinitData);
        [DllImport("gdi32.dll")]
        static public extern bool DeleteDC(IntPtr DC);
        static public byte GetRValue(uint color)
        {
            return (byte)color;
        }
        static public byte GetGValue(uint color)
        {
            return ((byte)(((short)(color)) >> 8));
        }
        static public byte GetBValue(uint color)
        {
            return ((byte)((color) >> 16));
        }
        static public byte GetAValue(uint color)
        {
            return ((byte)((color) >> 24));
        }

        public Color GetColor(Point screenPoint)
        {
            IntPtr displayDC = CreateDC("DISPLAY", null, null, IntPtr.Zero);
            uint colorref = GetPixel(displayDC, screenPoint.X, screenPoint.Y);
            DeleteDC(displayDC);
            byte Red = GetRValue(colorref);
            byte Green = GetGValue(colorref);
            byte Blue = GetBValue(colorref);
            return Color.FromArgb(Red, Green, Blue);
        }

        private void timer_rgb_Tick(object sender, EventArgs e)
        {
            Point pt = new Point(Control.MousePosition.X, Control.MousePosition.Y);
            Color cl = GetColor(pt);
            panel1.BackColor = cl;
            lb_rgb_r.Text = cl.R.ToString();
            lb_rgb_g.Text = cl.G.ToString();
            lb_rgb_b.Text = cl.B.ToString();

            RGB pp = new RGB(cl.R, cl.G, cl.B);
            YUV yyy = new YUV();
            yyy = RGBToYUV(pp);
            lb_yuv_y.Text = ((int)yyy.Y).ToString();
            lb_yuv_u.Text = ((int)yyy.U).ToString();
            lb_yuv_v.Text = ((int)yyy.V).ToString();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "SetPixel 彩色轉灰階\n";

            Bitmap bmp = (Bitmap)pictureBox0.Image;    //原圖

            int xx;
            int yy;

            for (yy = 0; yy < bmp.Height; yy++)
            {
                for (xx = 0; xx < bmp.Width; xx++)
                {
                    byte rrr = bmp.GetPixel(xx, yy).R;
                    byte ggg = bmp.GetPixel(xx, yy).G;
                    byte bbb = bmp.GetPixel(xx, yy).B;

                    int Gray = (rrr * 299 + ggg * 587 + bbb * 114 + 500) / 1000;
                    Color zz = Color.FromArgb(255, Gray, Gray, Gray);

                    bmp.SetPixel(xx, yy, zz);
                }
            }
            pictureBox0.Image = bmp;
            pictureBox1.Image = bmp;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //亮度量測
            bitmap0 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式

            bitmap0 = draw_selectionArea(bitmap0, SelectionRectangle);  //畫紅框

            pictureBox0.Image = bitmap0;

            measure_brightness(bitmap0);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //Channel 交換
            do_channel_conversion();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //統計
            do_measure_brightness_all();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //停止統計
            timer1.Enabled = false;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //顏色比例

            int ratio_r = hScrollBar1.Value;
            int ratio_g = hScrollBar2.Value;
            int ratio_b = hScrollBar3.Value;

            Bitmap bmp = (Bitmap)pictureBox0.Image;    //原圖

            int W = bmp.Width;
            int H = bmp.Height;

            richTextBox1.Text += "圖片寬度 : " + W.ToString() + "\n";
            richTextBox1.Text += "圖片高度 : " + H.ToString() + "\n";

            int i;
            int j;

            for (j = 0; j < H; j++)
            {
                for (i = 0; i < W; i++)
                {
                    Color cc = bmp.GetPixel(i, j);
                    //bmp.SetPixel(i, j, Color.FromArgb(255, cc.R, cc.B, 0));
                    int R_old = cc.R;
                    int G_old = cc.G;
                    int B_old = cc.B;
                    int R_new = R_old * ratio_r / 100;
                    int G_new = G_old * ratio_g / 100;
                    int B_new = B_old * ratio_b / 100;

                    R_new -= 50;
                    if (R_new < 0)
                        R_new = 0;

                    B_new += 50;
                    if (B_new > 255)
                        B_new = 255;

                    bmp.SetPixel(i, j, Color.FromArgb(255, R_new, G_new, B_new));
                }
            }
            //Graphics g = Graphics.FromImage(bmp);
            //g.DrawRectangle(Pens.Red, 5, 5, this.ClientSize.Width - 10, this.ClientSize.Height - 10);

            pictureBox1.Image = bmp;

        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //test
            int x_st = 100;
            int y_st = 100;
            int w = 200;
            int h = 100;

            SelectionRectangle = MakeRectangle(x_st, y_st, x_st + w, y_st + h);

            Bitmap bmp1 = (Bitmap)pictureBox0.Image;    //原圖
            Bitmap bmp2 = draw_selectionArea(bmp1, SelectionRectangle); //畫紅框

            pictureBox1.Image = bmp2;


        }

        private void button8_Click(object sender, EventArgs e)
        {
            clear_all_pictures();
        }

        private void bt_open_picture_Click(object sender, EventArgs e)
        {
            do_select_picture(sender, e);
        }

        private void bt_save_picture_Click(object sender, EventArgs e)
        {
            do_save_picture(sender, e);
        }
    }
}
