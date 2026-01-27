using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;  // for ColorMatrix, ImageAttributes
using System.Drawing.Drawing2D;  // for SmoothingMode

namespace vcs_Draw_ColorMatrix
{
    public partial class Form1 : Form
    {
        Bitmap bitmap1;
        Graphics g;
        int W = 800;
        int H = 600;
        string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            bitmap1 = new Bitmap(W, H);
            g = Graphics.FromImage(bitmap1);

            pictureBox2.Image = Image.FromFile(filename);
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

            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            pictureBox1.Size = new Size(W, H);
            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            pictureBox2.Size = new Size(300, H / 2);
            pictureBox2.Location = new Point(x_st + dx * 6, y_st + dy * 0);
            pictureBox2.SizeMode = PictureBoxSizeMode.Zoom;

            richTextBox1.Size = new Size(300, H / 2);
            richTextBox1.Location = new Point(x_st + dx * 6, y_st + dy * 0 + H / 2 + 10);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1610, 760);
            this.Text = "vcs_Draw_ColorMatrix";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //測試ColorMatrix
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bmp = new Bitmap(filename);

            float[][] matrix =
            { 
                new float[] {2,  0,  0,  0, 0},        // red scaling factor of 2
                new float[] {0,  1,  0,  0, 0},        // green scaling factor of 1
                new float[] {0,  0,  1,  0, 0},        // blue scaling factor of 1
                new float[] {0,  0,  0,  1, 0},        // alpha scaling factor of 1
                new float[] {.2f, .2f, .2f, 0, 1}    // three translations of 0.2
            };
            ColorMatrix cm = new ColorMatrix(matrix);
            ImageAttributes ia = new ImageAttributes();
            ia.SetColorMatrix(cm, ColorMatrixFlag.Default, ColorAdjustType.Bitmap);

            //畫使用ColorMatrix的圖
            g.DrawImage(bmp, new Rectangle(0, 0, bmp.Width, bmp.Height), 0, 0, bmp.Width, bmp.Height, GraphicsUnit.Pixel, ia);

            pictureBox1.Image = bitmap1;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //使用ColorMatrix圖片亮度處理
            //圖片亮度處理
            //亮度百分比
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

            ColorMatrix cm = new ColorMatrix(matrix);
            ImageAttributes attr = new ImageAttributes();
            attr.SetColorMatrix(cm);

            Image tmp = Image.FromFile(filename);

            this.pictureBox1.Image = Image.FromFile(filename);

            Graphics g = Graphics.FromImage(tmp);
            Rectangle destRect = new Rectangle(0, 0, tmp.Width, tmp.Height);
            g.DrawImage(tmp, destRect, 0, 0, tmp.Width, tmp.Height, GraphicsUnit.Pixel, attr);
            this.pictureBox1.Image = (Image)tmp.Clone();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //調整亮度2
            //調整亮度

            float brightness = 1.7f;  // 0 ~ 2.5
            this.Text = "Brightness = " + brightness.ToString();

            Image image = Image.FromFile(filename);

            // Make the ColorMatrix.
            float b = brightness;

            float[][] matrix =
            {
                new float[] {b, 0, 0, 0, 0},
                new float[] {0, b, 0, 0, 0},
                new float[] {0, 0, b, 0, 0},
                new float[] {0, 0, 0, 1, 0},
                new float[] {0, 0, 0, 0, 1},
            };
            ColorMatrix cm = new ColorMatrix(matrix);
            ImageAttributes ia = new ImageAttributes();
            ia.SetColorMatrix(cm);

            // Draw the image onto the new bitmap while applying the new ColorMatrix.
            Point[] points =
            {
                new Point(0, 0),
                new Point(image.Width, 0),
                new Point(0, image.Height),
            };
            Rectangle rect = new Rectangle(0, 0, image.Width, image.Height);

            Bitmap bm = new Bitmap(image.Width, image.Height);
            Graphics gr = Graphics.FromImage(bm);
            gr.DrawImage(image, points, rect, GraphicsUnit.Pixel, ia);
            pictureBox1.Image = bm;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //單色圖片1 30
            richTextBox1.Text += "單色圖片1\n";
            string filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";
            //單色圖片30
            //單色圖片 1
            // Convert the image into red, green, and blue monochrome.
            Image image = Image.FromFile(filename);

            //pictureBox1.Image = ScaleColorComponents(image, 1, 0, 0, 1);//R
            //pictureBox1.Image = ScaleColorComponents(image, 0, 1, 0, 1);//G
            //pictureBox1.Image = ScaleColorComponents(image, 0, 0, 1, 1);//B
            float r = 1;
            float g = 0;
            float b = 0;
            float a = 1;

            float[][] matrix =
            {
                new float[] {r, 0, 0, 0, 0},
                new float[] {0, g, 0, 0, 0},
                new float[] {0, 0, b, 0, 0},
                new float[] {0, 0, 0, a, 0},
                new float[] {0, 0, 0, 0, 1},
            };
            ColorMatrix cm = new ColorMatrix(matrix);
            ImageAttributes ia = new ImageAttributes();
            ia.SetColorMatrix(cm);

            // Draw the image onto the new bitmap while applying the new ColorMatrix.
            Point[] points =
            {
                new Point(0, 0),
                new Point(image.Width - 1, 0),
                new Point(0, image.Height - 1),
            };
            Rectangle rect = new Rectangle(0, 0, image.Width, image.Height);

            Bitmap bm = new Bitmap(image.Width, image.Height);
            Graphics gr = Graphics.FromImage(bm);
            gr.DrawImage(image, points, rect, GraphicsUnit.Pixel, ia);

            pictureBox1.Image = bm;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //使用ColorMatrix取灰階1

            bitmap1 = new Bitmap(W, H);
            g = Graphics.FromImage(bitmap1);

            Bitmap bmp = new Bitmap(filename);

            float[][] matrix =
            {
                new float[] {0.299f,   0.299f,   0.299f,   0,   0},
                new float[] {0.587f,   0.587f,   0.587f,   0,   0},
                new float[] {0.114f,   0.114f,   0.114f,   0,   0},
                new float[] {0,   0,   0,   1,   0},
                new float[] {0,   0,   0,   0,   1}
            };
            ColorMatrix cm = new ColorMatrix(matrix);
            ImageAttributes ia = new ImageAttributes();
            ia.SetColorMatrix(cm, ColorMatrixFlag.Default, ColorAdjustType.Bitmap);

            g.DrawImage(bmp, new Rectangle(0, 0, bmp.Width, bmp.Height), 0, 0, bmp.Width, bmp.Height, GraphicsUnit.Pixel, ia);

            pictureBox1.Image = bitmap1;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //使用ColorMatrix取灰階2

            string filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";
            Bitmap bitmap1 = new Bitmap(filename);
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            //Bitmap bitmap2 = new Bitmap(W, H);

            float[][] matrix =
            {
                new float[] {0.299f, 0.299f, 0.299f, 0, 0},
                new float[] {0.587f, 0.587f, 0.587f, 0, 0},
                new float[] {0.114f, 0.114f, 0.114f, 0, 0},
                new float[] { 0, 0, 0, 1, 0},
                new float[] { 0, 0, 0, 0, 1}
            };
            ColorMatrix cm = new ColorMatrix(matrix);
            ImageAttributes ia = new ImageAttributes();
            ia.SetColorMatrix(cm);

            // Draw the image onto the new bitmap while applying the new ColorMatrix.
            Point[] points =
            {
                new Point(0, 0),
                new Point(W - 1, 0),
                new Point(0, H - 1),
            };
            Rectangle rect = new Rectangle(0, 0, W, H);

            Bitmap bm = new Bitmap(W, H);
            Graphics gr = Graphics.FromImage(bm);
            gr.DrawImage(bitmap1, points, rect, GraphicsUnit.Pixel, ia);

            pictureBox1.Image = bm;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //使用ColorMatrix取灰階3

            string filename = @"D:\_git\vcs\_1.data\______test_files1\ims01.bmp";
            Bitmap bmp = new Bitmap(filename);
            Bitmap bitmap2 = new Bitmap(bmp.Width, bmp.Height);

            Graphics g = Graphics.FromImage(bitmap2); // 從點陣圖 建立 新的畫布

            // 定義含有 RGBA 空間座標的 5 x 5 矩陣
            // (R, G, B, A, 1) 乘上 此矩陣

            float[][] matrix =
            {
                new float[]{0.3f, 0.3f, 0.3f, 0, 0},
                new float[]{0.6f, 0.6f, 0.6f, 0, 0},
                new float[]{0.1f, 0.1f, 0.1f, 0, 0},
                new float[]{  0,    0,    0,  1, 0},
                new float[]{  0,    0,    0,  0, 1}
            };
            ColorMatrix cm = new ColorMatrix(matrix);
            ImageAttributes ia = new ImageAttributes();  // ImageAttributes 類別的多個方法會使用色彩矩陣來調整影像色彩
            ia.SetColorMatrix(cm);  // 設定預設分類的色彩調整矩陣

            g.DrawImage(bitmap1, new Rectangle(0, 0, bmp.Width, bmp.Height), 0, 0, bmp.Width, bmp.Height, GraphicsUnit.Pixel, ia);

            pictureBox1.Image = bitmap2;
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //測試 ColorMatrix

            // 色彩調整矩陣 透明度 20%
            float[][] matrix =
            {
                new float[] {1, 0, 0, 0,    0},
                new float[] {0, 1, 0, 0,    0},
                new float[] {0, 0, 1, 0,    0},
                new float[] {0, 0, 0, 0.2f, 0},
                new float[] {0, 0, 0, 0,    1}
            };
            ColorMatrix cm = new ColorMatrix(matrix);
            ImageAttributes ia = new ImageAttributes();
            ia.SetColorMatrix(cm, ColorMatrixFlag.Default, ColorAdjustType.Bitmap);

            string filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";
            pictureBox2.Image = Image.FromFile(filename);

            Bitmap bmp = new Bitmap(filename);

            g.DrawRectangle(Pens.Red, 100, 100, 100, 100);
            g.DrawImage(bmp, 0, 0, bmp.Width / 2, bmp.Height / 2);

            Rectangle dest2 = new Rectangle(0, 300, bmp.Width / 2, bmp.Height / 2);
            g.DrawImage(bmp, dest2, 0, 0, bmp.Width, bmp.Height, GraphicsUnit.Pixel, ia);

            pictureBox1.Image = bitmap1;
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //SetColorMatrixExample

            // Create a rectangle image with all colors set to 128 (medium gray).
            //建立一個矩形全灰色影像
            /*
            Bitmap myBitmap = new Bitmap(50, 50, PixelFormat.Format32bppArgb);
            Graphics g = Graphics.FromImage(myBitmap);
            g.FillRectangle(new SolidBrush(Color.FromArgb(255, 128, 128, 128)),
                new Rectangle(0, 0, 50, 50));
            myBitmap.Save("Rectangle1.jpg");
            */

            // Open an Image file and draw it to the screen.
            // string filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";

            Image myImage = Image.FromFile("Rectangle1.jpg");
            g.DrawImage(myImage, 20, 20);

            //建立 ColorMatrix，並將其 Matrix 位置設定為 1.75，強調影像的紅色元件。

            ColorMatrix cm = new ColorMatrix();

            // Red
            cm.Matrix00 = 1.75f;

            // Green
            cm.Matrix11 = 1.00f;

            // Blue
            cm.Matrix22 = 1.00f;

            // alpha
            cm.Matrix33 = 1.00f;

            // w
            cm.Matrix44 = 1.00f;

            ImageAttributes ia = new ImageAttributes();  // 建立 ImageAttributes 物件，並呼叫 SetColorMatrix 方法。
            ia.SetColorMatrix(cm);

            // Draw the image using the color matrix.
            Rectangle rect = new Rectangle(100, 20, 200, 200);
            g.DrawImage(myImage, rect, 0, 0, 200, 200, GraphicsUnit.Pixel, ia);

            pictureBox1.Image = bitmap1;
        }

        private void button9_Click(object sender, EventArgs e)
        {
            int W = 640;
            int H = 480;
            Bitmap bitmap1 = new Bitmap(W, H);

            string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_game\airplane.bmp";
            pictureBox2.Image = Image.FromFile(filename);

            Bitmap bmp = new Bitmap(filename);

            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.Pink);

            // ColorMatrix, 設定 Alpha = 0.5
            ColorMatrix color_matrix = new ColorMatrix();
            color_matrix.Matrix33 = 0.5f;  // 設定Alpha = 0.5
            //color_matrix.Matrix33 = 1.0f;  // 設定Alpha = 0.5

            // Make an ImageAttributes that uses the ColorMatrix.
            ImageAttributes ia = new ImageAttributes();
            ia.SetColorMatrices(color_matrix, null);

            // Make pixels that are the same color as the
            // one in the upper left transparent.
            // 設定邊角點的顏色為透明色
            // bmp.MakeTransparent(bmp.GetPixel(5, 60));

            int x_st = 50;
            int y_st = 50;
            Rectangle rect = new Rectangle(x_st, y_st, bmp.Width / 2, bmp.Height / 2);
            g.DrawImage(bmp, rect, 0, 0, bmp.Width, bmp.Height, GraphicsUnit.Pixel, ia);
            g.DrawRectangle(Pens.Green, rect);

            pictureBox1.Image = bitmap1;
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //彩虹化圖片28
            string filename = @"D:\_git\vcs\_1.data\______test_files1\bear.jpg";
            Bitmap bitmap1 = new Bitmap(filename);
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            Bitmap bitmap2 = new Bitmap(W, H);

            Graphics gr = Graphics.FromImage(bitmap2);
            // Define target colors.
            Color[] color =
                {
                    //Color.Red, Color.Orange, Color.Yellow,
                    //Color.Green, Color.Blue, Color.Indigo,
                    //Color.Violet,

                    Color.Red, Color.OrangeRed, Color.Yellow,
                    Color.Green, Color.Blue, Color.Indigo,
                    Color.Fuchsia,
                };
            const float scale = 2.0f;

            // Draw.
            for (int i = 0; i < color.Length; i++)
            {
                float[][] matrix =
                {
                    new float[] {color[i].R / 255f * scale, 0, 0, 0, 0},
                    new float[] {0, color[i].G / 255f * scale, 0, 0, 0},
                    new float[] {0, 0, color[i].B / 255f * scale, 0, 0},
                    new float[] {0, 0, 0, 1, 0},
                    new float[] {0, 0, 0, 0, 1},
                };
                ColorMatrix cm = new ColorMatrix(matrix);
                ImageAttributes ia = new ImageAttributes();
                ia.SetColorMatrix(cm);

                // Draw the next part of the image.
                int x = (int)(i * bitmap1.Width / color.Length);
                Point[] points =
                    {
                        new Point(x, 0),
                        new Point(W, 0),
                        new Point(x, H),
                    };
                Rectangle rect = new Rectangle(x, 0, W - x, H);
                gr.DrawImage(bitmap1, points, rect, GraphicsUnit.Pixel, ia);
            }
            pictureBox1.Image = bitmap2;
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //Sepia 效果
            string filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";
            pictureBox2.Image = Image.FromFile(filename);

            Bitmap bitmap1 = new Bitmap(filename);
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            //Bitmap bitmap2 = new Bitmap(W, H);

            // Make the ColorMatrix.

            float[][] matrix =
            {
                new float[] {0.393f, 0.349f, 0.272f, 0, 0},
                new float[] {0.769f, 0.686f, 0.534f, 0, 0},
                new float[] {0.189f, 0.168f, 0.131f, 0, 0},
                new float[] { 0, 0, 0, 1, 0},
                new float[] { 0, 0, 0, 0, 1}
            };
            ColorMatrix cm = new ColorMatrix(matrix);
            //ColorMatrix cm = new ColorMatrix(new float[][]
            //{
            //    new float[] {0.300f, 0.066f, 0.300f, 0, 0},
            //    new float[] {0.500f, 0.350f, 0.600f, 0, 0},
            //    new float[] {0.100f, 0.000f, 0.200f, 0, 0},
            //    new float[] { 0, 0, 0, 1, 0},
            //    new float[] { 0, 0, 0, 0, 1}
            //});
            ImageAttributes ia = new ImageAttributes();
            ia.SetColorMatrix(cm);

            // Draw the image onto the new bitmap while applying the new ColorMatrix.
            Point[] points =
            {
                new Point(0, 0),
                new Point(bitmap1.Width - 1, 0),
                new Point(0, bitmap1.Height - 1),
            };
            Rectangle rect = new Rectangle(0, 0, bitmap1.Width, bitmap1.Height);

            Bitmap bitmap2 = new Bitmap(bitmap1.Width, bitmap1.Height);
            Graphics gr = Graphics.FromImage(bitmap2);
            gr.DrawImage(bitmap1, points, rect, GraphicsUnit.Pixel, ia);

            pictureBox1.Image = bitmap2;
        }

        float alpha = 0f;
        private void button12_Click(object sender, EventArgs e)
        {
            //透明度
            string filename = @"D:\_git\vcs\_1.data\______test_files1\ims01.bmp";

            alpha += 0.1f;
            if (alpha >= 1)
                alpha = 0;
            Bitmap bitmap1 = new Bitmap(filename);
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            Bitmap bitmap2 = new Bitmap(W, H);

            Graphics g = Graphics.FromImage(bitmap2);

            ImageAttributes ia = new ImageAttributes();
            ColorMatrix cm = new ColorMatrix();
            cm.Matrix33 = alpha; // 透明度
            ia.SetColorMatrix(cm);

            g.DrawImage(bitmap1, new Rectangle(0, 0, W, H), 0, 0, W, H, GraphicsUnit.Pixel, ia);

            pictureBox1.Image = bitmap2;
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //半透明貼上banner
            // With translucency.
            Bitmap bm = new Bitmap(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height);

            // Make adjusted images.
            Image banner = AdjustAlpha(Image.FromFile(@"D:\_git\vcs\_1.data\______test_files1\_material\ims3.bmp"), 0.60f);

            // Draw the adjusted images.
            Graphics gr = Graphics.FromImage(bm);
            Image img = Image.FromFile(@"D:\_git\vcs\_1.data\______test_files1\picture1.jpg");
            gr.Clear(Color.White);
            gr.DrawImage(img, 0, 0, img.Width, img.Height);
            gr.DrawImage(banner, 0, 200, 300, 130);
            pictureBox1.Image = bm;
        }

        // Adjust an image's translucency.
        private Bitmap AdjustAlpha(Image image, float translucency)
        {
            // Make the ColorMatrix.
            float t = translucency;

            float[][] matrix =
            {
                new float[] {1, 0, 0, 0, 0},
                new float[] {0, 1, 0, 0, 0},
                new float[] {0, 0, 1, 0, 0},
                new float[] {0, 0, 0, t, 0},
                new float[] {0, 0, 0, 0, 1},
            };
            ColorMatrix cm = new ColorMatrix(matrix);
            ImageAttributes ia = new ImageAttributes();
            ia.SetColorMatrix(cm);

            // Draw the image onto the new bitmap while applying the new ColorMatrix.
            Point[] points =
            {
                new Point(0, 0),
                new Point(image.Width, 0),
                new Point(0, image.Height),
            };
            Rectangle rect = new Rectangle(0, 0, image.Width, image.Height);

            Bitmap bm = new Bitmap(image.Width, image.Height);
            Graphics gr = Graphics.FromImage(bm);
            gr.DrawImage(image, points, rect, GraphicsUnit.Pixel, ia);
            return bm;
        }

        private void button14_Click(object sender, EventArgs e)
        {
        }

        private void button15_Click(object sender, EventArgs e)
        {
        }

        private void button16_Click(object sender, EventArgs e)
        {
        }

        private void button17_Click(object sender, EventArgs e)
        {
        }

        private void button18_Click(object sender, EventArgs e)
        {

        }

        private void button19_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_game\airplane.bmp";
            pictureBox2.Image = Image.FromFile(filename);

            Bitmap bitmap1 = new Bitmap(filename);

            bitmap1 = MakeGrayscale(bitmap1);

            pictureBox1.Image = bitmap1;
        }

        // 圖片去色（圖片黑白化）
        /// <summary>
        /// 圖片去色（圖片黑白化）
        /// </summary>
        /// <param name="original">一個需要處理的圖片</param>
        /// <returns></returns>
        public static Bitmap MakeGrayscale(Bitmap original)
        {
            //create a blank bitmap the same size as original
            Bitmap bitmap1 = new Bitmap(original.Width, original.Height);

            //get a graphics object from the new image
            Graphics g = Graphics.FromImage(bitmap1);
            g.SmoothingMode = SmoothingMode.HighQuality;
            //create the grayscale ColorMatrix

            float[][] matrix =
            {
                new float[] {.3f, .3f, .3f, 0, 0},
                new float[] {.59f, .59f, .59f, 0, 0},
                new float[] {.11f, .11f, .11f, 0, 0},
                new float[] {0, 0, 0, 1, 0},
                new float[] {0, 0, 0, 0, 1}
            };
            ColorMatrix cm = new ColorMatrix(matrix);
            ImageAttributes ia = new ImageAttributes();
            ia.SetColorMatrix(cm);

            //draw the original image on the new image
            //using the grayscale color matrix
            g.DrawImage(original, new Rectangle(0, 0, original.Width, original.Height), 0, 0, original.Width, original.Height, GraphicsUnit.Pixel, ia);

            //dispose the Graphics object
            g.Dispose();
            return bitmap1;
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            return;

            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6_draw\data\color_chart.bmp";
            Bitmap image = new Bitmap(filename);
            int width = image.Width;
            int height = image.Height;
            float degrees = 60f;
            double r = degrees * System.Math.PI / 180; // degrees to radians

            float[][] matrix =
            {
                new float[] {(float)System.Math.Cos(r),  (float)System.Math.Sin(r),  0,  0, 0},
                new float[] {(float)-System.Math.Sin(r),  (float)-System.Math.Cos(r),  0,  0, 0},
                new float[] {0,  0,  2,  0, 0},
                new float[] {0,  0,  0,  1, 0},
                new float[] {0, 0, 0, 0, 1}
            };
            ColorMatrix cm = new ColorMatrix(matrix);
            ImageAttributes ia = new ImageAttributes();
            ia.SetColorMatrix(cm, ColorMatrixFlag.Default, ColorAdjustType.Bitmap);

            e.Graphics.DrawImage(image, 10, 10, width, height);

            e.Graphics.DrawImage(
               image,
               new Rectangle(10, 300, width, height),  // destination rectangle 
                0, 0,        // upper-left corner of source rectangle 
                width,       // width of source rectangle
                height,      // height of source rectangle
                GraphicsUnit.Pixel,
               ia);
        }
    }
}
