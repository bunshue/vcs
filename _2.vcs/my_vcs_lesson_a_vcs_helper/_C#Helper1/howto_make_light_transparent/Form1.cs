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
        Bitmap bitmap1 = null;

        //string filename = @"C:\_git\vcs\_1.data\______test_files1\bear.jpg";
        string filename = @"C:\_git\vcs\_1.data\______test_files1\elephant.jpg";
        int cutoff_value = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bitmap1 = new Bitmap(filename);
            cutoff_value = scrBrightness.Value;
            label1.Text = "亮度 " + cutoff_value.ToString() + " 以上, 設定為透明";
            ShowImage();
        }

        // Rebuild the image.
        private void scrBrightness_Scroll(object sender, ScrollEventArgs e)
        {
            cutoff_value = scrBrightness.Value;
            label1.Text = "亮度 " + cutoff_value.ToString() + " 以上, 設定為透明";
            ShowImage();
        }

        // Make an image setting pixels brighter
        // than the cutoff value to magenta.
        private void ShowImage()
        {
            if (bitmap1 == null)
            {
                return;
            }

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
            pictureBox1.Image = bitmap2;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // Make a copy of the result image.
            using (Bitmap bmp = (Bitmap)pictureBox1.Image.Clone())
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

