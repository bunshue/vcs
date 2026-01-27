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
        Bitmap bitmap1;
        Graphics g;
        string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            bitmap1 = new Bitmap(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height);
            g = Graphics.FromImage(bitmap1);
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
            dx = 200 + 10;
            dy = 60 + 10;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            pictureBox1.Size = new Size(800, 600);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);

            richTextBox1.Size = new Size(300, 600);
            richTextBox1.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1400, 760);
            this.Text = "vcs_Draw_ColorMatrix";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //測試ColorMatrix
            string pic_filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

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
               new Rectangle(0 + W, 0, W, H),  // destination rectangle, 向右移動W
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
                Image img = Image.FromFile(@"D:\_git\vcs\_1.data\______test_files1\picture1.jpg");
                gr.Clear(Color.White);
                gr.DrawImage(img, 0, 0, img.Width, img.Height);
                Image banner = Image.FromFile(@"D:\_git\vcs\_1.data\______test_files1\_material\ims3.bmp");
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
            Image banner = AdjustAlpha(Image.FromFile(@"D:\_git\vcs\_1.data\______test_files1\_material\ims3.bmp"), 0.60f);

            // Draw the adjusted images.
            using (Graphics gr = Graphics.FromImage(bm))
            {
                Image img = Image.FromFile(@"D:\_git\vcs\_1.data\______test_files1\picture1.jpg");
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
            //使用ColorMatrix圖片亮度處理

            //圖片亮度處理

            //亮度百分比

            int percent = 50;

            Single v = 0.006F * percent;

            Single[][] matrix = {         
                new Single[] { 1, 0, 0, 0, 0 },         
                new Single[] { 0, 1, 0, 0, 0 },          
                new Single[] { 0, 0, 1, 0, 0 },         
                new Single[] { 0, 0, 0, 1, 0 },         
                new Single[] { v, v, v, 0, 1 }     
            };

            System.Drawing.Imaging.ColorMatrix cm = new System.Drawing.Imaging.ColorMatrix(matrix);
            System.Drawing.Imaging.ImageAttributes attr = new System.Drawing.Imaging.ImageAttributes();
            attr.SetColorMatrix(cm);
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            Image tmp = Image.FromFile(filename);

            this.pictureBox1.Image = Image.FromFile(filename);

            Graphics g = Graphics.FromImage(tmp);
            try
            {
                Rectangle destRect = new Rectangle(0, 0, tmp.Width, tmp.Height);
                g.DrawImage(tmp, destRect, 0, 0, tmp.Width, tmp.Height, GraphicsUnit.Pixel, attr);
            }
            finally
            {
                g.Dispose();
            }
            this.pictureBox1.Image = (Image)tmp.Clone();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //使用ColorMatrix取灰度
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            //取灰度
            this.pictureBox1.Image = Image.FromFile(filename);
            Bitmap currentBitmap = new Bitmap(this.pictureBox1.Image);
            Graphics g = Graphics.FromImage(currentBitmap);
            ImageAttributes ia = new ImageAttributes();
            float[][] colorMatrix =   {    
                new   float[]   {0.299f,   0.299f,   0.299f,   0,   0},
                new   float[]   {0.587f,   0.587f,   0.587f,   0,   0},
                new   float[]   {0.114f,   0.114f,   0.114f,   0,   0},
                new   float[]   {0,   0,   0,   1,   0},
                new   float[]   {0,   0,   0,   0,   1}
            };

            ColorMatrix cm = new ColorMatrix(colorMatrix);
            ia.SetColorMatrix(cm, ColorMatrixFlag.Default, ColorAdjustType.Bitmap);
            g.DrawImage(currentBitmap, new Rectangle(0, 0, currentBitmap.Width, currentBitmap.Height), 0, 0, currentBitmap.Width, currentBitmap.Height, GraphicsUnit.Pixel, ia);
            this.pictureBox1.Image = (Image)(currentBitmap.Clone());
            g.Dispose();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //ColorMatrix
            //使用ColorMatrix改亮度

            //亮度百分比
            int percent = 50;

            Single v = 0.006F * percent;

            Single[][] matrix = {         
                new Single[] { 1, 0, 0, 0, 0 },         
                new Single[] { 0, 1, 0, 0, 0 },          
                new Single[] { 0, 0, 1, 0, 0 },         
                new Single[] { 0, 0, 0, 1, 0 },         
                new Single[] { v, v, v, 0, 1 }     
            };

            System.Drawing.Imaging.ColorMatrix cm = new System.Drawing.Imaging.ColorMatrix(matrix);
            System.Drawing.Imaging.ImageAttributes attr = new System.Drawing.Imaging.ImageAttributes();

            attr.SetColorMatrix(cm);

            //Image tmp 

            Image tmp = Image.FromFile(filename);
            this.pictureBox1.Image = Image.FromFile(filename);
            Graphics g = Graphics.FromImage(tmp);
            try
            {
                Rectangle destRect = new Rectangle(0, 0, tmp.Width, tmp.Height);
                g.DrawImage(tmp, destRect, 0, 0, tmp.Width, tmp.Height, GraphicsUnit.Pixel, attr);
            }
            finally
            {
                g.Dispose();
            }
            this.pictureBox1.Image = (Image)tmp.Clone();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //ColorMatrix

            //使用ColorMatrix取灰度

            Bitmap currentBitmap = new Bitmap(filename);

            Graphics g = Graphics.FromImage(currentBitmap);

            ImageAttributes ia = new ImageAttributes();

            float[][] colorMatrix =   {    
                new   float[]   {0.299f,   0.299f,   0.299f,   0,   0},
                new   float[]   {0.587f,   0.587f,   0.587f,   0,   0},
                new   float[]   {0.114f,   0.114f,   0.114f,   0,   0},
                new   float[]   {0,   0,   0,   1,   0},
                new   float[]   {0,   0,   0,   0,   1}
            };

            ColorMatrix cm = new ColorMatrix(colorMatrix);

            ia.SetColorMatrix(cm, ColorMatrixFlag.Default, ColorAdjustType.Bitmap);

            g.DrawImage(currentBitmap, new Rectangle(0, 0, currentBitmap.Width, currentBitmap.Height), 0, 0, currentBitmap.Width, currentBitmap.Height, GraphicsUnit.Pixel, ia);

            this.pictureBox1.Image = (Image)(currentBitmap.Clone());

            g.Dispose();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //test ColorMatrix
            //測試 ColorMatrix

            float[][] m_cmArray = // 色彩調整矩陣 透明度 20%
               {
                  new float[] {1, 0, 0, 0,    0},
                  new float[] {0, 1, 0, 0,    0},
                  new float[] {0, 0, 1, 0,    0},
                  new float[] {0, 0, 0, 0.2f, 0},
                  new float[] {0, 0, 0, 0,    1}
               };

            ColorMatrix cm = new ColorMatrix(m_cmArray);
            ImageAttributes ia = new ImageAttributes();
            ia.SetColorMatrix(cm, ColorMatrixFlag.Default, ColorAdjustType.Bitmap);

            string filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";
            Bitmap bmp = new Bitmap(filename);

            g.DrawRectangle(Pens.Red, 100, 100, 100, 100);
            g.DrawImage(bmp, 0, 0, bmp.Width / 2, bmp.Height / 2);

            Rectangle dest2 = new Rectangle(0, 300, bmp.Width / 2, bmp.Height / 2);
            g.DrawImage(bmp, dest2, 0, 0, bmp.Width, bmp.Height, GraphicsUnit.Pixel, ia);

            pictureBox1.Image = bitmap1;

        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {

        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            //SetColorMatrixExample

            // Create a rectangle image with all colors set to 128 (medium gray).
            /*
            Bitmap myBitmap = new Bitmap(50, 50, PixelFormat.Format32bppArgb);
            Graphics g = Graphics.FromImage(myBitmap);
            g.FillRectangle(new SolidBrush(Color.FromArgb(255, 128, 128, 128)),
                new Rectangle(0, 0, 50, 50));
            myBitmap.Save("Rectangle1.jpg");
            */

            // Open an Image file and draw it to the screen.

            string filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";

            Image myImage = Image.FromFile("Rectangle1.jpg");
            e.Graphics.DrawImage(myImage, 20, 20);

            ColorMatrix myColorMatrix = new ColorMatrix();

            // Red
            myColorMatrix.Matrix00 = 1.75f;

            // Green
            myColorMatrix.Matrix11 = 1.00f;

            // Blue
            myColorMatrix.Matrix22 = 1.00f;

            // alpha
            myColorMatrix.Matrix33 = 1.00f;

            // w
            myColorMatrix.Matrix44 = 1.00f;

            // Create an ImageAttributes object and set the color matrix.
            ImageAttributes imageAttr = new ImageAttributes();
            imageAttr.SetColorMatrix(myColorMatrix);

            // Draw the image using the color matrix.
            Rectangle rect = new Rectangle(100, 20, 200, 200);
            e.Graphics.DrawImage(myImage, rect, 0, 0, 200, 200, GraphicsUnit.Pixel, imageAttr);
        }

    }
}

