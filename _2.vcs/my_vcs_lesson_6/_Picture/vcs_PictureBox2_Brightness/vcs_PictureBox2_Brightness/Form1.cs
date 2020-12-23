using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageAttributes

namespace vcs_PictureBox2_Brightness
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
            trackBar1.Value = 10;
            AdjustImage();
        }

        // Perform the adjustment.
        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            AdjustImage();
        }

        // Perform the gamma adjustment and display the result.
        private void AdjustImage()
        {
            //label2.Text = "Gamma = " + (trackBar1.Value / 10.0).ToString();
            //pictureBox2.Image = AdjustGamma(pictureBox1.Image, (float)(trackBar1.Value / 10.0));

            label2.Text = "Brightness = " + (trackBar1.Value / 10.0).ToString();
            pictureBox2.Image = AdjustBrightness(pictureBox1.Image, (float)(trackBar1.Value / 10.0));



            //lblBrightness.Text = "Brightness = " + (scrBrightness.Value / 100.0).ToString();
            //picAdjusted.Image = AdjustBrightness(picOriginal.Image, (float)(scrBrightness.Value / 100.0));


        }


        // Adjust the image's brightness.
        private Bitmap AdjustBrightness(Image image, float brightness)
        {
            // Make the ColorMatrix.
            float b = brightness;
            ColorMatrix cm = new ColorMatrix(new float[][]
                {
                    new float[] {b, 0, 0, 0, 0},
                    new float[] {0, b, 0, 0, 0},
                    new float[] {0, 0, b, 0, 0},
                    new float[] {0, 0, 0, 1, 0},
                    new float[] {0, 0, 0, 0, 1},
                });
            ImageAttributes attributes = new ImageAttributes();
            attributes.SetColorMatrix(cm);

            // Draw the image onto the new bitmap while applying the new ColorMatrix.
            Point[] points =
            {
                new Point(0, 0),
                new Point(image.Width, 0),
                new Point(0, image.Height),
            };
            Rectangle rect = new Rectangle(0, 0, image.Width, image.Height);

            // Make the result bitmap.
            Bitmap bm = new Bitmap(image.Width, image.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.DrawImage(image, points, rect, GraphicsUnit.Pixel, attributes);
            }

            // Return the result.
            return bm;
        }


        // Perform gamma correction on the image.
        private Bitmap AdjustGamma(Image image, float gamma)
        {
            // Set the ImageAttributes object's gamma value.
            ImageAttributes attributes = new ImageAttributes();
            attributes.SetGamma(gamma);

            // Draw the image onto the new bitmap while applying the new gamma value.
            Point[] points =
            {
                new Point(0, 0),
                new Point(image.Width, 0),
                new Point(0, image.Height),
            };
            Rectangle rect = new Rectangle(0, 0, image.Width, image.Height);

            // Make the result bitmap.
            Bitmap bm = new Bitmap(image.Width, image.Height);
            using (Graphics g = Graphics.FromImage(bm))
            {
                g.DrawImage(image, points, rect, GraphicsUnit.Pixel, attributes);
            }

            // Return the result.
            return bm;
        }

    }
}
