using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for PixelFormat
using System.IO;    //for Path

namespace vcs_ImageProcessing2
{
    public partial class Form1 : Form
    {
        string filename1 = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
        string filename2 = @"C:\_git\vcs\_1.data\______test_files1\bear.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            pictureBox1.Image = Bitmap.FromFile(filename1);
            PictureToSepia1();  //To Sepia 方法一
            //PictureToSepia2();  //To Sepia 方法二
            PictureToGray1();
            PictureToGray4();
            PictureToGray5();
            PictureToMonochrome();
            PictureToNegative();
            PictureToBlur();
            PictureToMirror();
            PictureToRainbow();

            // Convert the image into red, green, and blue monochrome.
            pictureBox7.Image = ScaleColorComponents(pictureBox1.Image, 1, 0, 0, 1);
            pictureBox8.Image = ScaleColorComponents(pictureBox1.Image, 0, 1, 0, 1);
            pictureBox9.Image = ScaleColorComponents(pictureBox1.Image, 0, 0, 1, 1);

            //另外的方法製作單色圖片
            //show_mono_color_picture();

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            bt_exit_setup();
        }

        void show_item_location()
        {
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom; //原圖
            pictureBox2.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox3.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox4.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox5.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox6.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox7.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox8.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox9.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox10.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox11.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox12.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox13.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox14.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox15.SizeMode = PictureBoxSizeMode.Zoom;
            //pictureBox16.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox17.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox18.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox19.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox20.SizeMode = PictureBoxSizeMode.Zoom;

            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 1700;
            y_st = 12;
            dx = 190;
            dy = 50;

            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 13);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            int W = 250;
            int H = 250;
            x_st = 12;
            y_st = 50;
            dx = 270;
            dy = 300;
            pictureBox1.Size = new Size(W, H);
            pictureBox2.Size = new Size(W, H);
            pictureBox3.Size = new Size(W, H);
            pictureBox4.Size = new Size(W, H);
            pictureBox5.Size = new Size(W, H);
            pictureBox6.Size = new Size(W, H);
            pictureBox7.Size = new Size(W, H);
            pictureBox8.Size = new Size(W, H);
            pictureBox9.Size = new Size(W, H);
            pictureBox10.Size = new Size(W, H);
            pictureBox11.Size = new Size(W, H);
            pictureBox12.Size = new Size(W, H);
            pictureBox13.Size = new Size(W, H);
            pictureBox14.Size = new Size(W, H);
            pictureBox15.Size = new Size(W * 2, H);
            pictureBox17.Size = new Size(W, H);
            pictureBox18.Size = new Size(W, H);
            pictureBox19.Size = new Size(W, H);
            pictureBox20.Size = new Size(W + 110, H + 100);
            pictureBox20.BackColor = Color.Pink;

            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox3.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox4.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            pictureBox5.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            pictureBox6.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            pictureBox7.Location = new Point(x_st + dx * 6, y_st + dy * 0);

            pictureBox8.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox9.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            pictureBox10.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            pictureBox11.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            pictureBox12.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            pictureBox13.Location = new Point(x_st + dx * 5, y_st + dy * 1);
            pictureBox14.Location = new Point(x_st + dx * 6, y_st + dy * 1);

            pictureBox15.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            //pictureBox16.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            pictureBox17.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            pictureBox18.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            pictureBox19.Location = new Point(x_st + dx * 4, y_st + dy * 2);
            pictureBox20.Location = new Point(x_st + dx * 5 - 30, y_st + dy * 2);

            label1.Location = new Point(x_st + dx * 0, y_st + dy * 0 - 25);
            label2.Location = new Point(x_st + dx * 1, y_st + dy * 0 - 25);
            label3.Location = new Point(x_st + dx * 2, y_st + dy * 0 - 25);
            label4.Location = new Point(x_st + dx * 3, y_st + dy * 0 - 25);
            label5.Location = new Point(x_st + dx * 4, y_st + dy * 0 - 25);
            label6.Location = new Point(x_st + dx * 5, y_st + dy * 0 - 25);
            label7.Location = new Point(x_st + dx * 6, y_st + dy * 0 - 25);

            label8.Location = new Point(x_st + dx * 0, y_st + dy * 1 - 25);
            label9.Location = new Point(x_st + dx * 1, y_st + dy * 1 - 25);
            label10.Location = new Point(x_st + dx * 2, y_st + dy * 1 - 25);
            label11.Location = new Point(x_st + dx * 3, y_st + dy * 1 - 25);
            label12.Location = new Point(x_st + dx * 4, y_st + dy * 1 - 25);
            label13.Location = new Point(x_st + dx * 5, y_st + dy * 1 - 25);
            label14.Location = new Point(x_st + dx * 6, y_st + dy * 1 - 25);

            label15.Location = new Point(x_st + dx * 0, y_st + dy * 2 - 25);
            label16.Location = new Point(x_st + dx * 1, y_st + dy * 2 - 25);
            label17.Location = new Point(x_st + dx * 2, y_st + dy * 2 - 25);
            label18.Location = new Point(x_st + dx * 3, y_st + dy * 2 - 25);
            label19.Location = new Point(x_st + dx * 4, y_st + dy * 2 - 25);
            label20.Location = new Point(x_st + dx * 5, y_st + dy * 2 - 25);

            label1.Text = "原圖";
            label2.Text = "Sepia";
            label3.Text = "灰階SetPixel";
            label4.Text = "";
            label5.Text = "";
            label6.Text = "單色處理";
            label7.Text = "單色 R";
            label8.Text = "單色 G";
            label9.Text = "單色 B";
            label10.Text = "負片";
            label11.Text = "原圖";
            label12.Text = "灰階 Grayscale";
            label13.Text = "灰階 Average";
            label14.Text = "模糊處理";
            label15.Text = "鏡像圖片";
            label16.Text = "";
            label17.Text = "彩虹化圖片";
            label18.Text = "";
            label19.Text = "";
            label20.Text = "";
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void PictureToSepia1()
        {
            //將圖片轉為 Sepia 效果
            // Display the image converted to sepia tone.
            pictureBox2.Image = ToSepiaTone1(pictureBox1.Image);
        }

        // Convert an image to sepia tone.
        private Bitmap ToSepiaTone1(Image image)
        {
            // Make the ColorMatrix.
            ColorMatrix cm = new ColorMatrix(new float[][]
            {
                new float[] {0.393f, 0.349f, 0.272f, 0, 0},
                new float[] {0.769f, 0.686f, 0.534f, 0, 0},
                new float[] {0.189f, 0.168f, 0.131f, 0, 0},
                new float[] { 0, 0, 0, 1, 0},
                new float[] { 0, 0, 0, 0, 1}
            });
            //ColorMatrix cm = new ColorMatrix(new float[][]
            //{
            //    new float[] {0.300f, 0.066f, 0.300f, 0, 0},
            //    new float[] {0.500f, 0.350f, 0.600f, 0, 0},
            //    new float[] {0.100f, 0.000f, 0.200f, 0, 0},
            //    new float[] { 0, 0, 0, 1, 0},
            //    new float[] { 0, 0, 0, 0, 1}
            //});
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
            Bitmap bmp = new Bitmap(image.Width, image.Height);
            using (Graphics gr = Graphics.FromImage(bmp))
            {
                gr.DrawImage(image, points, rect, GraphicsUnit.Pixel, attributes);
            }

            // Return the result.
            return bmp;
        }

        private void PictureToSepia2()
        {
            //將圖片轉為 Sepia 效果
            // Display the image converted to sepia tone.
            pictureBox2.Image = ToSepiaTone2(pictureBox1.Image);
        }

        // Convert an image to sepia tone.
        private Bitmap ToSepiaTone2(Image image)
        {
            //將圖片轉為 Sepia 效果
            //read image
            Bitmap bmp = new Bitmap(image);

            //get image dimension
            int width = bmp.Width;
            int height = bmp.Height;

            //color of pixel
            Color p;

            //sepia
            for (int y = 0; y < height; y++)
            {
                for (int x = 0; x < width; x++)
                {
                    //get pixel value
                    p = bmp.GetPixel(x, y);

                    //extract pixel component ARGB
                    int a = p.A;
                    int r = p.R;
                    int g = p.G;
                    int b = p.B;

                    //calculate temp value
                    int tr = (int)(0.393 * r + 0.769 * g + 0.189 * b);
                    int tg = (int)(0.349 * r + 0.686 * g + 0.168 * b);
                    int tb = (int)(0.272 * r + 0.534 * g + 0.131 * b);

                    //set new RGB value
                    if (tr > 255)
                    {
                        r = 255;
                    }
                    else
                    {
                        r = tr;
                    }

                    if (tg > 255)
                    {
                        g = 255;
                    }
                    else
                    {
                        g = tg;
                    }

                    if (tb > 255)
                    {
                        b = 255;
                    }
                    else
                    {
                        b = tb;
                    }

                    //set the new RGB value in image pixel
                    bmp.SetPixel(x, y, Color.FromArgb(a, r, g, b));
                }
            }
            return bmp;
        }

        private void PictureToGray1()
        {
            //SetPixel 彩色轉灰階
            color_to_gray_1(filename1);
        }

        void color_to_gray_1(string filename)
        {
            richTextBox1.Text += "SetPixel 彩色轉灰階\n";

            Bitmap bmp0 = new Bitmap(filename);
            Bitmap bmp = new Bitmap(filename);
            pictureBox1.Image = bmp0;

            int xx;
            int yy;

            for (yy = 0; yy < bmp.Height; yy++)
            {
                for (xx = 0; xx < bmp.Width; xx++)
                {
                    byte rrr = bmp.GetPixel(xx, yy).R;
                    byte ggg = bmp.GetPixel(xx, yy).G;
                    byte bbb = bmp.GetPixel(xx, yy).B;

                    int Gray = (rrr * 299 + ggg * 587 + bbb * 114 + 500) / 1000;
                    Color zz = Color.FromArgb(255, Gray, Gray, Gray);

                    bmp.SetPixel(xx, yy, zz);
                }
            }
            pictureBox3.Image = bmp;
        }



        #region 將圖片改為灰階 Grayscale Average

        private void PictureToGray4()
        {
            //將圖片改為灰階 Grayscale
            ConvertFile(filename2, false);
        }

        private void PictureToGray5()
        {
            //將圖片改為灰階 Average
            ConvertFile(filename2, true);
        }

        // Convert a file.
        private void ConvertFile(string filename, bool use_average)
        {
            richTextBox1.Text += "filename old = " + filename + "\n";

            string d_name = Path.GetDirectoryName(filename);
            string f_name = Path.GetFileNameWithoutExtension(filename);
            string ext_name = Path.GetExtension(filename);

            string filename2;

            if (use_average == true)
            {
                filename2 = "tmp_" + f_name + "_average" + ext_name;
            }
            else
            {
                filename2 = "tmp_" + f_name + "_grayscale" + ext_name;
            }

            richTextBox1.Text += "filename new = " + filename2 + "\n";

            pictureBox11.Image = Bitmap.FromFile(filename);

            // Convert to grayscale.
            //Bitmap bmp = new Bitmap(pictureBox1.Image);       same
            Bitmap bmp = LoadBitmapWithoutLocking(filename);

            // Convert the image.
            ConvertBitmapToGrayscale(bmp, use_average);

            // Show the converted bitmap
            if (use_average == true)
                pictureBox13.Image = bmp;
            else
                pictureBox12.Image = bmp;

            //自動檔名 與 存檔語法
            //string filename2 = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
            try
            {
                bmp.Save(filename2, ImageFormat.Bmp);

                richTextBox1.Text += "已存檔 : " + filename2 + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
        }

        // Convert the Bitmap to grayscale.
        private void ConvertBitmapToGrayscale(Bitmap bm, bool use_average)
        {
            // Make a Bitmap24 object.
            Bitmap32 bm32 = new Bitmap32(bm);

            // Lock the bitmap.
            bm32.LockBitmap();

            // Process the pixels.
            for (int x = 0; x < bm.Width; x++)
            {
                for (int y = 0; y < bm.Height; y++)
                {
                    byte r = bm32.GetRed(x, y);
                    byte g = bm32.GetGreen(x, y);
                    byte b = bm32.GetBlue(x, y);
                    byte gray = (use_average ? (byte)((r + g + b) / 3) : (byte)(0.3 * r + 0.5 * g + 0.2 * b));
                    bm32.SetPixel(x, y, gray, gray, gray, 255);
                }
            }

            // Unlock the bitmap.
            bm32.UnlockBitmap();
        }

        // Load a Bitmap without locking its file.
        // The caller must dispose of the Bitmap if desired.
        private Bitmap LoadBitmapWithoutLocking(string filename)
        {
            Bitmap result;
            using (Bitmap bm = new Bitmap(filename))
            {
                result = new Bitmap(bm.Width, bm.Height);
                using (Graphics gr = Graphics.FromImage(result))
                {
                    gr.DrawImage(bm, 0, 0);
                }
            }

            return result;
        }

        #endregion

        private void PictureToMonochrome()
        {
            richTextBox1.Text += "PictureToMonochrome\n";
            pictureBox6.Image = ToMonochrome(pictureBox1.Image);
        }

        // Convert an image to monochrome.
        private Bitmap ToMonochrome(Image image)
        {
            // Make the ColorMatrix.
            ColorMatrix cm = new ColorMatrix(new float[][]
            {
                new float[] {0.299f, 0.299f, 0.299f, 0, 0},
                new float[] {0.587f, 0.587f, 0.587f, 0, 0},
                new float[] {0.114f, 0.114f, 0.114f, 0, 0},
                new float[] { 0, 0, 0, 1, 0},
                new float[] { 0, 0, 0, 0, 1}
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

        // Scale an image's color components.
        private Bitmap ScaleColorComponents(Image image, float r, float g, float b, float a)
        {
            // Make the ColorMatrix.
            ColorMatrix cm = new ColorMatrix(new float[][]
                {
                    new float[] {r, 0, 0, 0, 0},
                    new float[] {0, g, 0, 0, 0},
                    new float[] {0, 0, b, 0, 0},
                    new float[] {0, 0, 0, a, 0},
                    new float[] {0, 0, 0, 0, 1},
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

        private void bt_clear_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = null;
            pictureBox2.Image = null;
            richTextBox1.Clear();
        }

        private void PictureToNegative()
        {
            richTextBox1.Text += "PictureToNegative\n";
            pictureBox10.Image = ToNegative(pictureBox1.Image);
        }

        private Bitmap ToNegative(Image image)
        {
            // Make the result bitmap.
            Bitmap bmp = new Bitmap(image);

            //get image dimension
            int width = image.Width;
            int height = image.Height;

            //negative
            for (int y = 0; y < height; y++)
            {
                for (int x = 0; x < width; x++)
                {
                    //get pixel value
                    Color p = bmp.GetPixel(x, y);

                    //extract ARGB value from p
                    int a = p.A;
                    int r = p.R;
                    int g = p.G;
                    int b = p.B;

                    //find negative value
                    r = 255 - r;
                    g = 255 - g;
                    b = 255 - b;

                    //set new ARGB value in pixel
                    bmp.SetPixel(x, y, Color.FromArgb(a, r, g, b));
                }
            }
            // Return the result.
            return bmp;
        }

        private void PictureToBlur()
        {
            richTextBox1.Text += "PictureToBlur\n";
            pictureBox14.Image = ToBlur(pictureBox1.Image);
        }

        private Bitmap ToBlur(Image image)
        {
            Bitmap bitmap1 = (Bitmap)image;
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            Bitmap bitmap2 = new Bitmap(W, H);

            for (int j = 0; j < H; j++)
            {
                for (int i = 0; i < W; i++)
                {
                    int ok_cnt = 0;
                    int R = 0;
                    int G = 0;
                    int B = 0;

                    // 檢查相鄰像素, 每個點的鄰居不一樣多, 所以要做不同的平均

                    //自己
                    R += bitmap1.GetPixel(i, j).R;
                    G += bitmap1.GetPixel(i, j).G;
                    B += bitmap1.GetPixel(i, j).B;

                    ok_cnt++;

                    if (j - 1 > 0)       //上
                    {
                        R += bitmap1.GetPixel(i, j - 1).R;
                        G += bitmap1.GetPixel(i, j - 1).G;
                        B += bitmap1.GetPixel(i, j - 1).B;

                        ok_cnt++;
                    }
                    if (j + 1 < H)      //下
                    {
                        R += bitmap1.GetPixel(i, j + 1).R;
                        G += bitmap1.GetPixel(i, j + 1).G;
                        B += bitmap1.GetPixel(i, j + 1).B;
                        ok_cnt++;
                    }
                    if (i - 1 > 0)       //左
                    {
                        R += bitmap1.GetPixel(i - 1, j).R;
                        G += bitmap1.GetPixel(i - 1, j).G;
                        B += bitmap1.GetPixel(i - 1, j).B;
                        ok_cnt++;
                    }
                    if (i + 1 < W)       //右
                    {
                        R += bitmap1.GetPixel(i + 1, j).R;
                        G += bitmap1.GetPixel(i + 1, j).G;
                        B += bitmap1.GetPixel(i + 1, j).B;
                        ok_cnt++;
                    }
                    if ((i - 1 > 0) && (j - 1 > 0))     //左上
                    {
                        R += bitmap1.GetPixel(i - 1, j - 1).R;
                        G += bitmap1.GetPixel(i - 1, j - 1).G;
                        B += bitmap1.GetPixel(i - 1, j - 1).B;
                        ok_cnt++;
                    }
                    if ((i - 1 > 0) && (j + 1 < H)) //左下
                    {
                        R += bitmap1.GetPixel(i - 1, j + 1).R;
                        G += bitmap1.GetPixel(i - 1, j + 1).G;
                        B += bitmap1.GetPixel(i - 1, j + 1).B;
                        ok_cnt++;
                    }
                    if ((i + 1 < W) && (j - 1 > 0))      //右上
                    {
                        R += bitmap1.GetPixel(i + 1, j - 1).R;
                        G += bitmap1.GetPixel(i + 1, j - 1).G;
                        B += bitmap1.GetPixel(i + 1, j - 1).B;
                        ok_cnt++;
                    }
                    if ((i + 1 < W) && (j + 1 < H)) //右下
                    {
                        R += bitmap1.GetPixel(i + 1, j + 1).R;
                        G += bitmap1.GetPixel(i + 1, j + 1).G;
                        B += bitmap1.GetPixel(i + 1, j + 1).B;
                        ok_cnt++;
                    }

                    //平均, 設定個點的像素值
                    bitmap2.SetPixel(i, j, Color.FromArgb((R / ok_cnt), (G / ok_cnt), (B / ok_cnt)));
                }
            }
            return bitmap2;
        }

        private void PictureToMirror()
        {
            richTextBox1.Text += "PictureToMirror\n";
            pictureBox15.Image = ToMirror(pictureBox1.Image);
        }

        private Bitmap ToMirror(Image image)
        {
            // Make the result bitmap.
            Bitmap bmp = new Bitmap(image);

            //get image dimension
            int width = image.Width;
            int height = image.Height;

            //mirror image
            Bitmap mimg = new Bitmap(width * 2, height);

            for (int y = 0; y < height; y++)
            {
                for (int lx = 0, rx = width * 2 - 1; lx < width; lx++, rx--)
                {
                    //get source pixel value
                    Color p = bmp.GetPixel(lx, y);

                    //set mirror pixel value
                    mimg.SetPixel(lx, y, p);
                    mimg.SetPixel(rx, y, p);
                }
            }
            return mimg;
        }

        private void show_mono_color_picture()
        {
            Bitmap bmp = new Bitmap(filename1);

            //load original image in picturebox1
            //pictureBox1.Image = Image.FromFile(filename);

            //get image dimension
            int width = bmp.Width;
            int height = bmp.Height;

            //3 bitmap for red green blue image
            Bitmap rbmp = new Bitmap(bmp);
            Bitmap gbmp = new Bitmap(bmp);
            Bitmap bbmp = new Bitmap(bmp);

            //red green blue image
            for (int y = 0; y < height; y++)
            {
                for (int x = 0; x < width; x++)
                {
                    //get pixel value
                    Color p = bmp.GetPixel(x, y);

                    //extract ARGB value from p
                    int a = p.A;
                    int r = p.R;
                    int g = p.G;
                    int b = p.B;

                    //set red image pixel
                    rbmp.SetPixel(x, y, Color.FromArgb(a, r, 0, 0));

                    //set green image pixel
                    gbmp.SetPixel(x, y, Color.FromArgb(a, 0, g, 0));

                    //set blue image pixel
                    bbmp.SetPixel(x, y, Color.FromArgb(a, 0, 0, b));
                }
            }

            //load red image in picturebox7
            pictureBox7.Image = rbmp;

            //load green image in picturebox8
            pictureBox8.Image = gbmp;

            //load blue image in picturebox9
            pictureBox9.Image = bbmp;
        }

        private void PictureToRainbow()
        {
            richTextBox1.Text += "PictureToRainbow\n";
            pictureBox17.Image = ToRainbow(pictureBox11.Image);
        }

        private Bitmap ToRainbow(Image image)
        {
            //get image dimension
            int width = image.Width;
            int height = image.Height;

            Bitmap bmp = new Bitmap(width, height);
            using (Graphics gr = Graphics.FromImage(bmp))
            {
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
                    // Create the ColorMatrix.
                    ColorMatrix cm = new ColorMatrix(new float[][]
                    {
                        new float[] {color[i].R / 255f * scale, 0, 0, 0, 0},
                        new float[] {0, color[i].G / 255f * scale, 0, 0, 0},
                        new float[] {0, 0, color[i].B / 255f * scale, 0, 0},
                        new float[] {0, 0, 0, 1, 0},
                        new float[] {0, 0, 0, 0, 1},
                    });
                    ImageAttributes attr = new ImageAttributes();
                    attr.SetColorMatrix(cm);

                    // Draw the next part of the image.
                    int x = (int)(i * image.Width / color.Length);
                    Point[] points =
                    {
                        new Point(x, 0),
                        new Point(width, 0),
                        new Point(x, height),
                    };
                    Rectangle rect = new Rectangle(x, 0, width - x, height);
                    gr.DrawImage(image, points, rect, GraphicsUnit.Pixel, attr);
                }
            }
            return bmp;
        }
    }
}
