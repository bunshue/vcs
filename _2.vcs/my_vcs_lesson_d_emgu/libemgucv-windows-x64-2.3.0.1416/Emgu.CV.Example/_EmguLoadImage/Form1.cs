using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.Threading;

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
            richTextBox1.Text += "��OpenCV�}�Ҥ@�ӹ���\n";
            IntPtr inputImage = CvInvoke.cvLoadImage(filename, LOAD_IMAGE_TYPE.CV_LOAD_IMAGE_COLOR);
            CvInvoke.cvShowImage("IntPtr", inputImage);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "��OpenCV�}�Ҥ@�ӹ���\n";
            //EmguCV �v���榡 Image<Bgr, Byte>: a wrapper to IplImage of OpenCV
            Image<Bgr, Byte> inputImage = new Image<Bgr, byte>(filename);
            CvInvoke.cvShowImage("Image<Bgr, Byte>", inputImage);

            //same
            /*
            pictureBox1.Load(filename);
            Image<Bgr, Byte> inputImage2 = new Image<Bgr, Byte>((Bitmap)(pictureBox1.Image));
            CvInvoke.cvShowImage("Image<Bgr, Byte>", inputImage2);
            */
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "��OpenCV�}�Ҥ@�ӹ��ɡA���ন�Ƕ��v���榡\n";
            //EmguCV �v���榡 Image<Gray, Byte>: �ŧi�@��EmguCV�Ƕ��v���榡
            Image<Gray, Byte> inputImage = new Image<Gray, byte>(filename);     //�m��|�۰���Ƕ�
            CvInvoke.cvShowImage("Image<Gray, Byte>", inputImage);
            //���اP�_, �����۰ʱN��J�m�⪺�Ӥ��ন�Ƕ�

            //same
            /*
            pictureBox1.Load(filename);
            Image<Gray, Byte> inputImage2 = new Image<Gray, Byte>((Bitmap)(pictureBox1.Image));
            CvInvoke.cvShowImage("Image<Bgr, Byte>", inputImage2);
            */
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "�NPictureBox.Image�૬Bitmpap�ᵹImage\n";
            //��JPictureBox Ū�J�v��, �NPictureBox.Image�૬Bitmpap�ᵹImage<Bgr, Byte>
            pictureBox1.Load(filename);
            Image<Bgr, Byte> inputImage = new Image<Bgr, Byte>((Bitmap)(pictureBox1.Image));
            CvInvoke.cvShowImage("Image<Bgr, Byte>", inputImage);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "�}�Ҥ@�i�Ū��v��(�©�), �j�p�� 640 X 480\n";
            Image<Gray, Byte> inputImage = new Image<Gray, byte>(new Size(640, 480));
            pictureBox1.Image = inputImage.ToBitmap();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "�ۤv�w�q�@���v���j�p�M������, �j�p�� 640 X 480\n";
            Image<Bgr, Byte> inputImage = new Image<Bgr, byte>(640, 480, new Bgr(255, 0, 255)); //�۩w�q�C��
            //Image<Bgr, Byte> inputImage2 = new Image<Bgr, byte>(new Size(640, 480));    //�¦�

            pictureBox1.Image = inputImage.ToBitmap();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "�Q��BitmapŪ�J�@�i�Ϥ�, �öǵ�Image<Bgr, Byte>�v���榡\n";
            Bitmap bmp = new Bitmap(filename);
            System.Drawing.Imaging.BitmapData bd;
            bd = bmp.LockBits(new Rectangle(0, 0, bmp.Width, bmp.Height),
                              System.Drawing.Imaging.ImageLockMode.ReadWrite,
                              System.Drawing.Imaging.PixelFormat.Format24bppRgb);
            Image<Bgr, Byte> inputImage = new Image<Bgr, Byte>(bd.Width, bd.Height, bd.Stride, bd.Scan0);
            pictureBox1.Image = inputImage.ToBitmap();
            bmp.UnlockBits(bd);
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //�Ƕ�0->255
            for (int i = 0; i < 256; i++)
            {
                Image<Gray, Byte> inputImage = new Image<Gray, byte>(640, 480, new Gray(i));
                pictureBox1.Image = inputImage.ToBitmap();
                this.Text = i.ToString();
                Application.DoEvents();
                Thread.Sleep(10);
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {

        }
    }
}
