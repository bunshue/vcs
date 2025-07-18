using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;   //for BitmapData, ImageLockMode, PixelFormat
using System.Runtime.InteropServices;   //for Marshal
using System.Diagnostics;   //for Stopwatch

namespace vcs_ImageProcessing0
{
    public partial class Form1 : Form
    {
        string filename = @"C:\_git\vcs\_1.data\______test_files1\__pic\_anime\doraemon1.jpg";
        //string filename = @"C:\_git\vcs\_1.data\______test_files1\pic_256X100.bmp";
        //string filename = @"C:\_git\vcs\_1.data\______test_files1\__pic\_map_city/global.c.gif";   //超大圖, 要很久
        //string filename = @"C:\_git\vcs\_1.data\______test_files1\elephant.jpg";

        Stopwatch sw = new Stopwatch();

        //delay 10000 約 10秒
        //C# 不lag的延遲時間
        private void delay(int delay_milliseconds)
        {
            delay_milliseconds *= 2;
            DateTime time_before = DateTime.Now;
            while (((TimeSpan)(DateTime.Now - time_before)).TotalMilliseconds < delay_milliseconds)
            {
                Application.DoEvents();
            }
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
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
            dx = 140;
            dy = 70;

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
            button10.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            button11.Location = new Point(x_st + dx * 0, y_st + dy * 11);
            button12.Location = new Point(x_st + dx * 0, y_st + dy * 12);
            button13.Location = new Point(x_st + dx * 0, y_st + dy * 13);

            button14.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button20.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button21.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button22.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button23.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            button24.Location = new Point(x_st + dx * 1, y_st + dy * 10);
            button25.Location = new Point(x_st + dx * 1, y_st + dy * 11);
            button26.Location = new Point(x_st + dx * 1, y_st + dy * 12);
            button27.Location = new Point(x_st + dx * 1, y_st + dy * 13);

            bt_restore.Location = new Point(x_st + dx * 8, y_st + dy * 0);

            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox1.Size = new Size(640, 480);
            pictureBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0 + 480 + 10);
            pictureBox2.Size = new Size(640, 480);

            richTextBox1.Size = new Size(700, 900);
            richTextBox1.Location = new Point(x_st + dx * 8 + 80, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            bt_exit_setup();
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Name = "bt_exit";
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_restore_Click(object sender, EventArgs e)
        {
            Restore_Picture();
        }

        //各種影像處理速度比較 ST
        private void button0_Click(object sender, EventArgs e)
        {
            button0.BackColor = Color.Red;
            Application.DoEvents();

            //各種影像處理速度比較
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            var bmp = new Bitmap(filename);
            pictureBox1.Image = bmp;
            var sw = new Stopwatch();
            richTextBox1.Text += "各種影像處理速度比較 ST\n";
            Application.DoEvents();

            richTextBox1.Text += "方法4: usafe pointer\n";
            sw.Reset();
            sw.Start();
            // usafe pointer
            NegativeImage4(bmp);
            sw.Stop();
            pictureBox1.Refresh();
            richTextBox1.Text += "耗時 : " + string.Format("{0,10}", sw.ElapsedMilliseconds.ToString()) + "\tmsec\n";
            Application.DoEvents();

            richTextBox1.Text += "方法6: use BitmapData\n";
            sw.Reset();
            sw.Start();
            NegativeImage6(bmp);
            sw.Stop();
            pictureBox1.Refresh();
            richTextBox1.Text += "耗時 : " + string.Format("{0,10}", sw.ElapsedMilliseconds.ToString()) + "\tmsec\n";

            richTextBox1.Text += "各種影像處理速度比較 SP\n\n";

            button0.BackColor = SystemColors.ControlLight;
        }

        /// <summary>
        /// How to obtain brightness value by using unsafe pointer
        /// </summary>
        /// <param name="bmp"></param>
        private void NegativeImage4(Bitmap bmp)
        {
            int W = bmp.Width;
            int H = bmp.Height;

            //綁定bmp和bmpData
            BitmapData bmpData = bmp.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadWrite, bmp.PixelFormat);
            var stride = Math.Abs(bmpData.Stride);//取得記憶體寬度

            unsafe
            {
                // Arrange image data for saving
                var ptr = (byte*)bmpData.Scan0;
                byte r, g, b;
                byte* pLine = ptr;
                for (int y = 0; y < H; y++)
                {
                    // The first point of the line
                    ptr = pLine;
                    for (int x = 0; x < W; x++)
                    {
                        // Obtain brightness value
                        r = ptr[2];
                        g = ptr[1];
                        b = ptr[0];
                        // Set up brightness value
                        ptr[2] = (byte)(255 - r);
                        ptr[1] = (byte)(255 - g);
                        ptr[0] = (byte)(255 - b);
                        // Move to the next pixel 
                        ptr += 3;
                    }
                    // Move to the next line 
                    pLine += stride;
                }
            }

            //解除綁定bmp和bmpData
            bmp.UnlockBits(bmpData);
        }

        /// <summary>
        /// 使用BitmapData處理
        /// </summary>
        /// <param name="bmp"></param>
        private void NegativeImage6(Bitmap bmp)
        {
            int W = bmp.Width;
            int H = bmp.Height;

            //綁定bmp和bmpData
            BitmapData bmpData = bmp.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);

            unsafe
            {
                byte* p = (byte*)bmpData.Scan0.ToPointer();
                for (int y = 0; y < H; y++)
                {
                    for (int x = 0; x < W; x++)
                    {
                        //檢查圖片是否全白或全黑
                        if ((p[0] != 255 && p[0] != 0) || (p[1] != 255 && p[1] != 0) || (p[2] != 255 && p[2] != 0))
                        {
                            //NotNULL = true;
                            //break;
                        }

                        /*
                        //修改圖片的數值
                        p[0] -= 50;
                        p[1] -= 50;
                        p[2] -= 50;
                        */

                        //反相
                        p[0] = (byte)(255 - p[0]);
                        p[1] = (byte)(255 - p[1]);
                        p[2] = (byte)(255 - p[2]);

                        p += 3;
                    }
                    //if (NotNULL == true)
                    //break;
                }
                //解除綁定bmp和bmpData
                bmp.UnlockBits(bmpData);
            }
        }
        //各種影像處理速度比較 SP

        private void button1_Click(object sender, EventArgs e)
        {
        }

        private void button2_Click(object sender, EventArgs e)
        {
            int i;
            int j;
            Bitmap bitmap1 = new Bitmap(filename);

            int W = bitmap1.Width;
            int H = bitmap1.Height;

            //綁定bitmap1和bmpData
            BitmapData bmpData = bitmap1.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadWrite, bitmap1.PixelFormat);
            //BitmapData bmpData = bitmap1.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb); //指明PixelFormat

            unsafe
            {
                byte* ptr = (byte*)(bmpData.Scan0);

                for (j = 0; j < H; j++)
                {
                    for (i = 0; i < W; i++)
                    {
                        //三色平均 => 灰階
                        byte avg = (byte)((*(ptr + 0) + *(ptr + 1) + *(ptr + 2)) / 3);
                        *(ptr + 0) = avg;         //每個點的B改成三色平均
                        *(ptr + 1) = avg;     //每個點的G改成三色平均
                        *(ptr + 2) = avg;     //每個點的R改成三色平均
                        //*(ptr + 3) = 0;     //每個點的A改成三色平均
                        ptr += 3;   //jpg檔要加 3, bmp檔要加4
                    }
                }

                //解除綁定bitmap1和bmpData
                bitmap1.UnlockBits(bmpData);

                pictureBox1.Image = bitmap1;
            }
            //毫無疑問，採用這種方式是最快的，所以在實際工程中都是採用指針的方式來訪問圖像像素的。
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //使用unsafe加快處理圖像速度

            string filename = @"C:\_git\vcs\_1.data\______test_files1\red.bmp";

            Bitmap bitmap1 = new Bitmap(filename);

            int W = bitmap1.Width;
            int H = bitmap1.Height;

            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";

            //綁定bitmap1和bmpData
            BitmapData bmpData = bitmap1.LockBits(new Rectangle(100, 100, 20, 20), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);

            int w = bmpData.Width;
            int h = bmpData.Height;

            richTextBox1.Text += "w = " + w.ToString() + ", h = " + h.ToString() + "\n";

            unsafe
            {
                long r = 0;
                long g = 0;
                long b = 0;
                long pixelCount = h * w;

                byte* ptr = (byte*)(bmpData.Scan0);

                for (int i = 0; i < h; i++)
                {
                    for (int j = 0; j < w; j++)
                    {
                        //排列是BGR
                        b += *ptr;
                        g += *(ptr + 1);
                        r += *(ptr + 2);
                        ptr += 3;
                    }
                    ptr += bmpData.Stride - w * 3;
                }

                double totalRGB = (r / pixelCount + g / pixelCount + b / pixelCount) / 3;

                richTextBox1.Text += "平均 R : " + (r / pixelCount).ToString() + "\n";
                richTextBox1.Text += "平均 G : " + (g / pixelCount).ToString() + "\n";
                richTextBox1.Text += "平均 B : " + (b / pixelCount).ToString() + "\n";
                richTextBox1.Text += "平均亮度 : " + totalRGB.ToString() + "\n";
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //將byte數組轉換為8bit灰度圖像
            //將byte數組轉換為8bit灰度圖像
            byte[] byte_data = new byte[10000];//建立 byte[] Array 一維陣列
            int k = 0;

            for (int i = 0; i < 100; i++)
            {
                for (int j = 0; j < 100; j++)
                {
                    byte_data[k++] = (byte)(i + j);
                }
            }

            int width = 100;
            int height = 100;

            // 將一個字節數組轉換為8bit灰度位圖
            //public static Bitmap ToGrayBitmap(byte[] rawValues, int width, int height)
            // 申請目標位圖的變量，並將其內存區域鎖定
            Bitmap bitmap1 = new Bitmap(width, height, PixelFormat.Format8bppIndexed);

            //綁定bitmap1和bmpData
            BitmapData bmpData = bitmap1.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.WriteOnly, PixelFormat.Format8bppIndexed);

            // 獲取圖像參數
            int stride = bmpData.Stride;　 // 掃描線的寬度, 取得記憶體寬度
            int offset = stride - width;　 // 顯示寬度與掃描線寬度的間隙
            IntPtr iptr = bmpData.Scan0;　 // 獲取bmpData的內存起始位置

            // 下面把原始的顯示大小字節數組轉換為內存中實際存放的字節數組
            int posScan = 0, posReal = 0;　　 // 分別設置兩個位置指針，指向 源數組和目標數組

            //建立 byte[] Array 一維陣列
            int byte_data_len = stride * height;　　 // 用stride寬度，表示這是 內存區域的大小
            //byte[] byte_data = new byte[byte_data_len];//建立 byte[] Array 一維陣列

            for (int x = 0; x < height; x++)
            {
                // 下面的循環節是模擬行掃描
                for (int y = 0; y < width; y++)
                {
                    byte_data[posScan++] = byte_data[posReal++];
                }
                posScan += offset;　 //行掃描結束，要將目標位置指針移過 那段“間隙”
            }

            // 用Marshal的Copy方法，將剛才得到的內存字節數組複製到 BitmapData中
            Marshal.Copy(byte_data, 0, iptr, byte_data_len);//複製記憶體區塊

            //解除綁定bitmap1和bmpData
            bitmap1.UnlockBits(bmpData);　 // 解鎖內存區域

            //修改過調色板 ST
            // 下面的代碼是為了修改生成位圖的索引表，從偽彩修改為灰度
            ColorPalette tempPalette;
            using (Bitmap tempBmp = new Bitmap(1, 1, PixelFormat.Format8bppIndexed))
            {
                tempPalette = tempBmp.Palette;
            }
            for (int i = 0; i < 256; i++)
            {
                tempPalette.Entries[i] = Color.FromArgb(i, i, i);
            }
            bitmap1.Palette = tempPalette;
            //修改過調色板 SP

            pictureBox1.Image = bitmap1;
        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //使用Unsafe轉灰階
            Restore_Picture();

            sw.Reset();
            sw.Start();

            Use_Unsafe_Code();


            sw.Stop();
            richTextBox1.Text += "耗時 : " + string.Format("{0,10}", sw.ElapsedMilliseconds.ToString()) + "\tmsec\n";

        }

        void Use_Unsafe_Code()
        {
            if (pictureBox1.Image != null)
            {
                int W = pictureBox1.Image.Width;
                int H = pictureBox1.Image.Height;
                Bitmap bitmap1 = (Bitmap)pictureBox1.Image;
                Bitmap bitmap2 = new Bitmap(W, H, PixelFormat.Format24bppRgb);

                //綁定bitmap1和bmpData1
                BitmapData bmpData1 = bitmap1.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadOnly, PixelFormat.Format24bppRgb);  //原圖
                //綁定bitmap2和bmpData2
                BitmapData bmpData2 = bitmap2.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);  //新圖即邊緣圖

                unsafe
                {
                    //首先第一段代碼是提取邊緣，邊緣置為黑色，其他部分置為白色
                    byte* pin = (byte*)(bmpData1.Scan0.ToPointer());
                    byte* pout = (byte*)(bmpData2.Scan0.ToPointer());
                    for (int y = 0; y < bmpData1.Height - 1; y++)
                    {
                        for (int x = 0; x < bmpData1.Width; x++)
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
                        pin += bmpData1.Stride - bmpData1.Width * 3;
                        pout += bmpData2.Stride - bmpData2.Width * 3;
                    }

                    //解除綁定bitmap1和bmpData1
                    bitmap1.UnlockBits(bmpData1);
                    //解除綁定bitmap2和bmpData2
                    bitmap2.UnlockBits(bmpData2);

                    pictureBox1.Image = bitmap2;
                }
            }
        }

        void Restore_Picture()
        {
            pictureBox1.Image = Image.FromFile(filename);
            Application.DoEvents();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //灰階圖片處理1_Bitmap類
            //提取像素法
            //使用的是GDI+中的Bitmap.GetPixel和Bitmap.SetPixel方法。

            button7.BackColor = Color.Red;
            Application.DoEvents();

            int H = this.pictureBox1.Image.Height;
            int W = this.pictureBox1.Image.Width;
            Bitmap bitmap = new Bitmap(W, H);
            Bitmap MyBitmap = (Bitmap)this.pictureBox1.Image;//從pictureBox取得Bitmap

            Bitmap bitmap1 = (Bitmap)pictureBox1.Image;
            Bitmap bmp = bitmap1.Clone() as Bitmap;

            Color pixel;
            int gray;
            for (int x = 0; x < W; x++)
            {
                for (int y = 0; y < H; y++)
                {
                    pixel = bmp.GetPixel(x, y);
                    gray = (int)(pixel.R * 0.299 + pixel.G * 0.587 + pixel.B * 0.114);
                    bmp.SetPixel(x, y, Color.FromArgb(gray, gray, gray));
                }
            }
            pictureBox1.Image = bmp.Clone() as Image;
            button7.BackColor = SystemColors.ControlLight;
        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //灰階圖片處理1_Bitmap類
            //提取像素法
            //使用的是GDI+中的Bitmap.GetPixel和Bitmap.SetPixel方法。

            button9.BackColor = Color.Red;
            Application.DoEvents();

            int H = this.pictureBox1.Image.Height;
            int W = this.pictureBox1.Image.Width;
            Bitmap bitmap = new Bitmap(W, H);
            Bitmap MyBitmap = (Bitmap)this.pictureBox1.Image;
            Color pixel;
            for (int x = 0; x < W; x++)
            {
                for (int y = 0; y < H; y++)
                {
                    pixel = MyBitmap.GetPixel(x, y);
                    int r, g, b, gray = 0;
                    r = pixel.R;
                    g = pixel.G;
                    b = pixel.B;
                    //實例程序以加權平均值法產生黑白圖像  
                    int iType = 2;
                    switch (iType)
                    {
                        case 0://平均值法  
                            gray = ((r + g + b) / 3);
                            break;
                        case 1://最大值法  
                            gray = r > g ? r : g;
                            gray = gray > b ? gray : b;
                            break;
                        case 2://加權平均值法  
                            gray = ((int)(0.7 * r) + (int)(0.2 * g) + (int)(0.1 * b));
                            break;
                    }
                    bitmap.SetPixel(x, y, Color.FromArgb(gray, gray, gray));
                }
            }
            this.pictureBox1.Image = bitmap;
            button9.BackColor = SystemColors.ControlLight;
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //使用byte[]數據，生成Bitmap

            int W = 256;
            int H = 256;
            int byte_data_len = W * H;
            byte[] imagedata = new byte[byte_data_len];//建立 byte[] Array 一維陣列

            int i;
            int j;
            for (j = 0; j < H; j++)
            {
                for (i = 0; i < W; i++)
                {
                    imagedata[256 * i + j] = (byte)i;
                }
            }
            Bitmap bitmap1 = CreateBitmap(imagedata, W, H);
            pictureBox1.Image = bitmap1;
        }

        //C#中使用byte[]數據，生成Bitmap
        /// <summary>
        /// 使用byte[]數據，生成256色灰度　BMP 位圖
        /// </summary>
        /// <param name="originalImageData"></param>
        /// <param name="originalWidth"></param>
        /// <param name="originalHeight"></param>
        /// <returns></returns>
        public static Bitmap CreateBitmap(byte[] originalImageData, int originalWidth, int originalHeight)
        {
            //指定8位格式，即256色
            Bitmap resultBitmap = new Bitmap(originalWidth, originalHeight, PixelFormat.Format8bppIndexed);
            //將該位圖存入內存中
            MemoryStream curImageStream = new MemoryStream();
            resultBitmap.Save(curImageStream, ImageFormat.Bmp);
            curImageStream.Flush();
            //由於位圖數據需要DWORD對齊（4byte倍數），計算需要補位的個數
            int curPadNum = ((originalWidth * 8 + 31) / 32 * 4) - originalWidth;
            //最終生成的位圖數據大小
            int bmpDataSize = ((originalWidth * 8 + 31) / 32 * 4) * originalHeight;
            //數據部分相對文件開始偏移，具體可以參考位圖文件格式
            int dataOffset = ReadData(curImageStream, 10, 4);
            //改變調色板，因為默認的調色板是32位彩色的，需要修改為256色的調色板
            int paletteStart = 54;
            int paletteEnd = dataOffset;
            int color = 0;
            for (int i = paletteStart; i < paletteEnd; i += 4)
            {
                byte[] tempColor = new byte[4];
                tempColor[0] = (byte)color;
                tempColor[1] = (byte)color;
                tempColor[2] = (byte)color;
                tempColor[3] = (byte)0;
                color++;
                curImageStream.Position = i;
                curImageStream.Write(tempColor, 0, 4);
            }
            //最終生成的位圖數據，以及大小，高度沒有變，寬度需要調整
            byte[] destImageData = new byte[bmpDataSize];//建立 byte[] Array 一維陣列
            int destWidth = originalWidth + curPadNum;
            //生成最終的位圖數據，注意的是，位圖數據 從左到右，從下到上，所以需要顛倒
            for (int originalRowIndex = originalHeight - 1; originalRowIndex >= 0; originalRowIndex--)
            {
                int destRowIndex = originalHeight - originalRowIndex - 1;
                for (int dataIndex = 0; dataIndex < originalWidth; dataIndex++)
                {
                    //同時還要注意，新的位圖數據的寬度已經變化destWidth，否則會產生錯位
                    destImageData[destRowIndex * destWidth + dataIndex] = originalImageData[originalRowIndex * originalWidth + dataIndex];
                }
            }
            //將流的Position移到數據段　　
            curImageStream.Position = dataOffset;
            //將新位圖數據寫入內存中
            curImageStream.Write(destImageData, 0, bmpDataSize);
            curImageStream.Flush();
            //將內存中的位圖寫入Bitmap對象
            resultBitmap = new Bitmap(curImageStream);
            return resultBitmap;
        }

        /// <summary>
        /// 從內存流中指定位置，讀取數據
        /// </summary>
        /// <param name="curStream"></param>
        /// <param name="startPosition"></param>
        /// <param name="length"></param>
        /// <returns></returns>
        public static int ReadData(MemoryStream curStream, int startPosition, int length)
        {
            int result = -1;
            byte[] tempData = new byte[length];//建立 byte[] Array 一維陣列
            curStream.Position = startPosition;
            curStream.Read(tempData, 0, length);
            result = BitConverter.ToInt32(tempData, 0);
            return result;
        }

        /// <summary>
        /// 向內存流中指定位置，寫入數據
        /// </summary>
        /// <param name="curStream"></param>
        /// <param name="startPosition"></param>
        /// <param name="length"></param>
        /// <param name="value"></param>
        public static void WriteData(MemoryStream curStream, int startPosition, int length, int value)
        {
            curStream.Position = startPosition;
            curStream.Write(BitConverter.GetBytes(value), 0, length);
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //圖片測試
            string filename = @"C:\_git\vcs\_1.data\______test_files1\elephant.jpg";
            Image sample = new Bitmap(filename);
            MemoryStream buf = new MemoryStream();
            sample.Save(buf, ImageFormat.Bmp);
            byte[] currentImage = buf.GetBuffer();

            int[] stats = new int[3];
            for (int i = 0; i < currentImage.Length; )
            {
                for (int j = 0; j < 3; j++)
                {
                    stats[j] += currentImage[i];
                    ++i;
                }
            }
            richTextBox1.Text += "Blue: " + stats[0] + "\n";
            richTextBox1.Text += "Green: " + stats[1] + "\n";
            richTextBox1.Text += "Red: " + stats[2] + "\n";
            if ((stats[0] > stats[1]) && (stats[0] > stats[2]))
            {
                richTextBox1.Text += "This is a cold picture." + "\n";
            }
            if ((stats[1] > stats[0]) && (stats[1] > stats[2]))
            {
                richTextBox1.Text += "This is a summer picture." + "\n";
            }
            if ((stats[2] > stats[0]) && (stats[2] > stats[1]))
            {
                richTextBox1.Text += "This is a fiery picture." + "\n";
            }
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //建立一個GrayBitmapData類做影像處理

            //轉換爲灰度圖

            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bitmap1 = new Bitmap(filename);

            if (bitmap1 == null)
                return;

            GrayBitmapData gbmp = new GrayBitmapData(bitmap1);
            gbmp.ShowImage(pictureBox1);
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //建立一個GrayBitmapData類做影像處理

            //均值濾波

            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bitmap1 = new Bitmap(filename);

            if (bitmap1 == null)
                return;

            GrayBitmapData gbmp = new GrayBitmapData(bitmap1);
            gbmp.AverageFilter(3);
            gbmp.ShowImage(pictureBox1);
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //圖片 轉 拜列
            richTextBox1.Text += "圖片 轉 拜列\n";

            string filename = @"C:\_git\vcs\_1.data\______test_files1\__pic\_anime\doraemon1.jpg";
            Image image = Image.FromFile(filename);

            byte[] byte_data = null;

            using (MemoryStream mostream = new MemoryStream())
            {
                Bitmap bmp = new Bitmap(image);
                bmp.Save(mostream, ImageFormat.Bmp);//將圖像以指定的格式存入緩存內存流
                byte_data = new byte[mostream.Length];
                mostream.Position = 0;//設置留的初始位置
                mostream.Read(byte_data, 0, Convert.ToInt32(byte_data.Length));
            }

            for (int i = 0; i < 100; i++)
            {
                richTextBox1.Text += byte_data[i].ToString("D03");
                if ((i % 16) == 15)
                    richTextBox1.Text += "\n";
                else
                    richTextBox1.Text += " ";
            }
            richTextBox1.Text += "\n";
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //將圖片放入拜列
            //將圖片放入拜列 Image轉拜列

            string filename = @"C:\_git\vcs\_1.data\______test_files1\pic_256X100.bmp";

            Image image = Image.FromFile(filename);

            MemoryStream ms = new MemoryStream();
            image.Save(ms, image.RawFormat);
            Byte[] byte_array = ms.ToArray();

            int len = byte_array.Length;
            richTextBox1.Text += "len = " + len.ToString() + "\n";
            int i;
            for (i = 54; i < (54 + 256 * 2); i++)
            {
                richTextBox1.Text += byte_array[i].ToString("D03") + " ";
            }

            //拜列轉Image
        }

        private void button16_Click(object sender, EventArgs e)
        {
            //Marshal.Copy
            //C# 將 BitmapData 複製到 byte[] Array 一維陣列
            //Marshal.Copy() 應用

            richTextBox1.Text += "Marshal.Copy() 測試 複製記憶體區塊\n";

            string filename = @"C:\_git\vcs\_1.data\______test_files1\__pic\_anime\doraemon1.jpg";
            //string filename = @"C:\_git\vcs\_1.data\______test_files1\__pic\_map_city/global.c.gif";   //超大圖, 要很久

            Bitmap bmp = new Bitmap(filename);

            int W = bmp.Width;
            int H = bmp.Height;

            //綁定bmp和bmpData
            //使用原本的像素格式
            //BitmapData bmpData = bmp.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadWrite, bmp.PixelFormat);
            //指定像素格式轉為24比特
            BitmapData bmpData = bmp.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            var stride = Math.Abs(bmpData.Stride);//取得記憶體寬度

            //建立 byte[] Array 一維陣列
            int byte_data_len = stride * H;
            byte[] byte_data = new byte[byte_data_len];

            //拷貝出來 bmpData => byte_data 圖片轉陣列
            Marshal.Copy(bmpData.Scan0, byte_data, 0, byte_data_len);//複製記憶體區塊

            //做處理, 例如 灰階
            byte r, g, b;
            for (int y = 0; y < H; y++)
            {
                for (int x = 0; x < W * 3; x += 3)
                {
                    r = byte_data[stride * y + x + 2];
                    g = byte_data[stride * y + x + 1];
                    b = byte_data[stride * y + x];
                    //byte gray = (byte)((r + g + b) / 3);
                    byte gray = (byte)((double)r * .299000 + (double)g * .587000 + (double)b * .114000);
                    byte_data[stride * y + x + 2] = gray;
                    byte_data[stride * y + x + 1] = gray;
                    byte_data[stride * y + x] = gray;
                }
            }

            // 拷貝回去 byte_data => bmpData 陣列轉圖片
            Marshal.Copy(byte_data, 0, bmpData.Scan0, byte_data_len);//複製記憶體區塊

            //解除綁定bmp和bmpData
            bmp.UnlockBits(bmpData);

            pictureBox1.Image = bmp;
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
        }

        private void button17_Click(object sender, EventArgs e)
        {
            //比較Marshal.Copy
            //將 BitmapData 複製到 byte[] Array 陣列

            //Marshal.Copy()
            //C# 將 BitmapData 複製到 byte[] Array 陣列
            //以下有兩種方法複製 BitmapData，一個是使用 unsafe 方法，一個一個 byte 複製，另外一個是複製記憶體區塊，較為快速。
            //目前測試為，第二種方法比第一種方法快四倍。

            //編譯時要選用/unsafe選項

            Bitmap bmp = new Bitmap(@"C:/_git/vcs/_1.data/______test_files1/test_ReadAllBytes.bmp");
            int W = bmp.Width;
            int H = bmp.Height;

            int w;
            int h;
            int dataIndex = 0;

            BitmapData bmpData = bmp.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadOnly, PixelFormat.Format24bppRgb);
            Stopwatch sw = new Stopwatch();
            sw.Start();
            for (int xx = 0; xx < 1000; xx++)   //做一千次 為了量測時間
            {
                //一個一個byte複製
                w = bmpData.Width;
                h = bmpData.Height;
                dataIndex = 0;
                byte[] data = new byte[w * h * 3];//建立 byte[] Array 一維陣列
                unsafe
                {
                    byte* p = (byte*)bmpData.Scan0.ToPointer();
                    for (int y = 0; y < h; y++)
                    {
                        for (int x = 0; x < w; x++)
                        {
                            data[dataIndex++] = p[0];
                            data[dataIndex++] = p[1];
                            data[dataIndex++] = p[2];
                            p += 3;
                        }
                    }
                }
            }
            sw.Stop();
            richTextBox1.Text += "Time1: " + (sw.ElapsedMilliseconds / 1000).ToString() + "." + (sw.ElapsedMilliseconds % 1000).ToString("D3") + " 秒\n";
            sw.Reset();
            sw.Start();
            for (int xx = 0; xx < 1000; xx++)   //做一千次 為了量測時間
            {
                byte[] data = new byte[bmpData.Width * bmpData.Height * 3];//建立 byte[] Array 一維陣列
                Marshal.Copy(bmpData.Scan0, data, 0, data.Length);//複製記憶體區塊
            }
            sw.Stop();
            richTextBox1.Text += "Time2: " + (sw.ElapsedMilliseconds / 1000).ToString() + "." + (sw.ElapsedMilliseconds % 1000).ToString("D3") + " 秒\n";

            //解除綁定bmp和bmpData
            bmp.UnlockBits(bmpData);

            BitmapData bmpData2 = bmp.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadOnly, PixelFormat.Format24bppRgb);

            //一個一個byte複製
            w = bmpData2.Width;
            h = bmpData2.Height;
            dataIndex = 0;
            byte[] data2 = new byte[w * h * 4];//建立 byte[] Array 一維陣列
            unsafe
            {
                byte* p = (byte*)bmpData2.Scan0.ToPointer();
                for (int y = 0; y < h; y++)
                {
                    for (int x = 0; x < w; x++)
                    {
                        data2[dataIndex++] = p[0];
                        data2[dataIndex++] = p[1];
                        data2[dataIndex++] = p[2];
                        data2[dataIndex++] = 0xFF;
                        p += 3;
                    }
                }
            }
            //解除綁定bmp和bmpData2
            bmp.UnlockBits(bmpData2);
        }

        private void button18_Click(object sender, EventArgs e)
        {
            //Marshal.Copy 1
            //Marshal 彩色轉灰階

            string filename = @"C:\_git\vcs\_1.data\______test_files1\__pic\_anime\doraemon1.jpg";
            color_to_gray_2(filename);
        }

        void color_to_gray_2(string filename)
        {
            richTextBox1.Text += "Marshal 彩色轉灰階\n";

            //int data_offset = 0;
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
            System.Runtime.InteropServices.Marshal.Copy(ptr, rgbValues, 0, len);

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
            for (int counter = 0; counter < (rgbValues.Length - 20); counter += 3)
            {
                byte bbb = rgbValues[counter];      //Blue
                byte ggg = rgbValues[counter + 1];  //Green
                byte rrr = rgbValues[counter + 2];  //Red

                int Gray = (rrr * 299 + ggg * 587 + bbb * 114 + 500) / 1000;

                rgbValues[counter] = (byte)Gray;
                rgbValues[counter + 1] = (byte)Gray;
                rgbValues[counter + 2] = (byte)Gray;
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
            System.Runtime.InteropServices.Marshal.Copy(rgbValues, 0, ptr, len);

            // Unlock the bits.
            bmp.UnlockBits(bmpData);

            // Draw the modified image.
            pictureBox1.Image = bmp;
        }

        private void button19_Click(object sender, EventArgs e)
        {
            //Marshal.Copy 2
            PictureToGray3();
        }

        #region 灰度處理

        private void PictureToGray3()
        {
            //灰度處理
            string filename = @"C:\_git\vcs\_1.data\______test_files1\__pic\_anime\doraemon1.jpg";
            Bitmap bitmap1 = new Bitmap(filename);
            pictureBox1.Image = bitmap1;
            Bitmap bitmap2 = 灰度處理(bitmap1);
            pictureBox1.Image = bitmap2;
        }

        /// <summary>  
        /// 灰度處理(BitmapData類)  
        /// </summary>  
        /// <returns>輸出8位灰度圖片</returns>  
        public static Bitmap 灰度處理(Bitmap 圖像)
        {
            Bitmap bmp = new Bitmap(圖像.Width, 圖像.Height, PixelFormat.Format8bppIndexed);

            //設定實例BitmapData相關信息  
            Rectangle rect = new Rectangle(0, 0, bmp.Width, bmp.Height);

            BitmapData data = 圖像.LockBits(rect, ImageLockMode.ReadOnly, PixelFormat.Format24bppRgb);
            //鎖定bmp到系統內存中  
            BitmapData data2 = bmp.LockBits(rect, ImageLockMode.ReadWrite, PixelFormat.Format8bppIndexed);

            //獲取位圖中第一個像素數據的地址  
            IntPtr ptr = data.Scan0;
            IntPtr ptr2 = data2.Scan0;

            int numBytes = data.Stride * data.Height;
            int numBytes2 = data2.Stride * data2.Height;

            int n2 = data2.Stride - bmp.Width; //// 顯示寬度與掃描線寬度的間隙  

            byte[] rgbValues = new byte[numBytes];
            byte[] rgbValues2 = new byte[numBytes2];
            //將bmp數據Copy到申明的數組中  
            Marshal.Copy(ptr, rgbValues, 0, numBytes);
            Marshal.Copy(ptr2, rgbValues2, 0, numBytes2);

            int n = 0;

            for (int y = 0; y < bmp.Height; y++)
            {
                for (int x = 0; x < bmp.Width * 3; x += 3)
                {
                    int i = data.Stride * y + x;

                    double value = rgbValues[i + 2] * 0.299 + rgbValues[i + 1] * 0.587 + rgbValues[i] * 0.114; //計算灰度  

                    rgbValues2[n] = (byte)value;

                    n++;
                }
                n += n2; //跳過差值  
            }

            //將數據Copy到內存指針  
            Marshal.Copy(rgbValues, 0, ptr, numBytes);
            Marshal.Copy(rgbValues2, 0, ptr2, numBytes2);

            //// 下面的代碼是為了修改生成位圖的索引表，從偽彩修改為灰度  
            ColorPalette tempPalette;
            using (Bitmap tempBmp = new Bitmap(1, 1, PixelFormat.Format8bppIndexed))
            {
                tempPalette = tempBmp.Palette;
            }
            for (int i = 0; i < 256; i++)
            {
                tempPalette.Entries[i] = Color.FromArgb(i, i, i);
            }

            bmp.Palette = tempPalette;


            //從系統內存解鎖bmp  
            圖像.UnlockBits(data);
            bmp.UnlockBits(data2);

            return bmp;
        }
        #endregion

        private void button20_Click(object sender, EventArgs e)
        {
            //影像資料處理
            Graphics g = this.pictureBox1.CreateGraphics();

            string filename = @"C:\_git\vcs\_1.data\______test_files1\__pic\rgb.jpg";

            richTextBox1.Text += "filename : " + filename + "\n";
            //Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);  //使用Image.FromFile創建圖形對象 same
            Bitmap bitmap1 = new Bitmap(filename);
            int W = bitmap1.Width;
            int H = bitmap1.Height;

            int bytes_per_pixel = 0;    //每個像素使用的拜數 bmp/png每點用4拜, jpg每點用3拜

            g.DrawImage(bitmap1, 0, 0);

            //把圖像複製到內存中

            //獲取圖像的BitmapData對像
            Rectangle rect = new Rectangle(0, 0, W, H);	//位圖矩形

            //以可讀寫的方式鎖定全部位圖像素
            BitmapData bmpData = bitmap1.LockBits(rect, ImageLockMode.ReadWrite, bitmap1.PixelFormat);   // Lock the bits.
            //BitmapData bmpData = bitmap1.LockBits(rect, ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb); //指明PixelFormat

            // Get the address of the first line.
            IntPtr ptr = bmpData.Scan0; //得到首地址

            // Declare an array to hold the bytes of the bitmap.
            //int len = W * 4 * H;    //每個pixel要用4拜存資料 R G B A
            int len = Math.Abs(bmpData.Stride) * H;   //24位BMP位圖字節數 stride = W * 4, 每個pixel要用4拜存資料 R G B A, 也有可能是3拜
            //stride : 每個掃描行的長度

            bytes_per_pixel = Math.Abs(bmpData.Stride) / W;

            richTextBox1.Text += "stride = " + bmpData.Stride.ToString() + "\n";
            richTextBox1.Text += "len = " + len.ToString() + "\n";

            //存bitmap資料的陣列
            byte[] rgbValues = new byte[len]; //定義位圖數組

            richTextBox1.Text += "len = " + len.ToString() + "\n";
            // Copy the RGB values into the array.
            Marshal.Copy(ptr, rgbValues, 0, len); //複製被鎖定的位圖像素到位圖數組

            richTextBox1.Text += "len2 = " + rgbValues.Length.ToString() + "\n";
            int i;
            string result = string.Empty;
            for (i = 0; i < len; i++)
            {
                if ((bytes_per_pixel == 4) && (((i % (256 * bytes_per_pixel)) == (256 * bytes_per_pixel - 1))))
                {
                    result += "\n";
                }

                if ((bytes_per_pixel == 4) && ((i % 4) == 3))
                    continue;

                result += rgbValues[i].ToString("X2");
                if ((i % (256 * bytes_per_pixel)) == (256 * bytes_per_pixel - 1))
                {
                    result += "\n";
                }
                else
                {
                    result += " ";
                }
            }
            richTextBox1.Text += result + "\n";

            // Set every third value to 255. A 24bpp bitmap will look red.  
            for (int counter = 2; counter < rgbValues.Length; counter += bytes_per_pixel)
            {
                rgbValues[counter] = 255;
            }

            // Copy the RGB values back to the bitmap
            Marshal.Copy(rgbValues, 0, ptr, len);

            // Unlock the bits.
            bitmap1.UnlockBits(bmpData);

            // Draw the modified image.
            g.DrawImage(bitmap1, 0, 50);
        }

        private void button21_Click(object sender, EventArgs e)
        {
            //偽色彩

            //string filename1 = @"C:\_git\vcs\_1.data\______test_files1\__pic\_ntuh\op1.jpg";
            string filename1 = @"C:\_git\vcs\_1.data\______test_files1\fakecolor.jpg";    //偽色彩處理

            /*
            //彩色轉灰階
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename1);	//Bitmap.FromFile出來的是Image格式

            //SetPixel 彩色轉灰階
            Bitmap bitmap2 = color_to_gray(bitmap1);

            pictureBox1.Image = bitmap1;
            */

            //彩色轉灰階

            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename1);	//Bitmap.FromFile出來的是Image格式

            //SetPixel 彩色轉灰階
            Bitmap bitmap2 = color_to_gray(bitmap1);

            bitmap2 = gcTrans(bitmap1, true, 255 / 10);
            pictureBox1.Image = bitmap2;

            /*
            int border = 80;
            x_st = border;
            y_st = border;
            w = W - border * 2;
            h = H - border * 2;


            ImageEnhancement(x_st, y_st, w, h);
            */


            //偽彩色處理
            /*
            //從pictureBox取得Bitmap
            Bitmap bitmap1 = (Bitmap)pictureBox1.Image;
            bitmap1 = gcTrans(bitmap1, true, 5);
            pictureBox2.Image = bitmap1;
            */
            /*
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename3);	//Bitmap.FromFile出來的是Image格式
            Bitmap bitmap2 = gcTrans(bitmap1, true, 255 / 10);
            pictureBox20.Image = bitmap2;
            */
        }

        Bitmap color_to_gray(Bitmap bitmap1)
        {
            //richTextBox1.Text += "SetPixel 彩色轉灰階\n";

            int xx;
            int yy;

            for (yy = 0; yy < bitmap1.Height; yy++)
            {
                for (xx = 0; xx < bitmap1.Width; xx++)
                {
                    byte rrr = bitmap1.GetPixel(xx, yy).R;
                    byte ggg = bitmap1.GetPixel(xx, yy).G;
                    byte bbb = bitmap1.GetPixel(xx, yy).B;

                    int Gray = (rrr * 299 + ggg * 587 + bbb * 114 + 500) / 1000;
                    Color zz = Color.FromArgb(255, Gray, Gray, Gray);

                    bitmap1.SetPixel(xx, yy, zz);
                }
            }
            return bitmap1;
        }

        //偽彩色圖像處理 ST

        /// <summary>
        /// 偽彩色圖像處理
        /// 博客園-初行 http://www.cnblogs.com/zxlovenet
        /// 日期：2014.2.14
        /// </summary>
        /// <param name="bmp">傳入的灰度圖像</param>
        /// <param name="method">使用何種方法，false強度分層法,true灰度級-彩色變換法</param>
        /// <param name="seg">強度分層中的分層數</param>
        /// <returns>返回偽彩色圖像</returns>
        private Bitmap gcTrans(Bitmap bmp, bool method, byte seg)
        {
            if (bmp != null)
            {
                if (System.Drawing.Imaging.PixelFormat.Format24bppRgb == bmp.PixelFormat)
                {
                    Rectangle rect = new Rectangle(0, 0, bmp.Width, bmp.Height);

                    //綁定bmp和bmpData
                    System.Drawing.Imaging.BitmapData bmpData = bmp.LockBits(rect, System.Drawing.Imaging.ImageLockMode.ReadWrite, bmp.PixelFormat);

                    IntPtr ptr = bmpData.Scan0;

                    //建立 byte[] Array 一維陣列
                    int bytes = bmp.Width * bmp.Height * 3;
                    byte[] grayValues = new byte[bytes];

                    //拷貝出來 bmpData => byte_data 圖片轉陣列
                    System.Runtime.InteropServices.Marshal.Copy(ptr, grayValues, 0, bytes);//複製記憶體區塊
                    bmp.UnlockBits(bmpData);

                    byte[] rgbValues = new byte[bytes];
                    //清零
                    Array.Clear(rgbValues, 0, bytes);
                    byte tempB;

                    if (method == false)
                    {
                        //強度分層法
                        for (int i = 0; i < bytes; i += 3)
                        {
                            byte ser = (byte)(256 / seg);
                            tempB = (byte)(grayValues[i] / ser);
                            //分配任意一種顏色
                            rgbValues[i + 1] = (byte)(tempB * ser);
                            rgbValues[i] = (byte)((seg - 1 - tempB) * ser);
                            rgbValues[i + 2] = 0;
                        }
                    }
                    else
                    {
                        //灰度級-彩色變換法
                        for (int i = 0; i < bytes; i += 3)
                        {
                            if (grayValues[i] < 64)
                            {
                                rgbValues[i + 2] = 0;
                                rgbValues[i + 1] = (byte)(4 * grayValues[i]);
                                rgbValues[i] = 255;
                            }
                            else if (grayValues[i] < 128)
                            {
                                rgbValues[i + 2] = 0;
                                rgbValues[i + 1] = 255;
                                rgbValues[i] = (byte)(-4 * grayValues[i] + 2 * 255);
                            }
                            else if (grayValues[i] < 192)
                            {
                                rgbValues[i + 2] = (byte)(4 * grayValues[i] - 2 * 255);
                                rgbValues[i + 1] = 255;
                                rgbValues[i] = 0;
                            }
                            else
                            {
                                rgbValues[i + 2] = 255;
                                rgbValues[i + 1] = (byte)(-4 * grayValues[i] + 4 * 255);
                                rgbValues[i] = 0;
                            }
                        }

                    }
                    bmp = new Bitmap(bmp.Width, bmp.Height, System.Drawing.Imaging.PixelFormat.Format24bppRgb);
                    bmpData = bmp.LockBits(rect, System.Drawing.Imaging.ImageLockMode.ReadWrite, bmp.PixelFormat);
                    ptr = bmpData.Scan0;

                    // 拷貝回去 byte_data => bmpData 陣列轉圖片
                    System.Runtime.InteropServices.Marshal.Copy(rgbValues, 0, ptr, bytes);//複製記憶體區塊

                    //解除綁定bmp和bmpData
                    bmp.UnlockBits(bmpData);

                    return bmp;
                }
                else
                {
                    return null;
                }
            }
            else
            {
                return null;
            }
        }
        //偽彩色圖像處理 SP

        private void button22_Click(object sender, EventArgs e)
        {
            //二值化圖片
            string filename = @"C:\_git\vcs\_1.data\______test_files1\__pic\_anime\doraemon1.jpg";
            pictureBox1.Image = OtsuThreshold(new Bitmap(filename));
        }

        //二值化圖片 ST

        #region 二值化
        #region Otsu閾值法二值化模組
        /// <summary>   
        /// Otsu閾值   
        /// </summary>   
        /// <param name="b">點陣圖流</param>   
        /// <returns></returns>   
        public Bitmap OtsuThreshold(Bitmap bitmap)
        {
            // 影像灰度化   
            // b = Gray(b);   
            int width = bitmap.Width;
            int height = bitmap.Height;
            byte threshold = 0;
            int[] hist = new int[256];

            int AllPixelNumber = 0, PixelNumberSmall = 0, PixelNumberBig = 0;

            double MaxValue, AllSum = 0, SumSmall = 0, SumBig, ProbabilitySmall, ProbabilityBig, Probability;
            BitmapData bmpData = bitmap.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, System.Drawing.Imaging.PixelFormat.Format32bppArgb);


            unsafe
            {
                byte* p = (byte*)bmpData.Scan0;
                int offset = bmpData.Stride - width * 4;
                for (int j = 0; j < height; j++)
                {
                    for (int i = 0; i < width; i++)
                    {
                        hist[p[0]]++;
                        p += 4;
                    }
                    p += offset;
                }
                bitmap.UnlockBits(bmpData);
            }
            //計算灰度為I的畫素出現的概率   
            for (int i = 0; i < 256; i++)
            {
                AllSum += i * hist[i];     //   質量矩   
                AllPixelNumber += hist[i];  //  質量       
            }
            MaxValue = -1.0;
            for (int i = 0; i < 256; i++)
            {
                PixelNumberSmall += hist[i];
                PixelNumberBig = AllPixelNumber - PixelNumberSmall;
                if (PixelNumberBig == 0)
                {
                    break;
                }

                SumSmall += i * hist[i];
                SumBig = AllSum - SumSmall;
                ProbabilitySmall = SumSmall / PixelNumberSmall;
                ProbabilityBig = SumBig / PixelNumberBig;
                Probability = PixelNumberSmall * ProbabilitySmall * ProbabilitySmall + PixelNumberBig * ProbabilityBig * ProbabilityBig;
                if (Probability > MaxValue)
                {
                    MaxValue = Probability;
                    threshold = (byte)i;
                }
            }
            this.Threshoding(bitmap, threshold);
            bitmap = twoBit(bitmap);
            return bitmap;

        }
        #endregion

        #region      固定閾值法二值化模組
        public Bitmap Threshoding(Bitmap b, byte threshold)
        {
            int width = b.Width;
            int height = b.Height;
            BitmapData data = b.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, System.Drawing.Imaging.PixelFormat.Format32bppArgb);
            unsafe
            {
                byte* p = (byte*)data.Scan0;
                int offset = data.Stride - width * 4;
                byte R, G, B, gray;
                for (int y = 0; y < height; y++)
                {
                    for (int x = 0; x < width; x++)
                    {
                        R = p[2];
                        G = p[1];
                        B = p[0];
                        gray = (byte)((R * 19595 + G * 38469 + B * 7472) >> 16);
                        if (gray >= threshold)
                        {
                            p[0] = p[1] = p[2] = 255;
                        }
                        else
                        {
                            p[0] = p[1] = p[2] = 0;
                        }
                        p += 4;
                    }
                    p += offset;
                }
                b.UnlockBits(data);
                return b;

            }

        }
        #endregion



        /// <summary>
        /// 建立1點陣圖像
        /// </summary>
        /// <param name="srcBitmap"></param>
        /// <returns></returns>
        public Bitmap twoBit(Bitmap srcBitmap)
        {
            int midrgb = System.Drawing.Color.FromArgb(128, 128, 128).ToArgb();
            int stride;//簡單公式((width/8)+3)&(~3)
            stride = (srcBitmap.Width % 8) == 0 ? (srcBitmap.Width / 8) : (srcBitmap.Width / 8) + 1;
            stride = (stride % 4) == 0 ? stride : ((stride / 4) + 1) * 4;
            int k = srcBitmap.Height * stride;
            byte[] buf = new byte[k];
            int x = 0, ab = 0;
            for (int j = 0; j < srcBitmap.Height; j++)
            {
                k = j * stride;//因影象寬度不同、有的可能有填充位元組需要跳越
                x = 0;
                ab = 0;
                for (int i = 0; i < srcBitmap.Width; i++)
                {
                    //從灰度變單色（下法如果直接從彩色變單色效果不太好，不過反相也可以在這裡控制）
                    if ((srcBitmap.GetPixel(i, j)).ToArgb() > midrgb)
                    {
                        ab = ab * 2 + 1;
                    }
                    else
                    {
                        ab = ab * 2;
                    }
                    x++;
                    if (x == 8)
                    {
                        buf[k++] = (byte)ab;//每位元組賦值一次，陣列buf中儲存的是十進位制。
                        ab = 0;
                        x = 0;
                    }
                }
                if (x > 0)
                {
                    //迴圈實現：剩餘有效資料不滿1位元組的情況下須把它們移往位元組的高位部分
                    for (int t = x; t < 8; t++) ab = ab * 2;
                    buf[k++] = (byte)ab;
                }
            }
            int width = srcBitmap.Width;
            int height = srcBitmap.Height;
            Bitmap dstBitmap = new Bitmap(width, height, System.Drawing.Imaging.PixelFormat.Format1bppIndexed);
            BitmapData dt = dstBitmap.LockBits(new Rectangle(0, 0, dstBitmap.Width, dstBitmap.Height), ImageLockMode.ReadWrite, dstBitmap.PixelFormat);
            Marshal.Copy(buf, 0, dt.Scan0, buf.Length);
            dstBitmap.UnlockBits(dt);
            return dstBitmap;
        }
        #endregion
        //二值化圖片 SP

        private void button23_Click(object sender, EventArgs e)
        {
            string filename = @"C:\_git\vcs\_1.data\______test_files1\__pic\_anime\doraemon1.jpg";
            pictureBox1.Image = RGB2Gray(new Bitmap(filename));
        }

        //建立8位灰度影像 ST
        /// 建立8位灰度影像
        /// </summary>
        /// <param name="width"></param>
        /// <param name="height"></param>
        /// <returns></returns>
        public static Bitmap CreateGrayscaleImage(int width, int height)
        {
            // create new image
            Bitmap bmp = new Bitmap(width, height, System.Drawing.Imaging.PixelFormat.Format8bppIndexed);
            // set palette to grayscale
            SetGrayscalePalette(bmp);
            // return new image
            return bmp;
        }

        ///<summary>
        /// Set pallete of the image to grayscale
        ///</summary>
        public static void SetGrayscalePalette(Bitmap srcImg)
        {
            // check pixel format
            if (srcImg.PixelFormat != System.Drawing.Imaging.PixelFormat.Format8bppIndexed)
                throw new ArgumentException();
            // get palette
            ColorPalette cp = srcImg.Palette;
            // init palette
            for (int i = 0; i < 256; i++)
            {
                cp.Entries[i] = System.Drawing.Color.FromArgb(i, i, i);
            }
            srcImg.Palette = cp;
        }

        /// <summary>
        /// 轉為灰度影象，位深度也改變
        /// </summary>
        /// <param name="srcBitmap"></param>
        /// <returns></returns>
        public static Bitmap RGB2Gray(Bitmap srcBitmap)
        {
            int wide = srcBitmap.Width;
            int height = srcBitmap.Height;
            Rectangle rect = new Rectangle(0, 0, wide, height);
            //將Bitmap鎖定到系統記憶體中,獲得BitmapData
            BitmapData srcBmData = srcBitmap.LockBits(rect, ImageLockMode.ReadWrite, System.Drawing.Imaging.PixelFormat.Format24bppRgb);
            //建立Bitmap
            Bitmap dstBitmap = CreateGrayscaleImage(wide, height);//這個函式在後面有定義
            BitmapData dstBmData = dstBitmap.LockBits(rect, ImageLockMode.ReadWrite, System.Drawing.Imaging.PixelFormat.Format8bppIndexed);
            //點陣圖中第一個畫素資料的地址。它也可以看成是點陣圖中的第一個掃描行
            System.IntPtr srcPtr = srcBmData.Scan0;
            System.IntPtr dstPtr = dstBmData.Scan0;
            //將Bitmap物件的資訊存放到byte陣列中
            int src_bytes = srcBmData.Stride * height;
            byte[] srcValues = new byte[src_bytes];
            int dst_bytes = dstBmData.Stride * height;
            byte[] dstValues = new byte[dst_bytes];

            //複製GRB資訊到byte陣列
            Marshal.Copy(srcPtr, srcValues, 0, src_bytes);
            Marshal.Copy(dstPtr, dstValues, 0, dst_bytes);
            //根據Y=0.299*R+0.114*G+0.587B,Y為亮度
            for (int i = 0; i < height; i++)
                for (int j = 0; j < wide; j++)
                {
                    //只處理每行中影象畫素資料,捨棄未用空間
                    //注意點陣圖結構中RGB按BGR的順序儲存
                    int k = 3 * j;
                    byte temp = (byte)(srcValues[i * srcBmData.Stride + k + 2] * .299 + srcValues[i * srcBmData.Stride + k + 1] * .587 + srcValues[i * srcBmData.Stride + k] * .114);
                    dstValues[i * dstBmData.Stride + j] = temp;
                }

            Marshal.Copy(dstValues, 0, dstPtr, dst_bytes);
            //解鎖點陣圖
            srcBitmap.UnlockBits(srcBmData);
            dstBitmap.UnlockBits(dstBmData);
            return dstBitmap;
        }
        //建立8位灰度影像 SP

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
            //解除綁定bmp和bmpData
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
            //解除綁定bmp和bmpData
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

/*
IntPtr iptr = bmpData.Scan0;　 // 獲取bmpData的內存起始位置

//richTextBox1.Text += "耗時 : " + string.Format("{0,10}", sw.ElapsedMilliseconds.ToString()) + "\tmsec\n";

//Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式

首先用 BitmapData.Scan0找到第0個像素的第0個分量的地址。這個地址指向的是個byte類型，所以當時定義為byte* pIn。

為使用了unsafe，所以編譯的時候需要設置“允許不安全的代碼”。

直接用 Marshal 操作
                    r = Marshal.ReadByte(bmpData.Scan0, stride * y + x + 2);
                    g = Marshal.ReadByte(bmpData.Scan0, stride * y + x + 1);
                    b = Marshal.ReadByte(bmpData.Scan0, stride * y + x);

                    Marshal.WriteByte(bmpData.Scan0, stride * y + x + 2, (byte)(255 - r));
                    Marshal.WriteByte(bmpData.Scan0, stride * y + x + 1, (byte)(255 - g));
                    Marshal.WriteByte(bmpData.Scan0, stride * y + x, (byte)(255 - b));
 
        //C#中將byte數組轉換為8bit灰度圖像
        byte數組存放的是圖像每個像素的灰度值，byte類型正好是從0~255，存放8bit灰度圖像的時候，一個 數組元素就是一個像素的灰度值。僅有這個數組還不足以恢復出原來的圖像，還必須事先知道圖像的長、 寬值；
        創建Bitmap類的時候必須指定PixelFormat為Format8bppIndexed，這樣才最符合圖像本身的特性；
        Bitmap類雖然提供了GetPixel()、SetPixel()這樣的方法，但我們絕對不能用這兩個方法來進行大規 模的像素讀寫，因為它們的性能實在很囧；
        托管代碼中，能不用unsafe就盡量不用。在.Net 2.0中已經提供了BitmapData類及其LockBits()、 UnLockBits()操作，能夠安全地進行內存讀寫；
        圖像的width和它存儲時的stride是不一樣的。位圖的掃描線寬度一定是4的倍數，因此圖像在內存中 的大小並不是它的顯示大小；
        Format8bppIndexed類型的PixelFormat是索引格式，其調色板並不是灰度的而是偽彩，因此需要我們 對其加以修改。
 

            int PixelCount = W * H;

            // get bmp bitmap pixel format size
            int Depth = Bitmap.GetPixelFormatSize(bmp.PixelFormat);

            // Check if bpp (Bits Per Pixel) is 8, 24, or 32
            if (Depth != 8 && Depth != 24 && Depth != 32)
            {
                throw new ArgumentException("Only 8, 24 and 32 bpp images are supported.");
            }


 int data_offset = 0;

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
            {
                richTextBox1.Text += "位元深度\tunknown, PixelFormat = " + bmp.PixelFormat.ToString() + "\n";
            }
*/
/*


            Color compareClr = Color.FromArgb(255, 255, 255, 255);
            for (int y = 0; y < bmp.Height; y++)
            {
                for (int x = 0; x < bmp.Width; x++)
                {
                    if (bmp.GetPixel(x, y) == compareClr)    //获取颜色
                    {
                        bmp.SetPixel(x, y, Color.Red);
                    }
                }
            }

            //内存法
            //定义一个类LockBitmap，通过把Bitmap数据拷贝出来，在内存上直接操作，操作完成后在拷贝到Bitmap中
            //使用：先锁定Bitmap，然后通过Pixels操作颜色对象，最后释放锁，把数据更新到Bitmap中


*/