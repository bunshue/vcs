using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for BitmapData
using System.Runtime.InteropServices;   //for Marshal

namespace vcs_EdgeDetection
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\naruto.jpg";

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
            Bitmap bitmap1 = new Bitmap(filename);
            Bitmap bitmap2 = Roberts(bitmap1);
            pictureBox1.Image = bitmap2;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = new Bitmap(filename);
            Bitmap bitmap2 = Sobel(bitmap1);
            pictureBox1.Image = bitmap2;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = new Bitmap(filename);
            Bitmap bitmap2 = Laplace4(bitmap1);
            Bitmap bitmap3 = Laplace8(bitmap1);

            pictureBox1.Image = bitmap2;
            pictureBox1.Image = bitmap3;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = new Bitmap(filename);
            Bitmap bitmap2 = RightBottomEdge(bitmap1);
            pictureBox1.Image = bitmap2;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = new Bitmap(filename);
            Bitmap bitmap2 = Prewitt(bitmap1);
            pictureBox1.Image = bitmap2;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = new Bitmap(filename);
            Bitmap bitmap2 = Robinson(bitmap1);
            pictureBox1.Image = bitmap2;
        }

        private void button7_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = new Bitmap(filename);
            Bitmap bitmap2 = Kirsch(bitmap1);
            pictureBox1.Image = bitmap2;
        }

        private void button8_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = new Bitmap(filename);
            Bitmap bitmap2 = Smoothed(bitmap1);
            pictureBox1.Image = bitmap2;
        }



        //Roberts算子
        //  gx = f(i,j) - f(i+1,j)
        //  gy = f(i+1,j) - f(i,j+1)
        //  g(i,j) = abs(gx) + abs(gy)
        private Bitmap Roberts(Bitmap bmp)
        {
            Bitmap newbmp = new Bitmap(bmp.Width, bmp.Height);
            LockBitmap lbmp = new LockBitmap(bmp);
            LockBitmap newlbmp = new LockBitmap(newbmp);
            lbmp.LockBits();
            newlbmp.LockBits();

            for (int i = 0; i < bmp.Width - 1; i++)
            {
                for (int j = 0; j < bmp.Height - 1; j++)
                {
                    Color c1 = lbmp.GetPixel(i, j);
                    Color c2 = lbmp.GetPixel(i + 1, j);
                    Color c3 = lbmp.GetPixel(i, j + 1);
                    Color c4 = lbmp.GetPixel(i + 1, j + 1);

                    int r = Math.Abs(c1.R - c4.R) + Math.Abs(c2.R - c3.R);
                    int g = Math.Abs(c1.G - c4.G) + Math.Abs(c2.G - c3.G);
                    int b = Math.Abs(c1.B - c4.B) + Math.Abs(c2.B - c3.B);

                    if (r > 255) r = 255;
                    if (g > 255) g = 255;
                    if (b > 255) b = 255;

                    newlbmp.SetPixel(i, j, Color.FromArgb(r, g, b));
                }
            }

            lbmp.UnlockBits();
            newlbmp.UnlockBits();

            return newbmp;
        }


        //Sobel算子
        //  gx = f(i-1,j-1) + 2f(i-1,j) + f(i-1,j+1) - f(i+1,j-1) - 2f(i+1,j) - f(i+1,j+1)
        //  gy = f(i-1,j-1) + 2f(i,j-1) + f(i+1,j-1) - f(i-1,j+1) - 2f(i,j+1) - f(i+1,j+1)
        //  g(i,j) = gx + gy
        private Bitmap Sobel(Bitmap bmp)
        {
            Bitmap newbmp = new Bitmap(bmp.Width, bmp.Height);
            LockBitmap lbmp = new LockBitmap(bmp);
            LockBitmap newlbmp = new LockBitmap(newbmp);
            lbmp.LockBits();
            newlbmp.LockBits();

            for (int i = 1; i < bmp.Width - 1; i++)
            {
                for (int j = 1; j < bmp.Height - 1; j++)
                {
                    Color c1 = lbmp.GetPixel(i - 1, j - 1);
                    Color c2 = lbmp.GetPixel(i, j - 1);
                    Color c3 = lbmp.GetPixel(i + 1, j - 1);
                    Color c4 = lbmp.GetPixel(i - 1, j);
                    Color c6 = lbmp.GetPixel(i + 1, j);
                    Color c7 = lbmp.GetPixel(i - 1, j + 1);
                    Color c8 = lbmp.GetPixel(i, j + 1);
                    Color c9 = lbmp.GetPixel(i + 1, j + 1);

                    int r1 = c1.R + 2 * c4.R + c7.R - c3.R - 2 * c6.R - c9.R;
                    int r2 = c1.R + 2 * c2.R + c3.R - c7.R - 2 * c8.R - c9.R;
                    int g1 = c1.G + 2 * c4.G + c7.G - c3.G - 2 * c6.G - c9.G;
                    int g2 = c1.G + 2 * c2.G + c3.G - c7.G - 2 * c8.G - c9.G;
                    int b1 = c1.B + 2 * c4.B + c7.B - c3.B - 2 * c6.B - c9.B;
                    int b2 = c1.B + 2 * c2.B + c3.B - c7.B - 2 * c8.B - c9.B;

                    int r = Math.Abs(r1) + Math.Abs(r2);
                    int g = Math.Abs(g1) + Math.Abs(g2);
                    int b = Math.Abs(b1) + Math.Abs(b2);

                    if (r > 255) r = 255;
                    if (r < 0) r = 0;
                    if (g > 255) g = 255;
                    if (g < 0) g = 0;
                    if (b > 255) b = 255;
                    if (b < 0) b = 0;

                    newlbmp.SetPixel(i, j, Color.FromArgb(r, g, b));
                    //newlbmp.SetPixel(i, j, Color.FromArgb(r, r, r));
                }
            }

            lbmp.UnlockBits();
            newlbmp.UnlockBits();

            return newbmp;
        }


        //拉普拉斯算子（四邻域）
        //  g(i,j) = abs(4f(i,j) - f(i,j-1) - f(i,j+1) - f(i-1,j) - f(i+1,j))
        private Bitmap Laplace4(Bitmap bmp)
        {
            Bitmap newbmp = new Bitmap(bmp.Width, bmp.Height);
            LockBitmap lbmp = new LockBitmap(bmp);
            LockBitmap newlbmp = new LockBitmap(newbmp);
            lbmp.LockBits();
            newlbmp.LockBits();

            for (int i = 1; i < bmp.Width - 1; i++)
            {
                for (int j = 1; j < bmp.Height - 1; j++)
                {
                    Color c2 = lbmp.GetPixel(i, j - 1);
                    Color c4 = lbmp.GetPixel(i - 1, j);
                    Color c5 = lbmp.GetPixel(i, j);
                    Color c6 = lbmp.GetPixel(i + 1, j);
                    Color c8 = lbmp.GetPixel(i, j + 1);

                    int r = Math.Abs(4 * c5.R - c2.R - c4.R - c6.R - c8.R);
                    int g = Math.Abs(4 * c5.G - c2.G - c4.G - c6.G - c8.G);
                    int b = Math.Abs(4 * c5.B - c2.B - c4.B - c6.B - c8.B);

                    if (r > 255) r = 255;
                    if (r < 0) r = 0;
                    if (g > 255) g = 255;
                    if (g < 0) g = 0;
                    if (b > 255) b = 255;
                    if (b < 0) b = 0;

                    newlbmp.SetPixel(i, j, Color.FromArgb(r, g, b));
                }
            }

            lbmp.UnlockBits();
            newlbmp.UnlockBits();

            return newbmp;
        }
        private Bitmap Laplace8(Bitmap bmp)
        {
            Bitmap newbmp = new Bitmap(bmp.Width, bmp.Height);
            LockBitmap lbmp = new LockBitmap(bmp);
            LockBitmap newlbmp = new LockBitmap(newbmp);
            lbmp.LockBits();
            newlbmp.LockBits();

            for (int i = 1; i < bmp.Width - 1; i++)
            {
                for (int j = 1; j < bmp.Height - 1; j++)
                {
                    Color c1 = lbmp.GetPixel(i - 1, j - 1);
                    Color c2 = lbmp.GetPixel(i, j - 1);
                    Color c3 = lbmp.GetPixel(i + 1, j - 1);
                    Color c4 = lbmp.GetPixel(i - 1, j);
                    Color c5 = lbmp.GetPixel(i, j);
                    Color c6 = lbmp.GetPixel(i + 1, j);
                    Color c7 = lbmp.GetPixel(i - 1, j + 1);
                    Color c8 = lbmp.GetPixel(i, j + 1);
                    Color c9 = lbmp.GetPixel(i + 1, j + 1);

                    int r = Math.Abs(8 * c5.R - c1.R - c2.R - c3.R - c4.R - c6.R - c7.R - c8.R - c9.R);
                    int g = Math.Abs(8 * c5.G - c1.G - c2.G - c3.G - c4.G - c6.G - c7.G - c8.G - c9.G);
                    int b = Math.Abs(8 * c5.B - c1.B - c2.B - c3.B - c4.B - c6.B - c7.B - c8.B - c9.B);

                    if (r > 255) r = 255;
                    if (r < 0) r = 0;
                    if (g > 255) g = 255;
                    if (g < 0) g = 0;
                    if (b > 255) b = 255;
                    if (b < 0) b = 0;

                    newlbmp.SetPixel(i, j, Color.FromArgb(r, g, b));
                }
            }

            lbmp.UnlockBits();
            newlbmp.UnlockBits();

            return newbmp;
        }


        //右下边缘抽出
        //  g(i,j) = abs(2f(i+1,j) + 2f(i,j+1) - 2f(i,j-1) - 2f(i-1,j));
        private Bitmap RightBottomEdge(Bitmap bmp)
        {
            Bitmap newbmp = new Bitmap(bmp.Width, bmp.Height);
            LockBitmap lbmp = new LockBitmap(bmp);
            LockBitmap newlbmp = new LockBitmap(newbmp);
            lbmp.LockBits();
            newlbmp.LockBits();

            for (int i = 1; i < bmp.Width - 1; i++)
            {
                for (int j = 1; j < bmp.Height - 1; j++)
                {
                    Color c2 = lbmp.GetPixel(i, j - 1);
                    Color c4 = lbmp.GetPixel(i - 1, j);
                    Color c6 = lbmp.GetPixel(i + 1, j);
                    Color c8 = lbmp.GetPixel(i, j + 1);

                    int r = 2 * Math.Abs(c6.R + c8.R - c2.R - c4.R);
                    int g = 2 * Math.Abs(c6.G + c8.G - c2.G - c4.G);
                    int b = 2 * Math.Abs(c6.B + c8.B - c2.B - c4.B);

                    if (r > 255) r = 255;
                    if (r < 0) r = 0;
                    if (g > 255) g = 255;
                    if (g < 0) g = 0;
                    if (b > 255) b = 255;
                    if (b < 0) b = 0;

                    newlbmp.SetPixel(i, j, Color.FromArgb(r, g, b));
                }
            }

            lbmp.UnlockBits();
            newlbmp.UnlockBits();

            return newbmp;
        }


        //Prewitt边缘检测样板算子（方向为右下）
        //  g(i,j) = abs(f(i-1,j-1) + f(i,j-1) + f(i+1,j-1) + f(i-1,j) + f(i-1,j+1) - f(i+1,j) - f(i,j+1) - f(i+1,j+1) - 2f(i,j))
        //
        //      右下              右上
        //  1   1   1           1   -1  -1
        //  1   -2  -1          1   -2  -1
        //  1   -1  -1          1   1   1
        //
        //      上               下
        //  -1  -1  -1          1   1   1
        //  1   -2  1           1   -2  1
        //  1   1   1           -1  -1  -1
        private Bitmap Prewitt(Bitmap bmp)
        {
            Bitmap newbmp = new Bitmap(bmp.Width, bmp.Height);
            LockBitmap lbmp = new LockBitmap(bmp);
            LockBitmap newlbmp = new LockBitmap(newbmp);
            lbmp.LockBits();
            newlbmp.LockBits();

            for (int i = 1; i < bmp.Width - 1; i++)
            {
                for (int j = 1; j < bmp.Height - 1; j++)
                {
                    Color c1 = lbmp.GetPixel(i - 1, j - 1);
                    Color c2 = lbmp.GetPixel(i, j - 1);
                    Color c3 = lbmp.GetPixel(i + 1, j - 1);
                    Color c4 = lbmp.GetPixel(i - 1, j);
                    Color c5 = lbmp.GetPixel(i, j);
                    Color c6 = lbmp.GetPixel(i + 1, j);
                    Color c7 = lbmp.GetPixel(i - 1, j + 1);
                    Color c8 = lbmp.GetPixel(i, j + 1);
                    Color c9 = lbmp.GetPixel(i + 1, j + 1);

                    int r = Math.Abs(c1.R + c2.R + c3.R + c4.R + c7.R - c6.R - c8.R - c9.R - 2 * c5.R);
                    int g = Math.Abs(c1.G + c2.G + c3.G + c4.G + c7.G - c6.G - c8.G - c9.G - 2 * c5.R);
                    int b = Math.Abs(c1.B + c2.B + c3.B + c4.B + c7.B - c6.B - c8.B - c9.B - 2 * c5.R);

                    if (r > 255) r = 255;
                    if (r < 0) r = 0;
                    if (g > 255) g = 255;
                    if (g < 0) g = 0;
                    if (b > 255) b = 255;
                    if (b < 0) b = 0;

                    newlbmp.SetPixel(i, j, Color.FromArgb(r, g, b));
                }
            }

            lbmp.UnlockBits();
            newlbmp.UnlockBits();

            return newbmp;
        }


        //Robinson算子（这里使用第一个）
        //Robinson算子有八个样板，这里列出四个，剩余四个为下面四个的取反
        //
        //  1   2   1               0   1   2
        //  0   0   0               -1  0   1
        //  -1  -2  -1              -2  -1  0
        //
        //  -1  0   1               -2  -1  0
        //  -2  0   2               -1  0   1
        //  -1  0   1               0   -1  2
        private Bitmap Robinson(Bitmap bmp)
        {
            Bitmap newbmp = new Bitmap(bmp.Width, bmp.Height);
            LockBitmap lbmp = new LockBitmap(bmp);
            LockBitmap newlbmp = new LockBitmap(newbmp);
            lbmp.LockBits();
            newlbmp.LockBits();

            for (int i = 1; i < bmp.Width - 1; i++)
            {
                for (int j = 1; j < bmp.Height - 1; j++)
                {
                    Color c1 = lbmp.GetPixel(i - 1, j - 1);
                    Color c2 = lbmp.GetPixel(i, j - 1);
                    Color c3 = lbmp.GetPixel(i + 1, j - 1);
                    Color c7 = lbmp.GetPixel(i - 1, j + 1);
                    Color c8 = lbmp.GetPixel(i, j + 1);
                    Color c9 = lbmp.GetPixel(i + 1, j + 1);

                    int r = Math.Abs(c1.R + 2 * c2.R + c3.R - c7.R - 2 * c8.R - c9.R);
                    int g = Math.Abs(c1.G + 2 * c2.G + c3.G - c7.G - 2 * c8.G - c9.G);
                    int b = Math.Abs(c1.B + 2 * c2.B + c3.B - c7.B - 2 * c8.B - c9.B);

                    if (r > 255) r = 255;
                    if (r < 0) r = 0;
                    if (g > 255) g = 255;
                    if (g < 0) g = 0;
                    if (b > 255) b = 255;
                    if (b < 0) b = 0;

                    newlbmp.SetPixel(i, j, Color.FromArgb(r, g, b));
                }
            }

            lbmp.UnlockBits();
            newlbmp.UnlockBits();

            return newbmp;
        }

        //Kirsch算子（这里使用第一个）
        //Kirsch算子有8个边缘样板，与Prewitt边缘样板类似，这里列出一个
        //
        //  5   5   5
        //  -3  0   -3
        //  -3  -3  -3
        //
        private Bitmap Kirsch(Bitmap bmp)
        {
            Bitmap newbmp = new Bitmap(bmp.Width, bmp.Height);
            LockBitmap lbmp = new LockBitmap(bmp);
            LockBitmap newlbmp = new LockBitmap(newbmp);
            lbmp.LockBits();
            newlbmp.LockBits();

            for (int i = 1; i < bmp.Width - 1; i++)
            {
                for (int j = 1; j < bmp.Height - 1; j++)
                {
                    Color c1 = lbmp.GetPixel(i - 1, j - 1);
                    Color c2 = lbmp.GetPixel(i, j - 1);
                    Color c3 = lbmp.GetPixel(i + 1, j - 1);
                    Color c4 = lbmp.GetPixel(i - 1, j);
                    Color c6 = lbmp.GetPixel(i + 1, j);
                    Color c7 = lbmp.GetPixel(i - 1, j + 1);
                    Color c8 = lbmp.GetPixel(i, j + 1);
                    Color c9 = lbmp.GetPixel(i + 1, j + 1);

                    int r = Math.Abs(5 * (c1.R + c2.R + c3.R) - 3 * (c4.R + c6.R + c7.R + c8.R + c9.R));
                    int g = Math.Abs(5 * (c1.G + c2.G + c3.G) - 3 * (c4.G + c6.G + c7.G + c8.G + c9.G));
                    int b = Math.Abs(5 * (c1.B + c2.B + c3.B) - 3 * (c4.B + c6.B + c7.B + c8.B + c9.B));

                    if (r > 255) r = 255;
                    if (r < 0) r = 0;
                    if (g > 255) g = 255;
                    if (g < 0) g = 0;
                    if (b > 255) b = 255;
                    if (b < 0) b = 0;

                    newlbmp.SetPixel(i, j, Color.FromArgb(r, g, b));
                }
            }

            lbmp.UnlockBits();
            newlbmp.UnlockBits();

            return newbmp;
        }


        //Smoothed算子
        //  gx = f(i,j) - f(i+1,j)
        //  gy = f(i+1,j) - f(i,j+1)
        //  g(i,j) = abs(gx) + abs(gy)
        private Bitmap Smoothed(Bitmap bmp)
        {
            Bitmap newbmp = new Bitmap(bmp.Width, bmp.Height);
            LockBitmap lbmp = new LockBitmap(bmp);
            LockBitmap newlbmp = new LockBitmap(newbmp);
            lbmp.LockBits();
            newlbmp.LockBits();

            for (int i = 1; i < bmp.Width - 1; i++)
            {
                for (int j = 1; j < bmp.Height - 1; j++)
                {
                    Color c1 = lbmp.GetPixel(i - 1, j - 1);
                    Color c2 = lbmp.GetPixel(i, j - 1);
                    Color c3 = lbmp.GetPixel(i + 1, j - 1);
                    Color c4 = lbmp.GetPixel(i - 1, j);
                    Color c6 = lbmp.GetPixel(i + 1, j);
                    Color c7 = lbmp.GetPixel(i - 1, j + 1);
                    Color c8 = lbmp.GetPixel(i, j + 1);
                    Color c9 = lbmp.GetPixel(i + 1, j + 1);

                    int r1 = c3.R + c6.R + c9.R - c1.R - c4.R - c7.R;
                    int r2 = c1.R + c2.R + c3.R - c7.R - c8.R - c9.R;

                    int g1 = c3.G + c6.G + c9.G - c1.G - c4.G - c7.G;
                    int g2 = c1.G + c2.G + c3.G - c7.G - c8.G - c9.G;
                    int b1 = c3.B + c6.B + c9.B - c1.B - c4.B - c7.B;
                    int b2 = c1.B + c2.B + c3.B - c7.B - c8.B - c9.B;

                    int r = Math.Abs(r1) + Math.Abs(r2);
                    int g = Math.Abs(g1) + Math.Abs(g2);
                    int b = Math.Abs(b1) + Math.Abs(b2);

                    if (r > 255) r = 255;
                    if (r < 0) r = 0;
                    if (g > 255) g = 255;
                    if (g < 0) g = 0;
                    if (b > 255) b = 255;
                    if (b < 0) b = 0;

                    newlbmp.SetPixel(i, j, Color.FromArgb(r, g, b));
                    //newlbmp.SetPixel(i, j, Color.FromArgb(r, r, r));
                }
            }

            lbmp.UnlockBits();
            newlbmp.UnlockBits();

            return newbmp;
        }

        private void button9_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = Image.FromFile(filename);
        }
    }

    //內存法
    public class LockBitmap
    {
        Bitmap source = null;
        IntPtr Iptr = IntPtr.Zero;
        BitmapData bitmapData = null;

        public byte[] Pixels { get; set; }
        public int Depth { get; private set; }
        public int Width { get; private set; }
        public int Height { get; private set; }

        public LockBitmap(Bitmap source)
        {
            this.source = source;
        }

        /// <summary>
        /// Lock bitmap data
        /// </summary>
        public void LockBits()
        {
            try
            {
                // Get width and height of bitmap
                Width = source.Width;
                Height = source.Height;

                // get total locked pixels count
                int PixelCount = Width * Height;

                // Create rectangle to lock
                Rectangle rect = new Rectangle(0, 0, Width, Height);

                // get source bitmap pixel format size
                Depth = System.Drawing.Bitmap.GetPixelFormatSize(source.PixelFormat);

                // Check if bpp (Bits Per Pixel) is 8, 24, or 32
                if (Depth != 8 && Depth != 24 && Depth != 32)
                {
                    throw new ArgumentException("Only 8, 24 and 32 bpp images are supported.");
                }

                // Lock bitmap and return bitmap data
                bitmapData = source.LockBits(rect, ImageLockMode.ReadWrite,
                                             source.PixelFormat);

                // create byte array to copy pixel values
                int step = Depth / 8;
                Pixels = new byte[PixelCount * step];
                Iptr = bitmapData.Scan0;

                // Copy data from pointer to array
                Marshal.Copy(Iptr, Pixels, 0, Pixels.Length);
            }
            catch (Exception ex)
            {
                throw ex;
            }
        }

        /// <summary>
        /// Unlock bitmap data
        /// </summary>
        public void UnlockBits()
        {
            try
            {
                // Copy data from byte array to pointer
                Marshal.Copy(Pixels, 0, Iptr, Pixels.Length);

                // Unlock bitmap data
                source.UnlockBits(bitmapData);
            }
            catch (Exception ex)
            {
                throw ex;
            }
        }

        /// <summary>
        /// Get the color of the specified pixel
        /// </summary>
        /// <param name="x"></param>
        /// <param name="y"></param>
        /// <returns></returns>
        public Color GetPixel(int x, int y)
        {
            Color clr = Color.Empty;

            // Get color components count
            int cCount = Depth / 8;

            // Get start index of the specified pixel
            int i = ((y * Width) + x) * cCount;

            if (i > Pixels.Length - cCount)
                throw new IndexOutOfRangeException();

            if (Depth == 32) // For 32 bpp get Red, Green, Blue and Alpha
            {
                byte b = Pixels[i];
                byte g = Pixels[i + 1];
                byte r = Pixels[i + 2];
                byte a = Pixels[i + 3]; // a
                clr = Color.FromArgb(a, r, g, b);
            }
            if (Depth == 24) // For 24 bpp get Red, Green and Blue
            {
                byte b = Pixels[i];
                byte g = Pixels[i + 1];
                byte r = Pixels[i + 2];
                clr = Color.FromArgb(r, g, b);
            }
            if (Depth == 8)
            // For 8 bpp get color value (Red, Green and Blue values are the same)
            {
                byte c = Pixels[i];
                clr = Color.FromArgb(c, c, c);
            }
            return clr;
        }

        /// <summary>
        /// Set the color of the specified pixel
        /// </summary>
        /// <param name="x"></param>
        /// <param name="y"></param>
        /// <param name="color"></param>
        public void SetPixel(int x, int y, Color color)
        {
            // Get color components count
            int cCount = Depth / 8;

            // Get start index of the specified pixel
            int i = ((y * Width) + x) * cCount;

            if (Depth == 32) // For 32 bpp set Red, Green, Blue and Alpha
            {
                Pixels[i] = color.B;
                Pixels[i + 1] = color.G;
                Pixels[i + 2] = color.R;
                Pixels[i + 3] = color.A;
            }
            if (Depth == 24) // For 24 bpp set Red, Green and Blue
            {
                Pixels[i] = color.B;
                Pixels[i + 1] = color.G;
                Pixels[i + 2] = color.R;
            }
            if (Depth == 8)
            // For 8 bpp set color value (Red, Green and Blue values are the same)
            {
                Pixels[i] = color.B;
            }
        }
    }

    //指針法
    public class PointBitmap
    {
        Bitmap source = null;
        IntPtr Iptr = IntPtr.Zero;
        BitmapData bitmapData = null;

        public int Depth { get; private set; }
        public int Width { get; private set; }
        public int Height { get; private set; }

        public PointBitmap(Bitmap source)
        {
            this.source = source;
        }

        public void LockBits()
        {
            try
            {
                // Get width and height of bitmap
                Width = source.Width;
                Height = source.Height;

                // get total locked pixels count
                int PixelCount = Width * Height;

                // Create rectangle to lock
                Rectangle rect = new Rectangle(0, 0, Width, Height);

                // get source bitmap pixel format size
                Depth = System.Drawing.Bitmap.GetPixelFormatSize(source.PixelFormat);

                // Check if bpp (Bits Per Pixel) is 8, 24, or 32
                if (Depth != 8 && Depth != 24 && Depth != 32)
                {
                    throw new ArgumentException("Only 8, 24 and 32 bpp images are supported.");
                }

                // Lock bitmap and return bitmap data
                bitmapData = source.LockBits(rect, ImageLockMode.ReadWrite,
                                             source.PixelFormat);

                //得到首地址
                unsafe
                {
                    Iptr = bitmapData.Scan0;
                    //二维图像循环

                }
            }
            catch (Exception ex)
            {
                throw ex;
            }
        }

        public void UnlockBits()
        {
            try
            {
                source.UnlockBits(bitmapData);
            }
            catch (Exception ex)
            {
                throw ex;
            }
        }

        public Color GetPixel(int x, int y)
        {
            unsafe
            {
                byte* ptr = (byte*)Iptr;
                ptr = ptr + bitmapData.Stride * y;
                ptr += Depth * x / 8;
                Color c = Color.Empty;
                if (Depth == 32)
                {
                    int a = ptr[3];
                    int r = ptr[2];
                    int g = ptr[1];
                    int b = ptr[0];
                    c = Color.FromArgb(a, r, g, b);
                }
                else if (Depth == 24)
                {
                    int r = ptr[2];
                    int g = ptr[1];
                    int b = ptr[0];
                    c = Color.FromArgb(r, g, b);
                }
                else if (Depth == 8)
                {
                    int r = ptr[0];
                    c = Color.FromArgb(r, r, r);
                }
                return c;
            }
        }

        public void SetPixel(int x, int y, Color c)
        {
            unsafe
            {
                byte* ptr = (byte*)Iptr;
                ptr = ptr + bitmapData.Stride * y;
                ptr += Depth * x / 8;
                if (Depth == 32)
                {
                    ptr[3] = c.A;
                    ptr[2] = c.R;
                    ptr[1] = c.G;
                    ptr[0] = c.B;
                }
                else if (Depth == 24)
                {
                    ptr[2] = c.R;
                    ptr[1] = c.G;
                    ptr[0] = c.B;
                }
                else if (Depth == 8)
                {
                    ptr[2] = c.R;
                    ptr[1] = c.G;
                    ptr[0] = c.B;
                }
            }
        }
    }

    public class Benchmark
    {
        private static DateTime startDate = DateTime.MinValue;
        private static DateTime endDate = DateTime.MinValue;

        public static TimeSpan Span { get { return endDate.Subtract(startDate); } }

        public static void Start() { startDate = DateTime.Now; }

        public static void End() { endDate = DateTime.Now; }

        public static double GetSeconds()
        {
            if (endDate == DateTime.MinValue) return 0.0;
            else return Span.TotalSeconds;
        }
    }
}
