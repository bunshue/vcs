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

        private bool flag_select_area = false;  //開始選取的旗標
        private Point pt_st = Point.Empty;//記錄鼠標按下時的坐標，用來確定繪圖起點
        private Point pt_sp = Point.Empty;//記錄鼠標放開時的坐標，用來確定繪圖終點
        private Bitmap bitmap1 = null;  //原圖位圖Bitmap
        private Bitmap bitmap2 = null;  //擷取部分位圖Bitmap
        private Rectangle select_rectangle;//用來保存截圖的矩形

        private Graphics g1 = null;
        private Graphics g2 = null;
        private bool MadeSelection = false;

        string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.bmp";

        private void Form1_Load(object sender, EventArgs e)
        {
            //讀取圖檔
            pictureBox1.Image = Image.FromFile(filename);

            bitmap1 = new Bitmap(pictureBox1.Image);

            this.KeyPreview = true;
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

        // Start selecting an area.
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            // Save the starting point.
            flag_select_area = true;
            pt_st = e.Location; //起始點座標

            // Make the selected image.
            bitmap2 = new Bitmap(bitmap1);
            g2 = Graphics.FromImage(bitmap2);
            pictureBox1.Image = bitmap2;
        }

        // Continue selecting an area.
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            // Do nothing if we're not selecting an area.
            if (flag_select_area == false)
                return;

            pt_sp = e.Location; //終點座標

            select_rectangle = MakeRectangle(pt_st, pt_sp);

            // Generate the new image with the selection rectangle.
            // Copy the original image.
            g2.DrawImage(bitmap1, 0, 0);

            // Draw the selection rectangle.
            Pen select_pen = new Pen(Color.Red);
            select_pen.DashStyle = System.Drawing.Drawing2D.DashStyle.Dash;
            g2.DrawRectangle(select_pen, select_rectangle);
            pictureBox1.Refresh();
        }

        // Finish selecting the area.
        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            // Do nothing if we're not selecting an area.
            if (flag_select_area == false)
                return;
            flag_select_area = false;

            // Stop selecting.
            g2 = null;

            // Convert the points into a Rectangle.
            select_rectangle = MakeRectangle(pt_st, pt_sp);
            MadeSelection = ((select_rectangle.Width > 0) && (select_rectangle.Height > 0));

            this.Text = "選取區域 : " + select_rectangle.ToString();
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
                g2 = null;
                pictureBox1.Image = bitmap1;
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
            using (Graphics g2 = Graphics.FromImage(bm))
            {
                Rectangle dest_rect = new Rectangle(0, 0, src_rect.Width, src_rect.Height);
                g2.DrawImage(bitmap1, dest_rect, src_rect, GraphicsUnit.Pixel);
            }

            // Copy the selection image to the clipboard.
            Clipboard.SetImage(bm);
        }

        //複製
        // Copy the selected area to the clipboard.
        private void button1_Click(object sender, EventArgs e)
        {
            CopyToClipboard(select_rectangle);
        }

        //剪下
        // Copy the selected area to the clipboard
        // and blank that area.
        private void button2_Click(object sender, EventArgs e)
        {
            // Copy the selection to the clipboard.
            CopyToClipboard(select_rectangle);

            // Blank the selected area in the original image.
            using (Graphics g2 = Graphics.FromImage(bitmap1))
            {
                using (SolidBrush br = new SolidBrush(pictureBox1.BackColor))
                {
                    g2.FillRectangle(br, select_rectangle);
                }
            }

            // Display the result.
            bitmap2 = new Bitmap(bitmap1);
            pictureBox1.Image = bitmap2;

            bitmap2 = null;
            //g2 = null;
            MadeSelection = false;
        }

        //貼上(中間)
        // Paste the image on the clipboard, centering it on the selected area.
        private void button3_Click(object sender, EventArgs e)
        {
            // Do nothing if the clipboard doesn't hold an image.
            if (!Clipboard.ContainsImage())
                return;

            // Get the clipboard's image.
            Image clipboard_image = Clipboard.GetImage();

            // Figure out where to put it.
            int cx = select_rectangle.X + (select_rectangle.Width - clipboard_image.Width) / 2;
            int cy = select_rectangle.Y + (select_rectangle.Height - clipboard_image.Height) / 2;
            Rectangle dest_rect = new Rectangle(cx, cy, clipboard_image.Width, clipboard_image.Height);

            // Copy the new image into position.
            using (Graphics g2 = Graphics.FromImage(bitmap1))
            {
                g2.DrawImage(clipboard_image, dest_rect);
            }

            // Display the result.
            pictureBox1.Image = bitmap1;
            pictureBox1.Refresh();

            bitmap2 = null;
            //g2 = null;
            MadeSelection = false;
        }

        //貼上(延展)
        // Paste the image on the clipboard, stretching it to fit the selected area.
        private void button4_Click(object sender, EventArgs e)
        {
            // Do nothing if the clipboard doesn't hold an image.
            if (!Clipboard.ContainsImage())
                return;

            // Get the clipboard's image.
            Image clipboard_image = Clipboard.GetImage();

            // Get the image's bounding Rectangle.
            Rectangle src_rect = new Rectangle(0, 0, clipboard_image.Width, clipboard_image.Height);

            // Copy the new image into position.
            using (Graphics g2 = Graphics.FromImage(bitmap1))
            {
                g2.DrawImage(clipboard_image, select_rectangle, src_rect, GraphicsUnit.Pixel);
            }

            // Display the result.
            pictureBox1.Image = bitmap1;
            pictureBox1.Refresh();

            bitmap2 = null;
            //g2 = null;
            MadeSelection = false;
        }
    }
}

