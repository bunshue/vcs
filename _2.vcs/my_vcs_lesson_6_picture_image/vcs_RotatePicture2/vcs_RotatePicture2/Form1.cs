using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;
using System.IO;
using System.Drawing.Imaging;


namespace vcs_RotatePicture2
{
    public partial class Form1 : Form
    {
        // The current scale.
        private float ImageScale = 1;
        private float angle = 0;

        // The original and rotated bitmaps.
        private Bitmap OriginalImage = null, RotatedImage = null;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";

            using (Bitmap bm = new Bitmap(filename))
            {
                OriginalImage = new Bitmap(bm);
                //mnuFileSaveAs.Enabled = true;
            }

            DisplayImage();

        }

        // Display the image at the current rotation and scale.
        private void DisplayImage()
        {
            if (OriginalImage == null)
                return;
            RotatedImage = null;
            pictureBox1.Visible = false;

            // Find the size of the image's rotated bounding box.
            Matrix rotation = new Matrix();
            rotation.Rotate(angle);
            int old_wid = OriginalImage.Width;
            int old_hgt = OriginalImage.Height;
            PointF[] points =
            {
                new PointF(0, 0),
                new PointF(old_wid, 0),
                new PointF(0, old_hgt),
                new PointF(old_wid, old_hgt),
            };
            rotation.TransformPoints(points);
            float[] xs = { points[0].X, points[1].X, points[2].X, points[3].X };
            float[] ys = { points[0].Y, points[1].Y, points[2].Y, points[3].Y };
            int new_wid = (int)(xs.Max() - xs.Min());
            int new_hgt = (int)(ys.Max() - ys.Min());

            // Make the rotated image.
            RotatedImage = new Bitmap(new_wid, new_hgt);
            using (Graphics gr = Graphics.FromImage(RotatedImage))
            {
                gr.TranslateTransform(-old_wid / 2, -old_hgt / 2,
                    MatrixOrder.Append);
                gr.RotateTransform(angle, MatrixOrder.Append);
                gr.TranslateTransform(new_wid / 2, new_hgt / 2,
                    MatrixOrder.Append);
                RectangleF source_rect = new RectangleF(0, 0,
                    OriginalImage.Width, OriginalImage.Height);
                PointF[] dest_points =
                {
                    new PointF(0, 0),
                    new PointF(OriginalImage.Width, 0),
                    new PointF(0, OriginalImage.Height),
                };
                gr.DrawImage(OriginalImage, dest_points, source_rect, GraphicsUnit.Pixel);

                // Uncomment to draw a red box around the image.
                //using (Pen pen = new Pen(Color.Red, 10))
                //{
                //    gr.DrawRectangle(pen, 0, 0,
                //        OriginalImage.Width - 1,
                //        OriginalImage.Height - 1);
                //}
            }

            // Scale the output PictureBox.
            SetPictureBoxSize();

            // Display the result.
            pictureBox1.Image = RotatedImage;
            pictureBox1.Visible = true;
        }





        // Set the PictureBox to display the image
        // at the desired scale.
        private void SetPictureBoxSize()
        {
            if (RotatedImage == null)
                return;
            pictureBox1.ClientSize = new Size((int)(RotatedImage.Width * ImageScale), (int)(RotatedImage.Height * ImageScale));
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            angle += 5;
            ImageScale += 0.01f;
            this.Text = (angle % 360).ToString() + " 度, " + ImageScale.ToString() + " 倍";
            DisplayImage();
            if (((angle % 360) == 0) && (ImageScale >= 1.7))
                timer1.Enabled = false;

        }


    }
}
