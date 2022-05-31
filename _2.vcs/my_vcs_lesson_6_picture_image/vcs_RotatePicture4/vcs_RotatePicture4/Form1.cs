using System;
using System.Drawing;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;
using System.Drawing.Drawing2D;

namespace vcs_RotatePicture4
{
    public partial class Form1 : Form
    {
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
            string filename = @"C:\______test_files\picture1.jpg";

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

            // Enable Save As.
            mnuFileSaveAs.Enabled = true;


        }

        // Load an image file.
        private void mnuFileOpen_Click(object sender, EventArgs e)
        {
            if (ofdFile.ShowDialog() == DialogResult.OK)
            {
                // Start with no rotation.
                CurrentAngle = 0;
                TotalAngle = 0;

                // Load the bitmap.
                Bitmap bm = new Bitmap(ofdFile.FileName);
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

                // Enable Save As.
                mnuFileSaveAs.Enabled = true;
            }
        }

        private void mnuFileSaveAs_Click(object sender, EventArgs e)
        {
            //自動檔名 與 存檔語法
            string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

            try
            {
                //bitmap1.Save(@file1, ImageFormat.Jpeg);
                RotatedBitmap.Save(filename, ImageFormat.Bmp);
                //bitmap1.Save(@file3, ImageFormat.Png);

                //richTextBox1.Text += "已存檔 : " + file1 + "\n";
                //richTextBox1.Text += "已存檔 : " + filename + "\n";
                //richTextBox1.Text += "已存檔 : " + file3 + "\n";
            }
            catch (Exception ex)
            {
                //richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }

        }

        private void mnuFileExit_Click(object sender, EventArgs e)
        {
            Close();
        }

        // Return a bitmap rotated around its center.
        private Bitmap RotateBitmap(Bitmap bm, float angle)
        {
            // Make a bitmap to hold the rotated result.
            Bitmap result = new Bitmap(bm.Width, bm.Height);

            // Create the real rotation transformation.
            Matrix rotate_at_center = new Matrix();
            rotate_at_center.RotateAt(angle, new PointF(bm.Width / 2f, bm.Height / 2f));

            // Draw the image onto the new bitmap rotated.
            using (Graphics g = Graphics.FromImage(result))
            {
                // Use smooth image interpolation.
                g.InterpolationMode = InterpolationMode.High;

                // Clear with the color in the image's upper left corner.
                g.Clear(OriginalBitmap.GetPixel(0, 0));

                //// For debugging. (Makes it easier to see the background.)
                //gr.Clear(Color.LightBlue);

                // Set up the transformation to rotate.
                g.Transform = rotate_at_center;

                // Draw the image centered on the bitmap.
                g.DrawImage(bm, 0, 0);
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

        // Let the user click and drag to rotate.
        private float StartAngle;
        private bool DragInProgress = false;
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            // Do nothing if there's no image loaded.
            if (OriginalBitmap == null)
            {
                return;
            }
            DragInProgress = true;

            // Get the initial angle from horizontal to the
            // vector between the center and the drag start point.
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
    }
}

