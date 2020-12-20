using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for PixelFormat
using System.Runtime.InteropServices;   //for Marshal
using System.IO;    //for Path

namespace vcs_PictureGray
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 850;
            y_st = 12;
            dx = 190;
            dy = 50;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //將圖片轉為 Sepia 效果
            // Display the image converted to sepia tone.
            string filename = @"C:\______test_files\picture1.jpg";
            pictureBox1.Image = Bitmap.FromFile(filename);
            pictureBox2.Image = ToSepiaTone(pictureBox1.Image);
        }

        // Convert an image to sepia tone.
        private Bitmap ToSepiaTone(Image image)
        {
            // Make the ColorMatrix.
            ColorMatrix cm = new ColorMatrix(new float[][]
            {
                new float[] {0.393f, 0.349f, 0.272f, 0, 0},
                new float[] {0.769f, 0.686f, 0.534f, 0, 0},
                new float[] {0.189f, 0.168f, 0.131f, 0, 0},
                new float[] { 0, 0, 0, 1, 0},
                new float[] { 0, 0, 0, 0, 1}
            });
            //ColorMatrix cm = new ColorMatrix(new float[][]
            //{
            //    new float[] {0.300f, 0.066f, 0.300f, 0, 0},
            //    new float[] {0.500f, 0.350f, 0.600f, 0, 0},
            //    new float[] {0.100f, 0.000f, 0.200f, 0, 0},
            //    new float[] { 0, 0, 0, 1, 0},
            //    new float[] { 0, 0, 0, 0, 1}
            //});
            ImageAttributes attributes = new ImageAttributes();
            attributes.SetColorMatrix(cm);

            // Draw the image onto the new bitmap while applying the new ColorMatrix.
            Point[] points =
            {
                new Point(0, 0),
                new Point(image.Width - 1, 0),
                new Point(0, image.Height - 1),
            };
            Rectangle rect = new Rectangle(0, 0, image.Width, image.Height);

            // Make the result bitmap.
            Bitmap bm = new Bitmap(image.Width, image.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.DrawImage(image, points, rect, GraphicsUnit.Pixel, attributes);
            }

            // Return the result.
            return bm;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //SetPixel 彩色轉灰階
            string filename = @"C:\______test_files\picture1.jpg";
            color_to_gray_1(filename);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //Marshal 彩色轉灰階
            string filename = @"C:\______test_files\picture1.jpg";
            color_to_gray_2(filename);
        }

        void color_to_gray_1(string filename)
        {
            richTextBox1.Text += "SetPixel 彩色轉灰階\n";

            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox2.SizeMode = PictureBoxSizeMode.Zoom;

            Bitmap bmp0 = new Bitmap(filename);
            Bitmap bmp = new Bitmap(filename);
            pictureBox1.Image = bmp0;

            int xx;
            int yy;

            for (yy = 0; yy < bmp.Height; yy++)
            {
                for (xx = 0; xx < bmp.Width; xx++)
                {
                    byte rrr = bmp.GetPixel(xx, yy).R;
                    byte ggg = bmp.GetPixel(xx, yy).G;
                    byte bbb = bmp.GetPixel(xx, yy).B;

                    int Gray = (rrr * 299 + ggg * 587 + bbb * 114 + 500) / 1000;
                    Color zz = Color.FromArgb(255, Gray, Gray, Gray);

                    bmp.SetPixel(xx, yy, zz);
                }
            }
            pictureBox2.Image = bmp;
        }

        void color_to_gray_2(string filename)
        {
            richTextBox1.Text += "Marshal 彩色轉灰階\n";

            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox2.SizeMode = PictureBoxSizeMode.Zoom;

            //int data_offset = 0;
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
            System.Runtime.InteropServices.Marshal.Copy(ptr, rgbValues, 0, len);

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
            for (int counter = 0; counter < (rgbValues.Length - 20); counter += 3)
            {
                byte bbb = rgbValues[counter];      //Blue
                byte ggg = rgbValues[counter + 1];  //Green
                byte rrr = rgbValues[counter + 2];  //Red

                int Gray = (rrr * 299 + ggg * 587 + bbb * 114 + 500) / 1000;

                rgbValues[counter] = (byte)Gray;
                rgbValues[counter + 1] = (byte)Gray;
                rgbValues[counter + 2] = (byte)Gray;
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
            System.Runtime.InteropServices.Marshal.Copy(rgbValues, 0, ptr, len);

            // Unlock the bits.
            bmp.UnlockBits(bmpData);

            // Draw the modified image.
            pictureBox2.Image = bmp;
        }

        #region 灰度處理
        private void button3_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";
            Bitmap bitmap1 = new Bitmap(filename);
            pictureBox1.Image = bitmap1;
            Bitmap bitmap2 = 灰度處理(bitmap1);
            pictureBox2.Image = bitmap2;
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
        #endregion

        #region 將圖片改為灰階 Grayscale Average
        private void button4_Click(object sender, EventArgs e)
        {
            //將圖片改為灰階 Grayscale
            string filename = @"C:\______test_files\bear.jpg";
            ConvertFile(filename, false);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //將圖片改為灰階 Average
            string filename = @"C:\______test_files\bear.jpg";
            ConvertFile(filename, true);
        }

        // Convert a file.
        private void ConvertFile(string filename, bool use_average)
        {
            richTextBox1.Text += "filename old = " + filename + "\n";

            string d_name = Path.GetDirectoryName(filename);
            string f_name = Path.GetFileNameWithoutExtension(filename);
            string ext_name = Path.GetExtension(filename);

            string filename2;

            if (use_average == true)
                filename2 = d_name + "\\" + f_name + "_average" + ext_name;
            else
                filename2 = d_name + "\\" + f_name + "_grayscale" + ext_name;

            richTextBox1.Text += "filename new = " + filename2 + "\n";

            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox2.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.Image = Bitmap.FromFile(filename);

            // Convert to grayscale.
            //Bitmap bmp = new Bitmap(pictureBox1.Image);       same
            Bitmap bmp = LoadBitmapWithoutLocking(filename);

            // Convert the image.
            ConvertBitmapToGrayscale(bmp, use_average);

            // Show the converted bitmap
            pictureBox2.Image = bmp;

            // Save the file.
            SaveBitmapUsingExtension(bmp, filename2);
        }

        // Convert the Bitmap to grayscale.
        private void ConvertBitmapToGrayscale(Bitmap bm, bool use_average)
        {
            // Make a Bitmap24 object.
            Bitmap32 bm32 = new Bitmap32(bm);

            // Lock the bitmap.
            bm32.LockBitmap();

            // Process the pixels.
            for (int x = 0; x < bm.Width; x++)
            {
                for (int y = 0; y < bm.Height; y++)
                {
                    byte r = bm32.GetRed(x, y);
                    byte g = bm32.GetGreen(x, y);
                    byte b = bm32.GetBlue(x, y);
                    byte gray = (use_average ?
                        (byte)((r + g + b) / 3) :
                        (byte)(0.3 * r + 0.5 * g + 0.2 * b));
                    bm32.SetPixel(x, y, gray, gray, gray, 255);
                }
            }

            // Unlock the bitmap.
            bm32.UnlockBitmap();
        }

        // Save the file with the appropriate format.
        // Throw a NotSupportedException if the file
        // has an unknown extension.
        public void SaveBitmapUsingExtension(Bitmap bm, string filename)
        {
            string extension = Path.GetExtension(filename);
            switch (extension.ToLower())
            {
                case ".bmp":
                    bm.Save(filename, ImageFormat.Bmp);
                    break;
                case ".exif":
                    bm.Save(filename, ImageFormat.Exif);
                    break;
                case ".gif":
                    bm.Save(filename, ImageFormat.Gif);
                    break;
                case ".jpg":
                case ".jpeg":
                    bm.Save(filename, ImageFormat.Jpeg);
                    break;
                case ".png":
                    bm.Save(filename, ImageFormat.Png);
                    break;
                case ".tif":
                case ".tiff":
                    bm.Save(filename, ImageFormat.Tiff);
                    break;
                default:
                    throw new NotSupportedException(
                        "Unknown file extension " + extension);
            }
        }

        // Load a Bitmap without locking its file.
        // The caller must dispose of the Bitmap if desired.
        private Bitmap LoadBitmapWithoutLocking(string filename)
        {
            Bitmap result;
            using (Bitmap bm = new Bitmap(filename))
            {
                result = new Bitmap(bm.Width, bm.Height);
                using (Graphics gr = Graphics.FromImage(result))
                {
                    gr.DrawImage(bm, 0, 0);
                }
            }

            return result;
        }






        #endregion





        private void bt_clear_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = null;
            pictureBox2.Image = null;
            richTextBox1.Clear();
        }


    }
}
