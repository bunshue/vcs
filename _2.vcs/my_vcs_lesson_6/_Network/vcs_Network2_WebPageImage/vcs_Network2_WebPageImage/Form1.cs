using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

// Add a reference to Microsoft.mshtml.
using mshtml;
using System.IO;
using System.Net;
using System.Drawing.Imaging;

namespace vcs_Network2_WebPageImage
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Navigate to the entered URL.
        private void btnGo_Click(object sender, EventArgs e)
        {
            try
            {
                wbrWebSite.Navigate(txtUrl.Text);
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error navigating to web site " +
                    txtUrl.Text + '\n' + ex.Message,
                    "Navigation Error",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Error);
            }
        }

        // Show the images from the URL.
        private bool Running = false;
        private void btnListImages_Click(object sender, EventArgs e)
        {
            if (btnListImages.Text == "List Images")
            {
                this.Cursor = Cursors.WaitCursor;
                btnListImages.Text = "Stop";
                btnGo.Enabled = false;
                btnSaveImages.Enabled = false;
                Application.DoEvents();

                // Remove old images.
                for (int i = flpPictures.Controls.Count - 1; i >= 0; i--)
                {
                    flpPictures.Controls[i].Parent = null;
                }

                // List the images on this page.
                HtmlDocument doc = wbrWebSite.Document;
                Running = true;
                foreach (HtmlElement element in doc.Images)
                {
                    mshtml.HTMLImg dom_element = (mshtml.HTMLImg)element.DomElement;
                    string src = dom_element.src;

                    PictureBox pic = new PictureBox();
                    pic.BorderStyle = BorderStyle.Fixed3D;
                    pic.Image = GetPicture(src);
                    SetPictureBoxSize(pic);
                    pic.Parent = flpPictures;
                    pic.Tag = src;
                    tipFileName.SetToolTip(pic, src);

                    pic.Click += pic_Click;

                    Application.DoEvents();

                    if (!Running)
                    {
                        break;
                    }
                }
                Running = false;

                btnListImages.Text = "List Images";
                btnGo.Enabled = true;
                btnSaveImages.Enabled = true;
                this.Cursor = Cursors.Default;
            }
            else
            {
                Running = false;
            }
        }

        // Set the PictureBox to AutoSize if it's reasonably small
        // or give it a maximum size if it's too big.
        private void SetPictureBoxSize(PictureBox pic)
        {
            const int max_width = 300;
            const int max_height = 300;
            if ((pic.Image.Width <= max_width) &&
                (pic.Image.Height <= max_height))
            {
                // It's small enough.
                pic.SizeMode = PictureBoxSizeMode.AutoSize;
            }
            else
            {
                // Restrict its size.
                float w_scale = max_width / (float)pic.Image.Width;
                float h_scale = max_height / (float)pic.Image.Height;
                float scale = Math.Min(w_scale, h_scale);
                pic.SizeMode = PictureBoxSizeMode.Zoom;
                pic.Size = new Size((int)(scale * pic.Image.Width), (int)(scale * pic.Image.Height));
            }
        }

        // Get the picture at a given URL.
        private Image GetPicture(string url)
        {
            WebClient wc = new WebClient();
            try
            {
                url = url.Trim();
                if (!url.ToLower().StartsWith("http://"))
                {
                    url = "http://" + url;
                }
                MemoryStream image_stream = new MemoryStream(wc.DownloadData(url));
                return Image.FromStream(image_stream);
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error downloading picture " + url + '\n' + ex.Message, "Download Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            return null;
        }

        // Remove the clicked PictureBox.
        private void pic_Click(object sender, EventArgs e)
        {
            PictureBox pic = sender as PictureBox;
            pic.Parent = null;
        }

        // Stop. This may take a little while as pending downloads complete.
        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            Running = false;
        }

        // Set the initial save directory.
        private void Form1_Load(object sender, EventArgs e)
        {
            txtDirectory.Text = Path.Combine(Application.StartupPath, "Images");
        }

        // Save the images that have not been removed.
        private void btnSaveImages_Click(object sender, EventArgs e)
        {
            Cursor = Cursors.WaitCursor;

            // Get the directory path and make sure the directory exists.
            string dir_name = txtDirectory.Text;
            if (!dir_name.EndsWith(@"\"))
            {
                dir_name += @"\";
            }
            Directory.CreateDirectory(dir_name);

            foreach (PictureBox pic in flpPictures.Controls)
            {
                Bitmap bm = (Bitmap)pic.Image;
                string filename = dir_name + Path.GetFileName(pic.Tag.ToString());
                SaveImage(bm, filename);
            }

            Cursor = Cursors.Default;
        }

        // Save the file with the appropriate format.
        public void SaveImage(Image image, string filename)
        {
            string extension = Path.GetExtension(filename);
            switch (extension.ToLower())
            {
                case ".bmp":
                    image.Save(filename, ImageFormat.Bmp);
                    break;
                case ".exif":
                    image.Save(filename, ImageFormat.Exif);
                    break;
                case ".gif":
                    image.Save(filename, ImageFormat.Gif);
                    break;
                case ".jpg":
                case ".jpeg":
                    image.Save(filename, ImageFormat.Jpeg);
                    break;
                case ".png":
                    image.Save(filename, ImageFormat.Png);
                    break;
                case ".tif":
                case ".tiff":
                    image.Save(filename, ImageFormat.Tiff);
                    break;
                default:
                    throw new NotSupportedException("Unknown file extension " + extension);
            }
        }
    }
}
