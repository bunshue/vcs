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

namespace vcs_RotatePicture2
{
    public partial class Form1 : Form
    {
        // The current scale.
        private float angle = 0;

        string filename = @"C:\______test_files\picture1.jpg";
        private Bitmap bitmap1 = null;  //原圖
        private Bitmap bitmap2 = null;  //旋轉過的圖

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            using (Bitmap bm = new Bitmap(filename))
            {
                bitmap1 = new Bitmap(bm);
                //mnuFileSaveAs.Enabled = true;
            }
            DisplayImage();
        }

        // Display the image at the current rotation and scale.
        private void DisplayImage()
        {
            if (bitmap1 == null)
                return;
            bitmap2 = null;

            // Find the size of the image's rotated bounding box.
            Matrix matrix1 = new Matrix();
            matrix1.Rotate(angle);
            int W1 = bitmap1.Width;
            int H1 = bitmap1.Height;
            PointF[] points =
            {
                new PointF(0, 0),
                new PointF(W1, 0),
                new PointF(0, H1),
                new PointF(W1, H1),
            };
            matrix1.TransformPoints(points);
            float[] xs = { points[0].X, points[1].X, points[2].X, points[3].X };
            float[] ys = { points[0].Y, points[1].Y, points[2].Y, points[3].Y };
            int W2 = (int)(xs.Max() - xs.Min());
            int H2 = (int)(ys.Max() - ys.Min());

            // Make the rotated image.
            bitmap2 = new Bitmap(W2, H2);
            using (Graphics g = Graphics.FromImage(bitmap2))
            {
                g.TranslateTransform(-W1 / 2, -H1 / 2, MatrixOrder.Append);
                g.RotateTransform(angle, MatrixOrder.Append);
                g.TranslateTransform(W2 / 2, H2 / 2, MatrixOrder.Append);
                RectangleF source_rect = new RectangleF(0, 0, W1, H1);
                PointF[] dest_points =
                {
                    new PointF(0, 0),
                    new PointF(W1, 0),
                    new PointF(0, H1),
                };
                g.DrawImage(bitmap1, dest_points, source_rect, GraphicsUnit.Pixel);

                // Uncomment to draw a red box around the image.
                //using (Pen pen = new Pen(Color.Red, 10))
                //{
                //    gr.DrawRectangle(pen, 0, 0,
                //        W1 - 1,
                //        H1 - 1);
                //}
            }

            // Display the result.
            pictureBox1.Image = bitmap2;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            angle += 5;
            this.Text = (angle % 360).ToString() + " 度";
            DisplayImage();
            if ((angle % 360) == 0)
            {
                timer1.Enabled = false;
            }
        }
    }
}
