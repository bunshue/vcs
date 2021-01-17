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

namespace vcs_ImageProcessing2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom; //原圖
            pictureBox2.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox3.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox4.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox5.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox6.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox7.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox8.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox9.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox10.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox11.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox12.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox13.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox14.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox15.SizeMode = PictureBoxSizeMode.Zoom;
            //pictureBox16.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox17.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox18.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox19.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox20.SizeMode = PictureBoxSizeMode.Zoom;

            show_item_location();

            string filename = @"C:\______test_files\picture1.jpg";
            pictureBox1.Image = Bitmap.FromFile(filename);
            PictureToSepia1();  //To Sepia 方法一
            //PictureToSepia2();  //To Sepia 方法二
            PictureToGray1();
            PictureToGray2();
            PictureToGray3();
            PictureToGray4();
            PictureToGray5();
            PictureToMonochrome();
            PictureToNegative();
            PictureToMirror();
            PictureToRainbow();
            PictureToBinary();
            PictureTo8BitGrayScale();

            // Convert the image into red, green, and blue monochrome.
            pictureBox7.Image = ScaleColorComponents(pictureBox1.Image, 1, 0, 0, 1);
            pictureBox8.Image = ScaleColorComponents(pictureBox1.Image, 0, 1, 0, 1);
            pictureBox9.Image = ScaleColorComponents(pictureBox1.Image, 0, 0, 1, 1);

            //另外的方法製作單色圖片
            //show_mono_color_picture();

            //最大化螢幕
            //this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 1700;
            y_st = 12;
            dx = 190;
            dy = 50;

            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 13);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            int W = 250;
            int H = 250;
            x_st = 12;
            y_st = 50;
            dx = 270;
            dy = 300;
            pictureBox1.Size = new Size(W, H);
            pictureBox2.Size = new Size(W, H);
            pictureBox3.Size = new Size(W, H);
            pictureBox4.Size = new Size(W, H);
            pictureBox5.Size = new Size(W, H);
            pictureBox6.Size = new Size(W, H);
            pictureBox7.Size = new Size(W, H);
            pictureBox8.Size = new Size(W, H);
            pictureBox9.Size = new Size(W, H);
            pictureBox10.Size = new Size(W, H);
            pictureBox11.Size = new Size(W, H);
            pictureBox12.Size = new Size(W, H);
            pictureBox13.Size = new Size(W, H);
            pictureBox15.Size = new Size(W * 2, H);
            pictureBox17.Size = new Size(W, H);
            pictureBox18.Size = new Size(W, H);
            pictureBox19.Size = new Size(W, H);
            pictureBox20.Size = new Size(W, H);

            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox3.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox4.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            pictureBox5.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            pictureBox6.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            pictureBox7.Location = new Point(x_st + dx * 6, y_st + dy * 0);

            pictureBox8.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox9.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            pictureBox10.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            pictureBox11.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            pictureBox12.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            pictureBox13.Location = new Point(x_st + dx * 5, y_st + dy * 1);
            pictureBox14.Location = new Point(x_st + dx * 6, y_st + dy * 1);

            pictureBox15.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            //pictureBox16.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            pictureBox17.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            pictureBox18.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            pictureBox19.Location = new Point(x_st + dx * 4, y_st + dy * 2);
            pictureBox20.Location = new Point(x_st + dx * 5, y_st + dy * 2);

            label1.Location = new Point(x_st + dx * 0, y_st + dy * 0 - 25);
            label2.Location = new Point(x_st + dx * 1, y_st + dy * 0 - 25);
            label3.Location = new Point(x_st + dx * 2, y_st + dy * 0 - 25);
            label4.Location = new Point(x_st + dx * 3, y_st + dy * 0 - 25);
            label5.Location = new Point(x_st + dx * 4, y_st + dy * 0 - 25);
            label6.Location = new Point(x_st + dx * 5, y_st + dy * 0 - 25);
            label7.Location = new Point(x_st + dx * 6, y_st + dy * 0 - 25);

            label8.Location = new Point(x_st + dx * 0, y_st + dy * 1 - 25);
            label9.Location = new Point(x_st + dx * 1, y_st + dy * 1 - 25);
            label10.Location = new Point(x_st + dx * 2, y_st + dy * 1 - 25);
            label11.Location = new Point(x_st + dx * 3, y_st + dy * 1 - 25);
            label12.Location = new Point(x_st + dx * 4, y_st + dy * 1 - 25);
            label13.Location = new Point(x_st + dx * 5, y_st + dy * 1 - 25);
            label14.Location = new Point(x_st + dx * 6, y_st + dy * 1 - 25);

            label15.Location = new Point(x_st + dx * 0, y_st + dy * 2 - 25);
            label16.Location = new Point(x_st + dx * 1, y_st + dy * 2 - 25);
            label17.Location = new Point(x_st + dx * 2, y_st + dy * 2 - 25);
            label18.Location = new Point(x_st + dx * 3, y_st + dy * 2 - 25);
            label19.Location = new Point(x_st + dx * 4, y_st + dy * 2 - 25);
            label20.Location = new Point(x_st + dx * 5, y_st + dy * 2 - 25);

            label1.Text = "原圖";
            label2.Text = "Sepia";
            label3.Text = "灰階SetPixel";
            label4.Text = "灰階Marshal";
            label5.Text = "灰度處理";
            label6.Text = "單色處理";
            label7.Text = "單色 R";
            label8.Text = "單色 G";
            label9.Text = "單色 B";
            label10.Text = "負片";
            label11.Text = "原圖";
            label12.Text = "灰階 Grayscale";
            label13.Text = "灰階 Average";
            label14.Text = "";
            label15.Text = "鏡像圖片";
            label16.Text = "";
            label17.Text = "彩虹化圖片";
            label18.Text = "二值化圖片";
            label19.Text = "8位灰度影像";
            label20.Text = "";
        }

        private void PictureToSepia1()
        {
            //將圖片轉為 Sepia 效果
            // Display the image converted to sepia tone.
            pictureBox2.Image = ToSepiaTone1(pictureBox1.Image);
        }

        // Convert an image to sepia tone.
        private Bitmap ToSepiaTone1(Image image)
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
            Bitmap bmp = new Bitmap(image.Width, image.Height);
            using (Graphics gr = Graphics.FromImage(bmp))
            {
                gr.DrawImage(image, points, rect, GraphicsUnit.Pixel, attributes);
            }

            // Return the result.
            return bmp;
        }

        private void PictureToSepia2()
        {
            //將圖片轉為 Sepia 效果
            // Display the image converted to sepia tone.
            pictureBox2.Image = ToSepiaTone2(pictureBox1.Image);
        }

        // Convert an image to sepia tone.
        private Bitmap ToSepiaTone2(Image image)
        {
            //將圖片轉為 Sepia 效果
            //read image
            Bitmap bmp = new Bitmap(image);

            //get image dimension
            int width = bmp.Width;
            int height = bmp.Height;

            //color of pixel
            Color p;

            //sepia
            for (int y = 0; y < height; y++)
            {
                for (int x = 0; x < width; x++)
                {
                    //get pixel value
                    p = bmp.GetPixel(x, y);

                    //extract pixel component ARGB
                    int a = p.A;
                    int r = p.R;
                    int g = p.G;
                    int b = p.B;

                    //calculate temp value
                    int tr = (int)(0.393 * r + 0.769 * g + 0.189 * b);
                    int tg = (int)(0.349 * r + 0.686 * g + 0.168 * b);
                    int tb = (int)(0.272 * r + 0.534 * g + 0.131 * b);

                    //set new RGB value
                    if (tr > 255)
                    {
                        r = 255;
                    }
                    else
                    {
                        r = tr;
                    }

                    if (tg > 255)
                    {
                        g = 255;
                    }
                    else
                    {
                        g = tg;
                    }

                    if (tb > 255)
                    {
                        b = 255;
                    }
                    else
                    {
                        b = tb;
                    }

                    //set the new RGB value in image pixel
                    bmp.SetPixel(x, y, Color.FromArgb(a, r, g, b));
                }
            }
            return bmp;
        }

        private void PictureToGray1()
        {
            //SetPixel 彩色轉灰階
            string filename = @"C:\______test_files\picture1.jpg";
            color_to_gray_1(filename);
        }

        private void PictureToGray2()
        {
            //Marshal 彩色轉灰階
            string filename = @"C:\______test_files\picture1.jpg";
            color_to_gray_2(filename);
        }

        void color_to_gray_1(string filename)
        {
            richTextBox1.Text += "SetPixel 彩色轉灰階\n";

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
            pictureBox3.Image = bmp;
        }

        void color_to_gray_2(string filename)
        {
            richTextBox1.Text += "Marshal 彩色轉灰階\n";

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
            pictureBox4.Image = bmp;
        }

        #region 灰度處理

        private void PictureToGray3()
        {
            //灰度處理
            string filename = @"C:\______test_files\picture1.jpg";
            Bitmap bitmap1 = new Bitmap(filename);
            pictureBox1.Image = bitmap1;
            Bitmap bitmap2 = 灰度處理(bitmap1);
            pictureBox5.Image = bitmap2;
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

        private void PictureToGray4()
        {
            //將圖片改為灰階 Grayscale
            string filename = @"C:\______test_files\bear.jpg";
            ConvertFile(filename, false);
        }

        private void PictureToGray5()
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

            pictureBox11.Image = Bitmap.FromFile(filename);

            // Convert to grayscale.
            //Bitmap bmp = new Bitmap(pictureBox1.Image);       same
            Bitmap bmp = LoadBitmapWithoutLocking(filename);

            // Convert the image.
            ConvertBitmapToGrayscale(bmp, use_average);

            // Show the converted bitmap
            if (use_average == true)
                pictureBox13.Image = bmp;
            else
                pictureBox12.Image = bmp;

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

        private void PictureToMonochrome()
        {
            richTextBox1.Text += "PictureToMonochrome\n";
            pictureBox6.Image = ToMonochrome(pictureBox1.Image);
        }

        // Convert an image to monochrome.
        private Bitmap ToMonochrome(Image image)
        {
            // Make the ColorMatrix.
            ColorMatrix cm = new ColorMatrix(new float[][]
            {
                new float[] {0.299f, 0.299f, 0.299f, 0, 0},
                new float[] {0.587f, 0.587f, 0.587f, 0, 0},
                new float[] {0.114f, 0.114f, 0.114f, 0, 0},
                new float[] { 0, 0, 0, 1, 0},
                new float[] { 0, 0, 0, 0, 1}
            });
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

        // Scale an image's color components.
        private Bitmap ScaleColorComponents(Image image, float r, float g, float b, float a)
        {
            // Make the ColorMatrix.
            ColorMatrix cm = new ColorMatrix(new float[][]
                {
                    new float[] {r, 0, 0, 0, 0},
                    new float[] {0, g, 0, 0, 0},
                    new float[] {0, 0, b, 0, 0},
                    new float[] {0, 0, 0, a, 0},
                    new float[] {0, 0, 0, 0, 1},
                });
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


        private void bt_clear_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = null;
            pictureBox2.Image = null;
            richTextBox1.Clear();
        }

        private void PictureToNegative()
        {
            richTextBox1.Text += "PictureToNegative\n";
            pictureBox10.Image = ToNegative(pictureBox1.Image);
        }

        private Bitmap ToNegative(Image image)
        {
            // Make the result bitmap.
            Bitmap bmp = new Bitmap(image);

            //get image dimension
            int width = image.Width;
            int height = image.Height;

            //negative
            for (int y = 0; y < height; y++)
            {
                for (int x = 0; x < width; x++)
                {
                    //get pixel value
                    Color p = bmp.GetPixel(x, y);

                    //extract ARGB value from p
                    int a = p.A;
                    int r = p.R;
                    int g = p.G;
                    int b = p.B;

                    //find negative value
                    r = 255 - r;
                    g = 255 - g;
                    b = 255 - b;

                    //set new ARGB value in pixel
                    bmp.SetPixel(x, y, Color.FromArgb(a, r, g, b));
                }
            }
            // Return the result.
            return bmp;

        }

        private void PictureToMirror()
        {
            richTextBox1.Text += "PictureToMirror\n";
            pictureBox15.Image = ToMirror(pictureBox1.Image);
        }

        private Bitmap ToMirror(Image image)
        {
            // Make the result bitmap.
            Bitmap bmp = new Bitmap(image);

            //get image dimension
            int width = image.Width;
            int height = image.Height;

            //mirror image
            Bitmap mimg = new Bitmap(width * 2, height);

            for (int y = 0; y < height; y++)
            {
                for (int lx = 0, rx = width * 2 - 1; lx < width; lx++, rx--)
                {
                    //get source pixel value
                    Color p = bmp.GetPixel(lx, y);

                    //set mirror pixel value
                    mimg.SetPixel(lx, y, p);
                    mimg.SetPixel(rx, y, p);
                }
            }
            // Return the result.
            return mimg;
        }

        private void show_mono_color_picture()
        {
            //image path
            string filename = @"C:\______test_files\picture1.jpg";

            //read image
            Bitmap bmp = new Bitmap(filename);

            //load original image in picturebox1
            //pictureBox1.Image = Image.FromFile(filename);

            //get image dimension
            int width = bmp.Width;
            int height = bmp.Height;

            //3 bitmap for red green blue image
            Bitmap rbmp = new Bitmap(bmp);
            Bitmap gbmp = new Bitmap(bmp);
            Bitmap bbmp = new Bitmap(bmp);

            //red green blue image
            for (int y = 0; y < height; y++)
            {
                for (int x = 0; x < width; x++)
                {
                    //get pixel value
                    Color p = bmp.GetPixel(x, y);

                    //extract ARGB value from p
                    int a = p.A;
                    int r = p.R;
                    int g = p.G;
                    int b = p.B;

                    //set red image pixel
                    rbmp.SetPixel(x, y, Color.FromArgb(a, r, 0, 0));

                    //set green image pixel
                    gbmp.SetPixel(x, y, Color.FromArgb(a, 0, g, 0));

                    //set blue image pixel
                    bbmp.SetPixel(x, y, Color.FromArgb(a, 0, 0, b));
                }
            }

            //load red image in picturebox7
            pictureBox7.Image = rbmp;

            //load green image in picturebox8
            pictureBox8.Image = gbmp;

            //load blue image in picturebox9
            pictureBox9.Image = bbmp;
        }

        private void PictureToRainbow()
        {
            richTextBox1.Text += "PictureToRainbow\n";
            pictureBox17.Image = ToRainbow(pictureBox11.Image);
        }

        private Bitmap ToRainbow(Image image)
        {
            //get image dimension
            int width = image.Width;
            int height = image.Height;

            Bitmap bmp = new Bitmap(width, height);
            using (Graphics gr = Graphics.FromImage(bmp))
            {
                // Define target colors.
                Color[] color =
                {
                    //Color.Red, Color.Orange, Color.Yellow,
                    //Color.Green, Color.Blue, Color.Indigo,
                    //Color.Violet,

                    Color.Red, Color.OrangeRed, Color.Yellow,
                    Color.Green, Color.Blue, Color.Indigo,
                    Color.Fuchsia,
                };
                const float scale = 2.0f;

                // Draw.
                for (int i = 0; i < color.Length; i++)
                {
                    // Create the ColorMatrix.
                    ColorMatrix cm = new ColorMatrix(new float[][]
                    {
                        new float[] {color[i].R / 255f * scale, 0, 0, 0, 0},
                        new float[] {0, color[i].G / 255f * scale, 0, 0, 0},
                        new float[] {0, 0, color[i].B / 255f * scale, 0, 0},
                        new float[] {0, 0, 0, 1, 0},
                        new float[] {0, 0, 0, 0, 1},
                    });
                    ImageAttributes attr = new ImageAttributes();
                    attr.SetColorMatrix(cm);

                    // Draw the next part of the image.
                    int x = (int)(i * image.Width / color.Length);
                    Point[] points =
                    {
                        new Point(x, 0),
                        new Point(width, 0),
                        new Point(x, height),
                    };
                    Rectangle rect = new Rectangle(x, 0, width - x, height);
                    gr.DrawImage(image, points, rect, GraphicsUnit.Pixel, attr);
                }
            }
            return bmp;
        }

        //二值化圖片 ST
        private void PictureToBinary()
        {
            //二值化圖片
            richTextBox1.Text += "PictureToBinary\n";
            pictureBox18.Image = OtsuThreshold(new Bitmap("c:\\______test_files\\picture1.jpg"));
        }

        #region 二值化
        #region Otsu閾值法二值化模組
        /// <summary>   
        /// Otsu閾值   
        /// </summary>   
        /// <param name="b">點陣圖流</param>   
        /// <returns></returns>   
        public Bitmap OtsuThreshold(Bitmap bitmap)
        {

            // 影象灰度化   
            // b = Gray(b);   
            int width = bitmap.Width;
            int height = bitmap.Height;
            byte threshold = 0;
            int[] hist = new int[256];

            int AllPixelNumber = 0, PixelNumberSmall = 0, PixelNumberBig = 0;

            double MaxValue, AllSum = 0, SumSmall = 0, SumBig, ProbabilitySmall, ProbabilityBig, Probability;
            BitmapData bmpData = bitmap.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, System.Drawing.Imaging.PixelFormat.Format32bppArgb);


            unsafe
            {
                byte* p = (byte*)bmpData.Scan0;
                int offset = bmpData.Stride - width * 4;
                for (int j = 0; j < height; j++)
                {
                    for (int i = 0; i < width; i++)
                    {
                        hist[p[0]]++;
                        p += 4;
                    }
                    p += offset;
                }
                bitmap.UnlockBits(bmpData);
            }
            //計算灰度為I的畫素出現的概率   
            for (int i = 0; i < 256; i++)
            {
                AllSum += i * hist[i];     //   質量矩   
                AllPixelNumber += hist[i];  //  質量       
            }
            MaxValue = -1.0;
            for (int i = 0; i < 256; i++)
            {
                PixelNumberSmall += hist[i];
                PixelNumberBig = AllPixelNumber - PixelNumberSmall;
                if (PixelNumberBig == 0)
                {
                    break;
                }

                SumSmall += i * hist[i];
                SumBig = AllSum - SumSmall;
                ProbabilitySmall = SumSmall / PixelNumberSmall;
                ProbabilityBig = SumBig / PixelNumberBig;
                Probability = PixelNumberSmall * ProbabilitySmall * ProbabilitySmall + PixelNumberBig * ProbabilityBig * ProbabilityBig;
                if (Probability > MaxValue)
                {
                    MaxValue = Probability;
                    threshold = (byte)i;
                }
            }
            this.Threshoding(bitmap, threshold);
            bitmap = twoBit(bitmap);
            return bitmap;

        }
        #endregion

        #region      固定閾值法二值化模組
        public Bitmap Threshoding(Bitmap b, byte threshold)
        {
            int width = b.Width;
            int height = b.Height;
            BitmapData data = b.LockBits(new Rectangle(0, 0, width, height), ImageLockMode.ReadWrite, System.Drawing.Imaging.PixelFormat.Format32bppArgb);
            unsafe
            {
                byte* p = (byte*)data.Scan0;
                int offset = data.Stride - width * 4;
                byte R, G, B, gray;
                for (int y = 0; y < height; y++)
                {
                    for (int x = 0; x < width; x++)
                    {
                        R = p[2];
                        G = p[1];
                        B = p[0];
                        gray = (byte)((R * 19595 + G * 38469 + B * 7472) >> 16);
                        if (gray >= threshold)
                        {
                            p[0] = p[1] = p[2] = 255;
                        }
                        else
                        {
                            p[0] = p[1] = p[2] = 0;
                        }
                        p += 4;
                    }
                    p += offset;
                }
                b.UnlockBits(data);
                return b;

            }

        }
        #endregion


        #region 建立1點陣圖像

        /// <summary>
        /// 建立1點陣圖像
        /// </summary>
        /// <param name="srcBitmap"></param>
        /// <returns></returns>
        public Bitmap twoBit(Bitmap srcBitmap)
        {
            int midrgb = System.Drawing.Color.FromArgb(128, 128, 128).ToArgb();
            int stride;//簡單公式((width/8)+3)&(~3)
            stride = (srcBitmap.Width % 8) == 0 ? (srcBitmap.Width / 8) : (srcBitmap.Width / 8) + 1;
            stride = (stride % 4) == 0 ? stride : ((stride / 4) + 1) * 4;
            int k = srcBitmap.Height * stride;
            byte[] buf = new byte[k];
            int x = 0, ab = 0;
            for (int j = 0; j < srcBitmap.Height; j++)
            {
                k = j * stride;//因影象寬度不同、有的可能有填充位元組需要跳越
                x = 0;
                ab = 0;
                for (int i = 0; i < srcBitmap.Width; i++)
                {
                    //從灰度變單色（下法如果直接從彩色變單色效果不太好，不過反相也可以在這裡控制）
                    if ((srcBitmap.GetPixel(i, j)).ToArgb() > midrgb)
                    {
                        ab = ab * 2 + 1;
                    }
                    else
                    {
                        ab = ab * 2;
                    }
                    x++;
                    if (x == 8)
                    {
                        buf[k++] = (byte)ab;//每位元組賦值一次，陣列buf中儲存的是十進位制。
                        ab = 0;
                        x = 0;
                    }
                }
                if (x > 0)
                {
                    //迴圈實現：剩餘有效資料不滿1位元組的情況下須把它們移往位元組的高位部分
                    for (int t = x; t < 8; t++) ab = ab * 2;
                    buf[k++] = (byte)ab;
                }
            }
            int width = srcBitmap.Width;
            int height = srcBitmap.Height;
            Bitmap dstBitmap = new Bitmap(width, height, System.Drawing.Imaging.PixelFormat.Format1bppIndexed);
            BitmapData dt = dstBitmap.LockBits(new Rectangle(0, 0, dstBitmap.Width, dstBitmap.Height), ImageLockMode.ReadWrite, dstBitmap.PixelFormat);
            Marshal.Copy(buf, 0, dt.Scan0, buf.Length);
            dstBitmap.UnlockBits(dt);
            return dstBitmap;
        }

        #endregion

        #endregion
        //二值化圖片 SP


        //建立8位灰度影像 ST
        private void PictureTo8BitGrayScale()
        {
            richTextBox1.Text += "PictureTo8BitGrayScale\n";
            pictureBox19.Image = RGB2Gray(new Bitmap("c:\\______test_files\\picture1.jpg"));
        }

        /// 建立8位灰度影像
        /// </summary>
        /// <param name="width"></param>
        /// <param name="height"></param>
        /// <returns></returns>
        public static Bitmap CreateGrayscaleImage(int width, int height)
        {
            // create new image
            Bitmap bmp = new Bitmap(width, height, System.Drawing.Imaging.PixelFormat.Format8bppIndexed);
            // set palette to grayscale
            SetGrayscalePalette(bmp);
            // return new image
            return bmp;
        }

        ///<summary>
        /// Set pallete of the image to grayscale
        ///</summary>
        public static void SetGrayscalePalette(Bitmap srcImg)
        {
            // check pixel format
            if (srcImg.PixelFormat != System.Drawing.Imaging.PixelFormat.Format8bppIndexed)
                throw new ArgumentException();
            // get palette
            ColorPalette cp = srcImg.Palette;
            // init palette
            for (int i = 0; i < 256; i++)
            {
                cp.Entries[i] = System.Drawing.Color.FromArgb(i, i, i);
            }
            srcImg.Palette = cp;
        }

        /// <summary>
        /// 轉為灰度影象，位深度也改變
        /// </summary>
        /// <param name="srcBitmap"></param>
        /// <returns></returns>
        public static Bitmap RGB2Gray(Bitmap srcBitmap)
        {
            int wide = srcBitmap.Width;
            int height = srcBitmap.Height;
            Rectangle rect = new Rectangle(0, 0, wide, height);
            //將Bitmap鎖定到系統記憶體中,獲得BitmapData
            BitmapData srcBmData = srcBitmap.LockBits(rect, ImageLockMode.ReadWrite, System.Drawing.Imaging.PixelFormat.Format24bppRgb);
            //建立Bitmap
            Bitmap dstBitmap = CreateGrayscaleImage(wide, height);//這個函式在後面有定義
            BitmapData dstBmData = dstBitmap.LockBits(rect, ImageLockMode.ReadWrite, System.Drawing.Imaging.PixelFormat.Format8bppIndexed);
            //點陣圖中第一個畫素資料的地址。它也可以看成是點陣圖中的第一個掃描行
            System.IntPtr srcPtr = srcBmData.Scan0;
            System.IntPtr dstPtr = dstBmData.Scan0;
            //將Bitmap物件的資訊存放到byte陣列中
            int src_bytes = srcBmData.Stride * height;
            byte[] srcValues = new byte[src_bytes];
            int dst_bytes = dstBmData.Stride * height;
            byte[] dstValues = new byte[dst_bytes];
            //複製GRB資訊到byte陣列
            System.Runtime.InteropServices.Marshal.Copy(srcPtr, srcValues, 0, src_bytes);
            System.Runtime.InteropServices.Marshal.Copy(dstPtr, dstValues, 0, dst_bytes);
            //根據Y=0.299*R+0.114*G+0.587B,Y為亮度
            for (int i = 0; i < height; i++)
                for (int j = 0; j < wide; j++)
                {
                    //只處理每行中影象畫素資料,捨棄未用空間
                    //注意點陣圖結構中RGB按BGR的順序儲存
                    int k = 3 * j;
                    byte temp = (byte)(srcValues[i * srcBmData.Stride + k + 2] * .299 + srcValues[i * srcBmData.Stride + k + 1] * .587 + srcValues[i * srcBmData.Stride + k] * .114);
                    dstValues[i * dstBmData.Stride + j] = temp;
                }
            System.Runtime.InteropServices.Marshal.Copy(dstValues, 0, dstPtr, dst_bytes);
            //解鎖點陣圖
            srcBitmap.UnlockBits(srcBmData);
            dstBitmap.UnlockBits(dstBmData);
            return dstBitmap;
        }



        //建立8位灰度影像 SP

    }
}
