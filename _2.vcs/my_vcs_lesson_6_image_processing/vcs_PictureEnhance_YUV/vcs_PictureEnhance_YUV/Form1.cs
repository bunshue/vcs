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

            int pbx_W = 800;
            int pbx_H = 520;

            x_st = 10;
            y_st = 10;
            dx = pbx_W + 10;
            dy = pbx_H + 10;

            pictureBox1.Size = new Size(pbx_W, pbx_H);
            pictureBox2.Size = new Size(pbx_W, pbx_H);
            pictureBox3.Size = new Size(pbx_W, pbx_H);
            pictureBox4.Size = new Size(pbx_W, pbx_H);
            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox2.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox3.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox4.SizeMode = PictureBoxSizeMode.Normal;

            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox3.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox4.Location = new Point(x_st + dx * 1, y_st + dy * 1);

            dy = 50;
            button1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button2.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button3.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button5.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 2, y_st + dy * 4);

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
        }

        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {
            //richTextBox1.Text += draw_x_st.ToString() + "\t" + draw_y_st.ToString() + "\t" + draw_w.ToString() + "\t" + draw_h.ToString() + "\n";
            e.Graphics.DrawRectangle(new Pen(Color.Blue, 3), draw_x_st, draw_y_st, draw_w, draw_h);
        }
    }
}

