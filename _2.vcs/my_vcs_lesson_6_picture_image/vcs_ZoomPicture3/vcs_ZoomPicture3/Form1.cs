using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//調整 pictureBox1 大小，用zoom模式顯示圖片

namespace vcs_ZoomPicture3
{
    public partial class Form1 : Form
    {
        private int width;
        private int height;
        private float ImageScale = 1.0f; //縮放比例

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            //same
            //Image img = Image.FromFile(filename);
            //pictureBox1.Image = img;

            //same
            //pictureBox1.Image = Image.FromFile(filename); //載入圖檔，由檔案

            //same
            //Bitmap bitmap1 = new Bitmap(filename);
            //pictureBox1.Image = bitmap1;

            //same
            //Image img = Bitmap.FromFile(filename);
            //pictureBox1.Image = img;

            //same
            //Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);
            //pictureBox1.Image = bitmap1;

            //same
            pictureBox1.Image = new Bitmap(filename);

            //pictureBox1.ImageLocation = filename;   //可顯示圖片 但無法抓出圖片的相關資訊

            width = pictureBox1.Image.Width;
            height = pictureBox1.Image.Height;
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.Size = new Size(width, height);
            pictureBox1.Location = new Point(0, 0);
            this.MouseWheel += new MouseEventHandler(pictureBox1_MouseWheel);
            this.ClientSize = new Size(pictureBox1.Size.Width, pictureBox1.Size.Height);
        }

        // Respond to the mouse wheel.
        private void pictureBox1_MouseWheel(object sender, MouseEventArgs e)
        {
            // The amount by which we adjust scale per wheel click.
            const float scale_per_delta = 0.1f / 120;

            // Update the drawing based upon the mouse wheel scrolling.
            ImageScale += e.Delta * scale_per_delta;
            if (ImageScale < 0)
            {
                ImageScale = 0;
            }

            // Size the image.
            pictureBox1.Size = new Size(
                (int)(width * ImageScale),
                (int)(height * ImageScale));

            this.ClientSize = new Size(pictureBox1.Size.Width, pictureBox1.Size.Height);

            this.Text = "縮放比例 : " + ImageScale.ToString("p0");
        }
    }
}
