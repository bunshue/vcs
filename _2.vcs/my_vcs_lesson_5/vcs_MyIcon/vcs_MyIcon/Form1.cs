using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat

namespace vcs_MyIcon
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;

        public Form1()
        {
            InitializeComponent();
            pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
            p = new Pen(Color.Red, 3);
            sb = new SolidBrush(Color.Red);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 30;
            height = 20;
            bitmap1 = new Bitmap(width, height);
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, Color.Gray);
                }
            }

            //open
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    if((xx > (5+yy/2))&&(xx<25-yy/2))
                        bitmap1.SetPixel(xx, yy, Color.Red);
                }
            }
            pictureBox1.Image = bitmap1;

        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (bitmap1 != null)
            {
                String file = "C:\\______test_vcs\\IMG_" + DateTime.Now.ToString("yyyyMMdd_hhmmss");
                String file1 = file + ".jpg";
                String file2 = file + ".bmp";
                String file3 = file + ".png";

                bitmap1.Save(@file1, ImageFormat.Jpeg);
                bitmap1.Save(@file2, ImageFormat.Bmp);
                bitmap1.Save(@file3, ImageFormat.Png);

                richTextBox1.Text += "存檔成功\n";
                richTextBox1.Text += "已存檔 : " + file1 + "\n";
                richTextBox1.Text += "已存檔 : " + file2 + "\n";
                richTextBox1.Text += "已存檔 : " + file3 + "\n";
            }
            else
                richTextBox1.Text += "無圖可存\n";

        }

        private void button4_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 30;
            height = 20;
            bitmap1 = new Bitmap(width, height);
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, Color.Gray);
                }
            }

            //close
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    if ((xx < (15 + (yy + 1) / 2)) && (xx > 15 - (yy + 1) / 2))
                        bitmap1.SetPixel(xx, yy, Color.Red);
                }
            }

            pictureBox1.Image = bitmap1;


        }

        private void button5_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 45;
            height = 30;
            bitmap1 = new Bitmap(width, height);
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, Color.Gray);
                }
            }

            g = Graphics.FromImage(bitmap1);

            sb = new SolidBrush(Color.Red);

            Point[] points = new Point[3];
            points[0] = new Point(5, 5);
            points[1] = new Point(20, 15);
            points[2] = new Point(5, 25);
            g.FillPolygon(sb, points);

            g.FillRectangle(sb, new Rectangle(25, 5, 5, 20));

            g.FillRectangle(sb, new Rectangle(35, 5, 5, 20));

            pictureBox1.Image = bitmap1;

        }

        private void button6_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 30;
            height = 20;
            bitmap1 = new Bitmap(width, height);
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, Color.Gray);
                }
            }

            //stop
            width = 45;
            height = 30;
            bitmap1 = new Bitmap(width, height);
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    bitmap1.SetPixel(xx, yy, Color.Gray);
                }
            }

            g = Graphics.FromImage(bitmap1);

            sb = new SolidBrush(Color.Red);

            // stop
            g.FillRectangle(sb, new Rectangle(12, 5, 20, 20));

            pictureBox1.Image = bitmap1;

        }

        private void button7_Click(object sender, EventArgs e)
        {
            //逐點製作圖檔
            int width;
            int height;
            int xx;
            int yy;

            width = 150;
            height = 150;
            bitmap1 = new Bitmap(width, height);

            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, Color.White);
                }
            }
            g = Graphics.FromImage(bitmap1);
            p = new Pen(Color.Red, 10);
            g.DrawEllipse(p, new Rectangle(5, 5, width - 12, height - 12));
            Font f;


            int t = 10;
            int z = 30;
            Point point1a = new Point(5 + t, 5 + t + z);
            Point point2a = new Point(5 + 138 - t, 5 + 138 - t - z);
            g.DrawLine(p, point1a, point2a);     // Draw line to screen.

            sb = new SolidBrush(Color.Black);
            f = new Font("Arial", 100);

            g.DrawString("2", f, sb, new PointF(14, 0));
            
            pictureBox1.Image = bitmap1;

        }
    }
}
