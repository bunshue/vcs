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
using System.Drawing.Drawing2D;     //for SmoothingMode, CompositingQuality, InterpolationMode

namespace vcs_PictureThumbnailGet
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\bear.bmp";

        public Form1()
        {
            InitializeComponent();
            Image img = Image.FromFile(filename);

            pictureBox1.Image = img;
        }

        private Bitmap GetThumbNail(string path)
        {
            //取得原圖
            Bitmap myBitmap = new Bitmap(path);

            //產生一張與imagelist大小的Bitmap
            Bitmap newBmp = new Bitmap(100, 100);

            Graphics g = Graphics.FromImage(newBmp);

            Pen p = new Pen(Color.Black);

            //設定高品質插值法  
            //g.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.High;
            //g.InterpolationMode = InterpolationMode.High;

            //設定高品質,低速度呈現平滑程度  
            //g.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.HighQuality;
            //g.SmoothingMode = SmoothingMode.HighQuality;

            //縮圖的寬高
            int newWidth = 0;
            int newHeight = 0;

            //在畫布內重繪縮圖的x,y軸座標
            int startX = 0;
            int startY = 0;

            //100為imagelist大圖示的寬,高
            if (myBitmap.Width > 100 || myBitmap.Height > 100)
            {
                if (myBitmap.Width > myBitmap.Height)
                {
                    //指定寬，高按比例
                    newWidth = 100;
                    newHeight = myBitmap.Height * newWidth / myBitmap.Width;
                    startY = (100 - newHeight) / 2;
                }
                else if (myBitmap.Width < myBitmap.Height)
                {
                    //指定高，寬按比例
                    newHeight = 100;
                    newWidth = myBitmap.Width * newHeight / myBitmap.Height;
                    startX = (100 - newWidth) / 2;
                }
            }
            else
            {
                //保持原圖的大小
                newWidth = myBitmap.Width;
                newHeight = myBitmap.Height;
                startX = (100 - newWidth) / 2;
                startY = (100 - newHeight) / 2;
            }

            //在100*100的畫布中裡在繪出比例縮圖
            //怕有寬高過大的圖產生例外，故使用先縮圖一次(使用大量記憶體)
            //g.DrawImage(myBitmap.GetThumbnailImage(newWidth, newHeight, null, IntPtr.Zero), startX, startY, newWidth, newHeight);
            g.DrawImage(myBitmap, startX, startY, newWidth, newHeight);

            //畫出最外圍的方框
            g.DrawRectangle(p, 0, 0, 99, 99);

            g.Dispose();
            myBitmap.Dispose();

            return newBmp;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Bitmap bmp = GetThumbNail(filename);

            pictureBox2.Image = bmp;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //取得圖片的縮略圖

            //調用生成縮略圖方法
            string filename = @"C:\______test_files\picture1.jpg";
            ToThumbnailImages(filename, 200);
        }

        /// <summary>
        /// 生成縮略圖
        /// </summary>
        /// <param name="filename1">原圖片路徑(相對路徑)</param>
        /// <param name="thumbnailImageWidth">縮略圖的寬度（高度與按源圖片比例自動生成）</param>
        public void ToThumbnailImages(string filename1, int thumbnailImageWidth)
        {
            int ThumbnailImageWidth = thumbnailImageWidth;
            string sExt = filename1.Substring(filename1.LastIndexOf(".")).ToLower();

            //從 原圖片 創建 Image 對象
            System.Drawing.Image image = System.Drawing.Image.FromFile(filename1);

            int num = ((ThumbnailImageWidth / 4) * 3);
            int width = image.Width;
            int height = image.Height;
            //計算圖片的比例
            if ((((double)width) / ((double)height)) >= 1.3333333333333333f)
            {
                num = ((height * ThumbnailImageWidth) / width);
            }
            else
            {
                ThumbnailImageWidth = ((width * num) / height);
            }
            if ((ThumbnailImageWidth < 1) || (num < 1))
            {
                return;
            }
            //用指定的大小和格式初始化 Bitmap 類的新實例
            Bitmap bitmap1 = new Bitmap(ThumbnailImageWidth, num, PixelFormat.Format32bppArgb);
            //從指定的 Image 對象創建新 Graphics 對象
            Graphics graphics = Graphics.FromImage(bitmap1);
            //清除整個繪圖面並以透明背景色填充
            graphics.Clear(Color.Transparent);
            //在指定位置並且按指定大小繪制 原圖片 對象
            graphics.DrawImage(image, new Rectangle(0, 0, ThumbnailImageWidth, num));
            image.Dispose();
            try
            {
                //將此 原圖片 以指定格式並用指定的編解碼參數保存到指定文件
                string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
                try
                {
                    //bitmap1.Save(@file1, ImageFormat.Jpeg);
                    bitmap1.Save(filename, ImageFormat.Bmp);
                    //bitmap1.Save(@file3, ImageFormat.Png);

                    //richTextBox1.Text += "已存檔 : " + file1 + "\n";
                    //richTextBox1.Text += "已存檔 : " + filename + "\n";
                    //richTextBox1.Text += "已存檔 : " + file3 + "\n";
                }
                catch (Exception ex)
                {
                    //richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }

            catch (System.Exception e)
            {
                throw e;
            }
            finally
            {
                bitmap1.Dispose();
                graphics.Dispose();
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += ((Button)sender).Text + "\n";

            string filename = @"C:\______test_files\elephant.jpg";

            System.Drawing.Image.GetThumbnailImageAbort callb = null;

            try
            {
                // 保存到指定的文件夾
                Image MyImage = Image.FromFile(filename);
                // 保存大圖(原圖)
                Image NewImage = MyImage.GetThumbnailImage(800, 1000, callb, new System.IntPtr());
                NewImage.Save("big.jpg");
                // 保存中圖
                NewImage = MyImage.GetThumbnailImage(400, 500, callb, new System.IntPtr());
                NewImage.Save("middle.jpg");

                // 單款衣服的圖片大小
                NewImage = MyImage.GetThumbnailImage(255, 319, callb, new System.IntPtr());
                NewImage.Save("SingleImage.jpg");

                // 保存小圖
                NewImage = MyImage.GetThumbnailImage(115, 144, callb, new System.IntPtr());
                NewImage.Save("small.jpg");
                // 保存極小圖
                NewImage = MyImage.GetThumbnailImage(45, 56, callb, new System.IntPtr());
                NewImage.Save("dinky.jpg");

                MyImage.Dispose();
                NewImage.Dispose();
                // 一定要釋放，否則進程被占用
            }
            catch (Exception ex)
            {
                //Response.Write(ex.ToString());
            }
            richTextBox1.Text += "完成\n";

        }

        private void button4_Click(object sender, EventArgs e)
        {
            //生成縮略圖, shrink模式
            string filename1 = @"C:\______test_files\picture1.jpg";
            string filename2 = @"C:\______test_files\picture1small.jpg";

            ShowThumbnail(filename1, filename2, 100, 200);
        }

        public void ShowThumbnail(string oldfile, string newfile, int white, int height)
        {
            System.Drawing.Image image = System.Drawing.Image.FromFile(oldfile);
            //获取原图高度和宽度
            int oldh = image.Height;
            int oldw = image.Width;
            int neww, newh;
            neww = white; newh = height;   //直接设定新图的高宽,,

            try
            {
                System.Drawing.Image bt = new System.Drawing.Bitmap(neww, newh);
                System.Drawing.Graphics gr = System.Drawing.Graphics.FromImage(bt);
                gr.Clear(Color.White);
                gr.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.HighQualityBicubic;
                gr.DrawImage(image, new Rectangle(0, 0, neww, newh), 0, 0, oldw, oldh, GraphicsUnit.Pixel);
                switch (oldfile.Substring(oldfile.Length - 3).ToUpper())
                {
                    case "JPG":
                        bt.Save(newfile, ImageFormat.Jpeg);
                        break;
                    case "GIF":
                        bt.Save(newfile, ImageFormat.Gif);
                        break;
                    case "PNG":
                        bt.Save(newfile, ImageFormat.Png);
                        break;
                    default:
                        bt.Save(newfile, ImageFormat.Jpeg);
                        break;
                }
                gr.Dispose();
                bt.Dispose();
                image.Dispose();
            }
            catch { }

        }

        private void button5_Click(object sender, EventArgs e)
        {
            //生成縮略圖
            string filename1 = @"C:\______test_files\elephant.jpg";
            string filename2 = Application.StartupPath + "\\small_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";

            Image image = System.Drawing.Image.FromFile(filename1);
            int W1 = image.Width;
            int H1 = image.Height;
            float ratio = (float)W1 / H1;

            //微缩图高度和宽度  
            int DefaultHeight = 300;    //縮略圖之高度
            int W2 = H1 <= DefaultHeight ? W1 : Convert.ToInt32(DefaultHeight * ratio);
            int H2 = H1 <= DefaultHeight ? H1 : DefaultHeight;

            CreateThumbnailPicture(filename1, filename2, W2, H2);

            richTextBox1.Text += "縮略圖之高度 = " + DefaultHeight.ToString() + "\n";
            richTextBox1.Text += "已存檔 : " + filename2 + "\n";
        }

        /// <summary>
        /// 圖片微縮圖處理
        /// </summary>
        /// <param name="srcPath">源圖片</param>
        /// <param name="destPath">目標圖片</param>
        /// <param name="width">寬度</param>
        /// <param name="height">高度</param>
        public static void CreateThumbnailPicture(string srcPath, string destPath, int width, int height)
        {
            //根據圖片的磁盤絕對路徑獲取 源圖片 的Image對象
            System.Drawing.Image img = System.Drawing.Image.FromFile(srcPath);

            //bmp： 最終要建立的 微縮圖 位圖對象。
            Bitmap bmp = new Bitmap(width, height);

            //g: 繪制 bmp Graphics 對象
            Graphics g = Graphics.FromImage(bmp);
            g.Clear(Color.Transparent);
            //為Graphics g 對象 初始化必要參數，很容易理解。
            g.PixelOffsetMode = System.Drawing.Drawing2D.PixelOffsetMode.HighQuality;
            g.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.High;
            g.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.HighQuality;
            g.CompositingQuality = System.Drawing.Drawing2D.CompositingQuality.HighQuality;

            //源圖片寬和高
            int imgWidth = img.Width;
            int imgHeight = img.Height;

            //繪制微縮圖
            g.DrawImage(img, new System.Drawing.Rectangle(0, 0, width, height), new System.Drawing.Rectangle(0, 0, imgWidth, imgHeight)
                        , GraphicsUnit.Pixel);

            ImageFormat format = img.RawFormat;
            ImageCodecInfo info = ImageCodecInfo.GetImageEncoders().SingleOrDefault(i => i.FormatID == format.Guid);
            EncoderParameter param = new EncoderParameter(System.Drawing.Imaging.Encoder.Quality, 100L);
            EncoderParameters parameters = new EncoderParameters(1);
            parameters.Param[0] = param;
            img.Dispose();

            //保存已生成微缩图，这里将GIF格式转化成png格式。  
            if (format == ImageFormat.Gif)
            {
                destPath = destPath.ToLower().Replace(".gif", ".png");
                bmp.Save(destPath, ImageFormat.Png);
            }
            else
            {
                if (info != null)
                {
                    bmp.Save(destPath, info, parameters);
                }
                else
                {

                    bmp.Save(destPath, format);
                }
            }

            img.Dispose();
            g.Dispose();
            bmp.Dispose();

        }

        private void button6_Click(object sender, EventArgs e)
        {
            //為圖片生成縮略圖
            //讀取圖檔, 多一層Image結構
            string filename = @"C:\______test_files\picture1.jpg";
            Image image = Image.FromFile(filename);

            Image image2 = GetThumbnail(image, image.Width / 2, image.Height / 2);

            pictureBox1.Image = image2;
        }

        /// 為圖片生成縮略圖
        /// 原圖片的路徑
        /// 縮略圖寬
        /// 縮略圖高
        /// 
        public Image GetThumbnail(Image image, int width, int height)
        {
            Bitmap bmp = new Bitmap(width, height);
            //從Bitmap創建一個Graphics
            Graphics gr = Graphics.FromImage(bmp);
            //設置 
            gr.SmoothingMode = SmoothingMode.HighQuality;
            //下面這個也設成高質量
            gr.CompositingQuality = CompositingQuality.HighQuality;
            //下面這個設成High
            gr.InterpolationMode = InterpolationMode.HighQualityBicubic;
            //把原始圖像繪制成上面所設置寬高的縮小圖
            Rectangle rectDestination = new Rectangle(0, 0, width, height);

            gr.DrawImage(image, rectDestination, 0, 0, image.Width, image.Height, GraphicsUnit.Pixel);
            return bmp;

        }

        const int HEIGHT = 190;
        const int WIDTH = 190;
        private void button7_Click(object sender, EventArgs e)
        {
            //生成高品質小空間的縮略圖
            //生成高品質小空間的縮略圖
            string filename = @"C:\______test_files\elephant.jpg";
            string foldername = Application.StartupPath;
            SetThumbnail_1(filename, foldername);
            SetThumbnail_2(filename, foldername);
            SetThumbnail_3(filename, foldername);
        }

        static void SetThumbnail_1(string filename, string foldername)
        {
            using (Bitmap source = new Bitmap(filename))
            {
                // return the source image if it's smaller than the designated thumbnail   
                int wi, hi;
                wi = WIDTH;
                hi = HEIGHT;
                // maintain the aspect ratio despite the thumbnail size parameters   
                if (source.Width > source.Height)
                {
                    wi = WIDTH;
                    hi = (int)(source.Height * ((decimal)WIDTH / source.Width));
                }
                else
                {
                    hi = HEIGHT;
                    wi = (int)(source.Width * ((decimal)HEIGHT / source.Height));
                }
                using (Image thumb = source.GetThumbnailImage(wi, hi, null, IntPtr.Zero))
                {
                    string targetPath = Path.Combine(foldername, "th_1.jpg");
                    thumb.Save(targetPath);
                }
            }
        }

        static void SetThumbnail_2(string filename, string foldername)
        {
            using (Bitmap source = new Bitmap(filename))
            {
                // return the source image if it's smaller than the designated thumbnail   
                int wi, hi;
                wi = WIDTH;
                hi = HEIGHT;
                // maintain the aspect ratio despite the thumbnail size parameters   
                if (source.Width > source.Height)
                {
                    wi = WIDTH;
                    hi = (int)(source.Height * ((decimal)WIDTH / source.Width));
                }
                else
                {
                    hi = HEIGHT;
                    wi = (int)(source.Width * ((decimal)HEIGHT / source.Height));
                }
                // original code that creates lousy thumbnails   
                // System.Drawing.Image ret = source.GetThumbnailImage(wi,hi,null,IntPtr.Zero);   
                using (System.Drawing.Bitmap thumb = new Bitmap(wi, hi))
                {
                    using (Graphics g = Graphics.FromImage(thumb))
                    {
                        g.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.HighQualityBicubic;
                        g.FillRectangle(Brushes.White, 0, 0, wi, hi);
                        g.DrawImage(source, 0, 0, wi, hi);
                    }
                    string targetPath = Path.Combine(foldername, "th_2.jpg");
                    thumb.Save(targetPath);
                }
            }
        }

        static void SetThumbnail_3(string filename, string foldername)
        {
            //Configure JPEG Compression Engine   
            System.Drawing.Imaging.EncoderParameters encoderParams = new System.Drawing.Imaging.EncoderParameters();
            long[] quality = new long[1];
            quality[0] = 75;
            System.Drawing.Imaging.EncoderParameter encoderParam = new System.Drawing.Imaging.EncoderParameter(System.Drawing.Imaging.Encoder.Quality, quality);
            encoderParams.Param[0] = encoderParam;
            System.Drawing.Imaging.ImageCodecInfo[] arrayICI = System.Drawing.Imaging.ImageCodecInfo.GetImageEncoders();
            System.Drawing.Imaging.ImageCodecInfo jpegICI = null;
            for (int x = 0; x < arrayICI.Length; x++)
            {
                if (arrayICI[x].FormatDescription.Equals("JPEG"))
                {
                    jpegICI = arrayICI[x];
                    break;
                }
            }
            using (Bitmap source = new Bitmap(filename))
            {
                int wi, hi;
                wi = WIDTH;
                hi = HEIGHT;
                // maintain the aspect ratio despite the thumbnail size parameters   
                if (source.Width > source.Height)
                {
                    wi = WIDTH;
                    hi = (int)(source.Height * ((decimal)WIDTH / source.Width));
                }
                else
                {
                    hi = HEIGHT;
                    wi = (int)(source.Width * ((decimal)HEIGHT / source.Height));
                }
                // original code that creates lousy thumbnails   
                // System.Drawing.Image ret = source.GetThumbnailImage(wi,hi,null,IntPtr.Zero);   
                using (System.Drawing.Bitmap thumb = new Bitmap(wi, hi))
                {
                    using (Graphics g = Graphics.FromImage(thumb))
                    {
                        g.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.HighQualityBicubic;
                        g.FillRectangle(Brushes.White, 0, 0, wi, hi);
                        g.DrawImage(source, 0, 0, wi, hi);
                    }
                    string targetPath = Path.Combine(foldername, "th_3.jpg");
                    thumb.Save(targetPath, jpegICI, encoderParams);
                }
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //用GetThumbnailImage製作小圖

            string filename = @"C:\______test_files\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            pictureBox1.Image = bitmap1;


            Bitmap bitmap2 = (Bitmap)bitmap1.GetThumbnailImage(bitmap1.Width / 3, bitmap1.Height / 3, null, IntPtr.Zero);
            pictureBox1.Image = bitmap2;

            //自動檔名 與 存檔語法
            string filename2 = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

            try
            {
                //bitmap1.Save(@file1, ImageFormat.Jpeg);
                bitmap2.Save(filename2, ImageFormat.Bmp);
                //bitmap1.Save(@file3, ImageFormat.Png);

                //richTextBox1.Text += "已存檔 : " + file1 + "\n";
                richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                //richTextBox1.Text += "已存檔 : " + file3 + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }

        }
    }
}
