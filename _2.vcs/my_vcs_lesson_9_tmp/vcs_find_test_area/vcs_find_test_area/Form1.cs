using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for File

using System.Net;   //for WebClient

namespace vcs_find_test_area
{
    public partial class Form1 : Form
    {
        //string filename = @"C:\______test_files\_case1\\pic1.jpg";
        string filename = @"test_pic.bmp";

        
        Graphics g;
        Pen p;
        Bitmap bitmap1;

        Graphics g2;
        Pen p2;
        Bitmap bitmap2;

        public Form1()
        {
            InitializeComponent();
            //pictureBox1.SizeMode = PictureBoxSizeMode.Zoom; //圖片Zoom的方法
            //pictureBox1.SizeMode = PictureBoxSizeMode.Zoom; //圖片Zoom的方法
            //pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage; //圖片Zoom的方法
            pictureBox1.SizeMode = PictureBoxSizeMode.Normal; //圖片Zoom的方法
            //pictureBox1.ClientSize = new Size(640, 480);    //設定pictureBox的大小
            pictureBox1.BorderStyle = BorderStyle.Fixed3D;

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Image image1 = new Bitmap(filename, true);
            pictureBox1.Image = image1;

            richTextBox1.Text += "W = " + image1.Size.Width.ToString() + "  H = " + image1.Size.Height.ToString() + "\n";

            //pictureBox1.ClientSize = new Size(image1.Size.Width, image1.Size.Height);    //設定pictureBox的大小



        }

        private void button1_Click(object sender, EventArgs e)
        {
            bitmap1 = new Bitmap(filename);
            g = Graphics.FromImage(bitmap1);
            pictureBox1.Image = bitmap1;

            int i;
            int j;
            int A;
            int R;
            int G;
            int B;
            int search_size = 256;   //256X256
            int awb_block = 32;     //AWB block size width, height
            int ww = awb_block;
            int hh = awb_block;

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            int center_x = W / 2;
            int center_y = H / 2;
            int x_st = center_x - search_size / 2;
            int y_st = center_y - search_size / 2;

            for (i = 0; i <= (search_size/awb_block); i++)
            {
                g.DrawLine(new Pen(Color.Red, 1), x_st, y_st + awb_block * i, x_st + search_size - 1, y_st + awb_block * i);
                g.DrawLine(new Pen(Color.Red, 1), x_st + awb_block * i, y_st, x_st + awb_block * i, y_st + search_size - 1);
            }

            int[] saturation_array = new int[(search_size / awb_block) * (search_size / awb_block)];

            int upper_bound = 240;
            for (j = y_st; j < (y_st + search_size); j++)
            {
                for (i = x_st; i < (x_st + search_size); i++)
                {
                    Color pp = bitmap1.GetPixel(i, j);

                    A = pp.A;
                    R = pp.R;
                    G = pp.G;
                    B = pp.B;

                    if ((R >= upper_bound) && (G >= upper_bound) && (B >= upper_bound))
                    {
                        saturation_array[((i - x_st) / awb_block) + (((j - y_st) / awb_block)) * (search_size / awb_block)]++;

                    }
                }
            }

            SolidBrush semiTransBrush = new SolidBrush(Color.FromArgb(60, 0, 255, 0));
            //richTextBox1.Text += "\nresult:\n";
            for (i = 0; i < saturation_array.Length; i++)
            {
                //richTextBox1.Text += "saturation_array[" + i.ToString() + "] = " + saturation_array[i].ToString() + "\n";
                if (saturation_array[i] == 0)
                {
                    g.FillRectangle(semiTransBrush, new Rectangle(x_st + awb_block * (i % (search_size / awb_block)), y_st + awb_block * (i / (search_size / awb_block)), awb_block, awb_block));
                }
            }






        }

        private void button2_Click(object sender, EventArgs e)
        {
            bitmap1 = new Bitmap(filename);
            g = Graphics.FromImage(bitmap1);
            pictureBox1.Image = bitmap1;

        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button4_Click(object sender, EventArgs e)
        {


        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //下載檔案的範例 - 使用WebClient
            WebClient wc = new WebClient();
            wc.DownloadFile("http://s.pimg.tw/qrcode/charleslin74/blog.png", "d:\\blog.png");
        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void timer1_Tick(object sender, EventArgs e)
        {


        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {
            bitmap1 = new Bitmap(filename);
            g = Graphics.FromImage(bitmap1);
            pictureBox1.Image = bitmap1;


            g2 = pictureBox2.CreateGraphics();
            //pictureBox1.Image = bitmap1;

            int i;
            int j;
            int A;
            int R;
            int G;
            int B;
            int search_size = 256;   //256X256
            int awb_block = 32;     //AWB block size width, height
            int ww = awb_block;
            int hh = awb_block;

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            int center_x = W / 2;
            int center_y = H / 2;
            int x_st = center_x - search_size / 2;
            int y_st = center_y - search_size / 2;

            int[,] rgb_array = new int[3, 16];

            for (i = 0; i <= (search_size / awb_block); i++)
            {
                g.DrawLine(new Pen(Color.Red, 1), x_st, y_st + awb_block * i, x_st + search_size - 1, y_st + awb_block * i);
                g.DrawLine(new Pen(Color.Red, 1), x_st + awb_block * i, y_st, x_st + awb_block * i, y_st + search_size - 1);
            }

            int[] saturation_array = new int[(search_size / awb_block) * (search_size / awb_block)];

            int upper_bound = 240;
            for (j = y_st; j < (y_st + search_size); j++)
            {
                for (i = x_st; i < (x_st + search_size); i++)
                {
                    Color pp = bitmap1.GetPixel(i, j);

                    A = pp.A;
                    R = pp.R;
                    G = pp.G;
                    B = pp.B;

                    if ((R >= upper_bound) && (G >= upper_bound) && (B >= upper_bound))
                    {
                        saturation_array[((i - x_st) / awb_block) + (((j - y_st) / awb_block)) * (search_size / awb_block)]++;

                    }
                    rgb_array[0, (R / 16)] += R;
                    rgb_array[1, (G / 16)] += G;
                    rgb_array[2, (B / 16)] += B;
                }

            }

            SolidBrush semiTransBrush = new SolidBrush(Color.FromArgb(60, 0, 255, 0));
            //richTextBox1.Text += "\nresult:\n";
            for (i = 0; i < saturation_array.Length; i++)
            {
                //richTextBox1.Text += "saturation_array[" + i.ToString() + "] = " + saturation_array[i].ToString() + "\n";
                if (saturation_array[i] == 0)
                {
                    g.FillRectangle(semiTransBrush, new Rectangle(x_st + awb_block * (i % (search_size / awb_block)), y_st + awb_block * (i / (search_size / awb_block)), awb_block, awb_block));
                }
            }

            int rgb_max = 0;

            richTextBox1.Text += "R = " + "\n";
            for (i = 0; i < 16; i++)
            {
                richTextBox1.Text += rgb_array[0, i].ToString() + " ";
                if (rgb_max < rgb_array[0, i])
                    rgb_max = rgb_array[0, i];
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "G = " + "\n";
            for (i = 0; i < 16; i++)
            {
                richTextBox1.Text += rgb_array[1, i].ToString() + " ";
                if (rgb_max < rgb_array[1, i])
                    rgb_max = rgb_array[1, i];
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "B = " + "\n";
            for (i = 0; i < 16; i++)
            {
                richTextBox1.Text += rgb_array[2, i].ToString() + " ";
                if (rgb_max < rgb_array[2, i])
                    rgb_max = rgb_array[2, i];
            }
            richTextBox1.Text += "\n";
            richTextBox1.Text += "rgb_max = " + rgb_max.ToString() + "\n";

            //g2.DrawRectangle(new Pen(Color.Red, 1), new Rectangle(50, 50, 200, 100));

            //g2.FillRectangle(new SolidBrush(Color.FromArgb(255, 0, 255, 0)), new Rectangle(50, 50, 200, 100));


            //SolidBrush semiTransBrush = new SolidBrush(Color.FromArgb(255, 0, 255, 0));

            int height = 300;
            int h = 0;
            richTextBox1.Text += "normalize\n";

            richTextBox1.Text += "R = " + "\n";
            for (i = 0; i < 16; i++)
            {
                h = (int)((double)rgb_array[0, i] * height / rgb_max);
                richTextBox1.Text += ((int)((double)rgb_array[0, i] * height / rgb_max)).ToString() + " ";

                if (h < 1)
                    h = 1;
                g2.FillRectangle(new SolidBrush(Color.FromArgb(255, 255, 0, 0)), new Rectangle(20 + i * 20, pictureBox2.Height - 50 - h, 4, h));

                //g2.FillRectangle(new SolidBrush(Color.FromArgb(255, 128, 128, 0)), new Rectangle(20 + i * 20, 50, 4, h));

            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "G = " + "\n";
            for (i = 0; i < 16; i++)
            {
                h = (int)((double)rgb_array[1, i] * height / rgb_max);
                richTextBox1.Text += ((int)((double)rgb_array[1, i] * height / rgb_max)).ToString() + " ";
                if (h < 1)
                    h = 1;
                g2.FillRectangle(new SolidBrush(Color.FromArgb(255, 0, 255, 0)), new Rectangle(20 + i * 20 + 5, pictureBox2.Height - 50 - h, 4, h));
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "B = " + "\n";
            for (i = 0; i < 16; i++)
            {
                h = (int)((double)rgb_array[2, i] * height / rgb_max);
                richTextBox1.Text += ((int)((double)rgb_array[2, i] * height / rgb_max)).ToString() + " ";
                if (h < 1)
                    h = 1;
                g2.FillRectangle(new SolidBrush(Color.FromArgb(255, 0, 0, 255)), new Rectangle(20 + i * 20 + 10, pictureBox2.Height - 50 - h, 4, h));
            }
            richTextBox1.Text += "\n";





        }

        private void button10_Click(object sender, EventArgs e)
        {

            HttpWebRequest httpRequest = null;
            HttpWebResponse httpResponse;

            string result = "";
            String txtURL = "https://www.google.com.tw/";
            char[] cbuffer = new char[256];
            int byteRead = 0;
            try
            {

                Uri httpURL = new Uri(txtURL);
                httpRequest = (HttpWebRequest)WebRequest.Create(httpURL);
                httpResponse = (HttpWebResponse)httpRequest.GetResponse();
                System.IO.Stream respStream = httpResponse.GetResponseStream();
                System.IO.StreamReader respStreamReader = new StreamReader(respStream);
                byteRead = respStreamReader.Read(cbuffer, 0, 256);
                while (byteRead != 0)
                {
                    string response = new string(cbuffer, 0, byteRead);
                    result = result + response;
                    byteRead = respStreamReader.Read(cbuffer, 0, 256);
                    richTextBox1.Text += response + "\n";
                }



            }
            catch (Exception)
            {

            }
        }






    }
}
