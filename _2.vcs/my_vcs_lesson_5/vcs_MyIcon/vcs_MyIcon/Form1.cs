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

namespace vcs_MyIcon
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;

        string FileName = "";

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

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, Color.White);
                }
            }

            g = Graphics.FromImage(bitmap1);
            sb = new SolidBrush(Color.Red);

            //open
            Point[] points = new Point[3];
            points[0] = new Point(width / 8, height / 8);
            points[1] = new Point(width * 7 / 8, height / 8);
            points[2] = new Point(width / 2, height * 7 / 8);
            g.FillPolygon(sb, points);

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

            width = 128;
            height = 128;
            bitmap1 = new Bitmap(width, height);

            //background
            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    bitmap1.SetPixel(xx, yy, Color.White);
                }
            }

            g = Graphics.FromImage(bitmap1);
            sb = new SolidBrush(Color.Red);

            //close
            Point[] points = new Point[3];
            points[0] = new Point(width / 2, height / 8);
            points[1] = new Point(width * 7 / 8, height * 7 / 8);
            points[2] = new Point(width / 8, height * 7 / 8);
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
                    bitmap1.SetPixel(xx, yy, Color.White);
                }
            }

            g = Graphics.FromImage(bitmap1);
            sb = new SolidBrush(Color.Red);

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
                    bitmap1.SetPixel(xx, yy, Color.White);
                }
            }

            g = Graphics.FromImage(bitmap1);

            sb = new SolidBrush(Color.Red);

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
                    bitmap1.SetPixel(xx, yy, Color.White);
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
                        string icon_filename = "C://______test_vcs//" + DateTime.Now.ToString("yyyyMMdd_hhmmss") + ".ico";
                        using (Stream stream = new System.IO.FileStream(icon_filename, System.IO.FileMode.Create))
                        {
                            icon.Save(stream);
                            richTextBox1.Text += "轉換成功, 路徑是 : " + icon_filename + "\n";
                        }
                    }
                }
            }

        
        }

        private void button9_Click(object sender, EventArgs e)
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

        private void button10_Click(object sender, EventArgs e)
        {
            if (FileName == "")
            {
                richTextBox1.Text += "未選取圖片\n";
                return;
            }
            //圖示中包含的圖片常見尺寸有16×16（小圖示）、32×32、48×48，另外24×24、64×64、128×128也比較常見。
            Size size = new Size(256,256);
            //獲得原始圖片文件
            using (Bitmap bm = new Bitmap(FileName))
            {
                //從現有的圖像縮小, 為了得到合適的icon文件
                using (Bitmap iconBm = new Bitmap(bm, size))    //硬是把大圖縮成小圖
                {
                    using (Icon icon = Icon.FromHandle(iconBm.GetHicon()))
                    {
                        string icon_filename = "C://______test_vcs//" + DateTime.Now.ToString("yyyyMMdd_hhmmss") + ".ico";
                        using (Stream stream = new System.IO.FileStream(icon_filename, System.IO.FileMode.Create))
                        {
                            icon.Save(stream);
                            richTextBox1.Text += "轉換成功, 路徑是 : " + icon_filename + "\n";
                        }
                    }
                }
            }
        }

        private void button11_Click(object sender, EventArgs e)
        {
            System.Diagnostics.Process.Start("C://______test_vcs//");
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
                    bitmap1.SetPixel(xx, yy, Color.White);
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
            pictureBox1.Image = bitmap1;
        }
    }
}
