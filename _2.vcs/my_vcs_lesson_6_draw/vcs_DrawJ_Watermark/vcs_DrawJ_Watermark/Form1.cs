using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;

namespace vcs_DrawJ_Watermark
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename1 = @"C:\______test_files\picture1.jpg";
            string filename2 = @"C:\______test_files\_material\ims-small-logo.png";

            pictureBox1.Image = Image.FromFile(filename1);
            pictureBox2.Image = Image.FromFile(filename2);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Bitmap result_bm = new Bitmap(pictureBox1.Image);

            using (Bitmap watermark_bm = new Bitmap(pictureBox2.Image))
            {
                int x = (result_bm.Width - watermark_bm.Width) / 2;
                int y = (result_bm.Height - watermark_bm.Height) / 2;
                DrawWatermark1(watermark_bm, result_bm, x, y);
            }

            pictureBox1.Image = result_bm;
        }

        // Copy the watermark image over the result image.
        private void DrawWatermark1(Bitmap watermark_bm, Bitmap result_bm, int x, int y)
        {
            const byte ALPHA = 128;
            // Set the watermark's pixels' Alpha components.
            Color clr;
            for (int py = 0; py < watermark_bm.Height; py++)
            {
                for (int px = 0; px < watermark_bm.Width; px++)
                {
                    clr = watermark_bm.GetPixel(px, py);
                    watermark_bm.SetPixel(px, py, Color.FromArgb(ALPHA, clr.R, clr.G, clr.B));
                }
            }

            // Set the watermark's transparent color.
            watermark_bm.MakeTransparent(watermark_bm.GetPixel(0, 0));

            // Copy onto the result image.
            using (Graphics gr = Graphics.FromImage(result_bm))
            {
                gr.DrawImage(watermark_bm, x, y);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Bitmap result_bm = new Bitmap(pictureBox1.Image);

            using (Bitmap watermark_bm = new Bitmap(pictureBox2.Image))
            {
                int x = (result_bm.Width - watermark_bm.Width) / 2;
                int y = (result_bm.Height - watermark_bm.Height) / 2;
                DrawWatermark2(watermark_bm, result_bm, x, y);
            }

            pictureBox1.Image = result_bm;
        }

        // Copy the watermark image over the result image.
        private void DrawWatermark2(Bitmap watermark_bm, Bitmap result_bm, int x, int y)
        {
            // Make a ColorMatrix that multiplies
            // the alpha component by 0.5.
            ColorMatrix color_matrix = new ColorMatrix();
            color_matrix.Matrix33 = 0.5f;

            // Make an ImageAttributes that uses the ColorMatrix.
            ImageAttributes image_attributes = new ImageAttributes();
            image_attributes.SetColorMatrices(color_matrix, null);

            // Make pixels that are the same color as the
            // one in the upper left transparent.
            watermark_bm.MakeTransparent(watermark_bm.GetPixel(0, 0));

            // Draw the image using the ColorMatrix.
            using (Graphics gr = Graphics.FromImage(result_bm))
            {
                Rectangle rect = new Rectangle(x, y, watermark_bm.Width, watermark_bm.Height);
                gr.DrawImage(watermark_bm, rect, 0, 0,
                    watermark_bm.Width, watermark_bm.Height,
                    GraphicsUnit.Pixel, image_attributes);
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Form1_Load(sender, e);
        }

    }
}
