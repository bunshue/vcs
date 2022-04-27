using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;

namespace vcs_ImageProcessing4
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Display the image converted to sepia tone.
        private void Form1_Load(object sender, EventArgs e)
        {
            scrRed.Value = 128;
            scrGreen.Value = 128;
            scrBlue.Value = 128;
            scrBright.Value = 128;
            picColor.BackColor = Color.FromArgb(scrRed.Value, scrGreen.Value, scrBlue.Value);
            ColorPicture();
        }

        // Adjust the target color and redraw.
        private void scrColorComponent_Scroll(object sender, ScrollEventArgs e)
        {
            picColor.BackColor = Color.FromArgb(scrRed.Value, scrGreen.Value, scrBlue.Value);
            ColorPicture();
        }

        // Color the picture.
        private void ColorPicture()
        {
            picToned.Image = ToColorTone(picOriginal.Image, picColor.BackColor);
        }

        // Convert an image to sepia tone.
        private Bitmap ToColorTone(Image image, Color color)
        {
            float scale = scrBright.Value / 128f;

            float r = color.R / 255f * scale;
            float g = color.G / 255f * scale;
            float b = color.B / 255f * scale;

            // Make the ColorMatrix.
            ColorMatrix cm = new ColorMatrix(new float[][]
            {
                new float[] {r, 0, 0, 0, 0},
                new float[] {0, g, 0, 0, 0},
                new float[] {0, 0, b, 0, 0},
                new float[] {0, 0, 0, 1, 0},
                new float[] {0, 0, 0, 0, 1}
            });
            ImageAttributes attributes = new ImageAttributes();
            attributes.SetColorMatrix(cm);

            // Draw the image onto the new bitmap while applying the new ColorMatrix.
            Point[] points =
            {
                new Point(0, 0),
                new Point(image.Width - 1, 0),
                new Point(0, image.Height - 1),
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
    }
}
