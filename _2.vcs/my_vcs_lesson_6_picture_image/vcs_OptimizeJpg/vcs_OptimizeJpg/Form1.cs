using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;
using System.IO;

namespace vcs_OptimizeJpg
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private Image OriginalImage = null;

        // Select the default compression level.
        private void Form1_Load(object sender, EventArgs e)
        {
            cboCI.Text = "100";
        }

        // Display a sample that uses the selected compression index.
        private void cboCI_SelectedIndexChanged(object sender, EventArgs e)
        {
            lblCI.Text = cboCI.Text;
            ShowImageSample();
        }

        // Display a sample that uses the selected compression index.
        private void ShowImageSample()
        {
            if (OriginalImage == null)
            {
                return;
            }

            // Free the PictureBox's current image.
            if (pictureBox1.Image != null)
            {
                pictureBox1.Image.Dispose();
                pictureBox1.Image = null;
            }

            // Save the image with the selected compression level.
            long compression = long.Parse(cboCI.Text);
            string file_name = Application.StartupPath + "\\__temp.jpg";
            SaveJpg(OriginalImage, file_name, compression);

            // Display the result without locking the file.
            pictureBox1.Image = LoadBitmapUnlocked(file_name);

            // See how big the file is.
            FileInfo file_info = new FileInfo(file_name);
            lblFileSize.Text = file_info.Length.ToFileSizeApi();
        }

        // Return an ImageCodecInfo object for this mime type.
        private ImageCodecInfo GetEncoderInfo(string mime_type)
        {
            ImageCodecInfo[] encoders = ImageCodecInfo.GetImageEncoders();
            for (int i = 0; i <= encoders.Length; i++)
            {
                if (encoders[i].MimeType == mime_type)
                {
                    return encoders[i];
                }
            }
            return null;
        }

        // Save the file with a specific compression level.
        private void SaveJpg(Image image, string file_name, long compression)
        {
            try
            {
                EncoderParameters encoder_params = new EncoderParameters(1);
                encoder_params.Param[0] = new EncoderParameter(System.Drawing.Imaging.Encoder.Quality, compression);

                ImageCodecInfo image_codec_info = GetEncoderInfo("image/jpeg");
                File.Delete(file_name);
                image.Save(file_name, image_codec_info, encoder_params);
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error saving file '" + file_name + "'\nTry a different file name.\n" + ex.Message, "Save Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        // Load a bitmap without locking it.
        private Bitmap LoadBitmapUnlocked(string file_name)
        {
            using (Bitmap bm = new Bitmap(file_name))
            {
                return new Bitmap(bm);
            }
        }

        //開啟JPG檔
        private void button1_Click(object sender, EventArgs e)
        {
            if (ofdPicture.ShowDialog() == DialogResult.OK)
            {
                try
                {
                    // Load the file.
                    OriginalImage = LoadBitmapUnlocked(ofdPicture.FileName);

                    // Save at compression 100.
                    string file_name = Application.StartupPath + "\\__temp.jpg";
                    SaveJpg(OriginalImage, file_name, 100);

                    /*
                    string file_name100 = Application.StartupPath + "\\__temp100.jpg";
                    SaveJpg(OriginalImage, file_name100, 100);


                    string file_name60 = Application.StartupPath + "\\__temp60.jpg";
                    SaveJpg(OriginalImage, file_name60, 60);


                    string file_name05 = Application.StartupPath + "\\__temp05.jpg";
                    SaveJpg(OriginalImage, file_name05, 5);
                    */

                    // See how big the file is.
                    FileInfo file_info = new FileInfo(file_name);
                    lbl100.Text = file_info.Length.ToFileSizeApi();

                    // Display the file at the selected compression.
                    ShowImageSample();
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }
        }

        // Save the file with the selected compression level.
        private void button2_Click(object sender, EventArgs e)
        {
            if (OriginalImage == null)
            {
                richTextBox1.Text += "尚未開啟圖檔\n";
                return;
            }

            try
            {
                string filename = Application.StartupPath + "\\jpg_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
                OriginalImage.Save(filename, ImageFormat.Jpeg);
                richTextBox1.Text += "已存檔 : " + filename + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }

        }
    }
}
