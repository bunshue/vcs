using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace test_paint
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        Bitmap bmp;
        Graphics Draw;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            g = this.CreateGraphics();
            p = new Pen(Color.Red, 10);
            bmp = new Bitmap(this.Width, this.Height);
            Draw = Graphics.FromImage(bmp);
            Draw.Clear(BackColor);

        }

        private void button1_Click(object sender, EventArgs e)
        {
            g.DrawImage(bmp, 0, 0);
            g.DrawLine(p, 100, 100, 300, 300);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            //g.DrawImage(bmp, 0, 0);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            bmp.Save(@"D:\ssss.jpg");
        }

        private void button3_Click(object sender, EventArgs e)
        {
            bmp = new Bitmap(@"D:\bear.jpg");
            Draw = Graphics.FromImage(bmp);
            this.Size = bmp.Size;
            g = this.CreateGraphics();
            g.DrawImage(bmp, 0, 0);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            bmp = new Bitmap(500, 400);
            Draw = Graphics.FromImage(bmp);
            Draw.Clear(BackColor);
            this.Size = bmp.Size;
            g = this.CreateGraphics();
            g.DrawImage(bmp, 0, 0);


        }
    }
}
