using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageLockMode
using System.Runtime.InteropServices;   //for Marshal

namespace vcs_ImageProcessing1
{
    public partial class Form1 : Form
    {
        string filename = @"C:\_git\vcs\_1.data\______test_files1\_case1\\pic3.jpg";
        //Graphics g;
        Pen p;
        Bitmap bitmap1;

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

        public Form1()
        {
            InitializeComponent();
            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;   //圖片Zoom的方法
            pictureBox1.ClientSize = new Size(640, 480);    //設定pictureBox的大小
            pictureBox1.BorderStyle = BorderStyle.Fixed3D;
            pictureBox1.Cursor = Cursors.Cross;  //移到控件上，改變鼠標

            pictureBox2.SizeMode = PictureBoxSizeMode.Normal; //圖片Zoom的方法
            pictureBox2.ClientSize = new Size(640, 480);    //設定pictureBox的大小
            pictureBox2.BorderStyle = BorderStyle.Fixed3D;
            pictureBox2.Cursor = Cursors.Cross;  //移到控件上，改變鼠標
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Image image1 = new Bitmap(filename, true);
            pictureBox1.Image = image1;
            richTextBox1.Text += "圖片大小 " + image1.Width.ToString() + " X " + image1.Height.ToString() + "\n";
        }

        private void button7_Click(object sender, EventArgs e)
        {
            bitmap1 = null;
            pictureBox2.Image = null;
        }

        private void button19_Click(object sender, EventArgs e)
        {
            string filename = @"C:\_git\vcs\_1.data\______test_files1\ims_image.bmp";

            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";

            pictureBox2.Image = Image.FromFile(filename);

            bitmap1 = new Bitmap(filename);
            pictureBox1.Image = bitmap1;

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

        private void button18_Click(object sender, EventArgs e)
        {
            if (bitmap1 == null)
            {
                richTextBox1.Text += "未開啟圖片\n";
                return;
            }

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

        private void button17_Click(object sender, EventArgs e)
        {
            if (bitmap1 == null)
            {
                richTextBox1.Text += "未開啟圖片\n";
                return;
            }

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

        private void button20_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = (Bitmap)pictureBox1.Image;

            if (bitmap1 != null)
            {
                IntPtr pHdc;
                Graphics g = Graphics.FromImage(bitmap1);
                Pen p = new Pen(Color.Red, 1);
                SolidBrush drawBrush = new SolidBrush(Color.Yellow);
                Font drawFont = new Font("Arial", 6, FontStyle.Bold, GraphicsUnit.Millimeter);
                pHdc = g.GetHdc();

                g.ReleaseHdc();

                g.Dispose();

                String filename1 = string.Empty;

                filename1 = Application.StartupPath + "\\ims_image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");

                //String file1 = file + ".jpg";
                String filename1a = filename1 + ".bmp";
                //String file3 = file + ".png";

                try
                {
                    //bitmap1.Save(@file1, ImageFormat.Jpeg);
                    bitmap1.Save(filename1a, ImageFormat.Bmp);
                    //bitmap1.Save(@file3, ImageFormat.Png);

                    richTextBox1.Text += "存檔成功\n";
                    //richTextBox1.Text += "已存檔 : " + file1 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename1a + "\n";
                    //richTextBox1.Text += "已存檔 : " + file3 + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "xxx錯誤訊息b : " + ex.Message + "\n";
                }
            }
            else
            {
                richTextBox1.Text += "無圖可存\n";
            }

        }

        private void button22_Click(object sender, EventArgs e)
        {
            //恢復
            //讀取圖檔
            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            pictureBox1.Image = Image.FromFile(filename);
            pictureBox1.BackColor = Color.Lime;
        }

        private void button23_Click(object sender, EventArgs e)
        {
            //白色轉為透明
            //C#將圖片白色背景設置為透明
            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Image image = Image.FromFile(filename);
            Bitmap bitmap1 = new Bitmap(image);
            bitmap1.MakeTransparent(Color.White);
            pictureBox1.Image = bitmap1;
        }
    }
}
