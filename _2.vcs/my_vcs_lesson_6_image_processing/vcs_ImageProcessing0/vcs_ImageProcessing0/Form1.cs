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

/*
//使用C#的BitmapData編程實例

日期：2017/1/4 14:59:43      編輯：關於C#

最近要轉開發平台，正研究C#。C#好是好，不過處理圖片時一個像素一個像素的操作像素不是一般的慢。其實Delphi也一樣，但好在Delphi的Bitmap類提供了ScanLines，可以一行一行的讀圖，效率比較高。C#應該也有類似的東東。經過一番搜索，終於發現了BitmapData類。

先看個例子，這是對一張位圖的每個像素按FF取補，然後輸出到一個新圖（代碼有點啰嗦，不過應該可以說明問題了）。
*/


namespace vcs_ImageProcessing0
{
    public partial class Form1 : Form
    {
        string filename = @"C:\_git\vcs\_1.data\______test_files1\__pic\_anime\doraemon1.jpg";
        //string filename = @"C:\_git\vcs\_1.data\______test_files1\pic_256X100.bmp";
        //string filename = @"C:\_git\vcs\_1.data\______test_files1\__pic\global.c.gif";   //超大圖, 要很久
        //string filename = @"C:\_git\vcs\_1.data\______test_files1\elephant.jpg";

        Stopwatch sw = new Stopwatch();

        private Bitmap bitmap1;
        byte[] srcData;
        //int[] histoData;

        public struct RGB
        {
            private byte _r;
            private byte _g;
            private byte _b;

            public RGB(byte r, byte g, byte b)
            {
                this._r = r;
                this._g = g;
                this._b = b;
            }

            public byte R
            {
                get { return this._r; }
                set { this._r = value; }
            }

            public byte G
            {
                get { return this._g; }
                set { this._g = value; }
            }

            public byte B
            {
                get { return this._b; }
                set { this._b = value; }
            }

            public bool Equals(RGB rgb)
            {
                return (this.R == rgb.R) && (this.G == rgb.G) && (this.B == rgb.B);
            }
        }

        public struct YUV
        {
            private double _y;
            private double _u;
            private double _v;

            public YUV(double y, double u, double v)
            {
                this._y = y;
                this._u = u;
                this._v = v;
            }

            public double Y
            {
                get { return this._y; }
                set { this._y = value; }
            }

            public double U
            {
                get { return this._u; }
                set { this._u = value; }
            }

            public double V
            {
                get { return this._v; }
                set { this._v = value; }
            }

            public bool Equals(YUV yuv)
            {
                return (this.Y == yuv.Y) && (this.U == yuv.U) && (this.V == yuv.V);
            }
        }

        public static YUV RGBToYUV(RGB rgb)
        {
            double y = rgb.R * .299000 + rgb.G * .587000 + rgb.B * .114000;
            double u = rgb.R * -.168736 + rgb.G * -.331264 + rgb.B * .500000 + 128;
            double v = rgb.R * .500000 + rgb.G * -.418688 + rgb.B * -.081312 + 128;

            return new YUV(y, u, v);
        }

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
            pictureBox2.Location = new Point(x_st + dx * 3, y_st + dy * 0+480+10);
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

            button0.BackColor = System.Drawing.SystemColors.ControlLight;
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
            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
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
            button5.BackColor = Color.Red;
            Application.DoEvents();

            Restore_Picture();

            sw.Reset();
            sw.Start();

            Use_SetPixel_Code();

            sw.Stop();
            richTextBox1.Text += "耗時 : " + string.Format("{0,10}", sw.ElapsedMilliseconds.ToString()) + "\tmsec\n";
            button5.BackColor = System.Drawing.SystemColors.ControlLight;
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

            button7.BackColor = Color.Red;
            Application.DoEvents();

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
            button7.BackColor = System.Drawing.SystemColors.ControlLight;
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

            button9.BackColor = Color.Red;
            Application.DoEvents();

            int Height = this.pictureBox1.Image.Height;
            int Width = this.pictureBox1.Image.Width;
            Bitmap bitmap = new Bitmap(Width, Height);
            Bitmap MyBitmap = (Bitmap)this.pictureBox1.Image;
            Color pixel;
            for (int x = 0; x < Width; x++)
            {
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
            }
            this.pictureBox1.Image = bitmap;

            button9.BackColor = System.Drawing.SystemColors.ControlLight;
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //使用byte[]數據，生成Bitmap

            int W = 256;
            int H = 256;
            byte[] imagedata = new byte[W * H];

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
            Bitmap resultBitmap = new Bitmap(originalWidth, originalHeight, System.Drawing.Imaging.PixelFormat.Format8bppIndexed);
            //將該位圖存入內存中
            MemoryStream curImageStream = new MemoryStream();
            resultBitmap.Save(curImageStream, System.Drawing.Imaging.ImageFormat.Bmp);
            curImageStream.Flush();
            //由於位圖數據需要DWORD對齊（4byte倍數），計算需要補位的個數
            int curPadNum = ((originalWidth * 8 + 31) / 32 * 4) - originalWidth;
            //最終生成的位圖數據大小
            int bitmapDataSize = ((originalWidth * 8 + 31) / 32 * 4) * originalHeight;
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
            byte[] destImageData = new byte[bitmapDataSize];
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
            curImageStream.Write(destImageData, 0, bitmapDataSize);
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
            byte[] tempData = new byte[length];
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
            Benchmark.Start();
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
            Benchmark.End();
            double seconds = Benchmark.GetSeconds();
            richTextBox1.Text += "耗時 : " + string.Format("{0,10}", seconds.ToString()) + "\tsec\n";

            string filename_png = Application.StartupPath + "\\png_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".png";
            bmp.Save(filename_png);
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
            Benchmark.Start();

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
            Benchmark.End();
            double seconds = Benchmark.GetSeconds();
            richTextBox1.Text += "耗時 : " + string.Format("{0,10}", seconds.ToString()) + "\tsec\n";

            string filename_png = Application.StartupPath + "\\png_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".png";
            bmp.Save(filename_png);
            pictureBox1.Image = bmp;
        }

        private void button13_Click(object sender, EventArgs e)
        {
            button13.BackColor = Color.Red;
            Application.DoEvents();
            //量測時間 黑白
            string filename = @"C:\_git\vcs\_1.data\______test_files1\__pic\_book\2016122615573727.jpg";
            Bitmap bitmap1 = new Bitmap(filename);
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.Image = bitmap1; //顯示在 pictureBox1 圖片控制項中
            richTextBox1.Text += "W = " + bitmap1.Width.ToString() + ", H = " + bitmap1.Height.ToString() + "\n";

            richTextBox1.Text += "量測時間ST\t黑白\t約耗時 21 秒, 目前無法中斷\n";

            Application.DoEvents();

            Stopwatch stopwatch = new Stopwatch();

            int w = bitmap1.Width;
            int h = bitmap1.Height;
            int xx;
            int yy;
            Color c;

            stopwatch.Start();

            for (yy = 0; yy < h; yy++)
            {
                for (xx = 0; xx < w; xx++)
                {
                    c = bitmap1.GetPixel(xx, yy);

                    //黑白
                    bitmap1.SetPixel(xx, yy, Color.FromArgb((c.R + c.G + c.B) / 3, (c.R + c.G + c.B) / 3, (c.R + c.G + c.B) / 3));
                }
            }

            // Stop timing
            stopwatch.Stop();

            pictureBox1.Image = bitmap1; //顯示在 pictureBox1 圖片控制項中

            richTextBox1.Text += "完成, 總時間 : " + stopwatch.Elapsed.TotalSeconds.ToString() + " 秒\n";

            button13.BackColor = System.Drawing.SystemColors.ControlLight;
            Application.DoEvents();
        }

        private void button14_Click(object sender, EventArgs e)
        {
            button14.BackColor = Color.Red;
            Application.DoEvents();

            //量測時間 測光
            string filename = @"C:\_git\vcs\_1.data\______test_files1\__pic\_book\2016122615573727.jpg";
            Bitmap bitmap1 = new Bitmap(filename);
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.Image = bitmap1; //顯示在 pictureBox1 圖片控制項中
            richTextBox1.Text += "W = " + bitmap1.Width.ToString() + ", H = " + bitmap1.Height.ToString() + "\n";


            richTextBox1.Text += "量測時間ST\t測光\t約耗時 12 秒, 目前無法中斷\n";

            Application.DoEvents();


            Stopwatch stopwatch = new Stopwatch();

            int w = bitmap1.Width;
            int h = bitmap1.Height;
            int xx;
            int yy;
            Color c;
            double y_total = 0;

            stopwatch.Start();

            for (yy = 0; yy < h; yy++)
            {
                for (xx = 0; xx < w; xx++)
                {
                    c = bitmap1.GetPixel(xx, yy);

                    //測光
                    RGB pp = new RGB(c.R, c.G, c.B);
                    YUV yyy = new YUV();
                    yyy = RGBToYUV(pp);
                    y_total += yyy.Y;
                }
            }

            // Stop timing
            stopwatch.Stop();

            pictureBox1.Image = bitmap1; //顯示在 pictureBox1 圖片控制項中

            richTextBox1.Text += "亮度 : " + (y_total / (w * h)).ToString() + "\n";

            richTextBox1.Text += "完成, 總時間 : " + stopwatch.Elapsed.TotalSeconds.ToString() + " 秒\n";

            button14.BackColor = System.Drawing.SystemColors.ControlLight;
            Application.DoEvents();
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

        private void button17_Click(object sender, EventArgs e)
        {
            //BitmapData使用
            //用Marshal做影像處理, TBD

            filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            LoadBitmap(filename);


            int len = srcData.Length;
            int W = bitmap1.Width;
            int H = bitmap1.Height;

            richTextBox1.Text += "len = " + len.ToString() + "\n";
            richTextBox1.Text += "W = " + W.ToString() + "\n";
            richTextBox1.Text += "H = " + H.ToString() + "\n";
            int i;
            int j;
            for (j = 0; j < H; j++)
            {
                for (i = 0; i < W; i++)
                {
                    //richTextBox1.Text += srcData[j * H + i].ToString("X2") + " ";
                    //richTextBox1.Text += srcData[j * H + i].ToString() + " ";

                    //srcData[j * H + i] = (byte)(255 - srcData[j * H + i]);

                }
                //richTextBox1.Text += "\n";
            }

            //準備修改srcData值  並把 srcData恢復成圖片


            for (i = 0; i < 305 * 10; i++)
            {
                srcData[i] = 0;

            }

            richTextBox1.Text += "\n";
            richTextBox1.Text += "\n";
            richTextBox1.Text += "\n";


            for (i = 0; i < 150; i++)
            {
                //richTextBox1.Text += srcData[i].ToString() + " ";

            }
            richTextBox1.Text += "\n";
        }

        // load and initialize from file
        private void LoadBitmap(string filename)
        {
            // read from file
            bitmap1 = (Bitmap)Image.FromFile(filename);
            pictureBox1.Image = bitmap1;

            int W = bitmap1.Width;
            int H = bitmap1.Height;

            // read byte data
            BitmapData bmpData = bitmap1.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadWrite, PixelFormat.Format8bppIndexed);
            srcData = new byte[W * H];
            IntPtr srcPtr = bmpData.Scan0;
            Marshal.Copy(srcPtr, srcData, 0, W * H);
            // pay attention: order in byte array: height first
            bitmap1.UnlockBits(bmpData);
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
            //使用unsafe加快處理圖像速度

            string filename = @"C:\_git\vcs\_1.data\______test_files1\red.bmp";

            Bitmap bitmap1 = new Bitmap(filename);

            int W = bitmap1.Width;
            int H = bitmap1.Height;

            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";

            Rectangle rect = new Rectangle(100, 100, 20, 20);
            BitmapData data = bitmap1.LockBits(rect, ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);

            int w = data.Width;
            int h = data.Height;

            richTextBox1.Text += "w = " + w.ToString() + ", h = " + h.ToString() + "\n";

            unsafe
            {
                long r = 0;
                long g = 0;
                long b = 0;
                long pixelCount = h * w;

                byte* ptr = (byte*)(data.Scan0);

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
                    ptr += data.Stride - w * 3;
                }

                double totalRGB = (r / pixelCount + g / pixelCount + b / pixelCount) / 3;

                richTextBox1.Text += "平均 R : " + (r / pixelCount).ToString() + "\n";
                richTextBox1.Text += "平均 G : " + (g / pixelCount).ToString() + "\n";
                richTextBox1.Text += "平均 B : " + (b / pixelCount).ToString() + "\n";
                richTextBox1.Text += "平均亮度 : " + totalRGB.ToString() + "\n";
            }
        }

        private void button21_Click(object sender, EventArgs e)
        {
            //對圖片做Marshal處理1
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox2.SizeMode = PictureBoxSizeMode.Zoom;
            LockUnlockBitsExample1();
        }

        private void button22_Click(object sender, EventArgs e)
        {
            //對圖片做Marshal處理2
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox2.SizeMode = PictureBoxSizeMode.Zoom;
            LockUnlockBitsExample2();
        }

        private void LockUnlockBitsExample1()
        {
            string filename = @"C:\_git\vcs\_1.data\______test_files1\_case1\\pic3.jpg";

            int data_offset = 0;
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
            Marshal.Copy(ptr, rgbValues, 0, len);

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
            int tmp = 0;
            for (int counter = 0; counter < (rgbValues.Length - 20); counter += 3)
            {
                tmp = rgbValues[counter] + rgbValues[counter + 1] + rgbValues[counter + 2];
                tmp /= 3;
                rgbValues[counter] = (byte)tmp;
                rgbValues[counter + 1] = (byte)tmp;
                rgbValues[counter + 2] = (byte)tmp;
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
            Marshal.Copy(rgbValues, 0, ptr, len);

            // Unlock the bits.
            bmp.UnlockBits(bmpData);

            // Draw the modified image.
            pictureBox2.Image = bmp;
        }

        private void LockUnlockBitsExample2()
        {
            int data_offset = 0;
            // Create a new bitmap.
            //Bitmap bmp = new Bitmap(@"C:\_git\vcs\_1.data\______test_files1\IMG_256X32.bmp");
            Bitmap bmp0 = new Bitmap(@"C:\_git\vcs\_1.data\______test_files1\picture1.jpg");
            Bitmap bmp = new Bitmap(@"C:\_git\vcs\_1.data\______test_files1\picture1.jpg");
            pictureBox1.Image = bmp0;

            richTextBox1.Text += "W = " + bmp.Width.ToString() + ", H = " + bmp.Height.ToString() + "\n";
            richTextBox1.Text += "PixelFormat = " + bmp.PixelFormat.ToString() + "\n";

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
                richTextBox1.Text += "位元深度\tunknown, PixelFormat = " + bmp.PixelFormat.ToString() + "\n";

            // Lock the bitmap's bits.  
            Rectangle rect = new Rectangle(bmp.Width / 4, bmp.Width / 4, bmp.Width / 2, bmp.Height / 2);
            System.Drawing.Imaging.BitmapData bmpData = bmp.LockBits(rect, System.Drawing.Imaging.ImageLockMode.ReadWrite, bmp.PixelFormat);

            richTextBox1.Text += "W = " + bmpData.Width.ToString() + "\n";
            richTextBox1.Text += "H = " + bmpData.Height.ToString() + "\n";
            richTextBox1.Text += "Stride = " + bmpData.Stride.ToString() + "\n";    //圖片一橫條的拜數 即WX4(拜)
            richTextBox1.Text += "Scan0 = " + bmpData.Scan0.ToString() + "\n";

            // Get the address of the first line.
            IntPtr ptr = bmpData.Scan0;

            // Declare an array to hold the bytes of the bitmap.
            int len = Math.Abs(bmpData.Stride) * bmp.Height / 4;    //(W * 4) * H

            richTextBox1.Text += "len = " + len.ToString() + "\n";

            byte[] rgbValues = new byte[len];

            // Copy the RGB values into the array.
            Marshal.Copy(ptr, rgbValues, 0, len);

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
            int tmp = 0;
            for (int counter = 0; counter < (rgbValues.Length - data_offset); counter += data_offset)
            {
                tmp = rgbValues[counter] + rgbValues[counter + 1] + rgbValues[counter + 2];
                tmp /= 3;
                rgbValues[counter] = (byte)tmp;
                rgbValues[counter + 1] = (byte)tmp;
                rgbValues[counter + 2] = (byte)tmp;
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
            Marshal.Copy(rgbValues, 0, ptr, len);

            // Unlock the bits.
            bmp.UnlockBits(bmpData);

            // Draw the modified image.
            pictureBox2.Image = bmp;
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
                        bmp.Save(mostream, System.Drawing.Imaging.ImageFormat.Bmp);//將圖像以指定的格式存入緩存內存流
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
