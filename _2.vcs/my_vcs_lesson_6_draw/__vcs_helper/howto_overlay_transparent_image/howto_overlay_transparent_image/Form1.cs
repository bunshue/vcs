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

namespace howto_overlay_transparent_image
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void mnuFileExit_Click(object sender, EventArgs e)
        {
            Close();
        }

        // The background image.
        private Bitmap BackgroundBitmap = null;

        // The overlay image.
        private Bitmap OverlayBitmap = null;

        // The current combined image.
        private Bitmap CombinedBitmap = null;

        // The location of the overlay image.
        private Point OverlayLocation = new Point(0, 0);

        // Reduce flicker.
        private void Form1_Load(object sender, EventArgs e)
        {
            DoubleBuffered = true;
        }

        // Let the user open a file.
        private void mnuFileOpen_Click(object sender, EventArgs e)
        {
            if (ofdFile.ShowDialog() == DialogResult.OK)
            {
                try
                {
                    // Open the file.
                    BackgroundBitmap = new Bitmap(ofdFile.FileName);
                    picImage.Image = BackgroundBitmap;
                    picImage.Visible = true;
                    ClientSize = new Size(
                        picImage.Right + picImage.Left,
                        picImage.Bottom + picImage.Left);
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Error opening file.\n" + ex.Message,
                        "Open Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
        }

        // Load the overlay image.
        private void mnuFileOverlay_Click(object sender, EventArgs e)
        {
            if (ofdFile.ShowDialog() == DialogResult.OK)
            {
                try
                {
                    // Open the file.
                    OverlayBitmap = new Bitmap(ofdFile.FileName);
                    picImage.Cursor = Cursors.Cross;

                    // Display the combined image.
                    ShowCombinedImage();
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Error opening file.\n" + ex.Message,
                        "Open Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
        }

        // Display the combined image.
        private void ShowCombinedImage()
        {
            // If there's no background image, do nothing.
            if (BackgroundBitmap == null) return;

            // Copy the background.
            CombinedBitmap = new Bitmap(BackgroundBitmap);

            // Add the overlay.
            if (OverlayBitmap != null)
            {
                using (Graphics gr = Graphics.FromImage(CombinedBitmap))
                {
                    gr.DrawImage(OverlayBitmap, OverlayLocation);
                }
            }

            // Display the result.
            picImage.Image = CombinedBitmap;
        }

        // Drag the overlay image.
        private void picImage_MouseMove(object sender, MouseEventArgs e)
        {
            if (OverlayBitmap == null) return;
            OverlayLocation = new Point(
                e.X - OverlayBitmap.Width / 2,
                e.Y - OverlayBitmap.Height / 2);
            ShowCombinedImage();
        }

        // Finish dragging the overlay image.
        private void picImage_MouseClick(object sender, MouseEventArgs e)
        {
            if (OverlayBitmap == null) return;
            OverlayBitmap = null;
            picImage.Cursor = Cursors.Default;

            // Make the overlay permanent.
            BackgroundBitmap = CombinedBitmap;
        }

        // Save the current result image.
        private void mnuFileSave_Click(object sender, EventArgs e)
        {
            if (CombinedBitmap == null) return;
            if (sfdFile.ShowDialog() == DialogResult.OK)
            {
                SaveBitmapUsingExtension(CombinedBitmap, sfdFile.FileName);
            }
        }

        // Save the file with the appropriate format.
        // Throw a NotSupportedException if the file
        // has an unknown extension.
        public void SaveBitmapUsingExtension(Bitmap bm, string filename)
        {
            string extension = Path.GetExtension(filename);
            switch (extension.ToLower())
            {
                case ".bmp":
                    bm.Save(filename, ImageFormat.Bmp);
                    break;
                case ".exif":
                    bm.Save(filename, ImageFormat.Exif);
                    break;
                case ".gif":
                    bm.Save(filename, ImageFormat.Gif);
                    break;
                case ".jpg":
                case ".jpeg":
                    bm.Save(filename, ImageFormat.Jpeg);
                    break;
                case ".png":
                    bm.Save(filename, ImageFormat.Png);
                    break;
                case ".tif":
                case ".tiff":
                    bm.Save(filename, ImageFormat.Tiff);
                    break;
                default:
                    throw new NotSupportedException(
                        "Unknown file extension " + extension);
            }
        }
    }
}
