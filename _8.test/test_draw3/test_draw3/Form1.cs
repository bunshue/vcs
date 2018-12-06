using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace test_draw3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        Graphics g;
        Pen p;
        SolidBrush sb;
        //Brush b;
        Font f;

        Bitmap bmp;

        Point[] p_Array = { new Point(150, 50), new Point(100, 400), new Point(450, 400), new Point(400, 50) };

        private void Form1_Load(object sender, EventArgs e)
        {
            g = pictureBox1.CreateGraphics();
            p = new Pen(Color.Red, 8);
            sb = new SolidBrush(Color.Blue);
            f = new Font("標楷體", 20);

        }

        private void button5_Click(object sender, EventArgs e)
        {
            bmp = new Bitmap(@"D:\bear.jpg");
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.Image = bmp; //顯示在 pictureBox1 圖片控制項中
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //bmp.Save(@"D:\aaaaaaa.jpg");
            pictureBox1.Image.Save(@"D:\bbbbb.jpg");
        }

        private void button7_Click(object sender, EventArgs e)
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

    
    }
}
