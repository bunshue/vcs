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
using System.Drawing.Drawing2D;

namespace vcs_ZoomPicture5
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The loaded image.
        private Bitmap LoadedImage = null;

        // True if we should ignore change events.
        private bool IgnoreChanges = false;

        private void Form1_Load(object sender, EventArgs e)
        {
            // Load an image file.
            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            try
            {
                LoadedImage = LoadBitmap(filename);
                SetScale(1, true, true, true);
                txtWidth.Enabled = true;
                txtHeight.Enabled = true;
                txtPercent.Enabled = true;
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        // Load a bitmap without locking the file.
        private Bitmap LoadBitmap(string filename)
        {
            using (Bitmap bm = new Bitmap(filename))
            {
                return (Bitmap)bm.Clone();
            }
        }

        private void SetScale(double scale, bool show_width, bool show_height, bool show_percent)
        {
            int width = (int)(LoadedImage.Width * scale);
            int height = (int)(LoadedImage.Height * scale);
            if ((width < 1) || (height < 1)) return;

            Bitmap scaled_image = new Bitmap(width, height);
            using (Graphics gr = Graphics.FromImage(scaled_image))
            {
                gr.InterpolationMode = InterpolationMode.HighQualityBilinear;
                Rectangle source = new Rectangle(
                    0, 0, LoadedImage.Width, LoadedImage.Height);
                Point[] dest =
                {
                    new Point(0, 0),
                    new Point(width, 0),
                    new Point(0, height),
                };
                gr.DrawImage(LoadedImage, dest, source, GraphicsUnit.Pixel);
            }
            pictureBox1.Image = scaled_image;

            IgnoreChanges = true;
            if (show_width) txtWidth.Text = width.ToString("0");
            if (show_height) txtHeight.Text = height.ToString("0");
            if (show_percent)
            {
                int percent = (int)(scale * 100);
                txtPercent.Text = percent.ToString("0");
            }
            IgnoreChanges = false;
        }

        private void txtWidth_TextChanged(object sender, EventArgs e)
        {
            if (IgnoreChanges) return;

            double width;
            if (double.TryParse(txtWidth.Text, out width))
            {
                SetScale(width / LoadedImage.Width, false, true, true);
            }
        }

        private void txtHeight_TextChanged(object sender, EventArgs e)
        {
            if (IgnoreChanges) return;

            double height;
            if (double.TryParse(txtHeight.Text, out height))
            {
                SetScale(height / LoadedImage.Height, true, false, true);
            }
        }

        private void txtPercent_TextChanged(object sender, EventArgs e)
        {
            if (IgnoreChanges) return;

            double percent;
            if (double.TryParse(txtPercent.Text, out percent))
            {
                SetScale(percent / 100, true, true, false);
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

            try
            {
                pictureBox1.Image.Save(filename, ImageFormat.Bmp);
                richTextBox1.Text += "已存檔 : " + filename + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }

        }


    }
}
