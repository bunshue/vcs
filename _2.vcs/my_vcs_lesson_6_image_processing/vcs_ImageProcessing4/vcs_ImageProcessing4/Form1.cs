using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;   //for BitmapData
using System.Drawing.Drawing2D; //for InterpolationMode
using System.Runtime.InteropServices;   //for Marshal

namespace vcs_ImageProcessing4
{
    public partial class Form1 : Form
    {
        //string filename = @"C:\_git\vcs\_1.data\______test_files1\naruto.jpg";
        string filename = @"C:\_git\vcs\_1.data\______test_files1\elephant.jpg";
        //string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
        //string filename = @"C:\_git\vcs\_1.data\______test_files1\_image_processing\isinbaeva.jpg";

        Bitmap bitmap1;


        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
            reset_pictureBox();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 160 + 10;
            dy = 50 + 10;

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
            button10.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            button11.Location = new Point(x_st + dx * 0, y_st + dy * 11);

            button12.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button20.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button21.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            button22.Location = new Point(x_st + dx * 1, y_st + dy * 10);
            button23.Location = new Point(x_st + dx * 1, y_st + dy * 11);

            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox1.Size = new Size(600, 600);
            pictureBox2.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            pictureBox2.Size = new Size(600, 600);

            richTextBox1.Location = new Point(x_st + dx * 8, y_st + dy * 0);
            richTextBox1.Size = new Size(300, 600);

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
            openFileDialog1.InitialDirectory = @"C:\_git\vcs\_1.data\______test_files1";  //預設開啟的路徑
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

                filename = openFileDialog1.FileName;
                reset_pictureBox();
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
            bt_exit.Name = "bt_exit";
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

        void reset_pictureBox()
        {
            //讀取圖檔
            pictureBox1.Image = Image.FromFile(filename);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            reset_pictureBox();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //旋轉（90度/180度/270度, 3種）
            Bitmap bitmap1 = new Bitmap(filename);
            Bitmap bitmap2 = RotateImage(bitmap1, 90);
            pictureBox1.Image = bitmap2;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //重設大小
            Bitmap bitmap1 = new Bitmap(filename);
            Bitmap bitmap2 = ResizeImage(bitmap1, new Size(bitmap1.Width / 2, bitmap1.Height / 2));
            pictureBox1.Image = bitmap2;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string filename = @"C:\_git\vcs\_1.data\______test_files1\elephant.jpg";

            //水平Mirror
            int xx;
            int yy;
            int ww;
            int hh;

            richTextBox1.Text += "水平Mirror處理中~~~~~~\n";

            Bitmap bitmap1 = new Bitmap(filename);
            //g = Graphics.FromImage(bitmap1);

            ww = bitmap1.Width / 2;
            hh = bitmap1.Height / 1;

            for (yy = 0; yy < hh; yy++)
            {
                for (xx = 0; xx < ww; xx++)
                {
                    Color pp = bitmap1.GetPixel(bitmap1.Width - xx - 1, yy);
                    bitmap1.SetPixel(bitmap1.Width - xx - 1, yy, bitmap1.GetPixel(xx, yy));
                    bitmap1.SetPixel(xx, yy, pp);
                }
            }
            pictureBox1.Image = bitmap1;
            richTextBox1.Text += "處理完成\n";

        }

        private void button4_Click(object sender, EventArgs e)
        {
            string filename = @"C:\_git\vcs\_1.data\______test_files1\elephant.jpg";

            //垂直Mirror
            int xx;
            int yy;
            int ww;
            int hh;

            richTextBox1.Text += "垂直Mirror處理中~~~~~~\n";

            Bitmap bitmap1 = new Bitmap(filename);
            //g = Graphics.FromImage(bitmap1);

            ww = bitmap1.Width / 1;
            hh = bitmap1.Height / 2;

            for (xx = 0; xx < ww; xx++)
            {
                for (yy = 0; yy < hh; yy++)
                {
                    Color pp = bitmap1.GetPixel(xx, bitmap1.Height - yy - 1);
                    bitmap1.SetPixel(xx, bitmap1.Height - yy - 1, bitmap1.GetPixel(xx, yy));
                    bitmap1.SetPixel(xx, yy, pp);
                }
            }
            pictureBox1.Image = bitmap1;
            richTextBox1.Text += "處理完成\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //找過亮
            string filename = @"C:\_git\vcs\_1.data\______test_files1\ims_image.bmp";

            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";

            pictureBox1.Image = Image.FromFile(filename);

            Bitmap bitmap1 = new Bitmap(filename);
            pictureBox1.Image = bitmap1;

            int xx;
            int yy;
            Color p;

            for (yy = 0; yy < bitmap1.Height; yy++)
            {
                for (xx = 0; xx < bitmap1.Width; xx++)
                {
                    p = bitmap1.GetPixel(xx, yy);

                    RGB pp = new RGB(p.R, p.G, p.B);
                    YUV yyy = new YUV();
                    yyy = RGBToYUV(pp);

                    if (yyy.Y > 252)
                    {
                        //bitmap1.SetPixel(xx, yy, Color.FromArgb((int)yyy.Y, (int)yyy.Y, (int)yyy.Y));
                        bitmap1.SetPixel(xx, yy, Color.Red);
                    }
                    else
                    {
                    }
                }
            }
            pictureBox1.Image = bitmap1;
        }

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
            byte r = (byte)(yuv.Y + 1.4075 * (yuv.V - 128));
            byte g = (byte)(yuv.Y - 0.3455 * (yuv.U - 128) - (0.7169 * (yuv.V - 128)));
            byte b = (byte)(yuv.Y + 1.7790 * (yuv.U - 128));

            return new RGB(r, g, b);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //降亮度

            string filename = @"C:\_git\vcs\_1.data\______test_files1\ims_image.bmp";

            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";

            pictureBox1.Image = Image.FromFile(filename);

            Bitmap bitmap1 = new Bitmap(filename);
            pictureBox1.Image = bitmap1;

            int xx;
            int yy;
            Color p;

            for (yy = 0; yy < bitmap1.Height; yy++)
            {
                for (xx = 0; xx < bitmap1.Width; xx++)
                {
                    p = bitmap1.GetPixel(xx, yy);

                    RGB pp = new RGB(p.R, p.G, p.B);
                    YUV yyy = new YUV();
                    RGB rrr = new RGB();
                    yyy = RGBToYUV(pp);

                    if (yyy.Y > 50)
                    {
                        yyy.Y -= 10;
                    }
                    else
                    {
                        yyy.Y = 50;
                    }

                    rrr = YUVToRGB(yyy);
                    bitmap1.SetPixel(xx, yy, Color.FromArgb(rrr.R, rrr.G, rrr.B));
                }
            }
            pictureBox1.Image = bitmap1;


        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        //旋轉 90, 180, 270 度
        public Bitmap RotateImage(Bitmap bmp, int angle)
        {
            if (angle != 90 && angle != 180 && angle != 270)
            {
                return null;
            }
            int W = bmp.Width;
            int H = bmp.Height;

            if (angle == 90)
            {
                Bitmap newbmp = new Bitmap(H, W);
                using (Graphics g = Graphics.FromImage(newbmp))
                {
                    Point[] destinationPoints =
                    {
                        new Point(H, 0), // destination for upper-left point of original
                        new Point(H, W),// destination for upper-right point of original
                        new Point(0, 0)     // destination for lower-left point of original
                    };
                    g.DrawImage(bmp, destinationPoints);
                }
                return newbmp;
            }

            if (angle == 180)
            {
                Bitmap newbmp = new Bitmap(W, H);
                using (Graphics g = Graphics.FromImage(newbmp))
                {
                    Point[] destinationPoints =
                    {
                        new Point(W, H), // destination for upper-left point of original
                        new Point(0, H),// destination for upper-right point of original
                        new Point(W, 0)     // destination for lower-left point of original
                    };
                    g.DrawImage(bmp, destinationPoints);
                }
                return newbmp;
            }

            if (angle == 270)
            {
                Bitmap newbmp = new Bitmap(H, W);
                using (Graphics g = Graphics.FromImage(newbmp))
                {
                    Point[] destinationPoints = 
                    {
                        new Point(0, W), // destination for upper-left point of original
                        new Point(0, 0),// destination for upper-right point of original
                        new Point(H, W)    // destination for lower-left point of original
                    };
                    g.DrawImage(bmp, destinationPoints);
                }
                return newbmp;
            }
            return null;
        }

        //重設大小
        public Bitmap ResizeImage(Bitmap bmp, Size size)
        {
            Bitmap newbmp = new Bitmap(size.Width, size.Height);
            using (Graphics g = Graphics.FromImage(newbmp))
            {
                g.DrawImage(bmp, new Rectangle(Point.Empty, size));
            }
            return newbmp;
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //向右旋轉圖像90°
            Graphics g = this.pictureBox1.CreateGraphics();
            Bitmap bitmap1 = new Bitmap(filename);
            //g.FillRectangle(Brushes.White, this.pictureBox1.ClientRectangle);//填充窗體背景爲白色, 清空pictureBox
            Point[] destinationPoints = {
new Point(400, 0), // destination for upper-left point of original
new Point(400, 305),// destination for upper-right point of original
new Point(0, 0)}; // destination for lower-left point of original
            g.DrawImage(bitmap1, destinationPoints);

        }

        private void button11_Click(object sender, EventArgs e)
        {
            //旋轉圖像180°
            Graphics g = this.pictureBox1.CreateGraphics();
            Bitmap bitmap1 = new Bitmap(filename);
            //g.FillRectangle(Brushes.White, this.pictureBox1.ClientRectangle);//填充窗體背景爲白色, 清空pictureBox
            Point[] destinationPoints = {
new Point(0, 400), // destination for upper-left point of original
new Point(305, 400),// destination for upper-right point of original
new Point(0, 0)}; // destination for lower-left point of original
            g.DrawImage(bitmap1, destinationPoints);
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //圖像切變

            Graphics g = this.pictureBox1.CreateGraphics();
            Bitmap bitmap1 = new Bitmap(filename);
            //g.FillRectangle(Brushes.White, this.pictureBox1.ClientRectangle);//填充窗體背景爲白色, 清空pictureBox
            Point[] destinationPoints = {
new Point(0, 0), // destination for upper-left point of original
new Point(305, 0), // destination for upper-right point of original
new Point(100, 400)};// destination for lower-left point of original
            g.DrawImage(bitmap1, destinationPoints);
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //圖像截取

            Graphics g = this.pictureBox1.CreateGraphics();
            Bitmap bitmap1 = new Bitmap(filename);
            //g.FillRectangle(Brushes.White, this.pictureBox1.ClientRectangle);//填充窗體背景爲白色, 清空pictureBox
            Rectangle sr = new Rectangle(80, 60, 400, 400);//要截取的矩形區域
            Rectangle dr = new Rectangle(0, 0, 200, 200);//要顯示到Form的矩形區域
            g.DrawImage(bitmap1, dr, sr, GraphicsUnit.Pixel);
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //改變圖像大小

            Graphics g = this.pictureBox1.CreateGraphics();
            Bitmap bitmap1 = new Bitmap(filename);
            //g.FillRectangle(Brushes.White, this.pictureBox1.ClientRectangle);//填充窗體背景爲白色, 清空pictureBox
            int W = bitmap1.Width;
            int H = bitmap1.Height;

            // 改變圖像大小使用低質量的模式
            g.InterpolationMode = InterpolationMode.NearestNeighbor;

            g.DrawImage(bitmap1, new Rectangle(10, 10, 120, 120), // source rectangle
            new Rectangle(0, 0, W, H), // destination rectangle
            GraphicsUnit.Pixel);

            // 使用高質量模式
            //g.CompositingQuality = CompositingQuality.HighSpeed;
            g.InterpolationMode = InterpolationMode.HighQualityBicubic;

            g.DrawImage(bitmap1, new Rectangle(130, 10, 120, 120), new Rectangle(0, 0, W, H), GraphicsUnit.Pixel);
        }

        private void button15_Click(object sender, EventArgs e)
        {
            reset_pictureBox();

            //轉成灰階
            pictureBox1.Image = ConvertToGrayscale(filename);
        }

        private void button16_Click(object sender, EventArgs e)
        {
            reset_pictureBox();

            //轉成灰階
            pictureBox1.Image = ConvertToGrayscale_CM(filename);
        }

        private void button17_Click(object sender, EventArgs e)
        {
            reset_pictureBox();

            //透明度
            pictureBox1.Image = ConvertToTransparency(pictureBox1.Image);
        }

        private void button18_Click(object sender, EventArgs e)
        {
            reset_pictureBox();

            //旋轉
            pictureBox1.Image = ConvertToRotate(pictureBox1.Image);
        }

        private void button19_Click(object sender, EventArgs e)
        {
            //轉成藍色系
            // Retrieve the image.
            Bitmap image1 = new Bitmap(filename, true);

            int x, y;

            // Loop through the images pixels to reset color.
            for (x = 0; x < image1.Width; x++)
            {
                for (y = 0; y < image1.Height; y++)
                {
                    Color pixelColor = image1.GetPixel(x, y);
                    //Color newColor = Color.FromArgb(pixelColor.R, 0, 0);
                    //Color newColor = Color.FromArgb(0, pixelColor.G, 0);
                    Color newColor = Color.FromArgb(0, 0, pixelColor.B);
                    image1.SetPixel(x, y, newColor);
                }
            }

            // Set the PictureBox to display the image.
            pictureBox1.Image = image1;

            richTextBox1.Text += "圖片大小 " + image1.Width.ToString() + " X " + image1.Height.ToString() + "\n";

            // Display the pixel format in Label1.
            richTextBox1.Text += "Pixel format: " + image1.PixelFormat.ToString() + "\n";
        }

        private void button20_Click(object sender, EventArgs e)
        {
        }

        private void button21_Click(object sender, EventArgs e)
        {
        }

        private void button22_Click(object sender, EventArgs e)
        {
            //擷取其中一塊
            int xx;
            int yy;
            int ww;
            int hh;

            richTextBox1.Text += "擷取其中一塊處理中~~~~~~, 九宮格之正中央\n";

            bitmap1 = new Bitmap(filename);
            //g = Graphics.FromImage(bitmap1);

            ww = bitmap1.Width / 3;
            hh = bitmap1.Height / 3;

            Bitmap bitmap2 = new Bitmap(ww, hh);

            int x_st = ww;
            int y_st = hh;

            for (yy = 0; yy < hh; yy++)
            {
                for (xx = 0; xx < ww; xx++)
                {
                    bitmap2.SetPixel(xx, yy, bitmap1.GetPixel(x_st + xx, y_st + yy));
                }
            }
            pictureBox2.Image = bitmap2;
            pictureBox2.SizeMode = PictureBoxSizeMode.Normal;   //圖片Zoom的方法
            richTextBox1.Text += "處理完成\n";
        }

        private void button23_Click(object sender, EventArgs e)
        {
            //縮圖成一半
            int xx;
            int yy;
            int ww;
            int hh;

            richTextBox1.Text += "縮圖成一半\n";

            bitmap1 = new Bitmap(filename);
            //g = Graphics.FromImage(bitmap1);

            ww = bitmap1.Width / 2;
            hh = bitmap1.Height / 2;

            Bitmap bitmap2 = new Bitmap(ww, hh);

            int x_st = 0;
            int y_st = 0;

            for (yy = 0; yy < hh; yy++)
            {
                for (xx = 0; xx < ww; xx++)
                {
                    bitmap2.SetPixel(xx, yy, bitmap1.GetPixel(x_st + xx * 2 + 1, y_st + yy * 2 + 1));
                }
            }

            pictureBox2.Image = bitmap2;
            pictureBox2.SizeMode = PictureBoxSizeMode.Normal;   //圖片Zoom的方法
            richTextBox1.Text += "處理完成\n";
        }

        public Bitmap ConvertToGrayscale(string filename)
        {
            Bitmap bitmap1 = new Bitmap(filename);
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            Bitmap bitmap2 = new Bitmap(W, H);

            for (int y = 0; y < H; y++)
            {
                for (int x = 0; x < W; x++)
                {
                    Color c = bitmap1.GetPixel(x, y); // 得到 原始像素 的 Color
                    int luma = (int)(c.R * 0.3 + c.G * 0.6 + c.B * 0.1);  // 以 3:6:1 的比例得到設定值
                    bitmap2.SetPixel(x, y, Color.FromArgb(luma, luma, luma)); // 寫入 像素値
                }
            }
            return bitmap2;
        }

        // 使用色彩矩陣來調整影像色彩
        public Bitmap ConvertToGrayscale_CM(string filename)
        {
            Bitmap bitmap1 = new Bitmap(filename);
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            Bitmap bitmap2 = new Bitmap(W, H);

            Graphics g = Graphics.FromImage(bitmap2); // 從點陣圖 建立 新的畫布

            // 定義含有 RGBA 空間座標的 5 x 5 矩陣
            // (R, G, B, A, 1) 乘上 此矩陣
            ColorMatrix cm = new ColorMatrix(
                   new float[][]{ new float[]{0.3f, 0.3f, 0.3f, 0, 0},
                                  new float[]{0.6f, 0.6f, 0.6f, 0, 0},
                                  new float[]{0.1f, 0.1f, 0.1f, 0, 0},
                                  new float[]{  0,    0,    0,  1, 0},
                                  new float[]{  0,    0,    0,  0, 1}});

            // ImageAttributes 類別的多個方法會使用色彩矩陣來調整影像色彩
            ImageAttributes ia = new ImageAttributes();

            // 設定預設分類的色彩調整矩陣。
            ia.SetColorMatrix(cm);
            g.DrawImage(bitmap1, new Rectangle(0, 0, W, H), 0, 0, W, H, GraphicsUnit.Pixel, ia);
            g.Dispose();

            return bitmap2;
        }

        public Bitmap ConvertToTransparency(Image image)
        {
            Bitmap bitmap1 = new Bitmap(filename);
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            Bitmap bitmap2 = new Bitmap(W, H);

            Graphics g = Graphics.FromImage(bitmap2);

            ImageAttributes ia = new ImageAttributes();

            ColorMatrix cm = new ColorMatrix();

            cm.Matrix33 = 0.5f; // 透明度

            ia.SetColorMatrix(cm);

            g.DrawImage(image, new Rectangle(0, 0, W, H), 0, 0, W, H, GraphicsUnit.Pixel, ia);
            g.Dispose();

            return bitmap2;
        }

        public Bitmap ConvertToRotate(Image image)
        {
            Bitmap bitmap1 = new Bitmap(filename);
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            Bitmap bitmap2 = new Bitmap(W, H);

            Graphics g = Graphics.FromImage(bitmap2);

            Matrix mx = new Matrix();

            mx.Rotate(30);
            g.Transform = mx;

            g.DrawImage(image, new Rectangle(0, 0, W, H));

            g.Dispose();

            return bitmap2;
        }
    }
}
