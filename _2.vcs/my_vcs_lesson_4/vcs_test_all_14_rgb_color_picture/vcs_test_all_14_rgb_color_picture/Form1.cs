using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_test_all_14_rgb_color_picture
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Image myImage = System.Drawing.Image.FromFile("C:\\______test_vcs\\bear.bmp");
            pictureBox1.Image = myImage;
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            //好像沒有很準～～～～～
            Bitmap bmp = (Bitmap)pictureBox1.Image;
            try
            {
                Color pointColor = bmp.GetPixel(e.X, e.Y);
                textBox1.Text = pointColor.R.ToString();
                textBox2.Text = pointColor.G.ToString();
                textBox3.Text = pointColor.B.ToString();
                panel1.BackColor = Color.FromArgb(pointColor.R, pointColor.G, pointColor.B);
            }
            catch { }


        }
    }
}
