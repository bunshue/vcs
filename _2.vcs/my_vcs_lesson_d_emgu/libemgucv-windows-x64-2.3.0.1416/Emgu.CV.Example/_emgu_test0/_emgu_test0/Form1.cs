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

namespace _emgu_test0
{
    public partial class Form1 : Form
    {
        int W = 305;
        int H = 400;

        string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

        Emgu.CV.UI.ImageBox ibox = new Emgu.CV.UI.ImageBox();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
            clear_all();
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point(200, 10);
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 12;
            y_st = 40;
            dx = 130;
            dy = 50;

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
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            pictureBox1.Size = new Size(W + 10, H + 10);
            pictureBox2.Size = new Size(W + 10, H + 10);
            pictureBox3.Size = new Size(W + 10, H + 10);
            pictureBox4.Size = new Size(W + 10, H + 10);
            imageBox1.Size = new Size(W * 2 / 3, H * 2 / 3);
            imageBox1.SizeMode = PictureBoxSizeMode.Zoom;
            ibox.Size = new Size(W + 10, H + 10);
            richTextBox1.Size = new Size(W + 10, H + 10);

            int dxx = W + 15 + 20;
            int dyy = H + 15 + 40;
            pictureBox1.Location = new Point(x_st + dx * 2 + dxx * 0, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 2 + dxx * 1, y_st + dy * 0);

            ibox.SizeMode = PictureBoxSizeMode.Normal;
            ibox.Location = new Point(x_st + dx * 2 + dxx * 2, y_st + dy * 0);
            this.Controls.Add(ibox);

            pictureBox3.Location = new Point(x_st + dx * 2 + dxx * 0, y_st + dy * 0 + dyy);
            pictureBox4.Location = new Point(x_st + dx * 2 + dxx * 1, y_st + dy * 0 + dyy);
            richTextBox1.Location = new Point(x_st + dx * 2 + dxx * 2, y_st + dy * 0 + dyy);

            label1.Location = new Point(pictureBox1.Location.X, pictureBox1.Location.Y - 30);
            label2.Location = new Point(pictureBox2.Location.X, pictureBox2.Location.Y - 30);
            label3.Location = new Point(pictureBox3.Location.X, pictureBox3.Location.Y - 30);
            label4.Location = new Point(pictureBox4.Location.X, pictureBox4.Location.Y - 30);
            label5.Location = new Point(ibox.Location.X, ibox.Location.Y - 30);

            imageBox1.Location = new Point(x_st + dx * 0 + dxx * 0, y_st + dy * 11);
            imageBox1.BackColor = Color.Pink;
        }

        void clear_all()
        {
            label1.Text = "";
            label2.Text = "";
            label3.Text = "";
            label4.Text = "";
            label5.Text = "";
            pictureBox1.Image = null;
            pictureBox2.Image = null;
            pictureBox3.Image = null;
            pictureBox4.Image = null;
            richTextBox1.Clear();
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            clear_all();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            clear_all();
            richTextBox1.Text += "用OpenCV開啟一個圖檔\t開啟cvShowImage\n";

            //EmguCV 影像格式 Image<Bgr, Byte>: a wrapper to IplImage of OpenCV
            Image<Bgr, Byte> image = new Image<Bgr, byte>(filename);
            if (image != null)
            {
                //CvInvoke.cvShowImage("使用cvShowImage開啟一圖", image);   //same
                CvInvoke.cvShowImage("使用cvShowImage開啟一圖", image.Ptr);
            }

            /*
            //same
            pictureBox1.Load(filename);
            Image<Bgr, Byte> image2 = new Image<Bgr, Byte>((Bitmap)(pictureBox1.Image));
            CvInvoke.cvShowImage("Image<Bgr, Byte>", image2);
            */
        }

        private void button1_Click(object sender, EventArgs e)
        {
            clear_all();
            richTextBox1.Text += "建立一張灰階圖到Image裏\n";
            label1.Text = "建立一張灰階圖到Image裏";
            Image<Gray, Byte> img1 = new Image<Gray, Byte>(W, H);
            pictureBox1.Image = img1.ToBitmap();

            richTextBox1.Text += "建立一張藍色彩圖到Image裏\n";
            label2.Text += "建立一張藍色彩圖到Image裏";
            Image<Bgr, Byte> img2 = new Image<Bgr, Byte>(W, H, new Bgr(255, 0, 0));
            pictureBox2.Image = img2.ToBitmap();

            richTextBox1.Text += "開啟一圖檔到Image裏\n";
            label3.Text += "開啟一圖檔到Image裏";
            Image<Bgr, Byte> img3 = new Image<Bgr, Byte>(filename);
            pictureBox3.Image = img3.ToBitmap();

            richTextBox1.Text += "開啟一圖檔到Bitmap裏, 再轉到Image裏\n";
            label4.Text += "開啟一圖檔到Bitmap裏, 再轉到Image裏";
            Bitmap bmp = new Bitmap(filename);
            Image<Bgr, Byte> img4 = new Image<Bgr, Byte>(bmp);
            pictureBox4.Image = img4.ToBitmap();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            clear_all();
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
            clear_all();
            richTextBox1.Text += "對Image結構進行操作\n";
            //Image<TColor, TDepth>还对操作运算符进行了重载（ + - * / ）

            Image<Bgr, byte> img1 = new Image<Bgr, byte>(480, 320, new Bgr(255, 0, 0));
            Image<Bgr, byte> img2 = new Image<Bgr, byte>(480, 320, new Bgr(0, 255, 0));
            Image<Bgr, byte> img3 = new Image<Bgr, byte>(480, 320, new Bgr(0, 0, 255));

            Image<Bgr, byte> img4 = img1 + img2 + img3;

            pictureBox1.Image = img1.ToBitmap();
            pictureBox2.Image = img2.ToBitmap();
            pictureBox3.Image = img3.ToBitmap();
            pictureBox4.Image = img4.ToBitmap();
            label1.Text = "img1 (255,0,0)";
            label2.Text = "img2 (0,255,0)";
            label3.Text = "img3 (0,0,255)";
            label4.Text = "img4 = img1 + img2 + img3";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            clear_all();
            richTextBox1.Text += "開啟一圖檔到Image裏\n";
            Image<Bgr, Byte> img1 = new Image<Bgr, Byte>(filename);
            pictureBox1.Image = img1.ToBitmap();
            label1.Text = "原圖";

            Image<Bgr, Byte> img2 = img1.Not();     //Not函數, 讓圖片反色
            pictureBox2.Image = img2.ToBitmap();
            label2.Text = "Not函數, 讓圖片反色";

            //same sugar可用、kilo不可用
            //Image<Bgr, Byte> img3 = img1.Convert<byte>(delegate(Byte b) { return (Byte)(255 - b); });
            //pictureBox3.Image = img1.ToBitmap();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            clear_all();
            //Martix的使用与Image类似

            Matrix<Single> matrix = new Matrix<Single>(480, 320);

            float f = matrix[100, 100];
            float df = matrix.Data[100, 100];

            //不知道怎麼轉成bitmap, 顯示在picturebox裏

        }

        private void button6_Click(object sender, EventArgs e)
        {
            clear_all();
            richTextBox1.Text += "圖片轉向\n";

            Image<Bgr, Byte> img1 = new Image<Bgr, Byte>(filename);
            pictureBox1.Image = img1.ToBitmap();
            label1.Text = "原圖";

            Image<Bgr, Byte> img2 = img1.Flip(FLIP.HORIZONTAL);
            pictureBox2.Image = img2.ToBitmap();
            label2.Text = "左右相反";

            Image<Bgr, Byte> img3 = img1.Flip(FLIP.VERTICAL);
            pictureBox3.Image = img3.ToBitmap();
            label3.Text = "上下顛倒";

            Image<Bgr, Byte> img4 = img1.Flip(FLIP.HORIZONTAL).Flip(FLIP.VERTICAL);
            pictureBox4.Image = img4.ToBitmap();
            label4.Text = "左右相反 + 上下顛倒";

        }

        private void button7_Click(object sender, EventArgs e)
        {
            clear_all();
            richTextBox1.Text += "讀取圖片檔案\n";
            //string filename = @"D:\_git\vcs\_1.data\______test_files1\pic_256X100.jpg";
            string filename = @"D:\_git\vcs\_1.data\______test_files1\pic_256X100b.bmp";

            //Load the Image
            Image<Bgr, Byte> img1 = new Image<Bgr, byte>(filename);

            pictureBox1.Image = img1.ToBitmap();
            label1.Text = "原圖";
            Application.DoEvents();

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
        }

        private void button8_Click(object sender, EventArgs e)
        {
            clear_all();
            //灰階
            richTextBox1.Text += "開啟一圖檔到Image裏\n";
            Image<Bgr, Byte> img = new Image<Bgr, Byte>(filename);
            pictureBox1.Image = img.ToBitmap();
            label1.Text = "原圖";

            //灰階, 需要 opencv_imgproc231.dll
            Image<Gray, Byte> gray = img.Convert<Gray, Byte>().PyrDown().PyrUp();
            pictureBox2.Image = gray.ToBitmap();
            label2.Text = "轉灰階";
        }



        private void button9_Click(object sender, EventArgs e)
        {
            clear_all();

            richTextBox1.Text += "讀圖片檔案至記憶體(Bitmap結構)\n";
            Bitmap bmp = new Bitmap(filename);

            richTextBox1.Text += "Bitmap 轉成 Image\n";
            Image<Bgr, Byte> image = new Image<Bgr, Byte>(bmp);
            image.Save("file1.bmp");
            pictureBox1.Image = image.ToBitmap();
            label1.Text = "原圖 Bitmap 轉成 Image";

            richTextBox1.Text += "Image(RGB) 轉成 Image(Gray), 彩色轉成灰階\n";
            Image<Gray, Byte> gimage = image.Convert<Gray, Byte>();
            gimage.Save("file2.bmp");
            pictureBox2.Image = gimage.ToBitmap();
            label2.Text = "彩色轉成灰階";

            richTextBox1.Text += "灰階轉成彩色\n";
            Image<Rgb, Byte> newimage = gimage.Convert<Rgb, Byte>();
            newimage.Save("file3.bmp");
            pictureBox3.Image = newimage.ToBitmap();
            label3.Text = "灰階轉成彩色";

            richTextBox1.Text += "Image 轉成 Bitmap\n";
            Bitmap result = image.ToBitmap();
            result.Save("file4.bmp");
            pictureBox4.Image = result;
            label4.Text = "Image 轉成 Bitmap";
        }

        private void button10_Click(object sender, EventArgs e)
        {
            clear_all();
            //使用ImageBox
            Bitmap bmp = new Bitmap(filename);

            //Bitmap 轉成 Image
            Image<Bgr, Byte> image = new Image<Bgr, Byte>(bmp);

            pictureBox1.Image = image.ToBitmap();
            label1.Text += "用pictureBox顯示圖片";

            ibox.Image = image;
            label5.Text += "用ImageBox顯示圖片";
        }

        private void button11_Click(object sender, EventArgs e)
        {
            clear_all();
            //Image<Gray, Byte> image = new Image<Gray, Byte>(new Size(640, 480));    //灰階 黑圖
            //                                                          B    G  R
            Image<Bgr, Byte> image = new Image<Bgr, Byte>(W, H, new Bgr(255, 0, 0));    //彩圖，指明顏色

            //寫字
            MCvFont f = new MCvFont(FONT.CV_FONT_HERSHEY_TRIPLEX, 1.0, 1.0);            //寫字
            //image.Draw("用Image製作一圖，並在其上寫字", ref f, new Point(10, 80), new Bgr(0, 0, 0));      //寫字
            image.Draw("Good Morning !", ref f, new Point(20, 80), new Bgr(0, 0, 0));      //寫字，只能用英文

            pictureBox1.Image = image.ToBitmap();
        }

        private void button12_Click(object sender, EventArgs e)
        {
            String win1 = "Test Window"; //The name of the window
            CvInvoke.cvNamedWindow(win1); //Create the window using the specific name
            Image<Bgr, Byte> img = new Image<Bgr, byte>(400, 200, new Bgr(255, 0, 0)); //Create an image of 400x200 of Blue color
            MCvFont font = new MCvFont(FONT.CV_FONT_HERSHEY_COMPLEX, 1.0, 1.0); //Create the font

            img.Draw("Hello, world", ref font, new Point(10, 80), new Bgr(0, 255, 0)); //Draw "Hello, world." on the image using the specific font

            CvInvoke.cvShowImage(win1, img); //Show the image
            CvInvoke.cvWaitKey(0);  //Wait for the key pressing event
            CvInvoke.cvDestroyWindow(win1); //Destory the window
        }

        private void button13_Click(object sender, EventArgs e)
        {
            clear_all();
            richTextBox1.Text += "讀圖片檔案至記憶體(Bitmap結構)\n";
            Bitmap bmp = new Bitmap(filename);

            richTextBox1.Text += "Bitmap 轉成 Image\n";
            Image<Bgr, Byte> image = new Image<Bgr, Byte>(bmp);

            Image<Gray, Byte> grayFrame = image.Convert<Gray, Byte>();      //彩色轉灰階
            Image<Gray, Byte> smallGrayFrame = grayFrame.PyrDown();
            Image<Gray, Byte> smoothedGrayFrame = smallGrayFrame.PyrUp();
            Image<Gray, Byte> cannyFrame = smoothedGrayFrame.Canny(new Gray(100), new Gray(60));

            // 把畫面轉換成bitmap型態，再丟給pictureBox元件
            ibox.Image = image; //原圖
            pictureBox1.Image = grayFrame.ToBitmap();   //灰階
            pictureBox2.Image = smallGrayFrame.ToBitmap();   //smallGrayFrame
            pictureBox3.Image = smoothedGrayFrame.ToBitmap();   //smoothedGrayFrame
            pictureBox4.Image = cannyFrame.ToBitmap();   //cannyFrame

            label1.Text += "灰階";
            label2.Text += "smallGrayFrame";
            label3.Text += "smoothedGrayFrame";
            label4.Text += "cannyFrame";
            label5.Text += "原圖";
        }

        private void button14_Click(object sender, EventArgs e)
        {
            clear_all();
            //圖片內容相減
            richTextBox1.Text += "對Image結構進行操作 圖片內容相減\n";
            //Image<TColor, TDepth>还对操作运算符进行了重载（ + - * / ）

            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\compare\compare1.jpg";
            string filename2 = @"D:\_git\vcs\_1.data\______test_files1\compare\compare2.jpg";

            Image<Bgr, Byte> image1 = new Image<Bgr, byte>(filename1);
            Image<Bgr, Byte> image2 = new Image<Bgr, byte>(filename2);
            Image<Bgr, Byte> image_diff = image1 - image2;

            pictureBox1.Image = image1.ToBitmap();
            pictureBox2.Image = image2.ToBitmap();
            pictureBox3.Image = image_diff.ToBitmap();
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //使用ImageBox
            Bitmap bmp = new Bitmap(filename);

            //Bitmap 轉成 Image
            Image<Bgr, Byte> image = new Image<Bgr, Byte>(bmp);
            imageBox1.Image = image;
        }

        private void button16_Click(object sender, EventArgs e)
        {
            CvInvoke.cvDestroyWindow("使用cvShowImage開啟一圖");   //關閉剛剛開啟的CV視窗
        }
    }
}

/*
            Bitmap bmp = new Bitmap(filename);

            //傳檔名或傳Bitmap都可以
            Image<Bgr, Byte> img1 = new Image<Bgr, Byte>(bmp);
            Image<Bgr, Byte> img2 = new Image<Bgr, Byte>(filename); //same


*/
