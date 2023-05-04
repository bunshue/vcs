using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat

using System.Drawing.Drawing2D;   //for PixelOffsetMode, InterpolationMode

namespace vcs_ZoomPicture4c
{
    public partial class Form1 : Form
    {
        // The current scale.
        private float ImageScale = 1.0f;

        // The original image.
        private Bitmap OriginalImage;

        // The currently cropped image.
        private Bitmap CroppedImage;

        // The currently scaled cropped image.
        private Bitmap ScaledImage;

        // The cropped image with the selection rectangle.
        private Bitmap DisplayImage;
        private Graphics DisplayGraphics;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files1\picture1.jpg";

            OriginalImage = LoadBitmapUnlocked(filename);
            CroppedImage = OriginalImage.Clone() as Bitmap;

            MakeScaledImage();
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


        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            int value = trackBar1.Value;
            switch (value)
            {
                case 0: ImageScale = 0.5f; break;
                case 1: ImageScale = 0.75f; break;
                case 2: ImageScale = 1.0f; break;
                case 3: ImageScale = 1.25f; break;
                default: ImageScale = (value + 2) / 4f; break;
            }
            label1.Text = ImageScale.ToString() + " X";

            MakeScaledImage();

            //SetScale(ImageScale);
            //pictureBox1.ClientSize = new Size((int)(ImageScale * pictureBox1.Image.Width), (int)(ImageScale * pictureBox1.Image.Height));
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = Application.StartupPath + "\\zoom_picture_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

            // Make a bitmap of the correct size.
            using (Bitmap bitmap1 = new Bitmap(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height))
            {
                // Copy the original image onto the new bitmap.
                using (Graphics gr = Graphics.FromImage(bitmap1))
                {
                    Rectangle source_rect = new Rectangle(
                        0, 0, pictureBox1.Image.Width, pictureBox1.Image.Height);
                    Rectangle dest_rect = new Rectangle(
                        0, 0, bitmap1.Width, bitmap1.Height);
                    gr.DrawImage(pictureBox1.Image,
                        dest_rect, source_rect, GraphicsUnit.Pixel);
                }

                bitmap1.Save(filename, ImageFormat.Bmp);
                //richTextBox1.Text += "已存檔 : " + filename + "\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            // Display the original image.
            CroppedImage = OriginalImage.Clone() as Bitmap;
            MakeScaledImage();
        }

        // Make the scaled cropped image.
        private void MakeScaledImage()
        {
            int wid = (int)(ImageScale * (CroppedImage.Width));
            int hgt = (int)(ImageScale * (CroppedImage.Height));
            ScaledImage = new Bitmap(wid, hgt);
            using (Graphics gr = Graphics.FromImage(ScaledImage))
            {
                Rectangle src_rect = new Rectangle(0, 0,
                    CroppedImage.Width, CroppedImage.Height);
                Rectangle dest_rect = new Rectangle(0, 0, wid, hgt);
                gr.PixelOffsetMode = PixelOffsetMode.Half;
                gr.InterpolationMode = InterpolationMode.NearestNeighbor;
                gr.DrawImage(CroppedImage, dest_rect, src_rect,
                    GraphicsUnit.Pixel);
            }

            DisplayImage = ScaledImage.Clone() as Bitmap;
            if (DisplayGraphics != null) DisplayGraphics.Dispose();
            DisplayGraphics = Graphics.FromImage(DisplayImage);

            pictureBox1.Image = DisplayImage;
        }

        // Let the user select an area.
        private bool Drawing = false;
        private Point StartPoint, EndPoint;
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            Drawing = true;

            StartPoint = RoundPoint(e.Location);

            // Draw the area selected.
            DrawSelectionBox(StartPoint);
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (!Drawing) return;

            // Draw the area selected.
            DrawSelectionBox(RoundPoint(e.Location));
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            if (!Drawing) return;
            Drawing = false;

            // Crop.
            // Get the selected area's dimensions.
            int x = (int)(Math.Min(StartPoint.X, EndPoint.X) / ImageScale);
            int y = (int)(Math.Min(StartPoint.Y, EndPoint.Y) / ImageScale);
            int width = (int)(Math.Abs(StartPoint.X - EndPoint.X) / ImageScale);
            int height = (int)(Math.Abs(StartPoint.Y - EndPoint.Y) / ImageScale);

            if ((width == 0) || (height == 0))
            {
                MessageBox.Show("Width and height must be greater than 0.");
                return;
            }

            Rectangle source_rect = new Rectangle(x, y, width, height);
            Rectangle dest_rect = new Rectangle(0, 0, width, height);

            // Copy that part of the image to a new bitmap.
            Bitmap new_image = new Bitmap(width, height);
            using (Graphics gr = Graphics.FromImage(new_image))
            {
                gr.DrawImage(CroppedImage, dest_rect, source_rect,
                    GraphicsUnit.Pixel);
            }
            CroppedImage = new_image;

            // Display the new scaled image.
            MakeScaledImage();
        }

        // Round the point to the nearest unscaled pixel location.
        private Point RoundPoint(Point point)
        {
            int x = (int)(ImageScale * (int)(point.X / ImageScale));
            int y = (int)(ImageScale * (int)(point.Y / ImageScale));
            return new Point(x, y);
        }

        // Draw the area selected.
        private void DrawSelectionBox(Point end_point)
        {
            // Save the end point.
            EndPoint = end_point;
            if (EndPoint.X < 0) EndPoint.X = 0;
            if (EndPoint.X >= ScaledImage.Width) EndPoint.X = ScaledImage.Width - 1;
            if (EndPoint.Y < 0) EndPoint.Y = 0;
            if (EndPoint.Y >= ScaledImage.Height) EndPoint.Y = ScaledImage.Height - 1;

            // Reset the image.
            DisplayGraphics.DrawImageUnscaled(ScaledImage, 0, 0);

            // Draw the selection area.
            int x = Math.Min(StartPoint.X, EndPoint.X);
            int y = Math.Min(StartPoint.Y, EndPoint.Y);
            int width = Math.Abs(StartPoint.X - EndPoint.X);
            int height = Math.Abs(StartPoint.Y - EndPoint.Y);
            DisplayGraphics.DrawRectangle(Pens.Red, x, y, width, height);
            pictureBox1.Refresh();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {

        }

    
    
    
    }
}
