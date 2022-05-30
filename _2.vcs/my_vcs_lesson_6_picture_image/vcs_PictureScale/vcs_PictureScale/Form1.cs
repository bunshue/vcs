using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for PixelOffsetMode

namespace vcs_PictureScale
{
    public partial class Form1 : Form
    {
        string filename = "C:\\______test_files\\__RW\\_png\\scale16X16.png";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Bitmap bitmap1 = new Bitmap(filename);
            pictureBox1.Image = bitmap1; //顯示在 pictureBox1 圖片控制項中
            pictureBox2.Image = bitmap1; //顯示在 pictureBox1 圖片控制項中
            label1.Text = "原圖 " + pictureBox1.Image.Width.ToString() + " X " + pictureBox1.Image.Height.ToString();
            label2.Text = "放大 " + pictureBox2.Image.Width.ToString() + " X " + pictureBox2.Image.Height.ToString();
        }

        // Return a scaled version of the input image.
        private Bitmap MakeScaledImage(Image image, float scale_x, float scale_y, PixelOffsetMode mode)
        {
            int W = (int)(scale_x * image.Width);
            int H = (int)(scale_y * image.Height);
            Bitmap bm = new Bitmap(W, H);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.Clear(Color.Yellow);
                Rectangle src_rect = new Rectangle(0, 0, image.Width, image.Height);
                Rectangle dest_rect = new Rectangle(0, 0, W, H);
                gr.PixelOffsetMode = mode;
                gr.InterpolationMode = InterpolationMode.NearestNeighbor;
                gr.DrawImage(image, dest_rect, src_rect, GraphicsUnit.Pixel);
            }
            return bm;
        }

        float ratio_x = 1.0f;
        float ratio_y = 1.0f;
        private void timer1_Tick(object sender, EventArgs e)
        {
            ratio_x += 0.1f;
            ratio_y += 0.1f;

            if (ratio_x > 15.0f)
                timer1.Enabled = false;
            if (ratio_y > 15.0f)
                timer1.Enabled = false;

            PixelOffsetMode mode = PixelOffsetMode.HighQuality;

            // Make the scaled image.
            pictureBox2.Image = MakeScaledImage(pictureBox1.Image, ratio_x, ratio_y, mode);

            label1.Text = "原圖 " + pictureBox1.Image.Width.ToString() + " X " + pictureBox1.Image.Height.ToString();
            label2.Text = "放大 " + pictureBox2.Image.Width.ToString() + " X " + pictureBox2.Image.Height.ToString();
            //richTextBox1.Text += ratio_x.ToString() + "\t" + ratio_y.ToString() + "\n";

            Application.DoEvents();

        }
    }
}

