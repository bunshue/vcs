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

namespace howto_optimize_jpg
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

        // Open a file.
        private void mnuFileOpen_Click(object sender, EventArgs e)
        {
            if (ofdPicture.ShowDialog()==DialogResult.OK)
            {
                try
                {
                    // Load the file.
                    OriginalImage = LoadBitmapUnlocked(ofdPicture.FileName);

                    // Save at compression 100.
                    string file_name = Application.StartupPath + "\\__temp.jpg";
                    SaveJpg(OriginalImage, file_name, 100);

                    // See how big the file is.
                    FileInfo file_info = new FileInfo(file_name);
                    lbl100.Text = file_info.Length.ToFileSizeApi();

                    // Display the file at the selected compression.
                    ShowImageSample();
                    mnuFileSaveAs.Enabled = true;
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Error loading file //" +
                        ofdPicture.FileName + "//\n" + ex.Message,
                        "Load Error", MessageBoxButtons.OK, 
                        MessageBoxIcon.Error);
                }
            }
        }

        // Save the file with the selected compression level.
        private void mnuFileSaveAs_Click(object sender, EventArgs e)
        {
            if (OriginalImage == null) return;

            if (sfdPicture.ShowDialog() == DialogResult.OK)
            {
                try
                {
                    OriginalImage.Save(sfdPicture.FileName, ImageFormat.Jpeg);
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Error saving file //" +
                        sfdPicture.FileName + "//\n" + ex.Message,
                        "Save Error", MessageBoxButtons.OK,
                        MessageBoxIcon.Error);
                }
            }
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
            if (OriginalImage == null) return;

            // Free the PictureBox's current image.
            if (picImage.Image != null)
            {
                picImage.Image.Dispose();
                picImage.Image = null;
            }

            // Save the image with the selected compression level.
            long compression = long.Parse(cboCI.Text);
            string file_name = Application.StartupPath + "\\__temp.jpg";
            SaveJpg(OriginalImage, file_name, compression);

            // Display the result without locking the file.
            picImage.Image = LoadBitmapUnlocked(file_name);

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
                if (encoders[i].MimeType == mime_type) return encoders[i];
            }
            return null;
        }

        // Save the file with a specific compression level.
        private void SaveJpg(Image image, string file_name, long compression)
        {
            try
            {
                EncoderParameters encoder_params = new EncoderParameters(1);
                encoder_params.Param[0] = new EncoderParameter(
                    System.Drawing.Imaging.Encoder.Quality, compression);

                ImageCodecInfo image_codec_info = GetEncoderInfo("image/jpeg");
                File.Delete(file_name);
                image.Save(file_name, image_codec_info, encoder_params);
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error saving file '" + file_name +
                    "'\nTry a different file name.\n" + ex.Message,
                    "Save Error", MessageBoxButtons.OK,
                    MessageBoxIcon.Error);
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
    }
}
