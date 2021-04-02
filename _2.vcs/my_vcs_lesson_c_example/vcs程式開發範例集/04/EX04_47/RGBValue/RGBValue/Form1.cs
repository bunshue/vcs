using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;

namespace RGBValue
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            openFileDialog1.Filter = "*.jpg,*.jpeg,*.bmp,*.gif,*.ico,*.png,*.tif,*.wmf|*.jpg;*.jpeg;*.bmp;*.gif;*.ico;*.png;*.tif;*.wmf";
            openFileDialog1.ShowDialog();
            Image myImage = System.Drawing.Image.FromFile(openFileDialog1.FileName);
            pictureBox1.Image = myImage;
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            Bitmap bmp = (Bitmap)pictureBox1.Image;
            try
            {
                Color pointColor = bmp.GetPixel(e.X, e.Y);
                textBox1.Text = pointColor.R.ToString();
                textBox2.Text = pointColor.G.ToString();
                textBox3.Text = pointColor.B.ToString();
            }
            catch { }
        }
    }
}