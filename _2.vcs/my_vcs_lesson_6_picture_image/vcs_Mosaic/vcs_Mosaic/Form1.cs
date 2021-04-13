using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for BitmapData

namespace vcs_Mosaic
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\naruto.jpg";

        int borderwidth = 1;
        int mosaicwidth = 3;
        Color bordercolor = Color.FromArgb(211, 172, 158);

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
            Bitmap bitmap2 = CreateMosaicImage(bitmap1);
            pictureBox1.Image = bitmap2;
        }

        //重設大小
        public Bitmap Resize(Bitmap source, Size size)
        {
            int widthskip = source.Width / size.Width;
            int heightskip = source.Height / size.Height;

            Bitmap bmp = new Bitmap(size.Width, size.Height);

            PointBitmap pbmp = new PointBitmap(source);
            PointBitmap newpbmp = new PointBitmap(bmp);

            pbmp.LockBits();
            newpbmp.LockBits();

            for (int height = 0; height < newpbmp.Height; height++)
            {
                for (int width = 0; width < newpbmp.Width; width++)
                {
                    int x = width > 0 ? 1 + (width - 1) * widthskip : 0;
                    int y = height > 0 ? 1 + (height - 1) * heightskip : 0;
                    Color c = pbmp.GetPixel(x, y);
                    newpbmp.SetPixel(width, height, c);
                }
            }

            pbmp.UnlockBits();
            newpbmp.UnlockBits();

            return bmp;
        }

        //生成马赛克图像
        public Bitmap CreateMosaicImage(Bitmap source)
        {
            //计算新图像需要的尺寸
            int widthcount = source.Width / mosaicwidth;
            int heightcount = source.Height / mosaicwidth;

            int newwidth = widthcount * mosaicwidth + (widthcount + 1) * borderwidth;
            int newheight = heightcount * mosaicwidth + (heightcount + 1) * borderwidth;

            Bitmap bmp = new Bitmap(newwidth, newheight);
            source = Resize(source, new Size(widthcount, heightcount));

            PointBitmap sourcepbmp = new PointBitmap(source);
            PointBitmap newpbmp = new PointBitmap(bmp);
            sourcepbmp.LockBits();
            newpbmp.LockBits();

            //绘制背景
            for (int height = 0; height < newpbmp.Height; height++)
            {
                for (int width = 0; width < newpbmp.Width; width++)
                {
                    newpbmp.SetPixel(width, height, bordercolor);
                }
            }

            for (int height = 0; height < sourcepbmp.Height; height++)
            {
                for (int width = 0; width < sourcepbmp.Width; width++)
                {
                    int x = borderwidth * (width + 1) + mosaicwidth * width;
                    int y = borderwidth * (height + 1) + mosaicwidth * height;

                    Color c = sourcepbmp.GetPixel(width, height);

                    for (int k = 0; k < mosaicwidth; k++, y++, x -= mosaicwidth)
                    {
                        for (int l = 0; l < mosaicwidth; l++, x++)
                        {
                            newpbmp.SetPixel(x, y, c);
                        }
                    }
                }
            }
            sourcepbmp.UnlockBits();
            newpbmp.UnlockBits();
            return bmp;
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
}
