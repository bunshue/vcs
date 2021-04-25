using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;

namespace vcs_PictureCrop2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private bool flag_select_area = false;  //開始選取的旗標
        private Point pt_st, pt_sp;             //選取的起始點和終點
        private Bitmap bitmap1 = null;  //原圖位圖Bitmap
        private Bitmap bitmap2 = null;  //擷取部分位圖Bitmap

        // The cropped image with the selection rectangle.
        private Bitmap DisplayImage;
        private Graphics DisplayGraphics;

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            flag_select_area = true;
            pt_st = e.Location;

            // Draw the area selected.
            DrawSelectionBox(e.Location);
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_select_area == false)
                return;

            // Draw the area selected.
            DrawSelectionBox(e.Location);
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            if (flag_select_area == false)
                return;

            flag_select_area = false;

            // Crop.
            // Get the selected area's dimensions.
            int x = Math.Min(pt_st.X, pt_sp.X);
            int y = Math.Min(pt_st.Y, pt_sp.Y);
            int width = Math.Abs(pt_st.X - pt_sp.X);
            int height = Math.Abs(pt_st.Y - pt_sp.Y);
            Rectangle source_rect = new Rectangle(x, y, width, height);
            Rectangle dest_rect = new Rectangle(0, 0, width, height);

            // Copy that part of the image to a new bitmap.
            DisplayImage = new Bitmap(width, height);
            DisplayGraphics = Graphics.FromImage(DisplayImage);
            DisplayGraphics.DrawImage(bitmap2, dest_rect, source_rect, GraphicsUnit.Pixel);

            // Display the new bitmap.
            bitmap2 = DisplayImage;
            DisplayImage = bitmap2.Clone() as Bitmap;
            DisplayGraphics = Graphics.FromImage(DisplayImage);
            pictureBox1.Image = DisplayImage;
            pictureBox1.Refresh();
        }

        // Draw the area selected.
        private void DrawSelectionBox(Point end_point)
        {
            // Save the end point.
            pt_sp = end_point;
            if (pt_sp.X < 0)
                pt_sp.X = 0;
            if (pt_sp.X >= bitmap2.Width)
                pt_sp.X = bitmap2.Width - 1;
            if (pt_sp.Y < 0)
                pt_sp.Y = 0;
            if (pt_sp.Y >= bitmap2.Height)
                pt_sp.Y = bitmap2.Height - 1;

            // Reset the image.
            DisplayGraphics.DrawImageUnscaled(bitmap2, 0, 0);

            // Draw the selection area.
            int x = Math.Min(pt_st.X, pt_sp.X);
            int y = Math.Min(pt_st.Y, pt_sp.Y);
            int width = Math.Abs(pt_st.X - pt_sp.X);
            int height = Math.Abs(pt_st.Y - pt_sp.Y);
            DisplayGraphics.DrawRectangle(Pens.Red, x, y, width, height);
            pictureBox1.Refresh();
        }

        // Load the image into a Bitmap, clone it, and
        // set the PictureBox's Image property to the Bitmap.
        private Bitmap LoadBitmapUnlocked(string file_name)
        {
            using (Bitmap bm = new Bitmap(file_name))
            {
                Bitmap new_bitmap = new Bitmap(bm.Width, bm.Height);
                using (Graphics gr = Graphics.FromImage(new_bitmap))
                {
                    gr.DrawImage(bm, 0, 0);
                }
                return new_bitmap;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //Open
            string filename = @"C:\______test_files\picture1.jpg";
            bitmap1 = LoadBitmapUnlocked(filename);
            bitmap2 = bitmap1.Clone() as Bitmap;
            DisplayImage = bitmap2.Clone() as Bitmap;
            DisplayGraphics = Graphics.FromImage(DisplayImage);

            pictureBox1.Image = DisplayImage;
            pictureBox1.Visible = true;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            save_select_picture_to_drive();
        }

        void save_select_picture_to_drive()
        {
            if (bitmap2 != null)
            {
                string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

                try
                {
                    bitmap2.Save(filename, ImageFormat.Bmp);

                    richTextBox1.Text += "存檔成功\n";
                    richTextBox1.Text += "已存檔 : " + filename + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }
            else
                richTextBox1.Text += "無圖可存\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //Reset
            // Display the original image.
            bitmap2 = bitmap1.Clone() as Bitmap;
            DisplayImage = bitmap1.Clone() as Bitmap;
            DisplayGraphics = Graphics.FromImage(DisplayImage);
            pictureBox1.Image = DisplayImage;
        }
    }
}
