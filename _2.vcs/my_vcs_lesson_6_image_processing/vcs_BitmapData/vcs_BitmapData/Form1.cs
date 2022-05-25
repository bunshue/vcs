using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for BitmapData, ImageLockMode, PixelFormat
using System.Runtime.InteropServices;   //for Marshal
using System.Diagnostics;   //for Stopwatch
using System.Threading.Tasks;   //for Parallel

/*
//使用C#的BitmapData編程實例

日期：2017/1/4 14:59:43      編輯：關於C#

最近要轉開發平台，正研究C#。C#好是好，不過處理圖片時一個像素一個像素的操作像素不是一般的慢。其實Delphi也一樣，但好在Delphi的Bitmap類提供了ScanLines，可以一行一行的讀圖，效率比較高。C#應該也有類似的東東。經過一番搜索，終於發現了BitmapData類。

先看個例子，這是對一張位圖的每個像素按FF取補，然後輸出到一個新圖（代碼有點啰嗦，不過應該可以說明問題了）。
*/


namespace vcs_BitmapData
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\__pic\_anime\doraemon1.jpg";
        //string filename = @"C:\______test_files\pic_256X100.bmp";
        //string filename = @"C:\______test_files\__pic\global.c.gif";   //超大圖, 要很久
        //string filename = @"C:\______test_files\elephant.jpg";

        Stopwatch sw = new Stopwatch();

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

            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox1.Size = new Size(640, 480);

        }

        private void bt_restore_Click(object sender, EventArgs e)
        {
            Restore_Picture();
        }

        //各種影像處理速度比較 ST
        private void button0_Click(object sender, EventArgs e)
        {
            //各種影像處理速度比較
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            var bmp = new Bitmap(filename);
            pictureBox1.Image = bmp;
            var sw = new Stopwatch();
            richTextBox1.Text += "各種影像處理速度比較 ST\n";
            Application.DoEvents();

            richTextBox1.Text += "方法1: 使用GetPixel、SetPixel\n";
            sw.Start();
            NegativeImage1(bmp);
            sw.Stop();
            pictureBox1.Refresh();
            richTextBox1.Text += "耗時 : " + string.Format("{0,10}", sw.ElapsedMilliseconds.ToString()) + "\tmsec\n";
            Application.DoEvents();

            richTextBox1.Text += "方法2: Method in consideration of the arrangement\n";
            sw.Reset();
            sw.Start();
            NegativeImage2(bmp);
            sw.Stop();
            pictureBox1.Refresh();
            richTextBox1.Text += "耗時 : " + string.Format("{0,10}", sw.ElapsedMilliseconds.ToString()) + "\tmsec\n";
            Application.DoEvents();

            richTextBox1.Text += "方法3: Mershal ReadByte、WriteByte\n";
            sw.Reset();
            sw.Start();
            NegativeImage3(bmp);
            sw.Stop();
            pictureBox1.Refresh();
            richTextBox1.Text += "耗時 : " + string.Format("{0,10}", sw.ElapsedMilliseconds.ToString()) + "\tmsec\n";
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
        }

        /// <summary>
        /// Set up the brightness value with GetPixel、SetPixel
        /// </summary>
        /// <param name="bmp"></param>
        private void NegativeImage1(Bitmap bmp)
        {
            var W = bmp.Width;
            var H = bmp.Height;
            Color col;
            int r, g, b;
            for (int y = 0; y < H; y++)
            {
                for (int x = 0; x < W; x++)
                {
                    // Obtaining brightness value
                    col = bmp.GetPixel(x, y);
                    r = col.R;
                    g = col.G;
                    b = col.B;
                    // color reversal
                    col = Color.FromArgb(255 - r, 255 - g, 255 - b);
                    // set up brightness value
                    bmp.SetPixel(x, y, col);
                }
            }
        }

        /// <summary>
        /// Obtain the image data at Lock Bits, Unlock Bits with pointer and process the data in sequence 
        /// </summary>
        /// <param name="bmp"></param>
        private void NegativeImage2(Bitmap bmp)
        {
            var W = bmp.Width;
            var H = bmp.Height;
            // Lock Bitmap
            var bmpData = bmp.LockBits(
            new Rectangle(0, 0, W, H),
            ImageLockMode.ReadWrite,
            bmp.PixelFormat
            );
            // Obtain Bytes of memory width
            var stride = Math.Abs(bmpData.Stride);
            // Arrange image data for saving
            var data = new byte[stride * bmpData.Height];
            // Copy Bitmap data
            Marshal.Copy(bmpData.Scan0, data, 0, stride * bmpData.Height);
            byte r, g, b;
            int lineIndex = 0;
            for (int y = 0; y < H; y++)
            {
                for (int x = 0; x < W * 3; x += 3)
                {
                    // Obtain the brightness value
                    r = data[lineIndex + x + 2];
                    g = data[lineIndex + x + 1];
                    b = data[lineIndex + x]; ;
                    // Set up the brightness value
                    data[lineIndex + x + 2] = (byte)(255 - r);
                    data[lineIndex + x + 1] = (byte)(255 - g);
                    data[lineIndex + x] = (byte)(255 - b);
                }
                lineIndex += stride;
            }
            // Copy the arrangement as Bitmap data
            Marshal.Copy(data, 0, bmpData.Scan0, stride * bmpData.Height);
            // Unlock
            bmp.UnlockBits(bmpData);
        }

        /// <summary>
        /// How to obtain brightness value with ReadByte, WriteByte in Marshal class
        /// </summary>
        /// <param name="bmp"></param>
        private void NegativeImage3(Bitmap bmp)
        {
            var W = bmp.Width;
            var H = bmp.Height;
            // Lock the Bitmap
            var bmpData = bmp.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadWrite, bmp.PixelFormat);
            // Obtain Bytes of memory width
            var stride = Math.Abs(bmpData.Stride);
            byte r, g, b;
            int lineIndex = 0;
            var ptr = bmpData.Scan0;
            for (int y = 0; y < H; y++)
            {
                for (int x = 0; x < W * 3; x += 3)
                {
                    // Obtain brightness value
                    r = Marshal.ReadByte(ptr, lineIndex + x + 2);
                    g = Marshal.ReadByte(ptr, lineIndex + x + 1);
                    b = Marshal.ReadByte(ptr, lineIndex + x);
                    // Set up brightness value
                    Marshal.WriteByte(ptr, lineIndex + x + 2, (byte)(255 - r));
                    Marshal.WriteByte(ptr, lineIndex + x + 1, (byte)(255 - g));
                    Marshal.WriteByte(ptr, lineIndex + x, (byte)(255 - b));
                }
                lineIndex += stride;
            }
            // Unlock
            bmp.UnlockBits(bmpData);
        }

        /// <summary>
        /// How to obtain brightness value by using unsafe pointer
        /// </summary>
        /// <param name="bmp"></param>
        private void NegativeImage4(Bitmap bmp)
        {
            var W = bmp.Width;
            var H = bmp.Height;
            // Bitmap Lock
            var bmpData = bmp.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadWrite, bmp.PixelFormat);
            // Obtain Bytes of memory width
            var stride = Math.Abs(bmpData.Stride);
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
            // Unlock
            bmp.UnlockBits(bmpData);
        }

        /// <summary>
        /// Parallel processing of the brightness value acquiring setup using usafe pointer
        /// </summary>
        /// <param name="bmp"></param>
        private void NegativeImage5(Bitmap bmp)
        {
            var W = bmp.Width;
            var H = bmp.Height;
            // Bitmap Lock
            var bmpData = bmp.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadWrite, bmp.PixelFormat);
            // Obtain Bytes of memory width
            var stride = Math.Abs(bmpData.Stride);
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
            // Unlock
            bmp.UnlockBits(bmpData);
        }

        /// <summary>
        /// 使用BitmapData處理
        /// </summary>
        /// <param name="bmp"></param>
        private void NegativeImage6(Bitmap bmp)
        {
            var W = bmp.Width;
            var H = bmp.Height;

            //richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";
            BitmapData bData = bmp.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);

            unsafe
            {
                byte* p = (byte*)bData.Scan0.ToPointer();
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
                bmp.UnlockBits(bData);
            }
        }
        //各種影像處理速度比較 SP

        private void button1_Click(object sender, EventArgs e)
        {
            sw.Reset();
            sw.Start();

            int i;
            Bitmap bitmap1 = new Bitmap(filename);

            int W = bitmap1.Width;
            int H = bitmap1.Height;

            //獲取圖像的BitmapData對像
            Rectangle rect = new Rectangle(0, 0, W, H);
            BitmapData bmpData = bitmap1.LockBits(rect, ImageLockMode.ReadWrite, bitmap1.PixelFormat);   // Lock the bits.
            //BitmapData bmpData = bitmap1.LockBits(rect, ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb); //指明PixelFormat

            // Get the address of the first line.
            IntPtr ptr = bmpData.Scan0;

            // Declare an array to hold the bytes of the bitmap.
            int len = bmpData.Stride * H;
            //richTextBox1.Text += "bmpData.Stride = " + bmpData.Stride.ToString() + "\n";
            //richTextBox1.Text += "len = " + len.ToString() + "\n";
            byte[] rgbValues = new byte[len];

            // Copy the RGB values into the array.
            Marshal.Copy(ptr, rgbValues, 0, len);

            /*
            for (i = 0; i < bmpData.Stride; i++)
            {
                richTextBox1.Text += rgbValues[i].ToString() + " ";
            }
            richTextBox1.Text += "\n\n\n";
            */

            ////jpg檔要加 3, bmp檔要加4
            for (i = 0; i < len; i += 3)
            {
                /*
                //只存紅
                rgbValues[i] = 0;   //每個點的B改成255
                rgbValues[i + 1] = 0;   //每個點的G改成255
                //rgbValues[i + 2] = 0;   //每個點的R改成255
                //rgbValues[i + 3] = 0;   //每個點的A改成255

                //只存綠
                rgbValues[i] = 0;   //每個點的B改成255
                //rgbValues[i + 1] = 0;   //每個點的G改成255
                rgbValues[i + 2] = 0;   //每個點的R改成255
                //rgbValues[i + 3] = 0;   //每個點的A改成255

                //只存藍
                //rgbValues[i] = 0;   //每個點的B改成255
                rgbValues[i + 1] = 0;   //每個點的G改成255
                rgbValues[i + 2] = 0;   //每個點的R改成255
                //rgbValues[i + 3] = 0;   //每個點的A改成255
                */

                //三色平均 => 灰階
                byte avg = (byte)((rgbValues[i] + rgbValues[i + 1] + rgbValues[i + 2]) / 3);
                rgbValues[i] = avg;         //每個點的B改成三色平均
                rgbValues[i + 1] = avg;     //每個點的G改成三色平均
                rgbValues[i + 2] = avg;     //每個點的R改成三色平均
                //rgbValues[i + 3] = 0;     //每個點的A改成三色平均
            }

            /*
            for (i = 0; i < bmpData.Stride; i++)
            {
                richTextBox1.Text += rgbValues[i].ToString() + " ";
            }
            richTextBox1.Text += "\n\n\n";
            */

            // Copy the RGB values back to the bitmap
            Marshal.Copy(rgbValues, 0, ptr, len);
            bitmap1.UnlockBits(bmpData);        // Unlock the bits.

            pictureBox1.Image = bitmap1;
            sw.Stop();
            richTextBox1.Text += "耗時 : " + string.Format("{0,10}", sw.ElapsedMilliseconds.ToString()) + "\tmsec\n";
            //richTextBox1.Text += "耗時 : " + sw.Elapsed.TotalSeconds.ToString("0.000") + " 秒\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            sw.Reset();
            sw.Start();

            int i;
            int j;
            Bitmap bitmap1 = new Bitmap(filename);

            int W = bitmap1.Width;
            int H = bitmap1.Height;

            //獲取圖像的BitmapData對像
            Rectangle rect = new Rectangle(0, 0, W, H);
            BitmapData bmpData = bitmap1.LockBits(rect, ImageLockMode.ReadWrite, bitmap1.PixelFormat);   // Lock the bits.
            //BitmapData bmpData = bitmap1.LockBits(rect, ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb); //指明PixelFormat

            //循環處理
            unsafe
            {
                byte* ptr = (byte*)(bmpData.Scan0);

                //richTextBox1.Text += "W = " + W.ToString() + "\n";
                for (j = 0; j < H; j++)
                {
                    for (i = 0; i < W; i++)
                    {
                        /*
                        if (j == 0)
                        {
                            //richTextBox1.Text += "[" + i.ToString() + "]" + (*ptr).ToString() + " ";
                            richTextBox1.Text += (*ptr).ToString() + " ";
                            richTextBox1.Text += (*(ptr + 1)).ToString() + " ";
                            richTextBox1.Text += (*(ptr + 2)).ToString() + " ";
                            richTextBox1.Text += (*(ptr + 3)).ToString() + " ";
                        }
                        */

                        /*
                        //只存紅
                        *(ptr + 0) = 0;   //每個點的B改成255
                        *(ptr + 1) = 0;   //每個點的G改成255
                        //*(ptr + 2) = 0;   //每個點的R改成255
                        //*(ptr + 3) = 0;   //每個點的A改成255
                        */

                        /*
                        //只存綠
                        *(ptr + 0) = 0;   //每個點的B改成255
                        //*(ptr + 1) = 0;   //每個點的G改成255
                        *(ptr + 2) = 0;   //每個點的R改成255
                        //*(ptr + 3) = 0;   //每個點的A改成255
                        */

                        /*
                        //只存藍
                        //*(ptr + 0) = 0;   //每個點的B改成255
                        *(ptr + 1) = 0;   //每個點的G改成255
                        *(ptr + 2) = 0;   //每個點的R改成255
                        //*(ptr + 3) = 0;   //每個點的A改成255
                        */

                        //三色平均 => 灰階
                        byte avg = (byte)((*(ptr + 0) + *(ptr + 1) + *(ptr + 2)) / 3);
                        *(ptr + 0) = avg;         //每個點的B改成三色平均
                        *(ptr + 1) = avg;     //每個點的G改成三色平均
                        *(ptr + 2) = avg;     //每個點的R改成三色平均
                        //*(ptr + 3) = 0;     //每個點的A改成三色平均

                        ptr += 3;   //jpg檔要加 3, bmp檔要加4
                    }
                }
                //richTextBox1.Text += "\n\n\n";

                bitmap1.UnlockBits(bmpData);        // Unlock the bits.

                pictureBox1.Image = bitmap1;
                sw.Stop();
                richTextBox1.Text += "耗時 : " + string.Format("{0,10}", sw.ElapsedMilliseconds.ToString()) + "\tmsec\n";
            }
            //毫無疑問，採用這種方式是最快的，所以在實際工程中都是採用指針的方式來訪問圖像像素的。
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            //pictureBox1.Image = bitmap1;

            int h = bitmap1.Height;
            int w = bitmap1.Width;
            Bitmap bitmap2 = new Bitmap(w, h, PixelFormat.Format24bppRgb);
            BitmapData dataIn = bitmap1.LockBits(new Rectangle(0, 0, w, h), ImageLockMode.ReadOnly, PixelFormat.Format24bppRgb);
            BitmapData dataOut = bitmap2.LockBits(new Rectangle(0, 0, w, h), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            unsafe
            {
                byte* pIn = (byte*)(dataIn.Scan0.ToPointer());
                byte* pOut = (byte*)(dataOut.Scan0.ToPointer());
                for (int y = 0; y < dataIn.Height; y++)
                {
                    for (int x = 0; x < dataIn.Width; x++)
                    {
                        pOut[0] = (byte)(255 - pIn[0]);
                        pOut[1] = (byte)(255 - pIn[1]);
                        pOut[2] = (byte)(255 - pIn[2]);
                        pIn += 3;
                        pOut += 3;
                    }
                    pIn += dataIn.Stride - dataIn.Width * 3;
                    pOut += dataOut.Stride - dataOut.Width * 3;
                }
            }
            bitmap2.UnlockBits(dataOut);
            bitmap1.UnlockBits(dataIn);

            //就是掃描每一行，然後對當前像素點的三個分量做處理

            pictureBox1.Image = bitmap2;


            /*
            C#代碼中的Stride是個什麼東東？

            查找了不少資料，現在我是這麼理解的：

            假設有一張圖片寬度為6，因為是Format24bppRgb格式(每像素3字節。在以下的討論中，除非特別說明，否則Bitmap都被認為是24位RGB)的，顯然，每一行需要6*3=18個字節存儲。對於Bitmap就是如此。但對於BitmapData，雖然BitmapData.Width還是等於Bitmap.Width，但大概是出於顯示性能的考慮，每行的實際的字節數將變成大於等於它的那個離它最近的4的整倍數，此時的實際字節數就是Stride。就此例而言，18不是4的整倍數，而比18大的離18最近的4的倍數是20，所以這個BitmapData.Stride = 20。顯然，當寬度本身就是4的倍數時，BitmapData.Stride = Bitmap.Width * 3。
            */

            /*
            畫個圖可能更好理解。R、G、B 分別代表3個原色分量字節，BGR就表示一個像素。為了看起來方便我在每個像素之間插了個空格，實際上是沒有的。X表示補足4的倍數而自動插入的字節。為了符合人類的閱讀習慣我分行了，其實在計算機內存中應該看成連續的一大段。

            Scan0

            ---------Stride-----------------

            ---------Width-------------　 　 注：Width是圖片（BGR作為一個單位）寬度

            BGR BGR BGR BGR BGR BGR XX

            BGR BGR BGR BGR BGR BGR XX
            .
            .
            .

            現在應該很好理解了。首先用 BitmapData.Scan0找到第0個像素的第0個分量的地址。這個地址指向的是個byte類型，所以當時定義為byte* pIn。

            行掃描時，在當前指針位置（不妨看成當前像素的第0個顏色分量）連續取出三個值（3個原色分量。注意，0 1 2代表的次序是B G R。在取指針指向的值時，貌似p[n]和p += n再取p[0]是等價的），然後下移3個位置（pIn += 3，看成指到下一個像素的第0個顏色分量）。做過Bitmap.Width次操作後，就到達了Bitmap.Width * 3的位置，應該要跳過圖中標記為X的字節了（共有Stride - Width * 3個字節），代碼中就是 pIn += dataIn.Stride - dataIn.Width * 3;

            跳過以後指針就到達下行的第0個像素了。按照此算法,一共需要做Bitmap.Height次行掃描（代碼就是 for (int y = 0; y < dataIn.Height; y++)）。

            另外，因為使用了unsafe，所以編譯的時候需要設置“允許不安全的代碼”。
            */



        }

        private void button4_Click(object sender, EventArgs e)
        {
            //將byte數組轉換為8bit灰度圖像
            //將byte數組轉換為8bit灰度圖像
            byte[] bytes = new byte[10000];
            int k = 0;

            for (int i = 0; i < 100; i++)
            {
                for (int j = 0; j < 100; j++)
                {
                    bytes[k++] = (byte)(i + j);
                }
            }

            Bitmap bitmap1 = ToGrayBitmap(bytes, 100, 100);
            pictureBox1.Image = bitmap1;
            //bitmap1.Save(@"aaaaa.png", ImageFormat.Png);
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
            //// 申請目標位圖的變量，並將其內存區域鎖定
            Bitmap bitmap1 = new Bitmap(width, height, PixelFormat.Format8bppIndexed);
            BitmapData bmpData = bitmap1.LockBits(new Rectangle(0, 0, width, height),
            ImageLockMode.WriteOnly, PixelFormat.Format8bppIndexed);

            //// 獲取圖像參數
            int stride = bmpData.Stride;　 // 掃描線的寬度
            int offset = stride - width;　 // 顯示寬度與掃描線寬度的間隙
            IntPtr iptr = bmpData.Scan0;　 // 獲取bmpData的內存起始位置
            int scanBytes = stride * height;　　 // 用stride寬度，表示這是 內存區域的大小

            //// 下面把原始的顯示大小字節數組轉換為內存中實際存放的字節數組
            int posScan = 0, posReal = 0;　　 // 分別設置兩個位置指針，指向 源數組和目標數組
            byte[] pixelValues = new byte[scanBytes];　 //為目標數組分配內 存

            for (int x = 0; x < height; x++)
            {
                //// 下面的循環節是模擬行掃描
                for (int y = 0; y < width; y++)
                {
                    pixelValues[posScan++] = rawValues[posReal++];
                }
                posScan += offset;　 //行掃描結束，要將目標位置指針移過 那段“間隙”
            }

            //// 用Marshal的Copy方法，將剛才得到的內存字節數組復制到 BitmapData中
            System.Runtime.InteropServices.Marshal.Copy(pixelValues, 0, iptr, scanBytes);
            bitmap1.UnlockBits(bmpData);　 // 解鎖內存區域

            //修改過調色板 ST
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
            bitmap1.Palette = tempPalette;
            //修改過調色板 SP

            return bitmap1;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //使用SetPixel轉灰階

            Restore_Picture();

            sw.Reset();
            sw.Start();

            Use_SetPixel_Code();

            sw.Stop();
            richTextBox1.Text += "耗時 : " + string.Format("{0,10}", sw.ElapsedMilliseconds.ToString()) + "\tmsec\n";

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

        void Restore_Picture()
        {
            pictureBox1.Image = Image.FromFile(filename);
            Application.DoEvents();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //灰階圖片處理1_Bitmap類

            //從pictureBox取得Bitmap
            Bitmap bitmap1 = (Bitmap)pictureBox1.Image;

            //提取像素法
            //使用的是GDI+中的Bitmap.GetPixel和Bitmap.SetPixel方法。

            if (bitmap1 != null)
            {
                Bitmap newbitmap = bitmap1.Clone() as Bitmap;
                Color pixel;
                int ret;
                for (int x = 0; x < newbitmap.Width; x++)
                {
                    for (int y = 0; y < newbitmap.Height; y++)
                    {
                        pixel = newbitmap.GetPixel(x, y);
                        ret = (int)(pixel.R * 0.299 + pixel.G * 0.587 + pixel.B * 0.114);
                        newbitmap.SetPixel(x, y, Color.FromArgb(ret, ret, ret));
                    }
                }
                pictureBox1.Image = newbitmap.Clone() as Image;
            }


        }

        private void button8_Click(object sender, EventArgs e)
        {
            //灰階圖片處理2_BitmapData類
            //灰階圖片處理2_BitmapData類

            //從pictureBox取得Bitmap
            Bitmap bitmap1 = (Bitmap)pictureBox1.Image;


            //內存法

            //內存法是把圖像數據直接復制到內存中，這樣程序的運行速度就能大大提高了。

            if (bitmap1 != null)
            {
                Bitmap newbitmap = bitmap1.Clone() as Bitmap;
                Rectangle rect = new Rectangle(0, 0, newbitmap.Width, newbitmap.Height);
                BitmapData bmpdata = newbitmap.LockBits(rect, ImageLockMode.ReadWrite, newbitmap.PixelFormat);
                IntPtr ptr = bmpdata.Scan0;

                int bytes = newbitmap.Width * newbitmap.Height * 3;
                byte[] rgbvalues = new byte[bytes];

                Marshal.Copy(ptr, rgbvalues, 0, bytes);

                double colortemp = 0;
                for (int i = 0; i < rgbvalues.Length; i += 3)
                {
                    colortemp = rgbvalues[i + 2] * 0.299 + rgbvalues[i + 1] * 0.587 + rgbvalues[i] * 0.114;
                    rgbvalues[i] = rgbvalues[i + 1] = rgbvalues[i + 2] = (byte)colortemp;
                }

                Marshal.Copy(rgbvalues, 0, ptr, bytes);

                newbitmap.UnlockBits(bmpdata);
                pictureBox1.Image = newbitmap.Clone() as Image;
            }

        }

        private void button9_Click(object sender, EventArgs e)
        {
            //灰階圖片處理1_Bitmap類
            int Height = this.pictureBox1.Image.Height;
            int Width = this.pictureBox1.Image.Width;
            Bitmap bitmap = new Bitmap(Width, Height);
            Bitmap MyBitmap = (Bitmap)this.pictureBox1.Image;
            Color pixel;
            for (int x = 0; x < Width; x++)
                for (int y = 0; y < Height; y++)
                {
                    pixel = MyBitmap.GetPixel(x, y);
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
                    bitmap.SetPixel(x, y, Color.FromArgb(Result, Result, Result));
                }
            this.pictureBox1.Image = bitmap;
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

        }


    }
}
