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

namespace vcs_PictureOverlay
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
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

        //開啟底圖
        private void button1_Click(object sender, EventArgs e)
        {
            if (ofdFile.ShowDialog() == DialogResult.OK)
            {
                try
                {
                    // Open the file.
                    BackgroundBitmap = new Bitmap(ofdFile.FileName);
                    pictureBox1.Image = BackgroundBitmap;
                    pictureBox1.Visible = true;
                    ClientSize = new Size(pictureBox1.Right + pictureBox1.Left, pictureBox1.Bottom + pictureBox1.Left);
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Error opening file.\n" + ex.Message, "Open Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
        }

        //選擇貼上圖片
        private void button2_Click(object sender, EventArgs e)
        {
            if (ofdFile.ShowDialog() == DialogResult.OK)
            {
                try
                {
                    // Open the file.
                    OverlayBitmap = new Bitmap(ofdFile.FileName);
                    pictureBox1.Cursor = Cursors.Cross;

                    // Display the combined image.
                    ShowCombinedImage();
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Error opening file.\n" + ex.Message, "Open Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
        }

        // Display the combined image.
        private void ShowCombinedImage()
        {
            // If there's no background image, do nothing.
            if (BackgroundBitmap == null)
            {
                return;
            }

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
            pictureBox1.Image = CombinedBitmap;
        }

        // Drag the overlay image.
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (OverlayBitmap == null)
            {
                return;
            }
            OverlayLocation = new Point(e.X - OverlayBitmap.Width / 2, e.Y - OverlayBitmap.Height / 2);
            ShowCombinedImage();
        }

        // Finish dragging the overlay image.
        private void pictureBox1_MouseClick(object sender, MouseEventArgs e)
        {
            if (OverlayBitmap == null)
            {
                return;
            }
            OverlayBitmap = null;
            pictureBox1.Cursor = Cursors.Default;

            // Make the overlay permanent.
            BackgroundBitmap = CombinedBitmap;
        }

    }
}
