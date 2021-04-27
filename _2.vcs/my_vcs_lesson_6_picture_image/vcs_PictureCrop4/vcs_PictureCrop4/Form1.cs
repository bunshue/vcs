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

        private int W = 0;  //原圖的寬
        private int H = 0;  //原圖的高
        private int w = 0;  //擷取圖的寬
        private int h = 0;  //擷取圖的高

        // Save the original image.
        private void Form1_Load(object sender, EventArgs e)
        {
            bitmap1 = new Bitmap(filename);
            pictureBox1.Image = bitmap1;

            W = bitmap1.Width;
            H = bitmap1.Height;
            pictureBox1.ClientSize = new Size(W, H);
            pictureBox2.ClientSize = new Size(W, H);
        }

        // Return a Rectangle with these points as corners.
        private Rectangle MakeRectangle(int x0, int y0, int x1, int y1)
        {
            return new Rectangle(Math.Min(x0, x1), Math.Min(y0, y1), Math.Abs(x0 - x1), Math.Abs(y0 - y1));
        }

        private Rectangle MakeRectangle(Point pt1, Point pt2)
        {
            return new Rectangle(Math.Min(pt1.X, pt2.X), Math.Min(pt1.Y, pt2.Y), Math.Abs(pt1.X - pt2.X), Math.Abs(pt1.Y - pt2.Y));
        }

        // Start selecting the rectangle.
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            flag_select_area = true;
            pt_st = e.Location; //起始點座標
        }

        // Continue selecting.
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            // Do nothing it we're not selecting an area.
            if (flag_select_area == false)
                return;

            pt_sp = e.Location; //終點座標

            select_rectangle = MakeRectangle(pt_st, pt_sp);

            // Make a Bitmap to display the selection rectangle.
            Bitmap bm = new Bitmap(bitmap1);

            // Draw the rectangle.
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.DrawRectangle(Pens.Green, select_rectangle);
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
            //pictureBox1.Image = bitmap1;  //仍應保留選取區域

            int w = select_rectangle.Width;
            int h = select_rectangle.Height;

            if (w < 1)
                return;
            if (h < 1)
                return;

            Bitmap area = new Bitmap(w, h);
            using (Graphics g2 = Graphics.FromImage(area))
            {
                Rectangle dest_rectangle = new Rectangle(0, 0, w, h);
                g2.DrawImage(bitmap1, dest_rectangle, select_rectangle, GraphicsUnit.Pixel);
            }

            // Display the result.
            pictureBox2.Image = area;
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
                //g2 = null;
                pictureBox1.Image = bitmap1;
                pictureBox1.Refresh();
            }
        }
    }
}
