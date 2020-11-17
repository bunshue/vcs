using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_RotatePicture1
{
    public partial class Form1 : Form
    {
        // The image's original size.
        private int width;
        private int height;

        // The current scale.
        private float ImageScale = 1.0f;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename = "C:\\______test_files\\picture1.jpg";
            Image loadedImage = Image.FromFile(filename);
            pictureBox1.Image = loadedImage;



            width = pictureBox1.Image.Width;
            height = pictureBox1.Image.Height;
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.Size = new Size(width, height);
            this.MouseWheel += new MouseEventHandler(pictureBox1_MouseWheel);
        }

        // Respond to the mouse wheel.
        private void pictureBox1_MouseWheel(object sender, MouseEventArgs e)
        {
            // The amount by which we adjust scale per wheel click.
            const float scale_per_delta = 0.1f / 120;

            // Update the drawing based upon the mouse wheel scrolling.
            ImageScale += e.Delta * scale_per_delta;
            if (ImageScale < 0) ImageScale = 0;

            // Size the image.
            pictureBox1.Size = new Size(
                (int)(width * ImageScale),
                (int)(height * ImageScale));

            // Display the new scale.
            this.Text = "縮放比例 : " + ImageScale.ToString("p0");
        }

    }
}
