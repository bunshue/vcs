using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat

namespace my_rgb_yuv
{
    public partial class Form1 : Form
    {
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
            pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
            p = new Pen(Color.Red, 3);

            lb_y.Text = "Y";
            lb_u.Text = "U";
            lb_v.Text = "V";
            lb_r.Text = "R";
            lb_g.Text = "G";
            lb_b.Text = "B";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            bool conversionSuccessful = false;
            int rr = 0;
            int gg = 0;
            int bb = 0;

            conversionSuccessful = int.TryParse(textBox1.Text, out rr);    //out為必須
            if (conversionSuccessful == true)
            {
                //richTextBox1.Text += "rr： " + rr.ToString() + "\n";
            }
            else
            {
                richTextBox1.Text += "int.TryParse R 失敗\n";
                return;
            }

            conversionSuccessful = int.TryParse(textBox2.Text, out gg);    //out為必須
            if (conversionSuccessful == true)
            {
                //richTextBox1.Text += "gg： " + gg.ToString() + "\n";
            }
            else
            {
                richTextBox1.Text += "int.TryParse G 失敗\n";
                return;
            }

            conversionSuccessful = int.TryParse(textBox3.Text, out bb);    //out為必須
            if (conversionSuccessful == true)
            {
                //richTextBox1.Text += "bb： " + bb.ToString() + "\n";
            }
            else
            {
                richTextBox1.Text += "int.TryParse B 失敗\n";
                return;
            }

            RGB pp = new RGB((byte)rr, (byte)gg, (byte)bb);
            YUV yy = new YUV();
            yy = RGBToYUV(pp);
            lb_y.Text = "Y = " + yy.Y.ToString();
            lb_u.Text = "U = " + yy.U.ToString();
            lb_v.Text = "V = " + yy.V.ToString();
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

        private void button2_Click(object sender, EventArgs e)
        {
            string filename = "C:\\______test_files\\picture\\ims_image_20191220_162739.bmp";

            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";

            pictureBox2.Image = Image.FromFile(filename);

            bitmap1 = new Bitmap(filename);
            pictureBox1.Image = bitmap1;















        }

        private void button3_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = (Bitmap)pictureBox1.Image;

            if (bitmap1 != null)
            {
                IntPtr pHdc;
                Graphics g = Graphics.FromImage(bitmap1);
                Pen p = new Pen(Color.Red, 1);
                SolidBrush drawBrush = new SolidBrush(Color.Yellow);
                Font drawFont = new Font("Arial", 6, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);
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

        private void button4_Click(object sender, EventArgs e)
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

        private void button5_Click(object sender, EventArgs e)
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

        private void button6_Click(object sender, EventArgs e)
        {
            bool conversionSuccessful = false;
            int yy = 0;
            int uu = 0;
            int vv = 0;

            conversionSuccessful = int.TryParse(textBox4.Text, out yy);    //out為必須
            if (conversionSuccessful == true)
            {
                //richTextBox1.Text += "yy： " + yy.ToString() + "\n";
            }
            else
            {
                richTextBox1.Text += "int.TryParse Y 失敗\n";
                return;
            }

            conversionSuccessful = int.TryParse(textBox5.Text, out uu);    //out為必須
            if (conversionSuccessful == true)
            {
                //richTextBox1.Text += "uu： " + uu.ToString() + "\n";
            }
            else
            {
                richTextBox1.Text += "int.TryParse U 失敗\n";
                return;
            }

            conversionSuccessful = int.TryParse(textBox6.Text, out vv);    //out為必須
            if (conversionSuccessful == true)
            {
                //richTextBox1.Text += "vv： " + vv.ToString() + "\n";
            }
            else
            {
                richTextBox1.Text += "int.TryParse V 失敗\n";
                return;
            }

            YUV yyy = new YUV(yy, uu, vv);
            RGB rrr = new RGB();
            rrr = YUVToRGB(yyy);
            lb_r.Text = "R = " + rrr.R.ToString();
            lb_g.Text = "G = " + rrr.G.ToString();
            lb_b.Text = "B = " + rrr.B.ToString();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

    }
}
