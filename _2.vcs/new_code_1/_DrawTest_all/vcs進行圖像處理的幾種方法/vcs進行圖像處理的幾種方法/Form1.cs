using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //BitmapData

namespace vcs進行圖像處理的幾種方法
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = "c:\\______test_files\\picture1.jpg";
            //利用 BitmapData 檢查圖片是否為空白
            //檢查圖片是否擷取成功
            bool NotNULL = false;
            Bitmap b;
            using (b = (Bitmap)Bitmap.FromFile(filename))
            {
                richTextBox1.Text += "W = " + b.Width.ToString() + ", H = " + b.Height.ToString() + "\n";
                BitmapData bData = b.LockBits(new Rectangle(0, 0, b.Width, b.Height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
                unsafe
                {
                    byte* p = (byte*)bData.Scan0.ToPointer();
                    for (int y = 0; y < b.Height; y++)
                    {
                        for (int x = 0; x < b.Width; x++)
                        {
                            if ((p[0] != 255 && p[0] != 0) || (p[1] != 255 && p[1] != 0) || (p[2] != 255 && p[2] != 0))
                            {
                                NotNULL = true;
                                break;
                            }
                            p += 3;
                        }
                        if (NotNULL) break;
                    }
                    b.UnlockBits(bData);
                }
            }
            richTextBox1.Text += NotNULL ? "不是空白" : "空白" + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string filename = "c:\\______test_files\\picture1.jpg";
            // Create a Bitmap object from an image file.

            Bitmap myBitmap = new Bitmap(filename);
            pictureBox1.Image = myBitmap;

            // Get the color of a pixel within myBitmap.

            Color pixelColor = myBitmap.GetPixel(10, 10);

            // Fill a rectangle with pixelColor.

            SolidBrush pixelBrush = new SolidBrush(pixelColor);

            Graphics g = pictureBox2.CreateGraphics();
            g.FillRectangle(pixelBrush, 0, 0, 100, 100);
            //最慢速

        }

        private void button3_Click(object sender, EventArgs e)
        {
            string filename = "c:\\______test_files\\picture1.jpg";
             // Create a new bitmap.

            Bitmap bmp = new Bitmap(filename);

            // Lock the bitmap’s bits.

            Rectangle rect = new Rectangle(0, 0, bmp.Width, bmp.Height);

            System.Drawing.Imaging.BitmapData bmpData =

            bmp.LockBits(rect, System.Drawing.Imaging.ImageLockMode.ReadWrite,

            bmp.PixelFormat);

            // Get the address of the first line.

            IntPtr ptr = bmpData.Scan0;

            // Declare an array to hold the bytes of the bitmap.

            int bytes = bmpData.Stride * bmp.Height;

            byte[] rgbValues = new byte[bytes];

            // Copy the RGB values into the array.

            System.Runtime.InteropServices.Marshal.Copy(ptr, rgbValues, 0, bytes);

            // Set every red value to 255.

            for (int counter = 0; counter < rgbValues.Length; counter += 3)

                rgbValues[counter] = 255;

            // Copy the RGB values back to the bitmap

            System.Runtime.InteropServices.Marshal.Copy(rgbValues, 0, ptr, bytes);

            // Unlock the bits.

            bmp.UnlockBits(bmpData);

            // Draw the modified image.

            Graphics g = pictureBox2.CreateGraphics();
            //g.FillRectangle(pixelBrush, 0, 0, 100, 100);
            g.DrawImage(bmp, 0, 150);
            //e.Graphics.DrawImage(bmp, 0, 150);

        }

        private void button4_Click(object sender, EventArgs e)
        {
            string filename = "c:\\______test_files\\picture1.jpg";


            //創建圖像

            Bitmap image = new Bitmap(filename);

            //獲取圖像的BitmapData對像

            BitmapData data = image.LockBits(new Rectangle(0, 0, image.Width, image.Height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);

            //循環處理

            unsafe
            {

                byte* ptr = (byte*)(data.Scan0);

                for (int i = 0; i < data.Height; i++)
                {

                    for (int j = 0; j < data.Width; j++)
                    {

                        // write the logic implementation here

                        ptr += 3;

                    }

                    ptr += data.Stride - data.Width * 3;

                }

            }

            //毫無疑問，採用這種方式是最快的，所以在實際工程中都是採用指針的方式來訪問圖像像素的。


        }
    }
}
