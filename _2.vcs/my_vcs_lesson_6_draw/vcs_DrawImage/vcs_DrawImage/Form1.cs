using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_DrawImage
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
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox_old.Image = Image.FromFile("c:\\______test_files\\picture1.jpg"); //載入圖檔，由檔案

            p = new Pen(Color.Red, 3);

            //指定畫布大小
            pictureBox1.Width = 710;
            pictureBox1.Height = 700;
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.DrawRectangle(p, 0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1);
            pictureBox1.Image = bitmap1;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //載入圖檔，由檔案
            Bitmap bmp = new Bitmap("c:\\______test_files\\picture1.jpg");
            Image img = Image.FromFile("c:\\______test_files\\picture1.jpg");

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

            g.DrawString("原圖貼上", new Font("Arial", 80), Brushes.Red, new PointF(200, 260));

            pictureBox1.Image = bitmap1;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Image img = Image.FromFile("c:\\______test_files\\picture1.jpg");

            int x_st = 20;
            int y_st = 250;

            //原圖貼上
            //             貼上位置x,貼上位置y,貼上大小W,貼上大小H
            g.DrawImage(img, x_st, y_st, img.Width * 10 / 10, img.Height * 10 / 10);

            int W = img.Width;
            int H = img.Height;

            int sx = 130;
            int sy = 110;
            int sw = W / 3;
            int sh = H / 3;

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

                Point[] destRect = { ulCorner, urCorner, llCorner };

                //擷取部分圖片貼上
                //            貼上位置與大小,擷取部分圖片位置與大小,單位
                g.DrawImage(img, destRect, srcRect, units);
            }


            x_st = 450;
            y_st = 350;

            //擷取部分圖片[非矩形]貼上
            Point ulCorner2 = new Point(x_st, y_st);
            Point urCorner2 = new Point(x_st + sw * 4 / 2, y_st);
            Point llCorner2 = new Point(x_st - 100, y_st + sh * 4 / 2);
            Point[] destRect2 = { ulCorner2, urCorner2, llCorner2 };

            //richTextBox1.Text += "x_st = " + x_st.ToString() + ", y_st = " + y_st.ToString() + ", j = " + j.ToString() + "\n";

            //擷取部分圖片貼上
            //            貼上位置與大小,擷取部分圖片位置與大小,單位
            g.DrawImage(img, destRect2, srcRect, units);



            pictureBox1.Image = bitmap1;

            g.DrawString("擷取部分圖片貼上", new Font("Arial", 50), Brushes.Red, new PointF(100, 400));
        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;
        }

    }
}
