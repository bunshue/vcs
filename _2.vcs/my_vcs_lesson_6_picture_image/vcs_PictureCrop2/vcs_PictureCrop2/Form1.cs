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

namespace vcs_PictureCrop2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Exit the program.
        private void mnuFileExit_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        // The original image.
        private Bitmap OriginalImage;
        
        // The currently cropped image.
        private Bitmap CroppedImage;

        // The cropped image with the selection rectangle.
        private Bitmap DisplayImage;
        private Graphics DisplayGraphics;

        // Open a file.
        private void mnuFileOpen_Click(object sender, EventArgs e)
        {
            if (ofdPicture.ShowDialog() == DialogResult.OK)
            {
                OriginalImage = LoadBitmapUnlocked(ofdPicture.FileName);
                CroppedImage = OriginalImage.Clone() as Bitmap;
                DisplayImage = CroppedImage.Clone() as Bitmap;
                DisplayGraphics = Graphics.FromImage(DisplayImage);

                picCropped.Image = DisplayImage;
                picCropped.Visible = true;
            }
        }

        // Let the user select an area.
        private bool Drawing = false;
        private Point StartPoint, EndPoint;
        private void picCropped_MouseDown(object sender, MouseEventArgs e)
        {
            Drawing = true;
            StartPoint = e.Location;

            // Draw the area selected.
            DrawSelectionBox(e.Location);
        }

        private void picCropped_MouseMove(object sender, MouseEventArgs e)
        {
            if (!Drawing) return;

            // Draw the area selected.
            DrawSelectionBox(e.Location);
        }

        private void picCropped_MouseUp(object sender, MouseEventArgs e)
        {
            if (!Drawing) return;
            Drawing = false;

            // Crop.
            // Get the selected area's dimensions.
            int x = Math.Min(StartPoint.X, EndPoint.X);
            int y = Math.Min(StartPoint.Y, EndPoint.Y);
            int width = Math.Abs(StartPoint.X - EndPoint.X);
            int height = Math.Abs(StartPoint.Y - EndPoint.Y);
            Rectangle source_rect = new Rectangle(x, y, width, height);
            Rectangle dest_rect = new Rectangle(0, 0, width, height);

            // Copy that part of the image to a new bitmap.
            DisplayImage = new Bitmap(width, height);
            DisplayGraphics = Graphics.FromImage(DisplayImage);
            DisplayGraphics.DrawImage(CroppedImage, dest_rect, source_rect, GraphicsUnit.Pixel);

            // Display the new bitmap.
            CroppedImage = DisplayImage;
            DisplayImage = CroppedImage.Clone() as Bitmap;
            DisplayGraphics = Graphics.FromImage(DisplayImage);
            picCropped.Image = DisplayImage;
            picCropped.Refresh();
        }

        // Draw the area selected.
        private void DrawSelectionBox(Point end_point)
        {
            // Save the end point.
            EndPoint = end_point;
            if (EndPoint.X < 0) EndPoint.X = 0;
            if (EndPoint.X >= CroppedImage.Width) EndPoint.X = CroppedImage.Width - 1;
            if (EndPoint.Y < 0) EndPoint.Y = 0;
            if (EndPoint.Y >= CroppedImage.Height) EndPoint.Y = CroppedImage.Height - 1;

            // Reset the image.
            DisplayGraphics.DrawImageUnscaled(CroppedImage, 0, 0);

            // Draw the selection area.
            int x = Math.Min(StartPoint.X, EndPoint.X);
            int y = Math.Min(StartPoint.Y, EndPoint.Y);
            int width = Math.Abs(StartPoint.X - EndPoint.X);
            int height = Math.Abs(StartPoint.Y - EndPoint.Y);
            DisplayGraphics.DrawRectangle(Pens.Red, x, y, width, height);
            picCropped.Refresh();
        }

        // Display the original image.
        private void mnuPictureReset_Click(object sender, EventArgs e)
        {
            CroppedImage = OriginalImage.Clone() as Bitmap;
            DisplayImage = OriginalImage.Clone() as Bitmap;
            DisplayGraphics = Graphics.FromImage(DisplayImage);
            picCropped.Image = DisplayImage;
        }

        // Save the current file.
        private void mnuFileSave_Click(object sender, EventArgs e)
        {
            if (sfdPicture.ShowDialog() == DialogResult.OK)
            {
                SaveBitmapUsingExtension(CroppedImage, sfdPicture.FileName);
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

        // Load the image into a Bitmap, clone it, and
        // set the PictureBox's Image property to the Bitmap.
        private Bitmap LoadBitmapUnlocked(string file_name)
        {
            using (Bitmap bm = new Bitmap(file_name))
            {
                Bitmap new_bitmap = new Bitmap(bm.Width, bm.Height);
                using (Graphics gr = Graphics.FromImage(new_bitmap))
                {
                    gr.DrawImage(bm, 0, 0);
                }
                return new_bitmap;
            }
        }
    }
}
