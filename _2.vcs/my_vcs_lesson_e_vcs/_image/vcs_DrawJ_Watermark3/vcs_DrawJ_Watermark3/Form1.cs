using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;
using System.Drawing.Drawing2D;
using System.IO;

//C#圖片加水印

namespace vcs_DrawJ_Watermark3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //讀取圖檔, 多一層Image結構
            string filename = @"C:\______test_files\picture1.jpg";
            Image image = Image.FromFile(filename);
            pictureBox1.Image = image;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //讀取圖檔, 多一層Image結構
            string filename = @"C:\______test_files\picture1.jpg";
            Image image = Image.FromFile(filename);

            image = AddTextToImg(image, "牡丹亭");

            pictureBox1.Image = image;
        }

        //圖片加水印
        public static Image AddTextToImg(Image image, string text)
        {
            Bitmap bitmap = new Bitmap(image, image.Width, image.Height);
            Graphics g = Graphics.FromImage(bitmap);

            float fontSize = 12.0f; //字體大小
            float textWidth = text.Length * fontSize; //文本的長度
            //下面定義一個矩形區域，以後在這個矩形裡畫上白底黑字
            float rectX = 0;
            float rectY = 0;
            float rectWidth = text.Length * (fontSize + 8);
            float rectHeight = fontSize + 8;
            //聲明矩形域
            RectangleF textArea = new RectangleF(rectX, rectY, rectWidth, rectHeight);

            Font font = new Font("宋體", fontSize); //定義字體
            Brush whiteBrush = new SolidBrush(Color.White); //白筆刷，畫文字用
            Brush blackBrush = new SolidBrush(Color.Black); //黑筆刷，畫背景用

            g.FillRectangle(blackBrush, rectX, rectY, rectWidth, rectHeight);

            g.DrawString(text, font, whiteBrush, textArea);
            MemoryStream ms = new MemoryStream();
            //保存為Jpg類型
            bitmap.Save(ms, ImageFormat.Jpeg);

            Image h_hovercImg = Image.FromStream(ms);

            g.Dispose();
            bitmap.Dispose();
            return h_hovercImg;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            pictureBox1.Image.Dispose();

            //調用方法：命名空間.類名.AddWaterText(picpath, "Tandy Tang - 博客園", picpath, 255, 18);
            string filename1 = @"C:\______test_files\picture1.jpg";
            string filename2 = @"C:\______test_files\picture1add.jpg";
            string text = "牡丹亭";
            int alpha = 255;
            int fontsize = 30;

            AddWaterText(filename1, filename2, text, alpha, fontsize);
        }

        /// <summary>
        /// 圖片加水印文字
        /// </summary>
        /// <param name="oldpath">舊圖片地址</param>
        /// <param name="newpath">新圖片地址</param>
        /// <param name="text">水印文字</param>
        /// <param name="Alpha">透明度</param>
        /// <param name="fontsize">字體大小</param>
        void AddWaterText(string oldpath, string newpath, string text, int Alpha, int fontsize)
        {
            try
            {
                text = text + "版權所有";
                FileStream fs = new FileStream(oldpath, FileMode.Open);
                BinaryReader br = new BinaryReader(fs);
                byte[] bytes = br.ReadBytes((int)fs.Length);
                br.Close();
                fs.Close();
                MemoryStream ms = new MemoryStream(bytes);

                Image imgPhoto = Image.FromStream(ms);
                int imgPhotoWidth = imgPhoto.Width;
                int imgPhotoHeight = imgPhoto.Height;

                Bitmap bitmap1 = new Bitmap(imgPhotoWidth, imgPhotoHeight, PixelFormat.Format24bppRgb);

                bitmap1.SetResolution(72, 72);
                Graphics g = Graphics.FromImage(bitmap1);
                //gif背景色
                g.Clear(Color.FromName("white"));
                g.InterpolationMode = InterpolationMode.High;
                g.SmoothingMode = SmoothingMode.HighQuality;
                g.DrawImage(imgPhoto, new Rectangle(0, 0, imgPhotoWidth, imgPhotoHeight), 0, 0, imgPhotoWidth, imgPhotoHeight, GraphicsUnit.Pixel);
                Font font = null;
                SizeF crSize = new SizeF();
                font = new Font("宋體", fontsize, FontStyle.Bold);
                //測量指定區域 www.2cto.com
                crSize = g.MeasureString(text, font);
                float y = imgPhotoHeight - crSize.Height;
                float x = imgPhotoWidth - crSize.Width;
                StringFormat StrFormat = new StringFormat();
                StrFormat.Alignment = StringAlignment.Center;

                //畫兩次制造透明效果
                SolidBrush semiTransBrush2 = new SolidBrush(Color.FromArgb(Alpha, 56, 56, 56));
                g.DrawString(text, font, semiTransBrush2, x + 1, y + 1);

                g.DrawRectangle(Pens.Red, 10, 10, 100, 100);

                SolidBrush semiTransBrush = new SolidBrush(Color.FromArgb(Alpha, 176, 176, 176));
                g.DrawString(text, font, semiTransBrush, x, y);
                bitmap1.Save(newpath, ImageFormat.Jpeg);
                //g.Dispose();
                imgPhoto.Dispose();
                pictureBox1.Image = bitmap1;
                //bitmap1.Dispose();
            }
            catch
            {
                ;
            }
        }


    }
}
