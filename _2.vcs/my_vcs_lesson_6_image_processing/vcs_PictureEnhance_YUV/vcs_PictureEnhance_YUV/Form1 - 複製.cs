using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;
using System.Runtime.InteropServices;

using AForge.Video;             //需要添加這兩個.dll
using AForge.Video.DirectShow;

namespace vcs_PictureEnhance_YUV
{
    public partial class Form1 : Form
    {
        int flag_operation_mode = 0;    //0 : 圖片模式, 1 : 視訊模式

        string filename1 = @"C:\______test_files1\ims01.bmp";
        //string filename1 = @"C:\______test_files1\__pic\_ntuh\op1.bmp";
        //string filename1 = @"C:\______test_files1\color1.bmp";
        //string filename2 = @"C:\______test_files1\color2.bmp";

        private Point pt_st = Point.Empty;//記錄鼠標按下時的坐標，用來確定繪圖起點
        private Point pt_sp = Point.Empty;//記錄鼠標放開時的坐標，用來確定繪圖終點
        private Bitmap bitmap1 = null;  //原圖
        private Bitmap bitmap2 = null;  //從原圖修改過的
        private Rectangle SelectionRectangle = new Rectangle(new Point(0, 0), new Size(0, 0));    //用來保存截圖的矩形

        public Point firstPoint = new Point(0, 0);  //鼠標第一點 
        public Point secondPoint = new Point(0, 0);  //鼠標第二點 
        public bool begin = false;   //是否開始畫矩形 

        private int W = 0;  //原圖的寬
        private int H = 0;  //原圖的高
        private int w = 0;  //擷取圖的寬
        private int h = 0;  //擷取圖的高
        int x_st = 0;   //擷取開始x
        int y_st = 0;   //擷取開始y

        private int brightness_max = 0;
        private int brightness_min = 0;
        private int brightness_avg = 0;
        private double brightness_sd = 0;
        private float brightness_ratio = 0;
        private int brightness_max_mod = 0;
        private int brightness_min_mod = 0;
        private float brightness_ratio_mod = 0;

        int[] brightness_data = new int[256];

        int max = 255;
        int min = 0;

        bool flag_webcam_ok = false;
        bool flag_do_enhancement = false;

        //參考
        //【AForge.NET】C#上使用AForge.Net擷取視訊畫面
        //https://ccw1986.blogspot.com/2013/01/ccaforgenetcapture-image.html

        //AForge下載鏈結
        //http://www.aforgenet.com/framework/downloads.html

        //參考/右鍵/加入參考/瀏覽AForge.Video.dll和AForge.Video.DirectShow.dll

        public FilterInfoCollection USBWebcams = null;
        public VideoCaptureDevice Cam = null;
        DateTime webcam_start_time = DateTime.Now;

        int[,] rgb_array = new int[64, 3] {
{   0,   0, 143},
{   0,   0, 159},
{   0,   0, 175},
{   0,   0, 191},
{   0,   0, 207},
{   0,   0, 223},
{   0,   0, 239},
{   0,   0, 255},
{   0,  16, 255},
{   0,  32, 255},
{   0,  48, 255},
{   0,  64, 255},
{   0,  80, 255},
{   0,  96, 255},
{   0, 112, 255},
{   0, 128, 255},
{   0, 143, 255},
{   0, 159, 255},
{   0, 175, 255},
{   0, 191, 255},
{   0, 207, 255},
{   0, 223, 255},
{   0, 239, 255},
{   0, 255, 255},
{  16, 255, 239},
{  32, 255, 223},
{  48, 255, 207},
{  64, 255, 191},
{  80, 255, 175},
{  96, 255, 159},
{ 112, 255, 143},
{ 128, 255, 128},
{ 143, 255, 112},
{ 159, 255,  96},
{ 175, 255,  80},
{ 191, 255,  64},
{ 207, 255,  48},
{ 223, 255,  32},
{ 239, 255,  16},
{ 255, 255,   0},
{ 255, 239,   0},
{ 255, 223,   0},
{ 255, 207,   0},
{ 255, 191,   0},
{ 255, 175,   0},
{ 255, 159,   0},
{ 255, 143,   0},
{ 255, 128,   0},
{ 255, 112,   0},
{ 255,  96,   0},
{ 255,  80,   0},
{ 255,  64,   0},
{ 255,  48,   0},
{ 255,  32,   0},
{ 255,  16,   0},
{ 255,   0,   0},
{ 239,   0,   0},
{ 223,   0,   0},
{ 207,   0,   0},
{ 191,   0,   0},
{ 175,   0,   0},
{ 159,   0,   0},
{ 143,   0,   0},
{ 128,   0,   0}
};

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

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //C# 跨 Thread 存取 UI
            //Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效	same
            Control.CheckForIllegalCrossThreadCalls = false;//忽略跨執行緒錯誤

            pictureBox1.MouseDown += new MouseEventHandler(pictureBox1_MouseDown);
            pictureBox1.MouseMove += new MouseEventHandler(pictureBox1_MouseMove);
            pictureBox2.MouseMove += new MouseEventHandler(pictureBox2_MouseMove);
            pictureBox1.MouseUp += new MouseEventHandler(pictureBox1_MouseUp);
            pictureBox1.Paint += new PaintEventHandler(pictureBox1_Paint);
            pictureBox2.Paint += new PaintEventHandler(pictureBox2_Paint);
            pictureBox3a.Paint += new PaintEventHandler(pictureBox3a_Paint);
            pictureBox3b.Paint += new PaintEventHandler(pictureBox3b_Paint);
            nud_x_st.ValueChanged += new EventHandler(select_crop_area);
            nud_y_st.ValueChanged += new EventHandler(select_crop_area);
            nud_w.ValueChanged += new EventHandler(select_crop_area);
            nud_h.ValueChanged += new EventHandler(select_crop_area);

            show_item_location();
            reset_picture();

            if (flag_operation_mode == 0)   //圖片模式
            {
            }
            else if (flag_operation_mode == 1)  //視訊模式
            {
                bitmap1 = new Bitmap(640, 480);
                bitmap2 = new Bitmap(640, 480);
                gc = Graphics.FromImage(bitmap1);

                Start_Webcam();

                this.Visible = true;
                this.KeyPreview = true;
            }
            else
            {
            }
        }

        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            if (flag_operation_mode == 0)   //圖片模式
            {

            }
            else if (flag_operation_mode == 1)  //視訊模式
            {
                Stop_Webcam();
            }
        }

        private void select_crop_area(object sender, EventArgs e)
        {
            if ((SelectionRectangle.Width <= 0) || (SelectionRectangle.Height <= 0))
                return;

            int x_st = (int)nud_x_st.Value;
            int y_st = (int)nud_y_st.Value;
            int w = (int)nud_w.Value;
            int h = (int)nud_h.Value;

            draw_x_st = x_st;
            draw_y_st = y_st;
            draw_w = w;
            draw_h = h;

            this.pictureBox1.Invalidate();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;
            int dy2;

            int pbx_W = 640 + 10;
            int pbx_H = 480 + 10;
            int pbx_W2 = 480 + 60;
            int pbx_H2 = 520 * 2 / 3;
            int pbx_W3 = 480;

            x_st = 10;
            y_st = 10;
            dx = pbx_W + 10;
            dy = pbx_H + 10;
            dy2 = pbx_H2 + 10;

            groupBox_selection.Size = new Size(pbx_W, 65);
            pictureBox1.Size = new Size(pbx_W, pbx_H);
            pictureBox2.Size = new Size(pbx_W, pbx_H);
            pictureBox3a.Size = new Size(pbx_W2, pbx_H2);
            pictureBox3b.Size = new Size(pbx_W2, pbx_H2);
            pictureBox4.Size = new Size(pbx_W3 * 2 + 10, pbx_H2 * 2 + 16);
            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox2.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox3a.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox3b.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox4.SizeMode = PictureBoxSizeMode.Normal;

            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            groupBox_selection.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            pictureBox3a.Location = new Point(x_st + dx * 1, y_st + dy2 * 0);
            pictureBox3b.Location = new Point(x_st + dx * 1 + pbx_W2, y_st + dy2 * 0);
            pictureBox4.Location = new Point(x_st + dx * 1, y_st + dy2 * 1);

            lb_brightness.Text = "";
            y_st = 420;
            dx += 160;
            dy = 40;
            lb_brightness.Location = new Point(x_st + dx * 2, y_st + dy * -1 - 10);
            button0.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 2, y_st + dy * 9);
            button10.Location = new Point(x_st + dx * 2, y_st + dy * 10);
            button11.Location = new Point(x_st + dx * 2, y_st + dy * 11);
            button12.Location = new Point(x_st + dx * 2, y_st + dy * 12);
            button13.Location = new Point(x_st + dx * 2, y_st + dy * 13);
            button14.Location = new Point(x_st + dx * 2, y_st + dy * 14);
            cb_magnify.Location = new Point(x_st + dx * 2, y_st + dy * 15);
            cb_modify.Location = new Point(x_st + dx * 2, y_st + dy * 15 + 25);

            y_st = 10;
            richTextBox1.Size = new Size(160, 1040);
            richTextBox1.Location = new Point(x_st + dx * 2 + 105, y_st + dy * 0);

            x_st = 10;
            y_st = 20;
            dx = 50;
            dy = 50;
            lb_x_st.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            nud_x_st.Location = new Point(x_st + dx * 1 - 28, y_st + dy * 0);
            lb_y_st.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            nud_y_st.Location = new Point(x_st + dx * 3 - 28, y_st + dy * 0);

            lb_w.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            nud_w.Location = new Point(x_st + dx * 5 - 28, y_st + dy * 0);
            lb_h.Location = new Point(x_st + dx * 6, y_st + dy * 0);
            nud_h.Location = new Point(x_st + dx * 7 - 28, y_st + dy * 0);

            bt_apply.Location = new Point(x_st + dx * 8 + 10, y_st + dy * 0 - 4);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            bt_open_file_setup();
            bt_exit_setup();
        }

        private void bt_open_file_Click(object sender, EventArgs e)
        {
            OpenFileDialog openFileDialog1 = new OpenFileDialog();

            openFileDialog1.Title = "單選檔案";
            //openFileDialog1.ShowHelp = true;
            openFileDialog1.FileName = "";              //預設開啟的檔名
            openFileDialog1.DefaultExt = "*.txt";
            openFileDialog1.Filter = "圖片(*.bmp,*.jpg,*.png)|*.bmp;*.jpg;*.png";   //存檔類型
            //openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
            openFileDialog1.RestoreDirectory = true;
            //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            //openFileDialog1.InitialDirectory = @"c:\______test_files1";  //預設開啟的路徑
            openFileDialog1.InitialDirectory = @"C:\______test_files1\__pic\_ntuh";  //預設開啟的路徑
            openFileDialog1.Multiselect = false;    //單選
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "已選取檔案: " + openFileDialog1.FileName + "\n";
                FileInfo f = new FileInfo(openFileDialog1.FileName);
                richTextBox1.Text += "Name: " + f.Name + "\n";
                richTextBox1.Text += "FullName: " + f.FullName + "\n";
                richTextBox1.Text += "Extension: " + f.Extension + "\n";
                richTextBox1.Text += "size: " + f.Length.ToString() + "\n";
                richTextBox1.Text += "Directory: " + f.Directory + "\n";
                richTextBox1.Text += "DirectoryName: " + f.DirectoryName + "\n";

                filename1 = openFileDialog1.FileName;

                reset_picture();
            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";
            }
        }

        void bt_open_file_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_open_file = new Button();  // 實例化按鈕
            bt_open_file.Size = new Size(w, h);
            bt_open_file.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Blue, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, w / 4, 0, (w - 1) / 2, h - 1);
            g.DrawLine(p, (w - 1) * 3 / 4, 0, (w - 1) / 2, h - 1);
            bt_open_file.Image = bmp;

            bt_open_file.Location = new Point(this.ClientSize.Width - bt_open_file.Width, 0 + h);
            bt_open_file.Click += bt_open_file_Click;     // 加入按鈕事件

            this.Controls.Add(bt_open_file); // 將按鈕加入表單
            bt_open_file.BringToFront();     //移到最上層
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
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

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void reset_picture()
        {
            if (flag_operation_mode == 0)   //圖片模式
            {
                bitmap1 = (Bitmap)Image.FromFile(filename1);	//Image.FromFile出來的是Image格式
                bitmap2 = (Bitmap)bitmap1.Clone();

                pictureBox1.Image = bitmap1;
                pictureBox2.Image = bitmap2;

                W = bitmap1.Width;
                H = bitmap1.Height;
                //richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";

            }
            else if (flag_operation_mode == 1)  //視訊模式
            {
                W = 640;
                H = 480;
            }
        }

        int sel = 0;
        void enhance_bitmap_data(Bitmap bitmap1, int x_st, int y_st, int w, int h)
        {
            //影像加強前 統計所有亮度, TBD

            int i;
            int j;
            int Y_max = 0;
            int Y_min = 255;
            Color pt;

            //一維陣列用法：
            double[] sd_num = new double[w * h];
            int total_points = 0;
            double total_brightness = 0;

            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {
                    pt = bitmap1.GetPixel(x_st + i, y_st + j);

                    RGB pp = new RGB(pt.R, pt.G, pt.B);
                    YUV yyy = new YUV();
                    yyy = RGBToYUV(pp);

                    total_brightness += yyy.Y;
                    sd_num[total_points] = yyy.Y;
                    total_points++;
                }
            }

            //richTextBox1.Text += "共有 " + total_points.ToString() + " 個點\n";
            //richTextBox1.Text += "共有 " + (w * h).ToString() + " 個點\n";
            //richTextBox1.Text += "總亮度 " + total_brightness.ToString() + "\n";
            //richTextBox1.Text += "平均亮度 " + (total_brightness / total_points).ToString() + "\n";
            double sd = SD(sd_num);
            //richTextBox1.Text += "標準差 " + sd.ToString("F2") + "\n";
            brightness_sd = sd;

            int average_brightness = (int)Math.Round(total_brightness / total_points); //四捨五入
            //richTextBox1.Text += "平均亮度 " + average_brightness.ToString() + "\n";
            brightness_avg = average_brightness;

            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {
                    pt = bitmap1.GetPixel(x_st + i, y_st + j);

                    RGB pp = new RGB(pt.R, pt.G, pt.B);
                    YUV yyy = new YUV();
                    yyy = RGBToYUV(pp);

                    int y = (int)Math.Round(yyy.Y); //四捨五入

                    if (y > 255)
                        y = 255;
                    if (y < 0)
                        y = 0;

                    if (Y_max < y)
                        Y_max = y;

                    if (Y_min > y)
                        Y_min = y;
                }
            }
            if (Y_max > 255)
                Y_max = 255;
            if (Y_min < 0)
                Y_min = 0;

            brightness_max = Y_max;
            brightness_min = Y_min;

            int diff_Y = Y_max - Y_min;

            if (diff_Y == 0)
                diff_Y = 1;

            float ratio_Y = 255 / (float)diff_Y;
            brightness_ratio = ratio_Y;

            richTextBox1.Text += "\nM = " + Y_max.ToString() + "\tm = " + Y_min.ToString() + "\n";
            richTextBox1.Text += "D = " + diff_Y.ToString("F2") + "\tR = " + ratio_Y.ToString("F2") + "\n";

            if (cb_modify.Checked == true)
            {
                float rr_sp = 2.0f;
                if ((Y_max - average_brightness) > sd * rr_sp)
                {
                    richTextBox1.Text += "調整Ymax\n";

                    Y_max = (int)(average_brightness + sd * rr_sp);
                }

                float rr_st = 3.0f;
                if ((average_brightness - Y_min) > sd * rr_st)
                {
                    richTextBox1.Text += "調整Ymin\n";

                    Y_min = (int)(average_brightness - sd * rr_st);
                }

                diff_Y = Y_max - Y_min;

                if (diff_Y == 0)
                    diff_Y = 1;

                ratio_Y = 255 / (float)diff_Y;
                brightness_ratio = ratio_Y;

                richTextBox1.Text += "調整後:\n";
                richTextBox1.Text += "M = " + Y_max.ToString() + "\tm = " + Y_min.ToString() + "\n";
                richTextBox1.Text += "D = " + diff_Y.ToString("F2") + "\tR = " + ratio_Y.ToString("F2") + "\n";
            }

            brightness_max_mod = Y_max;
            brightness_min_mod = Y_min;
            brightness_ratio_mod = ratio_Y;

            if ((sel % 2) == 0)
            {
                //僅套用到選取的區域
                for (j = 0; j < h; j++)
                {
                    for (i = 0; i < w; i++)
                    {
                        pt = bitmap1.GetPixel(x_st + i, y_st + j);

                        RGB pp = new RGB(pt.R, pt.G, pt.B);
                        YUV yyy = new YUV();
                        yyy = RGBToYUV(pp);

                        int y = (int)Math.Round(yyy.Y); //四捨五入

                        int Y_new = (int)((y - Y_min) * ratio_Y);
                        if (Y_new > 255)
                            Y_new = 255;
                        if (Y_new < 0)
                            Y_new = 0;

                        YUV yyy2 = new YUV(Y_new, yyy.U, yyy.V);
                        RGB rrr = new RGB();
                        rrr = YUVToRGB(yyy2);

                        bitmap1.SetPixel(x_st + i, y_st + j, Color.FromArgb(255, rrr.R, rrr.G, rrr.B));
                    }
                }
            }
            else
            {
                //套用到選取全圖
                for (j = 0; j < H; j++)
                {
                    for (i = 0; i < W; i++)
                    {
                        pt = bitmap1.GetPixel(i, j);

                        RGB pp = new RGB(pt.R, pt.G, pt.B);
                        YUV yyy = new YUV();
                        yyy = RGBToYUV(pp);

                        int y = (int)Math.Round(yyy.Y); //四捨五入

                        int Y_new = (int)((y - Y_min) * ratio_Y);
                        if (Y_new > 255)
                            Y_new = 255;
                        if (Y_new < 0)
                            Y_new = 0;

                        YUV yyy2 = new YUV(Y_new, yyy.U, yyy.V);
                        RGB rrr = new RGB();
                        rrr = YUVToRGB(yyy2);

                        bitmap1.SetPixel(i, j, Color.FromArgb(255, rrr.R, rrr.G, rrr.B));
                    }
                }
            }

            //若是幾乎沒什麼變化的, 畫一個框來表示區域
            if ((ratio_Y < 1.4) || ((sel % 2) == 1))
            {
                Graphics g = Graphics.FromImage(bitmap1);
                g.DrawRectangle(Pens.Blue, x_st - 1, y_st - 1, w + 2, h + 2);
            }


            //影像加強後 統計所有亮度, TBD

            sel++;
        }

        void show_part_image(Bitmap bmp, int x_st, int y_st, int w, int h)
        {
            if ((x_st < 0) || (x_st >= W))
                return;
            if ((y_st < 0) || (y_st >= H))
                return;
            if ((w <= 0) || (w > W))
                return;
            if ((h <= 0) || (h > H))
                return;
            if (((x_st + w) > W) || ((y_st + h) > H))
                return;

            //滿框放大顯示
            Bitmap bitmap3b = bmp.Clone(new Rectangle(x_st, y_st, w, h), PixelFormat.Format32bppArgb);
            pictureBox3b.Image = bitmap3b;

            int pbox3a_w = pictureBox3a.Width;
            int pbox3a_h = pictureBox3a.Height;
            //richTextBox1.Text += "pbox3a_w = " + pbox3a_w.ToString() + ", pbox3a_h = " + pbox3a_h.ToString() + "\n";

            if (w > (pbox3a_w / 4))
            {
                pictureBox3a.Image = null;
                return;
            }

            if (h > (pbox3a_h / 2))
            {
                pictureBox3a.Image = null;
                return;
            }

            if ((w > 640 / 2) || (h > 480 / 2))
            {
                pictureBox3a.Image = null;
                return;
            }

            //準備放大兩倍
            //richTextBox1.Text += "x_st = " + x_st.ToString() + ", y_st = " + y_st.ToString() + ", w = " + w.ToString() + ", h = " + h.ToString() + "\n";

            Bitmap bitmap3a = new Bitmap(w * 2, h * 2);

            int i;
            int j;
            Color pt;
            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {
                    pt = bitmap3b.GetPixel(i, j);

                    //把最亮和最暗的標示出來
                    RGB pp = new RGB(pt.R, pt.G, pt.B);
                    YUV yyy = new YUV();
                    yyy = RGBToYUV(pp);

                    int y = (int)Math.Round(yyy.Y); //四捨五入

                    if (y > (255 - 20))
                    {
                        pt = Color.Lime;
                    }
                    if (y < 30)
                    {
                        pt = Color.Blue;
                    }

                    bitmap3a.SetPixel(i * 2, j * 2, pt);
                    bitmap3a.SetPixel(i * 2, j * 2 + 1, pt);
                    bitmap3a.SetPixel(i * 2 + 1, j * 2, pt);
                    bitmap3a.SetPixel(i * 2 + 1, j * 2 + 1, pt);
                }
            }

            Bitmap bitmap33 = new Bitmap(pbox3a_w, pbox3a_h);

            Graphics g = Graphics.FromImage(bitmap33);

            Bitmap bitmap30 = bitmap1.Clone(new Rectangle(x_st, y_st, w, h), PixelFormat.Format32bppArgb);

            int xx0 = 0;
            int xx1 = pbox3a_w / 4;
            int xx2 = pbox3a_w / 2;

            int yy0 = (pbox3a_h - bitmap30.Height) / 2;
            int yy1 = (pbox3a_h - bitmap3b.Height) / 2;
            int yy2 = (pbox3a_h - bitmap3a.Height) / 2;

            int dx = (pbox3a_w / 2 - bitmap3a.Width) / 2;

            g.DrawImage(bitmap30, xx0 + dx, yy0, bitmap30.Width, bitmap30.Height);   //原圖 一倍
            g.DrawImage(bitmap3b, xx1 + dx, yy1, bitmap3b.Width, bitmap3b.Height);   //增強後的圖 一倍
            g.DrawImage(bitmap3a, xx2 + dx, yy2, bitmap3a.Width, bitmap3a.Height);   //增強後的圖 二倍

            int height = 20;
            SolidBrush b = new SolidBrush(Color.Lime);
            g.FillRectangle(b, bitmap33.Width / 2, 0, bitmap33.Width / 2, height);
            g.DrawString("20", new Font("標楷體", 12), new SolidBrush(Color.Red), new PointF(bitmap33.Width / 2, 0));

            b = new SolidBrush(Color.Blue);
            g.FillRectangle(b, bitmap33.Width / 2, bitmap33.Height - height, bitmap33.Width / 2, height);
            g.DrawString("30", new Font("標楷體", 12), new SolidBrush(Color.Red), new PointF(bitmap33.Width / 2, bitmap33.Height - height));

            pictureBox3a.Image = bitmap33;
        }

        void draw_enhanced_image(Bitmap bmp, int x_st, int y_st, int w, int h)
        {
            enhance_bitmap_data(bmp, x_st, y_st, w, h);
            show_part_image(bmp, x_st, y_st, w, h);

            pictureBox2.Image = bmp;    //把影像增強後的結果顯示出來
        }

        void ImageEnhancement(int x_st, int y_st, int w, int h)
        {
            enhance_bitmap_data(bitmap2, x_st, y_st, w, h);
            show_part_image(bitmap2, x_st, y_st, w, h);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            show_item_location();
            reset_picture();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            reset_picture();
            pictureBox2.Image = null;

            Pen p = new Pen(Color.Red, 3);
            SolidBrush sb = new SolidBrush(Color.Blue);
            Bitmap bitmap2 = new Bitmap(pictureBox2.Width, pictureBox2.Height);
            Graphics g = Graphics.FromImage(bitmap2);
            g.Clear(Color.White);

            int border = 60;
            x_st = border;
            y_st = border;
            w = W - border * 2;
            h = H - border * 2;


            richTextBox1.Text += "跳點量測亮度 x_st = " + x_st.ToString() + ", y_st = " + y_st.ToString() + ", w = " + w.ToString() + ", h = " + h.ToString() + "\n";

            int dx = 1;
            int dy = 1;

            int i = 1;

            for (i = 0; i < 40; i++)
            {
                dx = i * 5;
                dy = i * 5;

                if (dx == 0)
                    dx = 1;
                if (dy == 0)
                    dy = 1;

                richTextBox1.Text += "\n每隔 " + dx.ToString() + " 點計算\n";

                int max = 0;
                int min = 0;
                int avg = 0;
                double sd = 0;

                read_bitmap_data(bitmap1, x_st, y_st, w, h, dx, dy, out max, out min, out avg, out sd);
                richTextBox1.Text += "max = " + max.ToString() + ", min = " + max.ToString() + ", avg = " + avg.ToString() + ", sd = " + sd.ToString("F2") + "\n";

                int width = 15;

                int HH = 400;

                p = new Pen(Color.Red, 3);
                g.DrawLine(p, width * i, HH - max * 1, width * i + width, HH - max * 1);
                p = new Pen(Color.Blue, 3);
                g.DrawLine(p, width * i, HH - min * 1, width * i + width, HH - min * 1);
                p = new Pen(Color.Yellow, 3);
                g.DrawLine(p, width * i, HH - avg * 1, width * i + width, HH - avg * 1);

                //p = new Pen(Color.Pink, 3);
                //g.DrawLine(p, width * i, HH - (int)sd, width * i + 40, HH - (int)sd);
            }
            pictureBox2.Image = bitmap2;
        }

        void read_bitmap_data(Bitmap bitmap1, int x_st, int y_st, int w, int h, int dx, int dy, out int max, out int min, out int avg, out double sd)
        {
            int i;
            int j;
            int Y_max = 0;
            int Y_min = 255;
            Color pt;

            int total_points = 0;
            double total_brightness = 0;
            int average_brightness;
            int diff_Y;
            float ratio_Y;

            int len = (int)(Math.Ceiling(w / (double)dx)) * (int)(Math.Ceiling(h / (double)dy));
            double[] sd_num = new double[len];

            richTextBox1.Text += "len = " + len.ToString() + "\n";

            for (j = 0; j < h; j += dy)
            {
                for (i = 0; i < w; i += dx)
                {
                    pt = bitmap1.GetPixel(x_st + i, y_st + j);

                    RGB pp = new RGB(pt.R, pt.G, pt.B);
                    YUV yyy = new YUV();
                    yyy = RGBToYUV(pp);

                    total_brightness += yyy.Y;

                    sd_num[total_points] = yyy.Y;

                    total_points++;
                }
            }

            richTextBox1.Text += "共有 " + total_points.ToString() + " 個點\n";
            //richTextBox1.Text += "共有 " + (w * h).ToString() + " 個點\n";
            //richTextBox1.Text += "總亮度 " + total_brightness.ToString() + "\n";
            //richTextBox1.Text += "平均亮度 " + (total_brightness / total_points).ToString() + "\n";
            sd = SD(sd_num);
            richTextBox1.Text += "標準差 " + sd.ToString("F2") + "\n";

            average_brightness = (int)Math.Round(total_brightness / total_points); //四捨五入
            richTextBox1.Text += "平均亮度 " + average_brightness.ToString() + "\n";
            avg = average_brightness;

            for (j = 0; j < h; j += dy)
            {
                for (i = 0; i < w; i += dx)
                {
                    pt = bitmap1.GetPixel(x_st + i, y_st + j);

                    RGB pp = new RGB(pt.R, pt.G, pt.B);
                    YUV yyy = new YUV();
                    yyy = RGBToYUV(pp);

                    int y = (int)Math.Round(yyy.Y); //四捨五入

                    if (y > 255)
                        y = 255;
                    if (y < 0)
                        y = 0;

                    if (Y_max < y)
                        Y_max = y;

                    if (Y_min > y)
                        Y_min = y;
                }
            }
            if (Y_max > 255)
                Y_max = 255;
            if (Y_min < 0)
                Y_min = 0;

            brightness_max = Y_max;
            brightness_min = Y_min;

            max = brightness_max;
            min = brightness_min;

            diff_Y = Y_max - Y_min;

            if (diff_Y == 0)
                diff_Y = 1;

            ratio_Y = 255 / (float)diff_Y;
            brightness_ratio = ratio_Y;

            richTextBox1.Text += "M = " + Y_max.ToString() + "\tm = " + Y_min.ToString() + "\t";
            richTextBox1.Text += "D = " + diff_Y.ToString("F2") + "\tR = " + ratio_Y.ToString("F2") + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            int x_st = 50;
            int y_st = 50;
            int w = W / 2;
            int h = H / 2;

            reset_picture();
            ImageEnhancement(x_st, y_st, w, h);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //偽色彩

            string filename1 = @"C:\______test_files1\__pic\_ntuh\op1.jpg";
            //string filename1 = @"C:\______test_files1\fakecolor.jpg";

            /*
            //彩色轉灰階
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename1);	//Bitmap.FromFile出來的是Image格式

            //SetPixel 彩色轉灰階
            Bitmap bitmap2 = color_to_gray(bitmap1);

            pictureBox1.Image = bitmap1;
            */

            //彩色轉灰階

            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename1);	//Bitmap.FromFile出來的是Image格式

            //SetPixel 彩色轉灰階
            Bitmap bitmap2 = color_to_gray(bitmap1);

            bitmap2 = gcTrans(bitmap1, true, 255 / 10);
            pictureBox1.Image = bitmap2;



            /*
            int border = 80;
            x_st = border;
            y_st = border;
            w = W - border * 2;
            h = H - border * 2;


            ImageEnhancement(x_st, y_st, w, h);
            */

        }

        Bitmap color_to_gray(Bitmap bitmap1)
        {
            //richTextBox1.Text += "SetPixel 彩色轉灰階\n";

            int xx;
            int yy;

            for (yy = 0; yy < bitmap1.Height; yy++)
            {
                for (xx = 0; xx < bitmap1.Width; xx++)
                {
                    byte rrr = bitmap1.GetPixel(xx, yy).R;
                    byte ggg = bitmap1.GetPixel(xx, yy).G;
                    byte bbb = bitmap1.GetPixel(xx, yy).B;

                    int Gray = (rrr * 299 + ggg * 587 + bbb * 114 + 500) / 1000;
                    Color zz = Color.FromArgb(255, Gray, Gray, Gray);

                    bitmap1.SetPixel(xx, yy, zz);
                }
            }
            return bitmap1;
        }

        //偽彩色圖像處理 ST

        /// <summary>
        /// 偽彩色圖像處理
        /// 博客園-初行 http://www.cnblogs.com/zxlovenet
        /// 日期：2014.2.14
        /// </summary>
        /// <param name="bmp">傳入的灰度圖像</param>
        /// <param name="method">使用何種方法，false強度分層法,true灰度級-彩色變換法</param>
        /// <param name="seg">強度分層中的分層數</param>
        /// <returns>返回偽彩色圖像</returns>
        private Bitmap gcTrans(Bitmap bmp, bool method, byte seg)
        {
            if (bmp != null)
            {
                if (System.Drawing.Imaging.PixelFormat.Format24bppRgb == bmp.PixelFormat)
                {
                    Rectangle rect = new Rectangle(0, 0, bmp.Width, bmp.Height);
                    System.Drawing.Imaging.BitmapData bmpData = bmp.LockBits(rect, System.Drawing.Imaging.ImageLockMode.ReadWrite, bmp.PixelFormat);
                    IntPtr ptr = bmpData.Scan0;
                    int bytes = bmp.Width * bmp.Height * 3;
                    byte[] grayValues = new byte[bytes];
                    System.Runtime.InteropServices.Marshal.Copy(ptr, grayValues, 0, bytes);
                    bmp.UnlockBits(bmpData);

                    byte[] rgbValues = new byte[bytes];
                    //清零
                    Array.Clear(rgbValues, 0, bytes);
                    byte tempB;

                    if (method == false)
                    {
                        //強度分層法
                        for (int i = 0; i < bytes; i += 3)
                        {
                            byte ser = (byte)(256 / seg);
                            tempB = (byte)(grayValues[i] / ser);
                            //分配任意一種顏色
                            rgbValues[i + 1] = (byte)(tempB * ser);
                            rgbValues[i] = (byte)((seg - 1 - tempB) * ser);
                            rgbValues[i + 2] = 0;
                        }
                    }
                    else
                    {
                        //灰度級-彩色變換法
                        for (int i = 0; i < bytes; i += 3)
                        {
                            if (grayValues[i] < 64)
                            {
                                rgbValues[i + 2] = 0;
                                rgbValues[i + 1] = (byte)(4 * grayValues[i]);
                                rgbValues[i] = 255;
                            }
                            else if (grayValues[i] < 128)
                            {
                                rgbValues[i + 2] = 0;
                                rgbValues[i + 1] = 255;
                                rgbValues[i] = (byte)(-4 * grayValues[i] + 2 * 255);
                            }
                            else if (grayValues[i] < 192)
                            {
                                rgbValues[i + 2] = (byte)(4 * grayValues[i] - 2 * 255);
                                rgbValues[i + 1] = 255;
                                rgbValues[i] = 0;
                            }
                            else
                            {
                                rgbValues[i + 2] = 255;
                                rgbValues[i + 1] = (byte)(-4 * grayValues[i] + 4 * 255);
                                rgbValues[i] = 0;
                            }
                        }

                    }
                    bmp = new Bitmap(bmp.Width, bmp.Height, System.Drawing.Imaging.PixelFormat.Format24bppRgb);
                    bmpData = bmp.LockBits(rect, System.Drawing.Imaging.ImageLockMode.ReadWrite, bmp.PixelFormat);
                    ptr = bmpData.Scan0;

                    System.Runtime.InteropServices.Marshal.Copy(rgbValues, 0, ptr, bytes);
                    bmp.UnlockBits(bmpData);

                    return bmp;
                }
                else
                {
                    return null;
                }
            }
            else
            {
                return null;
            }
        }
        //偽彩色圖像處理 SP

        private void button4_Click(object sender, EventArgs e)
        {
            //選取範圍 : 418	149	145	203
            x_st = 418;
            y_st = 149;
            w = 145;
            h = 203;

            reset_picture();
            ImageEnhancement(x_st, y_st, w, h);

            //亮度分布
            draw_x_st = x_st;
            draw_y_st = y_st;
            draw_w = w;
            draw_h = h;

            measure_brightness();
            this.pictureBox1.Invalidate();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            int border = 80;
            x_st = border;
            y_st = border;
            w = W - border * 2;
            h = H - border * 2;

            //選取範圍 : 385	253	186	96
            x_st = 385;
            y_st = 253;
            w = 186;
            h = 96;

            reset_picture();
            ImageEnhancement(x_st, y_st, w, h);

            //亮度分布
            draw_x_st = x_st;
            draw_y_st = y_st;
            draw_w = w;
            draw_h = h;

            measure_brightness();
            this.pictureBox1.Invalidate();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            x_st = 640 / 2;
            y_st = 480 / 2;
            w = 50;
            h = 50;

            reset_picture();

            //修改bitmap1資料, debug ST
            int i;
            int j;
            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {
                    bitmap1.SetPixel(x_st + i, y_st + j, Color.Red);
                    bitmap1.SetPixel(x_st + i, y_st + j, Color.FromArgb(255, 100 + i, 100 + i, 100 + i));
                    //bitmap1.SetPixel(x_st + i, y_st + j, Color.FromArgb(255, 120, 120, 120));
                }
            }

            for (j = 0; j < 5; j++)
            {
                for (i = 0; i < 5; i++)
                {
                    //bitmap1.SetPixel(x_st+w/2 + i, y_st+h/2 + j, Color.FromArgb(255, 130, 130, 130));
                }
            }

            bitmap2 = (Bitmap)bitmap1.Clone();
            pictureBox1.Image = bitmap1;
            pictureBox2.Image = bitmap2;
            //修改bitmap1資料, debug SP

            ImageEnhancement(x_st, y_st, w, h);

            //亮度分布
            draw_x_st = x_st;
            draw_y_st = y_st;
            draw_w = w;
            draw_h = h;

            measure_brightness();
            this.pictureBox1.Invalidate();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            if (cb_modify.Checked == false)
                cb_modify.Checked = true;
            else
                cb_modify.Checked = false;
            x_st = 226;
            y_st = 196;
            w = 206;
            h = 179;

            //ntuh1
            x_st = 124;
            y_st = 177;
            w = 135;
            h = 135;

            reset_picture();
            ImageEnhancement(x_st, y_st, w, h);

            //亮度分布
            draw_x_st = x_st;
            draw_y_st = y_st;
            draw_w = w;
            draw_h = h;

            measure_brightness();
            this.pictureBox1.Invalidate();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //richTextBox1.Text += x_st.ToString() + "\t" + y_st.ToString() + "\t" + w.ToString() + "\t" + h.ToString() + "\n";

            richTextBox1.Text += "bitmap1 :\n";
            find_bitmap_info(bitmap1, x_st, y_st, w, h);

            richTextBox1.Text += "\nbitmap2 :\n";
            find_bitmap_info(bitmap2, x_st, y_st, w, h);
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //黑白
            pictureBox4.SizeMode = PictureBoxSizeMode.CenterImage;
            pictureBox4.Size = new Size(800, 800);
            pictureBox4.Location = new Point(700, 250);
            pictureBox4.BringToFront();

            draw_2d_plot(bitmap2, x_st, y_st, w, h, 0);
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //彩色
            pictureBox4.SizeMode = PictureBoxSizeMode.CenterImage;
            pictureBox4.Size = new Size(800, 800);
            pictureBox4.Location = new Point(700, 250);
            pictureBox4.BringToFront();

            draw_2d_plot(bitmap2, x_st, y_st, w, h, 1);
        }

        private List<Point> Points = new List<Point>();
        private void button11_Click(object sender, EventArgs e)
        {
            //2D plot test

            int W = 800;
            int H = 800;

            pictureBox4.SizeMode = PictureBoxSizeMode.CenterImage;
            pictureBox4.Size = new Size(W, H);
            pictureBox4.Location = new Point(700, 250);
            pictureBox4.BringToFront();

            //10 X 10 array
            int w = 8;
            int h = 6;

            int point_size = 20;    //放大倍率
            if ((W / w) < (H / h))
                point_size = W / w;
            else
                point_size = H / h;

            Pen p = new Pen(Color.Red, 10);
            SolidBrush sb = new SolidBrush(Color.Blue);
            Bitmap bitmap1 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);

            int[,] gray = new int[w, h];

            int i;
            int j;

            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {
                    gray[i, j] = (i * i + j * j + 100) % 256;
                }
            }
            Random r = new Random();
            gray[3, 0] = r.Next(200, 256);
            gray[2, 1] = r.Next(200, 256);
            gray[3, 1] = r.Next(200, 256);
            gray[4, 1] = r.Next(200, 256);
            gray[2, 2] = r.Next(200, 256);
            gray[3, 2] = r.Next(200, 256);
            gray[4, 2] = r.Next(200, 256);
            gray[5, 2] = r.Next(200, 256);
            gray[1, 3] = r.Next(200, 256);
            gray[2, 3] = r.Next(200, 256);
            gray[3, 3] = r.Next(200, 256);
            gray[4, 3] = r.Next(200, 256);
            gray[2, 4] = r.Next(200, 256);
            gray[3, 4] = r.Next(200, 256);
            gray[4, 4] = r.Next(200, 256);
            gray[5, 4] = r.Next(200, 256);
            gray[3, 5] = r.Next(200, 256);
            gray[4, 5] = r.Next(200, 256);

            int[,] gray_new = new int[w, h];

            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {
                    gray_new[i, j] = gray[i, j];

                    if (gray[i, j] >= 200)
                        gray_new[i, j] = 200;
                    else
                        gray_new[i, j] = 0;
                }
            }

            //中間挖空
            int[,] gray_new2 = new int[w, h];
            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {
                    gray_new2[i, j] = gray_new[i, j];

                    //不在邊界的點
                    if ((i > 0) && (i < (w - 1)) && (j > 0) && (j < (h - 1)))
                    {
                        if (gray_new[i, j] < 200)
                            continue;

                        //四鄰皆有者
                        if ((gray_new[i + 1, j] >= 200) && (gray_new[i - 1, j] >= 200) && (gray_new[i, j + 1] >= 200) && (gray_new[i, j - 1] >= 200))
                        {
                            gray_new2[i, j] = 0;
                        }
                    }
                }
            }

            int xx;
            int yy;
            int width = point_size * w;
            int height = point_size * h;

            bitmap1 = new Bitmap(width, height);
            g = Graphics.FromImage(bitmap1);

            byte aa = 255;
            byte rr = 0;
            byte gg = 0;
            byte bb = 0;

            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //設置像素的ＲＧＢ顏色值

                    //黑白
                    rr = (byte)gray_new2[xx / point_size, yy / point_size];
                    gg = (byte)gray_new2[xx / point_size, yy / point_size];
                    bb = (byte)gray_new2[xx / point_size, yy / point_size];
                    bitmap1.SetPixel(xx, yy, Color.FromArgb(aa, rr, gg, bb));
                }
            }
            g.DrawString(w.ToString() + " X " + h.ToString() + ", " + point_size.ToString() + "倍", new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(0, 0));
            pictureBox4.Image = bitmap1;

            find_connected_points(gray_new2);

            richTextBox1.Text += "point array:\n";
            richTextBox1.Text += "len = " + Points.Count.ToString() + "\n";
        }

        void find_connected_points(int[,] array)
        {
            Points.Clear();

            int row = array.Rank;//獲取行數
            int col1 = array.GetLength(1);//獲取指定維中的元 個數，這裡也就是列數了。（1表示的是第二維，0是第一維）
            int col2 = array.GetUpperBound(0) + 1;//獲取指定維度的上限，在 上一個1就是列數
            int num1 = array.Length;//獲取整個二維陣列的長度，即所有元 的個數

            richTextBox1.Text += "row = " + row.ToString() + "\n";
            richTextBox1.Text += "col1 = " + col1.ToString() + "\n";
            richTextBox1.Text += "col2 = " + col2.ToString() + "\n";
            richTextBox1.Text += "num1 = " + num1.ToString() + "\n";

            int total_rows = array.GetUpperBound(0) + 1;
            richTextBox1.Text += "total_rows = " + total_rows.ToString() + "\n";

            int w = array.GetUpperBound(0) + 1;
            int h = array.GetLength(1);
            int i;
            int j;
            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {
                    richTextBox1.Text += array[i, j] + "\t";

                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";

            int i_st = 0;
            int j_st = 0;
            int total_points = 0;
            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {

                    if (array[i, j] >= 200)
                    {
                        total_points++;
                    }
                }
            }
            richTextBox1.Text += "共找到 : " + total_points.ToString() + " 點\n";


            bool flag_got_break = false;
            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {

                    if (array[i, j] >= 200)
                    {
                        richTextBox1.Text += "找到 i = " + i.ToString() + ", j = " + j.ToString() + "\n";
                        i_st = i;
                        j_st = j;
                        flag_got_break = true;
                        break;
                    }


                }
                if (flag_got_break == true)
                    break;
            }
            richTextBox1.Text += "找到起始點 i_st = " + i_st.ToString() + ", j_st = " + j_st.ToString() + "\n";

            int i_next = i_st;
            int j_next = j_st;
            Points.Add(new Point(i_next, j_next));

            for (i = 0; i < total_points; i++)
            {
                i_st = i_next;
                j_st = j_next;
                FindNeighborPoint(array, i_st, j_st, out i_next, out j_next);
                Points.Add(new Point(i_next, j_next));
                richTextBox1.Text += "i_next = " + i_next.ToString() + "\t" + "j_next = " + j_next.ToString() + "\n";
                array[i_next, j_next] = 0;
            }

        }

        void FindNeighborPoint(int[,] array, int i_st, int j_st, out int i_next, out int j_next)
        {
            //int i;
            int len = array.Length;
            i_next = int.MaxValue;
            j_next = int.MinValue;

            int i = 0;
            int j = 0;

            //richTextBox1.Text += "1111 i_st = " + i_st.ToString() + ", j_st = " + j_st.ToString() + "\n";
            //richTextBox1.Text += "2222 i = " + i.ToString() + ", j = " + j.ToString() + "\n";

            int w = array.GetUpperBound(0) + 1;
            int h = array.GetLength(1);

            //richTextBox1.Text += "上";
            i = i_st;
            j = j_st - 1;

            if ((i < 0) || (j < 0) || (i >= w) || (j >= h))
            {

            }
            else if (array[i, j] >= 200)
            {
                richTextBox1.Text += "找到";
                i_next = i;
                j_next = j;
                return;
            }
            //richTextBox1.Text += "\n";

            //richTextBox1.Text += "右上";
            i = i_st + 1;
            j = j_st - 1;
            if ((i < 0) || (j < 0) || (i >= w) || (j >= h))
            {

            }
            else if (array[i, j] >= 200)
            {
                richTextBox1.Text += "找到\n";
                i_next = i;
                j_next = j;
                return;

            }
            //richTextBox1.Text += "\n";

            //richTextBox1.Text += "右";
            i = i_st + 1;
            j = j_st;
            if ((i < 0) || (j < 0) || (i >= w) || (j >= h))
            {

            }
            else if (array[i, j] >= 200)
            {
                richTextBox1.Text += "找到\n";
                i_next = i;
                j_next = j;
                return;

            }
            //richTextBox1.Text += "\n";

            //richTextBox1.Text += "右下";
            i = i_st + 1;
            j = j_st + 1;
            if ((i < 0) || (j < 0) || (i >= w) || (j >= h))
            {

            }
            else if (array[i, j] >= 200)
            {
                richTextBox1.Text += "找到\n";
                i_next = i;
                j_next = j;
                return;

            }
            //richTextBox1.Text += "\n";

            //richTextBox1.Text += "下";
            i = i_st;
            j = j_st + 1;
            if ((i < 0) || (j < 0) || (i >= w) || (j >= h))
            {

            }
            else if (array[i, j] >= 200)
            {
                richTextBox1.Text += "找到\n";
                i_next = i;
                j_next = j;
                return;

            }
            //richTextBox1.Text += "\n";

            //richTextBox1.Text += "左下";
            i = i_st - 1;
            j = j_st + 1;
            if ((i < 0) || (j < 0) || (i >= w) || (j >= h))
            {

            }
            else if (array[i, j] >= 200)
            {
                richTextBox1.Text += "找到\n";
                i_next = i;
                j_next = j;
                return;

            }
            //richTextBox1.Text += "\n";

            //richTextBox1.Text += "左";
            i = i_st - 1;
            j = j_st;
            if ((i < 0) || (j < 0) || (i >= w) || (j >= h))
            {

            }
            else if (array[i, j] >= 200)
            {
                richTextBox1.Text += "找到\n";
                i_next = i;
                j_next = j;
                return;

            }
            //richTextBox1.Text += "\n";

            //richTextBox1.Text += "左上";
            i = i_st - 1;
            j = j_st - 1;
            if ((i < 0) || (j < 0) || (i >= w) || (j >= h))
            {

            }
            else if (array[i, j] >= 200)
            {
                richTextBox1.Text += "找到\n";
                i_next = i;
                j_next = j;
                return;

            }
            //richTextBox1.Text += "\n";
        }

        void find_bitmap_info(Bitmap bmp, int x_st, int y_st, int w, int h)
        {
            //richTextBox1.Text += x_st.ToString() + "\t" + y_st.ToString() + "\t" + w.ToString() + "\t" + h.ToString() + "\n";

            int i;
            int j;
            int Y_max = 0;
            int Y_min = 255;
            Color pt;
            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {
                    pt = bmp.GetPixel(x_st + i, y_st + j);

                    RGB pp = new RGB(pt.R, pt.G, pt.B);
                    YUV yyy = new YUV();
                    yyy = RGBToYUV(pp);

                    int y = (int)Math.Round(yyy.Y); //四捨五入

                    if (y > 255)
                        y = 255;
                    if (y < 0)
                        y = 0;

                    if (Y_max < y)
                        Y_max = y;

                    if (Y_min > y)
                        Y_min = y;

                    //if (j == 10)
                    {
                        //richTextBox1.Text += yyy.Y.ToString() + " ";
                        if ((i % 16) == 15)
                        {
                            //richTextBox1.Text += "\n";
                        }
                    }
                    //richTextBox1.Text += "\n";

                    if (y < 100)
                    {
                        //bmp.SetPixel(x_st + i, y_st + j, Color.Red);
                    }
                }
            }
            //richTextBox1.Text += "\n";

            if (Y_max > 255)
                Y_max = 255;
            if (Y_min < 0)
                Y_min = 0;

            brightness_max = Y_max;
            brightness_min = Y_min;

            richTextBox1.Text += "Y_max = " + Y_max.ToString() + "\tY_min = " + Y_min.ToString() + "\n";
        }

        private void button12_Click(object sender, EventArgs e)
        {
            bitmap2.Save("bbbbb.bmp", ImageFormat.Bmp);
        }

        int[] r_data = new int[256];
        int[] g_data = new int[256];
        int[] b_data = new int[256];

        private void button13_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";

            int border = 60;
            x_st = border;
            y_st = border;
            w = W - border * 2;
            h = H - border * 2;


            x_st = 220;
            y_st = 30;
            w = 250;
            h = 220;

            x_st = 240;
            y_st = 10;
            w = 220;
            h = 250;


            int i;
            int j;
            Color pt;
            int total_points = 0;
            double total_brightness = 0;

            brightness_data = new int[256];
            r_data = new int[256];
            g_data = new int[256];
            b_data = new int[256];

            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {
                    pt = bitmap1.GetPixel(x_st + i, y_st + j);
                    r_data[pt.R]++;
                    g_data[pt.G]++;
                    b_data[pt.B]++;

                    RGB pp = new RGB(pt.R, pt.G, pt.B);
                    YUV yyy = new YUV();
                    yyy = RGBToYUV(pp);

                    total_brightness += yyy.Y;

                    int y = (int)Math.Round(yyy.Y); //四捨五入

                    if (y > 255)
                        y = 255;
                    if (y < 0)
                        y = 0;

                    brightness_data[y]++;
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


                    //b = new SolidBrush(Color.FromArgb(255, rgb_array[i, 0], rgb_array[i, 1], rgb_array[i, 2]));

                    bitmap1.SetPixel(x_st + i, y_st + j, Color.FromArgb(255, rgb_array[y / 4, 0], rgb_array[y / 4, 1], rgb_array[y / 4, 2]));


                }
                //richTextBox1.Text += "\n";
            }
            //richTextBox1.Text += "\n";
            richTextBox1.Text += "共有 " + total_points.ToString() + " 個點\n";
            richTextBox1.Text += "總亮度 " + total_brightness.ToString() + "\n";
            richTextBox1.Text += "平均亮度 " + (total_brightness / total_points).ToString() + "\n";


            int most = 0;
            int brightness_st = 0;
            int brightness_sp = 0;
            int r_st = 0;
            int r_sp = 0;
            int g_st = 0;
            int g_sp = 0;
            int b_st = 0;
            int b_sp = 0;

            for (i = 0; i < 256; i++)
            {
                total_points += brightness_data[i];
                total_brightness += i * brightness_data[i];
                //richTextBox1.Text += brightness_data[i].ToString() + " ";
                if (brightness_data[i] > most)
                    most = brightness_data[i];
                /*
                if (brightness_data[i] == 0)
                    brightness_data[i] = 5;
                */
                if ((brightness_data[i] > 0) && (brightness_st == 0))
                {
                    brightness_st = i;
                }
                if (brightness_data[i] > 0)
                {
                    brightness_sp = i;
                }


                if ((r_data[i] > 0) && (r_st == 0))
                {
                    r_st = i;
                }
                if (r_data[i] > 0)
                {
                    r_sp = i;
                }



                if ((g_data[i] > 0) && (g_st == 0))
                {
                    g_st = i;
                }
                if (g_data[i] > 0)
                {
                    g_sp = i;
                }



                if ((b_data[i] > 0) && (b_st == 0))
                {
                    b_st = i;
                }
                if (b_data[i] > 0)
                {
                    b_sp = i;
                }
            }

            richTextBox1.Text += "\n最多 " + most.ToString() + "\n";

            richTextBox1.Text += "亮度範圍 : " + brightness_st.ToString() + " 到 " + brightness_sp.ToString() + "\n";
            richTextBox1.Text += "亮差 : " + (brightness_sp - brightness_st).ToString() + "\n";

            richTextBox1.Text += "R範圍 : " + r_st.ToString() + " 到 " + r_sp.ToString() + "\n";
            richTextBox1.Text += "R差 : " + (r_sp - r_st).ToString() + "\n";


            richTextBox1.Text += "G範圍 : " + g_st.ToString() + " 到 " + g_sp.ToString() + "\n";
            richTextBox1.Text += "G差 : " + (g_sp - g_st).ToString() + "\n";


            richTextBox1.Text += "B範圍 : " + b_st.ToString() + " 到 " + b_sp.ToString() + "\n";
            richTextBox1.Text += "B差 : " + (b_sp - b_st).ToString() + "\n";


            richTextBox1.Text += "共有 " + total_points.ToString() + " 個點\n";
            richTextBox1.Text += "總亮度 " + total_brightness.ToString() + "\n";
            richTextBox1.Text += "平均亮度 " + (total_brightness / total_points).ToString() + "\n";

            Graphics g = Graphics.FromImage(bitmap1);

            Brush b;
            //int i;
            int N = rgb_array.Length / 3;
            int hh = 4;

            border = 10;

            for (i = 0; i < N; i++)
            {
                b = new SolidBrush(Color.FromArgb(255, rgb_array[63 - i, 0], rgb_array[63 - i, 1], rgb_array[63 - i, 2]));
                //rgb_array
                //g.FillRectangle(b, w / 10, i * hh + h/10, w / 10 * 8, hh);
                g.FillRectangle(b, 550, i * hh + border, 80, hh);
            }


            pictureBox1.Image = bitmap1;



        }

        private void button14_Click(object sender, EventArgs e)
        {
            int W = 640;
            int H = 480;
            bitmap1 = new Bitmap(W, H);

            int i;
            int j;
            for (j = 0; j < H; j++)
            {
                if (j < H)
                {
                    if (j < H / 2)
                    {
                        for (i = 0; i < W; i++)
                        {
                            bitmap1.SetPixel(i, j, Color.Red);
                        }
                    }
                    else
                    {
                        for (i = 0; i < W; i++)
                        {
                            bitmap1.SetPixel(i, j, Color.FromArgb(255, 164, 0, 39));



                        }
                    }
                }
            }

            pictureBox1.Image = bitmap1;
            pictureBox2.Image = bitmap1;

            bitmap2 = bitmap1;

            /*
            Random r = new Random();
            for (i = 0; i < 100; i++)
            {
                byte R = (byte)r.Next(0, 256);
                byte G = (byte)r.Next(0, 256);
                byte B = (byte)r.Next(0, 256);
                richTextBox1.Text += "前 : " + R.ToString() + ", " + G.ToString() + ", " + B.ToString() + "\n";

                RGB pp = new RGB(R, G, B);
                YUV yyy = new YUV();
                yyy = RGBToYUV(pp);

                YUV yyy2 = new YUV(yyy.Y, yyy.U, yyy.V);
                RGB rrr = new RGB();
                rrr = YUVToRGB(yyy2);


                int sum = ((int)rrr.R - (int)R) * ((int)rrr.R - (int)R) + ((int)rrr.G - (int)G) * ((int)rrr.G - (int)G) + ((int)rrr.B - (int)B) * ((int)rrr.B - (int)B);

                richTextBox1.Text += "後 : " + rrr.R.ToString() + ", " + rrr.G.ToString() + ", " + rrr.B.ToString() + ", 差 : " + sum.ToString() + "\n";
                delay(10);
            }
            */

            Random r = new Random();
            byte R = 255;
            byte G = 0;
            byte B = 0;
            richTextBox1.Text += "前 : " + R.ToString() + ", " + G.ToString() + ", " + B.ToString() + "\n";

            RGB pp = new RGB(R, G, B);
            YUV yyy = new YUV();
            yyy = RGBToYUV(pp);

            YUV yyy2 = new YUV(yyy.Y, yyy.U, yyy.V);
            RGB rrr = new RGB();
            rrr = YUVToRGB(yyy2);


            int sum = ((int)rrr.R - (int)R) * ((int)rrr.R - (int)R) + ((int)rrr.G - (int)G) * ((int)rrr.G - (int)G) + ((int)rrr.B - (int)B) * ((int)rrr.B - (int)B);

            richTextBox1.Text += "後 : " + rrr.R.ToString() + ", " + rrr.G.ToString() + ", " + rrr.B.ToString() + ", 差 : " + sum.ToString() + "\n";


            YUV yyy3 = new YUV(200, yyy.U, yyy.V);
            rrr = YUVToRGB(yyy3);

            sum = ((int)rrr.R - (int)R) * ((int)rrr.R - (int)R) + ((int)rrr.G - (int)G) * ((int)rrr.G - (int)G) + ((int)rrr.B - (int)B) * ((int)rrr.B - (int)B);
            richTextBox1.Text += "後 : " + rrr.R.ToString() + ", " + rrr.G.ToString() + ", " + rrr.B.ToString() + ", 差 : " + sum.ToString() + "\n";



            R = 255;
            G = 123;
            B = 123;
            richTextBox1.Text += "前2 : " + R.ToString() + ", " + G.ToString() + ", " + B.ToString() + "\n";
            pp = new RGB(R, G, B);
            yyy = new YUV();
            yyy = RGBToYUV(pp);


            richTextBox1.Text += "得到 : " + yyy.Y.ToString() + ", " + yyy.U.ToString() + ", " + yyy.V.ToString() + "\n";


        }


        bool flag_pictureBox1_mouse_down = false;
        int pictureBox1_position_x_old = 0;
        int pictureBox1_position_y_old = 0;

        int draw_x_st = 0;
        int draw_y_st = 0;
        int draw_w = 0;
        int draw_h = 0;

        // Return a Rectangle with these points as corners.
        private Rectangle MakeRectangle(int x0, int y0, int x1, int y1)
        {
            return new Rectangle(Math.Min(x0, x1), Math.Min(y0, y1), Math.Abs(x0 - x1), Math.Abs(y0 - y1));
        }

        private Rectangle MakeRectangle(Point pt1, Point pt2)
        {
            return new Rectangle(Math.Min(pt1.X, pt2.X), Math.Min(pt1.Y, pt2.Y), Math.Abs(pt1.X - pt2.X), Math.Abs(pt1.Y - pt2.Y));
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            //bitmap1 = (Bitmap)Image.FromFile(filename1);	//Image.FromFile出來的是Image格式
            //bitmap2 = (Bitmap)bitmap1.Clone();

            flag_pictureBox1_mouse_down = true;
            pt_st = e.Location; //起始點座標

            //richTextBox1.Text += "Down : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
            pictureBox1_position_x_old = e.X;
            pictureBox1_position_y_old = e.Y;

            nud_w.Value = 0;
            nud_h.Value = 0;
            nud_x_st.Value = 0;
            nud_y_st.Value = 0;
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_pictureBox1_mouse_down == true)
            {
                pt_sp = e.Location; //終點座標

                SelectionRectangle = MakeRectangle(pt_st, pt_sp);

                //richTextBox1.Text += "Up : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
                int dx = e.X - pictureBox1_position_x_old;
                int dy = e.Y - pictureBox1_position_y_old;

                if (dx > 0)
                {
                    draw_x_st = pictureBox1_position_x_old;
                    draw_w = dx;
                }
                else
                {
                    draw_x_st = e.X;
                    draw_w = -dx;
                }

                if (dy > 0)
                {
                    draw_y_st = pictureBox1_position_y_old;
                    draw_h = dy;
                }
                else
                {
                    draw_y_st = e.Y;
                    draw_h = -dy;
                }

                this.pictureBox1.Invalidate();
                //richTextBox1.Text += "dx, dy : (" + dx.ToString() + ", " + dy.ToString() + ")\n";
                //pictureBox1.Location = new Point(pictureBox1.Location.X + dx, pictureBox1.Location.Y + dy);

                nud_x_st.Value = SelectionRectangle.X;
                nud_y_st.Value = SelectionRectangle.Y;
                nud_w.Value = SelectionRectangle.Width;
                nud_h.Value = SelectionRectangle.Height;
            }
            else if (cb_magnify.Checked == true)
            {
                int r = 50;
                int R = 200;

                //由 r X r 放大到 R X R
                try
                {
                    Graphics g = pictureBox1.CreateGraphics();
                    Rectangle rect1 = new Rectangle(e.X - r / 2, e.Y - r / 2, r, r); //要放大的區域 
                    Rectangle rect2 = new Rectangle(e.X - R / 2, e.Y - R / 2, R, R);
                    g.DrawImage(bitmap1, 0, 0, bitmap1.Width, bitmap1.Height);
                    g.DrawImage(bitmap1, rect2, rect1, GraphicsUnit.Pixel);
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }
        }

        private void pictureBox2_MouseMove(object sender, MouseEventArgs e)
        {
            if (cb_magnify.Checked == true)
            {
                int r = 50;
                int R = 200;

                //由 r X r 放大到 R X R
                try
                {
                    Graphics g = pictureBox2.CreateGraphics();
                    Rectangle rect1 = new Rectangle(e.X - r / 2, e.Y - r / 2, r, r); //要放大的區域 
                    Rectangle rect2 = new Rectangle(e.X - R / 2, e.Y - R / 2, R, R);
                    g.DrawImage(bitmap2, 0, 0, bitmap2.Width, bitmap2.Height);
                    g.DrawImage(bitmap2, rect2, rect1, GraphicsUnit.Pixel);
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            flag_pictureBox1_mouse_down = false;
            //richTextBox1.Text += "Up : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";

            if ((draw_x_st < 0) || (draw_x_st >= W))
                return;
            if ((draw_y_st < 0) || (draw_y_st >= H))
                return;
            if ((draw_w <= 0) || (draw_w > W))
                return;
            if ((draw_h <= 0) || (draw_h > H))
                return;
            if (((draw_x_st + draw_w) > W) || ((draw_y_st + draw_h) > H))
                return;

            flag_do_enhancement = true;

            nud_x_st.Value = SelectionRectangle.X;
            nud_y_st.Value = SelectionRectangle.Y;
            nud_w.Value = SelectionRectangle.Width;
            nud_h.Value = SelectionRectangle.Height;

            richTextBox1.Text += "\n選取範圍 : " + draw_x_st.ToString() + "\t" + draw_y_st.ToString() + "\t" + draw_w.ToString() + "\t" + draw_h.ToString() + "\n";
            draw_enhanced_image(bitmap2, draw_x_st, draw_y_st, draw_w, draw_h);

            measure_brightness();
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            //richTextBox1.Text += draw_x_st.ToString() + "\t" + draw_y_st.ToString() + "\t" + draw_w.ToString() + "\t" + draw_h.ToString() + "\n";
            //e.Graphics.DrawRectangle(new Pen(Color.Blue, 3), draw_x_st, draw_y_st, draw_w, draw_h);
            e.Graphics.DrawRectangle(new Pen(Color.Blue, 3), draw_x_st - 1, draw_y_st - 1, draw_w + 2, draw_h + 2);

            e.Graphics.DrawString("原圖", new Font("標楷體", 30), new SolidBrush(Color.Red), new PointF(0, 0));
        }

        int ccc = 0;
        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {
            //richTextBox1.Text += draw_x_st.ToString() + "\t" + draw_y_st.ToString() + "\t" + draw_w.ToString() + "\t" + draw_h.ToString() + "\n";
            //e.Graphics.DrawRectangle(new Pen(Color.Blue, 3), draw_x_st, draw_y_st, draw_w, draw_h);
            e.Graphics.DrawRectangle(new Pen(Color.Blue, 3), draw_x_st - 1, draw_y_st - 1, draw_w + 2, draw_h + 2);

            //e.Graphics.DrawString("原圖", new Font("標楷體", 30), new SolidBrush(Color.Red), new PointF(0, 0));

            e.Graphics.DrawString((ccc++).ToString(), new Font("標楷體", 30), new SolidBrush(Color.Red), new PointF(0, 0));

            //mouseup

            /*
            if ((flag_webcam_ok == true)&&(flag_do_enhancement==true))
            {
                draw_enhanced_image(bitmap2, draw_x_st, draw_y_st, draw_w, draw_h);

                measure_brightness();
                flag_do_enhancement = false;
            }
            */
        }

        private void pictureBox3a_Paint(object sender, PaintEventArgs e)
        {
            if ((draw_w > 640 / 2) || (draw_h > 480 / 2))
            {
                e.Graphics.DrawString("選取範圍太大", new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(0, 0));
            }
            else
            {
                e.Graphics.DrawString("兩倍 " + draw_w.ToString() + " X " + draw_h.ToString(), new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(0, 0));
            }
        }

        private void pictureBox3b_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.DrawString("滿框", new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(0, 0));
        }

        void get_brigheness_data(Bitmap bitmap1, int x_st, int y_st, int w, int h)
        {
            brightness_data = new int[256];

            int i;
            int j;
            Color pt;
            int total_points = 0;
            double total_brightness = 0;

            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {
                    pt = bitmap1.GetPixel(x_st + i, y_st + j);

                    RGB pp = new RGB(pt.R, pt.G, pt.B);
                    YUV yyy = new YUV();
                    yyy = RGBToYUV(pp);

                    total_brightness += yyy.Y;

                    int y = (int)Math.Round(yyy.Y); //四捨五入

                    if (y > 255)
                        y = 255;
                    if (y < 0)
                        y = 0;

                    brightness_data[y]++;
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

        void measure_brightness()
        {
            x_st = draw_x_st;
            y_st = draw_y_st;
            w = draw_w;
            h = draw_h;

            //量測原圖 bitmap1

            get_brigheness_data(bitmap1, x_st, y_st, w, h);

            int i;
            int most = 0;
            int brightness_st = 0;
            int brightness_sp = 0;
            int total_points = 0;
            double total_brightness = 0;
            for (i = 0; i < 256; i++)
            {
                total_points += brightness_data[i];
                total_brightness += i * brightness_data[i];
                //richTextBox1.Text += brightness_data[i].ToString() + " ";
                if (brightness_data[i] > most)
                    most = brightness_data[i];
                /*
                if (brightness_data[i] == 0)
                    brightness_data[i] = 5;
                */
                if ((brightness_data[i] > 0) && (brightness_st == 0))
                {
                    brightness_st = i;
                }
                if (brightness_data[i] > 0)
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
                    pt = bitmap1.GetPixel(x_st + i, y_st + j);

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
                g4.FillRectangle(Brushes.Red, i * 2, hh2 - (float)(brightness_data[i] * ratio), 2, (float)(brightness_data[i] * ratio));
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
            FindYMaxYMin(brightness_data, out y_min, out y_max);
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
            bool flag_modify_boundary_sp = true;
            if ((brightness_sp - average_brightness) < sd * rr_sp)
            {
                g4.DrawString("YMax太近", new Font("標楷體", 18), new SolidBrush(Color.Navy), 512, 10 + dy * 8);
                flag_modify_boundary_sp = false;
            }

            float rr_st = 3.0f;
            bool flag_modify_boundary_st = true;
            if ((average_brightness - brightness_st) < sd * rr_st)
            {
                g4.DrawString("YMin太近", new Font("標楷體", 18), new SolidBrush(Color.Navy), 512 + 100, 10 + dy * 8);
                flag_modify_boundary_st = false;
            }

            g4.DrawString(((int)Math.Round((average_brightness - sd * rr_st))).ToString() + " " +
                average_brightness.ToString() + " " +
                ((int)Math.Round((average_brightness + sd * rr_sp))).ToString(), new Font("標楷體", 18), new SolidBrush(Color.Navy), 512, 10 + dy * 9);

            if ((flag_modify_boundary_sp == false) || (cb_modify.Checked == false))
            {
                g4.DrawString("亮場未調整", new Font("標楷體", 13), new SolidBrush(Color.Red), 512 + 105, 10 + dy * 10);
            }

            if ((flag_modify_boundary_st == false) || (cb_modify.Checked == false))
            {
                g4.DrawString("暗場未調整", new Font("標楷體", 13), new SolidBrush(Color.Red), 512, 10 + dy * 10);
            }

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
            //printArrayData(brightness_data);
            int mm = brightness_data.Max();
            //richTextBox1.Text += "mm = " + mm.ToString() + "\n";
            float rr = mm / (float)width;
            for (i = 0; i < 256; i++)
            {
                g4.DrawLine(Pens.Red, 750, hh2 - i, 750 + (int)(brightness_data[i] / rr), hh2 - i);

            }

            Point[] curvePoints = new Point[256];    //一維陣列內有 256 個Point
            for (i = 0; i < 256; i++)
            {
                curvePoints[i].X = 750 + (int)(brightness_data[i] / rr);
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





            //量測修改過的圖 bitmap2

            get_brigheness_data(bitmap2, x_st, y_st, w, h);

            most = 0;
            brightness_st = 0;
            brightness_sp = 0;
            total_points = 0;
            total_brightness = 0;
            for (i = 0; i < 256; i++)
            {
                total_points += brightness_data[i];
                total_brightness += i * brightness_data[i];
                //richTextBox1.Text += brightness_data[i].ToString() + " ";
                if (brightness_data[i] > most)
                    most = brightness_data[i];
                /*
                if (brightness_data[i] == 0)
                    brightness_data[i] = 5;
                */
                if ((brightness_data[i] > 0) && (brightness_st == 0))
                {
                    brightness_st = i;
                }
                if (brightness_data[i] > 0)
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
            sd_num = new double[total_points];

            index = 0;

            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {
                    pt = bitmap2.GetPixel(x_st + i, y_st + j);

                    RGB pp = new RGB(pt.R, pt.G, pt.B);
                    YUV yyy = new YUV();
                    yyy = RGBToYUV(pp);

                    sd_num[index] = yyy.Y;
                    index++;
                }
            }

            sd = SD(sd_num);
            //richTextBox1.Text += "標準差 " + sd.ToString("F2") + "\n";
            brightness_sd = sd;

            average_brightness = (int)Math.Round(total_brightness / total_points); //四捨五入
            //richTextBox1.Text += "平均亮度 " + average_brightness.ToString() + "\n";
            brightness_avg = average_brightness;

            ww = 480 * 2 - 10;
            hh1 = 300;
            hh2 = 256;
            Bitmap bmp5 = new Bitmap(ww, hh1);
            Graphics g5 = Graphics.FromImage(bmp5);
            g5.Clear(Color.Pink);
            p = new Pen(Color.Blue, 2);

            ratio = 0;
            ratio = (double)hh2 / most;
            richTextBox1.Text += "ratio = " + ratio.ToString() + "\n";

            for (i = 0; i < 256; i++)
            {
                g5.FillRectangle(Brushes.Red, i * 2, hh2 - (float)(brightness_data[i] * ratio), 2, (float)(brightness_data[i] * ratio));
            }

            g5.DrawRectangle(p, 0 + 1, 0 + 1, ww - 2, hh1 - 2);
            g5.DrawRectangle(p, 0 + 1, 0 + 1, ww - 2, hh2 - 2);

            p = new Pen(Color.Yellow, 3);
            g5.DrawLine(p, average_brightness * 2, 0, average_brightness * 2, hh2 - 2);
            g5.DrawLine(p, brightness_st * 2, 0, brightness_st * 2, hh2 - 2);
            g5.DrawLine(p, brightness_sp * 2, 0, brightness_sp * 2, hh2 - 2);

            b = new SolidBrush(Color.FromArgb(33, Color.RoyalBlue.R, Color.RoyalBlue.G, Color.RoyalBlue.B));

            g5.FillRectangle(b, min * 2, 0, (max - min) * 2, hh1);

            f = new Font("標楷體", 20);

            if ((min >= 0) && (min <= 103))
            {
                g5.DrawString(min.ToString(), f, new SolidBrush(Color.Blue), new PointF(min * 2, hh2));
            }
            else if (min < 0)
            {
                g5.DrawString(min.ToString(), f, new SolidBrush(Color.Blue), new PointF(0, hh2));
            }
            else
            {
                g5.DrawString(min.ToString(), f, new SolidBrush(Color.Blue), new PointF(103 * 2, hh2));
            }

            if ((max <= 255) && (max >= 152))
            {
                g5.DrawString(max.ToString(), f, new SolidBrush(Color.Blue), new PointF(max * 2 - 50, hh2));

                g5.DrawString(brightness_st.ToString(), f, new SolidBrush(Color.Yellow), new PointF(brightness_st * 2 - 25, hh2));
                g5.DrawString(brightness_sp.ToString(), f, new SolidBrush(Color.Yellow), new PointF(brightness_sp * 2 - 25, hh2));
                g5.DrawString(average_brightness.ToString(), f, new SolidBrush(Color.Yellow), new PointF(average_brightness * 2 - 25, hh2));
            }
            else if (max > 255)
            {
                g5.DrawString(max.ToString(), f, new SolidBrush(Color.Blue), new PointF(512 - 50, hh2));
            }
            else
            {
                g5.DrawString(max.ToString(), f, new SolidBrush(Color.Blue), new PointF(152 * 2 - 50, hh2));
            }


            width = 40;
            b = new SolidBrush(Color.FromArgb(30, Color.Lime.R, Color.Lime.G, Color.Lime.B));
            g5.FillRectangle(b, 750, 0, width, 256);
            g5.FillRectangle(b, 800, 0, width, 256);
            g5.FillRectangle(b, 850, 0, width, 256);

            g5.DrawRectangle(Pens.Red, 750, hh2 - brightness_sp, width, brightness_sp - brightness_st);


            //richTextBox1.Text += "brightness data :\n";
            //printArrayData(brightness_data);
            mm = brightness_data.Max();
            //richTextBox1.Text += "mm = " + mm.ToString() + "\n";
            rr = mm / (float)width;
            for (i = 0; i < 256; i++)
            {
                g5.DrawLine(Pens.Red, 750, hh2 - i, 750 + (int)(brightness_data[i] / rr), hh2 - i);

            }

            curvePoints = new Point[256];    //一維陣列內有 256 個Point
            for (i = 0; i < 256; i++)
            {
                curvePoints[i].X = 750 + (int)(brightness_data[i] / rr);
                curvePoints[i].Y = hh2 - i;
            }
            // Draw lines between original points to screen.
            g5.DrawLines(Pens.Yellow, curvePoints);   //畫直線
            // Draw curve to screen.
            //g5.DrawCurve(Pens.Yellow, curvePoints); //畫曲線


            g4.DrawImage(bmp5, 0, 300 + 50, bmp5.Width, bmp5.Height);

            pictureBox4.Image = bmp4;
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

        void draw_2d_plot(Bitmap bmp, int x_st, int y_st, int w, int h, int type)
        {
            int pb5_width = 800;
            int pb5_height = 800;

            if ((draw_x_st < 0) || (draw_x_st >= pb5_width))
                return;
            if ((draw_y_st < 0) || (draw_y_st >= pb5_height))
                return;
            if ((draw_w <= 0) || (draw_w > pb5_width))
                return;
            if ((draw_h <= 0) || (draw_h > pb5_height))
                return;
            if (((draw_x_st + draw_w) > pb5_width) || ((draw_y_st + draw_h) > pb5_height))
                return;

            Graphics g;
            Bitmap bitmap1;

            if (w > 400)
            {
                bitmap1 = new Bitmap(pictureBox4.Width, pictureBox4.Height);

                g = Graphics.FromImage(bitmap1);
                g.DrawString("選取範圍太大", new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(0, 0));
                pictureBox4.Image = bitmap1;
                return;
            }

            int point_size = 20;    //放大倍率

            if ((pb5_width / w) < (pb5_height / h))
                point_size = pb5_width / w;
            else
                point_size = pb5_height / h;

            Pen p = new Pen(Color.Red, 10);
            SolidBrush sb = new SolidBrush(Color.Blue);

            int W = pictureBox4.ClientSize.Width;
            int H = pictureBox4.ClientSize.Height;

            bitmap1 = new Bitmap(W, H);
            g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);

            int[,] gray = new int[w, h];

            int i;
            int j;
            int Y_max = 0;
            int Y_min = 255;
            Color pt;

            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {
                    pt = bmp.GetPixel(x_st + i, y_st + j);

                    RGB pp = new RGB(pt.R, pt.G, pt.B);
                    YUV yyy = new YUV();
                    yyy = RGBToYUV(pp);

                    int y = (int)Math.Round(yyy.Y); //四捨五入

                    if (y > 255)
                        y = 255;
                    if (y < 0)
                        y = 0;

                    gray[i, j] = y;

                    if (Y_max < y)
                        Y_max = y;

                    if (Y_min > y)
                        Y_min = y;
                }
            }

            if (Y_max > 255)
                Y_max = 255;
            if (Y_min < 0)
                Y_min = 0;

            brightness_max = Y_max;
            brightness_min = Y_min;

            richTextBox1.Text += "M = " + Y_max.ToString() + "\tm = " + Y_min.ToString() + "\n";

            int xx;
            int yy;
            int width = point_size * w;
            int height = point_size * h;

            bitmap1 = new Bitmap(width, height);
            g = Graphics.FromImage(bitmap1);

            byte aa = 255;
            byte rr = 0;
            byte gg = 0;
            byte bb = 0;

            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //設置像素的ＲＧＢ顏色值

                    if (type == 0)
                    {
                        //黑白
                        rr = (byte)gray[xx / point_size, yy / point_size];
                        gg = (byte)gray[xx / point_size, yy / point_size];
                        bb = (byte)gray[xx / point_size, yy / point_size];
                        bitmap1.SetPixel(xx, yy, Color.FromArgb(aa, rr, gg, bb));
                    }
                    else
                    {
                        //彩色
                        pt = bmp.GetPixel(x_st + xx / point_size, y_st + yy / point_size);
                        bitmap1.SetPixel(xx, yy, Color.FromArgb(aa, pt.R, pt.G, pt.B));
                    }
                }
            }
            g.DrawString(w.ToString() + " X " + h.ToString() + ", " + point_size.ToString() + "倍", new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(0, 0));
            pictureBox4.Image = bitmap1;
        }

        void printArrayData(int[] array)
        {
            int i;
            int len = array.Length;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += array[i].ToString("D3") + " ";
                if ((i % 24) == 23)
                {
                    richTextBox1.Text += "\n";
                }
            }
            richTextBox1.Text += "\n";
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

            RGB pp = new RGB(cl.R, cl.G, cl.B);
            YUV yyy = new YUV();
            yyy = RGBToYUV(pp);

            int y = (int)Math.Round(yyy.Y); //四捨五入

            if (y > 255)
                y = 255;
            if (y < 0)
                y = 0;

            lb_brightness.Text = y.ToString();
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

        private void bt_apply_Click(object sender, EventArgs e)
        {
            x_st = (int)nud_x_st.Value;
            y_st = (int)nud_y_st.Value;
            w = (int)nud_w.Value;
            h = (int)nud_h.Value;

            if ((x_st < 0) || (y_st < 0) || (w <= 0) || (h <= 0))
            {
                richTextBox1.Text += "選取位置錯誤\n";
                return;
            }

            reset_picture();
            ImageEnhancement(x_st, y_st, w, h);

            //亮度分布
            draw_x_st = x_st;
            draw_y_st = y_st;
            draw_w = w;
            draw_h = h;

            measure_brightness();
            this.pictureBox1.Invalidate();
        }

        void Start_Webcam()
        {
            //richTextBox1.Text += "重新抓取USB影像\t";

            int camera_index = 0;
            USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice); //枚舉所有視頻輸入設備

            int webcam_count = USBWebcams.Count;
            richTextBox1.Text += "找到 " + webcam_count.ToString() + " 台WebCam\n";

            if (webcam_count > 0)  // The quantity of WebCam must be more than 0.
            {
                flag_webcam_ok = false;
                for (camera_index = 0; camera_index < webcam_count; camera_index++)
                {
                    richTextBox1.Text += "\ncamera " + camera_index.ToString() + "\t";
                    richTextBox1.Text += "name : " + USBWebcams[camera_index].Name + "\n";

                    if (USBWebcams[camera_index].Name.Contains("Virtual"))
                    {
                        richTextBox1.Text += "跳過 Virtual\t" + USBWebcams[camera_index].Name + "\n";
                        continue;
                    }

                    if (USBWebcams[camera_index].Name == "InsightEyes")
                    {
                        richTextBox1.Text += "找到 InsightEyes 在 index = " + camera_index.ToString() + "\n";
                        flag_webcam_ok = true;
                        break;
                    }
                }

                if (flag_webcam_ok == true)
                {
                    Cam = new VideoCaptureDevice(USBWebcams[camera_index].MonikerString);  //實例化對象
                    Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);
                    Cam.Start();   // WebCam starts capturing images.
                    //richTextBox1.Text += "有影像裝置\n";

                    Cam.VideoResolution = Cam.VideoCapabilities[camera_index];

                    string webcam_name = string.Empty;

                    int ww;
                    int hh;
                    ww = Cam.VideoCapabilities[camera_index].FrameSize.Width;
                    hh = Cam.VideoCapabilities[camera_index].FrameSize.Height;

                    webcam_name = USBWebcams[camera_index].Name + " " + Cam.VideoCapabilities[camera_index].FrameSize.Width.ToString() + " X " + Cam.VideoCapabilities[camera_index].FrameSize.Height.ToString() + " @ " + Cam.VideoCapabilities[camera_index].AverageFrameRate.ToString() + " Hz";
                    richTextBox1.Text += webcam_name + "\n";
                    richTextBox1.Text += "啟動時間 : " + DateTime.Now.ToString() + "\n";
                    webcam_start_time = DateTime.Now;
                }
                else
                {
                    richTextBox1.Text += "找不到裝置\n";
                }
            }
            else
            {
                richTextBox1.Text += "無影像裝置\n";
            }
        }

        void Stop_Webcam()
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

        int frame_count = 0;        //計算fps用
        //int frame_count_old = 0;    //計算fps用
        DateTime dt_old = DateTime.Now;

        Graphics gc;    //for camera
        public Bitmap bm = null;
        //自定義函數, 捕獲每一幀圖像並顯示
        void Cam_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            frame_count++;
            try
            {
                //pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();
                bm = (Bitmap)eventArgs.Frame.Clone();
                //pictureBox1.Image = bm;
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }

            try
            {
                gc = Graphics.FromImage(bm);
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                GC.Collect();       //回收資源
                return;
            }

            int w;
            int h;
            try
            {
                w = bm.Width;
                h = bm.Height;
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                GC.Collect();       //回收資源
                return;
            }

            /*
            if (rb2.Checked == false)
            {
                SolidBrush sb = new SolidBrush(Color.Black);
                Point[] points = new Point[3];
                int dd = 90;
                points[0] = new Point(0, 0);
                points[1] = new Point(dd, 0);
                points[2] = new Point(0, dd);
                gc.FillPolygon(sb, points);

                points[0] = new Point(640 - dd, 0);
                points[1] = new Point(640, 0);
                points[2] = new Point(640, dd);
                gc.FillPolygon(sb, points);

                points[0] = new Point(0, 480);
                points[1] = new Point(0, 480 - dd);
                points[2] = new Point(dd, 480);
                gc.FillPolygon(sb, points);

                points[0] = new Point(640 - dd, 480);
                points[1] = new Point(640, 480);
                points[2] = new Point(640, 480 - dd);
                gc.FillPolygon(sb, points);
            }
            */

            try
            {
                pictureBox1.Image = bm;
                //pictureBox2.Image = bm;
                bitmap1 = (Bitmap)bm.Clone();
                //bitmap2 = (Bitmap)bm.Clone();
                //flag_do_enhancement = true;
                //pictureBox2.Invalidate();
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
            GC.Collect();       //回收資源
        }

        //delay 10000 約 10秒
        //C# 不lag的延遲時間
        private void delay(int delay_milliseconds)
        {
            delay_milliseconds *= 2;
            DateTime time_before = DateTime.Now;
            while (((TimeSpan)(DateTime.Now - time_before)).TotalMilliseconds < delay_milliseconds)
            {
                Application.DoEvents();
            }
        }

        private void timer_enhancement_Tick(object sender, EventArgs e)
        {
            if (flag_webcam_ok == false)
                return;

            if (bm == null)
                return;

            try
            {
                bitmap2 = (Bitmap)bm.Clone();

                if (flag_do_enhancement == true)
                {
                    draw_enhanced_image(bitmap2, draw_x_st, draw_y_st, draw_w, draw_h);

                    measure_brightness();

                    //pictureBox2.Image = bitmap2;
                    //pictureBox2.Invalidate();
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
            GC.Collect();       //回收資源
        }

    }
}
