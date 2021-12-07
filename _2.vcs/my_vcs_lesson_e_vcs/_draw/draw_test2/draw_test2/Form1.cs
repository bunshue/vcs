using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;

namespace draw_test2
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

        private void button0_Click(object sender, EventArgs e)
        {
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
                    richTextBox1.Text += "已存檔 : " + filename + "\n";
                    //richTextBox1.Text += "已存檔 : " + file3 + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
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

        //C#獲取圖片的指定部分
        /// <summary>
        /// 獲取圖片指定部分
        /// </summary>
        /// <param name="filename">圖片路徑</param>
        /// <param name="sx">原始圖片開始截取處的坐標X值</param>
        /// <param name="sy">原始圖片開始截取處的坐標Y值</param>
        /// <param name="sWidth">原始圖片的寬度</param>
        /// <param name="sHeight">原始圖片的高度</param>
        /// <param name="dx">目標圖片開始繪制處的坐標X值(通常為0)</param>
        /// <param name="dy">目標圖片開始繪制處的坐標Y值(通常為0)</param>
        /// <param name="dWidth">目標圖片的寬度</param>
        /// <param name="dHeight">目標圖片的高度</param>
        static Bitmap GetPart(string filename, int sx, int sy, int sWidth, int sHeight, int dx, int dy, int dWidth, int dHeight)
        {
            Image image = Image.FromFile(filename);

            Bitmap bitmap1 = new Bitmap(dWidth, dHeight);
            Graphics g = Graphics.FromImage(bitmap1);
            Rectangle rec1 = new Rectangle(new Point(sx, sy), new Size(sWidth, sHeight));//原圖位置
            Rectangle rec2 = new Rectangle(new Point(dx, dy), new Size(dWidth, dHeight));//目標位置

            g.DrawImage(image, rec2, rec1, GraphicsUnit.Pixel);

            return bitmap1;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //取得圖片的一部分

            string filename = @"C:\______test_files\picture1.jpg";

            int sx = 0;
            int sy = 0;
            int sWidth = 305 / 2;
            int sHeight = 400 / 2;
            int dx = 0;
            int dy = 0;
            int dWidth = 305 / 1;
            int dHeight = 400 / 1;

            Bitmap bitmap1 = GetPart(filename, sx, sy, sWidth, sHeight, dx, dy, dWidth, dHeight);
            pictureBox1.Image = bitmap1;

        }

        private void button2_Click(object sender, EventArgs e)
        {

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
