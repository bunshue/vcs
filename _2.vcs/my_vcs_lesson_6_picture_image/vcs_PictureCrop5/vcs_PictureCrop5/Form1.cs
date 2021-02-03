using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace vcs_PictureCrop5
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private Bitmap m_OriginalImage = null;
        private int X0, Y0, X1, Y1;
        private bool SelectingArea = false;
        private Bitmap SelectedImage = null;
        private Graphics SelectedGraphics = null;

        // Save the original image.
        private void Form1_Load(object sender, EventArgs e)
        {
            m_OriginalImage = new Bitmap(pictureBox1.Image);
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
            SelectedImage = new Bitmap(m_OriginalImage);
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
            SelectedGraphics.DrawImage(m_OriginalImage, 0, 0);

            // Draw the selection rectangle.
            using (Pen select_pen = new Pen(Color.Red))
            {
                select_pen.DashStyle = DashStyle.Dash;
                Rectangle rect = MakeRectangle(X0, Y0, X1, Y1);
                SelectedGraphics.DrawRectangle(select_pen, rect);
            }

            pictureBox1.Refresh();
        }

        // Finish selecting the area.
        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            if (!SelectingArea) return;
            SelectingArea = false;
            SelectedImage = null;
            SelectedGraphics = null;
            pictureBox1.Image = m_OriginalImage;
            pictureBox1.Refresh();

            // Convert the points into a Rectangle.
            Rectangle rect = MakeRectangle(X0, Y0, X1, Y1);
            if ((rect.Width > 0) && (rect.Height > 0))
            {
                // Display the Rectangle.
                //MessageBox.Show(rect.ToString());
                //richTextBox1.Text += rect.ToString() + "\n";
                richTextBox1.Text += "起點(" + rect.X.ToString() + ", " + rect.Y.ToString() + "), W = " + rect.Width.ToString() + " H = " + rect.Height.ToString() + "\n";
            }
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
                pictureBox1.Image = m_OriginalImage;
                pictureBox1.Refresh();
            }
        }
    }
}
