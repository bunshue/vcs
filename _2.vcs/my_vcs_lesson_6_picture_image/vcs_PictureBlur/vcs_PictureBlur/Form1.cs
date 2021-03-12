using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_PictureBlur
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
            pictureBox1.Image = Image.FromFile(filename);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int W = pictureBox1.Image.Width;
            int H = pictureBox1.Image.Height;
            Bitmap bmp2 = new Bitmap(W, H);

            Bitmap bmp = new Bitmap("c:\\______test_files\\picture1.jpg");

            for (int j = 0; j < bmp.Height; j++)
            {
                for (int i = 0; i < bmp.Width; i++)
                {
                    int ok_cnt = 0;
                    int R = 0;
                    int G = 0;
                    int B = 0;

                    // 檢查上相鄰像素

                    //自己
                    R += bmp.GetPixel(i, j).R;
                    G += bmp.GetPixel(i, j).G;
                    B += bmp.GetPixel(i, j).B;

                    ok_cnt++;

                    if (j - 1 > 0)       //上
                    {
                        R += bmp.GetPixel(i, j - 1).R;
                        G += bmp.GetPixel(i, j - 1).G;
                        B += bmp.GetPixel(i, j - 1).B;

                        ok_cnt++;
                    }
                    if (j + 1 < H)      //下
                    {
                        R += bmp.GetPixel(i, j + 1).R;
                        G += bmp.GetPixel(i, j + 1).G;
                        B += bmp.GetPixel(i, j + 1).B;
                        ok_cnt++;
                    }
                    if (i - 1 > 0)       //左
                    {
                        R += bmp.GetPixel(i - 1, j).R;
                        G += bmp.GetPixel(i - 1, j).G;
                        B += bmp.GetPixel(i - 1, j).B;
                        ok_cnt++;
                    }
                    if (i + 1 < W)       //右
                    {
                        R += bmp.GetPixel(i + 1, j).R;
                        G += bmp.GetPixel(i + 1, j).G;
                        B += bmp.GetPixel(i + 1, j).B;
                        ok_cnt++;
                    }
                    if ((i - 1 > 0) && (j - 1 > 0))     //左上
                    {
                        R += bmp.GetPixel(i - 1, j - 1).R;
                        G += bmp.GetPixel(i - 1, j - 1).G;
                        B += bmp.GetPixel(i - 1, j - 1).B;
                        ok_cnt++;
                    }
                    if ((i - 1 > 0) && (j + 1 < H)) //左下
                    {
                        R += bmp.GetPixel(i - 1, j + 1).R;
                        G += bmp.GetPixel(i - 1, j + 1).G;
                        B += bmp.GetPixel(i - 1, j + 1).B;
                        ok_cnt++;
                    }
                    if ((i + 1 < W) && (j - 1 > 0))      //右上
                    {
                        R += bmp.GetPixel(i + 1, j - 1).R;
                        G += bmp.GetPixel(i + 1, j - 1).G;
                        B += bmp.GetPixel(i + 1, j - 1).B;
                        ok_cnt++;
                    }
                    if ((i + 1 < W) && (j + 1 < H)) //右下
                    {
                        R += bmp.GetPixel(i + 1, j + 1).R;
                        G += bmp.GetPixel(i + 1, j + 1).G;
                        B += bmp.GetPixel(i + 1, j + 1).B;
                        ok_cnt++;
                    }

                    bmp2.SetPixel(i, j, Color.FromArgb((R / ok_cnt), (G / ok_cnt), (B / ok_cnt)));
                }
            }

            richTextBox1.Text += "done\n";

            pictureBox1.Image = bmp;
            pictureBox2.Image = bmp2;
        }
    }
}
