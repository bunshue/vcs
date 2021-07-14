using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for InterpolationMode

namespace vcs_PictureResize4
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
            Image image = Image.FromFile(filename);
            pictureBox1.Image = image;


            int value = trackBar1.Value;

            richTextBox1.Text += "放大倍率 : " + (value * 100 / 10).ToString() + " %\n";


            int W1 = image.Width;
            int H1 = image.Height;

            int W2 = W1 * value / 10;
            int H2 = H1 * value / 10;

            Size new_size = new Size(W2, H2);
            pictureBox2.Image = ResizeImage(image, new_size);



        }

        /// <summary>
        ///  圖片寬高設定 
        /// </summary>
        /// <param name="imgToResize"></param>
        /// <param name="size"></param>
        /// <returns></returns>
        public Image ResizeImage(Image img_old, Size size)
        {
            int W1 = img_old.Width;
            int H1 = img_old.Height;
            int W2 = size.Width;
            int H2 = size.Height;

            float nPercent = 0;
            float nPercentW = 0;
            float nPercentH = 0;

            //計算寬度的縮放比例
            nPercentW = ((float)W2 / (float)W1);
            //計算高度的縮放比例
            nPercentH = ((float)H2 / (float)H1);

            if (nPercentH < nPercentW)
                nPercent = nPercentH;
            else
                nPercent = nPercentW;

            //期望的寬度
            int W3 = (int)(W1 * nPercent);
            //期望的高度
            int H3 = (int)(H1 * nPercent);

            Bitmap b = new Bitmap(W3, H3);
            Graphics g = Graphics.FromImage((Image)b);
            g.InterpolationMode = InterpolationMode.HighQualityBicubic;
            //繪製圖像
            g.DrawImage(img_old, 0, 0, W3, H3);
            g.Dispose();

            richTextBox1.Text += "W1 = " + W1.ToString() + ", H1 = " + H1.ToString() + "\n";
            richTextBox1.Text += "W2 = " + W2.ToString() + ", H2 = " + H2.ToString() + "\n";
            richTextBox1.Text += "W3 = " + W3.ToString() + ", H3 = " + H3.ToString() + "\n";
            richTextBox1.Text += "PW = " + nPercentW.ToString() + ", PH = " + nPercentH.ToString() + ", P = " + nPercent.ToString() + "\n";

            return (Image)b;
        }


        private void trackBar1_Scroll(object sender, EventArgs e)
        {

        }

        private void trackBar1_MouseDown(object sender, MouseEventArgs e)
        {

        }

        private void trackBar1_MouseUp(object sender, MouseEventArgs e)
        {
            int value = trackBar1.Value;

            richTextBox1.Text += "放大倍率 : " + (value * 100 / 10).ToString() + " %\n";


            string filename = @"C:\______test_files\picture1.jpg";
            Image image = Image.FromFile(filename);

            int W1 = image.Width;
            int H1 = image.Height;

            int W2 = W1 * value / 10;
            int H2 = H1 * value / 10;

            Size new_size = new Size(W2, H2);
            pictureBox2.Image = ResizeImage(image, new_size);



        }
    }
}
