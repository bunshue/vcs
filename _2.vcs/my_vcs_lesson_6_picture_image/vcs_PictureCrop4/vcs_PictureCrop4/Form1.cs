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

        string filename = @"C:\______test_files\picture1.jpg";

        private bool flag_select_area = false;  //開始選取的旗標
        private Point pt_st = Point.Empty;//記錄鼠標按下時的坐標，用來確定繪圖起點
        private Point pt_sp = Point.Empty;//記錄鼠標放開時的坐標，用來確定繪圖終點
        private Bitmap bitmap1 = null;  //原圖位圖Bitmap
        private Bitmap bitmap2 = null;  //擷取部分位圖Bitmap
        private Rectangle select_rectangle;//用來保存截圖的矩形

        // The area we are selecting.
        private int X0, Y0, X1, Y1;

        // Save the original image.
        private void Form1_Load(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";
            bitmap1 = new Bitmap(filename);
            pictureBox1.Image = bitmap1;

            int w;
            int h;
            w = bitmap1.Width;
            h = bitmap1.Height;
            pictureBox1.ClientSize = new Size(w, h);
            pictureBox2.ClientSize = new Size(w, h);
        }

        // Return a Rectangle with these points as corners.
        private Rectangle MakeRectangle(int x0, int y0, int x1, int y1)
        {
            return new Rectangle(Math.Min(x0, x1), Math.Min(y0, y1), Math.Abs(x0 - x1), Math.Abs(y0 - y1));
        }

        // Start selecting the rectangle.
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            flag_select_area = true;

            // Save the start point.
            X0 = e.X;
            Y0 = e.Y;
            pt_st = e.Location;
        }
        
        // Continue selecting.
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            // Do nothing it we're not selecting an area.
            if (flag_select_area == false)
                return;

            // Save the new point.
            X1 = e.X;
            Y1 = e.Y;
            pt_sp = e.Location;

            // Make a Bitmap to display the selection rectangle.
            Bitmap bm = new Bitmap(bitmap1);

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
            if (flag_select_area == false)
                return;
            flag_select_area = false;

            // Display the original image.
            pictureBox1.Image = bitmap1;

            // Copy the selected part of the image.
            int w = Math.Abs(X0 - X1);
            int h = Math.Abs(Y0 - Y1);
            if ((w < 1) || (h < 1)) return;

            Bitmap area = new Bitmap(w, h);
            using (Graphics gr = Graphics.FromImage(area))
            {
                Rectangle source_rectangle = new Rectangle(Math.Min(X0, X1), Math.Min(Y0, Y1), w, h);
                Rectangle dest_rectangle = new Rectangle(0, 0, w, h);
                gr.DrawImage(bitmap1, dest_rectangle, source_rectangle, GraphicsUnit.Pixel);
            }

            // Display the result.
            pictureBox2.Image = area;
        }
    }
}
