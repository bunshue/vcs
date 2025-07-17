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
using System.Threading.Tasks;   //for Parallel

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
            pictureBox1.Size = new Size(640, 480);
            pictureBox2.Location = new Point(x_st + dx * 3, y_st + dy * 0 + 480 + 10);
            pictureBox2.Size = new Size(640, 480);

            richTextBox1.Size = new Size(500, 900);
            richTextBox1.Location = new Point(x_st + dx * 10, y_st + dy * 0);

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

            richTextBox1.Text += "方法5: parallel processing of usafe pointer\n";
            sw.Reset();
            sw.Start();
            NegativeImage5(bmp);
            sw.Stop();
            pictureBox1.Refresh();
            richTextBox1.Text += "NegativeImage5: " + string.Format("{0,10}", sw.ElapsedMilliseconds.ToString()) + "\tmsec\n";
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
        /// Parallel processing of the brightness value acquiring setup using usafe pointer
        /// </summary>
        /// <param name="bmp"></param>
        private void NegativeImage5(Bitmap bmp)
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
                Parallel.For(0, H, y =>
                {
                    // The first pointer of the line
                    byte* pLine = ptr + y * stride;
                    for (int x = 0; x < W; x++)
                    {
                        // Obtain brightness value
                        byte r = pLine[2];
                        byte g = pLine[1];
                        byte b = pLine[0];
                        // Set up brightness value
                        pLine[2] = (byte)(255 - r);
                        pLine[1] = (byte)(255 - g);
                        pLine[0] = (byte)(255 - b);
                        // Move to the next pixel
                        pLine += 3;
                    }
                }
                );
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

            //循環處理
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
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //將byte數組轉換為8bit灰度圖像
            //將byte數組轉換為8bit灰度圖像
            byte[] byte_data_len = new byte[10000];//建立 byte[] Array 一維陣列
            int k = 0;

            for (int i = 0; i < 100; i++)
            {
                for (int j = 0; j < 100; j++)
                {
                    byte_data_len[k++] = (byte)(i + j);
                }
            }

            Bitmap bitmap1 = ToGrayBitmap(byte_data_len, 100, 100);
            pictureBox1.Image = bitmap1;
        }

        //C#中將byte數組轉換為8bit灰度圖像
        /*
        byte數組存放的是圖像每個像素的灰度值，byte類型正好是從0~255，存放8bit灰度圖像的時候，一個 數組元素就是一個像素的灰度值。僅有這個數組還不足以恢復出原來的圖像，還必須事先知道圖像的長、 寬值；

        創建Bitmap類的時候必須指定PixelFormat為Format8bppIndexed，這樣才最符合圖像本身的特性；

        Bitmap類雖然提供了GetPixel()、SetPixel()這樣的方法，但我們絕對不能用這兩個方法來進行大規 模的像素讀寫，因為它們的性能實在很囧；

        托管代碼中，能不用unsafe就盡量不用。在.Net 2.0中已經提供了BitmapData類及其LockBits()、 UnLockBits()操作，能夠安全地進行內存讀寫；

        圖像的width和它存儲時的stride是不一樣的。位圖的掃描線寬度一定是4的倍數，因此圖像在內存中 的大小並不是它的顯示大小；

        Format8bppIndexed類型的PixelFormat是索引格式，其調色板並不是灰度的而是偽彩，因此需要我們 對其加以修改。
        */

        /// <summary>
        /// 將一個字節數組轉換為8bit灰度位圖
        /// </summary>
        /// <param name="rawValues">顯示字節數組</param>
        /// <param name="width">圖像寬度</param>
        /// <param name="height">圖像高度</param>
        /// <returns>位圖</returns>
        public static Bitmap ToGrayBitmap(byte[] rawValues, int width, int height)
        {
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
            byte[] byte_data = new byte[byte_data_len];//建立 byte[] Array 一維陣列

            for (int x = 0; x < height; x++)
            {
                // 下面的循環節是模擬行掃描
                for (int y = 0; y < width; y++)
                {
                    byte_data[posScan++] = rawValues[posReal++];
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

            return bitmap1;
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
            //LockBitmap內存法
            richTextBox1.Text += "内存法\t";
            string filename = @"C:\_git\vcs\_1.data\______test_files1\__pic\_anime\doraemon1.jpg";
            Application.DoEvents();

            //内存法
            //定义一个类LockBitmap，通过把Bitmap数据拷贝出来，在内存上直接操作，操作完成后在拷贝到Bitmap中

            //使用：先锁定Bitmap，然后通过Pixels操作颜色对象，最后释放锁，把数据更新到Bitmap中

            Bitmap bmp = (Bitmap)Image.FromFile(filename);
            LockBitmap lockBitmap = new LockBitmap(bmp);
            lockBitmap.LockBits();  //锁定Bitmap，通过Pixel访问颜色

            Color compareClr = Color.FromArgb(255, 255, 255, 255);
            for (int y = 0; y < lockBitmap.Height; y++)
            {
                for (int x = 0; x < lockBitmap.Width; x++)
                {
                    if (lockBitmap.GetPixel(x, y) == compareClr)    //获取颜色
                    {
                        lockBitmap.SetPixel(x, y, Color.Red);
                    }
                }
            }

            lockBitmap.UnlockBits();    //从内存解锁Bitmap

            pictureBox1.Image = bmp;
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //LockBitmap指針法

            richTextBox1.Text += "指針法\t";
            string filename = @"C:\_git\vcs\_1.data\______test_files1\__pic\_anime\doraemon1.jpg";
            Application.DoEvents();

            //指針法
            Bitmap bmp = (Bitmap)Image.FromFile(filename);

            PointBitmap lockBitmap = new PointBitmap(bmp);
            lockBitmap.LockBits();  //锁定Bitmap，通过Pixel访问颜色

            Color compareClr = Color.FromArgb(255, 255, 255, 255);
            for (int y = 0; y < lockBitmap.Height; y++)
            {
                for (int x = 0; x < lockBitmap.Width; x++)
                {
                    if (lockBitmap.GetPixel(x, y) == compareClr)    //获取颜色
                    {
                        lockBitmap.SetPixel(x, y, Color.Red);
                    }
                }
            }

            lockBitmap.UnlockBits();    //从内存解锁Bitmap

            pictureBox1.Image = bmp;
        }

        private void button13_Click(object sender, EventArgs e)
        {
        }

        private void button14_Click(object sender, EventArgs e)
        {
        }

        private void button15_Click(object sender, EventArgs e)
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

        private void button16_Click(object sender, EventArgs e)
        {
        }

        private void button17_Click(object sender, EventArgs e)
        {
        }

        private void button18_Click(object sender, EventArgs e)
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

        private void button19_Click(object sender, EventArgs e)
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

        private void button20_Click(object sender, EventArgs e)
        {
        }

        private void button21_Click(object sender, EventArgs e)
        {
        }

        private void button22_Click(object sender, EventArgs e)
        {
        }

        //圖片與二進制互轉

        /// <summary>
        /// Image轉二進制
        /// </summary>
        /// <param name="img">圖片</param>
        /// <returns>轉換得到的二進制</returns>
        public byte[] GetByteByImage(System.Drawing.Image img)
        {
            try
            {
                byte[] bt = null;
                if (!img.Equals(null))
                {
                    using (MemoryStream mostream = new MemoryStream())
                    {
                        Bitmap bmp = new Bitmap(img);
                        bmp.Save(mostream, ImageFormat.Bmp);//將圖像以指定的格式存入緩存內存流
                        bt = new byte[mostream.Length];
                        mostream.Position = 0;//設置留的初始位置
                        mostream.Read(bt, 0, Convert.ToInt32(bt.Length));
                    }
                }
                return bt;
            }
            catch
            {
                return null;
            }
        }

        /// <summary>
        /// 字節流轉換成圖片
        /// </summary>
        /// <param name="byt">要轉換的字節流</param>
        /// <returns>轉換得到的Image對象</returns>
        public static Image BytToImg(byte[] byt)
        {
            MemoryStream ms = new MemoryStream(byt);
            Image img = Image.FromStream(ms);
            return img;
        }

        private void button23_Click(object sender, EventArgs e)
        {
            //圖片與二進制互轉

            //函數在上



            //TBD

        }

        private void button24_Click(object sender, EventArgs e)
        {
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

        private void button25_Click(object sender, EventArgs e)
        {
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

        private void button26_Click(object sender, EventArgs e)
        {
            //將圖片放入拜列

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
        }

        private void button27_Click(object sender, EventArgs e)
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
        Bitmap bmp = null;
        IntPtr Iptr = IntPtr.Zero;
        BitmapData bmpData = null;

        public byte[] byte_data { get; set; }
        public int Depth { get; private set; }
        public int Width { get; private set; }
        public int Height { get; private set; }

        public LockBitmap(Bitmap bmp)
        {
            this.bmp = bmp;
        }

        /// <summary>
        /// Lock bitmap data
        /// </summary>
        public void LockBits()
        {
            try
            {
                // Get width and height of bitmap
                Width = bmp.Width;
                Height = bmp.Height;

                // get total locked pixels count
                int PixelCount = Width * Height;

                // get bmp bitmap pixel format size
                Depth = System.Drawing.Bitmap.GetPixelFormatSize(bmp.PixelFormat);

                // Check if bpp (Bits Per Pixel) is 8, 24, or 32
                if (Depth != 8 && Depth != 24 && Depth != 32)
                {
                    throw new ArgumentException("Only 8, 24 and 32 bpp images are supported.");
                }

                // Lock bitmap and return bitmap data
                bmpData = bmp.LockBits(new Rectangle(0, 0, Width, Height), ImageLockMode.ReadWrite, bmp.PixelFormat);

                // create byte array to copy pixel values
                int step = Depth / 8;
                byte_data = new byte[PixelCount * step];

                // Copy data from pointer to array
                Marshal.Copy(bmpData.Scan0, byte_data, 0, byte_data.Length);//複製記憶體區塊
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
                Marshal.Copy(byte_data, 0, bmpData.Scan0, byte_data.Length);//複製記憶體區塊

                //解除綁定bmp和bmpData
                bmp.UnlockBits(bmpData);
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

            if (i > byte_data.Length - cCount)
                throw new IndexOutOfRangeException();

            if (Depth == 32) // For 32 bpp get Red, Green, Blue and Alpha
            {
                byte b = byte_data[i];
                byte g = byte_data[i + 1];
                byte r = byte_data[i + 2];
                byte a = byte_data[i + 3]; // a
                clr = Color.FromArgb(a, r, g, b);
            }
            if (Depth == 24) // For 24 bpp get Red, Green and Blue
            {
                byte b = byte_data[i];
                byte g = byte_data[i + 1];
                byte r = byte_data[i + 2];
                clr = Color.FromArgb(r, g, b);
            }
            if (Depth == 8)
            // For 8 bpp get color value (Red, Green and Blue values are the same)
            {
                byte c = byte_data[i];
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
                byte_data[i] = color.B;
                byte_data[i + 1] = color.G;
                byte_data[i + 2] = color.R;
                byte_data[i + 3] = color.A;
            }
            if (Depth == 24) // For 24 bpp set Red, Green and Blue
            {
                byte_data[i] = color.B;
                byte_data[i + 1] = color.G;
                byte_data[i + 2] = color.R;
            }
            if (Depth == 8)
            // For 8 bpp set color value (Red, Green and Blue values are the same)
            {
                byte_data[i] = color.B;
            }
        }
    }

    //指針法
    public class PointBitmap
    {
        Bitmap bmp = null;
        IntPtr Iptr = IntPtr.Zero;
        BitmapData bmpData = null;

        public int Depth { get; private set; }
        public int Width { get; private set; }
        public int Height { get; private set; }

        public PointBitmap(Bitmap bmp)
        {
            this.bmp = bmp;
        }

        public void LockBits()
        {
            try
            {
                // Get width and height of bitmap
                Width = bmp.Width;
                Height = bmp.Height;

                // get total locked pixels count
                int PixelCount = Width * Height;

                // get bmp bitmap pixel format size
                Depth = Bitmap.GetPixelFormatSize(bmp.PixelFormat);

                // Check if bpp (Bits Per Pixel) is 8, 24, or 32
                if (Depth != 8 && Depth != 24 && Depth != 32)
                {
                    throw new ArgumentException("Only 8, 24 and 32 bpp images are supported.");
                }

                // Lock bitmap and return bitmap data
                bmpData = bmp.LockBits(new Rectangle(0, 0, Width, Height), ImageLockMode.ReadWrite, bmp.PixelFormat);

                //得到首地址
                unsafe
                {
                    Iptr = bmpData.Scan0;
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
                //解除綁定bmp和bmpData
                bmp.UnlockBits(bmpData);
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
                ptr = ptr + bmpData.Stride * y;
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
                ptr = ptr + bmpData.Stride * y;
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



