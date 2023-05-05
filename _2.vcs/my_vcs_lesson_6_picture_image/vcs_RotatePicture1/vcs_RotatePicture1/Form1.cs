using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat
using System.Drawing.Drawing2D;

namespace vcs_RotatePicture1
{
    public partial class Form1 : Form
    {
        string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";

        private Bitmap bitmap1 = null;  //原圖
        private Bitmap bitmap2 = null;  //旋轉過的圖

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            //Image loadedImage = Image.FromFile(filename);
            //pictureBox1.Image = loadedImage;
            //pictureBox1.Size = new Size(

            bitmap1 = new Bitmap(filename);
            pictureBox1.Image = bitmap1;
            pictureBox1.Visible = true;

            pictureBox1.Size = new Size(bitmap1.Width + 20, bitmap1.Height + 20);
            //this.Size = new Size(bitmap1.Width + 250, bitmap1.Height + 250);


            //width = pictureBox1.Image.Width;
            //height = pictureBox1.Image.Height;
            //pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            //pictureBox1.Size = new Size(width, height);
        }

        // Return a bitmap rotated around its center.
        private Bitmap RotateBitmap(Bitmap bm, float angle)
        {
            // Make a Matrix to represent rotation by this angle.
            Matrix matrix1 = new Matrix();
            matrix1.Rotate(angle);

            // Rotate the image's corners to see how big
            // it will be after rotation.
            PointF[] points =
            {
                new PointF(0, 0),
                new PointF(bm.Width, 0),
                new PointF(bm.Width, bm.Height),
                new PointF(0, bm.Height),
            };
            matrix1.TransformPoints(points);
            float xmin, xmax, ymin, ymax;
            GetPointBounds(points, out xmin, out xmax, out ymin, out ymax);

            // Make a bitmap to hold the rotated result.
            int W = (int)Math.Round(xmax - xmin);
            int H = (int)Math.Round(ymax - ymin);
            Bitmap result = new Bitmap(W, H);

            // Create the real rotation transformation.
            Matrix matrix2 = new Matrix();
            matrix2.RotateAt(angle, new PointF(W / 2f, H / 2f));

            // Draw the image onto the new bitmap rotated.
            using (Graphics gr = Graphics.FromImage(result))
            {
                // Use smooth image interpolation.
                gr.InterpolationMode = InterpolationMode.High;

                // Clear with the color in the image's upper left corner.
                gr.Clear(bm.GetPixel(0, 0));

                //// For debugging. (Makes it easier to see the background.)
                //gr.Clear(Color.LightBlue);

                // Set up the transformation to rotate.
                gr.Transform = matrix2;

                // Draw the image centered on the bitmap.
                int x = (W - bm.Width) / 2;
                int y = (H - bm.Height) / 2;
                gr.DrawImage(bm, x, y);
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
            int W = pictureBox1.Right + pictureBox1.Left;
            int H = pictureBox1.Bottom + pictureBox1.Left;
            this.ClientSize = new Size(Math.Max(W, this.ClientSize.Width), Math.Max(H, this.ClientSize.Height));
        }

        float angle = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            angle += 15;

            this.Text = (angle % 360).ToString() + " 度";

            // Rotate.
            bitmap2 = RotateBitmap(bitmap1, angle);

            // Display the result.
            pictureBox1.Image = bitmap2;

            // Size the form to fit.
            SizeForm();
        }
    }
}
