using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;
using System.Drawing.Drawing2D;

namespace vcs_PictureThumbnail2
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

        private void button0_Click(object sender, EventArgs e)
        {
            //根據原圖生成縮略圖
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            richTextBox1.Text += "圖檔 轉 Bitmap\n";
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式

            richTextBox1.Text += "Bitmap 轉 MemoryStream\n";
            MemoryStream ms = new MemoryStream();
            bitmap1.Save(ms, ImageFormat.Jpeg);

            richTextBox1.Text += "MemoryStream 轉 拜列\n";
            byte[] pic_array1 = ms.ToArray();


            byte[] pic_array2 = GenerateThumbImg(pic_array1, bitmap1.Width / 2, bitmap1.Height / 2);

            //then....  拜列 轉圖片~~~~

        }


        //C#根據原圖生成縮略圖
        /// <summary>
        /// 生成縮略圖
        /// </summary>
        /// <param name="imgBuffer">原圖byte[]</param>
        /// <param name="width">生成的縮略圖寬度</param>
        /// <param name="height">生成的縮略圖高度</param>
        /// <returns></returns>
        private byte[] GenerateThumbImg(byte[] imgBuffer, int width, int height)
        {
            MemoryStream imgStream = null;
            MemoryStream thumbStream = new MemoryStream(); ;
            Image img = null;
            Image thumbImg = null;
            Graphics g = null;
            try
            {
                imgStream = new MemoryStream(imgBuffer);
                img = Image.FromStream(imgStream);
                thumbImg = new Bitmap(img, width, height);
                g = Graphics.FromImage(thumbImg);
                g.DrawImage(thumbImg, 0, 0, width, height);
                /*g.DrawImage(img, new Rectangle(0, 0, width, height),
                    0, 0, width, height, GraphicsUnit.Pixel);*/
                thumbImg.Save(thumbStream, ImageFormat.Jpeg);
                return thumbStream.ToArray();
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                return null;
            }
            finally
            {
                if (g != null)
                    g.Dispose();
                if (thumbImg != null)
                    thumbImg.Dispose();
                if (img != null)
                    img.Dispose();
                if (thumbStream != null)
                    thumbStream.Close();
                if (imgStream != null)
                    imgStream.Close();
            }
        }


        private void button1_Click(object sender, EventArgs e)
        {
            //圖片縮為 100 X 100
            richTextBox1.Text += "建立縮圖\t圖片縮為 100 X 100\n";
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            int w = 100;
            int h = 100;
            int flag = 100;
            GetPicThumbnail(filename, w, h, flag);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //圖片縮為 一半 X 一半
            richTextBox1.Text += "建立縮圖\t圖片縮為 一半 X 一半\n";
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            //讀圖片檔案至記憶體
            //read image
            Bitmap bitmap1 = new Bitmap(filename);

            int w = bitmap1.Width / 2;
            int h = bitmap1.Height / 2;
            int flag = 100;
            GetPicThumbnail(filename, w, h, flag);
        }

        /// <summary>
        /// 根據指定尺寸得到按比例縮放的尺寸,返回true表示已更改尺寸
        /// </summary>
        /// <param name="picWidth">圖片寬度</param>
        /// <param name="picHeight">圖片高度</param>
        /// <param name="specifiedWidth">指定寬度</param>
        /// /// <param name="specifiedHeight">指定高度</param>
        /// <returns>返回true表示以更改尺寸</returns>
        private bool GetPicZoomSize(ref int picWidth, ref int picHeight, int specifiedWidth, int specifiedHeight)
        {
            int sW = 0, sH = 0;
            Boolean isZoomSize = false;
            //按比例縮放
            Size tem_size = new Size(picWidth, picHeight);
            if (tem_size.Width > specifiedWidth || tem_size.Height > specifiedHeight) //將**改成c#中的或者操作符號
            {
                if ((tem_size.Width * specifiedHeight) > (tem_size.Height * specifiedWidth))
                {
                    sW = specifiedWidth;
                    sH = (specifiedWidth * tem_size.Height) / tem_size.Width;
                }
                else
                {
                    sH = specifiedHeight;
                    sW = (tem_size.Width * specifiedHeight) / tem_size.Height;
                }
                isZoomSize = true;
            }
            else
            {
                sW = tem_size.Width;
                sH = tem_size.Height;
            }
            picHeight = sH;
            picWidth = sW;
            return isZoomSize;
        }
        /// <summary>
        /// 無損壓縮圖片
        /// </summary>
        /// <param name="sFile">原圖片</param>
        /// <param name="dWidth">寬度</param>
        /// <param name="dHeight">高度</param>
        /// <param name="flag">壓縮質量 1-100</param>
        /// <returns></returns>

        public bool GetPicThumbnail(string sFile, int dWidth, int dHeight, int flag)
        {
            Image iSource = Image.FromFile(sFile);
            ImageFormat tFormat = iSource.RawFormat;
            int sW = iSource.Width, sH = iSource.Height;

            GetPicZoomSize(ref sW, ref sH, dWidth, dHeight);

            Bitmap ob = new Bitmap(dWidth, dHeight);
            Graphics g = Graphics.FromImage(ob);
            g.Clear(Color.WhiteSmoke);
            g.CompositingQuality = CompositingQuality.HighQuality;
            g.SmoothingMode = SmoothingMode.HighQuality;
            g.InterpolationMode = InterpolationMode.HighQualityBicubic;
            g.DrawImage(iSource, new Rectangle((dWidth - sW) / 2, (dHeight - sH) / 2, sW, sH), 0, 0, iSource.Width, iSource.Height, GraphicsUnit.Pixel);
            g.Dispose();
            //以下代碼為保存圖片時，設置壓縮質量
            EncoderParameters ep = new EncoderParameters();
            long[] qy = new long[1];
            qy[0] = flag;//設置壓縮的比例1-100
            EncoderParameter eParam = new EncoderParameter(System.Drawing.Imaging.Encoder.Quality, qy);
            ep.Param[0] = eParam;
            try
            {
                ImageCodecInfo[] arrayICI = ImageCodecInfo.GetImageEncoders();

                ImageCodecInfo jpegICIinfo = null;

                for (int x = 0; x < arrayICI.Length; x++)
                {
                    if (arrayICI[x].FormatDescription.Equals("JPEG"))
                    {
                        jpegICIinfo = arrayICI[x];
                        break;
                    }
                }

                if (jpegICIinfo != null)
                {
                    string filename = Application.StartupPath + "\\jpg_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
                    //richTextBox1.Text += "save file " + dFile + "\n";
                    ob.Save(filename, jpegICIinfo, ep);
                    //ob.Save(@file1, ImageFormat.Jpeg);
                }
                else
                {
                    string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
                    //ob.Save(dFile, tFormat);
                    ob.Save(filename, tFormat);
                }
                return true;
            }
            catch
            {
                return false;
            }
            finally
            {
                iSource.Dispose();
                ob.Dispose();
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //圖片縮略圖
            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            string filename2 = Application.StartupPath + "\\thumb_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
            bool result = getThumImage(filename1, 100, 3, filename2);
            if (result == true)
                richTextBox1.Text += "OK\n";
            else
                richTextBox1.Text += "FAIL\n";
        }

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
                System.Drawing.Imaging.Encoder myEncoder = System.Drawing.Imaging.Encoder.Quality;
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


        private void button4_Click(object sender, EventArgs e)
        {
            //產生縮略圖
            //產生縮略圖
            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            string filename2 = Application.StartupPath + "\\thumb_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
            bool result = getThumImage2(filename1, filename2);
            if (result == true)
                richTextBox1.Text += "OK\n";
            else
                richTextBox1.Text += "FAIL\n";
        }

        //　產生縮略圖

        public bool ThumbnailCallback()
        {
            return true;
        }

        private bool getThumImage2(string imgPath, string thumbPath)
        {
            Image.GetThumbnailImageAbort myCallback = new Image.GetThumbnailImageAbort(ThumbnailCallback);
            Image img = Image.FromFile(imgPath);　//　通過文件構造
            //生成縮略圖
            Image myThumbnail = img.GetThumbnailImage(100, 50, myCallback, IntPtr.Zero);
            myThumbnail.Save(thumbPath);　//　保存縮略圖
            return true;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //減少圖片文件大小和尺寸
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            pictureBox1.Image = reduce_bitmap(bitmap1, 80);
            //pictureBox2.Image = reduce_bitmap(bitmap1, 50);
            //pictureBox3.Image = reduce_bitmap(bitmap1, 20);
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

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {

        }

        private void button10_Click(object sender, EventArgs e)
        {

        }

        private void button11_Click(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {

        }

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button15_Click(object sender, EventArgs e)
        {

        }




    }
}
