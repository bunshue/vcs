using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_PictureCrop4
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The original image.
        private Bitmap bmp;
        string filename = @"C:\______test_files\picture1.jpg";

        // True when we're selecting a rectangle.
        private bool IsSelecting = false;

        // The area we are selecting.
        private int X0, Y0, X1, Y1;

        // Save the original image.
        private void Form1_Load(object sender, EventArgs e)
        {
            int w;
            int h;
            bmp = new Bitmap(filename);
            w = bmp.Width;
            h = bmp.Height;
            pictureBox1.ClientSize = new Size(w, h);
            pictureBox2.ClientSize = new Size(w, h);

            pictureBox1.Image = bmp;
        }

        // Start selecting the rectangle.
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            IsSelecting = true;

            // Save the start point.
            X0 = e.X;
            Y0 = e.Y;
        }
        
        // Continue selecting.
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            // Do nothing it we're not selecting an area.
            if (!IsSelecting) return;

            // Save the new point.
            X1 = e.X;
            Y1 = e.Y;

            // Make a Bitmap to display the selection rectangle.
            Bitmap bm = new Bitmap(bmp);

            // Draw the rectangle.
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.DrawRectangle(Pens.Red, Math.Min(X0, X1), Math.Min(Y0, Y1), Math.Abs(X0 - X1), Math.Abs(Y0 - Y1));
            }
            // Display the temporary bitmap.
            pictureBox1.Image = bm;
        }

        // Finish selecting the area.
        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            // Do nothing it we're not selecting an area.
            if (!IsSelecting) return;
            IsSelecting = false;

            // Display the original image.
            pictureBox1.Image = bmp;

            // Copy the selected part of the image.
            int wid = Math.Abs(X0 - X1);
            int hgt = Math.Abs(Y0 - Y1);
            if ((wid < 1) || (hgt < 1)) return;

            Bitmap area = new Bitmap(wid, hgt);
            using (Graphics gr = Graphics.FromImage(area))
            {
                Rectangle source_rectangle = 
                    new Rectangle(Math.Min(X0, X1), Math.Min(Y0, Y1), wid, hgt);
                Rectangle dest_rectangle = 
                    new Rectangle(0, 0, wid, hgt);
                gr.DrawImage(bmp, dest_rectangle, 
                    source_rectangle, GraphicsUnit.Pixel);
            }

            // Display the result.
            pictureBox2.Image = area;
        }
    }
}
