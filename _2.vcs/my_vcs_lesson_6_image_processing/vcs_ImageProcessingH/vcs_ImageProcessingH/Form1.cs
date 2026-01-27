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
        string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
        int cutoff_value = 0;

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

            filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";
            pictureBox6.Image = Image.FromFile(filename);
            cutoff_value = trackBar_transparent.Value;
            label6.Text = "亮度 " + cutoff_value.ToString() + " 以上, 設定為透明";
            //ShowImage();
        }

        void show_item_location()
        {
            int W = 305;
            int H = 400;
            int x_st = 20;
            int y_st = 20;
            int dx = W + 50;
            int dy = H + 100;
            int dd1 = 40;
            int dd2 = 85;

            bt_auto.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            label0.Location = new Point(x_st + dx * 0 + 100, y_st + dy * 0);
            label1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            label2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            label4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            label5.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            label6.Location = new Point(x_st + dx * 3, y_st + dy * 1);

            label0.Text = "原圖";
            label1.Text = "Gamma";
            label2.Text = "Gamma";
            label4.Text = "Threshold";
            label5.Text = "二值化對比";
            label6.Text = "亮度";

            trackBar_gamma1.Location = new Point(x_st + dx * 1, y_st + dy * 0 + dd1);
            trackBar_gamma2.Location = new Point(x_st + dx * 2, y_st + dy * 0 + dd1);
            trackBar_threshold.Location = new Point(x_st + dx * 1, y_st + dy * 1 + dd1);
            trackBar_binary.Location = new Point(x_st + dx * 2, y_st + dy * 1 + dd1);
            trackBar_transparent.Location = new Point(x_st + dx * 3, y_st + dy * 1 + dd1);
            bt_save.Location = new Point(x_st + dx * 4, y_st + dy * 1 + dd1);

            pictureBox0.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox2.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox3.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox4.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox5.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox6.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox6.BackColor = Color.Pink;

            pictureBox0.Size = new Size(W, H);
            pictureBox1.Size = new Size(W, H);
            pictureBox2.Size = new Size(W, H);
            pictureBox3.Size = new Size(W, H);
            pictureBox4.Size = new Size(W, H);
            pictureBox5.Size = new Size(W, H);
            pictureBox6.Size = new Size(W * 3 / 2, H);

            pictureBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0 + dd2);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0 + dd2);
            pictureBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0 + dd2);
            pictureBox3.Location = new Point(x_st + dx * 0, y_st + dy * 1 + dd2);
            pictureBox4.Location = new Point(x_st + dx * 1, y_st + dy * 1 + dd2);
            pictureBox5.Location = new Point(x_st + dx * 2, y_st + dy * 1 + dd2);
            pictureBox6.Location = new Point(x_st + dx * 3, y_st + dy * 1 + dd2);

            richTextBox1.Size = new Size(W, H);
            richTextBox1.Location = new Point(x_st + dx * 4 + 150, y_st + dy * 1 + dd2);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            groupBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);

            trackBar_gamma1.MouseMove += new MouseEventHandler(trackBar_gamma1_MouseMove);
            trackBar_gamma1.MouseUp += new MouseEventHandler(trackBar_gamma1_MouseUp);
            trackBar_gamma2.MouseMove += new MouseEventHandler(trackBar_gamma2_MouseMove);
            trackBar_gamma2.MouseUp += new MouseEventHandler(trackBar_gamma2_MouseUp);
            trackBar_threshold.MouseMove += new MouseEventHandler(trackBar_threshold_MouseMove);
            trackBar_threshold.MouseUp += new MouseEventHandler(trackBar_threshold_MouseUp);
            trackBar_binary.MouseMove += new MouseEventHandler(trackBar_binary_MouseMove);
            trackBar_binary.MouseUp += new MouseEventHandler(trackBar_binary_MouseUp);
            trackBar_transparent.MouseMove += new MouseEventHandler(trackBar_transparent_MouseMove);
            trackBar_transparent.MouseUp += new MouseEventHandler(trackBar_transparent_MouseUp);

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            bt_exit_setup();
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

        void trackBar_gamma1_MouseMove(object sender, MouseEventArgs e)
        {
            float gamma = (float)(trackBar_gamma1.Value) / 10;
            label1.Text = "Gamma = " + gamma.ToString();
        }

        void trackBar_gamma1_MouseUp(object sender, MouseEventArgs e)
        {
            float gamma = (float)(trackBar_gamma1.Value) / 10;
            if (gamma < 0.1)
                gamma = 0.1f;
            pictureBox1.Image = apply_gamma1(filename, gamma);
        }

        void trackBar_gamma2_MouseMove(object sender, MouseEventArgs e)
        {
            float gamma = (float)(trackBar_gamma2.Value) / 10;
            label2.Text = "Gamma = " + gamma.ToString();
        }

        void trackBar_gamma2_MouseUp(object sender, MouseEventArgs e)
        {
            float gamma = (float)(trackBar_gamma2.Value) / 10;
            pictureBox2.Image = apply_gamma2(filename, gamma);
        }

        void trackBar_threshold_MouseMove(object sender, MouseEventArgs e)
        {
            float threshold = (float)(trackBar_threshold.Value) / 100;
            label4.Text = "Threshold = " + threshold.ToString();
        }

        void trackBar_threshold_MouseUp(object sender, MouseEventArgs e)
        {
            float threshold = (float)(trackBar_threshold.Value) / 100;
            pictureBox4.Image = apply_threshold(filename, threshold);
        }

        void trackBar_binary_MouseMove(object sender, MouseEventArgs e)
        {
            int binary = trackBar_binary.Value;
            label5.Text = "二值化對比 = " + binary.ToString();
        }

        void trackBar_binary_MouseUp(object sender, MouseEventArgs e)
        {
            int binary = trackBar_binary.Value;
            pictureBox5.Image = apply_contrast_enhancement(filename, binary);
        }

        void trackBar_transparent_MouseMove(object sender, MouseEventArgs e)
        {
            cutoff_value = trackBar_transparent.Value;
            label6.Text = "亮度 " + cutoff_value.ToString() + " 以上, 設定為透明";
        }

        void trackBar_transparent_MouseUp(object sender, MouseEventArgs e)
        {
            int binary = trackBar_transparent.Value;
            //pictureBox5.Image = apply_contrast_enhancement(filename, binary);

            cutoff_value = trackBar_transparent.Value;
            label6.Text = "亮度 " + cutoff_value.ToString() + " 以上, 設定為透明";

            string filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";
            ShowImage(filename);
        }

        private void ShowImage(string filename)
        {
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式

            // Prepare the ImageAttributes.
            Color low_color = Color.FromArgb(cutoff_value, cutoff_value, cutoff_value);
            Color high_color = Color.FromArgb(255, 255, 255);
            ImageAttributes image_attr = new ImageAttributes();
            image_attr.SetColorKey(low_color, high_color);

            // Make the result image.
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            Bitmap bitmap2 = new Bitmap(W, H);

            // Process the image.
            using (Graphics g = Graphics.FromImage(bitmap2))
            {
                // Fill with magenta.
                //g.Clear(Color.Magenta);
                //g.Clear(Color.Lime);

                // Copy the original image onto the result
                // image while using the ImageAttributes.
                Rectangle dest_rect = new Rectangle(0, 0, W, H);
                g.DrawImage(bitmap1, dest_rect, 0, 0, W, H, GraphicsUnit.Pixel, image_attr);
            }
            // Display the image.
            pictureBox6.Image = bitmap2;
        }

        float gamma = 0.1f;
        float threshold = 0.01f;
        int binary = 20;
        private void timer1_Tick(object sender, EventArgs e)
        {
            gamma += 0.3f;
            if (gamma > 2.5f)
                gamma = 0.1f;
            pictureBox1.Image = apply_gamma1(filename, gamma);

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

        private Bitmap apply_gamma1(string filename, float gamma)
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

        private Bitmap apply_threshold(string filename, float threshold)
        {
            label4.Text = "Threshold = " + threshold.ToString();

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
            label5.Text = "二值化對比 " + binary.ToString();

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
            label2.Text = "Gamma = " + gamma.ToString();

            //從pictureBox取得Bitmap
            Bitmap bitmap1 = (Bitmap)pictureBox0.Image;
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

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_auto_Click(object sender, EventArgs e)
        {
            if (bt_auto.Text == "自動")
            {
                bt_auto.Text = "手動";
                timer1.Enabled = true;
                trackBar_gamma1.Visible = false;
                trackBar_gamma2.Visible = false;
                trackBar_threshold.Visible = false;
                trackBar_binary.Visible = false;
                trackBar_transparent.Visible = false;
            }
            else
            {
                bt_auto.Text = "自動";
                timer1.Enabled = false;
                trackBar_gamma1.Visible = true;
                trackBar_gamma2.Visible = true;
                trackBar_threshold.Visible = true;
                trackBar_binary.Visible = true;
                trackBar_transparent.Visible = true;
            }
        }

        private void bt_save_Click(object sender, EventArgs e)
        {
            // Make a copy of the result image.
            using (Bitmap bmp = (Bitmap)pictureBox6.Image.Clone())
            {
                bmp.MakeTransparent(Color.Magenta);

                save_image_to_drive(bmp);
            }
        }

        void save_image_to_drive(Bitmap bitmap1)
        {
            if (bitmap1 != null)
            {
                string filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".png";
                bitmap1.Save(@filename, ImageFormat.Png);

                richTextBox1.Text += "已存檔 : " + filename + "\n";
            }
            else
            {
                richTextBox1.Text += "無圖可存\n";
            }
        }
    }
}
