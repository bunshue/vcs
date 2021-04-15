using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using Emgu.CV;
using Emgu.CV.Structure;
using Emgu.Util;
using Emgu.CV.CvEnum;

namespace _emgu_test1
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\picture1.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            /*
            richTextBox1.Text += "用OpenCV開啟一個圖檔\n";
            //EmguCV 影像格式 Image<Bgr, Byte>: a wrapper to IplImage of OpenCV
            Image<Bgr, Byte> image = new Image<Bgr, byte>(filename);
            CvInvoke.cvShowImage("Image<Bgr, Byte>", image);
            */

            //same
            /*
            pictureBox1.Load(filename);
            Image<Bgr, Byte> image2 = new Image<Bgr, Byte>((Bitmap)(pictureBox1.Image));
            CvInvoke.cvShowImage("Image<Bgr, Byte>", image2);
            */

            //讀圖片檔案至記憶體
            //read image
            //Bitmap bmp = new Bitmap(@"C:\______test_files\picture1.jpg");



            /*

            //Bitmap 轉成 Image
            Image<Bgr, Byte> image = new Image<Rgb, Byte>(bmp);

            //Image(RGB) 轉成 Image(Gray), 彩色轉成灰階
            Image<Gray, Byte> gimage = image.Convert<Gray, Byte>();


            //灰階轉成彩色
            Image<Rgb, Byte> newimage = gimage.Convert<Rgb, Byte>();

            //Image 轉成 Bitmap
            Bitmap result = image.ToBitmap();

            */

            richTextBox1.Text += "建立一張灰階圖到Image裏\n";
            Image<Gray, Byte> img1 = new Image<Gray, Byte>(480, 320);

            richTextBox1.Text += "建立一張藍色彩圖到Image裏\n";
            Image<Bgr, Byte> img2 = new Image<Bgr, Byte>(480, 320, new Bgr(255, 0, 0));

            richTextBox1.Text += "開啟一圖檔到Image裏\n";
            Image<Bgr, Byte> img3 = new Image<Bgr, Byte>(filename);

            richTextBox1.Text += "開啟一圖檔到Bitmap裏, 再轉到Image裏\n";
            Bitmap bmp = new Bitmap(filename);
            Image<Bgr, Byte> img4 = new Image<Bgr, Byte>(bmp);

            pictureBox1.Image = img4.ToBitmap();
        }


        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "對像素進行直接操作\n";

            Image<Bgr, byte> img = new Image<Bgr, byte>(420, 420, new Bgr(0, 255, 0));

            //直接通过索引访问，速度较慢，返回TColor类型

            //取得像素值
            Bgr color = img[100, 100];
            richTextBox1.Text += color.Red.ToString() + " " + color.Green.ToString() + " " + color.Blue.ToString() + "\n";

            color = new Bgr(0, 0, 255); //Blue, Green, Red

            img[100, 100] = color;
            int i;

            for (i = 0; i < 200; i++)
            {
                img[50, i] = color;
                img[100, i] = color;
                img[150, i] = color;
            }

            //通过Data索引访问，速度快
            //最后一个参数为通道数，例如Bgr图片的 0：蓝色，1：绿色，2：红色，Gray的0：灰度，返回TDepth类型
            Byte blue = img.Data[100, 100, 0];
            Byte green = img.Data[100, 100, 1];
            Byte red = img.Data[100, 100, 2];

            red = 0;
            green = 0;
            blue = 255;
            for (i = 0; i < 200; i++)
            {
                img.Data[200, i, 0] = blue;
                img.Data[200, i, 1] = green;
                img.Data[200, i, 2] = red;

                img.Data[250, i, 0] = blue;
                img.Data[250, i, 1] = green;
                img.Data[250, i, 2] = red;

                img.Data[300, i, 0] = blue;
                img.Data[300, i, 1] = green;
                img.Data[300, i, 2] = red;
            }

            pictureBox1.Image = img.ToBitmap();
        }


        private void button3_Click(object sender, EventArgs e)
        {
            //Image<TColor, TDepth>还对操作运算符进行了重载（ + - * / ）

            Image<Bgr, byte> img1 = new Image<Bgr, byte>(480, 320, new Bgr(255, 0, 0));
            Image<Bgr, byte> img2 = new Image<Bgr, byte>(480, 320, new Bgr(0, 255, 0));
            Image<Bgr, byte> img3 = new Image<Bgr, byte>(480, 320, new Bgr(0, 0, 255));

            Image<Bgr, byte> img4 = img1 + img2 + img3;

            pictureBox1.Image = img4.ToBitmap();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "開啟一圖檔到Image裏\n";
            Image<Bgr, Byte> img1 = new Image<Bgr, Byte>(filename);

            Image<Bgr, byte> img2 = img1.Not();     //Not函數, 讓圖片反色

            //pictureBox1.Image = img2.ToBitmap();

            //same
            Image<Bgr, Byte> img3 = img1.Convert<byte>(delegate(Byte b) { return (Byte)(255 - b); });
            pictureBox1.Image = img1.ToBitmap();


        }

        private void button5_Click(object sender, EventArgs e)
        {
            //Martix的使用与Image类似

            Matrix<Single> matrix = new Matrix<Single>(480, 320);

            float f = matrix[100, 100];
            float df = matrix.Data[100, 100];

            //不知道怎麼轉成bitmap, 顯示在picturebox裏

        }

        private void button6_Click(object sender, EventArgs e)
        {
            Image<Bgr, byte> img = new Image<Bgr, byte>(480, 320, new Bgr(0, 255, 0));

            MCvFont f = new MCvFont(FONT.CV_FONT_HERSHEY_TRIPLEX, 1.0, 1.0);
            img.Draw("hello world", ref f, new Point(10, 80), new Bgr(0, 0, 0));
            pictureBox1.Image = img.ToBitmap();
        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        private void button10_Click(object sender, EventArgs e)
        {
        }

    }
}
