using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//http://www.aspphp.online/bianchen/cyuyan/gycyy/201701/81415.html

namespace vcs_ImageProcessingG
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\picture1.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //讀取圖檔
            pictureBox1.Image = Image.FromFile(filename);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";
            pictureBox1.Image = image_processing1(filename);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";
            pictureBox1.Image = image_processing2(filename);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";
            pictureBox1.Image = image_processing3(filename);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";
            pictureBox1.Image = image_processing4(filename);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";
            pictureBox1.Image = image_processing5(filename);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";
            pictureBox1.Image = image_processing6(filename);
        }

        private void button7_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";
            pictureBox1.Image = image_processing7(filename);
        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";
            image_processing9(filename);
        }

        private void button10_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";
            pictureBox1.Image = image_processing10(filename);
        }

        private void button11_Click(object sender, EventArgs e)
        {
        }

        private void button12_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";
            pictureBox1.Image = image_processing12(filename);
        }

        private void button13_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";
            image_processing11(filename);
        }

        /*
        一. 底片效果
        原理: GetPixel方法獲得每一點像素的值, 然後再使用SetPixel方法將取反後的顏色值設置到對應的點.
        */

        //底片效果
        private Bitmap image_processing1(string filename)
        {
            //以底片效果顯示圖像

            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            //pictureBox1.Image = bitmap1;

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            Bitmap bitmap2 = new Bitmap(W, H);
            Color pixel;
            for (int x = 1; x < W; x++)
            {
                for (int y = 1; y < H; y++)
                {
                    int r, g, b;
                    pixel = bitmap1.GetPixel(x, y);
                    r = 255 - pixel.R;
                    g = 255 - pixel.G;
                    b = 255 - pixel.B;
                    bitmap2.SetPixel(x, y, Color.FromArgb(r, g, b));
                }
            }
            return bitmap2;
        }

        /*
        二. 浮雕效果

        原理: 對圖像像素點的像素值分別與相鄰像素點的像素值相減後加上128, 然後將其作為新的像素點的值.

        使圖像產生浮雕的效果，主要通過對圖像像素點的像素值分別與相鄰像素點的像素值相減後加上128，然後將其作為新的像素點的值。
        以浮雕效果顯示圖像主要通過GetPixel方法獲得每一點像素的值，通過SetPixel設置該像素點的像素值。
        */
        //浮雕效果
        private Bitmap image_processing2(string filename)
        {
            //以浮雕效果顯示圖像
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            Bitmap bitmap2 = new Bitmap(W, H);
            Color pixel1, pixel2;
            for (int x = 0; x < W - 1; x++)
            {
                for (int y = 0; y < H - 1; y++)
                {
                    int r = 0, g = 0, b = 0;
                    pixel1 = bitmap1.GetPixel(x, y);
                    pixel2 = bitmap1.GetPixel(x + 1, y + 1);
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
                    bitmap2.SetPixel(x, y, Color.FromArgb(r, g, b));
                }
            }
            return bitmap2;
        }

        /*
        三. 黑白效果
        原理: 彩色圖像處理成黑白效果通常有3種算法；
        (1).最大值法: 使每個像素點的 R, G, B 值等於原像素點的 RGB (顏色值) 中最大的一個；
        (2).平均值法: 使用每個像素點的 R,G,B值等於原像素點的RGB值的平均值；
        (3).加權平均值法: 對每個像素點的 R, G, B值進行加權
        ---自認為第三種方法做出來的黑白效果圖像最 "真實".
        */

        //黑白效果
        private Bitmap image_processing3(string filename)
        {
            //以黑白效果顯示圖像
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            int W = bitmap1.Width;
            int H = bitmap1.Height;
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
                    //實例程序以加權平均值法產生黑白圖像
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
                        case 2://加權平均值法
                            Result = ((int)(0.7 * r) + (int)(0.2 * g) + (int)(0.1 * b));
                            break;
                    }
                    bitmap2.SetPixel(x, y, Color.FromArgb(Result, Result, Result));
                }
            }
            return bitmap2;
        }

        /*
        四. 柔化效果
        原理: 當前像素點與周圍像素點的顏色差距較大時取其平均值.
        */
        //柔化效果
        private Bitmap image_processing4(string filename)
        {
            //以柔化效果顯示圖像

            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            Bitmap bitmap2 = new Bitmap(W, H);

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
                        for (int row = -1; row <= 1; row++)
                        {
                            pixel = bitmap1.GetPixel(x + row, y + col);
                            r += pixel.R * Gauss[Index];
                            g += pixel.G * Gauss[Index];
                            b += pixel.B * Gauss[Index];
                            Index++;
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
                    bitmap2.SetPixel(x - 1, y - 1, Color.FromArgb(r, g, b));
                }
            }
            return bitmap2;
        }

        /*
        五.銳化效果
        原理:突出顯示顏色值大(即形成形體邊緣)的像素點.
        */

        //銳化效果
        private Bitmap image_processing5(string filename)
        {
            //以銳化效果顯示圖像
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            Bitmap bitmap2 = new Bitmap(W, H);

            Color pixel;
            //拉普拉斯模板
            int[] Laplacian = { -1, -1, -1, -1, 9, -1, -1, -1, -1 };
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
                            pixel = bitmap1.GetPixel(x + row, y + col); r += pixel.R * Laplacian[Index];
                            g += pixel.G * Laplacian[Index];
                            b += pixel.B * Laplacian[Index];
                            Index++;
                        }
                    }
                    //處理顏色值溢出
                    r = r > 255 ? 255 : r;
                    r = r < 0 ? 0 : r;
                    g = g > 255 ? 255 : g;
                    g = g < 0 ? 0 : g;
                    b = b > 255 ? 255 : b;
                    b = b < 0 ? 0 : b;
                    bitmap2.SetPixel(x - 1, y - 1, Color.FromArgb(r, g, b));
                }
            }
            return bitmap2;
        }

        /*
        六. 霧化效果
        原理: 在圖像中引入一定的隨機值, 打亂圖像中的像素值
        */

        //霧化效果
        private Bitmap image_processing6(string filename)
        {
            //以霧化效果顯示圖像
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            Bitmap bitmap2 = new Bitmap(W, H);
            Color pixel;
            for (int x = 1; x < W - 1; x++)
            {
                for (int y = 1; y < H - 1; y++)
                {
                    System.Random MyRandom = new Random();
                    int k = MyRandom.Next(123456);
                    //像素塊大小
                    int dx = x + k % 19;
                    int dy = y + k % 19;
                    if (dx >= W)
                        dx = W - 1;
                    if (dy >= H)
                        dy = H - 1;
                    pixel = bitmap1.GetPixel(dx, dy);
                    bitmap2.SetPixel(x, y, pixel);
                }
            }
            return bitmap2;
        }

        /*
        七. 光照效果
        原理: 對圖像中的某一范圍內的像素的亮度分別進行處理.
        */

        //光照效果
        private Bitmap image_processing7(string filename)
        {
            //以光照效果顯示圖像
            Graphics g = this.pictureBox1.CreateGraphics();
            g.Clear(Color.White);
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            Bitmap bitmap2 = bitmap1.Clone(new RectangleF(0, 0, W, H), System.Drawing.Imaging.PixelFormat.DontCare);

            //光照中心點
            int cx = W / 2;
            int cy = H / 2;
            //MyCenter圖片中心點，發亮此值會讓強光中心發生偏移
            Point MyCenter = new Point(cx, cy);
            //R強光照射面的半徑，即”光暈”
            int radius = Math.Min(W / 2, H / 2);
            for (int i = W - 1; i >= 1; i--)
            {
                for (int j = H - 1; j >= 1; j--)
                {
                    float MyLength = (float)Math.Sqrt(Math.Pow((i - MyCenter.X), 2) + Math.Pow((j - MyCenter.Y), 2));
                    //如果像素位於”光暈”之內
                    if (MyLength < radius)
                    {
                        Color MyColor = bitmap2.GetPixel(i, j);
                        int R, G, B;
                        //220亮度增加常量，該值越大，光亮度越強
                        float MyPixel = 220.0f * (1.0f - MyLength / radius);
                        R = MyColor.R + (int)MyPixel;
                        R = Math.Max(0, Math.Min(R, 255));
                        G = MyColor.G + (int)MyPixel;
                        G = Math.Max(0, Math.Min(G, 255));
                        B = MyColor.B + (int)MyPixel;
                        B = Math.Max(0, Math.Min(B, 255));
                        //將增亮後的像素值回寫到位圖
                        Color MyNewColor = Color.FromArgb(255, R, G, B);
                        bitmap2.SetPixel(i, j, MyNewColor);
                    }
                }
                //重新繪制圖片
                g.DrawImage(bitmap2, new Rectangle(0, 0, W, H));
            }
            return bitmap2;
        }

        /*
        九.馬賽克效果
        原理: 確定圖像的隨機位置點和確定馬賽克塊的大小,然後馬賽克塊圖像覆蓋隨機點即可.
        */

        //馬賽克效果
        private void image_processing9(string filename)
        {
            //以馬賽克效果顯示圖像
            try
            {
                Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
                int W = bitmap1.Width;
                int H = bitmap1.Height;
                Bitmap bitmap2 = new Bitmap(W, H);

                int dw = bitmap1.Width / 50;
                int dh = bitmap1.Height / 50;
                Graphics g = this.pictureBox1.CreateGraphics();
                g.Clear(Color.Gray);
                Point[] MyPoint = new Point[2500];
                for (int x = 0; x < 50; x++)
                    for (int y = 0; y < 50; y++)
                    {
                        MyPoint[x * 50 + y].X = x * dw;
                        MyPoint[x * 50 + y].Y = y * dh;
                    }
                for (int i = 0; i < 10000; i++)
                {
                    System.Random MyRandom = new Random();
                    int iPos = MyRandom.Next(2500);
                    for (int m = 0; m < dw; m++)
                        for (int n = 0; n < dh; n++)
                        {
                            bitmap2.SetPixel(MyPoint[iPos].X + m, MyPoint[iPos].Y + n, bitmap1.GetPixel(MyPoint[iPos].X + m, MyPoint[iPos].Y + n));
                        }
                    this.pictureBox1.Refresh();
                    this.pictureBox1.Image = bitmap2;
                }
                for (int i = 0; i < 2500; i++)
                    for (int m = 0; m < dw; m++)
                        for (int n = 0; n < dh; n++)
                        {
                            bitmap2.SetPixel(MyPoint[i].X + m, MyPoint[i].Y + n, bitmap1.GetPixel(MyPoint[i].X + m, MyPoint[i].Y + n));
                        }
                this.pictureBox1.Refresh();
                this.pictureBox1.Image = bitmap2;
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "信息提示");
            }
        }



        /*
        十. 油畫效果

        原理: 對圖像中某一范圍內的像素引入隨機值.
        */

        //油畫效果
        private Bitmap image_processing10(string filename)
        {
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            //Bitmap bitmap2 = new Bitmap(W, H);

            //以油畫效果顯示圖像
            Graphics g = this.pictureBox1.CreateGraphics();
            RectangleF rect = new RectangleF(0, 0, W, H);
            Bitmap bitmap2 = bitmap1.Clone(rect, System.Drawing.Imaging.PixelFormat.DontCare);
            //產生隨機數序列
            Random rnd = new Random();
            //取不同的值決定油畫效果的不同程度
            int iModel = 2;
            int i = W - iModel;
            while (i > 1)
            {
                int j = H - iModel;
                while (j > 1)
                {
                    int iPos = rnd.Next(100000) % iModel;
                    //將該點的RGB值設置成附近iModel點之內的任一點
                    Color color = bitmap2.GetPixel(i + iPos, j + iPos);
                    bitmap2.SetPixel(i, j, color);
                    j = j - 1;
                }
                i = i - 1;
            }
            //重新繪制圖像
            g.Clear(Color.White);
            g.DrawImage(bitmap2, new Rectangle(0, 0, W, H));
            return bitmap2;
        }

        /*
        十一: 扭曲效果
        原理: 將圖像縮放為一個非矩形的平等四邊形即可
        */

        //扭曲效果
        private void image_processing11(string filename)
        {
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式

            int W = bitmap1.Width;
            int H = bitmap1.Height;

            Graphics g = this.pictureBox1.CreateGraphics();

            Size offset = new Size(W++, H++);//設置偏移量
            Rectangle rect = this.pictureBox1.ClientRectangle;
            Point[] points = new Point[3];
            points[0] = new Point(rect.Left + offset.Width, rect.Top + offset.Height);
            points[1] = new Point(rect.Right, rect.Top + offset.Height);
            points[2] = new Point(rect.Left, rect.Bottom - offset.Height);
            g.Clear(Color.White);
            g.DrawImage(bitmap1, points);
        }

        /*
        十二.積木效果
        原理: 對圖像中的各個像素點著重(即加大分像素的顏色值)著色.
        */

        //積木效果
        private Bitmap image_processing12(string filename)
        {
            //以積木效果顯示圖像

            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            //Bitmap bitmap2 = new Bitmap(W, H);

            Graphics g = this.pictureBox1.CreateGraphics();
            //Bitmap bitmap1 = new Bitmap(this.BackgroundImage);
            int i, j, iAvg, iPixel;
            Color myColor, myNewColor;
            RectangleF myRect;
            myRect = new RectangleF(0, 0, W, H);
            Bitmap bitmap2 = bitmap1.Clone(myRect, System.Drawing.Imaging.PixelFormat.DontCare);
            i = 0;
            while (i < W - 1)
            {
                j = 0;
                while (j < H - 1)
                {
                    myColor = bitmap2.GetPixel(i, j);
                    iAvg = (myColor.R + myColor.G + myColor.B) / 3;
                    iPixel = 0;
                    if (iAvg >= 128)
                        iPixel = 255;
                    else
                        iPixel = 0;
                    myNewColor = Color.FromArgb(255, iPixel, iPixel, iPixel);
                    bitmap2.SetPixel(i, j, myNewColor);
                    j = j + 1;
                }
                i = i + 1;
            }
            g.Clear(Color.WhiteSmoke);
            g.DrawImage(bitmap2, new Rectangle(0, 0, W, H));
            return bitmap2;
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //以霧化效果顯示圖像
            try
            {
                int Height = this.pictureBox1.Image.Height;
                int Width = this.pictureBox1.Image.Width;
                Bitmap newBitmap = new Bitmap(Width, Height);
                Bitmap oldBitmap = (Bitmap)this.pictureBox1.Image;
                Color pixel;
                for (int x = 1; x < Width - 1; x++)
                    for (int y = 1; y < Height - 1; y++)
                    {
                        System.Random MyRandom = new Random();
                        int k = MyRandom.Next(123456);
                        //像素塊大小
                        int dx = x + k % 19;
                        int dy = y + k % 19;
                        if (dx >= Width)
                            dx = Width - 1;
                        if (dy >= Height)
                            dy = Height - 1;
                        pixel = oldBitmap.GetPixel(dx, dy);
                        newBitmap.SetPixel(x, y, pixel);
                    }
                this.pictureBox1.Image = newBitmap;
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "信息提示");
            }

        }
    }
}

