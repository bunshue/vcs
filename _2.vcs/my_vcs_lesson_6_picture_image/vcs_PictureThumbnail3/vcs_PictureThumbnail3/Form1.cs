using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;

/*
以下是五种生成缩略图的模式：

1、自动缩放：如果需要生成缩略图的宽度比高度大，那么效果跟第二种模式产生的效果一样；如果宽度比高度小，则效果跟第三种模式产生的效果一样。

2、指定宽高按比例：这种模式下，宽度即为需要生成的图片宽度，高度为需要生成的缩略图的宽度与原图宽度的比再乘以需要生成的缩略图的高度。

3、指定高宽按比例：这种模式证号和第二种模式相反，高度一定，宽度乘以比值。

4、指定高宽缩放：按照指定的尺寸生成缩略图。

5、指定高宽裁剪：指定高，把两边的宽裁剪掉。
*/

namespace vcs_PictureThumbnail3
{
    public partial class Form1 : Form
    {
        string filename1 = @"C:\______test_files1\picture1.jpg";
        string filename2 = @"picture1_thumbnail.jpg";

        public enum MakeThumbnailMode
        {
            Auto,//自動裁剪模式
            W,//指定寬，高按比例
            H, //指定高，寬按比例
            HW,//指定高，寬縮放
            Cut//指定寬，高裁剪
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename1);	//Bitmap.FromFile出來的是Image格式
            pictureBox1.Image = bitmap1;

            textBox1.Text = filename1;
            textBox2.Text = Application.StartupPath + "\\" + filename2;
            radioButton1.Text = "auto : 自動裁剪模式";
            radioButton2.Text = "W : 指定寬，高按比例";
            radioButton3.Text = "H : 指定高，寬按比例";
            radioButton4.Text = "HW : 指定高，寬縮放";
            radioButton5.Text = "Cut : 指定寬，高裁剪";
        }

        static Bitmap getThumBitmap(Image originalImage, int width, int height, MakeThumbnailMode mode, out Graphics graphics)
        {
            Bitmap bitmap;
            int thumbWidth = width;
            int thumbHeight = height;
            int x = 0;
            int y = 0;
            int originalWidth = originalImage.Width;
            int originalHeight = originalImage.Height;
            if (mode == MakeThumbnailMode.Auto)
            {
                if (thumbWidth > thumbHeight)
                {
                    mode = MakeThumbnailMode.W;
                }
                else
                {
                    mode = MakeThumbnailMode.H;
                }

            }
            if (originalHeight < thumbHeight && originalWidth < thumbWidth)
            {
                thumbWidth = originalWidth;
                thumbHeight = originalHeight;
            }
            switch (mode)
            {
                case MakeThumbnailMode.W:
                    thumbHeight = originalHeight * width / originalWidth;
                    break;
                case MakeThumbnailMode.H:
                    thumbWidth = originalWidth * height / originalHeight;
                    break;
                case MakeThumbnailMode.HW:
                    break;
                case MakeThumbnailMode.Cut:
                    if ((double)originalWidth / (double)originalHeight > (double)width / (double)height)
                    {
                        originalHeight = originalImage.Height;
                        originalWidth = width * originalHeight / height;
                        y = 0;
                        x = (originalWidth - width) / 2;

                    }
                    else
                    {
                        originalWidth = originalImage.Width;
                        originalHeight = height * originalWidth / width;
                        x = 0;
                        y = (originalHeight - height) / 2;
                    }
                    break;
            }
            bitmap = new Bitmap(thumbWidth, thumbHeight);
            bitmap.MakeTransparent(Color.Transparent);
            graphics = Graphics.FromImage(bitmap);
            graphics.Clear(Color.Transparent);
            graphics.DrawImage(originalImage, new Rectangle(0, 0, thumbWidth, thumbHeight), new Rectangle(x, y, originalWidth, originalHeight), GraphicsUnit.Pixel);
            //bitmap.Save("aaaaa.jpg", ImageFormat.Jpeg);
            return bitmap;
        }

        void MakeThumbPic(string originalImagePath, string thumbnailPath, int width, int height, MakeThumbnailMode mode, ImageFormat imageFormat)
        {
            using (Image image = Image.FromFile(originalImagePath))
            {
                Graphics graphics;
                Bitmap bitmap1 = getThumBitmap(image, width, height, mode, out graphics);

                pictureBox2.Image = bitmap1;
                
                try
                {
                    bitmap1.Save(thumbnailPath, imageFormat);

                }
                catch (Exception)
                {
                    throw;
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            MakeThumbnailMode mode = 0;
            if (radioButton1.Checked == true)
            {
                richTextBox1.Text += "你選擇了 auto : 自動裁剪模式\n";
                mode = MakeThumbnailMode.Auto;
            }
            else if (radioButton2.Checked == true)
            {
                richTextBox1.Text += "你選擇了 W : 指定寬，高按比例\n";
                mode = MakeThumbnailMode.W;
            }
            else if (radioButton3.Checked == true)
            {
                richTextBox1.Text += "你選擇了 H : 指定高，寬按比例\n";
                mode = MakeThumbnailMode.H;
            }
            else if (radioButton4.Checked == true)
            {
                richTextBox1.Text += "你選擇了 HW : 指定高，寬縮放\n";
                mode = MakeThumbnailMode.HW;
            }
            else if (radioButton5.Checked == true)
            {
                richTextBox1.Text += "你選擇了 Cut : 指定寬，高裁剪\n";
                mode = MakeThumbnailMode.Cut;
            }
            else
            {
                richTextBox1.Text += "你還未選擇裁剪模式\n";
                return;
            }


            int W = int.Parse(tb_w.Text);
            int H = int.Parse(tb_h.Text);

            MakeThumbPic(filename1, filename2, W, H, mode, ImageFormat.Jpeg);



        }
    }
}
