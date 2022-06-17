using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;
using System.Drawing.Imaging;   //for BitmapData

namespace vcs_ImageProcessingNew
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            string filename = @"C:\______test_files\picture1.jpg";
            pictureBox1.Image = Image.FromFile(filename);
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
            dx = 170;
            dy = 80;

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

        }


        private void button0_Click(object sender, EventArgs e)
        {
            //底片效果
            //底片效果
            //原理: GetPixel方法獲得每一點像素的值, 然後再使用SetPixel方法將取反後的顏色值設置到對應的點.
            //以底片效果顯示圖像
            try
            {
                int Height = this.pictureBox1.Image.Height;
                int Width = this.pictureBox1.Image.Width;
                Bitmap newbitmap = new Bitmap(Width, Height);
                Bitmap oldbitmap = (Bitmap)this.pictureBox1.Image;
                Color pixel;
                for (int x = 1; x < Width; x++)
                {
                    for (int y = 1; y < Height; y++)
                    {
                        int r, g, b;
                        pixel = oldbitmap.GetPixel(x, y);
                        r = 255 - pixel.R;
                        g = 255 - pixel.G;
                        b = 255 - pixel.B;
                        newbitmap.SetPixel(x, y, Color.FromArgb(r, g, b));
                    }
                }
                this.pictureBox1.Image = newbitmap;
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "信息提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //浮雕效果1
            //浮雕效果
            //原理: 對圖像像素點的像素值分別與相鄰像素點的像素值相減後加上128, 然後將其作為新的像素點的值
            //以浮雕效果顯示圖像
            //C#實現浮雕效果顯示圖片

            /*
            使圖像產生浮雕的效果，主要通過對圖像像素點的像素值分別與相鄰像素點的像素值相減後加上128，然後將其作為新的像素點的值。
            以浮雕效果顯示圖像主要通過GetPixel方法獲得每一點像素的值，通過SetPixel設置該像素點的像素值。
            */

            try
            {
                int Height = this.pictureBox1.Image.Height;
                int Width = this.pictureBox1.Image.Width;
                Bitmap newBitmap = new Bitmap(Width, Height);
                Bitmap oldBitmap = (Bitmap)this.pictureBox1.Image;
                Color pixel1, pixel2;
                for (int x = 0; x < Width - 1; x++)
                {
                    for (int y = 0; y < Height - 1; y++)
                    {
                        int r = 0, g = 0, b = 0;
                        pixel1 = oldBitmap.GetPixel(x, y);
                        pixel2 = oldBitmap.GetPixel(x + 1, y + 1);
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
                        newBitmap.SetPixel(x, y, Color.FromArgb(r, g, b));
                    }
                }
                this.pictureBox1.Image = newBitmap;
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "信息提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            //浮雕效果2
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //圖像邊緣提取
            /*
用到的算法是robert算子，這是一種比較簡單的算法：
f(x,y)=sqrt((g(x,y)-g(x+1,y+1))^2+(g(x+1,y)-g(x,y+1))^2)
*/

            //圖像邊緣提取
            Image_Test();
        }

        private void Image_Test()
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
                    byte* pin_1 = (byte*)(bitmapdata1.Scan0.ToPointer());
                    byte* pin_2 = pin_1 + (bitmapdata1.Stride);
                    byte* pout = (byte*)(bitmapdata2.Scan0.ToPointer());
                    for (int y = 0; y < bitmapdata1.Height - 1; y++)
                    {
                        for (int x = 0; x < bitmapdata1.Width; x++)
                        {
                            //使用robert算子
                            double b = System.Math.Sqrt(((double)pin_1[0] - (double)(pin_2[0] + 3)) * ((double)pin_1[0] - (double)(pin_2[0] + 3)) + ((double)(pin_1[0] + 3) - (double)pin_2[0]) * ((double)(pin_1[0] + 3) - (double)pin_2[0]));
                            double g = System.Math.Sqrt(((double)pin_1[1] - (double)(pin_2[1] + 3)) * ((double)pin_1[1] - (double)(pin_2[1] + 3)) + ((double)(pin_1[1] + 3) - (double)pin_2[1]) * ((double)(pin_1[1] + 3) - (double)pin_2[1]));
                            double r = System.Math.Sqrt(((double)pin_1[2] - (double)(pin_2[2] + 3)) * ((double)pin_1[2] - (double)(pin_2[2] + 3)) + ((double)(pin_1[2] + 3) - (double)pin_2[2]) * ((double)(pin_1[2] + 3) - (double)pin_2[2]));
                            double bgr = b + g + r;//博主一直在糾結要不要除以3，感覺沒差，選阈值的時候調整一下就好了- -

                            if (bgr > 80) //阈值，超過阈值判定為邊緣（選取適當的阈值）
                            {
                                b = 0;
                                g = 0;
                                r = 0;
                            }
                            else
                            {
                                b = 255;
                                g = 255;
                                r = 255;
                            }
                            pout[0] = (byte)(b);
                            pout[1] = (byte)(g);
                            pout[2] = (byte)(r);
                            pin_1 = pin_1 + 3;
                            pin_2 = pin_2 + 3;
                            pout = pout + 3;

                        }
                        pin_1 += bitmapdata1.Stride - bitmapdata1.Width * 3;
                        pin_2 += bitmapdata1.Stride - bitmapdata1.Width * 3;
                        pout += bitmapdata2.Stride - bitmapdata2.Width * 3;
                    }

                    /*
                    //這裡博主加粗了一下線條- -，不喜歡的同學可以刪了這段代碼
                    byte* pin_5 = (byte*)(bitmapdata2.Scan0.ToPointer());
                    for (int y = 0; y < bitmapdata1.Height - 1; y++)
                    {
                        for (int x = 3; x < bitmapdata1.Width; x++)
                        {
                            if (pin_5[0] == 0 && pin_5[1] == 0 && pin_5[2] == 0)
                            {
                                pin_5[-3] = 0;
                                pin_5[-2] = 0;
                                pin_5[-1] = 0;      //邊緣點的前一個像素點置為黑色（注意一定要是遍歷過的像素點）                                                    
                            }
                            pin_5 += 3;

                        }
                        pin_5 += bitmapdata2.Stride - bitmapdata2.Width * 3;
                    }
                    */

                    /*
                    //這段代碼是把原圖和邊緣圖重合
                    byte* pin_3 = (byte*)(bitmapdata1.Scan0.ToPointer());
                    byte* pin_4 = (byte*)(bitmapdata2.Scan0.ToPointer());
                    for (int y = 0; y < bitmapdata1.Height - 1; y++)
                    {
                        for (int x = 0; x < bitmapdata1.Width; x++)
                        {
                            if (pin_4[0] == 255 && pin_4[1] == 255 && pin_4[2] == 255)
                            {
                                pin_4[0] = pin_3[0];
                                pin_4[1] = pin_3[1];
                                pin_4[2] = pin_3[2];
                            }
                            pin_3 += 3;
                            pin_4 += 3;
                        }
                        pin_3 += bitmapdata1.Stride - bitmapdata1.Width * 3;
                        pin_4 += bitmapdata2.Stride - bitmapdata2.Width * 3;
                    }
                    */

                    bitmap1.UnlockBits(bitmapdata1);
                    bitmap2.UnlockBits(bitmapdata2);

                    pictureBox1.Image = bitmap2;
                }
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //圖像邊緣提取2
            //圖像邊緣提取

            /*
            用到的算法是robert算子，這是一種比較簡單的算法：

            f(x,y)=sqrt((g(x,y)-g(x+1,y+1))^2+(g(x+1,y)-g(x,y+1))^2)

            博主一共寫了三段代碼，第一段是邊緣提取，第二段是線條加粗，第三段是原圖和邊緣圖重合，三段代碼可以放在一起，但為了看得清晰我就把他們分開了。
            */

            string filename = @"C:\______test_files\picture1.jpg";
            pictureBox1.Image = Image.FromFile(filename);

            if (this.pictureBox1.Image != null)
            {

                int Height = this.pictureBox1.Image.Height;
                int Width = this.pictureBox1.Image.Width;
                Bitmap bitmap = new Bitmap(Width, Height, PixelFormat.Format24bppRgb);
                Bitmap MyBitmap = (Bitmap)this.pictureBox1.Image;
                BitmapData oldData = MyBitmap.LockBits(new Rectangle(0, 0, Width, Height), ImageLockMode.ReadOnly, PixelFormat.Format24bppRgb); //原圖
                BitmapData newData = bitmap.LockBits(new Rectangle(0, 0, Width, Height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);  //新圖即邊緣圖
                unsafe
                {
                    //首先第一段代碼是提取邊緣，邊緣置為黑色，其他部分置為白色
                    byte* pin_1 = (byte*)(oldData.Scan0.ToPointer());
                    byte* pin_2 = pin_1 + (oldData.Stride);
                    byte* pout = (byte*)(newData.Scan0.ToPointer());
                    for (int y = 0; y < oldData.Height - 1; y++)
                    {
                        for (int x = 0; x < oldData.Width; x++)
                        {
                            //使用robert算子
                            double b = System.Math.Sqrt(((double)pin_1[0] - (double)(pin_2[0] + 3)) * ((double)pin_1[0] - (double)(pin_2[0] + 3)) + ((double)(pin_1[0] + 3) - (double)pin_2[0]) * ((double)(pin_1[0] + 3) - (double)pin_2[0]));
                            double g = System.Math.Sqrt(((double)pin_1[1] - (double)(pin_2[1] + 3)) * ((double)pin_1[1] - (double)(pin_2[1] + 3)) + ((double)(pin_1[1] + 3) - (double)pin_2[1]) * ((double)(pin_1[1] + 3) - (double)pin_2[1]));
                            double r = System.Math.Sqrt(((double)pin_1[2] - (double)(pin_2[2] + 3)) * ((double)pin_1[2] - (double)(pin_2[2] + 3)) + ((double)(pin_1[2] + 3) - (double)pin_2[2]) * ((double)(pin_1[2] + 3) - (double)pin_2[2]));
                            double bgr = b + g + r;//博主一直在糾結要不要除以3，感覺沒差，選阈值的時候調整一下就好了- -

                            if (bgr > 80) //阈值，超過阈值判定為邊緣（選取適當的阈值）
                            {
                                b = 0;
                                g = 0;
                                r = 0;
                            }
                            else
                            {
                                b = 255;
                                g = 255;
                                r = 255;
                            }
                            pout[0] = (byte)(b);
                            pout[1] = (byte)(g);
                            pout[2] = (byte)(r);
                            pin_1 = pin_1 + 3;
                            pin_2 = pin_2 + 3;
                            pout = pout + 3;

                        }
                        pin_1 += oldData.Stride - oldData.Width * 3;
                        pin_2 += oldData.Stride - oldData.Width * 3;
                        pout += newData.Stride - newData.Width * 3;
                    }

                    //這裡博主加粗了一下線條- -，不喜歡的同學可以刪了這段代碼
                    byte* pin_5 = (byte*)(newData.Scan0.ToPointer());
                    for (int y = 0; y < oldData.Height - 1; y++)
                    {
                        for (int x = 3; x < oldData.Width; x++)
                        {
                            if (pin_5[0] == 0 && pin_5[1] == 0 && pin_5[2] == 0)
                            {
                                pin_5[-3] = 0;
                                pin_5[-2] = 0;
                                pin_5[-1] = 0;      //邊緣點的前一個像素點置為黑色（注意一定要是遍歷過的像素點）                                                    
                            }
                            pin_5 += 3;

                        }
                        pin_5 += newData.Stride - newData.Width * 3;
                    }

                    //這段代碼是把原圖和邊緣圖重合
                    byte* pin_3 = (byte*)(oldData.Scan0.ToPointer());
                    byte* pin_4 = (byte*)(newData.Scan0.ToPointer());
                    for (int y = 0; y < oldData.Height - 1; y++)
                    {
                        for (int x = 0; x < oldData.Width; x++)
                        {
                            if (pin_4[0] == 255 && pin_4[1] == 255 && pin_4[2] == 255)
                            {
                                pin_4[0] = pin_3[0];
                                pin_4[1] = pin_3[1];
                                pin_4[2] = pin_3[2];
                            }
                            pin_3 += 3;
                            pin_4 += 3;
                        }
                        pin_3 += oldData.Stride - oldData.Width * 3;
                        pin_4 += newData.Stride - newData.Width * 3;
                    }
                    //......
                    bitmap.UnlockBits(newData);
                    MyBitmap.UnlockBits(oldData);
                    this.pictureBox1.Image = bitmap;
                }
            }
        }

        int borderwidth = 1;
        int mosaicwidth = 3;
        Color bordercolor = Color.FromArgb(211, 172, 158);
        private void button5_Click(object sender, EventArgs e)
        {
            //馬賽克效果1
            string filename = @"C:\______test_files\naruto.jpg";
            Bitmap bitmap1 = new Bitmap(filename);
            Bitmap bitmap2 = CreateMosaicImage(bitmap1);
            pictureBox1.Image = bitmap1;
            pictureBox2.Image = bitmap2;
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

        private void button6_Click(object sender, EventArgs e)
        {
            //馬賽克效果2
            //C#處理數碼相片之馬賽克的實現
            string filename = @"C:\______test_files\elephant.jpg";
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            pictureBox1.Image = bitmap1;
            int val = 10;
            Bitmap bitmap2 = KiMosaic(bitmap1, val);
            pictureBox2.Image = bitmap2;


            //讀取圖檔
            pictureBox1.Image = Image.FromFile(filename);
        }

        //馬賽克算法很簡單，說白了就是把一張圖片分割成若干個val * val像素的小區塊（可能在邊緣有零星的小塊，但不影響整體算法），每個小區塊的顏色都是相同的。
        public static Bitmap KiMosaic(Bitmap b, int val)
        {
            if (b.Equals(null))
            {
                return null;
            }
            int w = b.Width;
            int h = b.Height;
            int stdR, stdG, stdB;
            stdR = 0;
            stdG = 0;
            stdB = 0;
            BitmapData srcData = b.LockBits(new Rectangle(0, 0, w, h), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            unsafe
            {
                byte* p = (byte*)srcData.Scan0.ToPointer();
                for (int y = 0; y < h; y++)
                {
                    for (int x = 0; x < w; x++)
                    {
                        if (y % val == 0)
                        {
                            if (x % val == 0)
                            {
                                stdR = p[2]; stdG = p[1]; stdB = p[0];
                            }
                            else
                            {
                                p[0] = (byte)stdB;
                                p[1] = (byte)stdG;
                                p[2] = (byte)stdR;
                            }
                        }
                        else
                        {
                            // 復制上一行
                            byte* pTemp = p - srcData.Stride;
                            p[0] = (byte)pTemp[0];
                            p[1] = (byte)pTemp[1];
                            p[2] = (byte)pTemp[2];
                        }
                        p += 3;
                    } // end of x
                    p += srcData.Stride - w * 3;
                } // end of y
                b.UnlockBits(srcData);
            }
            return b;
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //色階調整
            //色階調整

            string filename = @"C:\______test_files\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式

            Bitmap bitmap2 = img_color_gradation(bitmap1, 0, 100, 0);

            pictureBox1.Image = bitmap2;


        }

        //色階調整
        public static unsafe Bitmap img_color_gradation(Bitmap src, int r, int g, int b)
        {
            int width = src.Width;
            int height = src.Height;
            Bitmap back = new Bitmap(width, height);
            Rectangle rect = new Rectangle(0, 0, width, height);
            //這種速度最快  
            BitmapData bmpData = src.LockBits(rect, ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);//24位rgb顯示一個像素，即一個像素點3個字節，每個字節是BGR分量。Format32bppRgb是用4個字節表示一個像素  
            byte* ptr = (byte*)(bmpData.Scan0);
            for (int j = 0; j < height; j++)
            {
                for (int i = 0; i < width; i++)
                {
                    //ptr[2]爲r值，ptr[1]爲g值，ptr[0]爲b值  
                    int red = ptr[2] + r; if (red > 255) red = 255; if (red < 0) red = 0;
                    int green = ptr[1] + g; if (green > 255) green = 255; if (green < 0) green = 0;
                    int blue = ptr[0] + b; if (blue > 255) blue = 255; if (blue < 0) blue = 0;
                    back.SetPixel(i, j, Color.FromArgb(red, green, blue));
                    ptr += 3; //Format24bppRgb格式每個像素佔3字節  
                }
                ptr += bmpData.Stride - bmpData.Width * 3;//每行讀取到最後“有用”數據時，跳過未使用空間XX  
            }
            src.UnlockBits(bmpData);
            return back;
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //使用ColorMatrix圖片亮度處理


            //圖片亮度處理

            //亮度百分比

            int percent = 50;

            Single v = 0.006F * percent;

            Single[][] matrix = {         

                new Single[] { 1, 0, 0, 0, 0 },         

                new Single[] { 0, 1, 0, 0, 0 },          

                new Single[] { 0, 0, 1, 0, 0 },         

                new Single[] { 0, 0, 0, 1, 0 },         

                new Single[] { v, v, v, 0, 1 }     

            };

            System.Drawing.Imaging.ColorMatrix cm = new System.Drawing.Imaging.ColorMatrix(matrix);

            System.Drawing.Imaging.ImageAttributes attr = new System.Drawing.Imaging.ImageAttributes();

            attr.SetColorMatrix(cm);

            string filename = @"C:\______test_files\picture1.jpg";

            Image tmp = Image.FromFile(filename);



            this.pictureBox1.Image = Image.FromFile(filename);



            Graphics g = Graphics.FromImage(tmp);

            try
            {

                Rectangle destRect = new Rectangle(0, 0, tmp.Width, tmp.Height);

                g.DrawImage(tmp, destRect, 0, 0, tmp.Width, tmp.Height, GraphicsUnit.Pixel, attr);

            }

            finally
            {

                g.Dispose();

            }



            this.pictureBox2.Image = (Image)tmp.Clone();

        }

        private void button9_Click(object sender, EventArgs e)
        {
            //使用ColorMatrix取灰度
            string filename = @"C:\______test_files\picture1.jpg";

            //取灰度
            this.pictureBox1.Image = Image.FromFile(filename);

            Bitmap currentBitmap = new Bitmap(this.pictureBox1.Image);

            Graphics g = Graphics.FromImage(currentBitmap);

            ImageAttributes ia = new ImageAttributes();

            float[][] colorMatrix =   {    

                new   float[]   {0.299f,   0.299f,   0.299f,   0,   0},

                new   float[]   {0.587f,   0.587f,   0.587f,   0,   0},

                new   float[]   {0.114f,   0.114f,   0.114f,   0,   0},

                new   float[]   {0,   0,   0,   1,   0},

                new   float[]   {0,   0,   0,   0,   1}

            };

            ColorMatrix cm = new ColorMatrix(colorMatrix);

            ia.SetColorMatrix(cm, ColorMatrixFlag.Default, ColorAdjustType.Bitmap);

            g.DrawImage(currentBitmap, new Rectangle(0, 0, currentBitmap.Width, currentBitmap.Height), 0, 0, currentBitmap.Width, currentBitmap.Height, GraphicsUnit.Pixel, ia);

            this.pictureBox2.Image = (Image)(currentBitmap.Clone());

            g.Dispose();



        }

        private void button10_Click(object sender, EventArgs e)
        {
            //浮雕效果3

            string filename = @"C:\______test_files\picture1.jpg";
            pictureBox1.Image = Image.FromFile(filename);


            /*
使圖像產生浮雕的效果，主要通過對圖像像素點的像素值分別與相鄰像素點的像素值相減後加上128，然後將其作為新的像素點的值。

以浮雕效果顯示圖像主要通過GetPixel方法獲得每一點像素的值，通過SetPixel設置該像素點的像素值。
*/

            //以浮雕效果顯示圖像
            try
            {
                int Height = this.pictureBox1.Image.Height;
                int Width = this.pictureBox1.Image.Width;
                Bitmap newBitmap = new Bitmap(Width, Height);
                Bitmap oldBitmap = (Bitmap)this.pictureBox1.Image;
                Color pixel1, pixel2;
                for (int x = 0; x < Width - 1; x++)
                {
                    for (int y = 0; y < Height - 1; y++)
                    {
                        int r = 0, g = 0, b = 0;
                        pixel1 = oldBitmap.GetPixel(x, y);
                        pixel2 = oldBitmap.GetPixel(x + 1, y + 1);
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
                        newBitmap.SetPixel(x, y, Color.FromArgb(r, g, b));
                    }
                }
                this.pictureBox1.Image = newBitmap;
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "信息提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }

        private void button11_Click(object sender, EventArgs e)
        {
            float gamma = 1.5f;

            //從pictureBox取得Bitmap
            Bitmap bitmap1 = (Bitmap)pictureBox1.Image;

            Bitmap bitmap2 = KiGamma(bitmap1, gamma);

            pictureBox1.Image = bitmap2;
        }

        //C#圖片處理之Gamma校正
        //gamma值是用曲線表示的，這是一種人的眼睛對光的一種感應曲線，其中包括了物理量、身理感官及心理的感知度。

        /// <summary>
        /// Gamma校正
        /// </summary>
        /// <param name="bmp">輸入Bitmap</param>
        /// <param name="val">[0 <-明- 1 -暗-> 2]</param>
        /// <returns>輸出Bitmap</returns>
        public static Bitmap KiGamma(Bitmap bmp, float val)
        {
            if (bmp == null)
            {
                return null;
            }

            // 1表示無變化，就不做
            if (val == 1.0000f) return bmp;

            try
            {
                Bitmap b = new Bitmap(bmp.Width, bmp.Height);
                Graphics g = Graphics.FromImage(b);
                ImageAttributes attr = new ImageAttributes();

                attr.SetGamma(val, ColorAdjustType.Bitmap);
                g.DrawImage(bmp, new Rectangle(0, 0, bmp.Width, bmp.Height), 0, 0, bmp.Width, bmp.Height, GraphicsUnit.Pixel, attr);
                g.Dispose();
                return b;
            }
            catch
            {
                return null;
            }
        }

        public static Image resizeImage(Image imgToResize, Size size)
        {
            return (Image)(new Bitmap(imgToResize, size));
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //調整影像大小 1
            //調整影像大小
            //使用 C# 中的 Bitmap 類調整影象大小
            string filename = @"C:\______test_files\picture1.jpg";
            Image image1 = Image.FromFile(filename);
            Bitmap bitmap1 = new Bitmap(image1);
            //Image image2 = resizeImage(bitmap1, new Size(image1.Width / 2, image1.Height / 2));
            Image image2 = resizeImage(bitmap1, new Size(100, 300));

            pictureBox1.Image = image2;


        }

        private void button13_Click(object sender, EventArgs e)
        {
            //調整影像大小 2
            //調整影像大小 2
            //使用 C# 中的 Graphics.DrawImage() 函式調整影象大小
            string filename = @"C:\______test_files\picture1.jpg";
            Image image1 = Image.FromFile(filename);
            Bitmap bitmap1 = new Bitmap(image1);
            Image image2 = resizeImage(bitmap1, new Size(200, 200));

            pictureBox1.Image = image2;
        }

        public static Image resizeImage2(Image image, int width, int height)
        {
            var destinationRect = new Rectangle(0, 0, width, height);
            var destinationImage = new Bitmap(width, height);

            destinationImage.SetResolution(image.HorizontalResolution, image.VerticalResolution);

            using (var graphics = Graphics.FromImage(destinationImage))
            {
                graphics.CompositingMode = CompositingMode.SourceCopy;
                graphics.CompositingQuality = CompositingQuality.HighQuality;

                using (var wrapMode = new ImageAttributes())
                {
                    wrapMode.SetWrapMode(WrapMode.TileFlipXY);
                    graphics.DrawImage(image, destinationRect, 0, 0, image.Width, image.Height, GraphicsUnit.Pixel, wrapMode);
                }
            }

            return (Image)destinationImage;
            /*
            destinationImage.SetResolution() 函式保持影象的 dpi，而不考慮其實際大小
            graphics.CompositingMode = CompositingMode.SourceCopy 屬性指定在渲染顏色時它將覆蓋背景顏色
            graphics.CompositingQuality = CompositingQuality.HighQuality 屬性指定我們只希望渲染高質量的影象
            wrapMode.SetWrapMode(WrapMode.TileFlipXY) 函式可以防止在影象邊界周圍出現鬼影
            graphics.DrawImage() 繪製具有指定尺寸的實際影象。
            */
        }

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button15_Click(object sender, EventArgs e)
        {

        }

        private void button16_Click(object sender, EventArgs e)
        {

        }

        private void button17_Click(object sender, EventArgs e)
        {

        }

        private void button18_Click(object sender, EventArgs e)
        {

        }

        private void button19_Click(object sender, EventArgs e)
        {

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
