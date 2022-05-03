using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_PictureMagnify5
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Save the original image.
        private Bitmap OriginalImage, ShadedImage;
        private int SmallWidth, SmallHeight;
        private float ScaleX, ScaleY;
        private void Form1_Load(object sender, EventArgs e)
        {
            OriginalImage = picWhole.Image as Bitmap;
            picCloseup.Image = OriginalImage;
            picCloseup.SizeMode = PictureBoxSizeMode.AutoSize;

            // Make a shaded version of the image.
            ShadedImage = new Bitmap(OriginalImage);
            using (Graphics gr = Graphics.FromImage(ShadedImage))
            {
                using (Brush br = new SolidBrush(Color.FromArgb(128, 255, 255, 255)))
                {
                    Rectangle rect = new Rectangle(0, 0, ShadedImage.Width, ShadedImage.Height);
                    gr.FillRectangle(br, rect);
                }
            }

            // Get scale factors to map from big scale to small scale.
            ScaleX = (float)panCloseup.ClientSize.Width / OriginalImage.Width;
            ScaleY = (float)panCloseup.ClientSize.Height / OriginalImage.Height;

            // See how big the closeup is on the small scale.
            SmallWidth = (int)(ScaleX * picWhole.ClientSize.Width);
            SmallHeight = (int)(ScaleY * picWhole.ClientSize.Height);
        }

        // Go to the Astronomy Picture of the Day web site.
        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            System.Diagnostics.Process.Start("http://antwrp.gsfc.nasa.gov/apod/ap090628.html");
        }

        // Display a closeup of this area.
        private Rectangle ViewingRectangle;
        private void picWhole_MouseMove(object sender, MouseEventArgs e)
        {
            // Position picCloseup inside its parent Panel.
            float x = (float)e.X / picWhole.ClientSize.Width * OriginalImage.Width - (float)panCloseup.ClientSize.Width / 2;
            float y = (float)e.Y / picWhole.ClientSize.Height * OriginalImage.Height - (float)panCloseup.ClientSize.Height / 2;
            if (x < 0) x = 0;
            if (y < 0) y = 0;
            if (x > OriginalImage.Width - panCloseup.ClientSize.Width)
                x = OriginalImage.Width - panCloseup.ClientSize.Width;
            if (y > OriginalImage.Height - panCloseup.ClientSize.Height)
                y = OriginalImage.Height - panCloseup.ClientSize.Height;
            picCloseup.Location = new Point(-(int)x, -(int)y);

            // Record the position we are viewing.
            ViewingRectangle = new Rectangle((int)x, (int)y,
                panCloseup.ClientSize.Width, 
                panCloseup.ClientSize.Height);

            // Draw the closeup area.
            picWhole.Invalidate();
        }

        // Draw the viewing area.
        private void picWhole_Paint(object sender, PaintEventArgs e)
        {
            // Scale so we can draw in the full scale coordinates.
            e.Graphics.ScaleTransform(ScaleX, ScaleY);

            // Draw the viewing area using the original image.
            e.Graphics.DrawImage(OriginalImage, ViewingRectangle, 
                ViewingRectangle, GraphicsUnit.Pixel);
            //e.Graphics.DrawRectangle(Pens.Red, ViewingRectangle);
        }

        // Use the shaded background image.
        private void picWhole_MouseEnter(object sender, EventArgs e)
        {
            picWhole.Image = ShadedImage;
            panCloseup.Visible = true;
        }

        // Use the regular image.
        private void picWhole_MouseLeave(object sender, EventArgs e)
        {
            picWhole.Image = OriginalImage;
            panCloseup.Visible = false;
        }
    }
}
