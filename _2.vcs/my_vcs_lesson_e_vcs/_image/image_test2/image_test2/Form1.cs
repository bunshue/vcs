using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
//using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;
using System.Drawing.Imaging;

namespace image_test2
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

            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
        }



        //圖片切割、圖片壓縮、縮略圖生成代碼


        #region imageCut
        /// 图片切割函数
        /// </summary>
        /// <param name="sourceFile">原始图片文件</param>
        /// <param name="xNum">在Ｘ轴上的切割数量</param>
        /// <param name="yNum">在Ｙ轴上的切割数量</param>
        /// <param name="quality">质量压缩比</param>
        /// <param name="outputFile">输出文件名，不带后缀</param>
        /// <returns>成功返回true，失败则返回false</returns>
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
        /// 图片压缩函数
        /// </summary>
        /// <param name="sourceFile">原始图片文件</param>
        /// <param name="quality">质量压缩比</param>
        /// <param name="ouputFile">输出文件名,请用 .jpg 后缀 </param>
        /// <returns>成功返回true，失败则返回false</returns>
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
        /// 生成缩略图
        /// </summary>
        /// <param name="sourceFile">原始图片文件</param>
        /// <param name="quality">质量压缩比</param>
        /// <param name="multiple">收缩倍数</param>
        /// <param name="outputFile">输出文件名</param>
        /// <returns>成功返回true,失败则返回false</returns>
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
        /// 获取图片编码信息
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
            //圖片切割

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //圖片壓縮

        }

        private void button2_Click(object sender, EventArgs e)
        {
            //圖片縮略圖
        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {

        }
    }
}
