using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;
using System.Drawing.Drawing2D;

namespace vcs_ImageProcessingK
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
            dx = 130 + 10;
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
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //均值濾波

            string filename = @"C:\______test_files\picture1.jpg";
            Bitmap bitmap1 = new Bitmap(filename);

            if (bitmap1 == null)
                return;

            GrayBitmapData gbmp = new GrayBitmapData(bitmap1);
            gbmp.AverageFilter(3);
            gbmp.ShowImage(pictureBox1);


        }

        private void button1_Click(object sender, EventArgs e)
        {
            //轉換爲灰度圖
            string filename = @"C:\______test_files\picture1.jpg";
            Bitmap bitmap1 = new Bitmap(filename);

            if (bitmap1 == null)
                return;

            GrayBitmapData gbmp = new GrayBitmapData(bitmap1);
            gbmp.ShowImage(pictureBox1);

        }

        private void button2_Click(object sender, EventArgs e)
        {
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {
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
    }

    class GrayBitmapData
    {
        public byte[,] Data;//保存像素矩陣
        public int Width;//圖像的寬度
        public int Height;//圖像的高度

        public GrayBitmapData()
        {
            this.Width = 0;
            this.Height = 0;
            this.Data = null;
        }

        public GrayBitmapData(Bitmap bmp)
        {
            BitmapData bmpData = bmp.LockBits(new Rectangle(0, 0, bmp.Width, bmp.Height), ImageLockMode.ReadOnly, PixelFormat.Format24bppRgb);
            this.Width = bmpData.Width;
            this.Height = bmpData.Height;
            Data = new byte[Height, Width];
            unsafe
            {
                byte* ptr = (byte*)bmpData.Scan0.ToPointer();
                for (int i = 0; i < Height; i++)
                {
                    for (int j = 0; j < Width; j++)
                    {
                        //將24位的RGB彩色圖轉換爲灰度圖
                        int temp = (int)(0.114 * (*ptr++)) + (int)(0.587 * (*ptr++)) + (int)(0.299 * (*ptr++));
                        Data[i, j] = (byte)temp;
                    }
                    ptr += bmpData.Stride - Width * 3;//指針加上填充的空白空間
                    //其中BitmapData類的Stride屬性爲每行像素所佔的字節。
                }
            }
            bmp.UnlockBits(bmpData);
        }

        public GrayBitmapData(string path)
            : this(new Bitmap(path))
        {
        }

        public Bitmap ToBitmap()
        {
            Bitmap bmp = new Bitmap(Width, Height, PixelFormat.Format24bppRgb);
            BitmapData bmpData = bmp.LockBits(new Rectangle(0, 0, Width, Height), ImageLockMode.WriteOnly, PixelFormat.Format24bppRgb);
            unsafe
            {
                byte* ptr = (byte*)bmpData.Scan0.ToPointer();
                for (int i = 0; i < Height; i++)
                {
                    for (int j = 0; j < Width; j++)
                    {
                        *(ptr++) = Data[i, j];
                        *(ptr++) = Data[i, j];
                        *(ptr++) = Data[i, j];
                    }
                    ptr += bmpData.Stride - Width * 3;
                    //其中BitmapData類的Stride屬性爲每行像素所佔的字節。
                }
            }
            bmp.UnlockBits(bmpData);
            return bmp;
        }

        public void ShowImage(PictureBox pbx)
        {
            Bitmap b = this.ToBitmap();
            pbx.Image = b;
            //b.Dispose();
        }

        public void SaveImage(string path)
        {
            Bitmap b = ToBitmap();
            b.Save(path);
            //b.Dispose();
        }
        //均值濾波
        public void AverageFilter(int windowSize)
        {
            if (windowSize % 2 == 0)
            {
                return;
            }

            for (int i = 0; i < Height; i++)
            {
                for (int j = 0; j < Width; j++)
                {
                    int sum = 0;
                    for (int g = -(windowSize - 1) / 2; g <= (windowSize - 1) / 2; g++)
                    {
                        for (int k = -(windowSize - 1) / 2; k <= (windowSize - 1) / 2; k++)
                        {
                            int a = i + g, b = j + k;
                            if (a < 0) a = 0;
                            if (a > Height - 1) a = Height - 1;
                            if (b < 0) b = 0;
                            if (b > Width - 1) b = Width - 1;
                            sum += Data[a, b];
                        }
                    }
                    Data[i, j] = (byte)(sum / (windowSize * windowSize));
                }
            }
        }

        //中值濾波
        public void MidFilter(int windowSize)
        {
            if (windowSize % 2 == 0)
            {
                return;
            }

            int[] temp = new int[windowSize * windowSize];
            byte[,] newdata = new byte[Height, Width];
            for (int i = 0; i < Height; i++)
            {
                for (int j = 0; j < Width; j++)
                {
                    int n = 0;
                    for (int g = -(windowSize - 1) / 2; g <= (windowSize - 1) / 2; g++)
                    {
                        for (int k = -(windowSize - 1) / 2; k <= (windowSize - 1) / 2; k++)
                        {
                            int a = i + g, b = j + k;
                            if (a < 0) a = 0;
                            if (a > Height - 1) a = Height - 1;
                            if (b < 0) b = 0;
                            if (b > Width - 1) b = Width - 1;
                            temp[n++] = Data[a, b];
                        }
                    }
                    newdata[i, j] = GetMidValue(temp, windowSize * windowSize);
                }
            }

            for (int i = 0; i < Height; i++)
            {
                for (int j = 0; j < Width; j++)
                {
                    Data[i, j] = newdata[i, j];
                }
            }
        }

        //獲得一個向量的中值
        private byte GetMidValue(int[] t, int length)
        {
            int temp = 0;
            for (int i = 0; i < length - 2; i++)
            {
                for (int j = i + 1; j < length - 1; j++)
                {
                    if (t[i] > t[j])
                    {
                        temp = t[i];
                        t[i] = t[j];
                        t[j] = temp;
                    }
                }
            }

            return (byte)t[(length - 1) / 2];
        }

        //一種新的濾波方法，是亮的更亮、暗的更暗
        public void NewFilter(int windowSize)
        {
            if (windowSize % 2 == 0)
            {
                return;
            }

            for (int i = 0; i < Height; i++)
            {
                for (int j = 0; j < Width; j++)
                {
                    int sum = 0;
                    for (int g = -(windowSize - 1) / 2; g <= (windowSize - 1) / 2; g++)
                    {
                        for (int k = -(windowSize - 1) / 2; k <= (windowSize - 1) / 2; k++)
                        {
                            int a = i + g, b = j + k;
                            if (a < 0) a = 0;
                            if (a > Height - 1) a = Height - 1;
                            if (b < 0) b = 0;
                            if (b > Width - 1) b = Width - 1;
                            sum += Data[a, b];
                        }
                    }
                    double avg = (sum + 0.0) / (windowSize * windowSize);
                    if (avg / 255 < 0.5)
                    {
                        Data[i, j] = (byte)(2 * avg / 255 * Data[i, j]);
                    }
                    else
                    {
                        Data[i, j] = (byte)((1 - 2 * (1 - avg / 255.0) * (1 - Data[i, j] / 255.0)) * 255);
                    }
                }
            }
        }


        //直方圖均衡
        public void HistEqual()
        {
            double[] num = new double[256];
            for (int i = 0; i < 256; i++) num[i] = 0;

            for (int i = 0; i < Height; i++)
            {
                for (int j = 0; j < Width; j++)
                {
                    num[Data[i, j]]++;
                }
            }

            double[] newGray = new double[256];
            double n = 0;
            for (int i = 0; i < 256; i++)
            {
                n += num[i];
                newGray[i] = n * 255 / (Height * Width);
            }

            for (int i = 0; i < Height; i++)
            {
                for (int j = 0; j < Width; j++)
                {
                    Data[i, j] = (byte)newGray[Data[i, j]];
                }
            }
        }
    }
}

