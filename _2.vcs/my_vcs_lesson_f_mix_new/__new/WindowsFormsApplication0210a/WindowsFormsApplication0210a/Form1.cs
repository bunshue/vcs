using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageLockMode;
using System.Runtime.InteropServices;   //for Marshal

namespace WindowsFormsApplication0210a
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = @"..\..\pic\rgb.bmp";
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            pictureBox1.Image = bitmap1;

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string filename = @"..\..\pic\rgb.bmp";
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);  //使用Image.FromFile創建圖形對象:
            int W = bitmap1.Width;
            int H = bitmap1.Height;

            //把圖像復制到內存中:
            //獲取圖像的BitmapData對像
            Rectangle rect = new Rectangle(0, 0, W, H);	//位圖矩形

            //以可讀寫的方式鎖定全部位圖像素
            BitmapData bmpData = bitmap1.LockBits(rect, ImageLockMode.ReadWrite, bitmap1.PixelFormat);   // Lock the bits.
            //BitmapData bmpData = bitmap1.LockBits(rect, ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb); //指明PixelFormat

            // Get the address of the first line.
            IntPtr ptr = bmpData.Scan0; //得到首地址

            //int len = W * 4 * H;    //每個pixel要用4拜存資料 R G B A
            int len = Math.Abs(bmpData.Stride) * H;   //24位BMP位圖字節數 stride = W * 4, 每個pixel要用4拜存資料 R G B A

            richTextBox1.Text += "stride = " + bmpData.Stride.ToString() + "\n";
            richTextBox1.Text += "len = " + len.ToString() + "\n";

            //存bitmap資料的陣列
            byte[] rgbValues = new byte[len]; //定義位圖數組

            richTextBox1.Text += "len = " + len.ToString() + "\n";
            Marshal.Copy(ptr, rgbValues, 0, len); //復制被鎖定的位圖像素到位圖數組

            richTextBox1.Text += "len2 = " + rgbValues.Length.ToString() + "\n";
            int i;
            string result = string.Empty;
            for (i = 0; i < len; i++)
            {
                result += rgbValues[i].ToString("X2");
                if ((i % (256 * 4)) == (256 * 4 - 1))
                {
                    result += "\n";
                }
                else
                {
                    result += " ";
                }
            }
            //richTextBox1.Text += result + "\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Graphics g = this.pictureBox1.CreateGraphics();

            string filename = @"..\..\pic\rgb.bmp";
            //Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);  //使用Image.FromFile創建圖形對象 same
            Bitmap bitmap1 = new Bitmap(filename);
            int W = bitmap1.Width;
            int H = bitmap1.Height;

            g.DrawImage(bitmap1, 0, 0);

            Rectangle rect = new Rectangle(0, 0, W, H);	//位圖矩形

            //以可讀寫的方式鎖定全部位圖像素
            BitmapData bmpData = bitmap1.LockBits(rect, ImageLockMode.ReadWrite, bitmap1.PixelFormat);   // Lock the bits.
            //BitmapData bmpData = bitmap1.LockBits(rect, ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb); //指明PixelFormat

            // Get the address of the first line.
            IntPtr ptr = bmpData.Scan0; //得到首地址

            // Declare an array to hold the bytes of the bitmap.
            int len = Math.Abs(bmpData.Stride) * H;   //24位BMP位圖字節數 stride = W * 4, 每個pixel要用4拜存資料 R G B A

            richTextBox1.Text += "stride = " + bmpData.Stride.ToString() + "\n";
            richTextBox1.Text += "len = " + len.ToString() + "\n";

            //存bitmap資料的陣列
            byte[] rgbValues = new byte[len]; //定義位圖數組

            // Copy the RGB values into the array.
            Marshal.Copy(ptr, rgbValues, 0, len);

            // Set every third value to 255. A 24bpp bitmap will look red.  
            for (int counter = 2; counter < rgbValues.Length; counter += 4)
            {
                rgbValues[counter] = 255;
            }

            // Copy the RGB values back to the bitmap
            Marshal.Copy(rgbValues, 0, ptr, len);

            // Unlock the bits.
            bitmap1.UnlockBits(bmpData);

            // Draw the modified image.
            //e.Graphics.DrawImage(bitmap1, 0, 150);
            g.DrawImage(bitmap1, 0, 50);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            Graphics g = this.pictureBox1.CreateGraphics();

            string filename = @"..\..\pic\rgb.bmp";
            //Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);  //使用Image.FromFile創建圖形對象 same
            Bitmap bitmap1 = new Bitmap(filename);
            int W = bitmap1.Width;
            int H = bitmap1.Height;

            g.DrawImage(bitmap1, 0, 0);

            Rectangle rect = new Rectangle(0, 0, W, H);	//位圖矩形

            //以可讀寫的方式鎖定全部位圖像素
            BitmapData bmpData = bitmap1.LockBits(rect, ImageLockMode.ReadWrite, bitmap1.PixelFormat);   // Lock the bits.
            //BitmapData bmpData = bitmap1.LockBits(rect, ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb); //指明PixelFormat

            // Get the address of the first line.
            IntPtr ptr = bmpData.Scan0;

            // Declare an array to hold the bytes of the bitmap.
            int bytes = Math.Abs(bmpData.Stride) * H;
            byte[] rgbValues = new byte[bytes];

            // Copy the RGB values into the array.
            Marshal.Copy(ptr, rgbValues, 0, bytes);

            // Set every third value to 255. A 24bpp bitmap will look red.  
            for (int counter = 2; counter < rgbValues.Length; counter += 4)
            {
                rgbValues[counter] = 255;
            }

            // Copy the RGB values back to the bitmap
            Marshal.Copy(rgbValues, 0, ptr, bytes);

            // Unlock the bits.
            bitmap1.UnlockBits(bmpData);

            // Draw the modified image.
            //e.Graphics.DrawImage(bitmap1, 0, 150);
            g.DrawImage(bitmap1, 0, 50);

        }
    }
}

