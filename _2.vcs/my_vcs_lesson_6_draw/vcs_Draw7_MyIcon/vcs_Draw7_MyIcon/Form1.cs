using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat

using System.IO;        //for File

namespace vcs_Draw7_MyIcon
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;
        Color foreground_color = Color.Red;
        Color background_color = Color.White;

        string FileName = "";

        public Form1()
        {
            InitializeComponent();
            pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
            p = new Pen(foreground_color, 3);
            sb = new SolidBrush(foreground_color);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            //open
            Point[] points = new Point[3];
            points[0] = new Point(width / 8, height / 8);
            points[1] = new Point(width * 7 / 8, height * 1 / 8);
            points[2] = new Point(width * 1 / 2, height * 7 / 8);
            g.FillPolygon(sb, points);

            pictureBox1.Image = bitmap1;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            //close
            Point[] points = new Point[3];
            points[0] = new Point(width / 2, height / 8);
            points[1] = new Point(width * 7 / 8, height * 7 / 8);
            points[2] = new Point(width * 1 / 8, height * 7 / 8);
            g.FillPolygon(sb, points);

            pictureBox1.Image = bitmap1;


        }

        private void button5_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            //play-pause
            Point[] points = new Point[3];
            points[0] = new Point(width / 8, height * 2 / 8);
            points[1] = new Point(width / 2, height / 2);
            points[2] = new Point(width / 8, height * 6 / 8);
            g.FillPolygon(sb, points);

            g.FillRectangle(sb, new Rectangle(width / 2, height * 2 / 8, width / 8, height / 2));
            g.FillRectangle(sb, new Rectangle(width / 2 + width * 2 / 8, height * 2 / 8, width / 8, height / 2));
            pictureBox1.Image = bitmap1;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            // stop
            g.FillRectangle(sb, new Rectangle(width / 8, height / 8, width * 6 / 8, height * 6 / 8));

            pictureBox1.Image = bitmap1;
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }
            g = Graphics.FromImage(bitmap1);
            p = new Pen(Color.Red, 10);
            g.DrawEllipse(p, new Rectangle(5, 5, width - 12, height - 12));
            Font f;


            int t = 5;
            int z = 20;
            Point point1a = new Point(5 + t, 5 + t + z);
            Point point2a = new Point(5 + 115 - t, 5 + 115 - t - z);
            g.DrawLine(p, point1a, point2a);     // Draw line to screen.

            sb = new SolidBrush(Color.Black);
            f = new Font("Arial", 88);

            g.DrawString("2", f, sb, new PointF(10, 0));
            
            pictureBox1.Image = bitmap1;

        }

        private void button8_Click(object sender, EventArgs e)
        {
      
        }

        private void button11_Click(object sender, EventArgs e)
        {
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            // refresh
            p = new Pen(Color.Red, 25);
            p.EndCap = System.Drawing.Drawing2D.LineCap.ArrowAnchor;
            g.DrawArc(p, 20, 20, 90, 90, 25, 335);
            pictureBox1.Image = bitmap1;

        }

        private void button13_Click(object sender, EventArgs e)
        {
            //加上標記
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;

            if (bitmap1 == null)
                bitmap1 = new Bitmap(width, height);
            g = Graphics.FromImage(bitmap1);

            //邊框黑白點
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    if (yy == 0)
                    {
                        if ((xx % 2) == 0)
                            bitmap1.SetPixel(xx, yy, Color.White);
                        else
                            bitmap1.SetPixel(xx, yy, Color.Black);
                    }
                    else if (yy == (height - 1))
                    {
                        if ((xx % 2) == 1)
                            bitmap1.SetPixel(xx, yy, Color.White);
                        else
                            bitmap1.SetPixel(xx, yy, Color.Black);
                    }
                    else if (xx == 0)
                    {
                        if ((yy % 2) == 0)
                            bitmap1.SetPixel(xx, yy, Color.White);
                        else
                            bitmap1.SetPixel(xx, yy, Color.Black);
                    }
                    else if (xx == (width - 1))
                    {
                        if ((yy % 2) == 1)
                            bitmap1.SetPixel(xx, yy, Color.White);
                        else
                            bitmap1.SetPixel(xx, yy, Color.Black);
                    }
                }
            }

            p = new Pen(Color.Blue, 1);
            g.DrawRectangle(p, new Rectangle(width / 8, height / 8, width * 6 / 8, height * 6 / 8));
            g.DrawEllipse(p, new Rectangle(5, 5, width - 12, height - 12));
            pictureBox1.Image = bitmap1;
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);


                    //background_color
                }
            }

            g = Graphics.FromImage(bitmap1);

            // record
            g.FillEllipse(sb, new Rectangle(width / 4, height / 4, width / 2, height / 2));

            pictureBox1.Image = bitmap1;
        }

        private void button16_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            //pause
            g.FillRectangle(sb, new Rectangle(width * 3 / 16, height * 2 / 8, width * 4 / 16, height / 2));
            g.FillRectangle(sb, new Rectangle(width * 9 / 16, height * 2 / 8, width * 4 / 16, height / 2));
            pictureBox1.Image = bitmap1;
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            //next
            Point[] points = new Point[3];
            points[0] = new Point(width / 8 + width / 8, height * 2 / 8);
            points[1] = new Point(width / 2 + width / 8, height / 2);
            points[2] = new Point(width / 8 + width / 8, height * 6 / 8);
            g.FillPolygon(sb, points);

            g.FillRectangle(sb, new Rectangle(width / 2 + width / 8, height * 2 / 8, width / 8, height / 2));
            pictureBox1.Image = bitmap1;

        }

        private void button17_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            //previous
            Point[] points = new Point[3];
            points[0] = new Point(width * 6 / 8, height * 2 / 8);
            points[1] = new Point(width / 8 + width / 8 + width /8, height / 2);
            points[2] = new Point(width * 6 / 8, height * 6 / 8);
            g.FillPolygon(sb, points);

            g.FillRectangle(sb, new Rectangle(width / 8 + width / 8, height * 2 / 8, width / 8, height / 2));
            pictureBox1.Image = bitmap1;

        }

        private void button20_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            //open-file
            Point[] points = new Point[3];
            points[0] = new Point(width / 8, height * 5 / 8);
            points[1] = new Point(width / 2, height / 8);
            points[2] = new Point(width * 7 / 8, height * 5 / 8);
            g.FillPolygon(sb, points);

            g.FillRectangle(sb, new Rectangle(width / 8, height * 5 / 8 + height / 16, width * 6 / 8, height / 8));
            pictureBox1.Image = bitmap1;

        }

        private void button24_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            //plus
            g.FillRectangle(sb, new Rectangle(width / 8, height * 7 / 16, width * 6 / 8, height * 2 / 16));
            g.FillRectangle(sb, new Rectangle(width * 7 / 16, height / 8, width * 2 / 16, height * 6 / 8));
            pictureBox1.Image = bitmap1;

        }

        private void button23_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            //minus
            g.FillRectangle(sb, new Rectangle(width / 8, height * 7 / 16, width * 6 / 8, height * 2 / 16));
            pictureBox1.Image = bitmap1;

        }

        private void button22_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            //up
            Point[] points = new Point[3];
            points[0] = new Point(width * 4 / 8, height * 2 / 8);
            points[1] = new Point(width * 6 / 8, height * 6 / 8);
            points[2] = new Point(width * 2 / 8, height * 6 / 8);
            g.FillPolygon(sb, points);

            pictureBox1.Image = bitmap1;

        }

        private void button21_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            //down
            Point[] points = new Point[3];
            points[0] = new Point(width * 4 / 8, height * 2 / 8);
            points[1] = new Point(width * 6 / 8, height * 6 / 8);
            points[2] = new Point(width * 2 / 8, height * 6 / 8);

            points[0] = new Point(width * 4 / 8, height * 6 / 8);
            points[1] = new Point(width * 6 / 8, height * 2 / 8);
            points[2] = new Point(width * 2 / 8, height * 2 / 8);
            g.FillPolygon(sb, points);

            pictureBox1.Image = bitmap1;

        }

        private void button25_Click(object sender, EventArgs e)
        {
            //加圓圈
            int width;
            int height;

            width = 128;
            height = 128;

            if(bitmap1 == null)
                bitmap1 = new Bitmap(width, height);
            g = Graphics.FromImage(bitmap1);

            sb = new SolidBrush(Color.Yellow);

            g.FillEllipse(sb, new Rectangle(width / 8, height / 8, width * 6 / 8, height * 6 / 8));

            sb = new SolidBrush(foreground_color);

            pictureBox1.Image = bitmap1;

        }

        private void button26_Click(object sender, EventArgs e)
        {
            int i;
            int j;
            int W = 640;
            int H = 480;

            int width;
            int height;

            Pen p1;
            Pen p2;

            width = W;
            height = H;

            if (bitmap1 == null)
                bitmap1 = new Bitmap(width, height);
            g = Graphics.FromImage(bitmap1);

            p1 = new Pen(Color.Black, 1);
            p2 = new Pen(Color.Pink, 1);

            // Draw transparency required on layer 1
            for (j = 0; j < H; j++)
            {
                for (i = 0; i < W; i++)
                {
                    if ((j > (1.5 * (H >> 3) - 1)) && (j < (H - 1.5 * (H >> 3))))
                    {
                        g.DrawEllipse(p2, i, j, 1, 1); //繪製粉紅色圓點 中段
                    }
                    else
                    {

                        if (j < 1.5 * (H >> 3))
                        { // Top lines
                            if ((i < (1.5 * (H >> 3) - j)) || (i > ((W - 1.5 * (H >> 3)) - 1 + j)))
                            {
                                g.DrawEllipse(p1, i, j, 1, 1); //繪製黑色圓點 上段的左右
                            }
                            else
                            {
                                g.DrawEllipse(p2, i, j, 1, 1); //繪製粉紅色圓點 上段的中間
                            }
                        }
                        else
                        { // Bottom lines
                            if ((i < (j + 1.5 * (H >> 3) - H)) || i > ((W - (1.5 * (H >> 3) - (H - j))) - 1))
                            {
                                g.DrawEllipse(p1, i, j, 1, 1); //繪製黑色圓點 下段的左右
                            }
                            else
                            {
                                g.DrawEllipse(p2, i, j, 1, 1); //繪製粉紅色圓點 下段的中間
                            }
                        }
                    }
                }
            }




            pictureBox1.Image = bitmap1;

        }

        private void button28_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            //up
            Point[] points = new Point[3];
            points[0] = new Point(width * 4 / 8, height * 2 / 8);
            points[1] = new Point(width * 6 / 8, height * 6 / 8);
            points[2] = new Point(width * 2 / 8, height * 6 / 8);
            g.FillPolygon(sb, points);

            pictureBox1.Image = bitmap1;

        }

        private void button27_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            //down
            Point[] points = new Point[3];
            points[0] = new Point(width * 4 / 8, height * 2 / 8);
            points[1] = new Point(width * 6 / 8, height * 6 / 8);
            points[2] = new Point(width * 2 / 8, height * 6 / 8);

            points[0] = new Point(width * 4 / 8, height * 6 / 8);
            points[1] = new Point(width * 6 / 8, height * 2 / 8);
            points[2] = new Point(width * 2 / 8, height * 2 / 8);
            g.FillPolygon(sb, points);

            pictureBox1.Image = bitmap1;

        }

        private void button29_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            //left
            Point[] points = new Point[3];
            points[0] = new Point(width * 2 / 8, height * 4 / 8);
            points[1] = new Point(width * 6 / 8, height * 2 / 8);
            points[2] = new Point(width * 6 / 8, height * 6 / 8);
            g.FillPolygon(sb, points);

            pictureBox1.Image = bitmap1;


        }

        private void button30_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            //right
            Point[] points = new Point[3];
            points[0] = new Point(width * 2 / 8, height * 2 / 8);
            points[1] = new Point(width * 6 / 8, height * 4 / 8);
            points[2] = new Point(width * 2 / 8, height * 6 / 8);
            g.FillPolygon(sb, points);

            pictureBox1.Image = bitmap1;

        }

        private void button31_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            p = new Pen(foreground_color, 7);

            g.DrawRectangle(p, new Rectangle(width * 2 / 8, height * 2 / 8, width * 4 / 8, height * 4 / 8));

            Point pointa;
            Point pointb;

            pointa = new Point(width * 4 / 8, height * 0 / 8);
            pointb = new Point(width * 4 / 8, height * 2 / 8);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 4 / 8, height * 6 / 8);
            pointb = new Point(width * 4 / 8, height * 8 / 8);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 0 / 8, height * 4 / 8);
            pointb = new Point(width * 2 / 8, height * 4 / 8);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 6 / 8, height * 4 / 8);
            pointb = new Point(width * 8 / 8, height * 4 / 8);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pictureBox1.Image = bitmap1;

        }

        private void button32_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            p = new Pen(foreground_color, 7);

            g.DrawRectangle(p, new Rectangle(width * 1 / 8, height * 1 / 8, width * 6 / 8, height * 6 / 8));

            Point pointa;
            Point pointb;

            p = new Pen(background_color, 7);

            pointa = new Point(width * 3 / 8, height * 1 / 8);
            pointb = new Point(width * 5 / 8, height * 1 / 8);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 1 / 8, height * 3 / 8);
            pointb = new Point(width * 1 / 8, height * 5 / 8);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 3 / 8, height * 7 / 8);
            pointb = new Point(width * 5 / 8, height * 7 / 8);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 7 / 8, height * 3 / 8);
            pointb = new Point(width * 7 / 8, height * 5 / 8);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.




            pictureBox1.Image = bitmap1;

        }

        private void button33_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            // refresh
            p = new Pen(foreground_color, 20);
            p.StartCap = System.Drawing.Drawing2D.LineCap.Round;
            p.EndCap = System.Drawing.Drawing2D.LineCap.Round;
            g.DrawArc(p, 20, 20, 90, 90, -45, 180+45+45);

            Point pointa;
            Point pointb;

            pointa = new Point(width * 4 / 8, height * 1 / 8);
            pointb = new Point(width * 4 / 8, height * 4 / 8);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pictureBox1.Image = bitmap1;


        }

        private void button34_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            p = new Pen(foreground_color, 7);

            g.DrawRectangle(p, new Rectangle(width * 1 / 16, height * 1 / 16, width * 14 / 16, height * 14 / 16));

            Point pointa;
            Point pointb;

            p = new Pen(background_color, 7);

            pointa = new Point(width * 6 / 16, height * 1 / 16);
            pointb = new Point(width * 10 / 16, height * 1 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 1 / 16, height * 6 / 16);
            pointb = new Point(width * 1 / 16, height * 10 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 6 / 16, height * 15 / 16);
            pointb = new Point(width * 10 / 16, height * 15 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 15 / 16, height * 6 / 16);
            pointb = new Point(width * 15 / 16, height * 10 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.


            p = new Pen(foreground_color, 7);
            p.EndCap = System.Drawing.Drawing2D.LineCap.ArrowAnchor;

            pointa = new Point(width * 5 / 16, height * 5 / 16);
            pointb = new Point(width * 2 / 16, height * 2 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 11 / 16, height * 5 / 16);
            pointb = new Point(width * 14 / 16, height * 2 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 5 / 16, height * 11 / 16);
            pointb = new Point(width * 2 / 16, height * 14 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 11 / 16, height * 11 / 16);
            pointb = new Point(width * 14 / 16, height * 14 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pictureBox1.Image = bitmap1;

        }

        private void button35_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            p = new Pen(foreground_color, 7);

            g.DrawRectangle(p, new Rectangle(width * 4 / 16, height * 4 / 16, width * 8 / 16, height * 8 / 16));

            Point pointa;
            Point pointb;

            p = new Pen(background_color, 7);

            pointa = new Point(width * 6 / 16, height * 4 / 16);
            pointb = new Point(width * 10 / 16, height * 4 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 4 / 16, height * 6 / 16);
            pointb = new Point(width * 4 / 16, height * 10 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 6 / 16, height * 12 / 16);
            pointb = new Point(width * 10 / 16, height * 12 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 12 / 16, height * 6 / 16);
            pointb = new Point(width * 12 / 16, height * 10 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.


            p = new Pen(foreground_color, 7);
            p.StartCap = System.Drawing.Drawing2D.LineCap.ArrowAnchor;

            pointa = new Point(width * 4 / 16 - 5, height * 4 / 16 - 5);
            pointb = new Point(width * 1 / 16, height * 1 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 12 / 16 + 5, height * 4 / 16 - 5);
            pointb = new Point(width * 15 / 16, height * 1 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 4 / 16 - 5, height * 12 / 16 + 5);
            pointb = new Point(width * 1 / 16, height * 15 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 12 / 16 + 5, height * 12 / 16 + 5);
            pointb = new Point(width * 15 / 16, height * 15 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pictureBox1.Image = bitmap1;


        }

        private void button36_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 160;
            height = 160;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            p = new Pen(foreground_color, 25);
            p.StartCap = System.Drawing.Drawing2D.LineCap.Square;

            Point pointa;
            Point pointb;

            pointa = new Point(width * 1 / 4, height * 3 / 16);
            pointb = new Point(width * 1 / 4, height * 7 / 8);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 1 / 4, height * 3 / 16);
            pointb = new Point(width * 3 / 4, height * 3 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 1 / 4, height * 8 / 16);
            pointb = new Point(width * 11 / 16, height * 8 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.


            pictureBox1.Image = bitmap1;


        }

        private void button37_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 160;
            height = 160;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            p = new Pen(foreground_color, 25);
            p.StartCap = System.Drawing.Drawing2D.LineCap.Square;

            Point pointa;
            Point pointb;

            pointa = new Point(width * 3 / 4, height * 3 / 16);
            pointb = new Point(width * 3 / 4, height * 7 / 8);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 5 / 16, height * 3 / 16);
            pointb = new Point(width * 3 / 4, height * 3 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 3 / 4, height * 8 / 16);
            pointb = new Point(width * 5 / 16, height * 8 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.


            pictureBox1.Image = bitmap1;


        }

        private void button38_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 160;
            height = 160;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            p = new Pen(foreground_color, 25);
            p.StartCap = System.Drawing.Drawing2D.LineCap.Square;

            Point pointa;
            Point pointb;

            pointa = new Point(width * 1 / 4, height * 3 / 16);
            pointb = new Point(width * 1 / 4, height * 7 / 8);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 1 / 4, height * 13 / 16);
            pointb = new Point(width * 3 / 4, height * 13 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 1 / 4, height * 8 / 16);
            pointb = new Point(width * 11 / 16, height * 8 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.


            pictureBox1.Image = bitmap1;

        }

        private void button39_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 160;
            height = 160;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            p = new Pen(foreground_color, 25);
            p.StartCap = System.Drawing.Drawing2D.LineCap.Square;

            Point pointa;
            Point pointb;

            pointa = new Point(width * 3 / 4, height * 3 / 16);
            pointb = new Point(width * 3 / 4, height * 7 / 8 + 3);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 5 / 16, height * 13 / 16);
            pointb = new Point(width * 3 / 4, height * 13 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 3 / 4, height * 8 / 16);
            pointb = new Point(width * 5 / 16, height * 8 / 16);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.


            pictureBox1.Image = bitmap1;


        }

        private void button40_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            //cross
            Point pointa;
            Point pointb;

            p = new Pen(foreground_color, 15);

            pointa = new Point(width * 2 / 8, height * 2 / 8);
            pointb = new Point(width * 6 / 8, height * 6 / 8);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 6 / 8, height * 2 / 8);
            pointb = new Point(width * 2 / 8, height * 6 / 8);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pictureBox1.Image = bitmap1;

        }

        private void button41_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            Font f;

            sb = new SolidBrush(Color.Red);
            f = new Font("Arial", 60);

            g.DrawString("C#", f, sb, new PointF(0, 20));


            pictureBox1.Image = bitmap1;

        }

        private void button42_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            Font f;

            sb = new SolidBrush(Color.Red);
            f = new Font("Arial", 80);

            g.DrawString("A", f, sb, new PointF(10, 5));

            g.DrawRectangle(p, new Rectangle(width / 8, height / 8, width * 6 / 8, height * 6 / 8));


            pictureBox1.Image = bitmap1;

        }

        private void button43_Click(object sender, EventArgs e)
        {
            //home
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 160;
            height = 160;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            p = new Pen(foreground_color, 25);
            p.StartCap = System.Drawing.Drawing2D.LineCap.Square;


            //close
            Point[] points = new Point[3];
            points[0] = new Point(width / 2, height / 8);
            points[1] = new Point(width * 7 / 8, height * 4 / 8);
            points[2] = new Point(width * 1 / 8, height * 4 / 8);
            g.FillPolygon(sb, points);

            g.FillRectangle(sb, new Rectangle(width * 2 / 8, height * 4 / 8, width * 4 / 8, height * 3 / 8));

            p = new Pen(Color.White, 2);
            g.DrawRectangle(p, new Rectangle(width * 6 / 16, height * 9 / 16, width * 4 / 16, height * 7 / 16));



            pictureBox1.Image = bitmap1;

        }

        private void button44_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            Font f;

            sb = new SolidBrush(Color.Red);
            f = new Font("標楷體", 65);

            g.DrawString("詞", f, sb, new PointF(10, 20));

            g.DrawRectangle(p, new Rectangle(width / 8, height / 8, width * 6 / 8, height * 6 / 8));


            pictureBox1.Image = bitmap1;

        }

        private void button45_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            Font f;

            int hh = 35;
            f = new Font("Arial", 35);
            sb = new SolidBrush(Color.Red);
            g.DrawString("R", f, sb, new PointF(5, hh));
            sb = new SolidBrush(Color.Green);
            g.DrawString("G", f, sb, new PointF(38, hh));
            sb = new SolidBrush(Color.Blue);
            g.DrawString("B", f, sb, new PointF(76, hh));

            g.DrawRectangle(p, new Rectangle(width / 16, height / 16, width * 14 / 16, height * 14 / 16));


            pictureBox1.Image = bitmap1;

        }

        private void button46_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            Font f;

            sb = new SolidBrush(Color.Red);
            f = new Font("Arial", 28);

            g.DrawString("Python", f, sb, new PointF(0, 42));


            pictureBox1.Image = bitmap1;

        }

        private void button47_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //bin2bmp
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    bitmap1.SetPixel(xx, yy, Color.FromArgb(255, (xx % 256), (xx % 256), (xx % 256)));
                }
            }

            g = Graphics.FromImage(bitmap1);
            pictureBox1.Image = bitmap1;
        }

        private void button48_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 256 * 100;
            height = 678;
            bitmap1 = new Bitmap(width, height);

            //bin2bmp
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    bitmap1.SetPixel(xx, yy, Color.FromArgb(255, (xx % 256), (xx % 256), (xx % 256)));
                }
            }

            g = Graphics.FromImage(bitmap1);

            Font f;
            f = new Font("Arial", 50);
            for (xx = 0; xx < width; xx += 256)
            {
                g.DrawString((xx / 256 + 1).ToString() + "/" + (width / 256).ToString(), f, sb, new PointF(xx, 100));
            }

            g.DrawRectangle(p, new Rectangle(0, 0, width-1, height-1));


            pictureBox1.Image = bitmap1;

        }

        private const int ON = 0x00;
        private const int OFF = 0x01;

        void draw_switch(int on_off)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 128;
            height = 64;
            bitmap1 = new Bitmap(width, height);

            Color background_color;
            Color foreground_color;
            Color active_color;
            Font f;

            if (on_off == ON)
            {
                background_color = Color.Black;
                foreground_color = Color.LimeGreen;
                active_color = Color.White;
            }
            else
            {
                background_color = Color.Black;
                foreground_color = Color.LimeGreen;
                active_color = Color.White;
            }

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            sb = new SolidBrush(foreground_color);

            g.FillEllipse(sb, new Rectangle(0, 0, width / 2, width / 2));
            g.FillEllipse(sb, new Rectangle(width / 2, 0, width / 2, width / 2));
            g.FillRectangle(sb, new Rectangle(width / 4, 0, width / 2, width / 2));

            sb = new SolidBrush(active_color);

            if (on_off == ON)
                g.FillEllipse(sb, new Rectangle(width / 2 + 2, 0 + 2, width / 2 - 4, width / 2 - 4));
            else
                g.FillEllipse(sb, new Rectangle(0 / 2 + 2, 0 + 2, width / 2 - 4, width / 2 - 4));


            sb = new SolidBrush(active_color);
            f = new Font("Arial", 20);

            if (on_off == ON)
                g.DrawString("ON", f, sb, new PointF(width / 16, height / 4));
            else
                g.DrawString("OFF", f, sb, new PointF(width / 2, height / 4));

            pictureBox1.Image = bitmap1;
        }

        private void button49_Click(object sender, EventArgs e)
        {
            draw_switch(ON);
        }

        private void button50_Click(object sender, EventArgs e)
        {
            draw_switch(OFF);
        }

        private void button51_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 256;
            height = 256;
            bitmap1 = new Bitmap(width, height);

            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    if (yy < 256 / 4)
                        bitmap1.SetPixel(xx, yy, Color.FromArgb(255, (xx % 256), 0, 0));
                    else if (yy < 256 / 4 * 2)
                        bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0, (xx % 256), 0));
                    else if (yy < 256 / 4 * 3)
                        bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0, 0, (xx % 256)));
                    else
                        bitmap1.SetPixel(xx, yy, Color.FromArgb(255, (xx % 256), (xx % 256), (xx % 256)));
                }
            }
            g = Graphics.FromImage(bitmap1);

            pictureBox1.Image = bitmap1;
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

            x_st = 500;
            y_st = 10;
            groupBox1.Location = new Point(x_st - 10, y_st);
            groupBox1.ClientSize = new Size(65*8+12, 80);

            x_st = 10;
            y_st = 13;
            dx = 65;
            dy = 65;
            bt0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt3.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt4.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            bt5.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            bt6.Location = new Point(x_st + dx * 6, y_st + dy * 0);
            bt7.Location = new Point(x_st + dx * 7, y_st + dy * 0);

            //button
            x_st = 500;
            y_st = 100;
            dx = 65;
            dy = 65;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button3.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            button4.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            button5.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            button6.Location = new Point(x_st + dx * 6, y_st + dy * 0);
            button7.Location = new Point(x_st + dx * 7, y_st + dy * 0);

            button8.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button9.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button10.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button11.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            button13.Location = new Point(x_st + dx * 5, y_st + dy * 1);
            button14.Location = new Point(x_st + dx * 6, y_st + dy * 1);
            button15.Location = new Point(x_st + dx * 7, y_st + dy * 1);

            button16.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button18.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button19.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            button20.Location = new Point(x_st + dx * 4, y_st + dy * 2);
            button21.Location = new Point(x_st + dx * 5, y_st + dy * 2);
            button22.Location = new Point(x_st + dx * 6, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 7, y_st + dy * 2);

            button24.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button25.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button27.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            button28.Location = new Point(x_st + dx * 4, y_st + dy * 3);
            button29.Location = new Point(x_st + dx * 5, y_st + dy * 3);
            button30.Location = new Point(x_st + dx * 6, y_st + dy * 3);
            button31.Location = new Point(x_st + dx * 7, y_st + dy * 3);

            button32.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button33.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button34.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button35.Location = new Point(x_st + dx * 3, y_st + dy * 4);
            button36.Location = new Point(x_st + dx * 4, y_st + dy * 4);
            button37.Location = new Point(x_st + dx * 5, y_st + dy * 4);
            button38.Location = new Point(x_st + dx * 6, y_st + dy * 4);
            button39.Location = new Point(x_st + dx * 7, y_st + dy * 4);

            button40.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button41.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button42.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button43.Location = new Point(x_st + dx * 3, y_st + dy * 5);
            button44.Location = new Point(x_st + dx * 4, y_st + dy * 5);
            button45.Location = new Point(x_st + dx * 5, y_st + dy * 5);
            button46.Location = new Point(x_st + dx * 6, y_st + dy * 5);
            button47.Location = new Point(x_st + dx * 7, y_st + dy * 5);

            button48.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button49.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button50.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button51.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            //button52.Location = new Point(x_st + dx * 4, y_st + dy * 6);
            //button53.Location = new Point(x_st + dx * 5, y_st + dy * 6);


            //richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            //richTextBox1.Size = new Size(richTextBox1.Size.Width, this.Height - richTextBox1.Location.Y - 50);

            pictureBox1.Location = new Point(10, 10);

            this.Size = new Size(1100, this.Size.Height);
        }

        private void bt0_Click(object sender, EventArgs e)
        {
            openFileDialog1.Filter = "圖片(*.bmp,*.jpg,*.png)|*.bmp;*.jpg;*.png";
            //openFileDialog1.Filter = "BMP|*.bmp|JPG|*.jpg|PNG|*.png|GIF|*.gif";
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                FileName = this.openFileDialog1.FileName.Trim();
                richTextBox1.Text += FileName + "\n";
                pictureBox1.ImageLocation = openFileDialog1.FileName;
            }
        }

        private void bt1_Click(object sender, EventArgs e)
        {
            if (bitmap1 != null)
            {
                string filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                String filename1 = filename + ".jpg";
                String filename2 = filename + ".bmp";
                String filename3 = filename + ".png";

                bitmap1.Save(@filename1, ImageFormat.Jpeg);
                bitmap1.Save(@filename2, ImageFormat.Bmp);
                bitmap1.Save(@filename3, ImageFormat.Png);

                richTextBox1.Text += "存檔成功\n";
                richTextBox1.Text += "已存檔 : " + filename1 + "\n";
                richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                richTextBox1.Text += "已存檔 : " + filename3 + "\n";
            }
            else
                richTextBox1.Text += "無圖可存\n";
        }

        private void bt2_Click(object sender, EventArgs e)
        {
            if (FileName == "")
            {
                richTextBox1.Text += "未選取圖片\n";
                return;
            }
            //圖示中包含的圖片常見尺寸有16×16（小圖示）、32×32、48×48，另外24×24、64×64、128×128也比較常見。
            Size size = new Size(256, 256);
            //獲得原始圖片文件
            using (Bitmap bm = new Bitmap(FileName))
            {
                //從現有的圖像縮小, 為了得到合適的icon文件
                using (Bitmap iconBm = new Bitmap(bm, size))    //硬是把大圖縮成小圖
                {
                    using (Icon icon = Icon.FromHandle(iconBm.GetHicon()))
                    {
                        string icon_filename = Application.StartupPath + "\\ICO_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".ico";
                        using (Stream stream = new System.IO.FileStream(icon_filename, System.IO.FileMode.Create))
                        {
                            icon.Save(stream);
                            richTextBox1.Text += "轉換成功, 路徑是 : " + icon_filename + "\n";
                        }
                    }
                }
            }
        }

        private void bt3_Click(object sender, EventArgs e)
        {
            if (bitmap1 == null)
            {
                richTextBox1.Text += "無圖片資料\n";
                return;
            }

            //圖示中包含的圖片常見尺寸有16×16（小圖示）、32×32、48×48，另外24×24、64×64、128×128也比較常見。
            Size size = new Size(128, 128);
            //獲得原始圖片文件
            //using (Bitmap bm = new Bitmap(FileName))
            {
                //從現有的圖像縮小, 為了得到合適的icon文件
                using (Bitmap iconBm = new Bitmap(bitmap1, size))
                {
                    using (Icon icon = Icon.FromHandle(iconBm.GetHicon()))
                    {
                        string icon_filename = Application.StartupPath + "\\ICO_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".ico";
                        using (Stream stream = new System.IO.FileStream(icon_filename, System.IO.FileMode.Create))
                        {
                            icon.Save(stream);
                            richTextBox1.Text += "轉換成功, 路徑是 : " + icon_filename + "\n";
                        }
                    }
                }
            }

        }

        private void bt4_Click(object sender, EventArgs e)
        {
            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                foreground_color = colorDialog1.Color;
                sb = new SolidBrush(foreground_color);
                button18.BackColor = foreground_color;
            }
        }

        private void bt5_Click(object sender, EventArgs e)
        {
            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                background_color = colorDialog1.Color;
                button19.BackColor = background_color;
            }

        }

        private void bt6_Click(object sender, EventArgs e)
        {

        }

        private void bt7_Click(object sender, EventArgs e)
        {

        }


        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button10_Click(object sender, EventArgs e)
        {

        }

        private void button18_Click(object sender, EventArgs e)
        {

        }

        private void button19_Click(object sender, EventArgs e)
        {

        }

        private void button0_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;
            int s = 5;

            width = 160;
            height = 160;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, background_color);
                }
            }

            g = Graphics.FromImage(bitmap1);

            p = new Pen(foreground_color, 8);
            p.StartCap = System.Drawing.Drawing2D.LineCap.Square;

            Point pointa;
            Point pointb;

            pointa = new Point(width * 0 / 4 + 10, height / 3+s);
            pointb = new Point(width * 4 / 4 - 10, height / 3-s);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 0 / 4 + 10, height * 2 / 3+s);
            pointb = new Point(width * 4 / 4 - 10, height * 2 / 3-s);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 1 / 3, height * 0 / 4 + 10);
            pointb = new Point(width * 1 / 3, height * 4 / 4 - 10);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(width * 2 / 3, height * 0 / 4 + 10);
            pointb = new Point(width * 2 / 3, height * 4 / 4 - 10);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            int r = 15;
            int cx;
            int cy;
            p = new Pen(foreground_color, 6);

            cx = width / 6;
            cy = height / 6;
            DrawCircle(g, p, cx, cy, r);

            cx = width * 5 / 6;
            cy = height * 5 / 6;
            DrawCircle(g, p, cx, cy, r);

            cx = width / 6;
            cy = height * 5 / 6;
            DrawCross(g, p, cx, cy, r);

            cx = width * 3 / 6;
            cy = height * 3 / 6;
            DrawCross(g, p, cx, cy, r);

            pictureBox1.Image = bitmap1;
        }

        void DrawCircle(Graphics g, Pen p, int cx, int cy, int r)
        {
            g.DrawEllipse(p, cx - r, cy - r, r * 2, r * 2);
        }

        void DrawCross(Graphics g, Pen p, int cx, int cy, int r)
        {
            //g.DrawEllipse(p, cx - r, cy - r, r * 2, r * 2);
            Point pointa;
            Point pointb;

            pointa = new Point(cx + r, cy - r);
            pointb = new Point(cx - r, cy + r);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

            pointa = new Point(cx - r, cy - r);
            pointb = new Point(cx + r, cy + r);
            g.DrawLine(p, pointa, pointb);     // Draw line to screen.

        }

    }
}
