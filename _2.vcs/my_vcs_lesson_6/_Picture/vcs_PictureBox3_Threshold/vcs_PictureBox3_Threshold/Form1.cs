using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageAttributes

namespace vcs_PictureBox3_Threshold
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Set an initial value.
        private void Form1_Load(object sender, EventArgs e)
        {
            trackBar1.Value = 50;
            AdjustImage();
        }

        // Perform the adjustment.
        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            AdjustImage();
        }

        // Perform the threshold adjustment and display the result.
        private void AdjustImage()
        {
            label2.Text = "Threshold = " + (trackBar1.Value / 100.0).ToString();
            pictureBox2.Image = AdjustThreshold(pictureBox1.Image, (float)(trackBar1.Value / 100.0));
        }

        // Perform threshold adjustment on the image.
        private Bitmap AdjustThreshold(Image image, float threshold)
        {
            // Make the result bitmap.
            Bitmap bm = new Bitmap(image.Width, image.Height);

            // Make the ImageAttributes object and set the threshold.
            ImageAttributes attributes = new ImageAttributes();
            attributes.SetThreshold(threshold);

            // Draw the image onto the new bitmap while applying the new ColorMatrix.
            Point[] points =
            {
                new Point(0, 0),
                new Point(image.Width, 0),
                new Point(0, image.Height),
            };
            Rectangle rect = new Rectangle(0, 0, image.Width, image.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.DrawImage(image, points, rect, GraphicsUnit.Pixel, attributes);
            }

            // Return the result.
            return bm;
        }

    }
}
