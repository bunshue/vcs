using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for InterpolationMode

namespace vcs_DragPicture3b
{
    public partial class Form1 : Form
    {
        string filename = @"C:\_git\vcs\_1.data\______test_files1\very_long_pic.jpg";

        private Bitmap bitmap1;
        private float CurrentScale;
        private Bitmap VisibleImage = null;
        private Graphics VisibleGraphics = null;

        // Upper left corner of the image in the PictureBox.
        private int PicX = 0, PicY = 0;

        public Form1()
        {
            InitializeComponent();
        }

        // Initially display at full scale.
        private void Form1_Load(object sender, EventArgs e)
        {
            // Use a grabbing hand cursor.
            pictureBox1.Cursor = new Cursor("hand2.cur");

            // Get the map image.
            //bitmap1 = Properties.Resources.Map;
            bitmap1 = (Bitmap)Image.FromFile(filename);

            richTextBox1.Text += "W = " + bitmap1.Width.ToString() + ", H = " + bitmap1.Height.ToString() + "\n";

            richTextBox1.Text += "pic_W = " + pictureBox1.Width.ToString() + ", pic_H = " + pictureBox1.Height.ToString() + "\n";

            // Get ready to draw.
            PrepareGraphics();

            CurrentScale = 1;
            // Draw.
            DrawMap();
        }

        private void PrepareGraphics()
        {
            // Skip it if we've been minimized.
            if ((pictureBox1.ClientSize.Width == 0) ||
                (pictureBox1.ClientSize.Height == 0)) return;

            // Free old resources.
            if (VisibleGraphics != null)
            {
                pictureBox1.Image = null;
                VisibleGraphics.Dispose();
                VisibleImage.Dispose();
            }

            // Make the new Bitmap and Graphics.
            VisibleImage = new Bitmap(
                pictureBox1.ClientSize.Width,
                pictureBox1.ClientSize.Height);
            VisibleGraphics = Graphics.FromImage(VisibleImage);
            VisibleGraphics.InterpolationMode = InterpolationMode.High;

            // Display the Bitmap.
            pictureBox1.Image = VisibleImage;
        }

        // Set the PictureBox's position.
        private void SetOrigin()
        {
            // Keep x and y within bounds.
            float scaled_width = CurrentScale * bitmap1.Width;
            int xmin = (int)(pictureBox1.ClientSize.Width - scaled_width);
            if (xmin > 0) xmin = 0;
            if (PicX < xmin) PicX = xmin;
            else if (PicX > 0) PicX = 0;

            float scaled_height = CurrentScale * bitmap1.Height;
            int ymin = (int)(pictureBox1.ClientSize.Height - scaled_height);
            if (ymin > 0) ymin = 0;
            if (PicY < ymin) PicY = ymin;
            else if (PicY > 0) PicY = 0;
        }

        // Draw the image at the correct scale and location.
        private void DrawMap()
        {
            // Validate PicX and PicY.
            SetOrigin();

            // Get the destination area.
            float scaled_width = CurrentScale * bitmap1.Width;
            float scaled_height = CurrentScale * bitmap1.Height;
            PointF[] dest_points =
            {
                new PointF(PicX, PicY),
                new PointF(PicX + scaled_width, PicY),
                new PointF(PicX, PicY + scaled_height),
            };

            // Draw the whole image.
            RectangleF source_rect = new RectangleF(
                0, 0, bitmap1.Width, bitmap1.Height);

            // Draw.
            VisibleGraphics.Clear(pictureBox1.BackColor);
            VisibleGraphics.DrawImage(bitmap1,
                dest_points, source_rect, GraphicsUnit.Pixel);

            // Update the display.
            pictureBox1.Refresh();
        }

        // Let the user drag the image around.
        private bool Dragging = false;
        private int LastX, LastY;

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            LastX = e.X;
            LastY = e.Y;
            Dragging = true;
            richTextBox1.Text += "Down (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (!Dragging) return;

            PicX += e.X - LastX;
            PicY += e.Y - LastY;
            LastX = e.X;
            LastY = e.Y;

            DrawMap();
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            Dragging = false;
        }
    }
}

