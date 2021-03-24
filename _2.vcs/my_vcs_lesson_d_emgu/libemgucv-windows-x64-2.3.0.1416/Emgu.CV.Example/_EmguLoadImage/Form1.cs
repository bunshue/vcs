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

namespace _EmguLoadImage
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
            IntPtr inputImage = CvInvoke.cvLoadImage(filename, LOAD_IMAGE_TYPE.CV_LOAD_IMAGE_COLOR);
            CvInvoke.cvShowImage("IntPtr", inputImage);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Image<Bgr, Byte> inputImage = new Image<Bgr, byte>(filename);
            CvInvoke.cvShowImage("Image<Bgr, Byte>", inputImage);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Image<Gray, Byte> inputImage = new Image<Gray, byte>(filename);
            CvInvoke.cvShowImage("Image<Gray, Byte>", inputImage);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            pictureBox1.Load(filename);
            Image<Bgr, Byte> inputImage = new Image<Bgr, Byte>((Bitmap)(pictureBox1.Image));
            CvInvoke.cvShowImage("Image<Bgr, Byte>", inputImage);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            Image<Gray, Byte> inputImage = new Image<Gray, byte>(new Size(640, 480));
            pictureBox1.Image = inputImage.ToBitmap();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            Image<Bgr, Byte> inputImage = new Image<Bgr, byte>(640, 480, new Bgr(255, 0, 255));
            pictureBox1.Image = inputImage.ToBitmap();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            Bitmap bmp = new Bitmap(filename);
            System.Drawing.Imaging.BitmapData bd;
            bd = bmp.LockBits(new Rectangle(0, 0, bmp.Width, bmp.Height),
                              System.Drawing.Imaging.ImageLockMode.ReadWrite,
                              System.Drawing.Imaging.PixelFormat.Format24bppRgb);
            Image<Bgr, Byte> inputImage = new Image<Bgr, Byte>(bd.Width, bd.Height, bd.Stride, bd.Scan0);
            pictureBox1.Image = inputImage.ToBitmap();
            bmp.UnlockBits(bd);
        }
    }
}

