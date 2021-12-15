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
        string filename = @"C:\______test_files\_case1\\pic3.jpg";
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

        private void trackBar_R_Scroll(object sender, EventArgs e)
        {
            tb_R.Text = trackBar_R.Value.ToString();
        }

        private void trackBar_G_Scroll(object sender, EventArgs e)
        {
            tb_G.Text = trackBar_G.Value.ToString();
        }

        private void trackBar_B_Scroll(object sender, EventArgs e)
        {
            tb_B.Text = trackBar_B.Value.ToString();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int ratio_r;
            int ratio_g;
            int ratio_b;
            ratio_r = trackBar_R.Value;
            ratio_g = trackBar_G.Value;
            ratio_b = trackBar_B.Value;

            draw_picture(ratio_r, ratio_g, ratio_b);
        }

        int ratio = 100;
        private void button2_Click(object sender, EventArgs e)
        {
            if (ratio <= 255)
            {
                ratio += 10;
                richTextBox1.Text += ratio.ToString() + " %\n";

                draw_picture(ratio, ratio, ratio);
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (ratio >= 10)
            {
                ratio -= 10;
                richTextBox1.Text += ratio.ToString() + " %\n";

                draw_picture(ratio, ratio, ratio);
            }
        }


        private void button7_Click(object sender, EventArgs e)
        {
            bitmap1 = null;
            pictureBox2.Image = null;
        }

        void draw_picture(int ratio_r, int ratio_g, int ratio_b)
        {
            int xx;
            int yy;
            int ww;
            int hh;
            Color ppp;
            int A;
            int R;
            int G;
            int B;

            richTextBox1.Text += "處理中~~~~~~\n";

            bitmap1 = new Bitmap(filename);
            //g = Graphics.FromImage(bitmap1);

            ww = bitmap1.Width / 2;
            hh = bitmap1.Height / 2;

            for (yy = 0; yy < hh; yy++)
            {
                for (xx = 0; xx < ww; xx++)
                {
                    Color pp = bitmap1.GetPixel(xx, yy);

                    A = pp.A;
                    R = pp.R;
                    G = pp.G;
                    B = pp.B;

                    R = R * ratio_r / 100;
                    if (R > 255)
                        R = 255;
                    G = G * ratio_g / 100;
                    if (G > 255)
                        G = 255;
                    B = B * ratio_b / 100;
                    if (B > 255)
                        B = 255;

                    ppp = Color.FromArgb(A, R, G, B);
                    bitmap1.SetPixel(xx, yy, ppp);
                }
            }
            pictureBox2.Image = bitmap1;
            richTextBox1.Text += "處理完成\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            draw_picture(100, 0, 0);

        }

        private void button5_Click(object sender, EventArgs e)
        {
            draw_picture(0, 100, 0);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            draw_picture(0, 0, 100);
        }

        private void button8_Click(object sender, EventArgs e)
        {
            int xx;
            int yy;
            int ww;
            int hh;

            richTextBox1.Text += "水平Mirror處理中~~~~~~\n";

            bitmap1 = new Bitmap(filename);
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
            pictureBox2.Image = bitmap1;
            richTextBox1.Text += "處理完成\n";

        }

        private void button9_Click(object sender, EventArgs e)
        {
            int xx;
            int yy;
            int ww;
            int hh;

            richTextBox1.Text += "垂直Mirror處理中~~~~~~\n";

            bitmap1 = new Bitmap(filename);
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
            pictureBox2.Image = bitmap1;
            richTextBox1.Text += "處理完成\n";
        }

        private void button10_Click(object sender, EventArgs e)
        {
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

        private void button11_Click(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {
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

        private void button14_Click(object sender, EventArgs e)
        {
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

        private void LockUnlockBitsExample1()
        {
            string filename = @"C:\______test_files\_case1\\pic3.jpg";

            int data_offset = 0;
            // Create a new bitmap.
            Bitmap bmp0 = new Bitmap(filename);
            Bitmap bmp = new Bitmap(filename);
            pictureBox1.Image = bmp0;

            richTextBox1.Text += "W = " + bmp.Width.ToString() + ", H = " + bmp.Height.ToString() + "\n";
            richTextBox1.Text += "PixelFormat = " + bmp.PixelFormat.ToString() + "\n";

            if (bmp.PixelFormat == PixelFormat.Format32bppRgb)
                richTextBox1.Text += "位元深度\t32\n";
            else if (bmp.PixelFormat == PixelFormat.Format24bppRgb)
                richTextBox1.Text += "位元深度\t24\n";
            else if (bmp.PixelFormat == PixelFormat.Format8bppIndexed)
                richTextBox1.Text += "位元深度\t8\n";
            else
                richTextBox1.Text += "位元深度\tunknown, PixelFormat = " + bmp.PixelFormat.ToString() + "\n";

            // Lock the bitmap's bits.  
            Rectangle rect = new Rectangle(0, 0, bmp.Width, bmp.Height);
            //System.Drawing.Imaging.BitmapData bmpData = bmp.LockBits(rect, System.Drawing.Imaging.ImageLockMode.ReadWrite, bmp.PixelFormat);
            System.Drawing.Imaging.BitmapData bmpData = bmp.LockBits(rect, System.Drawing.Imaging.ImageLockMode.ReadWrite, bmp.PixelFormat);

            richTextBox1.Text += "W = " + bmpData.Width.ToString() + "\n";
            richTextBox1.Text += "H = " + bmpData.Height.ToString() + "\n";
            richTextBox1.Text += "Stride = " + bmpData.Stride.ToString() + "\n";    //圖片一橫條的拜數 即WX4(拜)
            richTextBox1.Text += "Scan0 = " + bmpData.Scan0.ToString() + "\n";

            // Get the address of the first line.
            IntPtr ptr = bmpData.Scan0;

            // Declare an array to hold the bytes of the bitmap.
            int len = Math.Abs(bmpData.Stride) * bmp.Height;    //(W * 4) * H

            richTextBox1.Text += "len = " + len.ToString() + "\n";

            byte[] rgbValues = new byte[len];

            // Copy the RGB values into the array.
            Marshal.Copy(ptr, rgbValues, 0, len);

            /*
            int i;
            for (i = 0; i < 1024; i++)
            {
                richTextBox1.Text += rgbValues[i].ToString();
                if ((i % 64) == 63)
                    richTextBox1.Text += "\n";
                else
                    richTextBox1.Text += " ";
            }
            richTextBox1.Text += "\n";
            richTextBox1.Text += "\n";
            richTextBox1.Text += "\n";
            richTextBox1.Text += "\n";
            */

            //對特定點的資料作操作
            int tmp = 0;
            for (int counter = 0; counter < (rgbValues.Length - 20); counter += 3)
            {
                tmp = rgbValues[counter] + rgbValues[counter + 1] + rgbValues[counter + 2];
                tmp /= 3;
                rgbValues[counter] = (byte)tmp;
                rgbValues[counter + 1] = (byte)tmp;
                rgbValues[counter + 2] = (byte)tmp;
            }

            /*
            for (i = 0; i < 1024; i++)
            {
                richTextBox1.Text += rgbValues[i].ToString();
                if ((i % 64) == 63)
                    richTextBox1.Text += "\n";
                else
                    richTextBox1.Text += " ";
            }
            richTextBox1.Text += "\n";
            */

            // Copy the RGB values back to the bitmap
            Marshal.Copy(rgbValues, 0, ptr, len);

            // Unlock the bits.
            bmp.UnlockBits(bmpData);

            // Draw the modified image.
            pictureBox2.Image = bmp;
        }

        private void LockUnlockBitsExample2()
        {
            int data_offset = 0;
            // Create a new bitmap.
            //Bitmap bmp = new Bitmap("c:\\______test_files\\IMG_256X32.bmp");
            Bitmap bmp0 = new Bitmap("c:\\______test_files\\picture1.jpg");
            Bitmap bmp = new Bitmap("c:\\______test_files\\picture1.jpg");
            pictureBox1.Image = bmp0;

            richTextBox1.Text += "W = " + bmp.Width.ToString() + ", H = " + bmp.Height.ToString() + "\n";
            richTextBox1.Text += "PixelFormat = " + bmp.PixelFormat.ToString() + "\n";

            if (bmp.PixelFormat == PixelFormat.Format32bppRgb)
            {
                richTextBox1.Text += "位元深度\t32\n";
                data_offset = 4;
            }
            else if (bmp.PixelFormat == PixelFormat.Format24bppRgb)
            {
                richTextBox1.Text += "位元深度\t24\n";
                data_offset = 3;
            }
            else if (bmp.PixelFormat == PixelFormat.Format8bppIndexed)
            {
                richTextBox1.Text += "位元深度\t8\n";
                data_offset = 1;
            }
            else
                richTextBox1.Text += "位元深度\tunknown, PixelFormat = " + bmp.PixelFormat.ToString() + "\n";

            // Lock the bitmap's bits.  
            Rectangle rect = new Rectangle(bmp.Width / 4, bmp.Width / 4, bmp.Width / 2, bmp.Height / 2);
            System.Drawing.Imaging.BitmapData bmpData = bmp.LockBits(rect, System.Drawing.Imaging.ImageLockMode.ReadWrite, bmp.PixelFormat);

            richTextBox1.Text += "W = " + bmpData.Width.ToString() + "\n";
            richTextBox1.Text += "H = " + bmpData.Height.ToString() + "\n";
            richTextBox1.Text += "Stride = " + bmpData.Stride.ToString() + "\n";    //圖片一橫條的拜數 即WX4(拜)
            richTextBox1.Text += "Scan0 = " + bmpData.Scan0.ToString() + "\n";

            // Get the address of the first line.
            IntPtr ptr = bmpData.Scan0;

            // Declare an array to hold the bytes of the bitmap.
            int len = Math.Abs(bmpData.Stride) * bmp.Height / 4;    //(W * 4) * H

            richTextBox1.Text += "len = " + len.ToString() + "\n";

            byte[] rgbValues = new byte[len];

            // Copy the RGB values into the array.
            Marshal.Copy(ptr, rgbValues, 0, len);

            /*
            int i;
            for (i = 0; i < 1024; i++)
            {
                richTextBox1.Text += rgbValues[i].ToString();
                if ((i % 64) == 63)
                    richTextBox1.Text += "\n";
                else
                    richTextBox1.Text += " ";
            }
            richTextBox1.Text += "\n";
            richTextBox1.Text += "\n";
            richTextBox1.Text += "\n";
            richTextBox1.Text += "\n";
            */

            //對特定點的資料作操作
            int tmp = 0;
            for (int counter = 0; counter < (rgbValues.Length - data_offset); counter += data_offset)
            {
                tmp = rgbValues[counter] + rgbValues[counter + 1] + rgbValues[counter + 2];
                tmp /= 3;
                rgbValues[counter] = (byte)tmp;
                rgbValues[counter + 1] = (byte)tmp;
                rgbValues[counter + 2] = (byte)tmp;
            }

            /*
            for (i = 0; i < 1024; i++)
            {
                richTextBox1.Text += rgbValues[i].ToString();
                if ((i % 64) == 63)
                    richTextBox1.Text += "\n";
                else
                    richTextBox1.Text += " ";
            }
            richTextBox1.Text += "\n";
            */

            // Copy the RGB values back to the bitmap
            Marshal.Copy(rgbValues, 0, ptr, len);

            // Unlock the bits.
            bmp.UnlockBits(bmpData);

            // Draw the modified image.
            pictureBox2.Image = bmp;
        }

        private void button19_Click(object sender, EventArgs e)
        {
            string filename = "C:\\______test_files\\ims_image.bmp";

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

        private void button16_Click(object sender, EventArgs e)
        {
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox2.SizeMode = PictureBoxSizeMode.Zoom;
            LockUnlockBitsExample1();
        }

        private void button21_Click(object sender, EventArgs e)
        {
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox2.SizeMode = PictureBoxSizeMode.Zoom;
            LockUnlockBitsExample2();
        }

        //光暈效果 ST
        public Image pp(PictureBox Pict, int x, int y, int R, float better) //R強光照射面的半徑，即"光暈"
        {
            //Bitmap Var_Bmp = new Bitmap(Pict.Image, Pict.Width, Pict.Height);//根據圖像實例化Bitmap類
            Bitmap Var_Bmp = new Bitmap(Pict.Image, Pict.Image.Width, Pict.Image.Height);//根據圖像實例化Bitmap類

            int tem_W = Var_Bmp.Width;//獲取圖像的寬度
            int tem_H = Var_Bmp.Height;//獲取圖像的高度
            //定義一個Bitmap類的復本
            Bitmap Var_SaveBmp = Var_Bmp.Clone(new RectangleF(0, 0, tem_W, tem_H), System.Drawing.Imaging.PixelFormat.DontCare);
            Point Var_Center = new Point(x, y);//光暈的中心點
            //遍歷圖像中的各象素
            for (int i = tem_W - 1; i >= 1; i--)
            {
                for (int j = tem_H - 1; j >= 1; j--)
                {
                    float Var_Length = (float)Math.Sqrt(Math.Pow((i - Var_Center.X), 2) + Math.Pow((j - Var_Center.Y), 2));//設置光暈的範圍
                    //如果像素位於」光暈」之內
                    if (Var_Length < R)
                    {
                        Color Var_Color = Var_SaveBmp.GetPixel(i, j);
                        int r, g, b;
                        float Var_Pixel = better * (1.0f - Var_Length / R);//設置光亮度的強弱
                        r = Var_Color.R + (int)Var_Pixel;//設置加強後的R值
                        r = Math.Max(0, Math.Min(r, 255));//如果R值不在顏色值的範圍內，對R值進行設置
                        g = Var_Color.G + (int)Var_Pixel;//設置加強後的G值
                        g = Math.Max(0, Math.Min(g, 255));//如果G值不在顏色值的範圍內，對G值進行設置
                        b = Var_Color.B + (int)Var_Pixel;//設置加強後的B值
                        b = Math.Max(0, Math.Min(b, 255));//如果B值不在顏色值的範圍內，對B值進行設置
                        Var_SaveBmp.SetPixel(i, j, Color.FromArgb(255, r, g, b));//將增亮後的像素值回寫到位圖
                    }
                }
            }
            return Var_SaveBmp;
        }

        private void button12_Click(object sender, EventArgs e)
        {
            int cx = 50;
            int cy = 50;
            int R = 100;
            pictureBox1.Image = pp(pictureBox1, cx, cy, R, 150F);
        }
        //光暈效果 SP


        private void button15_Click(object sender, EventArgs e)
        {
            //string filename = "C:\\______test_files\\ims_image.bmp";
            string filename = @"C:\______test_files\ims1.bmp";

            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";

            pictureBox1.Image = Image.FromFile(filename);


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
                    byte newColor_r = (byte)((pixelColor.R / 20) * 20);
                    byte newColor_g = (byte)((pixelColor.G / 20) * 20);
                    byte newColor_b = (byte)((pixelColor.B / 20) * 20);

                    Color newColor = Color.FromArgb(newColor_r, newColor_g, newColor_b);

                    image1.SetPixel(x, y, newColor);
                }
            }

            // Set the PictureBox to display the image.
            pictureBox2.Image = image1;

            richTextBox1.Text += "圖片大小 " + image1.Width.ToString() + " X " + image1.Height.ToString() + "\n";

            // Display the pixel format in Label1.
            richTextBox1.Text += "Pixel format: " + image1.PixelFormat.ToString() + "\n";


        }
    }
}
