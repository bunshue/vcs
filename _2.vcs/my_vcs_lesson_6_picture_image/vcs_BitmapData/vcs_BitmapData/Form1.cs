using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //BitmapData
using System.Runtime.InteropServices;   //for Marshal
using System.Diagnostics;   //for Stopwatch

namespace vcs_BitmapData
{
    public partial class Form1 : Form
    {
        string filename = "c:\\______test_files\\doraemon.jpg";
        //string filename = "c:\\______test_files\\pic_256X100.bmp";

        Stopwatch sw = new Stopwatch();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox1.Image = Image.FromFile(filename);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            sw.Reset();
            sw.Start();

            int i;
            Bitmap bmp = new Bitmap(filename);

            int W = bmp.Width;
            int H = bmp.Height;

            //獲取圖像的BitmapData對像
            Rectangle rect = new Rectangle(0, 0, W, H);
            BitmapData bmpData = bmp.LockBits(rect, ImageLockMode.ReadWrite, bmp.PixelFormat);   // Lock the bits.
            //BitmapData bmpData = bmp.LockBits(rect, ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb); //指明PixelFormat

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
            bmp.UnlockBits(bmpData);        // Unlock the bits.

            pictureBox1.Image = bmp;
            sw.Stop();
            richTextBox1.Text += "耗時 : " + string.Format("{0,10}", sw.ElapsedMilliseconds.ToString()) + "\tmsec\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            sw.Reset();
            sw.Start();

            int i;
            int j;
            Bitmap bmp = new Bitmap(filename);

            int W = bmp.Width;
            int H = bmp.Height;

            //獲取圖像的BitmapData對像
            Rectangle rect = new Rectangle(0, 0, W, H);
            BitmapData bmpData = bmp.LockBits(rect, ImageLockMode.ReadWrite, bmp.PixelFormat);   // Lock the bits.
            //BitmapData bmpData = bmp.LockBits(rect, ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb); //指明PixelFormat

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

                bmp.UnlockBits(bmpData);        // Unlock the bits.

                pictureBox1.Image = bmp;
                sw.Stop();
                richTextBox1.Text += "耗時 : " + string.Format("{0,10}", sw.ElapsedMilliseconds.ToString()) + "\tmsec\n";
            }
            //毫無疑問，採用這種方式是最快的，所以在實際工程中都是採用指針的方式來訪問圖像像素的。
        }
    }
}

