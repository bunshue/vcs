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

namespace vcs_PictureEnhance_YUV
{
    public partial class Form1 : Form
    {
        string filename1 = @"C:\______test_files\ims01.bmp";
        //string filename1 = @"C:\______test_files\color1.bmp";
        //string filename2 = @"C:\______test_files\color2.bmp";

        int W = 0;
        int H = 0;

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
            pictureBox1.Image = Image.FromFile(filename1);
            pictureBox2.Image = Image.FromFile(filename1);
            W = pictureBox2.Image.Width;
            H = pictureBox2.Image.Height;

            pictureBox2.MouseDown += new MouseEventHandler(pictureBox2_MouseDown);
            pictureBox2.MouseMove += new MouseEventHandler(pictureBox2_MouseMove);
            pictureBox2.MouseUp += new MouseEventHandler(pictureBox2_MouseUp);
            pictureBox2.Paint += new PaintEventHandler(pictureBox2_Paint);

            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;
            int dy2;

            int pbx_W = 800;
            int pbx_H = 520;
            int pbx_H2 = 520 * 2 / 3;

            x_st = 10;
            y_st = 10;
            dx = pbx_W + 10;
            dy = pbx_H + 10;
            dy2 = pbx_H2 + 10;

            pictureBox1.Size = new Size(pbx_W, pbx_H);
            pictureBox2.Size = new Size(pbx_W, pbx_H);
            pictureBox3.Size = new Size(pbx_W, pbx_H2);
            pictureBox4.Size = new Size(pbx_W, pbx_H2);
            pictureBox5.Size = new Size(pbx_W, pbx_H2);
            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox2.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox3.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox4.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox5.SizeMode = PictureBoxSizeMode.Normal;

            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox3.Location = new Point(x_st + dx * 1, y_st + dy2 * 0);
            pictureBox4.Location = new Point(x_st + dx * 1, y_st + dy2 * 1);
            pictureBox5.Location = new Point(x_st + dx * 1, y_st + dy2 * 2);

            dy = 50;
            button1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button2.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button3.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button5.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button6.Location = new Point(x_st + dx * 2, y_st + dy * 5);

            richTextBox1.Size = new Size(180, pbx_H * 2 + 10);
            richTextBox1.Location = new Point(x_st + dx * 2 + 100, y_st + dy * 0);

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

                pictureBox2.Image = Image.FromFile(filename1);
                W = pictureBox2.Image.Width;
                H = pictureBox2.Image.Height;
                //richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";
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

        void enhance_bitmap_data(Bitmap bitmap1, int x_st, int y_st, int w, int h)
        {
            int i;
            int j;
            Color pt;

            int Y_max = 0;
            int Y_min = 255;

            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {
                    pt = bitmap1.GetPixel(x_st + i, y_st + j);

                    RGB pp = new RGB(pt.R, pt.G, pt.B);
                    YUV yyy = new YUV();
                    yyy = RGBToYUV(pp);

                    if (Y_max < yyy.Y)
                        Y_max = (int)yyy.Y;

                    if (Y_min > yyy.Y)
                        Y_min = (int)yyy.Y;
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

            //ratio_Y = 2.50f;

            richTextBox1.Text += "M = " + Y_max.ToString() + "\tm = " + Y_min.ToString() + "\n";
            richTextBox1.Text += "diff = " + diff_Y.ToString("F2") + "\tratio = " + ratio_Y.ToString("F2") + "\n";

            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {
                    pt = bitmap1.GetPixel(x_st + i, y_st + j);

                    RGB pp = new RGB(pt.R, pt.G, pt.B);
                    YUV yyy = new YUV();
                    yyy = RGBToYUV(pp);

                    int Y_new = (int)((yyy.Y - Y_min) * ratio_Y);
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
                g.DrawRectangle(Pens.Blue, x_st, y_st, w, h);
            }
        }

        void show_part_image(Bitmap bitmap1, int x_st, int y_st, int w, int h)
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

            Bitmap bitmap3 = bitmap1.Clone(new Rectangle(x_st, y_st, w, h), PixelFormat.Format32bppArgb);

            pictureBox3.Image = bitmap3;

            if ((w > 640 / 2) || (h > 480 / 2))
            {
                pictureBox4.Image = null;
                return;
            }

            //準備放大兩倍
            //richTextBox1.Text += "x_st = " + x_st.ToString() + ", y_st = " + y_st.ToString() + ", w = " + w.ToString() + ", h = " + h.ToString() + "\n";

            Bitmap bitmap4 = new Bitmap(w * 2, h * 2);
            int i;
            int j;
            Color p;

            for (j = 0; j < h; j++)
            {
                for (i = 0; i < w; i++)
                {
                    p = bitmap3.GetPixel(i, j);
                    bitmap4.SetPixel(i * 2, j * 2, p);
                    bitmap4.SetPixel(i * 2, j * 2 + 1, p);
                    bitmap4.SetPixel(i * 2 + 1, j * 2, p);
                    bitmap4.SetPixel(i * 2 + 1, j * 2 + 1, p);
                }
            }
            pictureBox4.Image = bitmap4;
        }

        void draw_enhanced_image(int x_st, int y_st, int w, int h)
        {
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename1);	//Bitmap.FromFile出來的是Image格式
            Graphics g = Graphics.FromImage(bitmap1);

            enhance_bitmap_data(bitmap1, x_st, y_st, w, h);
            show_part_image(bitmap1, x_st, y_st, w, h);

            pictureBox1.Image = bitmap1;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename1);	//Bitmap.FromFile出來的是Image格式
            Graphics g = Graphics.FromImage(bitmap1);

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            //richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";

            int x_st = W / 8;
            int y_st = H / 8;
            int w = W * 3 / 4;
            int h = H * 3 / 4;

            x_st = 100;
            y_st = 100;
            w = 640 - 200;
            h = 480 - 200;


            enhance_bitmap_data(bitmap1, x_st, y_st, w, h);
            show_part_image(bitmap1, x_st, y_st, w, h);

            pictureBox1.Image = bitmap1;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename1);	//Bitmap.FromFile出來的是Image格式
            Graphics g = Graphics.FromImage(bitmap1);

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            //richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";

            int x_st = 50;
            int y_st = 50;
            int w = W / 2;
            int h = H / 2;

            enhance_bitmap_data(bitmap1, x_st, y_st, w, h);
            show_part_image(bitmap1, x_st, y_st, w, h);

            pictureBox1.Image = bitmap1;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename1);	//Bitmap.FromFile出來的是Image格式
            Graphics g = Graphics.FromImage(bitmap1);

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            //richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";

            int x_st = W / 3;
            int y_st = H / 3;
            int w = W / 3;
            int h = H / 3;

            enhance_bitmap_data(bitmap1, x_st, y_st, w, h);
            show_part_image(bitmap1, x_st, y_st, w, h);

            pictureBox1.Image = bitmap1;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename1);	//Bitmap.FromFile出來的是Image格式
            Graphics g = Graphics.FromImage(bitmap1);

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            //richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";

            int x_st = W / 12;
            int y_st = H / 4;
            int w = W / 10;
            int h = H / 10;

            enhance_bitmap_data(bitmap1, x_st, y_st, w, h);
            show_part_image(bitmap1, x_st, y_st, w, h);

            pictureBox1.Image = bitmap1;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename1);	//Bitmap.FromFile出來的是Image格式
            Graphics g = Graphics.FromImage(bitmap1);

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            //richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";

            int x_st = W / 3;
            int y_st = H / 3 - 50;
            int w = W / 3;
            int h = H / 3;

            enhance_bitmap_data(bitmap1, x_st, y_st, w, h);
            show_part_image(bitmap1, x_st, y_st, w, h);

            pictureBox1.Image = bitmap1;
        }

        bool flag_pictureBox2_mouse_down = false;
        int pictureBox2_position_x_old = 0;
        int pictureBox2_position_y_old = 0;

        int draw_x_st = 0;
        int draw_y_st = 0;
        int draw_w = 0;
        int draw_h = 0;

        private void pictureBox2_MouseDown(object sender, MouseEventArgs e)
        {
            flag_pictureBox2_mouse_down = true;
            //richTextBox1.Text += "Down : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
            pictureBox2_position_x_old = e.X;
            pictureBox2_position_y_old = e.Y;
        }

        private void pictureBox2_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_pictureBox2_mouse_down == true)
            {
                //richTextBox1.Text += "Up : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
                int dx = e.X - pictureBox2_position_x_old;
                int dy = e.Y - pictureBox2_position_y_old;

                if (dx > 0)
                {
                    draw_x_st = pictureBox2_position_x_old;
                    draw_w = dx;
                }
                else
                {
                    draw_x_st = e.X;
                    draw_w = -dx;
                }

                if (dy > 0)
                {
                    draw_y_st = pictureBox2_position_y_old;
                    draw_h = dy;
                }
                else
                {
                    draw_y_st = e.Y;
                    draw_h = -dy;
                }

                this.pictureBox2.Invalidate();
                //richTextBox1.Text += "dx, dy : (" + dx.ToString() + ", " + dy.ToString() + ")\n";
                //pictureBox2.Location = new Point(pictureBox2.Location.X + dx, pictureBox2.Location.Y + dy);
            }
        }

        private void pictureBox2_MouseUp(object sender, MouseEventArgs e)
        {
            flag_pictureBox2_mouse_down = false;
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

            draw_enhanced_image(draw_x_st, draw_y_st, draw_w, draw_h);
            measure_brightness(pictureBox1, pictureBox4);
            measure_brightness(pictureBox2, pictureBox5);
        }

        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {
            //richTextBox1.Text += draw_x_st.ToString() + "\t" + draw_y_st.ToString() + "\t" + draw_w.ToString() + "\t" + draw_h.ToString() + "\n";
            e.Graphics.DrawRectangle(new Pen(Color.Blue, 3), draw_x_st, draw_y_st, draw_w, draw_h);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename1);	//Bitmap.FromFile出來的是Image格式
            Graphics g = Graphics.FromImage(bitmap1);

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            //richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";

            int x_st = W / 8;
            int y_st = H / 8;
            int w = W * 3 / 4;
            int h = H * 3 / 4;

            x_st = 640 / 2;
            y_st = 480 / 2;
            w = 100;
            h = 100;

            enhance_bitmap_data(bitmap1, x_st, y_st, w, h);
            show_part_image(bitmap1, x_st, y_st, w, h);
            pictureBox1.Image = bitmap1;

            //亮度分布
            draw_x_st = x_st;
            draw_y_st = y_st;
            draw_w = w;
            draw_h = h;

            draw_enhanced_image(draw_x_st, draw_y_st, draw_w, draw_h);
            measure_brightness(pictureBox1, pictureBox4);
            measure_brightness(pictureBox2, pictureBox5);

            this.pictureBox2.Invalidate();
        }

        string filename = string.Empty;

        public Point firstPoint = new Point(0, 0);  //鼠標第一點 
        public Point secondPoint = new Point(0, 0);  //鼠標第二點 
        public bool begin = false;   //是否開始畫矩形 
        Graphics g1;

        //private int W = 0;  //原圖的寬
        //private int H = 0;  //原圖的高
        private int w = 0;  //擷取圖的寬
        private int h = 0;  //擷取圖的高

        int x_st = 0;
        int y_st = 0;
        int x_sp = 0;
        int y_sp = 0;

        Image image;
        int[] brightness_data = new int[256];

        int max = 255;
        int min = 0;
        int brightness = 128;
        int brightness_old = 128;
        int contrast = 128;
        int contrast_old = 128;

        bool flag_no_update_crop_picture = false;



        void measure_brightness(PictureBox pbox1, PictureBox pbox2)
        {
            richTextBox1.Text += "\n\n圖片 : " + filename + "\n";
            if (pbox1.Image == null)
            {
                richTextBox1.Text += pbox1.Name + " 無影像, 離開\n";
                return;
            }

            brightness_data = new int[256];

            /*
            if (checkBox1.Checked == true)
            {
                x_st = 0;
                y_st = 0;
                w = 640;
                h = 480;
            }
            else
            */
            {
                x_st = 100;
                y_st = 100;
                w = 640 - 200;
                h = 480 - 200;
            }

            richTextBox1.Text += pbox1.Name + "\n";

            //draw_enhanced_image(draw_x_st, draw_y_st, draw_w, draw_h);
            x_st = draw_x_st;
            y_st = draw_y_st;
            w = draw_w;
            h = draw_h;

            Bitmap bitmap1 = (Bitmap)pbox1.Image;
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";
            int i;
            int j;
            int total_points = 0;

            for (j = y_st; j < (y_st + h); j++)
            {
                for (i = x_st; i < (x_st + w); i++)
                {
                    byte rrr = bitmap1.GetPixel(i, j).R;
                    //richTextBox1.Text += rrr.ToString() + "-";
                    brightness_data[rrr]++;
                    total_points++;
                }
            }


            //debug
            for (i = 0; i < 256; i++)
            {
                richTextBox1.Text += brightness_data[i].ToString("D3") + " ";
                if((i%24)==23)
                    richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";

            int y_min;
            int y_max;
            FindYMaxYMin(brightness_data, out y_min, out y_max);

            richTextBox1.Text += "y_min = " + y_min.ToString() + "\t" + "y_max = " + y_max.ToString() + "\n";

            //一律忽視最亮和最暗的數值   ????
            brightness_data[0] = 0;
            brightness_data[255] = 0;

            for (i = 0; i < 256; i++)
            {
                if (brightness_data[i] < 40)
                    brightness_data[i] = 0;

                //richTextBox1.Text += brightness_data[i].ToString() + " ";
            }

            for (i = 0; i < 256; i++)
            {
                richTextBox1.Text += brightness_data[i].ToString("D3") + " ";
                if ((i % 24) == 23)
                    richTextBox1.Text += "\n";

            }
            richTextBox1.Text += "\n";



            richTextBox1.Text += "共有 " + total_points.ToString() + " 個點\n";

            draw_brightness(pbox2);
        }

        void draw_brightness(PictureBox pbox)
        {
            int i;
            int most = 0;
            for (i = 0; i < 256; i++)
            {
                //richTextBox1.Text += brightness_data[i].ToString() + " ";
                if (brightness_data[i] > most)
                    most = brightness_data[i];
                if (brightness_data[i] == 0)
                    brightness_data[i] = 5;
            }
            richTextBox1.Text += "\n最多 " + most.ToString() + "\n";

            int ww = 512;
            int hh1 = 300;
            int hh2 = 256;
            Bitmap bitmap2 = new Bitmap(ww, hh1);
            Graphics g2 = Graphics.FromImage(bitmap2);
            g2.Clear(Color.Pink);
            Pen p = new Pen(Color.Blue, 2);

            double ratio = 0;
            ratio = (double)hh2 / most;

            richTextBox1.Text += "ratio = " + ratio.ToString() + "\n";

            for (i = 0; i < 256; i++)
            {
                //g2.FillRectangle(Brushes.Red, i * 2, 0, 2, (float)(brightness_data[i] * ratio));
                g2.FillRectangle(Brushes.Red, i * 2, hh2 - (float)(brightness_data[i] * ratio), 2, (float)(brightness_data[i] * ratio));
            }

            g2.DrawRectangle(p, 0 + 1, 0 + 1, ww - 2, hh1 - 2);
            g2.DrawRectangle(p, 0 + 1, 0 + 1, ww - 2, hh2 - 2);


            Brush b = new SolidBrush(Color.FromArgb(33, Color.RoyalBlue.R, Color.RoyalBlue.G, Color.RoyalBlue.B));

            g2.FillRectangle(b, min * 2, 0, (max - min) * 2, hh1);


            p = new Pen(Color.Green, 3);

            g2.DrawLine(p, min * 2, hh2, max * 2, 0);

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
            pbox.Image = bitmap2;
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
    }
}

