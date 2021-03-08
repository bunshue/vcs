using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Drawing2D;
using System.Drawing.Imaging;

namespace vcs_PropertiesSettingsDefault
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Restore parameters.
        private void Form1_Load(object sender, EventArgs e)
        {
            this.SetBounds(
                Properties.Settings.Default.Left,
                Properties.Settings.Default.Top,
                Properties.Settings.Default.Width,
                Properties.Settings.Default.Height);

            txtDirectory.Text = Properties.Settings.Default.Directory;
            if (txtDirectory.Text.Length == 0) txtDirectory.Text = Application.StartupPath;
            cboExtension.Text = Properties.Settings.Default.NewExtension;
        }

        // Save parameters.
        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            Properties.Settings.Default.Left = this.Left;
            Properties.Settings.Default.Top = this.Top;
            Properties.Settings.Default.Width = this.Width;
            Properties.Settings.Default.Height = this.Height;

            Properties.Settings.Default.Directory = txtDirectory.Text;
            Properties.Settings.Default.NewExtension = cboExtension.Text;

            Properties.Settings.Default.Save();
        }

        // Let the user browse for the directory.
        private void btnPickDirectory_Click(object sender, EventArgs e)
        {
            try
            {
                folderBrowserDialog1.SelectedPath = txtDirectory.Text;
            }
            catch
            {
            }

            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                txtDirectory.Text = folderBrowserDialog1.SelectedPath;
            }
        }

        // Process the files in the selected directory.
        private void btnGo_Click(object sender, EventArgs e)
        {
            this.Cursor = Cursors.WaitCursor;
            this.Refresh();

            // Get the new image format.
            string new_ext = cboExtension.Text;
            ImageFormat new_format = ExtensionFormat(new_ext);

            // Enumerate the files.
            DirectoryInfo dir_info = new System.IO.DirectoryInfo(txtDirectory.Text);
            foreach (FileInfo file_info in dir_info.GetFiles())
            {
                try
                {
                    txtProcessing.Text = file_info.Name;
                    txtProcessing.Refresh();

                    // See what kind of file this is.
                    string old_ext = file_info.Extension.ToLower();
                    ImageFormat old_format = ExtensionFormat(old_ext);

                    // Only process if the file has a graphic
                    // extension and we're changing the type
                    if ((old_format != null) && (old_format != new_format))
                    {
                        /*
                        Bitmap bm = new Bitmap(file_info.FullName);
                        string new_name = file_info.FullName.Replace(old_ext, new_ext);

                        bm.Save(new_name, new_format);
                        */
                    }
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Error processing file '" +
                        file_info.Name + "'\n" + ex.Message,
                        "Error",
                        MessageBoxButtons.OK,
                        MessageBoxIcon.Error);
                }
            } // foreach file_info

            txtProcessing.Clear();
            this.Cursor = Cursors.Default;
        }

        // Return the ImageFormat for this file extension.
        private ImageFormat ExtensionFormat(string extension)
        {
            switch (extension)
            {
                case ".png":
                    return ImageFormat.Png;
                case ".jpg":
                case ".jpeg":
                    return ImageFormat.Jpeg;
                case ".bmp":
                    return ImageFormat.Bmp;
                case ".gif":
                    return ImageFormat.Gif;
                case ".tif":
                case ".tiff":
                    return ImageFormat.Tiff;
            }
            return null;
        }

    }
}
