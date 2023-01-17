using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;
using System.Drawing.Imaging;
using System.IO;

namespace vcs_PictureMontage
{
    public partial class Form1 : Form
    {
        // The loaded images.
        private List<ImageInfo> Images = new List<ImageInfo>();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        // Redraw the images.
        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            DrawPictures(e.Graphics, true);
        }

        // Draw the pictures.
        private void DrawPictures(Graphics gr, bool with_border)
        {
            gr.InterpolationMode = InterpolationMode.High;
            gr.Clear(pictureBox1.BackColor);
            foreach (ImageInfo info in Images)
                info.Draw(gr, with_border);
        }

        // The type if drag in progress.
        private ImageInfo.HitTypes DragType = ImageInfo.HitTypes.None;

        // Variables to remember what the mouse is over.
        private ImageInfo MouseImage = null;
        private ImageInfo.HitTypes MouseHitType = ImageInfo.HitTypes.None;

        // The position where a drag started.
        private Point StartPoint;
        private Rectangle StartRect;

        // Return the image under the mouse and the hit type.
        private void FindImageAt(Point point, out ImageInfo image,
            out ImageInfo.HitTypes hit_type)
        {
            // See if we hit an image.
            for (int i = Images.Count - 1; i >= 0; i--)
            {
                hit_type = Images[i].HitType(point);
                if (hit_type != ImageInfo.HitTypes.None)
                {
                    image = Images[i];
                    return;
                }
            }

            image = null;
            hit_type = ImageInfo.HitTypes.None;
        }

        // Display an appropriate mouse pointer.
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            // See if a drag is in progress.
            if (DragType == ImageInfo.HitTypes.None)
            {
                // No drag is in progress. Set the appropriate cursor.
                SetMouseCursor(e.Location);
            }
            else
            {
                if (DragType == ImageInfo.HitTypes.Body)
                {
                    // Just move it.
                    int dx = e.X - StartPoint.X;
                    int dy = e.Y - StartPoint.Y;
                    MouseImage.DestRect.X = StartRect.X + dx;
                    MouseImage.DestRect.Y = StartRect.Y + dy;
                }
                else
                {
                    // Get the desired new width and height.
                    int new_wid, new_hgt;
                    if ((DragType == ImageInfo.HitTypes.NwCorner) ||
                        (DragType == ImageInfo.HitTypes.SwCorner))
                        new_wid = StartRect.Right - e.X;
                    else
                        new_wid = e.X - StartRect.Left;

                    if ((DragType == ImageInfo.HitTypes.NwCorner) ||
                        (DragType == ImageInfo.HitTypes.NeCorner))
                        new_hgt = StartRect.Bottom - e.Y;
                    else
                        new_hgt = e.Y - StartRect.Top;

                    // Fix the aspect ratio.
                    if (new_hgt != 0)
                    {
                        float orig_aspect =
                            MouseImage.SourceRect.Width /
                            (float)MouseImage.SourceRect.Height;
                        float new_aspect = new_wid / (float)new_hgt;

                        if (new_aspect > orig_aspect)
                        {
                            // Too short and wide. Make taller.
                            new_hgt = (int)(new_wid / orig_aspect);
                        }
                        else if (new_aspect < orig_aspect)
                        {
                            // Too tall and thin. Make wider.
                            new_wid = (int)(new_hgt * orig_aspect);
                        }
        }

                    // Update the destination rectangle.
                    int right = MouseImage.DestRect.Right;
                    int bottom = MouseImage.DestRect.Bottom;
                    if ((DragType == ImageInfo.HitTypes.NwCorner) ||
                        (DragType == ImageInfo.HitTypes.SwCorner))
                        MouseImage.DestRect.X = right - new_wid;
                    if ((DragType == ImageInfo.HitTypes.NwCorner) ||
                        (DragType == ImageInfo.HitTypes.NeCorner))
                        MouseImage.DestRect.Y = bottom - new_hgt;
                    MouseImage.DestRect.Width = new_wid;
                    MouseImage.DestRect.Height = new_hgt;
                }

                // Redraw.
                pictureBox1.Refresh();
            }
        }

        // Set the correct mouse cursor.
        private void SetMouseCursor(Point point)
        {
            // See if the mouse is over an image.
            FindImageAt(point, out MouseImage, out MouseHitType);

            switch (MouseHitType)
            {
                case ImageInfo.HitTypes.None:
                    pictureBox1.Cursor = Cursors.Default;
                    break;
                case ImageInfo.HitTypes.Body:
                    pictureBox1.Cursor = Cursors.SizeAll;
                    break;
                case ImageInfo.HitTypes.NwCorner:
                case ImageInfo.HitTypes.SeCorner:
                    pictureBox1.Cursor = Cursors.SizeNWSE;
                    break;
                case ImageInfo.HitTypes.NeCorner:
                case ImageInfo.HitTypes.SwCorner:
                    pictureBox1.Cursor = Cursors.SizeNESW;
                    break;
            }
        }

        // Start dragging a corner or an image.
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            // If we're not over anything, do nothing.
            if (MouseHitType == ImageInfo.HitTypes.None) return;

            // Bring the image to the top.
            Images.Remove(MouseImage);
            Images.Add(MouseImage);
            pictureBox1.Refresh();

            // Save the location and drag type.
            StartPoint = e.Location;
            StartRect = MouseImage.DestRect;
            DragType = MouseHitType;
        }

        // Stop dragging.
        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            DragType = ImageInfo.HitTypes.None;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // Remove all images.
            Images = new List<ImageInfo>();
            pictureBox1.Refresh();
        }

        // Select images to add to the montage.
        // Note that I set the dialog's Multiselect property
        // to True at design time.
        private void button2_Click(object sender, EventArgs e)
        {
            string filename1 = @"C:\______test_files\__pic\_書畫字圖\_peony1\p1.jpg";
            string filename2 = @"C:\______test_files\__pic\_書畫字圖\_peony1\p2.jpg";
            string filename3 = @"C:\______test_files\__pic\_書畫字圖\_peony1\p3.jpg";
            string filename4 = @"C:\______test_files\__pic\_書畫字圖\_peony1\p4.jpg";
            string filename5 = @"C:\______test_files\__pic\_書畫字圖\_peony1\p5.jpg";

            ImageInfo image;
            image = new ImageInfo(filename1);
            Images.Add(image);
            image = new ImageInfo(filename2);
            Images.Add(image);
            image = new ImageInfo(filename3);
            Images.Add(image);
            image = new ImageInfo(filename4);
            Images.Add(image);
            image = new ImageInfo(filename5);
            Images.Add(image);

            pictureBox1.Refresh();
        }

        // Save the result in a file.
        private void button3_Click(object sender, EventArgs e)
        {
            // Make a Bitmap to hold the result.
            using (Bitmap bitmap1 = new Bitmap(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height))
            {
                // Draw the pictures.
                using (Graphics gr = Graphics.FromImage(bitmap1))
                {
                    DrawPictures(gr, false);
                }

                if (bitmap1 != null)
                {
                    string filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                    String filename1 = filename + ".jpg";
                    String filename2 = filename + ".bmp";
                    String filename3 = filename + ".png";

                    // Save the file.
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
        }

        // Let the user set the PictureBox's background color.
        private void button4_Click(object sender, EventArgs e)
        {
            colorDialog1.Color = pictureBox1.BackColor;
            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                pictureBox1.BackColor = colorDialog1.Color;
            }
        }

        private void SetupPictureScale(object sender, EventArgs e)
        {
            float scale;
            if (radioButton1.Checked == true)
                scale = 1;
            else if (radioButton2.Checked == true)
                scale = 0.75f;
            else if (radioButton3.Checked == true)
                scale = 0.50f;
            else if (radioButton4.Checked == true)
                scale = 0.25f;
            else
                scale = 1;

            foreach (ImageInfo info in Images)
            {
                info.DestRect = new Rectangle(
                    info.DestRect.X,
                    info.DestRect.Y,
                    (int)(info.SourceRect.Width * scale),
                    (int)(info.SourceRect.Height * scale));
            }
            pictureBox1.Refresh();
        }

    }
}
