using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_DragPicture6
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The smiley image.
        private Bitmap Smiley;

        // The smiley image's location.
        private Rectangle SmileyLocation;

        private void Form1_Load(object sender, EventArgs e)
        {
            // Make the white pixels in the smiley transparent.
            Smiley = new Bitmap(Properties.Resources.smile);
            Smiley.MakeTransparent(Color.White);

            // Set the smiley's initial location.
            SmileyLocation = new Rectangle(10, 10,
                Smiley.Width, Smiley.Height);
        }

        // Draw the picture over the background.
        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.DrawImage(Smiley, SmileyLocation);
        }

        // True when we are dragging.
        private bool Dragging = false;

        // The offset from the mouse's down position
        // and the picture's upper left corner.
        private int OffsetX, OffsetY;

        // Start dragging the picture.
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            // See if we're over the picture.
            if (PointIsOverPicture(e.X, e.Y))
            {
                // Start dragging.
                Dragging = true;

                // Save the offset from the mouse to the picture's origin.
                OffsetX = SmileyLocation.X - e.X;
                OffsetY = SmileyLocation.Y - e.Y;
            }
        }

        // Continue dragging the picture.
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            // See if we're dragging.
            if (Dragging)
            {
                // We're dragging the image. Move it.
                SmileyLocation.X = e.X + OffsetX;
                SmileyLocation.Y = e.Y + OffsetY;

                // Redraw.
                pictureBox1.Invalidate();
            }
            else
            {
                // We're not dragging the image. See if we're over it.
                Cursor new_cursor = Cursors.Default;
                if (PointIsOverPicture(e.X, e.Y))
                {
                    new_cursor = Cursors.Hand;
                }
                if (pictureBox1.Cursor != new_cursor)
                    pictureBox1.Cursor = new_cursor;
            }
        }

        // Stop dragging the picture.
        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            Dragging = false;
        }

        // Return true if the point is over the picture's current location.
        private bool PointIsOverPicture(int x, int y)
        {
            // See if it's over the picture's bounding rectangle.
            if ((x < SmileyLocation.Left) || (x >= SmileyLocation.Right) ||
                (y < SmileyLocation.Top) || (y >= SmileyLocation.Bottom))
                return false;

            // See if the point is above a non-transparent pixel.
            int i = x - SmileyLocation.X;
            int j = y - SmileyLocation.Y;
            return (Smiley.GetPixel(i, j).A > 0);
        }
    }
}
