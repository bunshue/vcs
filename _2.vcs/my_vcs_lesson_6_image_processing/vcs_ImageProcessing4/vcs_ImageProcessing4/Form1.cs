using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for BitmapData
using System.Drawing.Drawing2D; //for InterpolationMode
using System.Runtime.InteropServices;   //for Marshal

namespace vcs_ImageProcessing4
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
            show_item_location();
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

            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            button20.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            pictureBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = Image.FromFile(filename);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //旋轉（90度，180度，270度）
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
            //底片效果（反色）（255-r, 255-g, 255-b）
            Bitmap bitmap1 = new Bitmap(filename);
            Bitmap bitmap2 = NegativeImage(bitmap1);
            pictureBox1.Image = bitmap2;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //黑白效果
            Bitmap bitmap1 = new Bitmap(filename);
            Bitmap bitmap2 = GrayImage(bitmap1, 1);
            pictureBox1.Image = bitmap2;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //浮雕：找出附近的像素點r1，abs（r-r2+128）
            Bitmap bitmap1 = new Bitmap(filename);
            Bitmap bitmap2 = EmbossmentImage(bitmap1);
            pictureBox1.Image = bitmap2;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //柔化
            Bitmap bitmap1 = new Bitmap(filename);
            Bitmap bitmap2 = SoftenImage(bitmap1);
            pictureBox1.Image = bitmap2;
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //銳化
            Bitmap bitmap1 = new Bitmap(filename);
            Bitmap bitmap2 = SharpenImage(bitmap1);
            pictureBox1.Image = bitmap2;
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //霧化
            Bitmap bitmap1 = new Bitmap(filename);
            Bitmap bitmap2 = AtomizationImage(bitmap1);
            pictureBox1.Image = bitmap2;
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

        //底片
        public Bitmap NegativeImage(Bitmap bmp)
        {
            int H = bmp.Height;
            int W = bmp.Width;
            Bitmap newbmp = new Bitmap(W, H);

            LockBitmap lbmp = new LockBitmap(bmp);
            LockBitmap newlbmp = new LockBitmap(newbmp);
            lbmp.LockBits();
            newlbmp.LockBits();

            Color pixel;
            for (int x = 1; x < W; x++)
            {
                for (int y = 1; y < H; y++)
                {
                    int r, g, b;
                    pixel = lbmp.GetPixel(x, y);
                    r = 255 - pixel.R;
                    g = 255 - pixel.G;
                    b = 255 - pixel.B;
                    newlbmp.SetPixel(x, y, Color.FromArgb(r, g, b));
                }
            }
            lbmp.UnlockBits();
            newlbmp.UnlockBits();
            return newbmp;
        }

        //黑白
        public Bitmap GrayImage(Bitmap bmp, int type)
        {
            int H = bmp.Height;
            int W = bmp.Width;
            Bitmap newbmp = new Bitmap(W, H);

            LockBitmap lbmp = new LockBitmap(bmp);
            LockBitmap newlbmp = new LockBitmap(newbmp);
            lbmp.LockBits();
            newlbmp.LockBits();

            Color pixel;
            for (int x = 0; x < W; x++)
            {
                for (int y = 0; y < H; y++)
                {
                    pixel = lbmp.GetPixel(x, y);
                    int r, g, b, Result = 0;
                    r = pixel.R;
                    g = pixel.G;
                    b = pixel.B;
                    switch (type)
                    {
                        case 0://平均值法
                            Result = ((r + g + b) / 3);
                            break;
                        case 1://最大值法
                            Result = r > g ? r : g;
                            Result = Result > b ? Result : b;
                            break;
                        case 2://加權平均值法
                            Result = ((int)(0.3 * r) + (int)(0.59 * g) + (int)(0.11 * b));
                            break;
                    }
                    newlbmp.SetPixel(x, y, Color.FromArgb(Result, Result, Result));
                }
            }
            lbmp.UnlockBits();
            newlbmp.UnlockBits();
            return newbmp;
        }

        //浮雕
        public Bitmap EmbossmentImage(Bitmap bmp)
        {
            int H = bmp.Height;
            int W = bmp.Width;
            Bitmap newbmp = new Bitmap(W, H);

            LockBitmap lbmp = new LockBitmap(bmp);
            LockBitmap newlbmp = new LockBitmap(newbmp);
            lbmp.LockBits();
            newlbmp.LockBits();

            Color pixel1, pixel2;
            for (int x = 0; x < W - 1; x++)
            {
                for (int y = 0; y < H - 1; y++)
                {
                    int r = 0, g = 0, b = 0;
                    pixel1 = lbmp.GetPixel(x, y);
                    pixel2 = lbmp.GetPixel(x + 1, y + 1);
                    r = Math.Abs(pixel1.R - pixel2.R + 128);
                    g = Math.Abs(pixel1.G - pixel2.G + 128);
                    b = Math.Abs(pixel1.B - pixel2.B + 128);
                    if (r > 255)
                        r = 255;
                    if (r < 0)
                        r = 0;
                    if (g > 255)
                        g = 255;
                    if (g < 0)
                        g = 0;
                    if (b > 255)
                        b = 255;
                    if (b < 0)
                        b = 0;
                    newlbmp.SetPixel(x, y, Color.FromArgb(r, g, b));
                }
            }
            lbmp.UnlockBits();
            newlbmp.UnlockBits();
            return newbmp;
        }

        //柔化
        public Bitmap SoftenImage(Bitmap bmp)
        {
            int H = bmp.Height;
            int W = bmp.Width;
            Bitmap newbmp = new Bitmap(W, H);

            LockBitmap lbmp = new LockBitmap(bmp);
            LockBitmap newlbmp = new LockBitmap(newbmp);
            lbmp.LockBits();
            newlbmp.LockBits();

            Color pixel;
            //高斯模板
            int[] Gauss = { 1, 2, 1, 2, 4, 2, 1, 2, 1 };
            for (int x = 1; x < W - 1; x++)
            {
                for (int y = 1; y < H - 1; y++)
                {
                    int r = 0, g = 0, b = 0;
                    int Index = 0;
                    for (int col = -1; col <= 1; col++)
                    {
                        for (int row = -1; row <= 1; row++)
                        {
                            pixel = lbmp.GetPixel(x + row, y + col);
                            r += pixel.R * Gauss[Index];
                            g += pixel.G * Gauss[Index];
                            b += pixel.B * Gauss[Index];
                            Index++;
                        }
                    }
                    r /= 16;
                    g /= 16;
                    b /= 16;
                    //處理顏色值溢出
                    r = r > 255 ? 255 : r;
                    r = r < 0 ? 0 : r;
                    g = g > 255 ? 255 : g;
                    g = g < 0 ? 0 : g;
                    b = b > 255 ? 255 : b;
                    b = b < 0 ? 0 : b;
                    newlbmp.SetPixel(x - 1, y - 1, Color.FromArgb(r, g, b));
                }
            }
            lbmp.UnlockBits();
            newlbmp.UnlockBits();
            return newbmp;
        }

        //銳化
        public Bitmap SharpenImage(Bitmap bmp)
        {
            int H = bmp.Height;
            int W = bmp.Width;
            Bitmap newbmp = new Bitmap(W, H);

            LockBitmap lbmp = new LockBitmap(bmp);
            LockBitmap newlbmp = new LockBitmap(newbmp);
            lbmp.LockBits();
            newlbmp.LockBits();

            //拉普拉斯模板
            int[] Laplacian = { -1, -1, -1, -1, 9, -1, -1, -1, -1 };
            for (int i = 1; i < W - 1; i++)
            {
                for (int j = 1; j < H - 1; j++)
                {
                    int r = 0, g = 0, b = 0;
                    int index = 0;
                    for (int col = -1; col <= 1; col++)
                    {
                        for (int row = -1; row <= 1; row++)
                        {
                            Color color = lbmp.GetPixel(i + row, j + col);
                            r += color.R * Laplacian[index];
                            g += color.G * Laplacian[index];
                            b += color.B * Laplacian[index];
                            index++;
                        }
                    }
                    //處理顏色值溢出
                    r = r > 255 ? 255 : r;
                    r = r < 0 ? 0 : r;
                    g = g > 255 ? 255 : g;
                    g = g < 0 ? 0 : g;
                    b = b > 255 ? 255 : b;
                    b = b < 0 ? 0 : b;
                    newlbmp.SetPixel(i - 1, j - 1, Color.FromArgb(r, g, b));
                }
            }
            lbmp.UnlockBits();
            newlbmp.UnlockBits();
            return newbmp;
        }

        //霧化
        public Bitmap AtomizationImage(Bitmap bmp)
        {
            int H = bmp.Height;
            int W = bmp.Width;
            Bitmap newbmp = new Bitmap(W, H);

            LockBitmap lbmp = new LockBitmap(bmp);
            LockBitmap newlbmp = new LockBitmap(newbmp);
            lbmp.LockBits();
            newlbmp.LockBits();

            System.Random MyRandom = new Random();
            Color pixel;
            for (int x = 1; x < W - 1; x++)
            {
                for (int y = 1; y < H - 1; y++)
                {
                    int k = MyRandom.Next(123456);
                    //像素塊大小
                    int dx = x + k % 19;
                    int dy = y + k % 19;
                    if (dx >= W)
                        dx = W - 1;
                    if (dy >= H)
                        dy = H - 1;
                    pixel = lbmp.GetPixel(dx, dy);
                    newlbmp.SetPixel(x, y, pixel);
                }
            }
            lbmp.UnlockBits();
            newlbmp.UnlockBits();
            return newbmp;
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //向右旋轉圖像90°
            Graphics g = this.pictureBox1.CreateGraphics();
            Bitmap bitmap1 = new Bitmap(filename);//加載圖像
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
            int width = bitmap1.Width;
            int height = bitmap1.Height;
            // 改變圖像大小使用低質量的模式
            g.InterpolationMode = InterpolationMode.NearestNeighbor;
            g.DrawImage(bitmap1, new Rectangle(10, 10, 120, 120), // source rectangle

            new Rectangle(0, 0, width, height), // destination rectangle
            GraphicsUnit.Pixel);
            // 使用高質量模式
            //g.CompositingQuality = CompositingQuality.HighSpeed;
            g.InterpolationMode = InterpolationMode.HighQualityBicubic;
            g.DrawImage(
            bitmap1,
            new Rectangle(130, 10, 120, 120),
            new Rectangle(0, 0, width, height),
            GraphicsUnit.Pixel);

        }

        private void button15_Click(object sender, EventArgs e)
        {
            //轉成灰階
            pictureBox1.Image = Image.FromFile(filename);

            pictureBox1.Image = ConvertToGrayscale(pictureBox1.Image);
        }

        private void button16_Click(object sender, EventArgs e)
        {
            //轉成灰階
            pictureBox1.Image = Image.FromFile(filename);

            pictureBox1.Image = ConvertToGrayscale_CM(pictureBox1.Image);
        }

        private void button17_Click(object sender, EventArgs e)
        {
            //透明度
            pictureBox1.Image = Image.FromFile(filename);

            pictureBox1.Image = ConvertToTransparency(pictureBox1.Image);
        }

        private void button18_Click(object sender, EventArgs e)
        {
            //旋轉
            pictureBox1.Image = Image.FromFile(filename);

            pictureBox1.Image = ConvertToRotate(pictureBox1.Image);
        }

        private void button19_Click(object sender, EventArgs e)
        {

        }


        public Bitmap ConvertToGrayscale(Image image) // Image 是抽象基底類別
        {
            Bitmap source = (Bitmap)image;  // Image 是 Bitmap 的父類別
            Bitmap dest = new Bitmap(source.Width, source.Height); //新增一樣寬高的點陣圖物件

            for (int y = 0; y < dest.Height; y++)
            {
                for (int x = 0; x < dest.Width; x++)
                {
                    Color c = source.GetPixel(x, y); // 得到 原始像素 的 Color
                    int luma = (int)(c.R * 0.3 + c.G * 0.6 + c.B * 0.1);  // 以 3:6:1 的比例得到設定值
                    dest.SetPixel(x, y, Color.FromArgb(luma, luma, luma)); // 寫入 像素値
                }
            }
            return dest;
        }

        // 使用色彩矩陣來調整影像色彩
        public Bitmap ConvertToGrayscale_CM(Image image)
        {
            Bitmap dest = new Bitmap(image.Width, image.Height);
            Graphics g = Graphics.FromImage(dest); // 從點陣圖 建立 新的畫布

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
            g.DrawImage(image, new Rectangle(0, 0, image.Width, image.Height), 0, 0, image.Width, image.Height, GraphicsUnit.Pixel, ia);
            g.Dispose();

            return dest;
        }

        public Bitmap ConvertToTransparency(Image image)
        {
            Bitmap dest = new Bitmap(image.Width, image.Height);
            Graphics g = Graphics.FromImage(dest);

            ImageAttributes ia = new ImageAttributes();

            ColorMatrix cm = new ColorMatrix();

            cm.Matrix33 = 0.5f; // 透明度

            ia.SetColorMatrix(cm);

            g.DrawImage(image, new Rectangle(0, 0, image.Width, image.Height), 0, 0, image.Width, image.Height, GraphicsUnit.Pixel, ia);
            g.Dispose();

            return dest;
        }

        public Bitmap ConvertToRotate(Image image)
        {
            Bitmap dest = new Bitmap(image.Width, image.Height);
            Graphics g = Graphics.FromImage(dest);

            Matrix mx = new Matrix();

            mx.Rotate(30);
            g.Transform = mx;

            g.DrawImage(image, new Rectangle(0, 0, image.Width, image.Height));

            g.Dispose();

            return dest;
        }

        private void button20_Click(object sender, EventArgs e)
        {

        }

        private void button21_Click(object sender, EventArgs e)
        {

        }

        private void button22_Click(object sender, EventArgs e)
        {

        }

        private void button23_Click(object sender, EventArgs e)
        {

        }

        private void button24_Click(object sender, EventArgs e)
        {

        }

        private void button25_Click(object sender, EventArgs e)
        {

        }

        private void button26_Click(object sender, EventArgs e)
        {

        }

        private void button27_Click(object sender, EventArgs e)
        {

        }

        private void button28_Click(object sender, EventArgs e)
        {

        }

        private void button29_Click(object sender, EventArgs e)
        {

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
                Depth = Bitmap.GetPixelFormatSize(source.PixelFormat);

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
                Depth = Bitmap.GetPixelFormatSize(source.PixelFormat);

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
                    //二維圖像循環

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
            if (endDate == DateTime.MinValue)
            {
                return 0.0;
            }
            else
            {
                return Span.TotalSeconds;
            }
        }
    }
}
