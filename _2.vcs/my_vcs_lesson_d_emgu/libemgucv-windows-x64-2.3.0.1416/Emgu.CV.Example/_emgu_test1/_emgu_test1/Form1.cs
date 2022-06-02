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
using Emgu.CV.CvEnum;

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
            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 180;
            dy = 53;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            button10.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            button11.Location = new Point(x_st + dx * 0, y_st + dy * 11);
        }

        //用EMGU播放檔案 需要 opencv_ffmpeg_64.dll
        private void button0_Click(object sender, EventArgs e)
        {
            //string filename = "F:\\Naval Legends Yamato  World of Warships.mp4";
            string filename = @"D:\\Carreno Busta vs Kei Nishikori Final Set Tie Break HD.mp4";
            //string filename = @"C:\______test_files\_video\i2c.avi";

            //Capture cap2 = null;
            Capture cap2 = new Capture(filename);

            double W;
            double H;
            double frame_count;
            double fps;

            W = cap2.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FRAME_WIDTH);
            H = cap2.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FRAME_HEIGHT);
            frame_count = cap2.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FRAME_COUNT);
            fps = cap2.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FPS);

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

            W = cap2.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FRAME_WIDTH);
            H = cap2.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FRAME_HEIGHT);
            frame_count = cap2.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FRAME_COUNT);
            fps = cap2.GetCaptureProperty(CAP_PROP.CV_CAP_PROP_FPS);

            richTextBox1.Text += "FRAME_WIDTH = " + W.ToString() + "\n";
            richTextBox1.Text += "FRAME_HEIGHT = " + H.ToString() + "\n";
            richTextBox1.Text += "FRAME_COUNT = " + frame_count.ToString() + "\n";
            richTextBox1.Text += "FPS = " + fps.ToString() + "\n";

            Image<Bgr, Byte> image = cap2.QueryFrame();
            pictureBox1.Image = image.ToBitmap();
        }

        private void button1_Click(object sender, EventArgs e)
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
            Image<Bgr, Byte> img2 = img1.Flip(FLIP.HORIZONTAL);
            pictureBox2.Image = img2.ToBitmap();

            Image<Bgr, Byte> img3 = img1.Flip(FLIP.VERTICAL);
            pictureBox3.Image = img3.ToBitmap();

            Image<Bgr, Byte> img4 = img1.Flip(FLIP.HORIZONTAL).Flip(FLIP.VERTICAL);
            pictureBox4.Image = img4.ToBitmap();
            */
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //圖片轉影片
            Image<Bgr, Byte> img;

            string filenamej;

            string filename = Application.StartupPath + "\\avi_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".avi";

            VideoWriter video = new VideoWriter(filename, CvInvoke.CV_FOURCC('X', 'V', 'I', 'D'), 1, 640, 480, true);

            filenamej = @"C:\______test_files\__pic\_MU\id_card_01.jpg";
            pictureBox1.Image = Image.FromFile(filenamej);
            img = new Image<Bgr, byte>(filenamej);
            video.WriteFrame<Bgr, byte>(img); //將每張圖片製作成影片
            Application.DoEvents();
            System.Threading.Thread.Sleep(1000);

            filenamej = @"C:\______test_files\__pic\_MU\id_card_02.jpg";
            pictureBox1.Image = Image.FromFile(filenamej);
            img = new Image<Bgr, byte>(filenamej);
            video.WriteFrame<Bgr, byte>(img); //將每張圖片製作成影片
            Application.DoEvents();
            System.Threading.Thread.Sleep(1000);

            filenamej = @"C:\______test_files\__pic\_MU\id_card_03.jpg";
            pictureBox1.Image = Image.FromFile(filenamej);
            img = new Image<Bgr, byte>(filenamej);
            video.WriteFrame<Bgr, byte>(img); //將每張圖片製作成影片
            Application.DoEvents();
            System.Threading.Thread.Sleep(1000);

            filenamej = @"C:\______test_files\__pic\_MU\id_card_04.jpg";
            pictureBox1.Image = Image.FromFile(filenamej);
            img = new Image<Bgr, byte>(filenamej);
            video.WriteFrame<Bgr, byte>(img); //將每張圖片製作成影片
            Application.DoEvents();
            System.Threading.Thread.Sleep(1000);

            filenamej = @"C:\______test_files\__pic\_MU\id_card_05.jpg";
            pictureBox1.Image = Image.FromFile(filenamej);
            img = new Image<Bgr, byte>(filenamej);
            video.WriteFrame<Bgr, byte>(img); //將每張圖片製作成影片
            Application.DoEvents();
            System.Threading.Thread.Sleep(1000);

            video.Dispose();

            richTextBox1.Text += "圖片轉影片, 完成\n";

        }

        private void button3_Click(object sender, EventArgs e)
        {
            Image<Bgr, Byte> image = new Image<Bgr, byte>(320, 400);      ////初始化一圖, 無背景色, 就是黑色
            //Image<Bgr, Byte> image = new Image<Bgr, byte>(320, 400, new Bgr(255, 0, 0));    //初始化一圖, 給定背景色, 藍色
            MCvFont font = new MCvFont(FONT.CV_FONT_HERSHEY_DUPLEX, 0.8d, 0.8d);
            image.Draw("Write on imageBox", ref font, new Point(20, 40), new Bgr(Color.Red));
            imageBox1.Image = image;

            /*
            image1.Source = ToBitmapSource(image);  //video player??
            */

        }

        private void button4_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";

            //Load the Image
            Image<Bgr, Byte> image = new Image<Bgr, byte>(filename);

            Point[] points = new Point[10];
            Random r = new Random();
            int i;
            for (i = 0; i < 10; i++)
            {
                points[i] = new Point(r.Next(300), r.Next(400));
            }

            Bgr bgr = new Bgr(Color.Red);
            MCvFont font = new MCvFont(FONT.CV_FONT_HERSHEY_PLAIN, 0.8, 0.8);

            int count = 1;
            foreach (PointF point in points)
            {
                //畫圓形
                image.Draw(new CircleF(point, 4), bgr, 2);
                Point p = new Point((int)Math.Round(point.X), (int)Math.Round(point.Y));

                //畫字
                image.Draw(count.ToString(), ref font, new Point(p.X + 5, p.Y - 5), bgr);
                count++;
            }

            //畫長方形
            image.Draw(new Rectangle(50, 50, 100, 100), new Bgr(Color.LawnGreen), 2);

            LineSegment2D line1 = new LineSegment2D(new Point(100, 0), new Point(200, 150));
            LineSegment2D line2 = new LineSegment2D(new Point(200, 150), new Point(150, 300));

            //畫線
            image.Draw(line1, new Bgr(Color.Red), 1);
            image.Draw(line2, new Bgr(Color.Blue), 1);

            Double angle = 0;
            angle = (line1.GetExteriorAngleDegree(line2));//* (180.0 / Math.PI) );

            MCvFont font2 = new MCvFont(FONT.CV_FONT_HERSHEY_COMPLEX, 0.6, 0.6);
            image.Draw(angle.ToString(), ref font2, new Point(50, 50), new Bgr(0, 0, 0));



            //Display the Image
            pictureBox1.Image = image.ToBitmap();

        }

        private void button5_Click(object sender, EventArgs e)
        {
            CvInvoke.cvNamedWindow("AAAAAAAAAA");

            //Create an image of 400x200 of Blue color
            using (Image<Bgr, Byte> img = new Image<Bgr, byte>(400, 200, new Bgr(255, 0, 0)))
            {
                //Create the font
                MCvFont font = new MCvFont(FONT.CV_FONT_HERSHEY_COMPLEX, 1.0, 1.0);
                //Draw "Hello, world." on the image using the specific font
                img.Draw("Hello, world", ref font, new Point(10, 80), new Bgr(0, 255, 0));

                img.Draw(new CircleF(new PointF(150, 50), 50), new Bgr(Color.Pink), 2);

                CvInvoke.cvCircle(img,
                  new Point(50, 50),
                  20,
                  new MCvScalar(0, 0, 255),
                  -1,
                  LINE_TYPE.CV_AA,
                  0);

                PointF p = new PointF(120, 120);

                CircleF c = new CircleF(p, 100);
                img.Draw(c, new Bgr(Color.Orange), 3);

                //Show the image
                CvInvoke.cvShowImage("AAAAAAAAAA", img.Ptr);
                //Wait for the key pressing event
                CvInvoke.cvWaitKey(0);
                //Destory the window
                CvInvoke.cvDestroyWindow("AAAAAAAAAA");
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            MCvFont font = new MCvFont(FONT.CV_FONT_HERSHEY_DUPLEX, 2d, 2d);
            Image<Bgr, Byte> image = new Image<Bgr, byte>(300, 300);
            FontFamily ff = new FontFamily("Courier New");
            Font f = new Font(ff, 50, FontStyle.Italic);

            image.Draw("ABCDEFG".ToString(), ref font, new Point(32, 55), new Bgr(Color.Red));


            imageBox1.Image = image;
        }

        private void button7_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";

            Image<Bgr, Byte> image = new Image<Bgr, Byte>(filename);

            MCvFont font = new MCvFont(FONT.CV_FONT_HERSHEY_SIMPLEX, 0.8f, 0.8f);
            MCvScalar color = new MCvScalar(255, 255, 255);

            CvInvoke.cvPutText(image, "New File", new Point(10, 20), ref font, color);  //無效

            image.Draw("ABCDEFG".ToString(), ref font, new Point(32, 55), new Bgr(Color.Red));

            image.Save("aaaaa.jpg"); //另存新圖

            imageBox1.Image = image;

        }

        private void button8_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式

            Image<Bgr, Byte> image = new Image<Bgr, Byte>(bitmap1);

            imageBox1.Image = image;
        }

        private void button9_Click(object sender, EventArgs e)
        {


            string filename = @"C:\______test_files\_emgu\pic3.png";

            //Load the image from file and resize it for display
            Image<Bgr, Byte> Image = new Image<Bgr, byte>(filename).Resize(400, 400, Emgu.CV.CvEnum.INTER.CV_INTER_LINEAR, true);


            imageBox1.Image = Image;

        }

        private void button10_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式

            Image<Bgr, Byte> Image = new Image<Bgr, Byte>(bitmap1);

            imageBox1.Image = Image;

        }

        private void button11_Click(object sender, EventArgs e)
        {

        }
    }
}

