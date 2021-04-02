using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;

namespace CrossImage
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

        private void button2_Click(object sender, EventArgs e)
        {
            Image myImage = pictureBox1.Image;
            myImage.RotateFlip(RotateFlipType.Rotate180FlipX);
            pictureBox1.Image = myImage;
        }
    }
}