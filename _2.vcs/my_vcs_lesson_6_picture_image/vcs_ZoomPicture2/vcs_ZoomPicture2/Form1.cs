using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ZoomPicture2
{
    public partial class Form1 : Form
    {
        public class ImageResize
        {
            public static Bitmap Resize(Bitmap originImage, Double times)
            {
                int width = Convert.ToInt32(originImage.Width * times);
                int height = Convert.ToInt32(originImage.Height * times);

                return Process(originImage, originImage.Width, originImage.Height, width, height);
            }

            private static Bitmap Process(Bitmap originImage, int oriwidth, int oriheight, int width, int height)
            {
                Bitmap resizedbitmap = new Bitmap(width, height);
                Graphics g = Graphics.FromImage(resizedbitmap);
                g.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.High;
                g.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.HighQuality;
                g.Clear(Color.Transparent);
                g.DrawImage(originImage, new Rectangle(0, 0, width, height), new Rectangle(0, 0, oriwidth, oriheight), GraphicsUnit.Pixel);
                return resizedbitmap;
            }
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = Image.FromFile("c:\\______test_files\\picture1.jpg"); //載入圖檔，由檔案
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1;
            Bitmap bitmap2;

            bitmap1 = new Bitmap("c:\\______test_files\\picture1.jpg");
            bitmap2 = ImageResize.Resize(bitmap1, 2);


            pictureBox1.Image = bitmap2;
        }

        bool do_image_size_change = false;
        private void hScrollBar1_Scroll(object sender, ScrollEventArgs e)
        {
            //影像檔大小縮放
            if (do_image_size_change == true)
            {
                //richTextBox1.Text += "處理中~~~~ abort\n";
            }

            do_image_size_change = true;

            Bitmap bitmap1;
            Bitmap bitmap2;

            bitmap1 = new Bitmap("c:\\______test_files\\picture1.jpg");
            bitmap2 = ImageResize.Resize(bitmap1, hScrollBar1.Value / 10);


            pictureBox1.Image = bitmap2;


            do_image_size_change = false;

        }

    }
}
