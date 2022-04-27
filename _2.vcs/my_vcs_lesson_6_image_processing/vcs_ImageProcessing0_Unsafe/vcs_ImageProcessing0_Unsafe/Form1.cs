using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageLockMode, PixelFormat
using System.Diagnostics;	//for Stopwatch

namespace vcs_ImageProcessing0_Unsafe
{
    public partial class Form1 : Form
    {
        //string filename = @"C:\______test_files\__pic\global.c.gif";   //超大圖, 要很久
        string filename = @"C:\______test_files\elephant.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox1.Image = Image.FromFile(filename);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Restore_Picture();

            Stopwatch stopwatch = new Stopwatch();

            stopwatch.Start();
            Use_SetPixel_Code();

            stopwatch.Stop();
            richTextBox1.Text += "經過時間 : " + stopwatch.Elapsed.TotalSeconds.ToString("0.000") + " 秒\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Restore_Picture();

            Stopwatch stopwatch = new Stopwatch();
            stopwatch.Start();

            Use_Unsafe_Code();

            stopwatch.Stop();
            richTextBox1.Text += "經過時間 : " + stopwatch.Elapsed.TotalSeconds.ToString("0.000") + " 秒\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Restore_Picture();

        }

        void Restore_Picture()
        {
            pictureBox1.Image = Image.FromFile(filename);
            Application.DoEvents();
        }

        void Use_SetPixel_Code()
        {
            if (pictureBox1.Image != null)
            {
                int W = pictureBox1.Image.Width;
                int H = pictureBox1.Image.Height;
                Bitmap bitmap1 = (Bitmap)pictureBox1.Image;
                Bitmap bitmap2 = new Bitmap(W, H);
                Color pixel;
                for (int x = 0; x < W; x++)
                {
                    for (int y = 0; y < H; y++)
                    {
                        pixel = bitmap1.GetPixel(x, y);
                        int r, g, b, Result = 0;
                        r = pixel.R;
                        g = pixel.G;
                        b = pixel.B;
                        //实例程序以加权平均值法产生黑白图像
                        int iType = 2;
                        switch (iType)
                        {
                            case 0://平均值法
                                Result = ((r + g + b) / 3);
                                break;
                            case 1://最大值法
                                Result = r > g ? r : g;
                                Result = Result > b ? Result : b;
                                break;
                            case 2://加权平均值法
                                Result = ((int)(0.7 * r) + (int)(0.2 * g) + (int)(0.1 * b));
                                break;
                        }
                        bitmap2.SetPixel(x, y, Color.FromArgb(Result, Result, Result));
                    }
                }
                pictureBox1.Image = bitmap2;
            }
        }

        void Use_Unsafe_Code()
        {
            if (pictureBox1.Image != null)
            {
                int W = pictureBox1.Image.Width;
                int H = pictureBox1.Image.Height;
                Bitmap bitmap1 = (Bitmap)pictureBox1.Image;
                Bitmap bitmap2 = new Bitmap(W, H, PixelFormat.Format24bppRgb);
                BitmapData bitmapdata1 = bitmap1.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadOnly, PixelFormat.Format24bppRgb);  //原圖
                BitmapData bitmapdata2 = bitmap2.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);  //新圖即邊緣圖

                unsafe
                {
                    //首先第一段代碼是提取邊緣，邊緣置為黑色，其他部分置為白色
                    byte* pin = (byte*)(bitmapdata1.Scan0.ToPointer());
                    byte* pout = (byte*)(bitmapdata2.Scan0.ToPointer());
                    for (int y = 0; y < bitmapdata1.Height - 1; y++)
                    {
                        for (int x = 0; x < bitmapdata1.Width; x++)
                        {
                            double b = (double)pin[0];
                            double g = (double)pin[1];
                            double r = (double)pin[2];

                            double bgr = (b + g + r) / 3;

                            pout[0] = (byte)(bgr);
                            pout[1] = (byte)(bgr);
                            pout[2] = (byte)(bgr);
                            pin = pin + 3;
                            pout = pout + 3;

                        }
                        pin += bitmapdata1.Stride - bitmapdata1.Width * 3;
                        pout += bitmapdata2.Stride - bitmapdata2.Width * 3;
                    }

                    bitmap1.UnlockBits(bitmapdata1);
                    bitmap2.UnlockBits(bitmapdata2);

                    pictureBox1.Image = bitmap2;
                }
            }
        }
    }
}


