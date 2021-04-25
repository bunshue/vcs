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

        private int X0, Y0, X1, Y1;
        private bool flag_select_area = false;  //開始選取的旗標
        private Point pt_st, pt_sp;             //選取的起始點和終點
        private Bitmap bitmap1 = null;  //原圖位圖Bitmap
        private Bitmap bitmap2 = null;  //擷取部分位圖Bitmap
        private Graphics SelectedGraphics = null;

        // Save the original image.
        private void Form1_Load(object sender, EventArgs e)
        {
            bitmap1 = new Bitmap(pictureBox1.Image);
            this.KeyPreview = true;
        }

        // Start selecting an area.
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            // Save the starting point.
            flag_select_area = true;
            X0 = e.X;
            Y0 = e.Y;

            // Make the selected image.
            bitmap2 = new Bitmap(bitmap1);
            SelectedGraphics = Graphics.FromImage(bitmap2);
            pictureBox1.Image = bitmap2;
        }

        // Continue selecting an area.
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            // Do nothing if we're not selecting an area.
            if (flag_select_area == false)
                return;

            // Generate the new image with the selection rectangle.
            X1 = e.X;
            Y1 = e.Y;

            // Copy the original image.
            SelectedGraphics.DrawImage(bitmap1, 0, 0);

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
            if (flag_select_area == false)
                return;
            flag_select_area = false;
            bitmap2 = null;
            SelectedGraphics = null;
            pictureBox1.Image = bitmap1;
            pictureBox1.Refresh();

            // Convert the points into a Rectangle.
            Rectangle select_rectangle = MakeRectangle(X0, Y0, X1, Y1);
            if ((select_rectangle.Width > 0) && (select_rectangle.Height > 0))
            {
                // Display the Rectangle.
                richTextBox1.Text += "select_rectangle = " + select_rectangle.ToString() + "\n";
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
                if (flag_select_area == false)
                    return;
                flag_select_area = false;

                // Stop selecting.
                bitmap2 = null;
                SelectedGraphics = null;
                pictureBox1.Image = bitmap1;
                pictureBox1.Refresh();
            }
        }
    }
}
