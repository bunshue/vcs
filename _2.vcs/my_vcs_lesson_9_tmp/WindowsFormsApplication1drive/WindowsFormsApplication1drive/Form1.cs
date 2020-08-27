using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

using System.Threading; //for Thread
using System.Diagnostics;   //即時運算視窗
using System.Drawing.Imaging;   //for ImageLockMode

using System.Runtime.InteropServices;   //for Marshal


namespace WindowsFormsApplication1drive
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        public class Worker
        {
            /* Initializes a new instance of the ManualResetEvent class 
            * with a Boolean value indicating whether to set the initial state to signaled.
            */
            ManualResetEvent _shutdownEvent = new ManualResetEvent(false);
            ManualResetEvent _pauseEvent = new ManualResetEvent(true);
            Thread _thread;
            public Worker() { }
            public void Job()
            {
                int cnt = 0;
                while (true)
                {
                    /* 封鎖目前執行緒, 直到waitHandle收到通知, 
                    * Timeout.Infinite表示無限期等候
                    */
                    _pauseEvent.WaitOne(Timeout.Infinite);
                    /* return true if the current instance receives a signal. 
                    * If the current instance is never signaled, WaitOne never returns
                    */
                    if (_shutdownEvent.WaitOne(0))
                        break;
                    /* if (_shutdownEvent.WaitOne(Timeout.Infinite))
                    * 因為沒有收到signal, 所以會停在if()這一行, 造成cnt無法累加
                    */





                    System.Diagnostics.Debug.WriteLine("{0}", cnt++);
                }
            }
            public void Start()
            {
                _thread = new Thread(Job);
                _thread.Start();
                System.Diagnostics.Debug.WriteLine("Thread started running");
            }
            public void Pause()
            {
                /* Sets the state of the event to nonsignaled, 
                * causing threads to block.
                */
                _pauseEvent.Reset();
                System.Diagnostics.Debug.WriteLine("Thread paused");
            }

            public void Resume()
            {
                /* Sets the state of the event to signaled, 
                * allowing one or more waiting threads to proceed.
                */
                _pauseEvent.Set();
                System.Diagnostics.Debug.WriteLine("Thread resuming ");
            }
            public void Stop()
            {
                // Signal the shutdown event
                _shutdownEvent.Set();
                System.Diagnostics.Debug.WriteLine("Thread Stopped ");

                // Make sure to resume any paused threads
                _pauseEvent.Set();

                // Wait for the thread to exit
                _thread.Join();
            }
        }



        private void button2_Click(object sender, EventArgs e)
        {
            return;
            //TBD
            System.Diagnostics.Debug.WriteLine("aaaaaaaaaaaaaaa\n");
            Worker w1 = new Worker();
            w1.Start();
            Thread.Sleep(500);
            w1.Pause();
            Thread.Sleep(200);
            w1.Resume();
            Thread.Sleep(500);
            w1.Pause();
            Thread.Sleep(1000);
            w1.Resume();
            Thread.Sleep(200);
            w1.Stop();
            Console.Read();
            System.Diagnostics.Debug.WriteLine("aaaaaaaaaaaaaaa2\n");
        }

        private void button3_Click(object sender, EventArgs e)
        {
            /*
Dim sText As String = "Hello World"
' Returns "hello world".
Dim sNewText As String = StrConv(sText, VbStrConv.LowerCase)
            */
            //string str = "Hello World";
            //string str2 = String.strconv

            //LockUnlockBitsExample((PaintEventArgs)e);


        }

        private void LockUnlockBitsExample(PaintEventArgs e)
        {

            // Create a new bitmap.
            Bitmap bmp = new Bitmap("c:\\______test_files\\pattern.jpg");

            // Lock the bitmap's bits.  
            Rectangle rect = new Rectangle(0, 0, bmp.Width, bmp.Height);
            System.Drawing.Imaging.BitmapData bmpData = bmp.LockBits(rect, System.Drawing.Imaging.ImageLockMode.ReadWrite, bmp.PixelFormat);

            // Get the address of the first line.
            IntPtr ptr = bmpData.Scan0;

            // Declare an array to hold the bytes of the bitmap.
            int len = Math.Abs(bmpData.Stride) * bmp.Height;

            richTextBox1.Text += "len = " + len.ToString() + "\n";

            byte[] rgbValues = new byte[len];

            // Copy the RGB values into the array.
            System.Runtime.InteropServices.Marshal.Copy(ptr, rgbValues, 0, len);

            int i;
            for (i = 0; i < 128; i++)
            {
                richTextBox1.Text += rgbValues[i].ToString();
                if ((i % 32) == 31)
                    richTextBox1.Text += "\n";
                else
                    richTextBox1.Text += " ";

            }
            richTextBox1.Text += "\n";

            // Set every third value to 255. A 24bpp bitmap will look red.  
            for (int counter = 2; counter < rgbValues.Length; counter += 3)
                rgbValues[counter] = 255;


            for (i = 0; i < 128; i++)
            {
                richTextBox1.Text += rgbValues[i].ToString();
                if ((i % 32) == 31)
                    richTextBox1.Text += "\n";
                else
                    richTextBox1.Text += " ";

            }
            richTextBox1.Text += "\n";

            // Copy the RGB values back to the bitmap
            System.Runtime.InteropServices.Marshal.Copy(rgbValues, 0, ptr, len);

            // Unlock the bits.
            bmp.UnlockBits(bmpData);

            // Draw the modified image.
            //e.Graphics.DrawImage(bmp, 0, 150);
            e.Graphics.DrawImage(bmp, 50, 50);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            //LockUnlockBitsExample(e);

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

        private void button4_Click(object sender, EventArgs e)
        {
            /*
            Graphics g;
            g = pictureBox1.CreateGraphics();



            // Create a new bitmap.
            //Bitmap bmp = new Bitmap("c:\\______test_files\\picture1.jpg");
            Bitmap bmp = new Bitmap("c:\\______test_files\\pattern.jpg");

            g.DrawImage(bmp, 0, 0);
            pictureBox1.Image = bmp;
            */

            Bitmap bitmap1;
            Graphics g;

            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 256;
            height = 256;
            bitmap1 = new Bitmap(width, height);

            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    if (yy < 256 / 4)
                        bitmap1.SetPixel(xx, yy, Color.FromArgb(255, (xx % 256), 0, 0));
                    else if (yy < 256 / 4 * 2)
                        bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0, (xx % 256), 0));
                    else if (yy < 256 / 4 * 3)
                        bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0, 0, (xx % 256)));
                    else
                        bitmap1.SetPixel(xx, yy, Color.FromArgb(255, (xx % 256), (xx % 256), (xx % 256)));
                }
            }

            Bitmap bitmap2 = 灰度處理(bitmap1);


            //g = Graphics.FromImage(bitmap1);


            
            pictureBox1.Image = bitmap2;



        }

        private void button1_Click(object sender, EventArgs e)
        {
            Worker w1 = new Worker();
            w1.Start();
            Thread.Sleep(500);
            richTextBox1.Text += "111111\n";
                 
            w1.Pause();
            Thread.Sleep(200);
            richTextBox1.Text += "222222\n";
            w1.Resume();
            Thread.Sleep(500);
            richTextBox1.Text += "333333\n";
            w1.Pause();
            Thread.Sleep(1000);
            richTextBox1.Text += "444444\n";
            w1.Resume();
            Thread.Sleep(200);
            richTextBox1.Text += "555555\n";
            w1.Stop();

        }  






    }
}
