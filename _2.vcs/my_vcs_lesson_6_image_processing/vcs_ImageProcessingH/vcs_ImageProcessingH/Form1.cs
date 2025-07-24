using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;   //for ImageAttributes

namespace vcs_ImageProcessingH
{
    public partial class Form1 : Form
    {
        string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";


        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            pictureBox0.Image = Image.FromFile(filename);

            scrRed.Scroll += new ScrollEventHandler(ChangeColorTone_Scroll);
            scrGreen.Scroll += new ScrollEventHandler(ChangeColorTone_Scroll);
            scrBlue.Scroll += new ScrollEventHandler(ChangeColorTone_Scroll);
            scrBright.Scroll += new ScrollEventHandler(ChangeColorTone_Scroll);

            // Display the image converted to sepia tone.
            scrRed.Value = 128;
            scrGreen.Value = 128;
            scrBlue.Value = 128;
            scrBright.Value = 128;
            picColor.BackColor = Color.FromArgb(scrRed.Value, scrGreen.Value, scrBlue.Value);
            ColorPicture();
        }

        void show_item_location()
        {
            pictureBox0.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox2.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox3.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox4.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox5.SizeMode = PictureBoxSizeMode.Normal;

            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 1700;
            y_st = 12;
            dx = 190;
            dy = 50;

            //richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 13);
            //bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            int W = 305;
            int H = 400;
            x_st = 12;
            y_st = 50;
            dx = W + 20;
            dy = H + 50;
            pictureBox0.Size = new Size(W, H);
            pictureBox1.Size = new Size(W, H);
            pictureBox2.Size = new Size(W, H);
            pictureBox3.Size = new Size(W, H);
            pictureBox4.Size = new Size(W, H);
            pictureBox5.Size = new Size(W, H);

            pictureBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox3.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            pictureBox4.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            pictureBox5.Location = new Point(x_st + dx * 5, y_st + dy * 0);

            label0.Location = new Point(x_st + dx * 0, y_st + dy * 0 - 25);
            label1.Location = new Point(x_st + dx * 1, y_st + dy * 0 - 25);
            label2.Location = new Point(x_st + dx * 2, y_st + dy * 0 - 25);
            label3.Location = new Point(x_st + dx * 3, y_st + dy * 0 - 25);
            label4.Location = new Point(x_st + dx * 4, y_st + dy * 0 - 25);
            label9.Location = new Point(x_st + dx * 5, y_st + dy * 0 - 25);

            label0.Text = "原圖";
            label2.Text = "";
            label3.Text = "";
            label4.Text = "";
            label9.Text = "";

            groupBox1.Location = new Point(x_st + dx * 0, y_st + dy * 1);

            x_st = 700;
            y_st = 800;
            dx = 100;
            dy = 30;

            trackBar_gamma1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            trackBar_gamma2.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            trackBar_brightness.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            trackBar_threshold.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            trackBar_binary.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            trackBar_gamma1.MouseDown += new MouseEventHandler(trackBar_gamma1_MouseDown);
            trackBar_gamma1.MouseMove += new MouseEventHandler(trackBar_gamma1_MouseMove);
            trackBar_gamma1.MouseUp += new MouseEventHandler(trackBar_gamma1_MouseUp);
            trackBar_gamma2.MouseDown += new MouseEventHandler(trackBar_gamma2_MouseDown);
            trackBar_gamma2.MouseMove += new MouseEventHandler(trackBar_gamma2_MouseMove);
            trackBar_gamma2.MouseUp += new MouseEventHandler(trackBar_gamma2_MouseUp);
            trackBar_brightness.MouseDown += new MouseEventHandler(trackBar_brightness_MouseDown);
            trackBar_brightness.MouseMove += new MouseEventHandler(trackBar_brightness_MouseMove);
            trackBar_brightness.MouseUp += new MouseEventHandler(trackBar_brightness_MouseUp);
            trackBar_threshold.MouseDown += new MouseEventHandler(trackBar_threshold_MouseDown);
            trackBar_threshold.MouseMove += new MouseEventHandler(trackBar_threshold_MouseMove);
            trackBar_threshold.MouseUp += new MouseEventHandler(trackBar_threshold_MouseUp);
            trackBar_binary.MouseDown += new MouseEventHandler(trackBar_binary_MouseDown);
            trackBar_binary.MouseMove += new MouseEventHandler(trackBar_binary_MouseMove);
            trackBar_binary.MouseUp += new MouseEventHandler(trackBar_binary_MouseUp);

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            bt_exit_setup();
        }

        void trackBar_gamma1_MouseDown(object sender, MouseEventArgs e)
        {
            // TBD
        }

        void trackBar_gamma1_MouseMove(object sender, MouseEventArgs e)
        {
            // TBD
        }

        void trackBar_gamma1_MouseUp(object sender, MouseEventArgs e)
        {
            // TBD
        }

        void trackBar_gamma2_MouseDown(object sender, MouseEventArgs e)
        {
            // TBD
        }

        void trackBar_gamma2_MouseMove(object sender, MouseEventArgs e)
        {
            // TBD
        }

        void trackBar_gamma2_MouseUp(object sender, MouseEventArgs e)
        {
            // TBD
        }

        void trackBar_brightness_MouseDown(object sender, MouseEventArgs e)
        {
            // TBD
        }

        void trackBar_brightness_MouseMove(object sender, MouseEventArgs e)
        {
            // TBD
        }

        void trackBar_brightness_MouseUp(object sender, MouseEventArgs e)
        {
            // TBD
        }

        void trackBar_threshold_MouseDown(object sender, MouseEventArgs e)
        {
            // TBD
        }

        void trackBar_threshold_MouseMove(object sender, MouseEventArgs e)
        {
            // TBD
        }

        void trackBar_threshold_MouseUp(object sender, MouseEventArgs e)
        {
            // TBD
        }

        void trackBar_binary_MouseDown(object sender, MouseEventArgs e)
        {
            // TBD
        }

        void trackBar_binary_MouseMove(object sender, MouseEventArgs e)
        {
            // TBD
        }

        void trackBar_binary_MouseUp(object sender, MouseEventArgs e)
        {
            // TBD
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

        float gamma = 0.1f;
        float brightness = 0.1f;
        float threshold = 0.01f;
        int binary = 20;
        private void timer1_Tick(object sender, EventArgs e)
        {
            gamma += 0.3f;
            if (gamma > 2.5f)
                gamma = 0.1f;
            pictureBox1.Image = apply_gamma(filename, gamma);

            brightness += 0.3f;
            if (brightness > 2.5f)
                brightness = 0.1f;
            pictureBox2.Image = apply_brightness(filename, brightness);

            threshold += 0.06f;
            if (threshold > 1.0f)
                threshold = 0.01f;
            pictureBox3.Image = apply_threshold(filename, threshold);

            binary += 13;
            if (binary > 255)
                binary -= 255;
            pictureBox4.Image = apply_contrast_enhancement(filename, binary);


            pictureBox5.Image = apply_gamma2(filename, gamma);
        }

        private Bitmap apply_gamma(string filename, float gamma)
        {
            label1.Text = "Gamma = " + gamma.ToString();

            Image image = Image.FromFile(filename);

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

        private Bitmap apply_brightness(string filename, float brightness)
        {
            label2.Text = "Brightness = " + brightness.ToString();

            Image image = Image.FromFile(filename);

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

        private Bitmap apply_threshold(string filename, float threshold)
        {
            label3.Text = "Threshold = " + threshold.ToString();

            Image image = Image.FromFile(filename);

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


        //二值化對比 ST
        //private Bitmap apply_threshold(string filename, float threshold)
        private Bitmap apply_contrast_enhancement(string filename, int binary)
        {
            label4.Text = "二值化對比 " + binary.ToString();

            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式

            BinaryContrast(bitmap1, 3 * binary);

            return bitmap1;
        }

        // Perform binary contrast enhancement on the bitmap.
        private void BinaryContrast(Bitmap bm, int cutoff)
        {
            for (int y = 0; y < bm.Height; y++)
            {
                for (int x = 0; x < bm.Width; x++)
                {
                    Color clr = bm.GetPixel(x, y);
                    if (clr.R + clr.G + clr.B > cutoff)
                        bm.SetPixel(x, y, Color.White);
                    else
                        bm.SetPixel(x, y, Color.Black);
                }
            }
        }
        //二值化對比 SP


        private Bitmap apply_gamma2(string filename, float gamma)
        {
            label9.Text = "Gamma = " + gamma.ToString();

            //從pictureBox取得Bitmap
            Bitmap bitmap1 = (Bitmap)pictureBox1.Image;
            Bitmap bitmap2 = KiGamma(bitmap1, gamma);

            return bitmap2;
        }

        //C#圖片處理之Gamma校正
        //gamma值是用曲線表示的，這是一種人的眼睛對光的一種感應曲線，其中包括了物理量、身理感官及心理的感知度。

        /// <summary>
        /// Gamma校正
        /// </summary>
        /// <param name="bmp">輸入Bitmap</param>
        /// <param name="val">[0 <-明- 1 -暗-> 2]</param>
        /// <returns>輸出Bitmap</returns>
        public static Bitmap KiGamma(Bitmap bmp, float val)
        {
            if (bmp == null)
            {
                return null;
            }

            // 1表示無變化，就不做
            if (val == 1.0000f) return bmp;

            try
            {
                Bitmap b = new Bitmap(bmp.Width, bmp.Height);
                Graphics g = Graphics.FromImage(b);
                ImageAttributes attr = new ImageAttributes();

                attr.SetGamma(val, ColorAdjustType.Bitmap);
                g.DrawImage(bmp, new Rectangle(0, 0, bmp.Width, bmp.Height), 0, 0, bmp.Width, bmp.Height, GraphicsUnit.Pixel, attr);
                g.Dispose();
                return b;
            }
            catch
            {
                return null;
            }
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

        private void ChangeColorTone_Scroll(object sender, ScrollEventArgs e)
        {
            picColor.BackColor = Color.FromArgb(scrRed.Value, scrGreen.Value, scrBlue.Value);
            ColorPicture();
        }
    }
}
