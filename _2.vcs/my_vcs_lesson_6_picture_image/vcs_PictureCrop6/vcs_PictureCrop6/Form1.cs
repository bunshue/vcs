using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_PictureCrop6
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private Bitmap OriginalImage = null;
        private int X0, Y0, X1, Y1;
        private bool SelectingArea = false;
        private Bitmap SelectedImage = null;
        private Graphics SelectedGraphics = null;
        private Rectangle SelectedRect;
        private bool MadeSelection = false;

        // Save the original image.
        private void Form1_Load(object sender, EventArgs e)
        {
            //讀取圖檔
            string filename = @"C:\______test_files\picture1.jpg";
            pictureBox1.Image = Image.FromFile(filename);

            OriginalImage = new Bitmap(pictureBox1.Image);

            this.KeyPreview = true;
        }

        // Start selecting an area.
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            // Save the starting point.
            SelectingArea = true;
            X0 = e.X;
            Y0 = e.Y;

            // Make the selected image.
            SelectedImage = new Bitmap(OriginalImage);
            SelectedGraphics = Graphics.FromImage(SelectedImage);
            pictureBox1.Image = SelectedImage;
        }

        // Continue selecting an area.
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            // Do nothing if we're not selecting an area.
            if (!SelectingArea) return;

            // Generate the new image with the selection rectangle.
            X1 = e.X;
            Y1 = e.Y;

            // Copy the original image.
            SelectedGraphics.DrawImage(OriginalImage, 0, 0);

            // Draw the selection rectangle.
            using (Pen select_pen = new Pen(Color.Red))
            {
                select_pen.DashStyle = System.Drawing.Drawing2D.DashStyle.Dash;
                Rectangle rect = MakeRectangle(X0, Y0, X1, Y1);
                SelectedGraphics.DrawRectangle(select_pen, rect);
            }

            pictureBox1.Refresh();
        }

        // Finish selecting the area.
        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            // Do nothing if we're not selecting an area.
            if (!SelectingArea) return;
            SelectingArea = false;

            // Stop selecting.
            SelectedGraphics = null;

            // Convert the points into a Rectangle.
            SelectedRect = MakeRectangle(X0, Y0, X1, Y1);
            MadeSelection = (
                (SelectedRect.Width > 0) &&
                (SelectedRect.Height > 0));
        }

        // Return a Rectangle with these points as corners.
        private Rectangle MakeRectangle(int x0, int y0, int x1, int y1)
        {
            return new Rectangle(
                Math.Min(x0, x1),
                Math.Min(y0, y1),
                Math.Abs(x0 - x1),
                Math.Abs(y0 - y1));
        }

        // If the user presses Escape, cancel.
        private void Form1_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == 27)
            {
                if (!SelectingArea) return;
                SelectingArea = false;

                // Stop selecting.
                SelectedImage = null;
                SelectedGraphics = null;
                pictureBox1.Image = OriginalImage;
                pictureBox1.Refresh();

                // There is no selection.
                MadeSelection = false;
            }
        }

        // Copy the selected area to the clipboard.
        private void CopyToClipboard(Rectangle src_rect)
        {
            // Make a bitmap for the selected area's image.
            Bitmap bm = new Bitmap(src_rect.Width, src_rect.Height);

            // Copy the selected area into the bitmap.
            using (Graphics gr = Graphics.FromImage(bm))
            {
                Rectangle dest_rect = new Rectangle(0, 0, src_rect.Width, src_rect.Height);
                gr.DrawImage(OriginalImage, dest_rect, src_rect, GraphicsUnit.Pixel);
            }

            // Copy the selection image to the clipboard.
            Clipboard.SetImage(bm);
        }

        //複製
        // Copy the selected area to the clipboard.
        private void button1_Click(object sender, EventArgs e)
        {
            CopyToClipboard(SelectedRect);
        }

        //剪下
        // Copy the selected area to the clipboard
        // and blank that area.
        private void button2_Click(object sender, EventArgs e)
        {
            // Copy the selection to the clipboard.
            CopyToClipboard(SelectedRect);

            // Blank the selected area in the original image.
            using (Graphics gr = Graphics.FromImage(OriginalImage))
            {
                using (SolidBrush br = new SolidBrush(pictureBox1.BackColor))
                {
                    gr.FillRectangle(br, SelectedRect);
                }
            }

            // Display the result.
            SelectedImage = new Bitmap(OriginalImage);
            pictureBox1.Image = SelectedImage;

            SelectedImage = null;
            SelectedGraphics = null;
            MadeSelection = false;
        }

        //貼上(中間)
        // Paste the image on the clipboard, centering it on the selected area.
        private void button3_Click(object sender, EventArgs e)
        {
            // Do nothing if the clipboard doesn't hold an image.
            if (!Clipboard.ContainsImage()) return;

            // Get the clipboard's image.
            Image clipboard_image = Clipboard.GetImage();

            // Figure out where to put it.
            int cx = SelectedRect.X + (SelectedRect.Width - clipboard_image.Width) / 2;
            int cy = SelectedRect.Y + (SelectedRect.Height - clipboard_image.Height) / 2;
            Rectangle dest_rect = new Rectangle(
                cx, cy,
                clipboard_image.Width,
                clipboard_image.Height);

            // Copy the new image into position.
            using (Graphics gr = Graphics.FromImage(OriginalImage))
            {
                gr.DrawImage(clipboard_image, dest_rect);
            }

            // Display the result.
            pictureBox1.Image = OriginalImage;
            pictureBox1.Refresh();

            SelectedImage = null;
            SelectedGraphics = null;
            MadeSelection = false;
        }

        //貼上(延展)
        // Paste the image on the clipboard, stretching it to fit the selected area.
        private void button4_Click(object sender, EventArgs e)
        {
            // Do nothing if the clipboard doesn't hold an image.
            if (!Clipboard.ContainsImage()) return;

            // Get the clipboard's image.
            Image clipboard_image = Clipboard.GetImage();

            // Get the image's bounding Rectangle.
            Rectangle src_rect = new Rectangle(
                0, 0,
                clipboard_image.Width,
                clipboard_image.Height);

            // Copy the new image into position.
            using (Graphics gr = Graphics.FromImage(OriginalImage))
            {
                gr.DrawImage(clipboard_image, SelectedRect,
                    src_rect, GraphicsUnit.Pixel);
            }

            // Display the result.
            pictureBox1.Image = OriginalImage;
            pictureBox1.Refresh();

            SelectedImage = null;
            SelectedGraphics = null;
            MadeSelection = false;
        }

        //離開
        private void button5_Click(object sender, EventArgs e)
        {
            this.Close();
        }


    }
}
