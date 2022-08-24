using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;

namespace howto_make_light_transparent
{
    public partial class Form1 : Form
    {
        // The original image.
        Bitmap bitmap1 = null;

        //string filename = "C:\\______test_files\\bear.jpg";
        string filename = @"C:\______test_files\elephant.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bitmap1 = new Bitmap(filename);
            ShowImage();
        }

        // Rebuild the image.
        private void scrBrightness_Scroll(object sender, ScrollEventArgs e)
        {
            lblBrightness.Text = scrBrightness.Value.ToString();
            ShowImage();
        }

        // Make an image setting pixels brighter
        // than the cutoff value to magenta.
        private void ShowImage()
        {
            if (bitmap1 == null) return;

            // Get the cutoff.
            int cutoff = scrBrightness.Value;

            // Prepare the ImageAttributes.
            Color low_color = Color.FromArgb(cutoff, cutoff, cutoff);
            Color high_color = Color.FromArgb(255, 255, 255);
            ImageAttributes image_attr = new ImageAttributes();
            image_attr.SetColorKey(low_color, high_color);

            // Make the result image.
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            Bitmap bm = new Bitmap(W, H);

            // Process the image.
            using (Graphics gr = Graphics.FromImage(bm))
            {
                // Fill with magenta.
                //gr.Clear(Color.Magenta);
                //gr.Clear(Color.Lime);

                // Copy the original image onto the result
                // image while using the ImageAttributes.
                Rectangle dest_rect = new Rectangle(0, 0, W, H);
                gr.DrawImage(bitmap1, dest_rect, 0, 0, W, H, GraphicsUnit.Pixel, image_attr);
            }

            // Display the image.
            pictureBox1.Image = bm;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // Make a copy of the result image.
            using (Bitmap bm = (Bitmap)pictureBox1.Image.Clone())
            {
                bm.MakeTransparent(Color.Magenta);

                save_image_to_drive(bm);
            }
        }

        void save_image_to_drive(Bitmap bitmap1)
        {
            if (bitmap1 != null)
            {
                string filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                String filename1 = filename + ".jpg";
                String filename2 = filename + ".bmp";
                String filename3 = filename + ".png";

                try
                {
                    bitmap1.Save(@filename1, ImageFormat.Jpeg);
                    bitmap1.Save(@filename2, ImageFormat.Bmp);
                    bitmap1.Save(@filename3, ImageFormat.Png);

                    //richTextBox1.Text += "存檔成功\n";
                    //richTextBox1.Text += "已存檔 : " + filename1 + "\n";
                    //richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                    //richTextBox1.Text += "已存檔 : " + filename3 + "\n";
                }
                catch (Exception ex)
                {
                    //richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }
            //else
                //richTextBox1.Text += "無圖可存\n";
        }



    }
}
