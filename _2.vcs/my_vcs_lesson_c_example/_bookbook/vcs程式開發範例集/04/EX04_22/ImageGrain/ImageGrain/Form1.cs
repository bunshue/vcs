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
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {

            string filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";

            Image image = System.Drawing.Image.FromFile(filename);
            Bitmap bitmap1 = new Bitmap(image);

            Rectangle rect = new Rectangle(0, 0, bitmap1.Width, bitmap1.Height);
            //將指定圖像鎖定到內存中
            System.Drawing.Imaging.BitmapData bmpData = bitmap1.LockBits(rect, System.Drawing.Imaging.ImageLockMode.ReadWrite, bitmap1.PixelFormat);

            // 獲得圖像中第一個像素數據的地址
            IntPtr ptr = bmpData.Scan0;
            int bytes = bitmap1.Width * bitmap1.Height * 3;
            byte[] rgbValues = new byte[bytes];
            // 使用RGB值為聲明的rgbValues數組賦值
            System.Runtime.InteropServices.Marshal.Copy(ptr, rgbValues, 0, bytes);
            for (int counter = 0; counter < rgbValues.Length; counter += 3)
            {
                rgbValues[counter] = 255;
            }
            // 使用RGB值為圖像的像素點著色
            System.Runtime.InteropServices.Marshal.Copy(rgbValues, 0, ptr, bytes);
            // 從內存中解鎖圖像
            bitmap1.UnlockBits(bmpData);

            this.BackgroundImage = bitmap1;
        }
    }
}
