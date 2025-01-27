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

//C#圖片加水印

namespace vcs_Draw_Watermark1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_reset_Click(sender, e);
        }

        private void bt_reset_Click(object sender, EventArgs e)
        {
            //讀取圖檔, 多一層Image結構
            string filename1 = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Image image = Image.FromFile(filename1);

            pictureBox1.Image = image;

            string filename2 = @"C:\_git\vcs\_1.data\______test_files1\_material\ims-small-logo.png";
            pictureBox2.Image = Image.FromFile(filename2);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //讀取圖檔, 多一層Image結構
            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Image image = Image.FromFile(filename);

            image = AddTextToImg(image, "牡丹亭");

            pictureBox1.Image = image;
        }

        //圖片加水印
        public static Image AddTextToImg(Image image, string text)
        {
            Bitmap bitmap1 = new Bitmap(image, image.Width, image.Height);
            Graphics g = Graphics.FromImage(bitmap1);

            float fontSize = 12.0f; //字體大小
            float textWidth = text.Length * fontSize; //文本的長度
            //下面定義一個矩形區域，以後在這個矩形裡畫上白底黑字
            float rectX = 0;
            float rectY = 0;
            float rectWidth = text.Length * (fontSize + 8);
            float rectHeight = fontSize + 8;
            //聲明矩形域
            RectangleF textArea = new RectangleF(rectX, rectY, rectWidth, rectHeight);

            Font f = new Font("標楷體", fontSize); //定義字體
            Brush whiteBrush = new SolidBrush(Color.White); //白筆刷，畫文字用
            Brush blackBrush = new SolidBrush(Color.Black); //黑筆刷，畫背景用

            g.FillRectangle(blackBrush, rectX, rectY, rectWidth, rectHeight);

            g.DrawString(text, f, whiteBrush, textArea);
            MemoryStream ms = new MemoryStream();
            //保存為Jpg類型
            bitmap1.Save(ms, ImageFormat.Jpeg);

            Image h_hovercImg = Image.FromStream(ms);

            g.Dispose();
            bitmap1.Dispose();
            return h_hovercImg;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            pictureBox1.Image.Dispose();

            string filename1 = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            string filename2 = @"C:\_git\vcs\_1.data\______test_files1\picture1add.jpg";
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

        private void button3_Click(object sender, EventArgs e)
        {
            Graphics g = this.pictureBox1.CreateGraphics();
            addWatermarkText1(g, 10, "lion-mouse", "WM_TOP_LEFT", 150, 150);
        }

        static void addWatermarkText1(Graphics g, int fontsize, string _watermarkText, string _watermarkPosition, int _width, int _height)
        {
            int[] sizes = new int[] { 32, 14, 12, 10, 8, 6, 4 };
            Font crFont = null;
            SizeF crSize = new SizeF();

            crFont = new Font("微軟雅黑", fontsize, FontStyle.Bold);
            crSize = g.MeasureString(_watermarkText, crFont);

            float xpos = 0;
            float ypos = 0;
            Color color = Color.Firebrick;

            switch (_watermarkPosition)
            {
                case "WM_TOP_LEFT":
                    xpos = ((float)_width * (float).01) + (crSize.Width / 2);
                    ypos = (float)_height * (float).01;
                    break;
                case "WM_TOP_RIGHT":
                    xpos = ((float)_width * (float).99) - (crSize.Width / 2);
                    ypos = (float)_height * (float).01;
                    break;
                case "WM_BOTTOM_RIGHT":
                    xpos = ((float)_width * (float).99) - (crSize.Width / 2);
                    ypos = ((float)_height * (float).99) - crSize.Height;
                    break;
                case "WM_BOTTOM_LEFT":
                    xpos = ((float)_width * (float).01) + (crSize.Width / 2);
                    ypos = ((float)_height * (float).99) - crSize.Height;
                    break;
            }

            StringFormat StrFormat = new StringFormat();
            StrFormat.Alignment = StringAlignment.Center;
            SolidBrush semiTransBrush2 = new SolidBrush(Color.FromArgb(153, 0, 0, 0));//加陰影
            g.DrawString(_watermarkText, crFont, semiTransBrush2, xpos + 1, ypos + 1, StrFormat);

            SolidBrush semiTransBrush = new SolidBrush(color);  //添加水印
            g.DrawString(_watermarkText, crFont, semiTransBrush, xpos, ypos, StrFormat);

            semiTransBrush2.Dispose();
            semiTransBrush.Dispose();
        }

        static void addWatermarkText2(Graphics g, string type, int fontsize, string _watermarkText)
        {
            //1、先畫矩形
            RectangleF drawRect;
            Color color;
            if (type == "Top")
            {
                drawRect = new RectangleF(73, 135, 450, 64);
                //color = Color.FromArgb(255, 255, 255);
                color = Color.Red;
            }
            else
            {
                drawRect = new RectangleF(194, 245, 250, 39);
                //color = Color.FromArgb(244, 226, 38);
                color = Color.Pink;
            }

            //2、在基於矩形畫水印文字
            Font crFont = null;

            StringFormat StrFormat = new StringFormat();
            StrFormat.Alignment = StringAlignment.Center;

            crFont = new Font("微軟雅黑", fontsize, FontStyle.Bold);
            SolidBrush semiTransBrush = new SolidBrush(color);  //添加水印
            g.DrawString(_watermarkText, crFont, semiTransBrush, drawRect, StrFormat);

            semiTransBrush.Dispose();
        }

        /*       和第一種方法比起來，第二種方法更直觀，更短小精悍，只需要在你需要添加水印的圖片上計算好固定坐標然後先畫一個矩形，然後把水印漢字畫在矩形內，這樣不管水印漢字如何變化都可以在圖片固定位置居中。
        */


        private void button4_Click(object sender, EventArgs e)
        {
            Graphics g = this.pictureBox1.CreateGraphics();
            addWatermarkText2(g, "Top", 20, "mouse");
        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = new Bitmap(pictureBox1.Image);

            using (Bitmap watermark_bm = new Bitmap(pictureBox2.Image))
            {
                int x = (bitmap1.Width - watermark_bm.Width) / 2;
                int y = (bitmap1.Height - watermark_bm.Height) / 2;
                DrawWatermark1(watermark_bm, bitmap1, x, y);
            }

            pictureBox1.Image = bitmap1;
        }

        // Copy the watermark image over the result image.
        private void DrawWatermark1(Bitmap bitmap1, Bitmap result_bm, int x, int y)
        {
            const byte ALPHA = 128;
            // Set the watermark's pixels' Alpha components.
            Color clr;
            for (int py = 0; py < bitmap1.Height; py++)
            {
                for (int px = 0; px < bitmap1.Width; px++)
                {
                    clr = bitmap1.GetPixel(px, py);
                    bitmap1.SetPixel(px, py, Color.FromArgb(ALPHA, clr.R, clr.G, clr.B));
                }
            }

            // Set the watermark's transparent color.
            bitmap1.MakeTransparent(bitmap1.GetPixel(0, 0));

            // Copy onto the result image.
            using (Graphics g = Graphics.FromImage(result_bm))
            {
                g.DrawImage(bitmap1, x, y);
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = new Bitmap(pictureBox1.Image);

            using (Bitmap bitmap2 = new Bitmap(pictureBox2.Image))
            {
                int x = (bitmap1.Width - bitmap2.Width) / 2;
                int y = (bitmap1.Height - bitmap2.Height) / 2;
                DrawWatermark2(bitmap2, bitmap1, x, y);
            }

            pictureBox1.Image = bitmap1;
        }

        // Copy the watermark image over the result image.
        private void DrawWatermark2(Bitmap bitmap1, Bitmap result_bm, int x, int y)
        {
            // Make a ColorMatrix that multiplies
            // the alpha component by 0.5.
            ColorMatrix color_matrix = new ColorMatrix();
            color_matrix.Matrix33 = 0.5f;

            // Make an ImageAttributes that uses the ColorMatrix.
            ImageAttributes image_attributes = new ImageAttributes();
            image_attributes.SetColorMatrices(color_matrix, null);

            // Make pixels that are the same color as the
            // one in the upper left transparent.
            bitmap1.MakeTransparent(bitmap1.GetPixel(0, 0));

            // Draw the image using the ColorMatrix.
            using (Graphics g = Graphics.FromImage(result_bm))
            {
                Rectangle rect = new Rectangle(x, y, bitmap1.Width, bitmap1.Height);
                g.DrawImage(bitmap1, rect, 0, 0, bitmap1.Width, bitmap1.Height, GraphicsUnit.Pixel, image_attributes);
            }
        }
    }
}


