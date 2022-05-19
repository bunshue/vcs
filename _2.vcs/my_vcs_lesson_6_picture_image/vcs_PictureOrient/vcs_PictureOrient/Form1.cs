using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_PictureOrient
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\orient1.jpg";

            // Open the file.
            using (Bitmap bm = new Bitmap(filename))
            {
                // Display the original image.
                Bitmap original_bm = new Bitmap(bm);
                pictureBox1.Image = original_bm;

                // Display the image property oriented.
                // Note: If you use new Bitmap(bm) to make the copy,
                //       then the EXIF properties are lost. Clone instead.
                Bitmap oriented_bm = (Bitmap)bm.Clone();
                ExifStuff.OrientImage(oriented_bm);
                pictureBox2.Image = oriented_bm;
            }


        }


    }
}
