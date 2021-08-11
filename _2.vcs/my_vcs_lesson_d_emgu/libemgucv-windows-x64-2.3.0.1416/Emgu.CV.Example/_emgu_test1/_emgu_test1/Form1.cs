using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using Emgu.CV;
using Emgu.CV.Structure;

/*
重建EMGU專案  x64
1. 參考/加入參考/ EMGU那3個
2. 加入/現有項目/opencv那3個, 屬性選 "有更新時才複製"
3. .csproj的PlatformTarget的x86改成x64
*/

namespace _emgu_test1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        //用EMGU播放檔案 需要 opencv_ffmpeg_64.dll
        private void button1_Click(object sender, EventArgs e)
        {
            //string filename = "F:\\Naval Legends Yamato  World of Warships.mp4";
            string filename = @"D:\\Carreno Busta vs Kei Nishikori Final Set Tie Break HD.mp4";
            //string filename = @"C:\______test_files\__RW\_avi\i2c.avi";

            //Capture cap2 = null;
            Capture cap2 = new Capture(filename);

            double W;
            double H;
            double frame_count;
            double fps;

            W = cap2.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FRAME_WIDTH);
            H = cap2.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FRAME_HEIGHT);
            frame_count = cap2.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FRAME_COUNT);
            fps = cap2.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FPS);

            richTextBox1.Text += "FRAME_WIDTH = " + W.ToString() + "\n";
            richTextBox1.Text += "FRAME_HEIGHT = " + H.ToString() + "\n";
            richTextBox1.Text += "FRAME_COUNT = " + frame_count.ToString() + "\n";
            richTextBox1.Text += "FPS = " + fps.ToString() + "\n";

            double sec = frame_count / fps;
            if (sec > 60)
                richTextBox1.Text += "duration = " + ((int)(sec / 60)).ToString() + " 分 " + (sec % 60).ToString() + " 秒\n";
            else
                richTextBox1.Text += "duration = " + sec.ToString() + " 秒\n";

            /*
            //test
            Image<Bgr, Byte> image = cap2.QueryFrame();
            pictureBox1.Image = image.ToBitmap();
            */


            filename = @"C:\______test_files\picture1.jpg";
            cap2 = new Capture(filename);

            W = cap2.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FRAME_WIDTH);
            H = cap2.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FRAME_HEIGHT);
            frame_count = cap2.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FRAME_COUNT);
            fps = cap2.GetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FPS);

            richTextBox1.Text += "FRAME_WIDTH = " + W.ToString() + "\n";
            richTextBox1.Text += "FRAME_HEIGHT = " + H.ToString() + "\n";
            richTextBox1.Text += "FRAME_COUNT = " + frame_count.ToString() + "\n";
            richTextBox1.Text += "FPS = " + fps.ToString() + "\n";

            Image<Bgr, Byte> image = cap2.QueryFrame();
            pictureBox1.Image = image.ToBitmap();


        }

        private void button2_Click(object sender, EventArgs e)
        {
            //Image<Gray, int> inputImage = new Image<Gray, byte>(new Size(640, 480));
            //pictureBox1.Image = inputImage.ToBitmap();




            //string filename = @"C:\______test_files\pic_256X100.jpg";
            string filename = @"C:\______test_files\pic_256X100b.bmp";

            //Load the Image
            Image<Bgr, Byte> img1 = new Image<Bgr, byte>(filename);

            //Display the Image
            pictureBox1.Image = img1.ToBitmap();

            int W = img1.Bitmap.Width;
            int H = img1.Bitmap.Height;
            int len = img1.Bytes.Length;


            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";
            richTextBox1.Text += "Length = " + len.ToString() + "\n";
            richTextBox1.Text += "W = " + img1.Size.Width.ToString() + ", H = " + img1.Size.Height.ToString() + "\n";
            richTextBox1.Text += "W = " + img1.Width.ToString() + ", H = " + img1.Height.ToString() + "\n";
            richTextBox1.Text += "cols = " + img1.Cols.ToString() + ", rows = " + img1.Rows.ToString() + "\n";

            int i;
            for (i = 0; i < img1.Bytes.Length / 100; i++)
            {
                richTextBox1.Text += img1.Bytes[i].ToString() + " ";
            }


            //不能直接修改數值 ?!?!
            for (i = 0; i < 500; i++)
            {
                //img1.Bytes[i] = (byte)(((int)img1.Bytes[i] + (int)img1.Bytes[i + 1] + (int)img1.Bytes[i + 2]) / 3);
                img1.Bytes[i] = 0;
            }


            pictureBox1.Image = img1.ToBitmap();

            richTextBox1.Text += "\n\n";

            for (i = 0; i < img1.Bytes.Length / 100; i++)
            {
                richTextBox1.Text += img1.Bytes[i].ToString() + " ";
            }



            /*
            Image<Bgr, Byte> img2 = img1.Flip(Emgu.CV.CvEnum.FLIP.HORIZONTAL);
            pictureBox2.Image = img2.ToBitmap();

            Image<Bgr, Byte> img3 = img1.Flip(Emgu.CV.CvEnum.FLIP.VERTICAL);
            pictureBox3.Image = img3.ToBitmap();

            Image<Bgr, Byte> img4 = img1.Flip(Emgu.CV.CvEnum.FLIP.HORIZONTAL).Flip(Emgu.CV.CvEnum.FLIP.VERTICAL);
            pictureBox4.Image = img4.ToBitmap();
            */


        }
    }
}
