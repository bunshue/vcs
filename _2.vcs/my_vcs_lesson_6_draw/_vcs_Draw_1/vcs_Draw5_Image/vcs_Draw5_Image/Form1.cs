using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Draw5_Image
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;

        string filename = @"C:\______test_files\picture1.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            pictureBox_old.Image = Image.FromFile(filename); //載入圖檔，由檔案

            p = new Pen(Color.Red, 3);

            //指定畫布大小
            pictureBox1.Width = 710;
            pictureBox1.Height = 700;
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.DrawRectangle(p, 0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1);
            pictureBox1.Image = bitmap1;
        }

        void show_item_location()
        {
            int x_st = 14;
            int y_st = 12;
            int dx = 100;
            int dy = 45;

            button1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 6);

            bt_clear.Location = new Point(x_st + dx * 0, y_st + dy * 8);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //載入圖檔，由檔案
            Bitmap bmp = new Bitmap(filename);
            Image img = Image.FromFile(filename);

            int x_st = 20;
            int y_st = 20;
            int dx = 180;
            int dy = 90;

            //原圖貼上
            //               貼上位置x      貼上位置y      貼上大小W            貼上大小H
            g.DrawImage(bmp, x_st + dx * 0, y_st + dy * 0, bmp.Width * 12 / 10, bmp.Height * 12 / 10);
            g.DrawImage(bmp, x_st + dx * 1, y_st + dy * 0, bmp.Width * 10 / 10, bmp.Height * 10 / 10);
            g.DrawImage(bmp, x_st + dx * 2, y_st + dy * 0, bmp.Width * 6 / 10, bmp.Height * 6 / 10);
            g.DrawImage(bmp, x_st + dx * 3, y_st + dy * 0, bmp.Width * 4 / 10, bmp.Height * 4 / 10);

            g.DrawImage(img, x_st + dx * 0, y_st + dy * 2, img.Width * 12 / 10, img.Height * 12 / 10);
            g.DrawImage(img, x_st + dx * 1, y_st + dy * 2, img.Width * 10 / 10, img.Height * 10 / 10);
            g.DrawImage(img, x_st + dx * 2, y_st + dy * 2, img.Width * 6 / 10, img.Height * 6 / 10);
            g.DrawImage(img, x_st + dx * 3, y_st + dy * 2, img.Width * 4 / 10, img.Height * 4 / 10);

            g.DrawImage(img, x_st + dx * 3 + 30, y_st + dy * 4 - 10, img.Width * 3 / 10, img.Height * 8 / 10);  //改變貼上比例

            //決定繪製影像的縮放比例和切變
            x_st = 400;
            y_st = 470;
            int w = bmp.Width / 2;
            int h = bmp.Height / 2;
            // Create parallelogram for drawing image.
            Point ulCorner = new Point(x_st + 50, y_st);   //左上
            Point urCorner = new Point(x_st + 50 + w, y_st);   //右上
            Point llCorner = new Point(x_st, y_st + h);   //左下
            Point[] destPara = { ulCorner, urCorner, llCorner };
            // Draw image to screen.
            g.DrawImage(bmp, destPara);

            //使用Rectangle結構
            // Create rectangle for displaying image.
            Rectangle destRect = new Rectangle(0, 0, bmp.Width / 3, bmp.Height / 3);
            // Draw image to screen.
            g.DrawImage(bmp, destRect);

            g.DrawString("原圖貼上", new Font("Arial", 80), Brushes.Red, new PointF(200, 260));
            pictureBox1.Image = bitmap1;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Image img = Image.FromFile(filename);
            int W = img.Width;
            int H = img.Height;

            int sx = 130;
            int sy = 110;
            int sw = W / 3;
            int sh = H / 3;

            //舊圖上標明位置
            Graphics g_old = pictureBox_old.CreateGraphics();
            //標示下一步要擷取的區域
            g_old.DrawRectangle(new Pen(Color.Red, 2), new Rectangle(sx, sy, sw, sh));

            int x_st = 20;
            int y_st = 250;

            //原圖貼上
            //             貼上位置x,貼上位置y,貼上大小W,貼上大小H
            g.DrawImage(img, x_st, y_st, W * 10 / 10, H * 10 / 10);

            // Create rectangle for source image.
            //Rectangle srcRect = new Rectangle(0, 0, W, H); //擷取全圖
            Rectangle srcRect = new Rectangle(sx, sy, sw, sh);   //擷取部分區域
            GraphicsUnit units = GraphicsUnit.Pixel;

            x_st = 20;
            y_st = 70;

            int i;
            int j = 8;
            for (i = 0; i < 600; i += 130)
            {
                x_st = i + 20;
                //y_st += i;
                //richTextBox1.Text += "x_st = " + x_st.ToString() + ", y_st = " + y_st.ToString() + ", j = " + j.ToString() + "\n";
                // 準備貼上的位置與放大縮小量,以平行四邊形(parallelogram)的左上點右上點左下點表示
                Point ulCorner = new Point(x_st, y_st);
                Point urCorner = new Point(x_st + sw * j / 10, y_st);
                Point llCorner = new Point(x_st, y_st + sh * j / 10);
                j += 2;

                Point[] destRect1 = { ulCorner, urCorner, llCorner };

                //擷取部分圖片貼上
                //            貼上位置與大小,擷取部分圖片位置與大小,單位
                g.DrawImage(img, destRect1, srcRect, units);
            }


            x_st = 450;
            y_st = 250;

            //擷取部分圖片[非矩形]貼上
            Point ulCorner2 = new Point(x_st, y_st);
            Point urCorner2 = new Point(x_st + sw * 4 / 2, y_st);
            Point llCorner2 = new Point(x_st - 100, y_st + sh * 4 / 2);
            Point[] destRect2 = { ulCorner2, urCorner2, llCorner2 };

            //richTextBox1.Text += "x_st = " + x_st.ToString() + ", y_st = " + y_st.ToString() + ", j = " + j.ToString() + "\n";

            //擷取部分圖片貼上
            //            貼上位置與大小,擷取部分圖片位置與大小,單位
            g.DrawImage(img, destRect2, srcRect, units);

            Rectangle destRect3 = new Rectangle(350, 530, 350, 150);
            sx = 50;
            sy = 50;
            sw = 150;
            sh = 150;

            g.DrawImage(img, destRect3, sx, sy, sw, sh, units);


            //來源矩形的大小會決定要將未縮放原始影像的哪個部分繪製到螢幕上。
            // Create coordinates for upper-left corner of image.
            int x = 0;  //貼上位置
            int y = 200;
            // Create rectangle for source image.
            Rectangle srcRect2 = new Rectangle(50, 50, 150, 150);   //來源矩形
            // Draw image to screen.
            g.DrawImage(img, x, y, srcRect2, units);

            int dx;
            int dy;
            int dw;
            int dh;

            //使用兩個Rectangle結構
            //source
            sx = 100;
            sy = 100;
            sw = 100;
            sh = 50;
            //destination
            dx = 200;
            dy = 250;
            dw = 200;
            dh = 100;

            // Create rectangle for displaying image.
            Rectangle destRect = new Rectangle(dx, dy, dw, dh);

            // Create rectangle for source image.
            Rectangle srcRect3 = new Rectangle(sx, sy, sw, sh);

            // Draw image to screen.
            g.DrawImage(img, destRect, srcRect3, units);

            pictureBox1.Image = bitmap1;

            g.DrawString("擷取部分圖片貼上", new Font("Arial", 50), Brushes.Red, new PointF(100, 400));
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //改變Bitmap大小
            //Bitmap bmp = new Bitmap(@"C:\______test_files\ims_image.bmp", true);
            Bitmap bmp = new Bitmap(filename, true);
            Bitmap bmp_zoom;

            int i;
            for (i = 15; i > 5; i--)
            {
                //將圖片縮放
                bmp_zoom = new Bitmap(bmp, bmp.Width * i / 10, bmp.Height * i / 10);   //用Bitmap直接進行縮放，比例自行調整
                g.DrawImage(bmp_zoom, 0, 0);
            }

            pictureBox1.Image = bitmap1;

            g.DrawString("改變Bitmap大小,\n貼在原點", new Font("Arial", 50), Brushes.Red, new PointF(100, 400));
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //改變Bitmap大小
            Bitmap bmp = new Bitmap(filename, true);
            Bitmap bmp_zoom;

            bmp_zoom = new Bitmap(bmp, bmp.Width, bmp.Height);

            g.DrawImage(bmp_zoom, 0, 0);    //zoom後再貼, 大小正確

            g.DrawImage(bmp, 0, 0);         //不zoom直接貼, 大小不對
            g.DrawImage(bmp, 350, 50, bmp.Width, bmp.Height);         //不zoom直接貼, 指名大小位置, 大小正確
            g.DrawImage(bmp, 350, 480, bmp.Width, bmp.Height / 2);         //不zoom直接貼, 指名大小位置, 大小正確, 改變貼上的圖片大小

            g.DrawRectangle(new Pen(Color.Green, 3), new Rectangle(0, 0, bmp.Width, bmp.Height));

            pictureBox1.Image = bitmap1;

            g.DrawString("有無zoom的比較", new Font("Arial", 50), Brushes.Red, new PointF(100, 450));

        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

    }
}
