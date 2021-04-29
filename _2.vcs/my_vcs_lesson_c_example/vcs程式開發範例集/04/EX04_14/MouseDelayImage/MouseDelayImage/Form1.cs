using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;

namespace MouseDelayImage
{
    public partial class Form1 : Form
    {
        bool flag = false;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";
            pictureBox1.Location = new System.Drawing.Point(10, 10);
            Image image = System.Drawing.Image.FromFile(filename);
            pictureBox1.Image = image;
            pictureBox1.Size = new Size(image.Width, image.Height);
        }

        private void pictureBox1_MouseEnter(object sender, EventArgs e)
        {
            flag = true;
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag == true)
            {
                pictureBox1.Location = new System.Drawing.Point(e.X, e.Y);
            }
        }
    }
}
