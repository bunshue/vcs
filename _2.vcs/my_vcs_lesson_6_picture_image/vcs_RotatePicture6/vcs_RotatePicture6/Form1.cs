using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_RotatePicture6
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Copy the bitmap, rotate it, and return the result.
        private Bitmap ModifiedBitmap(Image image, RotateFlipType rotate_flip_type)
        {
            // Copy the Bitmap.
            Bitmap bitmap1 = new Bitmap(image);

            // Rotate and flip.
            bitmap1.RotateFlip(rotate_flip_type);

            // Return the result.
            return bitmap1;
        }

        private void rad180FlipNone_CheckedChanged(object sender, EventArgs e)
        {
            pictureBox2.Image = ModifiedBitmap(pictureBox1.Image, RotateFlipType.Rotate180FlipNone);
        }
        private void rad180FlipX_CheckedChanged(object sender, EventArgs e)
        {
            pictureBox2.Image = ModifiedBitmap(pictureBox1.Image, RotateFlipType.Rotate180FlipX);
        }
        private void rad180FlipXY_CheckedChanged(object sender, EventArgs e)
        {
            pictureBox2.Image = ModifiedBitmap(pictureBox1.Image, RotateFlipType.Rotate180FlipXY);
        }
        private void rad180FlipY_CheckedChanged(object sender, EventArgs e)
        {
            pictureBox2.Image = ModifiedBitmap(pictureBox1.Image, RotateFlipType.Rotate180FlipY);
        }
        private void rad270FlipNone_CheckedChanged(object sender, EventArgs e)
        {
            pictureBox2.Image = ModifiedBitmap(pictureBox1.Image, RotateFlipType.Rotate270FlipNone);
        }
        private void rad270FlipX_CheckedChanged(object sender, EventArgs e)
        {
            pictureBox2.Image = ModifiedBitmap(pictureBox1.Image, RotateFlipType.Rotate270FlipX);
        }
        private void rad270FlipXY_CheckedChanged(object sender, EventArgs e)
        {
            pictureBox2.Image = ModifiedBitmap(pictureBox1.Image, RotateFlipType.Rotate270FlipXY);
        }
        private void rad270FlipY_CheckedChanged(object sender, EventArgs e)
        {
            pictureBox2.Image = ModifiedBitmap(pictureBox1.Image, RotateFlipType.Rotate270FlipY);
        }
        private void rad90FlipNone_CheckedChanged(object sender, EventArgs e)
        {
            pictureBox2.Image = ModifiedBitmap(pictureBox1.Image, RotateFlipType.Rotate90FlipNone);
        }
        private void rad90FlipX_CheckedChanged(object sender, EventArgs e)
        {
            pictureBox2.Image = ModifiedBitmap(pictureBox1.Image, RotateFlipType.Rotate90FlipX);
        }
        private void rad90FlipXY_CheckedChanged(object sender, EventArgs e)
        {
            pictureBox2.Image = ModifiedBitmap(pictureBox1.Image, RotateFlipType.Rotate90FlipXY);
        }
        private void rad90FlipY_CheckedChanged(object sender, EventArgs e)
        {
            pictureBox2.Image = ModifiedBitmap(pictureBox1.Image, RotateFlipType.Rotate90FlipY);
        }
        private void radNoneFlipNone_CheckedChanged(object sender, EventArgs e)
        {
            pictureBox2.Image = ModifiedBitmap(pictureBox1.Image, RotateFlipType.RotateNoneFlipNone);
        }
        private void radNoneFlipX_CheckedChanged(object sender, EventArgs e)
        {
            pictureBox2.Image = ModifiedBitmap(pictureBox1.Image, RotateFlipType.RotateNoneFlipX);
        }
        private void radNoneFlipXY_CheckedChanged(object sender, EventArgs e)
        {
            pictureBox2.Image = ModifiedBitmap(pictureBox1.Image, RotateFlipType.RotateNoneFlipXY);
        }
        private void radNoneFlipY_CheckedChanged(object sender, EventArgs e)
        {
            pictureBox2.Image = ModifiedBitmap(pictureBox1.Image, RotateFlipType.RotateNoneFlipY);
        }
    }
}

