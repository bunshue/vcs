using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;

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
    }
}

