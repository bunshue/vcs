using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat

namespace vcs_PictureCrop
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\bear.jpg";

        private bool flag_select_area = false;  //開始選取的旗標
        private Point pt_st = Point.Empty;//記錄鼠標按下時的坐標，用來確定繪圖起點
        private Point pt_sp = Point.Empty;//記錄鼠標放開時的坐標，用來確定繪圖終點
        private Bitmap bitmap1 = null;  //原圖位圖Bitmap
        private Bitmap bitmap2 = null;  //擷取部分位圖Bitmap
        private Rectangle select_rectangle;//用來保存截圖的矩形

        private int X0, Y0, X1, Y1;
        private Graphics g2 = null;     //繪圖物件

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bitmap1 = new Bitmap(filename);
            pictureBox1.Image = bitmap1;

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
            ConvertCoordinates(pictureBox1, out X0, out Y0, e.X, e.Y);

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

            // Generate the new image with the selection rectangle.
            ConvertCoordinates(pictureBox1, out X1, out Y1, e.X, e.Y);

            // Copy the original image.
            g2.DrawImage(bitmap1, 0, 0);

            // Draw the selection rectangle.
            using (Pen select_pen = new Pen(Color.Red))
            {
                select_pen.DashStyle = System.Drawing.Drawing2D.DashStyle.Dash;
                Rectangle rect = MakeRectangle(X0, Y0, X1, Y1);
                g2.DrawRectangle(select_pen, rect);
            }
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
            select_rectangle = MakeRectangle(X0, Y0, X1, Y1);

            richTextBox1.Text += "select_rectangle = " + select_rectangle.ToString() + "\n";
        }

        // Convert the coordinates for the image's SizeMode.
        private void ConvertCoordinates(PictureBox pic, out int X0, out int Y0, int x, int y)
        {
            int pic_hgt = pic.ClientSize.Height;
            int pic_wid = pic.ClientSize.Width;
            int img_hgt = pic.Image.Height;
            int img_wid = pic.Image.Width;

            X0 = x;
            Y0 = y;
            switch (pic.SizeMode)
            {
                case PictureBoxSizeMode.AutoSize:
                case PictureBoxSizeMode.Normal:
                    // These are okay. Leave them alone.
                    break;
                case PictureBoxSizeMode.CenterImage:
                    X0 = x - (pic_wid - img_wid) / 2;
                    Y0 = y - (pic_hgt - img_hgt) / 2;
                    break;
                case PictureBoxSizeMode.StretchImage:
                    X0 = (int)(img_wid * x / (float)pic_wid);
                    Y0 = (int)(img_hgt * y / (float)pic_hgt);
                    break;
                case PictureBoxSizeMode.Zoom:
                    float pic_aspect = pic_wid / (float)pic_hgt;
                    float img_aspect = img_wid / (float)img_hgt;
                    if (pic_aspect > img_aspect)
                    {
                        // The PictureBox is wider/shorter than the image.
                        Y0 = (int)(img_hgt * y / (float)pic_hgt);

                        // The image fills the height of the PictureBox.
                        // Get its width.
                        float scaled_width = img_wid * pic_hgt / img_hgt;
                        float dx = (pic_wid - scaled_width) / 2;
                        X0 = (int)((x - dx) * img_hgt / (float)pic_hgt);
                    }
                    else
                    {
                        // The PictureBox is taller/thinner than the image.
                        X0 = (int)(img_wid * x / (float)pic_wid);

                        // The image fills the height of the PictureBox.
                        // Get its height.
                        float scaled_height = img_hgt * pic_wid / img_wid;
                        float dy = (pic_hgt - scaled_height) / 2;
                        Y0 = (int)((y - dy) * img_wid / pic_wid);
                    }
                    break;
                default:
                    break;
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
                gr.DrawImage(bitmap1, dest_rect, src_rect, GraphicsUnit.Pixel);
            }

            // Copy the selection image to the clipboard.
            Clipboard.SetImage(bm);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if ((select_rectangle.Width <= 0) || (select_rectangle.Height <= 0))
            {
                richTextBox1.Text += "未選定區域，無法複製圖片\n";
                return;
            }

            // Copy the selected area to the clipboard.
            CopyToClipboard(select_rectangle);
            richTextBox1.Text += "已複製圖片\n";
        }

        // Copy the selected area to the clipboard
        // and blank that area.
        private void button3_Click(object sender, EventArgs e)
        {
            if ((select_rectangle.Width <= 0) || (select_rectangle.Height <= 0))
            {
                richTextBox1.Text += "未選定區域，無法剪下圖片\n";
                return;
            }

            // Copy the selection to the clipboard.
            CopyToClipboard(select_rectangle);

            // Blank the selected area in the original image.
            using (Graphics gr = Graphics.FromImage(bitmap1))
            {
                using (SolidBrush br = new SolidBrush(pictureBox1.BackColor))
                {
                    gr.FillRectangle(br, select_rectangle);
                }
            }

            // Display the result.
            bitmap2 = new Bitmap(bitmap1);
            pictureBox1.Image = bitmap2;
        }

        //貼上 定點
        private void button4_Click(object sender, EventArgs e)
        {
            // Paste the image on the clipboard, centering it on the selected area.
            // Do nothing if the clipboard doesn't hold an image.
            if (!Clipboard.ContainsImage()) return;

            // Get the clipboard's image.
            Image clipboard_image = Clipboard.GetImage();

            // Figure out where to put it.
            int cx = select_rectangle.X + (select_rectangle.Width - clipboard_image.Width) / 2;
            int cy = select_rectangle.Y + (select_rectangle.Height - clipboard_image.Height) / 2;
            Rectangle dest_rect = new Rectangle(
                cx, cy,
                clipboard_image.Width,
                clipboard_image.Height);

            // Copy the new image into position.
            using (Graphics gr = Graphics.FromImage(bitmap1))
            {
                gr.DrawImage(clipboard_image, dest_rect);
            }

            // Display the result.
            pictureBox1.Image = bitmap1;
            pictureBox1.Refresh();

            bitmap2 = null;
            g2 = null;
        }

        //貼上 伸展
        private void button5_Click(object sender, EventArgs e)
        {
            // Paste the image on the clipboard, stretching it to fit the selected area.
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
            using (Graphics gr = Graphics.FromImage(bitmap1))
            {
                gr.DrawImage(clipboard_image, select_rectangle,
                    src_rect, GraphicsUnit.Pixel);
            }

            // Display the result.
            pictureBox1.Image = bitmap1;
            pictureBox1.Refresh();

            bitmap2 = null;
            g2 = null;
        }

        // If the user presses Escape, cancel.
        private void Form1_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == 27)
            {
                richTextBox1.Text += "Esc\n";
                if (flag_select_area == false)
                    return;
                flag_select_area = false;

                // Stop selecting.
                bitmap2 = null;
                g2 = null;
                pictureBox1.Image = bitmap1;
                pictureBox1.Refresh();
            }
        }
    }
}
