﻿using System;
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

namespace vcs_RotatePicture6
{
    public partial class Form1 : Form
    {
        string filename = @"C:\_git\vcs\_1.data\______test_files1\elephant.jpg";

        // The original image.
        private Bitmap OriginalBitmap;

        // The rotated image.
        private Bitmap RotatedBitmap;

        // The center of the bitmap.
        private PointF ImageCenter;

        // The current angle of rotation during a drag.
        private float CurrentAngle = 0;

        // The total angle rotated so far in previous drags.
        private float TotalAngle = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // Start with no rotation.
            CurrentAngle = 0;
            TotalAngle = 0;

            // Load the bitmap.
            Bitmap bm = new Bitmap(filename);
            pictureBox1.Image = OriginalBitmap;
            pictureBox1.Visible = true;

            // See how big the rotated bitmap must be.
            int wid = (int)Math.Sqrt(bm.Width * bm.Width + bm.Height * bm.Height);

            // Make the original unrotated bitmap.
            OriginalBitmap = new Bitmap(wid, wid);

            // Save the center of the image for calculating rotation angles.
            ImageCenter = new PointF(wid / 2f, wid / 2f);

            // Copy the image into the middle of the bitmap.
            using (Graphics gr = Graphics.FromImage(OriginalBitmap))
            {
                // Clear with the color in the image's upper left corner.
                gr.Clear(bm.GetPixel(0, 0));

                //// For debugging. (Easier to see the background.)
                //gr.Clear(Color.LightBlue);

                // Draw the image centered.
                gr.DrawImage(bm, (wid - bm.Width) / 2, (wid - bm.Height) / 2);
            }

            // Display the original image.
            pictureBox1.Image = OriginalBitmap;

            // Size the form to fit.
            SizeForm();
        }

        // Let the user click and drag to rotate.
        private float StartAngle;
        private bool DragInProgress = false;
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            // Do nothing if there's no image loaded.
            if (OriginalBitmap == null) return;
            DragInProgress = true;

            // Get the initial angle from horizontal to the
            // vector between the center and the drag start point.
            //float dx = e.X - (pictureBox1.ClientSize.Width / 2f);
            //float dy = e.Y - (pictureBox1.ClientSize.Height / 2f);
            float dx = e.X - ImageCenter.X;
            float dy = e.Y - ImageCenter.Y;
            StartAngle = (float)Math.Atan2(dy, dx);
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            // Do nothing if there's no drag in progress.
            if (!DragInProgress) return;

            // Get the angle from horizontal to the
            // vector between the center and the current point.
            //float dx = e.X - (pictureBox1.ClientSize.Width / 2f);
            //float dy = e.Y - (pictureBox1.ClientSize.Height / 2f);
            float dx = e.X - ImageCenter.X;
            float dy = e.Y - ImageCenter.Y;
            float new_angle = (float)Math.Atan2(dy, dx);

            // Calculate the change in angle.
            CurrentAngle = new_angle - StartAngle;

            // Convert to degrees.
            CurrentAngle *= 180 / (float)Math.PI;

            // Add to the previous total angle rotated.
            CurrentAngle += TotalAngle;
            txtAngle.Text = CurrentAngle.ToString("0.00") + "°";

            // Rotate the original image to make the result bitmap.
            RotatedBitmap = RotateBitmap(OriginalBitmap, CurrentAngle);

            // Display the result.
            pictureBox1.Image = RotatedBitmap;
            pictureBox1.Refresh();
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            DragInProgress = false;

            // Save the new total angle of rotation.
            TotalAngle = CurrentAngle;
        }

        // Save the file with the appropriate format.
        // Throw a NotSupportedException if the file
        // has an unknown extension.
        public void SaveBitmapUsingExtension(Bitmap bm,
            string filename)
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

        // Return a bitmap rotated around its center.
        private Bitmap RotateBitmap(Bitmap bm, float angle)
        {
            // Make a bitmap to hold the rotated result.
            Bitmap result = new Bitmap(bm.Width, bm.Height);

            // Create the real rotation transformation.
            Matrix rotate_at_center = new Matrix();
            rotate_at_center.RotateAt(angle,
                new PointF(bm.Width / 2f, bm.Height / 2f));

            // Draw the image onto the new bitmap rotated.
            using (Graphics gr = Graphics.FromImage(result))
            {
                // Use smooth image interpolation.
                gr.InterpolationMode = InterpolationMode.High;

                // Clear with the color in the image's upper left corner.
                gr.Clear(OriginalBitmap.GetPixel(0, 0));

                //// For debugging. (Makes it easier to see the background.)
                //gr.Clear(Color.LightBlue);

                // Set up the transformation to rotate.
                gr.Transform = rotate_at_center;

                // Draw the image centered on the bitmap.
                gr.DrawImage(bm, 0, 0);
            }

            // Return the result bitmap.
            return result;
        }

        // Find the bounding rectangle for an array of points.
        private void GetPointBounds(PointF[] points, out float xmin, out float xmax, out float ymin, out float ymax)
        {
            xmin = points[0].X;
            xmax = xmin;
            ymin = points[0].Y;
            ymax = ymin;
            foreach (PointF point in points)
            {
                if (xmin > point.X) xmin = point.X;
                if (xmax < point.X) xmax = point.X;
                if (ymin > point.Y) ymin = point.Y;
                if (ymax < point.Y) ymax = point.Y;
            }
        }

        // Make sure the form is big enough to show the rotated image.
        private void SizeForm()
        {
            int wid = pictureBox1.Right + pictureBox1.Left;
            int hgt = pictureBox1.Bottom + pictureBox1.Left;
            if (wid > 900) wid = 900;
            if (hgt > 600) hgt = 600;
            this.ClientSize = new Size(
                Math.Max(wid, this.ClientSize.Width),
                Math.Max(hgt, this.ClientSize.Height));
        }

    }
}

//另存新檔
//SaveBitmapUsingExtension(RotatedBitmap, sfdFile.FileName);