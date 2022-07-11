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
            Bitmap bitmap1 = new Bitmap(filename);//加載圖像
            //g.FillRectangle(Brushes.White, this.pictureBox1.ClientRectangle);//填充窗體背景爲白色, 清空pictureBox
            Point[] destinationPoints = {
new Point(400, 0), // destination for upper-left point of original
new Point(400, 305),// destination for upper-right point of original
new Point(0, 0)}; // destination for lower-left point of original
            g.DrawImage(bitmap1, destinationPoints);

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //旋轉圖像180°
            Graphics g = this.pictureBox1.CreateGraphics();
            Bitmap bitmap1 = new Bitmap(filename);
            //g.FillRectangle(Brushes.White, this.pictureBox1.ClientRectangle);//填充窗體背景爲白色, 清空pictureBox
            Point[] destinationPoints = {
new Point(0, 400), // destination for upper-left point of original
new Point(305, 400),// destination for upper-right point of original
new Point(0, 0)}; // destination for lower-left point of original
            g.DrawImage(bitmap1, destinationPoints);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //圖像切變

            Graphics g = this.pictureBox1.CreateGraphics();
            Bitmap bitmap1 = new Bitmap(filename);
            //g.FillRectangle(Brushes.White, this.pictureBox1.ClientRectangle);//填充窗體背景爲白色, 清空pictureBox
            Point[] destinationPoints = {
new Point(0, 0), // destination for upper-left point of original
new Point(305, 0), // destination for upper-right point of original
new Point(100, 400)};// destination for lower-left point of original
            g.DrawImage(bitmap1, destinationPoints);

        }

        private void button3_Click(object sender, EventArgs e)
        {
            //圖像截取

            Graphics g = this.pictureBox1.CreateGraphics();
            Bitmap bitmap1 = new Bitmap(filename);
            //g.FillRectangle(Brushes.White, this.pictureBox1.ClientRectangle);//填充窗體背景爲白色, 清空pictureBox
            Rectangle sr = new Rectangle(80, 60, 400, 400);//要截取的矩形區域
            Rectangle dr = new Rectangle(0, 0, 200, 200);//要顯示到Form的矩形區域
            g.DrawImage(bitmap1, dr, sr, GraphicsUnit.Pixel);



        }

        private void button4_Click(object sender, EventArgs e)
        {
            //改變圖像大小

            Graphics g = this.pictureBox1.CreateGraphics();
            Bitmap bitmap1 = new Bitmap(filename);
            //g.FillRectangle(Brushes.White, this.pictureBox1.ClientRectangle);//填充窗體背景爲白色, 清空pictureBox
            int width = bitmap1.Width;
            int height = bitmap1.Height;
            // 改變圖像大小使用低質量的模式
            g.InterpolationMode = InterpolationMode.NearestNeighbor;
            g.DrawImage(bitmap1, new Rectangle(10, 10, 120, 120), // source rectangle

            new Rectangle(0, 0, width, height), // destination rectangle
            GraphicsUnit.Pixel);
            // 使用高質量模式
            //g.CompositingQuality = CompositingQuality.HighSpeed;
            g.InterpolationMode = InterpolationMode.HighQualityBicubic;
            g.DrawImage(
            bitmap1,
            new Rectangle(130, 10, 120, 120),
            new Rectangle(0, 0, width, height),
            GraphicsUnit.Pixel);

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

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {

        }
    }
}

