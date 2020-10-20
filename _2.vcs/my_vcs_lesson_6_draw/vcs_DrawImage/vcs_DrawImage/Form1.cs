using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_DrawImage
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox_old.Image = Image.FromFile("c:\\______test_files\\picture1.jpg"); //載入圖檔，由檔案

            p = new Pen(Color.Red, 3);

            //指定畫布大小
            pictureBox1.Width = 710;
            pictureBox1.Height = 700;
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.DrawRectangle(p, 0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1);
            pictureBox1.Image = bitmap1;


            /*
            // Create image.
            Image newImage = Image.FromFile("SampImag.jpg");

            // Create coordinates for upper-left corner of image.
            float x = 100.0F;
            float y = 100.0F;

            // Create rectangle for source image.
            RectangleF srcRect = new RectangleF(50.0F, 50.0F, 150.0F, 150.0F);
            GraphicsUnit units = GraphicsUnit.Pixel;
            */
            // Draw image to screen.
            //    e.Graphics.DrawImage(newImage, x, y, srcRect, units);


        }

        private void button1_Click(object sender, EventArgs e)
        {
            Image img = Image.FromFile("c:\\______test_files\\picture1.jpg"); //載入圖檔，由檔案

            Bitmap bmp = new Bitmap("c:\\______test_files\\picture1.jpg");
            //Bitmap bitmap2 = new Bitmap("c:\\______test_files\\picture1.jpg");

            richTextBox1.Text += "W1 = " + img.Width.ToString() + " H1 = " + img.Height.ToString() + "\n";
            richTextBox1.Text += "W2 = " + bmp.Width.ToString() + " H2 = " + bmp.Height.ToString() + "\n";

            //將圖２貼到圖１左上角
            //Graphics g = Graphics.FromImage(bitmap1);   //以記憶體圖像 bitmap1 建立 記憶體畫布g
            //g.DrawImage(bitmap1, 0, 0);
            //g.DrawImage(bitmap1, 200, 200);
            g.DrawImage(bmp, 400, 400);
            g.DrawImage(img, 0, 0);
            //g.DrawImage(bitmap1, 0, 0);
            //g.DrawImage(bitmap1, 0, 0);




            g.DrawString("aaaaaa", new Font("Arial", 80), Brushes.Red, new PointF(300, 100));



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

    }
}
