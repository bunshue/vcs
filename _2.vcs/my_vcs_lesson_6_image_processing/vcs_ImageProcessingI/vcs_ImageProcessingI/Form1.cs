using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;
using System.Drawing.Drawing2D;

//C#圖像處理(各種旋轉、改變大小、柔化、銳化、霧化、底片、浮雕、黑白、濾鏡效果)

namespace vcs_ImageProcessingI
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\picture1.jpg";
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox1.Image = Image.FromFile(filename);

            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 130 + 10;
            dy = 50 + 10;

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
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //向右旋轉圖像90°
            Graphics g = this.pictureBox1.CreateGraphics();
            Bitmap bmp = new Bitmap(filename);//加載圖像
            //g.FillRectangle(Brushes.White, this.pictureBox1.ClientRectangle);//填充窗體背景爲白色, 清空pictureBox
            Point[] destinationPoints = {
new Point(400, 0), // destination for upper-left point of original
new Point(400, 305),// destination for upper-right point of original
new Point(0, 0)}; // destination for lower-left point of original
            g.DrawImage(bmp, destinationPoints);

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //旋轉圖像180°
            Graphics g = this.pictureBox1.CreateGraphics();
            Bitmap bmp = new Bitmap(filename);
            //g.FillRectangle(Brushes.White, this.pictureBox1.ClientRectangle);//填充窗體背景爲白色, 清空pictureBox
            Point[] destinationPoints = {
new Point(0, 400), // destination for upper-left point of original
new Point(305, 400),// destination for upper-right point of original
new Point(0, 0)}; // destination for lower-left point of original
            g.DrawImage(bmp, destinationPoints);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //圖像切變

            Graphics g = this.pictureBox1.CreateGraphics();
            Bitmap bmp = new Bitmap(filename);
            //g.FillRectangle(Brushes.White, this.pictureBox1.ClientRectangle);//填充窗體背景爲白色, 清空pictureBox
            Point[] destinationPoints = {
new Point(0, 0), // destination for upper-left point of original
new Point(305, 0), // destination for upper-right point of original
new Point(100, 400)};// destination for lower-left point of original
            g.DrawImage(bmp, destinationPoints);

        }

        private void button3_Click(object sender, EventArgs e)
        {
            //圖像截取

            Graphics g = this.pictureBox1.CreateGraphics();
            Bitmap bmp = new Bitmap(filename);
            //g.FillRectangle(Brushes.White, this.pictureBox1.ClientRectangle);//填充窗體背景爲白色, 清空pictureBox
            Rectangle sr = new Rectangle(80, 60, 400, 400);//要截取的矩形區域
            Rectangle dr = new Rectangle(0, 0, 200, 200);//要顯示到Form的矩形區域
            g.DrawImage(bmp, dr, sr, GraphicsUnit.Pixel);



        }

        private void button4_Click(object sender, EventArgs e)
        {
            //改變圖像大小

            Graphics g = this.pictureBox1.CreateGraphics();
            Bitmap bmp = new Bitmap(filename);
            //g.FillRectangle(Brushes.White, this.pictureBox1.ClientRectangle);//填充窗體背景爲白色, 清空pictureBox
            int width = bmp.Width;
            int height = bmp.Height;
            // 改變圖像大小使用低質量的模式
            g.InterpolationMode = InterpolationMode.NearestNeighbor;
            g.DrawImage(bmp, new Rectangle(10, 10, 120, 120), // source rectangle

            new Rectangle(0, 0, width, height), // destination rectangle
            GraphicsUnit.Pixel);
            // 使用高質量模式
            //g.CompositingQuality = CompositingQuality.HighSpeed;
            g.InterpolationMode = InterpolationMode.HighQualityBicubic;
            g.DrawImage(
            bmp,
            new Rectangle(130, 10, 120, 120),
            new Rectangle(0, 0, width, height),
            GraphicsUnit.Pixel);

        }

        private void button5_Click(object sender, EventArgs e)
        {
            //設置圖像的分辨率

            Graphics g = this.pictureBox1.CreateGraphics();
            Bitmap bmp = new Bitmap(filename);
            //g.FillRectangle(Brushes.White, this.pictureBox1.ClientRectangle);//填充窗體背景爲白色, 清空pictureBox
            bmp.SetResolution(300f, 300f);
            g.DrawImage(bmp, 0, 0);
            bmp.SetResolution(1200f, 1200f);
            g.DrawImage(bmp, 180, 0);

        }

        private void button6_Click(object sender, EventArgs e)
        {
            //用GDI+畫圖

            Graphics g = this.pictureBox1.CreateGraphics();
            g.FillRectangle(Brushes.White, this.ClientRectangle);
            for (int i = 1; i <= 7; ++i)
            {
                //在窗體上面畫出橙色的矩形

                Rectangle r = new Rectangle(i * 40 - 15, 0, 15,
                this.ClientRectangle.Height);
                g.FillRectangle(Brushes.Orange, r);
            }
            //在內存中創建一個Bitmap並設置CompositingMode
            Bitmap bmp = new Bitmap(260, 260,

            System.Drawing.Imaging.PixelFormat.Format32bppArgb);
            Graphics gBmp = Graphics.FromImage(bmp);
            gBmp.CompositingMode = System.Drawing.Drawing2D.CompositingMode.SourceCopy;
            // 創建一個帶有Alpha的紅色區域
            // 並將其畫在內存的位圖裏面
            Color red = Color.FromArgb(0x60, 0xff, 0, 0);
            Brush redBrush = new SolidBrush(red);
            gBmp.FillEllipse(redBrush, 70, 70, 160, 160);
            // 創建一個帶有Alpha的綠色區域
            Color green = Color.FromArgb(0x40, 0, 0xff, 0);
            Brush greenBrush = new SolidBrush(green);
            gBmp.FillRectangle(greenBrush, 10, 10, 140, 140);
            //在窗體上面畫出位圖 now draw the bitmap on our window
            g.DrawImage(bmp, 20, 20, bmp.Width, bmp.Height);
            // 清理資源
            bmp.Dispose();
            gBmp.Dispose();
            redBrush.Dispose();
            greenBrush.Dispose();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //在窗體上面繪圖並顯示圖像
            Graphics g = this.pictureBox1.CreateGraphics();
            Pen blackPen = new Pen(Color.Black, 1);

            if (ClientRectangle.Height / 10 > 0)
            {

                for (int y = 0; y < ClientRectangle.Height; y += ClientRectangle.Height / 10)
                {

                    g.DrawLine(blackPen, new Point(0, 0), new Point(ClientRectangle.Width, y));

                }

            }

            blackPen.Dispose();
        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {

        }
    }
}

