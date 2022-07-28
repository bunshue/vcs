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

namespace vcs_PictureEnhance_YUV
{
    public partial class Form1 : Form
    {
        string filename1 = @"C:\______test_files\ims01.bmp";
        //string filename1 = @"C:\______test_files\color1.bmp";
        //string filename2 = @"C:\______test_files\color2.bmp";

        Bitmap bitmap1; //原圖
        Bitmap bitmap2; //從原圖修改過的

        public Point firstPoint = new Point(0, 0);  //鼠標第一點 
        public Point secondPoint = new Point(0, 0);  //鼠標第二點 
        public bool begin = false;   //是否開始畫矩形 

        private int W = 0;  //原圖的寬
        private int H = 0;  //原圖的高
        private int w = 0;  //擷取圖的寬
        private int h = 0;  //擷取圖的高
        int x_st = 0;   //擷取開始x
        int y_st = 0;   //擷取開始y

        int[] brightness_data = new int[256];

        int max = 255;
        int min = 0;

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
            pictureBox1.MouseDown += new MouseEventHandler(pictureBox1_MouseDown);
            pictureBox1.MouseMove += new MouseEventHandler(pictureBox1_MouseMove);
            pictureBox2.MouseMove += new MouseEventHandler(pictureBox2_MouseMove);
            pictureBox1.MouseUp += new MouseEventHandler(pictureBox1_MouseUp);
            pictureBox1.Paint += new PaintEventHandler(pictureBox1_Paint);
            pictureBox3a.Paint += new PaintEventHandler(pictureBox3a_Paint);
            pictureBox3b.Paint += new PaintEventHandler(pictureBox3b_Paint);

            show_item_location();
            reset_picture();
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

            pictureBox1.Size = new Size(pbx_W, pbx_H);
            pictureBox2.Size = new Size(pbx_W, pbx_H);
            pictureBox3a.Size = new Size(pbx_W2, pbx_H2);
            pictureBox3b.Size = new Size(pbx_W2, pbx_H2);
            pictureBox4.Size = new Size(pbx_W3 * 2, pbx_H2);
            pictureBox5.Size = new Size(pbx_W3 * 2, pbx_H2);
            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox2.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox3a.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox3b.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox4.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox5.SizeMode = PictureBoxSizeMode.Normal;

            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox3a.Location = new Point(x_st + dx * 1, y_st + dy2 * 0);
            pictureBox3b.Location = new Point(x_st + dx * 1 + pbx_W2, y_st + dy2 * 0);
            pictureBox4.Location = new Point(x_st + dx * 1, y_st + dy2 * 1);
            pictureBox5.Location = new Point(x_st + dx * 1, y_st + dy2 * 2);

            lb_brightness.Text = "";
            y_st = 420;
            dx += 160;
            dy = 50;
            lb_brightness.Location = new Point(x_st + dx * 2, y_st + dy * -1);
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
            cb_magnify.Location = new Point(x_st + dx * 2, y_st + dy * 12);

            y_st = 10;
            richTextBox1.Size = new Size(160, 1040);
            richTextBox1.Location = new Point(x_st + dx * 2 + 105, y_st + dy * 0);

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
            openFileDialog1.InitialDirectory = "c:\\______test_files";  //預設開啟的路徑
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
            bitmap1 = (Bitmap)Image.FromFile(filename1);	//Image.FromFile出來的是Image格式
            bitmap2 = (Bitmap)bitmap1.Clone();

            pictureBox1.Image = bitmap1;
            pictureBox2.Image = bitmap2;

            W = bitmap1.Width;
            H = bitmap1.Height;
            //richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";
        }

        void enhance_bitmap_data(Bitmap bitmap1, int x_st, int y_st, int w, int h)
        {
            //影像加強前 統計所有亮度, TBD

            int i;
            int j;
            int Y_max = 0;
            int Y_min = 255;
            Color pt;

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

            int diff_Y = Y_max - Y_min;

            if (diff_Y == 0)
                diff_Y = 1;

            float ratio_Y = 255 / (float)diff_Y;

            //ratio_Y = 3.0f;

            richTextBox1.Text += "\nM = " + Y_max.ToString() + "\tm = " + Y_min.ToString() + "\n";
            richTextBox1.Text += "D = " + diff_Y.ToString("F2") + "\tR = " + ratio_Y.ToString("F2") + "\n";

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

            //若是幾乎沒什麼變化的, 畫一個框來表示區域
            if (ratio_Y < 1.4)
            {
                Graphics g = Graphics.FromImage(bitmap1);
                g.DrawRectangle(Pens.Blue, x_st - 1, y_st - 1, w + 2, h + 2);
            }

            //影像加強後 統計所有亮度, TBD
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
                    if (y < 20)
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

            g.DrawImage(bitmap30, xx0+dx, yy0, bitmap30.Width, bitmap30.Height);   //原圖 一倍
            g.DrawImage(bitmap3b, xx1+dx, yy1, bitmap3b.Width, bitmap3b.Height);   //增強後的圖 一倍
            g.DrawImage(bitmap3a, xx2+dx, yy2, bitmap3a.Width, bitmap3a.Height);   //增強後的圖 二倍

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
            x_st = W / 8;
            y_st = H / 8;
            w = W * 3 / 4;
            h = H * 3 / 4;

            x_st = 100;
            y_st = 100;
            w = 640 - 200;
            h = 480 - 200;

            reset_picture();
            ImageEnhancement(x_st, y_st, w, h);
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
            x_st = W / 3;
            y_st = H / 3;
            w = W / 3;
            h = H / 3;

            reset_picture();
            ImageEnhancement(x_st, y_st, w, h);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            x_st = W / 12;
            y_st = H / 4;
            w = W / 10;
            h = H / 10;

            reset_picture();
            ImageEnhancement(x_st, y_st, w, h);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            x_st = W / 3;
            y_st = H / 3 - 50;
            w = W / 3;
            h = H / 3;

            reset_picture();
            ImageEnhancement(x_st, y_st, w, h);
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

            measure_brightness(pictureBox1, pictureBox4);
            measure_brightness(pictureBox2, pictureBox5);

            this.pictureBox1.Invalidate();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            x_st = 453;
            y_st = 177;
            w = 40;
            h = 40;

            reset_picture();
            ImageEnhancement(x_st, y_st, w, h);

            //亮度分布
            draw_x_st = x_st;
            draw_y_st = y_st;
            draw_w = w;
            draw_h = h;

            measure_brightness(pictureBox1, pictureBox4);
            measure_brightness(pictureBox2, pictureBox5);

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
            pictureBox5.SizeMode = PictureBoxSizeMode.CenterImage;
            pictureBox5.Size = new Size(800, 800);
            pictureBox5.Location = new Point(700, 250);
            pictureBox5.BringToFront();

            draw_2d_plot(bitmap2, x_st, y_st, w, h, 0);
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //彩色
            pictureBox5.SizeMode = PictureBoxSizeMode.CenterImage;
            pictureBox5.Size = new Size(800, 800);
            pictureBox5.Location = new Point(700, 250);
            pictureBox5.BringToFront();

            draw_2d_plot(bitmap2, x_st, y_st, w, h, 1);
        }

        private List<Point> Points = new List<Point>();
        private void button11_Click(object sender, EventArgs e)
        {
            //2D plot test

            int W = 800;
            int H = 800;

            pictureBox5.SizeMode = PictureBoxSizeMode.CenterImage;
            pictureBox5.Size = new Size(W, H);
            pictureBox5.Location = new Point(700, 250);
            pictureBox5.BringToFront();

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
            pictureBox5.Image = bitmap1;

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

            richTextBox1.Text += "Y_max = " + Y_max.ToString() + "\tY_min = " + Y_min.ToString() + "\n";
        }

        bool flag_pictureBox1_mouse_down = false;
        int pictureBox1_position_x_old = 0;
        int pictureBox1_position_y_old = 0;

        int draw_x_st = 0;
        int draw_y_st = 0;
        int draw_w = 0;
        int draw_h = 0;

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            bitmap1 = (Bitmap)Image.FromFile(filename1);	//Image.FromFile出來的是Image格式
            bitmap2 = (Bitmap)bitmap1.Clone();

            flag_pictureBox1_mouse_down = true;
            //richTextBox1.Text += "Down : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
            pictureBox1_position_x_old = e.X;
            pictureBox1_position_y_old = e.Y;
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_pictureBox1_mouse_down == true)
            {
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
                catch
                {
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
                catch
                {
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

            richTextBox1.Text += draw_x_st.ToString() + "\t" + draw_y_st.ToString() + "\t" + draw_w.ToString() + "\t" + draw_h.ToString() + "\n";
            draw_enhanced_image(bitmap2, draw_x_st, draw_y_st, draw_w, draw_h);
            measure_brightness(pictureBox1, pictureBox4);
            measure_brightness(pictureBox2, pictureBox5);
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            //richTextBox1.Text += draw_x_st.ToString() + "\t" + draw_y_st.ToString() + "\t" + draw_w.ToString() + "\t" + draw_h.ToString() + "\n";
            //e.Graphics.DrawRectangle(new Pen(Color.Blue, 3), draw_x_st, draw_y_st, draw_w, draw_h);
            e.Graphics.DrawRectangle(new Pen(Color.Blue, 3), draw_x_st - 1, draw_y_st - 1, draw_w + 2, draw_h + 2);

            e.Graphics.DrawString("原圖", new Font("標楷體", 30), new SolidBrush(Color.Red), new PointF(0, 0));
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
            //richTextBox1.Text += "共有 " + total_points.ToString() + " 個點\n";
        }

        void measure_brightness(PictureBox pbox1, PictureBox pbox2)
        {
            if (pbox1.Image == null)
            {
                richTextBox1.Text += pbox1.Name + " 無影像, 離開\n";
                return;
            }

            richTextBox1.Text += pbox1.Name + "\n";

            x_st = draw_x_st;
            y_st = draw_y_st;
            w = draw_w;
            h = draw_h;

            Bitmap bitmap1 = (Bitmap)pbox1.Image;
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            //richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";

            get_brigheness_data(bitmap1, x_st, y_st, w, h);

            /* debug
            richTextBox1.Text += "brightness data :\n";
            printArrayData(brightness_data);
            */

            int y_min = 0;
            int y_max = 0;
            FindYMaxYMin(brightness_data, out y_min, out y_max);
            richTextBox1.Text += "y_min = " + y_min.ToString() + "\t" + "y_max = " + y_max.ToString() + "\n";

            /*  修改數值
            //一律忽視最亮和最暗的數值   ????
            brightness_data[0] = 0;
            brightness_data[255] = 0;

            int i;
            for (i = 0; i < 256; i++)
            {
                if (brightness_data[i] < 40)
                {
                    brightness_data[i] = 0;
                }
                //richTextBox1.Text += brightness_data[i].ToString() + " ";
            }
            */

            /* debug
            richTextBox1.Text += "brightness data :\n";
            printArrayData(brightness_data);
            */

            draw_brightness(pbox2);
        }

        void draw_brightness(PictureBox pbox)
        {
            int i;

            /* debug
            richTextBox1.Text += "brightness data :\n";
            printArrayData(brightness_data);
            */

            int most = 0;
            int brightness_st = 0;
            int brightness_sp = 0;
            for (i = 0; i < 256; i++)
            {
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

            int y_min = 0;
            int y_max = 0;
            FindYMaxYMin(brightness_data, out y_min, out y_max);
            richTextBox1.Text += "M = " + y_max.ToString() + "\t" + "m = " + y_min.ToString() + "\n";

            int ww = 512 + 200;
            int hh1 = 300;
            int hh2 = 256;
            Bitmap bmp = new Bitmap(ww, hh1);
            Graphics g2 = Graphics.FromImage(bmp);
            g2.Clear(Color.Pink);
            Pen p = new Pen(Color.Blue, 2);

            double ratio = 0;
            ratio = (double)hh2 / most;
            richTextBox1.Text += "ratio = " + ratio.ToString() + "\n";

            for (i = 0; i < 256; i++)
            {
                g2.FillRectangle(Brushes.Red, i * 2, hh2 - (float)(brightness_data[i] * ratio), 2, (float)(brightness_data[i] * ratio));
            }

            g2.DrawRectangle(p, 0 + 1, 0 + 1, ww - 2, hh1 - 2);
            g2.DrawRectangle(p, 0 + 1, 0 + 1, ww - 2, hh2 - 2);

            Brush b = new SolidBrush(Color.FromArgb(33, Color.RoyalBlue.R, Color.RoyalBlue.G, Color.RoyalBlue.B));

            g2.FillRectangle(b, min * 2, 0, (max - min) * 2, hh1);


            //p = new Pen(Color.Green, 3);
            //g2.DrawLine(p, min * 2, hh2, max * 2, 0);

            Font f = new Font("標楷體", 20);

            if ((min >= 0) && (min <= 103))
            {
                g2.DrawString(min.ToString(), f, new SolidBrush(Color.Blue), new PointF(min * 2, hh2));
            }
            else if (min < 0)
            {
                g2.DrawString(min.ToString(), f, new SolidBrush(Color.Blue), new PointF(0, hh2));
            }
            else
            {
                g2.DrawString(min.ToString(), f, new SolidBrush(Color.Blue), new PointF(103 * 2, hh2));
            }

            if ((max <= 255) && (max >= 152))
            {
                g2.DrawString(max.ToString(), f, new SolidBrush(Color.Blue), new PointF(max * 2 - 50, hh2));
            }
            else if (max > 255)
            {
                g2.DrawString(max.ToString(), f, new SolidBrush(Color.Blue), new PointF(512 - 50, hh2));
            }
            else
            {
                g2.DrawString(max.ToString(), f, new SolidBrush(Color.Blue), new PointF(152 * 2 - 50, hh2));
            }

            g2.DrawString("Max = " + y_max.ToString(), new Font("標楷體", 20), new SolidBrush(Color.Navy), 512, 10);
            g2.DrawString("min = " + y_min.ToString(), new Font("標楷體", 20), new SolidBrush(Color.Navy), 512, 40);
            g2.DrawString("most = " + most.ToString(), new Font("標楷體", 20), new SolidBrush(Color.Navy), 512, 70);
            g2.DrawString("最亮 : " + brightness_sp.ToString(), new Font("標楷體", 20), new SolidBrush(Color.Navy), 512, 100);
            g2.DrawString("最暗 : " + brightness_st.ToString(), new Font("標楷體", 20), new SolidBrush(Color.Navy), 512, 130);
            g2.DrawString("亮差 : " + (brightness_sp - brightness_st).ToString(), new Font("標楷體", 20), new SolidBrush(Color.Navy), 512, 160);


            /*  沒幫上忙
            //畫個curve
            Point[] curvePoints = new Point[256];    //一維陣列內有 256 個Point

            for (i = 0; i < 256; i++)
            {
                curvePoints[i].X = i*2;
                curvePoints[i].Y = hh2 - (int)(brightness_data[i] * ratio);
            }

            // Draw lines between original points to screen.
            //g2.DrawLines(Pens.Green, curvePoints);   //畫直線
            // Draw curve to screen.
            g2.DrawCurve(Pens.Green, curvePoints); //畫曲線
            */

            pbox.Image = bmp;
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
                bitmap1 = new Bitmap(pictureBox5.Width, pictureBox5.Height);

                g = Graphics.FromImage(bitmap1);
                g.DrawString("選取範圍太大", new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(0, 0));
                pictureBox5.Image = bitmap1;
                return;
            }

            int point_size = 20;    //放大倍率

            if ((pb5_width / w) < (pb5_height / h))
                point_size = pb5_width / w;
            else
                point_size = pb5_height / h;

            Pen p = new Pen(Color.Red, 10);
            SolidBrush sb = new SolidBrush(Color.Blue);

            int W = pictureBox5.ClientSize.Width;
            int H = pictureBox5.ClientSize.Height;

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
            pictureBox5.Image = bitmap1;
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
    }
}
