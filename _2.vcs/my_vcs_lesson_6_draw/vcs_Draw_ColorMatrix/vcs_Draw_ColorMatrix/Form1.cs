using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ColorMatrix, ImageAttributes

namespace vcs_Draw_ColorMatrix
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 12;
            y_st = 12;
            dx = 170;
            dy = 50;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);

            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);

        }

        private void button0_Click(object sender, EventArgs e)
        {
            //測試ColorMatrix
            string pic_filename = @"C:\______test_files\picture1.jpg";

            Image image = new Bitmap(pic_filename);
            ImageAttributes imageAttributes = new ImageAttributes();
            int W = image.Width;
            int H = image.Height;

            float[][] colorMatrixElements = { 
   new float[] {2,  0,  0,  0, 0},        // red scaling factor of 2
   new float[] {0,  1,  0,  0, 0},        // green scaling factor of 1
   new float[] {0,  0,  1,  0, 0},        // blue scaling factor of 1
   new float[] {0,  0,  0,  1, 0},        // alpha scaling factor of 1
   new float[] {.2f, .2f, .2f, 0, 1}};    // three translations of 0.2

            ColorMatrix colorMatrix = new ColorMatrix(colorMatrixElements);

            imageAttributes.SetColorMatrix(
               colorMatrix,
               ColorMatrixFlag.Default,
               ColorAdjustType.Bitmap);

            Bitmap bitmap1 = new Bitmap(W * 2, H);

            Graphics g = Graphics.FromImage(bitmap1);

            //畫原圖
            g.DrawImage(image, 0, 0, W, H);

            //畫使用ColorMatrix的圖
            g.DrawImage(
               image,
               new Rectangle(0+W, 0, W, H),  // destination rectangle, 向右移動W
               0, 0,        // upper-left corner of source rectangle 
               W,       // width of source rectangle
               H,      // height of source rectangle
               GraphicsUnit.Pixel,
               imageAttributes);
            pictureBox1.Image = bitmap1;


        }

        private void button1_Click(object sender, EventArgs e)
        {
            //一般貼上banner
            Bitmap bm = new Bitmap(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height);

            using (Graphics gr = Graphics.FromImage(bm))
            {
                Image img = Image.FromFile("c:\\______test_files\\picture1.jpg");
                gr.Clear(Color.White);
                gr.DrawImage(img, 0, 0, img.Width, img.Height);
                Image banner = Image.FromFile("c:\\______test_files\\_material\\ims3.bmp");
                gr.DrawImage(banner, 0, 200, 300, 130);
            }
            pictureBox1.Image = bm;

        }

        private void button2_Click(object sender, EventArgs e)
        {
            //半透明貼上banner
            // With translucency.
            Bitmap bm = new Bitmap(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height);

            // Make adjusted images.
            Image banner = AdjustAlpha(Image.FromFile("c:\\______test_files\\_material\\ims3.bmp"), 0.60f);

            // Draw the adjusted images.
            using (Graphics gr = Graphics.FromImage(bm))
            {
                Image img = Image.FromFile("c:\\______test_files\\picture1.jpg");
                gr.Clear(Color.White);
                gr.DrawImage(img, 0, 0, img.Width, img.Height);
                gr.DrawImage(banner, 0, 200, 300, 130);
            }
            pictureBox1.Image = bm;
        }

        // Adjust an image's translucency.
        private Bitmap AdjustAlpha(Image image, float translucency)
        {
            // Make the ColorMatrix.
            float t = translucency;
            ColorMatrix cm = new ColorMatrix(new float[][]
                {
                    new float[] {1, 0, 0, 0, 0},
                    new float[] {0, 1, 0, 0, 0},
                    new float[] {0, 0, 1, 0, 0},
                    new float[] {0, 0, 0, t, 0},
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

        private void button3_Click(object sender, EventArgs e)
        {

        }


    }
}
