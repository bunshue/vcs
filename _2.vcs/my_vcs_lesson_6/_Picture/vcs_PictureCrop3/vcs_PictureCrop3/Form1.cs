using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat

namespace vcs_PictureCrop3
{
    public partial class Form1 : Form
    {
        private Bitmap bitmap1 = null;
        private Bitmap bitmap2 = null;
        private int X0, Y0, X1, Y1;
        private bool SelectingArea = false;
        private Graphics SelectedGraphics = null;
        private Rectangle SelectedRect;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bitmap1 = new Bitmap(pictureBox1.Image);

            this.KeyPreview = true;
        }

        // Start selecting an area.
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
        }

        // Continue selecting an area.
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
        }

        // Finish selecting the area.
        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "SelectedRect X = " + SelectedRect.X.ToString() + " Y = " + SelectedRect.Y.ToString() + "\n";
            richTextBox1.Text += "SelectedRect W = " + SelectedRect.Width.ToString() + " H = " + SelectedRect.Height.ToString() + "\n";
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
            if ((SelectedRect.Width <= 0) || (SelectedRect.Height <= 0))
            {
                richTextBox1.Text += "未選定區域，無法複製圖片\n";
                return;
            }

            // Copy the selected area to the clipboard.
            CopyToClipboard(SelectedRect);
            richTextBox1.Text += "已複製圖片\n";
        }


        // Copy the selected area to the clipboard
        // and blank that area.
        private void button3_Click(object sender, EventArgs e)
        {
            if ((SelectedRect.Width <= 0) || (SelectedRect.Height <= 0))
            {
                richTextBox1.Text += "未選定區域，無法剪下圖片\n";
                return;
            }

            // Copy the selection to the clipboard.
            CopyToClipboard(SelectedRect);

            // Blank the selected area in the original image.
            using (Graphics gr = Graphics.FromImage(bitmap1))
            {
                using (SolidBrush br = new SolidBrush(pictureBox1.BackColor))
                {
                    gr.FillRectangle(br, SelectedRect);
                }
            }

            // Display the result.
            bitmap2 = new Bitmap(bitmap1);
            pictureBox1.Image = bitmap2;

        }

        private void bt_save_Click(object sender, EventArgs e)
        {
            save_image_to_drive();
        }

        void save_image_to_drive()
        {
            if (bitmap1 != null)
            {
                string filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                String filename1 = filename + ".jpg";
                String filename2 = filename + ".bmp";
                String filename3 = filename + ".png";

                try
                {
                    bitmap1.Save(@filename1, ImageFormat.Jpeg);
                    bitmap1.Save(@filename2, ImageFormat.Bmp);
                    bitmap1.Save(@filename3, ImageFormat.Png);

                    richTextBox1.Text += "存檔成功\n";
                    richTextBox1.Text += "已存檔 : " + filename1 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename3 + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }
            else
                richTextBox1.Text += "無圖可存\n";
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
            int cx = SelectedRect.X + (SelectedRect.Width - clipboard_image.Width) / 2;
            int cy = SelectedRect.Y + (SelectedRect.Height - clipboard_image.Height) / 2;
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
            SelectedGraphics = null;
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
                gr.DrawImage(clipboard_image, SelectedRect,
                    src_rect, GraphicsUnit.Pixel);
            }

            // Display the result.
            pictureBox1.Image = bitmap1;
            pictureBox1.Refresh();

            bitmap2 = null;
            SelectedGraphics = null;
        }

        // If the user presses Escape, cancel.
        private void Form1_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == 27)
            {
                if (!SelectingArea) return;
                SelectingArea = false;

                // Stop selecting.
                bitmap2 = null;
                SelectedGraphics = null;
                pictureBox1.Image = bitmap1;
                pictureBox1.Refresh();
            }
        }

    }
}
