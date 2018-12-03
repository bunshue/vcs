using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace aaaaaa
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

        private void button1_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = bmp;

            g.DrawEllipse(p, 100, 100, 200, 200);
            p = new Pen(Color.Blue, 5);
            g.DrawEllipse(p, 300, 300, 200, 200);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            bmp.Save(@"D:\zzzzz.jpg");

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bmp = new Bitmap(@"D:\bear.jpg");
            g = Graphics.FromImage(bmp);
            p = new Pen(Color.Red, 10);
            pictureBox1.Image = bmp;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = bmp;
            g.DrawRectangle(p, 250, 250, 200, 200);

        }

        private void button5_Click(object sender, EventArgs e)
        {
            bmp = new Bitmap(@"D:\bear.jpg");
            g = Graphics.FromImage(bmp);
            pictureBox1.Image = bmp;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            int pic_width = pictureBox1.Width;
            int pic_height = pictureBox1.Height;
            bmp = new Bitmap(pic_width / 2, pic_height / 2);
            pictureBox1.Image = bmp;
            pictureBox1.BackColor = Color.Red;
        }
    }
}
