using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;
using System.IO;

namespace vcs_ImageProcessing3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Display the initial image.
        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox2.Image = pictureBox1.Image.Clone() as Image;
        }

        // Display the original image.
        private void btnReset_Click(object sender, EventArgs e)
        {
            pictureBox2.Image = pictureBox1.Image.Clone() as Image;
            lblElapsed.Text = "";
        }

        // Apply a filter.
        private void ApplyFilter(Bitmap32.Filter filter)
        {
            Bitmap bm = new Bitmap(pictureBox2.Image);
            this.Cursor = Cursors.WaitCursor;
            DateTime start_time = DateTime.Now;

            // Make a Bitmap24 object.
            Bitmap32 bm32 = new Bitmap32(bm);

            // Apply the filter.
            Bitmap32 new_bm32 = bm32.ApplyFilter(filter, false);

            // Display the result.
            pictureBox2.Image = new_bm32.Bitmap;

            DateTime stop_time = DateTime.Now;
            this.Cursor = Cursors.Default;

            TimeSpan elapsed_time = stop_time - start_time;
            lblElapsed.Text = elapsed_time.TotalSeconds.ToString("0.000000");
        }

        // Apply an embossing filter.
        private void btnEmboss1_Click(object sender, EventArgs e)
        {
            ApplyFilter(Bitmap32.EmbossingFilter);
        }

        // Apply an embossing filter.
        private void btnEmboss2_Click(object sender, EventArgs e)
        {
            ApplyFilter(Bitmap32.EmbossingFilter2);
        }

        // Apply an embossing filter.
        private void btnEmboss3_Click(object sender, EventArgs e)
        {
            ApplyFilter(Bitmap32.EmbossingFilter3);
        }

        // Apply a 5x5 Gaussian blurring filter.
        private void btnBlur1_Click(object sender, EventArgs e)
        {
            ApplyFilter(Bitmap32.BlurFilter5x5Gaussian);
        }

        // Apply a 5x5 mean blurring filter.
        private void btnBlur2_Click(object sender, EventArgs e)
        {
            ApplyFilter(Bitmap32.BlurFilter5x5Mean);
        }

        // Apply a high-pass filter.
        private void btnHighPass1_Click(object sender, EventArgs e)
        {
            ApplyFilter(Bitmap32.HighPassFilter3x3);
        }

        // Apply a high-pass filter.
        private void btnHighPass2_Click(object sender, EventArgs e)
        {
            ApplyFilter(Bitmap32.HighPassFilter5x5);
        }

        // Apply an edge-detecting filter.
        private void btnEdge1_Click(object sender, EventArgs e)
        {
            ApplyFilter(Bitmap32.EdgeDetectionFilterULtoLR);
        }

        // Apply an edge-detecting filter.
        private void btnEdge2_Click(object sender, EventArgs e)
        {
            ApplyFilter(Bitmap32.EdgeDetectionFilterTopToBottom);
        }

        // Apply an edge-detecting filter.
        private void btnEdge3_Click(object sender, EventArgs e)
        {
            ApplyFilter(Bitmap32.EdgeDetectionFilterLeftToRight);
        }

        // Average the colors.
        private void btnAverage_Click(object sender, EventArgs e)
        {
            Bitmap bm = new Bitmap(pictureBox2.Image);
            this.Cursor = Cursors.WaitCursor;
            DateTime start_time = DateTime.Now;

            // Make a Bitmap24 object.
            Bitmap32 bm32 = new Bitmap32(bm);

            // Average the colors.
            bm32.Average();

            // Display the result.
            pictureBox2.Image = bm;

            DateTime stop_time = DateTime.Now;
            this.Cursor = Cursors.Default;

            TimeSpan elapsed_time = stop_time - start_time;
            lblElapsed.Text = elapsed_time.TotalSeconds.ToString("0.000000");
        }

        // Convert to grayscale.
        private void btnGrayscale_Click(object sender, EventArgs e)
        {
            Bitmap bm = new Bitmap(pictureBox2.Image);
            this.Cursor = Cursors.WaitCursor;
            DateTime start_time = DateTime.Now;

            // Make a Bitmap24 object.
            Bitmap32 bm32 = new Bitmap32(bm);

            // Convert to grayscale.
            bm32.Grayscale();

            // Display the result.
            pictureBox2.Image = bm;

            DateTime stop_time = DateTime.Now;
            this.Cursor = Cursors.Default;

            TimeSpan elapsed_time = stop_time - start_time;
            lblElapsed.Text = elapsed_time.TotalSeconds.ToString("0.000000");
        }

        // Convert to a red scale.
        private void btnRed_Click(object sender, EventArgs e)
        {
            Bitmap bm = new Bitmap(pictureBox2.Image);
            this.Cursor = Cursors.WaitCursor;
            DateTime start_time = DateTime.Now;

            // Make a Bitmap24 object.
            Bitmap32 bm32 = new Bitmap32(bm);

            // Convert to red.
            bm32.ClearGreen();
            bm32.ClearBlue();

            // Display the result.
            pictureBox2.Image = bm;

            DateTime stop_time = DateTime.Now;
            this.Cursor = Cursors.Default;

            TimeSpan elapsed_time = stop_time - start_time;
            lblElapsed.Text = elapsed_time.TotalSeconds.ToString("0.000000");
        }

        // Convert to a green scale.
        private void btnGreen_Click(object sender, EventArgs e)
        {
            Bitmap bm = new Bitmap(pictureBox2.Image);
            this.Cursor = Cursors.WaitCursor;
            DateTime start_time = DateTime.Now;

            // Make a Bitmap24 object.
            Bitmap32 bm32 = new Bitmap32(bm);

            // Convert to green.
            bm32.ClearRed();
            bm32.ClearBlue();

            // Display the result.
            pictureBox2.Image = bm;

            DateTime stop_time = DateTime.Now;
            this.Cursor = Cursors.Default;

            TimeSpan elapsed_time = stop_time - start_time;
            lblElapsed.Text = elapsed_time.TotalSeconds.ToString("0.000000");
        }

        // Convert to a blue scale.
        private void btnBlue_Click(object sender, EventArgs e)
        {
            Bitmap bm = new Bitmap(pictureBox2.Image);
            this.Cursor = Cursors.WaitCursor;
            DateTime start_time = DateTime.Now;

            // Make a Bitmap24 object.
            Bitmap32 bm32 = new Bitmap32(bm);

            // Convert to blue.
            bm32.ClearRed();
            bm32.ClearGreen();

            // Display the result.
            pictureBox2.Image = bm;

            DateTime stop_time = DateTime.Now;
            this.Cursor = Cursors.Default;

            TimeSpan elapsed_time = stop_time - start_time;
            lblElapsed.Text = elapsed_time.TotalSeconds.ToString("0.000000");
        }

        // Invert the image.
        private void btnInvert_Click(object sender, EventArgs e)
        {
            Bitmap bm = new Bitmap(pictureBox2.Image);
            this.Cursor = Cursors.WaitCursor;
            DateTime start_time = DateTime.Now;

            // Make a Bitmap24 object.
            Bitmap32 bm32 = new Bitmap32(bm);

            // Convert to blue.
            bm32.Invert();

            // Display the result.
            pictureBox2.Image = bm;

            DateTime stop_time = DateTime.Now;
            this.Cursor = Cursors.Default;

            TimeSpan elapsed_time = stop_time - start_time;
            lblElapsed.Text = elapsed_time.TotalSeconds.ToString("0.000000");
        }

        // Pick the maximum brightness for pixels in areas.
        private void btnMaximum_Click(object sender, EventArgs e)
        {
            Bitmap bm = new Bitmap(pictureBox2.Image);
            this.Cursor = Cursors.WaitCursor;
            DateTime start_time = DateTime.Now;

            // Make a Bitmap24 object.
            Bitmap32 bm32 = new Bitmap32(bm);

            // Pick the maximum brightness colors.
            Bitmap32 new_bm32 = bm32.RankMaximum(int.Parse(txtRank.Text), false);

            // Display the result.
            pictureBox2.Image = new_bm32.Bitmap;

            DateTime stop_time = DateTime.Now;
            this.Cursor = Cursors.Default;

            TimeSpan elapsed_time = stop_time - start_time;
            lblElapsed.Text = elapsed_time.TotalSeconds.ToString("0.000000");
        }

        // Pick the minimum brightness for pixels in areas.
        private void btnMinimum_Click(object sender, EventArgs e)
        {
            Bitmap bm = new Bitmap(pictureBox2.Image);
            this.Cursor = Cursors.WaitCursor;
            DateTime start_time = DateTime.Now;

            // Make a Bitmap24 object.
            Bitmap32 bm32 = new Bitmap32(bm);

            // Pick the minimum brightness colors.
            Bitmap32 new_bm32 = bm32.RankMinimum(int.Parse(txtRank.Text), false);

            // Display the result.
            pictureBox2.Image = new_bm32.Bitmap;

            DateTime stop_time = DateTime.Now;
            this.Cursor = Cursors.Default;

            TimeSpan elapsed_time = stop_time - start_time;
            lblElapsed.Text = elapsed_time.TotalSeconds.ToString("0.000000");
        }

        // Pixellate the image.
        private void btnPixellate_Click(object sender, EventArgs e)
        {
            Bitmap bm = new Bitmap(pictureBox2.Image);
            this.Cursor = Cursors.WaitCursor;
            DateTime start_time = DateTime.Now;

            // Make a Bitmap24 object.
            Bitmap32 bm32 = new Bitmap32(bm);

            // Pixellate.
            bm32.Pixellate(int.Parse(txtRank.Text), false);

            // Display the result.
            pictureBox2.Image = bm;

            DateTime stop_time = DateTime.Now;
            this.Cursor = Cursors.Default;

            TimeSpan elapsed_time = stop_time - start_time;
            lblElapsed.Text = elapsed_time.TotalSeconds.ToString("0.000000");
        }

        private void mnuFileOpen_Click(object sender, EventArgs e)
        {
            if (ofdImage.ShowDialog() == DialogResult.OK)
            {
                pictureBox1.Image = new Bitmap(ofdImage.FileName);
                pictureBox2.Image = pictureBox1.Image.Clone() as Image;
                lblElapsed.Text = "";
            }
        }

        private void mnuFileSaveAs_Click(object sender, EventArgs e)
        {
            if (sfdImage.ShowDialog() == DialogResult.OK)
            {
                Bitmap bm = (Bitmap)pictureBox2.Image;
                SaveBitmapUsingExtension(bm, sfdImage.FileName);
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

        private void mnuFileExit_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        // Pointellate the image.
        private void btnPointellate_Click(object sender, EventArgs e)
        {
            Bitmap bm = new Bitmap(pictureBox2.Image);
            this.Cursor = Cursors.WaitCursor;
            DateTime start_time = DateTime.Now;

            // Make a Bitmap24 object.
            Bitmap32 bm32 = new Bitmap32(bm);

            // Pixellate.
            int rank = int.Parse(txtRank.Text);
            Bitmap new_bm = bm32.Pointellate(rank, rank, false);

            // Display the result.
            pictureBox2.Image = new_bm;

            DateTime stop_time = DateTime.Now;
            this.Cursor = Cursors.Default;

            TimeSpan elapsed_time = stop_time - start_time;
            lblElapsed.Text = elapsed_time.TotalSeconds.ToString("0.000000");
        }
    }
}
