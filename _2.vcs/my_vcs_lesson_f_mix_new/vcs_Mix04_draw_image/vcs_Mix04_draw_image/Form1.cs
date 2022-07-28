using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Drawing2D;
using System.Drawing.Imaging;   //for Encoder

namespace vcs_Mix04_draw_image
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
            string filename = @"C:\______test_files\picture1.jpg";
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
            dx = 180;
            dy = 90;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            //pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            richTextBox1.Location = new Point(x_st + dx * 4 + 75, y_st + dy * 0);
        }



        //圖片切割、圖片壓縮、縮略圖生成代碼


        #region imageCut
        /// 圖片切割函數
        /// </summary>
        /// <param name="sourceFile">原始圖片文件</param>
        /// <param name="xNum">在Ｘ軸上的切割數量</param>
        /// <param name="yNum">在Ｙ軸上的切割數量</param>
        /// <param name="quality">質量壓縮比</param>
        /// <param name="outputFile">輸出文件名，不帶后綴</param>
        /// <returns>成功返回true，失敗則返回false</returns>
        public static bool imageCut(String sourceFile, int xNum, int yNum, long quality, String outputFile)
        {
            try
            {
                long imageQuality = quality;
                Bitmap sourceImage = new Bitmap(sourceFile);
                ImageCodecInfo myImageCodecInfo = GetEncoderInfo("image/jpeg");
                Encoder myEncoder = Encoder.Quality;
                EncoderParameters myEncoderParameters = new EncoderParameters(1);
                EncoderParameter myEncoderParameter = new EncoderParameter(myEncoder, imageQuality);
                myEncoderParameters.Param[0] = myEncoderParameter;
                float xWidth = sourceImage.Width / xNum;
                float yWidth = sourceImage.Height / yNum;
                String outputImage = "";

                for (int countY = 0; countY < yNum; countY++)
                    for (int countX = 0; countX < xNum; countX++)
                    {

                        RectangleF cloneRect = new RectangleF(countX * xWidth, countY * yWidth, xWidth, yWidth);
                        Bitmap newImage = sourceImage.Clone(cloneRect, PixelFormat.Format24bppRgb);
                        outputImage = outputFile + countX + countY + ".jpg";
                        newImage.Save(outputImage, myImageCodecInfo, myEncoderParameters);

                    }
                return true;
            }
            catch
            {
                return false;
            }

        }
        #endregion


        #region imageCompress
        /**/
        /// <summary>
        /// 圖片壓縮函數
        /// </summary>
        /// <param name="sourceFile">原始圖片文件</param>
        /// <param name="quality">質量壓縮比</param>
        /// <param name="ouputFile">輸出文件名,請用 .jpg 后綴 </param>
        /// <returns>成功返回true，失敗則返回false</returns>
        public static bool imageCompress(String sourceFile, long quality, String outputFile)
        {
            try
            {
                long imageQuality = quality;
                Bitmap sourceImage = new Bitmap(sourceFile);
                ImageCodecInfo myImageCodecInfo = GetEncoderInfo("image/jpeg");
                Encoder myEncoder = Encoder.Quality;
                EncoderParameters myEncoderParameters = new EncoderParameters(1);
                EncoderParameter myEncoderParameter = new EncoderParameter(myEncoder, imageQuality);
                myEncoderParameters.Param[0] = myEncoderParameter;

                sourceImage.Save(outputFile, myImageCodecInfo, myEncoderParameters);
                return true;

            }
            catch
            {
                return false;
            }

        }
        #endregion

        #region getThumImage
        /**/
        /// <summary>
        /// 生成縮略圖
        /// </summary>
        /// <param name="sourceFile">原始圖片文件</param>
        /// <param name="quality">質量壓縮比</param>
        /// <param name="multiple">收縮倍數</param>
        /// <param name="outputFile">輸出文件名</param>
        /// <returns>成功返回true,失敗則返回false</returns>
        public static bool getThumImage(String sourceFile, long quality, int multiple, String outputFile)
        {
            try
            {
                long imageQuality = quality;
                Bitmap sourceImage = new Bitmap(sourceFile);
                ImageCodecInfo myImageCodecInfo = GetEncoderInfo("image/jpeg");
                Encoder myEncoder = Encoder.Quality;
                EncoderParameters myEncoderParameters = new EncoderParameters(1);
                EncoderParameter myEncoderParameter = new EncoderParameter(myEncoder, imageQuality);
                myEncoderParameters.Param[0] = myEncoderParameter;
                float xWidth = sourceImage.Width;
                float yWidth = sourceImage.Height;
                Bitmap newImage = new Bitmap((int)(xWidth / multiple), (int)(yWidth / multiple));
                Graphics g = Graphics.FromImage(newImage);

                g.DrawImage(sourceImage, 0, 0, xWidth / multiple, yWidth / multiple);
                g.Dispose();
                newImage.Save(outputFile, myImageCodecInfo, myEncoderParameters);
                return true;
            }
            catch
            {
                return false;
            }
        }
        #endregion


        #region ImageCodecInfo
        /**/
        /// <summary>
        /// 獲取圖片編碼信息
        /// </summary>
        private static ImageCodecInfo GetEncoderInfo(String mimeType)
        {
            int j;
            ImageCodecInfo[] encoders;
            encoders = ImageCodecInfo.GetImageEncoders();
            for (j = 0; j < encoders.Length; ++j)
            {
                if (encoders[j].MimeType == mimeType)
                    return encoders[j];
            }
            return null;
        }
        #endregion

        /*  
        C#圖片切割、圖片壓縮、縮略圖生成代碼匯總

        public static bool imageCut(String sourceFile, int xNum, int yNum, long quality, String outputFile)
        public static bool imageCompress(String sourceFile,long quality,String outputFile)
        public static bool getThumImage(String sourceFile, long quality, int multiple, String outputFile)
        */


        private void button0_Click(object sender, EventArgs e)
        {
            //圖片切割, 切成 M X N 個
            string filename1 = @"C:\______test_files\picture1.jpg";
            string filename2 = Application.StartupPath + "\\cut_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
            bool result = imageCut(filename1, 2, 2, 100, filename2);
            if (result == true)
                richTextBox1.Text += "OK\n";
            else
                richTextBox1.Text += "FAIL\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //圖片壓縮
            string filename1 = @"C:\______test_files\picture1.jpg";
            string filename2 = Application.StartupPath + "\\compress_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
            bool result = imageCompress(filename1, 30, filename2);
            if (result == true)
                richTextBox1.Text += "OK\n";
            else
                richTextBox1.Text += "FAIL\n";

        }

        private void button2_Click(object sender, EventArgs e)
        {
            //圖片縮略圖
            string filename1 = @"C:\______test_files\picture1.jpg";
            string filename2 = Application.StartupPath + "\\thumb_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
            bool result = getThumImage(filename1, 100, 3, filename2);
            if (result == true)
                richTextBox1.Text += "OK\n";
            else
                richTextBox1.Text += "FAIL\n";
        }

        public static Bitmap returnAlpha(Bitmap bmp, int alpha)
        {
            Color col;
            Bitmap bmp2 = new Bitmap(bmp);
            for (int i = 0; i < bmp.Width; i++)
                for (int j = 0; j < bmp.Height; j++)
                {
                    col = bmp.GetPixel(i, j);
                    if ((col.A - alpha) >= 0)
                    {
                        bmp2.SetPixel(i, j, Color.FromArgb(Math.Abs(col.A - alpha), col.R, col.G, col.B));
                        //bmp2.SetPixel(i, j, Color.FromArgb(10, col.R, col.G, col.B));
                    }
                }
            return bmp2;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //改變圖片透明度
            string filename = @"C:\______test_files\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            Bitmap bitmap80 = returnAlpha(bitmap1, 80);
            Bitmap bitmap160 = returnAlpha(bitmap1, 160);
            Bitmap bitmap220 = returnAlpha(bitmap1, 220);

            bitmap80.Save(@"picture_80.bmp", ImageFormat.Bmp);
            bitmap160.Save(@"picture_160.bmp", ImageFormat.Bmp);
            bitmap220.Save(@"picture_220.bmp", ImageFormat.Bmp);

            pictureBox1.Image = bitmap80;
            pictureBox2.Image = bitmap160;
            pictureBox3.Image = bitmap220;

            richTextBox1.Text += "OK\n";
        }

        Bitmap reduce_bitmap(Bitmap bitmap1, int percent)
        {
            //C#減少圖片文件大小和尺寸

            //生成80*100的縮略圖
            int W = bitmap1.Width;
            int H = bitmap1.Height;

            int w = W * percent / 100;
            int h = H * percent / 100;

            Bitmap bitmap2 = (Bitmap)bitmap1.GetThumbnailImage(w, h, null, IntPtr.Zero);

            return bitmap2;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //減少圖片文件大小和尺寸
            string filename = @"C:\______test_files\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            pictureBox1.Image = reduce_bitmap(bitmap1, 80);
            pictureBox2.Image = reduce_bitmap(bitmap1, 50);
            pictureBox3.Image = reduce_bitmap(bitmap1, 20);
        }


        //C#編程 jpg縮略圖函數 使用教程


        /// <summary>
        /// 生成jpg縮略圖字節,本人的小軟件中需要用到的功能，所以自己做了一個函數，和大家分享
        /// 為什麼要生成字節而不是文件，這是為了方便後續處理啦^_^
        /// </summary>
        /// <param name="originalImagePath">原始路徑</param>
        /// <param name="quality">質量0-100</param>
        /// <param name="width">寬度</param>
        /// <param name="height">高度</param>
        /// <param name="mode">模式：HW,W,H,Cut</param>
        /// <returns></returns>
        public static byte[] MakeJPGThumbnailBytes(string originalImagePath, long quality, int width, int height, string mode)
        {
            Image originalImage = Image.FromFile(originalImagePath);
            MemoryStream s = new MemoryStream();
            int towidth = width;
            int toheight = height;

            int x = 0;
            int y = 0;
            int ow = originalImage.Width;
            int oh = originalImage.Height;

            switch (mode)
            {
                case "HW"://指定高寬縮放（可能變形）
                    break;
                case "W"://指定寬，高按比例
                    toheight = originalImage.Height * width / originalImage.Width;
                    break;
                case "H"://指定高，寬按比例
                    towidth = originalImage.Width * height / originalImage.Height;
                    break;
                case "Cut"://指定高寬裁減（不變形）
                    if ((double)originalImage.Width / (double)originalImage.Height > (double)towidth / (double)toheight)
                    {
                        oh = originalImage.Height;
                        ow = originalImage.Height * towidth / toheight;
                        y = 0;
                        x = (originalImage.Width - ow) / 2;
                    }
                    else
                    {
                        ow = originalImage.Width;
                        oh = originalImage.Width * height / towidth;
                        x = 0;
                        y = (originalImage.Height - oh) / 2;
                    }
                    break;
                default:
                    break;
            }

            //新建一個bmp圖片
            Image bitmap = new System.Drawing.Bitmap(towidth, toheight);

            //新建一個畫板
            Graphics g = System.Drawing.Graphics.FromImage(bitmap);

            //設置高質量插值法
            g.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.High;

            //設置高質量,低速度呈現平滑程度
            g.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.HighQuality;

            //清空畫布並以透明背景色填充
            g.Clear(Color.Transparent);

            //在指定位置並且按指定大小繪制原圖片的指定部分
            g.DrawImage(originalImage, new Rectangle(0, 0, towidth, toheight),
            new Rectangle(x, y, ow, oh),
            GraphicsUnit.Pixel);

            try
            {
                //以jpg格式保存縮略圖
                EncoderParameters eps = new EncoderParameters(1);
                EncoderParameter ep = new EncoderParameter(Encoder.Quality, quality);
                eps.Param[0] = ep;
                bitmap.Save(s, GetCodecInfo("image/jpeg"), eps);
                return s.GetBuffer();
            }
            catch (System.Exception e)
            {
                throw e;
            }
            finally
            {
                originalImage.Dispose();
                bitmap.Dispose();
                s.Dispose();
                g.Dispose();
            }
        }

        /**/
        /// <summary>
        /// 保存JPG時用
        /// </summary>
        /// <param name="mimeType"></param>
        /// <returns>得到指定mimeType的ImageCodecInfo</returns>
        private static ImageCodecInfo GetCodecInfo(string mimeType)
        {
            ImageCodecInfo[] CodecInfo = ImageCodecInfo.GetImageEncoders();
            foreach (ImageCodecInfo ici in CodecInfo)
            {
                if (ici.MimeType == mimeType) return ici;
            }
            return null;
        }


        private void button5_Click(object sender, EventArgs e)
        {
            //jpg縮略圖

        }

        private void button6_Click(object sender, EventArgs e)
        {
            //改變圖片品質


            VaryQualityLevel();

        }

        private void VaryQualityLevel()
        {
            string filename = @"C:\______test_files\elephant.jpg";

            // Get a bitmap.
            Bitmap bitmap1 = new Bitmap(filename);
            bitmap1.Save(@"picture_old.jpg", ImageFormat.Jpeg);

            ImageCodecInfo jpgEncoder = GetEncoder(ImageFormat.Jpeg);

            // Create an Encoder object based on the GUID
            // for the Quality parameter category.
            Encoder myEncoder = Encoder.Quality;

            // Create an EncoderParameters object.
            // An EncoderParameters object has an array of EncoderParameter
            // objects. In this case, there is only one
            // EncoderParameter object in the array.
            EncoderParameters myEncoderParameters = new EncoderParameters(1);

            EncoderParameter myEncoderParameter = new EncoderParameter(myEncoder, 50L);
            myEncoderParameters.Param[0] = myEncoderParameter;
            bitmap1.Save(@"TestPhotoQuality050.jpg", jpgEncoder, myEncoderParameters);

            myEncoderParameter = new EncoderParameter(myEncoder, 100L);
            myEncoderParameters.Param[0] = myEncoderParameter;
            bitmap1.Save(@"TestPhotoQuality100.jpg", jpgEncoder, myEncoderParameters);

            // Save the bitmap as a JPG file with zero quality level compression.
            myEncoderParameter = new EncoderParameter(myEncoder, 0L);
            myEncoderParameters.Param[0] = myEncoderParameter;
            bitmap1.Save(@"TestPhotoQuality000.jpg", jpgEncoder, myEncoderParameters);

            richTextBox1.Text += "完成\n";
        }

        private ImageCodecInfo GetEncoder(ImageFormat format)
        {
            ImageCodecInfo[] codecs = ImageCodecInfo.GetImageEncoders();

            foreach (ImageCodecInfo codec in codecs)
            {
                if (codec.FormatID == format.Guid)
                {
                    return codec;
                }
            }

            return null;
        }

        private void button7_Click(object sender, EventArgs e)
        {

        }
    }
}
