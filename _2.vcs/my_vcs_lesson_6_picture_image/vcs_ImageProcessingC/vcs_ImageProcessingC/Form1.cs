using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for BitmapData
using System.Runtime.InteropServices;   //for Marshal

namespace vcs_ImageProcessingC
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\picture1.jpg";
        Image image;
        Bitmap bitmap1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox1.Image = Image.FromFile(filename);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //推拉效果顯示圖像
            image = Image.FromFile(filename);
            pictureBox1.Image = image;
            pictureBox1.Size = new Size(image.Width, image.Height - 1);

            try
            {
                Graphics g = this.pictureBox1.CreateGraphics();
                Bitmap bitmap1 = new Bitmap(image);
                g.Clear(this.pictureBox1.BackColor);
                for (int i = 0; i < this.pictureBox1.Height; i++)
                {
                    Rectangle rectangle1 = new Rectangle(0, 0, this.pictureBox1.Width, i);
                    Rectangle rectangle2 = new Rectangle(0, this.pictureBox1.Height - i, this.pictureBox1.Width, i + 1);
                    Bitmap cloneBitmap = bitmap1.Clone(rectangle2, PixelFormat.DontCare);
                    g.DrawImage(cloneBitmap, rectangle1);
                    this.pictureBox1.Show();
                }
            }
            catch { }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //水平交錯效果顯示圖像
            bitmap1 = new Bitmap(filename);
            pictureBox1.Image = bitmap1;
            pictureBox1.Size = new Size(bitmap1.Width, bitmap1.Height);

            bitmap1 = new Bitmap(filename);
            pictureBox1.Image = LevelInterleaving(bitmap1);
        }

        Bitmap LevelInterleaving(Bitmap bitmap1)
        {
            int W = pictureBox1.Width;
            int H = pictureBox1.Height;
            Graphics g = this.pictureBox1.CreateGraphics();
            g.Clear(Color.WhiteSmoke);
            Bitmap bitmap2 = new Bitmap(W, H);
            int i = 0;
            while (i <= W / 2)
            {
                for (int m = 0; m <= H - 1; m++)
                {
                    bitmap2.SetPixel(i, m, bitmap1.GetPixel(i, m));
                }
                for (int n = 0; n <= H - 1; n++)
                {
                    bitmap2.SetPixel(W - i - 1, n, bitmap1.GetPixel(W - i - 1, n));
                }
                i++;
                this.Refresh();
                this.pictureBox1.Image = bitmap2;
                System.Threading.Thread.Sleep(10);
            }
            return bitmap2;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //垂直交錯效果顯示圖像
            bitmap1 = new Bitmap(filename);
            pictureBox1.Image = bitmap1;
            pictureBox1.Size = new Size(bitmap1.Width, bitmap1.Height);
            bitmap1 = new Bitmap(filename);
            pictureBox1.Image = UprightnessInterleaving(bitmap1);
        }

        Bitmap UprightnessInterleaving(Bitmap bitmap1)
        {
            int W = pictureBox1.Width;
            int H = pictureBox1.Height;
            Graphics g = this.pictureBox1.CreateGraphics();
            g.Clear(Color.WhiteSmoke);
            Bitmap bitmap2 = new Bitmap(W, H);
            int i = 0;
            while (i <= H / 2)
            {
                for (int m = 0; m <= W - 1; m++)
                {
                    bitmap2.SetPixel(m, i, bitmap1.GetPixel(m, i));
                }
                for (int n = 0; n <= W - 1; n++)
                {
                    bitmap2.SetPixel(n, H - i - 1, bitmap1.GetPixel(n, H - i - 1));
                }
                i++;
                this.Refresh();
                pictureBox1.Image = bitmap2;
                System.Threading.Thread.Sleep(10);
            }
            return bitmap2;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //圖像浮雕效果
            bitmap1 = new Bitmap(filename);
            pictureBox1.Image = bitmap1;

            bitmap1 = new Bitmap(filename);
            pictureBox1.Image = BassoRelievo(bitmap1);
        }

        Bitmap BassoRelievo(Bitmap bmp)
        {
            try
            {
                for (int i = 0; i < bmp.Width - 1; i++)
                {
                    for (int j = 0; j < bmp.Height - 1; j++)
                    {
                        Color Color1 = bmp.GetPixel(i, j);
                        Color Color2 = bmp.GetPixel(i + 1, j + 1);
                        int red = Math.Abs(Color1.R - Color2.R + 128);
                        int green = Math.Abs(Color1.G - Color2.G + 128);
                        int blue = Math.Abs(Color1.B - Color2.B + 128);
                        //顏色處理
                        if (red > 255) red = 255;
                        if (red < 0) red = 0;

                        if (green > 255) green = 255;
                        if (green < 0) green = 0;

                        if (blue > 255) blue = 255;
                        if (blue < 0) blue = 0;
                        bmp.SetPixel(i, j, Color.FromArgb(red, green, blue));
                    }
                }
            }
            catch { }

            return bmp;
        }


        private void button5_Click(object sender, EventArgs e)
        {
            //積木效果
            Image image = Image.FromFile(filename);
            this.BackgroundImage = image;

            //TBD


        }

        private void button6_Click(object sender, EventArgs e)
        {
            //銳化效果顯示圖像

            //TBD
        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = Image.FromFile(filename);
        }
    }
}
