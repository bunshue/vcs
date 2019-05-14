using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_tmp_draw_all
{
    public partial class Form1 : Form
    {
        Bitmap bmp;
        Graphics g;
        Pen p;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bmp = new Bitmap(@"D:\bear.jpg");
            g = Graphics.FromImage(bmp);
            p = new Pen(Color.Red, 10);
            pictureBox1.Image = bmp;

        }

        private void button1_Click(object sender, EventArgs e)
        {
            int pic_width = pictureBox1.Width;
            int pic_height = pictureBox1.Height;
            bmp = new Bitmap(pic_width / 2, pic_height / 2);
            pictureBox1.Image = bmp;
            pictureBox1.BackColor = Color.Red;


        }

        private void button2_Click(object sender, EventArgs e)
        {
            bmp = new Bitmap(@"D:\bear.jpg");
            g = Graphics.FromImage(bmp);
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.Image = bmp; //顯示在 pictureBox1 圖片控制項中
        }

        private void button4_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = bmp;

            g.DrawEllipse(p, 100, 100, 200, 200);
            p = new Pen(Color.Blue, 5);
            g.DrawEllipse(p, 300, 300, 200, 200);

        }

        private void button3_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = bmp;
            g.DrawRectangle(p, 250, 250, 200, 200);

        }

        private void button5_Click(object sender, EventArgs e)
        {
            bmp.Save(@"D:\zzzzz.jpg");
        }

        private void button6_Click(object sender, EventArgs e)
        {
            // bmp 的大小和pictureBox1 相同
            Bitmap bmp = new Bitmap(this.pictureBox1.Width, this.pictureBox1.Height);
            // 以記憶體圖像 bmp 建立 myDraw 記憶體畫布
            Graphics myDraw = Graphics.FromImage(bmp);
            myDraw.Clear(this.pictureBox1.BackColor); //畫布背景色
            myDraw.DrawLine(p, 100, 100, 300, 100);
            //MyDraw.DrawLine(new pen(Color.Red, 2), x, y, e.X, e.Y); //可以繪圖了
            g.DrawImage(bmp, 0, 0);
            bmp.Save(@"D:\3333.jpg");

        }

        private void button7_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = null;
            pictureBox1.Size = new Size(300, 200);
            pictureBox1.BackColor = Color.Yellow;

        }
    }
}
