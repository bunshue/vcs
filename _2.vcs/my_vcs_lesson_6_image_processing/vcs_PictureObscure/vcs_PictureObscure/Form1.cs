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

namespace vcs_PictureObscure
{
    public partial class Form1 : Form
    {
        string filename = @"C:\_git\vcs\_1.data\______test_files1\elephant.jpg";

        // The original image.
        private Bitmap OriginalImage = null;

        // The image all fuzzy.
        private Bitmap ObscuredImage = null;

        // The current modified image.
        private Bitmap VisibleImage = null;

        // The style we should use.
        private string FuzzStyle = "Pixelated";

        // The filter.
        private Bitmap32.Filter Filter;

        // The kernel size.
        private int KernelSize = 3;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            try
            {
                // Load the image without locking its file.
                OriginalImage = LoadBitmapUnlocked(filename);
            }
            catch (Exception ex)
            {
                OriginalImage = null;
                pictureBox1.Visible = false;
                MessageBox.Show("Error opening file " + filename + "\n" + ex.Message);
                return;
            }

            // Make the fuzzy version of the image.
            MakeFuzzyImage();

            // Display the current image.
            VisibleImage = new Bitmap(OriginalImage);
            pictureBox1.Image = VisibleImage;
            pictureBox1.Refresh();
        }

        // Load a bitmap without locking it.
        private Bitmap LoadBitmapUnlocked(string file_name)
        {
            using (Bitmap bm = new Bitmap(file_name))
            {
                return new Bitmap(bm);
            }
        }

        // The rectangle being selected.
        private Point Point1, Point2;
        private bool Selecting = false;

        // Start selecting.
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            Selecting = true;
            Point1 = e.Location;
            Point2 = e.Location;
        }

        // Continue selecting.
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            Point2 = e.Location;
            pictureBox1.Refresh();
        }

        // Finish selecting.
        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            Selecting = false;
            FuzzImagePart();
        }

        // Draw the selection rectangle.
        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            if (!Selecting) return;
            Rectangle rect = new Rectangle(
                (int)Math.Min(Point1.X, Point2.X),
                (int)Math.Min(Point1.Y, Point2.Y),
                (int)Math.Abs(Point1.X - Point2.X),
                (int)Math.Abs(Point1.Y - Point2.Y));
            e.Graphics.DrawRectangle(Pens.Yellow, rect);
            using (Pen pen = new Pen(Color.Red))
            {
                pen.DashStyle = DashStyle.Custom;
                pen.DashPattern = new float[] { 5, 5 };
                e.Graphics.DrawRectangle(pen, rect);
            }
        }

        // Make part of the image fuzzy.
        private void FuzzImagePart()
        {
            // Copy the selected part of the image from the fuzzy image.
            using (Graphics gr = Graphics.FromImage(VisibleImage))
            {
                Rectangle rect = new Rectangle(
                    (int)Math.Min(Point1.X, Point2.X),
                    (int)Math.Min(Point1.Y, Point2.Y),
                    (int)Math.Abs(Point1.X - Point2.X),
                    (int)Math.Abs(Point1.Y - Point2.Y));
                if (FuzzStyle == "Redacted")
                    gr.FillRectangle(Brushes.Black, rect);
                else
                    gr.DrawImage(ObscuredImage, rect, rect, GraphicsUnit.Pixel);
                pictureBox1.Refresh();
            }
        }
        
        // Make the fuzzy version of the image.
        private void MakeFuzzyImage()
        {
            Cursor = Cursors.WaitCursor;
            Refresh();

            if (FuzzStyle == "Fuzzy")
            {
                FuzzImage();
            }
            else if (FuzzStyle == "Pixelated")
            {
                PixelateImage();
            }
            else if (FuzzStyle == "Redacted")
            {
            }
            else
            {
                MessageBox.Show("Unknown style " + FuzzStyle);
            }

            Cursor = Cursors.Default;
        }

        // Make a pixelated copy of the image.
        private void PixelateImage()
        {
            if (OriginalImage == null) return;

            try
            {
                // Make a Bitmap32 object.
                ObscuredImage = new Bitmap(OriginalImage);
                Bitmap32 bm32 = new Bitmap32(ObscuredImage);

                // Pixellate.
                bm32.Pixellate(KernelSize, false);
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error pixelating image\n" + ex.Message);
            }
        }

        // Make a fuzzy copy of the image.
        private void FuzzImage()
        {
            if (OriginalImage == null) return;

            // Make a low pass filter.
            try
            {
                Filter = new Bitmap32.Filter();
                Filter.Offset = 0;
                Filter.Kernel = new float[KernelSize, KernelSize];
                for (int i = 0; i < KernelSize; i++)
                    for (int j = 0; j < KernelSize; j++)
                        Filter.Kernel[i, j] = 1;
                Filter.Normalize();
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error making filter\n" + ex.Message);
            }

            // Apply the filter.
            try
            {
                Bitmap bm = new Bitmap(OriginalImage);

                // Make a Bitmap24 object.
                Bitmap32 bm32 = new Bitmap32(bm);

                // Apply the filter.
                Bitmap32 new_bm32 = bm32.ApplyFilter(Filter, false);

                // Save the result.
                ObscuredImage = new_bm32.Bitmap;
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error applying filter\n" + ex.Message);
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //Revert
            // Revert to the original image.
            VisibleImage = new Bitmap(OriginalImage);
            pictureBox1.Image = VisibleImage;

        }

        private void button4_Click(object sender, EventArgs e)
        {
            //Parameter
            ParametersForm dlg = new ParametersForm();
            dlg.KernelSize = KernelSize;
            dlg.lblKernelSize.Text = KernelSize.ToString();
            dlg.cboStyle.Text = FuzzStyle;
            if (dlg.ShowDialog() == DialogResult.OK)
            {
                KernelSize = dlg.KernelSize;
                FuzzStyle = dlg.cboStyle.Text;

                // Make the fuzzy version of the image.
                MakeFuzzyImage();
            }

        }

    }
}
