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
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
        }

        private void button3_Click(object sender, EventArgs e)
        {
            bmp = new Bitmap(@"C:\______test_vcs\bear.jpg");
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
