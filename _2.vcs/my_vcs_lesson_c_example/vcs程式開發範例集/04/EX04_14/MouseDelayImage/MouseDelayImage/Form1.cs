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

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";
            flag = false;
            pictureBox1.Location = new System.Drawing.Point(14, 8);
            Image myImage = System.Drawing.Image.FromFile(filename);
            pictureBox1.Image = myImage;
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if(flag)
                pictureBox1.Location = new System.Drawing.Point(e.X, e.Y);
        }

        private void pictureBox1_MouseEnter(object sender, EventArgs e)
        {
            flag = true;
        }
    }
}