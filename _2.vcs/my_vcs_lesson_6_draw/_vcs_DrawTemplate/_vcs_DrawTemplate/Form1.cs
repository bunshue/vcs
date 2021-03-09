using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for LineCap
using System.Drawing.Imaging;   //for ImageFormat

                            using System.Runtime.InteropServices;   //for Marshal


namespace _vcs_DrawTemplate
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

            button2.Enabled = false;
            button3.Enabled = false;
            button4.Enabled = false;
            button5.Enabled = false;
            button7.Enabled = false;
            button9.Enabled = false;

            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
            p = new Pen(Color.Red, 3);
            sb = new SolidBrush(Color.Red);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //新建圖檔, 初始化畫布
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;

            richTextBox1.Text += "已新建圖檔\n";
            richTextBox1.Text += "畫布大小 : W = " + bitmap1.Width.ToString() + " H = " + bitmap1.Height.ToString() + "\n";

            button2.Enabled = true;
            button3.Enabled = true;
            button4.Enabled = true;
            button5.Enabled = true;
            button7.Enabled = true;
            button9.Enabled = true;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //載入圖片至畫布
            string filename = string.Empty;
            //filename = "C:\\______test_files\\bear.jpg";
            filename = "C:\\______test_files\\picture1.jpg";
            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";
            bitmap1 = new Bitmap(filename);

            int width;
            int height;

            width = bitmap1.Width;
            height = bitmap1.Height;

            richTextBox1.Text += "畫布大小 : W = " + width.ToString() + " H = " + height.ToString() + "\n";

            //pictureBox1.Size = new Size(width, height);   //改變圖框大小
            pictureBox1.Location = new Point(0, 0);
            pictureBox1.Image = bitmap1;

            g = Graphics.FromImage(bitmap1);

            pictureBox1.Image = bitmap1;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //畫東西
            g.DrawRectangle(new Pen(Color.Red), new Rectangle(0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1));
            g.DrawRectangle(new Pen(Color.Red, 5), new Rectangle(100, 100, 300, 300));

            int width = 200;
            int height = 200;
            Point[] points = new Point[3];
            points[0] = new Point(width / 2, height / 8);
            points[1] = new Point(width * 7 / 8, height * 7 / 8);
            points[2] = new Point(width * 1 / 8, height * 7 / 8);
            g.FillPolygon(sb, points);

            //畫箭頭
            Pen pen = new Pen(Color.FromArgb(255, 0, 0, 255), 8);
            pen.StartCap = LineCap.RoundAnchor;
            pen.EndCap = LineCap.ArrowAnchor;
            g.DrawLine(pen, 100, 100, 300, 300);

            //畫聯結線條
            GraphicsPath path = new GraphicsPath();
            Pen penJoin = new Pen(Color.FromArgb(255, 0, 0, 255), 20);

            path.StartFigure();
            path.AddLine(new Point(50, 200), new Point(100, 200));
            path.AddLine(new Point(100, 200), new Point(100, 250));

            penJoin.LineJoin = LineJoin.Bevel;
            g.DrawPath(penJoin, path);

            //繪製自訂虛線
            float[] dashValues = { 5, 2, 15, 4 };
            Pen greenPen = new Pen(Color.Green, 10);
            greenPen.DashPattern = dashValues;
            g.DrawLine(greenPen, new Point(50, 150), new Point(600, 150));
            
            pictureBox1.Image = bitmap1;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //清除畫布
            g.Clear(Color.White);

            pictureBox1.Image = bitmap1;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //逐點繪圖
            int width = bitmap1.Width;
            int height = bitmap1.Height;
            int xx;
            int yy;
            Color pt;

            //讀取/修改每一的的RGB值
            for (yy = 0; yy < height / 2; yy += 1)
            {
                for (xx = 0; xx < width / 2; xx += 1)
                {
                    pt = bitmap1.GetPixel(xx, yy);
                    bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 255 - pt.R, 255 - pt.G, 255 - pt.B));
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    //bitmap1.SetPixel(xx, yy, Color.White);
                }
            }
            pictureBox1.Image = bitmap1;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            save_image_to_drive();
        }

        void save_image_to_drive()
        {
            if (bitmap1 != null)
            {
                string filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                String filename1 = filename + ".jpg";
                String filename2 = filename + ".bmp";
                String filename3 = filename + ".png";

                try
                {
                    bitmap1.Save(@filename1, ImageFormat.Jpeg);
                    bitmap1.Save(@filename2, ImageFormat.Bmp);
                    bitmap1.Save(@filename3, ImageFormat.Png);

                    richTextBox1.Text += "存檔成功\n";
                    richTextBox1.Text += "已存檔 : " + filename1 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename3 + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }
            else
                richTextBox1.Text += "無圖可存\n";
        }

        private double rad(double d)
        {
            return d * Math.PI / 180.0;
        }

        private double sind(double d)
        {
            return Math.Sin(d * Math.PI / 180.0);
        }

        private double cosd(double d)
        {
            return Math.Cos(d * Math.PI / 180.0);
        }

        int d = 0;

        private void button8_Click(object sender, EventArgs e)
        {
            //新建圖檔, 初始化畫布
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;

            //richTextBox1.Text += "已新建圖檔\n";
            //richTextBox1.Text += "畫布大小 : W = " + bitmap1.Width.ToString() + " H = " + bitmap1.Height.ToString() + "\n";

            button2.Enabled = true;
            button3.Enabled = true;
            button4.Enabled = true;
            button5.Enabled = true;
            button7.Enabled = true;
            button9.Enabled = true;
            int x_st = 200;
            int y_st = 200;
            int cx = 200;
            int cy = 200;
            int r = 200;
            int H = r * 2;
            //g.DrawRectangle(Pens.Red, 100, 100, 100, 100);
            //g.DrawEllipse(Pens.Red, x_st, y_st, r, r);
            int dx = (int)(r * cosd(d));
            int dy = (int)(r * sind(d));

            d += 20;

            g.DrawLine(Pens.Red, cx, H - cy, cx + dx, (H - (cy + dy)));
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //馬賽克   TBD
            int block_size = 30;

            int i;
            int xx;
            int yy;
            int r_total = 0;
            int g_total = 0;
            int b_total = 0;
            byte rrr;
            byte ggg;
            byte bbb;

            for (yy = 0; yy < bitmap1.Height / 5; yy++)
            {
                for (xx = 0; xx < bitmap1.Width / 5; xx += 5)
                {
                    r_total = 0;
                    g_total = 0;
                    b_total = 0;

                    for (i = 0; i < block_size; i++)
                    {

                        rrr = bitmap1.GetPixel(xx + i, yy).R;
                        ggg = bitmap1.GetPixel(xx + i, yy).G;
                        bbb = bitmap1.GetPixel(xx + i, yy).B;
                        r_total += rrr;
                        g_total += ggg;
                        b_total += bbb;
                    }

                    Color zz = Color.FromArgb(255, (byte)(r_total / block_size), (byte)(g_total / block_size), (byte)(b_total / block_size));
                    for (i = 0; i < block_size; i++)
                    {
                        bitmap1.SetPixel(xx + i, yy, zz);
                    }
                }
            }

            pictureBox1.Image = bitmap1;

        }

        private void button11_Click(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
        {

        }

        private void button10_Click(object sender, EventArgs e)
        {

        }





    }
}
