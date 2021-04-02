using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;
using System.Drawing.Imaging;

namespace ImageGrain
{
    public partial class Form1 : Form
    {
        Bitmap myBitmap;
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            openFileDialog1.Filter = "*.jpg,*.jpeg,*.bmp|*.jpg;*.jpeg;*.bmp";
            openFileDialog1.ShowDialog();
            Image myImage = System.Drawing.Image.FromFile(openFileDialog1.FileName);
            myBitmap = new Bitmap(myImage);
            this.BackgroundImage = myBitmap;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            try
            {
                Image myImage = System.Drawing.Image.FromFile(openFileDialog1.FileName);
                myBitmap = new Bitmap(myImage);
                Rectangle rect = new Rectangle(0, 0, myBitmap.Width, myBitmap.Height);
                //將指定圖像鎖定到內存中
                System.Drawing.Imaging.BitmapData bmpData = myBitmap.LockBits(rect, System.Drawing.Imaging.ImageLockMode.ReadWrite, myBitmap.PixelFormat);
                // 獲得圖像中第一個像素數據的地址
                IntPtr ptr = bmpData.Scan0;
                int bytes = myBitmap.Width * myBitmap.Height * 3;
                byte[] rgbValues = new byte[bytes];
                // 使用RGB值為聲明的rgbValues數組賦值
                System.Runtime.InteropServices.Marshal.Copy(ptr, rgbValues, 0, bytes);
                for (int counter = 0; counter < rgbValues.Length; counter += 3)
                    rgbValues[counter] = 255;
                // 使用RGB值為圖像的像素點著色
                System.Runtime.InteropServices.Marshal.Copy(rgbValues, 0, ptr, bytes);
                // 從內存中解鎖圖像
                myBitmap.UnlockBits(bmpData);
                this.BackgroundImage = myBitmap;
            }
            catch { }
        }
    }
}