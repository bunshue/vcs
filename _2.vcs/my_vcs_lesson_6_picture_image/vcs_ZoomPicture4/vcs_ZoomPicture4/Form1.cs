using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat

namespace vcs_ZoomPicture4
{
    public partial class Form1 : Form
    {
        private float PictureScale = 1.0f;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;

            string filename = @"C:\______test_files1\picture1.jpg";

            Bitmap bm = LoadBitmapUnlocked(filename);
            pictureBox1.ClientSize = new Size(bm.Width, bm.Height);
            pictureBox1.Image = bm;
        }

        // Load a bitmap without locking it.
        private Bitmap LoadBitmapUnlocked(string file_name)
        {
            using (Bitmap bm = new Bitmap(file_name))
            {
                return new Bitmap(bm);
            }
        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            int value = trackBar1.Value;
            switch (value)
            {
                case 0: PictureScale = 0.5f; break;
                case 1: PictureScale = 0.75f; break;
                case 2: PictureScale = 1.0f; break;
                case 3: PictureScale = 1.25f; break;
                case 4: PictureScale = 1.5f; break;
                case 5: PictureScale = 2f; break;
                default: PictureScale = 2.5f; break;
            }
            label1.Text = PictureScale.ToString() + " X";

            pictureBox1.ClientSize = new Size((int)(PictureScale * pictureBox1.Image.Width), (int)(PictureScale * pictureBox1.Image.Height));
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = Application.StartupPath + "\\zoom_picture_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

            // Make a bitmap of the correct size.
            using (Bitmap bitmap1 = new Bitmap(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height))
            {
                // Copy the original image onto the new bitmap.
                using (Graphics gr = Graphics.FromImage(bitmap1))
                {
                    Rectangle source_rect = new Rectangle(
                        0, 0, pictureBox1.Image.Width, pictureBox1.Image.Height);
                    Rectangle dest_rect = new Rectangle(
                        0, 0, bitmap1.Width, bitmap1.Height);
                    gr.DrawImage(pictureBox1.Image,
                        dest_rect, source_rect, GraphicsUnit.Pixel);
                }

                // Save the bitmap.
                bitmap1.Save(filename, ImageFormat.Bmp);
                //richTextBox1.Text += "存檔成功\n";
                //richTextBox1.Text += "已存檔 : " + filename + "\n";
            }


        }
    }
}
