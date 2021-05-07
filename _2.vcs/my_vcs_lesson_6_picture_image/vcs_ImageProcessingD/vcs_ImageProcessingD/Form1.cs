using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   // ColorMatrix
using System.Drawing.Drawing2D; // Matrix

namespace vcs_ImageProcessingD
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";
            pictureBox1.Image = Image.FromFile(filename);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            pictureBox2.Image = ConvertToGrayscale(pictureBox1.Image);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            pictureBox2.Image = ConvertToGrayscale_CM(pictureBox1.Image);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            pictureBox2.Image = ConvertToTransparency(pictureBox1.Image);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            pictureBox2.Image = ConvertToRotate(pictureBox1.Image);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            pictureBox2.Image = ImageAddText(pictureBox1.Image);
        }

        public Bitmap ConvertToGrayscale(Image image) // Image 是抽象基底類別
        {
            Bitmap source = (Bitmap)image;  // Image 是 Bitmap 的父類別
            Bitmap dest = new Bitmap(source.Width, source.Height); //新增一樣寬高的點陣圖物件

            for (int y = 0; y < dest.Height; y++)
            {
                for (int x = 0; x < dest.Width; x++)
                {
                    Color c = source.GetPixel(x, y); // 得到 原始像素 的 Color
                    int luma = (int)(c.R * 0.3 + c.G * 0.6 + c.B * 0.1);  // 以 3:6:1 的比例得到設定值
                    dest.SetPixel(x, y, Color.FromArgb(luma, luma, luma)); // 寫入 像素値
                }
            }
            return dest;
        }

        // 使用色彩矩陣來調整影像色彩
        public Bitmap ConvertToGrayscale_CM(Image image)
        {
            Bitmap dest = new Bitmap(image.Width, image.Height);
            Graphics g = Graphics.FromImage(dest); // 從點陣圖 建立 新的畫布

            // 定義含有 RGBA 空間座標的 5 x 5 矩陣
            // (R, G, B, A, 1) 乘上 此矩陣
            ColorMatrix cm = new ColorMatrix(
                   new float[][]{ new float[]{0.3f, 0.3f, 0.3f, 0, 0},
                                  new float[]{0.6f, 0.6f, 0.6f, 0, 0},
                                  new float[]{0.1f, 0.1f, 0.1f, 0, 0},
                                  new float[]{  0,    0,    0,  1, 0},
                                  new float[]{  0,    0,    0,  0, 1}});

            // ImageAttributes 類別的多個方法會使用色彩矩陣來調整影像色彩
            ImageAttributes ia = new ImageAttributes();

            // 設定預設分類的色彩調整矩陣。
            ia.SetColorMatrix(cm);
            g.DrawImage(image, new Rectangle(0, 0, image.Width, image.Height), 0, 0, image.Width, image.Height, GraphicsUnit.Pixel, ia);
            g.Dispose();

            return dest;
        }

        public Bitmap ConvertToTransparency(Image image)
        {
            Bitmap dest = new Bitmap(image.Width, image.Height);
            Graphics g = Graphics.FromImage(dest);

            ImageAttributes ia = new ImageAttributes();

            ColorMatrix cm = new ColorMatrix();

            cm.Matrix33 = 0.5f; // 透明度

            ia.SetColorMatrix(cm);

            g.DrawImage(image, new Rectangle(0, 0, image.Width, image.Height), 0, 0, image.Width, image.Height, GraphicsUnit.Pixel, ia);
            g.Dispose();

            return dest;
        }

        public Bitmap ConvertToRotate(Image image)
        {
            Bitmap dest = new Bitmap(image.Width, image.Height);
            Graphics g = Graphics.FromImage(dest);

            Matrix mx = new Matrix();

            mx.Rotate(30);
            g.Transform = mx;

            g.DrawImage(image, new Rectangle(0, 0, image.Width, image.Height));

            g.Dispose();

            return dest;
        }

        public Bitmap ImageAddText(Image image)
        {
            Bitmap dest = new Bitmap(image.Width, image.Height);
            Graphics g = Graphics.FromImage(dest);
            Font f = new Font("標楷體", 40);

            g.DrawImage(image, new Rectangle(0, 0, image.Width, image.Height));
            g.DrawString("牡丹亭", f, Brushes.Red, 130, 20, StringFormat.GenericTypographic);
            g.Dispose();

            return dest;
        }
    }
}
