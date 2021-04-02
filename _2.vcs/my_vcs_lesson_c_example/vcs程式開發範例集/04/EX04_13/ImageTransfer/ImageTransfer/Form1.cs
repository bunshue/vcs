using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;

namespace ImageTransfer
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
            Bitmap bitmap = (Bitmap)Bitmap.FromFile(openFileDialog1.FileName);
            pictureBox1.Image = bitmap;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Bitmap bitmap = (Bitmap)Bitmap.FromFile(openFileDialog1.FileName);
            bitmap.RotateFlip(RotateFlipType.Rotate90FlipX);
            pictureBox2.Image = bitmap;
        }
    }
}