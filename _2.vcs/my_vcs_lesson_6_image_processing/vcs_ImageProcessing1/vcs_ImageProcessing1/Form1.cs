/*
//圖片檔案 => Image => MemoryStream(ms) => 拜列
//拜列 => MemoryStream(ms) => Image => 圖片檔案
// bmp/png 資料長度 4*W*H + 檔頭54拜
// jpg     資料長度 3*W*H + 檔頭54拜

//圖片 拜列 MemoryStream Bitmap轉換
//圖片檔案 => Image => MemoryStream(ms) => 拜列
//拜列 => MemoryStream(ms) => Image => 圖片檔案
// bmp/png 資料長度 4*W*H + 檔頭54拜
// jpg     資料長度 3*W*H + 檔頭54拜
*/

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

namespace vcs_ImageProcessing1
{
    public partial class Form1 : Form
    {
        string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\doraemon1.jpg";
        //string filename = @"D:\_git\vcs\_1.data\______test_files1\pic_256X100.bmp";
        //string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_map_city/global.c.gif";   //超大圖, 要很久
        //string filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";

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
            dx = 200 + 10;
            dy = 60 + 10;

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

            pictureBox1.Size = new Size(1000, 900);
            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt_reset.Location = new Point(pictureBox1.Location.X + pictureBox1.Size.Width - bt_reset.Size.Width, pictureBox1.Location.Y);

            richTextBox1.Size = new Size(300, 900);
            richTextBox1.Location = new Point(x_st + dx * 7, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1820, 960);
            this.Text = "vcs_ImageProcessing1";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_reset_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = Image.FromFile(filename);
            Application.DoEvents();
        }

        //各種影像處理速度比較 ST
        private void button0_Click(object sender, EventArgs e)
        {
            button0.BackColor = Color.Red;
            Application.DoEvents();

            Stopwatch sw = new Stopwatch();

            richTextBox1.Text += "各種影像處理速度比較 ST\n";
            Application.DoEvents();

            //string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\doraemon1.jpg";
            //string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_image_processing\pic6_children2.png";

            richTextBox1.Text += "方法1: 像素法\n";
            sw.Reset();
            sw.Start();
            //像素法
            Bitmap bmp1 = image_process_pixel1(filename);
            sw.Stop();
            long elapsed = sw.ElapsedMilliseconds;
            richTextBox1.Text += "耗時 : " + string.Format("{0,10}", elapsed.ToString()) + "\tmsec\n";
            Application.DoEvents();

            richTextBox1.Text += "方法2: 內存法\n";
            sw.Reset();
            sw.Start();
            //內存法
            Bitmap bmp2 = image_process_memory1(filename);
            sw.Stop();
            elapsed = sw.ElapsedMilliseconds;
            richTextBox1.Text += "耗時 : " + string.Format("{0,10}", elapsed.ToString()) + "\tmsec\n";
            Application.DoEvents();

            richTextBox1.Text += "方法3: 指針法\n";
            sw.Reset();
            sw.Start();
            //指針法1
            Bitmap bmp3 = image_process_pointer1(filename);
            sw.Stop();
            elapsed = sw.ElapsedMilliseconds;
            richTextBox1.Text += "耗時 : " + string.Format("{0,10}", elapsed.ToString()) + "\tmsec\n";
            Application.DoEvents();

            richTextBox1.Text += "各種影像處理速度比較 SP\n\n";

            button0.BackColor = SystemColors.ControlLight;
        }
        //各種影像處理速度比較 SP

        private void button1_Click(object sender, EventArgs e)
        {
            //灰階圖片處理1_Bitmap類
            //提取像素法
            //使用的是GDI+中的Bitmap.GetPixel和Bitmap.SetPixel方法。

            richTextBox1.Text += "像素法\n";

            string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\doraemon1.jpg";
            Bitmap bmp = image_process_pixel1(filename);
            pictureBox1.Image = bmp;
        }

        Bitmap image_process_pixel1(string filename)
        {
            Bitmap bmp = new Bitmap(filename);
            int W = bmp.Width;
            int H = bmp.Height;

            Color pixel;
            byte r = 0;
            byte g = 0;
            byte b = 0;
            byte gray = 0;
            for (int x = 0; x < W; x++)
            {
                for (int y = 0; y < H; y++)
                {
                    //取值
                    pixel = bmp.GetPixel(x, y);//提取像素值
                    r = pixel.R;
                    g = pixel.G;
                    b = pixel.B;

                    //灰階
                    gray = (byte)(r * 0.299 + g * 0.587 + b * 0.114);
                    bmp.SetPixel(x, y, Color.FromArgb(gray, gray, gray));//設定像素值
                }
            }
            return bmp;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "內存法\n";
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\doraemon1.jpg";
            Bitmap bmp = image_process_memory1(filename);
            pictureBox1.Image = bmp;
        }

        Bitmap image_process_memory1(string filename)
        {
            //內存法建立灰階圖
            //Marshal.Copy, 將 BitmapData 複製到 byte[] Array 一維陣列, 複製記憶體區塊

            Bitmap bitmap1 = new Bitmap(filename);
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            Bitmap bitmap2 = new Bitmap(W, H);

            //將Bitmap鎖定到系統記憶體中,獲得BitmapData
            //綁定bitmap1和bmpData1
            //指定像素格式轉為24比特
            BitmapData bmpData1 = bitmap1.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);//指明PixelFormat
            //綁定bitmap2和bmpData2
            BitmapData bmpData2 = bitmap2.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);//指明PixelFormat

            //將Bitmap物件的資訊存放到byte陣列中
            //建立 byte[] Array 一維陣列
            var stride1 = bmpData1.Stride;//取得記憶體寬度, 影像寬度W*一點拜數 可4除
            int byte_data_len1 = stride1 * H;// 用stride寬度，表示這是 內存區域的大小
            byte[] byte_data1 = new byte[byte_data_len1];

            //建立 byte[] Array 一維陣列
            var stride2 = bmpData2.Stride;//取得記憶體寬度, 影像寬度W*一點拜數 可4除
            int byte_data_len2 = stride2 * H;// 用stride寬度，表示這是 內存區域的大小
            byte[] byte_data2 = new byte[byte_data_len2];

            //複製BGR資訊到byte陣列
            //拷貝出來 bmpData1 => byte_data1 圖片轉陣列
            Marshal.Copy(bmpData1.Scan0, byte_data1, 0, byte_data_len1);//複製記憶體區塊
            //拷貝出來 bmpData2 => byte_data2 圖片轉陣列
            Marshal.Copy(bmpData2.Scan0, byte_data2, 0, byte_data_len2);//複製記憶體區塊

            //做處理, 例如 灰階, Y=0.299*R+0.114*G+0.587B,Y為亮度
            byte r = 0;
            byte g = 0;
            byte b = 0;
            byte gray = 0;
            for (int y = 0; y < H; y++)
            {
                for (int x = 0; x < W * 3; x += 3)
                {
                    //取值
                    r = byte_data1[stride1 * y + x + 2];
                    g = byte_data1[stride1 * y + x + 1];
                    b = byte_data1[stride1 * y + x];

                    //灰階
                    gray = (byte)(r * 0.299 + g * 0.587 + b * 0.114);
                    byte_data2[stride1 * y + x + 2] = gray;
                    byte_data2[stride1 * y + x + 1] = gray;
                    byte_data2[stride1 * y + x] = gray;
                }
            }

            // 拷貝回去 byte_data1 => bmpData1 陣列轉圖片
            Marshal.Copy(byte_data1, 0, bmpData1.Scan0, byte_data_len1);//複製記憶體區塊
            // 拷貝回去 byte_data2 => bmpData2 陣列轉圖片
            Marshal.Copy(byte_data2, 0, bmpData2.Scan0, byte_data_len2);//複製記憶體區塊

            //解除綁定bitmap1和bmpData1
            bitmap1.UnlockBits(bmpData1);
            //解除綁定bitmap2和bmpData2
            bitmap2.UnlockBits(bmpData2);

            return bitmap2;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "指針法3\n";
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\doraemon1.jpg";
            Bitmap bmp = image_process_pointer1(filename);
            pictureBox1.Image = bmp;
        }

        //指針法, 毫無疑問，指針法是最快的，所以在實際工程中都是採用指針的方式來訪問圖像像素的。
        Bitmap image_process_pointer1(string filename)
        {
            Bitmap bmp = new Bitmap(filename);
            int W = bmp.Width;
            int H = bmp.Height;

            //綁定bmp和bmpData
            //指定像素格式轉為24比特
            BitmapData bmpData = bmp.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);//指明PixelFormat
            var stride = bmpData.Stride;//取得記憶體寬度, 影像寬度W*一點拜數 可4除

            unsafe
            {
                byte* ptr = (byte*)bmpData.Scan0;
                byte* pLine = ptr;
                int offset = stride - W * 3;//記憶體寬度-影像寬度W*一點拜數, 空白空間
                byte r;
                byte g;
                byte b;
                byte gray;
                for (int y = 0; y < H; y++)
                {
                    for (int x = 0; x < W; x++)
                    {
                        //取值
                        r = ptr[2];
                        g = ptr[1];
                        b = ptr[0];

                        //灰階
                        gray = (byte)(r * 0.299 + g * 0.587 + b * 0.114);
                        ptr[2] = gray;
                        ptr[1] = gray;
                        ptr[0] = gray;

                        ptr += 3;//指針移到下一個像素
                    }
                    ptr += offset;//指針加上填充的空白空間
                }
            }
            //解除綁定bmp和bmpData
            bmp.UnlockBits(bmpData);
            return bmp;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //Marshal.Copy 2 偽色彩

            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\fakecolor.jpg";    //偽色彩處理

            //彩色轉灰階

            Bitmap bmp1 = (Bitmap)Bitmap.FromFile(filename1);	//Bitmap.FromFile出來的是Image格式
            int W = bmp1.Width;
            int H = bmp1.Height;

            //SetPixel 彩色轉灰階
            Color pixel;
            byte r = 0;
            byte g = 0;
            byte b = 0;
            byte gray = 0;
            for (int y = 0; y < H; y++)
            {
                for (int x = 0; x < W; x++)
                {
                    //取值
                    pixel = bmp1.GetPixel(x, y);//提取像素值
                    r = pixel.R;
                    g = pixel.G;
                    b = pixel.B;

                    //灰階
                    gray = (byte)(r * 0.299 + g * 0.587 + b * 0.114);
                    bmp1.SetPixel(x, y, Color.FromArgb(255, gray, gray, gray));//設定像素值
                }
            }

            Bitmap bmp2 = gcTrans(bmp1, true, 255 / 10);
            pictureBox1.Image = bmp2;

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
            Bitmap bmp1 = (Bitmap)pictureBox1.Image;
            bmp2 = gcTrans(bmp1, true, 5);
            pictureBox2.Image = bmp2;
            */
            /*
            Bitmap bmp1 = (Bitmap)Bitmap.FromFile(filename3);	//Bitmap.FromFile出來的是Image格式
            Bitmap bmp2 = gcTrans(bmp1, true, 255 / 10);
            pictureBox20.Image = bmp2;
            */
        }

        //偽彩色圖像處理 ST
        /// <param name="bmp">傳入的灰度圖像</param>
        /// <param name="method">使用何種方法，false強度分層法,true灰度級-彩色變換法</param>
        /// <param name="seg">強度分層中的分層數</param>
        /// <returns>返回偽彩色圖像</returns>
        private Bitmap gcTrans(Bitmap bmp, bool method, byte seg)
        {
            if (bmp != null)
            {
                //取出原本的像素格式 bmp.PixelFormat
                if (PixelFormat.Format24bppRgb == bmp.PixelFormat)
                {
                    int W = bmp.Width;
                    int H = bmp.Height;

                    //綁定bmp和bmpData
                    //指定像素格式轉為24比特
                    BitmapData bmpData = bmp.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);//指明PixelFormat
                    var stride = bmpData.Stride;//取得記憶體寬度, 影像寬度W*一點拜數 可4除

                    //建立 byte[] Array 一維陣列
                    int bytes = W * H * 3;
                    byte[] grayValues = new byte[bytes];

                    //拷貝出來 bmpData => byte_data 圖片轉陣列
                    Marshal.Copy(bmpData.Scan0, grayValues, 0, bytes);//複製記憶體區塊

                    //解除綁定bmp和bmpData
                    bmp.UnlockBits(bmpData);

                    byte[] byte_data = new byte[bytes];
                    //清零
                    Array.Clear(byte_data, 0, bytes);
                    byte tempB;

                    if (method == false)
                    {
                        //強度分層法
                        for (int i = 0; i < bytes; i += 3)
                        {
                            byte ser = (byte)(256 / seg);
                            tempB = (byte)(grayValues[i] / ser);
                            //分配任意一種顏色
                            byte_data[i + 1] = (byte)(tempB * ser);
                            byte_data[i] = (byte)((seg - 1 - tempB) * ser);
                            byte_data[i + 2] = 0;
                        }
                    }
                    else
                    {
                        //灰度級-彩色變換法
                        for (int i = 0; i < bytes; i += 3)
                        {
                            if (grayValues[i] < 64)
                            {
                                byte_data[i + 2] = 0;
                                byte_data[i + 1] = (byte)(4 * grayValues[i]);
                                byte_data[i] = 255;
                            }
                            else if (grayValues[i] < 128)
                            {
                                byte_data[i + 2] = 0;
                                byte_data[i + 1] = 255;
                                byte_data[i] = (byte)(-4 * grayValues[i] + 2 * 255);
                            }
                            else if (grayValues[i] < 192)
                            {
                                byte_data[i + 2] = (byte)(4 * grayValues[i] - 2 * 255);
                                byte_data[i + 1] = 255;
                                byte_data[i] = 0;
                            }
                            else
                            {
                                byte_data[i + 2] = 255;
                                byte_data[i + 1] = (byte)(-4 * grayValues[i] + 4 * 255);
                                byte_data[i] = 0;
                            }
                        }
                    }
                    bmp = new Bitmap(W, H, PixelFormat.Format24bppRgb);//指明PixelFormat

                    //綁定bmp和bmpData
                    //取出原本的像素格式 bmp.PixelFormat
                    bmpData = bmp.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadWrite, bmp.PixelFormat);

                    //ptr = bmpData.Scan0;

                    // 拷貝回去 byte_data => bmpData 陣列轉圖片
                    Marshal.Copy(byte_data, 0, bmpData.Scan0, bytes);//複製記憶體區塊

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

        private void button5_Click(object sender, EventArgs e)
        {
            //Marshal.Copy()
            //將 BitmapData 複製到 byte[] Array 陣列

            Bitmap bmp = new Bitmap(@"D:/_git/vcs/_1.data/______test_files1/test_ReadAllBytes.bmp");
            int W = bmp.Width;
            int H = bmp.Height;

            int dataIndex = 0;

            //綁定bmp和bmpData
            BitmapData bmpData = bmp.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);//指明PixelFormat
            var stride = bmpData.Stride;//取得記憶體寬度, 影像寬度W*一點拜數 可4除

            //一個一個byte複製
            dataIndex = 0;

            //指針法

            //建立 byte[] Array 一維陣列
            byte[] data = new byte[W * H * 3];
            unsafe
            {
                byte* p = (byte*)bmpData.Scan0.ToPointer();
                for (int y = 0; y < H; y++)
                {
                    for (int x = 0; x < W; x++)
                    {
                        data[dataIndex++] = p[0];
                        data[dataIndex++] = p[1];
                        data[dataIndex++] = p[2];
                        p += 3;
                    }
                }
            }

            //建立 byte[] Array 一維陣列
            byte[] datab = new byte[W * H * 3];
            //拷貝出來 bmpData => byte_data 圖片轉陣列
            Marshal.Copy(bmpData.Scan0, datab, 0, datab.Length);//複製記憶體區塊

            //解除綁定bmp和bmpData
            bmp.UnlockBits(bmpData);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //MemoryStream 1
            richTextBox1.Text += "使用byte[]數據，生成Bitmap\n";

            //使用byte[]數據，生成Bitmap

            int W = 512;
            int H = 512;

            //建立 byte[] Array 一維陣列
            int byte_data_len = W * H;
            byte[] byte_data = new byte[byte_data_len];

            int i;
            int j;
            for (j = 0; j < H; j++)
            {
                for (i = 0; i < W; i++)
                {
                    byte_data[j * H + i] = (byte)((i + j) % 256);
                }
            }

            //指定8位格式，即256色
            Bitmap bmp = new Bitmap(W, H, PixelFormat.Format8bppIndexed);

            //將該位圖存入內存中
            MemoryStream ms = new MemoryStream();
            bmp.Save(ms, ImageFormat.Bmp);//Image 轉 MemoryStream(ms), bmp格式
            ms.Flush();

            //最終生成的位圖數據大小
            //int bmpDataSize = ((W * 8 + 31) / 32 * 4) * H;
            int bmpDataSize = 512 * 512;
            //數據部分相對文件開始偏移，具體可以參考位圖文件格式

            //最終生成的位圖數據，以及大小，高度沒有變，寬度需要調整
            //建立 byte[] Array 一維陣列
            byte[] byte_data_new = new byte[bmpDataSize];

            ms.Write(byte_data_new, 0, bmpDataSize);//拜列 轉 MemoryStream(ms)
            ms.Flush();

            //將內存中的位圖寫入Bitmap對象
            bmp = new Bitmap(ms);
            pictureBox1.Image = bmp;
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //MemoryStream 2 圖片 轉 拜列
            richTextBox1.Text += "圖片 轉 拜列\n";

            string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\doraemon1.jpg";
            //string filename = @"D:\_git\vcs\_1.data\______test_files1\pic_256X10.bmp";
            Image image = Image.FromFile(filename);//檔案 轉 Image

            //方法一
            MemoryStream ms = new MemoryStream();
            Bitmap bmp = new Bitmap(image);
            bmp.Save(ms, ImageFormat.Bmp);//Image 轉 MemoryStream(ms), bmp格式, 將圖像以指定的格式存入緩存內存流

            int byte_data_len = (int)ms.Length;
            richTextBox1.Text += "取得 MemoryStream 長度 : " + byte_data_len.ToString() + "\t多了檔頭54拜\n";

            //建立 byte[] Array 一維陣列
            byte[] byte_data = new byte[byte_data_len];

            ms.Position = 0;//設置留的初始位置
            ms.Read(byte_data, 0, byte_data_len);

            /*
            //方法二
            MemoryStream ms = new MemoryStream();
            image.Save(ms, image.RawFormat);
            Byte[] byte_data = ms.ToArray();//MemoryStream(ms) 轉 拜列
            */

            /*
            //方法三
            Image image = new Bitmap(filename);
            MemoryStream ms = new MemoryStream();
            image.Save(ms, ImageFormat.Bmp);//Image 轉 MemoryStream(ms), bmp格式

            int byte_data_len = (int)ms.Length;
            richTextBox1.Text += "取得 MemoryStream 長度 : " + byte_data_len.ToString() + "\t多了檔頭54拜\n";
            byte[] byte_data = ms.GetBuffer();//MemoryStream(ms) 轉 拜列
            */

            var cc = ms.ToArray();
            richTextBox1.Text += "len = " + cc.Length.ToString() + "\n";

            /*
            //全部資料以HEX表示出來
            StringBuilder sb = new StringBuilder();
            foreach (byte b in ms.ToArray())
            {
                sb.AppendFormat("{0:X2}", b);
            }
            string all_data = sb.ToString();
            richTextBox1.Text += all_data + "\n";
            */

            // bmp/png 資料長度 4*256*10 + 檔頭54 = 10294 拜
            // jpg     資料長度 3*256*10 + 檔頭54 =  7734 拜

            //對 byte_data 做處理, 反相
            int i;
            for (i = 54; i < byte_data.Length; i++)
            {
                if ((i % 4) == 2)//B
                    byte_data[i] = (byte)(255 - byte_data[i]);
                else if ((i % 4) == 3)//G
                    byte_data[i] = (byte)(255 - byte_data[i]);
                else if ((i % 4) == 0)//R
                    byte_data[i] = (byte)(255 - byte_data[i]);
            }
            //拜列 轉 Image

            MemoryStream ms2 = new MemoryStream();
            ms2.Write(byte_data, 0, byte_data.Length);//拜列 轉 MemoryStream(ms)
            ms2.Flush();

            //MemoryStream 轉 Image
            Image image2 = Image.FromStream(ms2);
            image2.Save("tmp_test.bmp");//Image 轉 檔案
            pictureBox1.Image = image2;

            //ms.Close();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //圖片 Bitmap MemoryStream 拜列 轉換

            //從圖片
            string filename = @"D:\_git\vcs\_1.data\______test_files1\pic_256X10.bmp";
            richTextBox1.Text += "圖片檔案 轉 Bitmap\n";
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式

            /*
            //從Bitmap
            Bitmap bitmap1 = new Bitmap(100, 100);//建立空白 Bitmap
            //對此Bitmap畫圖
            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.Pink);
            */
            pictureBox1.Image = bitmap1;

            richTextBox1.Text += "Bitmap 轉 MemoryStream(ms), bmp格式\n";
            MemoryStream ms = new MemoryStream();
            bitmap1.Save(ms, ImageFormat.Bmp);//Image 轉 MemoryStream(ms), bmp格式

            richTextBox1.Text += "MemoryStream(ms) 轉 拜列\n";
            Byte[] byte_data = ms.ToArray();//MemoryStream(ms) 轉 拜列
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        private void button10_Click(object sender, EventArgs e)
        {
        }

        private void button11_Click(object sender, EventArgs e)
        {
        }

        private void button12_Click(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {
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
            //測試

            //string filename = @"D:\_git\vcs\_1.data\______test_files1\pic_256X100.bmp";
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_image_processing\pic6_children2.png";

            Bitmap bmp = new Bitmap(filename);
            int W = bmp.Width;
            int H = bmp.Height;

            int PixelCount = W * H;

            // get bmp bitmap pixel format size
            //取出原本的像素格式 bmp.PixelFormat
            int Depth = Bitmap.GetPixelFormatSize(bmp.PixelFormat);

            // Check if bpp (Bits Per Pixel) is 8, 24, or 32
            if (Depth != 8 && Depth != 24 && Depth != 32)
            {
                throw new ArgumentException("Only 8, 24 and 32 bpp images are supported.");
            }

            //取出原本的像素格式 bmp.PixelFormat
            richTextBox1.Text += "PixelFormat = " + bmp.PixelFormat.ToString() + "\n";

            if (bmp.PixelFormat == PixelFormat.Format32bppRgb)
                richTextBox1.Text += "位元深度\t32\n";
            else if (bmp.PixelFormat == PixelFormat.Format24bppRgb)
                richTextBox1.Text += "位元深度\t24\n";
            else if (bmp.PixelFormat == PixelFormat.Format8bppIndexed)
                richTextBox1.Text += "位元深度\t8\n";
            else
                richTextBox1.Text += "位元深度\tunknown, PixelFormat = " + bmp.PixelFormat.ToString() + "\n";


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
            richTextBox1.Text += "data_offset = " + data_offset.ToString() + "\n";
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//------------------------------------------------------------

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個




/*
IntPtr ptr = bmpData.Scan0;　 // 獲取bmpData的內存起始位置
// Get the address of the first line.
//IntPtr ptr = bmpData.Scan0; //得到首地址
//獲取位圖中第一個像素數據的地址  
//IntPtr data.Scan0 = data.Scan0;
// Get the address of the first line.
//IntPtr ptr = bmpData.Scan0;
//點陣圖中第一個畫素資料的地址。它也可以看成是點陣圖中的第一個掃描行
IntPtr srcPtr = bmpData1.Scan0;
IntPtr dstPtr = bmpData2.Scan0;

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
*/
/*
            //内存法
            //定义一个类LockBitmap，通过把Bitmap数据拷贝出来，在内存上直接操作，操作完成后在拷贝到Bitmap中
            //使用：先锁定Bitmap，然后通过Pixels操作颜色对象，最后释放锁，把数据更新到Bitmap中

            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);  //使用Image.FromFile創建圖形對象 same
            Bitmap bitmap1 = new Bitmap(filename);

 
             //解除綁定bitmap1和bmpData   same  // 解鎖內存區域
            bitmap1.UnlockBits(bmpData);　 

            //編譯時要選用/unsafe選項

            //// 下面的代碼是為了修改生成位圖的索引表，從偽彩修改為灰度  
            using (Bitmap tempBmp = new Bitmap(1, 1, PixelFormat.Format8bppIndexed))
            {
            }
            for (int i = 0; i < 256; i++)
            {
            }

            // 下面的代碼是為了修改生成位圖的索引表，從偽彩修改為灰度
            using (Bitmap tempBmp = new Bitmap(1, 1, PixelFormat.Format8bppIndexed))
            {
            }
            for (i = 0; i < 256; i++)
            {
            }

            BitmapData bmpData = bmp.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadWrite, PixelFormat.Format8bppIndexed);//指明PixelFormat, 8位元
            BitmapData bmpData = bmp.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);//指明PixelFormat, 24位元

Bitmap bmp = new Bitmap(W, H, PixelFormat.Format1bppIndexed);
Bitmap bmp = new Bitmap(W, H, PixelFormat.Format8bppIndexed);//指定8位格式，即256色

            //綁定bmp和bmpData
            BitmapData bmpData = bmp.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadWrite, bmp.PixelFormat);

            // 拷貝回去 byte_data => bmpData 陣列轉圖片
            Marshal.Copy(buf, 0, dt.Scan0, buf.Length);//複製記憶體區塊

            //解除綁定bitmap1和bmpData
            bitmap2.UnlockBits(dt);
 各種影像處理速度比較
 * 
 * 
 * 
*/


/*

 * Bitmap bm = BytesToImage((byte[])reader.GetValue(6));


        // Convert a byte array into an image.
        private Bitmap BytesToImage(byte[] bytes)
        {
            using (MemoryStream image_stream = new MemoryStream(bytes))
            {
                Bitmap bm = new Bitmap(image_stream);
                return bm;
            }
        }


                MemoryStream image_stream = new MemoryStream(wc.DownloadData(url));
                return Image.FromStream(image_stream);


            string imgURL = @"https://www.google.com.tw/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png";
            MemoryStream ms = GetResponse(imgURL, cookie);
            File.WriteAllBytes("aaaaaaa.jpg", ms.ToArray());


            string imgURL = domain + imgBaseURL + fileName[0] + "?.&uf=ssr&zoom=2";
            MemoryStream ms = GetResponse(imgURL, cookie);
            File.WriteAllBytes(string.Format(@"Download\{0}.jpg", fileName[1]), ms.ToArray());


            Image image = barcode.Encode(TYPE.CODE128B, Code);
            using (MemoryStream ms = new MemoryStream())
            {
                image.Save(ms, ImageFormat.Jpeg);//Image 轉 MemoryStream(ms), jpg格式

                image.Save("lion.jpg", ImageFormat.Jpeg);

                pictureBox1.Image = image;

                //Response.ClearContent();
                //Response.ContentType = "image/png";
                //Response.BinaryWrite(ms.ToArray());
            }


            Image img = barcode.Encode(TYPE.CODE128B, Code);
            using (MemoryStream ms = new MemoryStream())
            {
                img.Save(ms, ImageFormat.Jpeg);//Image 轉 MemoryStream(ms), jpg格式

                img.Save("lion.jpg", ImageFormat.Jpeg);
 
                //Response.ClearContent();
                //Response.ContentType = "image/png";
                //Response.BinaryWrite(ms.ToArray());
            }


            Bitmap bitmap = null;
            //宣告 QRCode Reader 物件
            ZXing.IBarcodeReader reader = new ZXing.BarcodeReader();

            //讀取要解碼的圖片
            FileStream fs = new FileStream(filename, FileMode.Open);
            Byte[] data = new Byte[fs.Length];
            // 把檔案讀取到位元組陣列
            fs.Read(data, 0, data.Length);
            fs.Close();

            // 實例化一個記憶體資料流 MemoryStream，將位元組陣列放入
            MemoryStream ms = new MemoryStream(data);
            // 將記憶體資料流的資料放到 BitMap的物件中
            bitmap = (Bitmap)Image.FromStream(ms);

            //pictureBox2.Image = bitmap;       //將圖片顯示於 PictureBox 中

*/

/*
long elapsed = sw.ElapsedMilliseconds;
richTextBox1.Text += "耗時 : " + string.Format("{0,10}", elapsed.ToString()) + "\tmsec\n";
richTextBox1.Text += "耗時 : " + (elapsed / 1000).ToString() + "." + (elapsed % 1000).ToString("D3") + " 秒\n";
*/

//使用原本的像素格式
//BitmapData bmpData = bmp.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadWrite, bmp.PixelFormat);

/*
ImageLockMode 三種模式, 都使用 ReadWrite
ImageLockMode.ReadWrite
ImageLockMode.ReadOnly
ImageLockMode.ReadWrite
*/

// 其中BitmapData類的Stride屬性爲每行像素所佔的字節。
// int offset = stride - W * 3;
// ptr += offset;//指針加上填充的空白空間
