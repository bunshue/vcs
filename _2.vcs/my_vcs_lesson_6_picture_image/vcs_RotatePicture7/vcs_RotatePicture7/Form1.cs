using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_RotatePicture7
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\picture1.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox1.Image = Image.FromFile(filename);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "圖片轉向\n";

            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);
            pictureBox1.Image = bitmap1;

            Bitmap bitmap2 = (Bitmap)Bitmap.FromFile(filename);
            bitmap2.RotateFlip(RotateFlipType.Rotate90FlipX);
            pictureBox2.Image = bitmap2;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "圖片旋轉, 可連續旋轉\n";
            Image image = pictureBox1.Image;
            image.RotateFlip(RotateFlipType.Rotate90FlipXY);
            pictureBox1.Image = image;

        }

    }
}
