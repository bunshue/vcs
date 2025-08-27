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
        private Bitmap bitmap1 = null;  //背景bitmap
        private Bitmap bitmap2 = null;  //要疊合的bitmap
        private Bitmap bitmap12 = null; //疊合後的bitmap
        private Point OverlayLocation = new Point(0, 0);    //疊合的位置

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            DoubleBuffered = true;  // Reduce flicker.


        }

        //開啟底圖
        private void button1_Click(object sender, EventArgs e)
        {
            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";

            bitmap1 = new Bitmap(filename1);
            pictureBox1.Image = bitmap1;
        }

        //選擇貼上圖片
        private void button2_Click(object sender, EventArgs e)
        {
            string filename2 = @"D:\_git\vcs\_1.data\______test_files1\_material\ims-small-logo.png";

            bitmap2 = new Bitmap(filename2);
            pictureBox1.Cursor = Cursors.Cross;

            // Display the combined image.
            ShowCombinedImage();
        }

        // Display the combined image.
        private void ShowCombinedImage()
        {
            // If there's no background image, do nothing.
            if (bitmap1 == null)
            {
                return;
            }

            // Copy the background.
            bitmap12 = new Bitmap(bitmap1);

            // Add the overlay.
            if (bitmap2 != null)
            {
                using (Graphics gr = Graphics.FromImage(bitmap12))
                {
                    gr.DrawImage(bitmap2, OverlayLocation);
                }
            }

            // Display the result.
            pictureBox1.Image = bitmap12;
        }

        // Drag the overlay image.
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (bitmap2 == null)
            {
                return;
            }
            OverlayLocation = new Point(e.X - bitmap2.Width / 2, e.Y - bitmap2.Height / 2);
            ShowCombinedImage();
        }

        // Finish dragging the overlay image.
        private void pictureBox1_MouseClick(object sender, MouseEventArgs e)
        {
            if (bitmap2 == null)
            {
                return;
            }
            bitmap2 = null;
            pictureBox1.Cursor = Cursors.Default;

            // Make the overlay permanent.
            bitmap1 = bitmap12;
        }
    }
}
