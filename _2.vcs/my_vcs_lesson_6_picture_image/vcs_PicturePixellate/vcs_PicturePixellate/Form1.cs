using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_PicturePixellate
{
    public partial class Form1 : Form
    {
        // Select an area.
        private Point pt_st = Point.Empty;//記錄鼠標按下時的坐標，用來確定繪圖起點
        private Point pt_sp = Point.Empty;//記錄鼠標放開時的坐標，用來確定繪圖終點
        private int StartX = -1, StartY = -1;
        private Bitmap BoxBitmap = null;
        private Graphics BoxGraphics = null;

        // The current image without the rubberband rectangle.
        private Bitmap CurrentBitmap = null;

        string filename = "C:\\______test_files\\elephant.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            ClientSize = new Size(pictureBox1.Right + pictureBox1.Left + 150, pictureBox1.Bottom + pictureBox1.Left); //表單跟圖片框一樣大

            try
            {
                using (Bitmap bitmap1 = new Bitmap(filename))
                {
                    CurrentBitmap = bitmap1.Clone() as Bitmap;
                    pictureBox1.Image = bitmap1.Clone() as Image;
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        // Return a Rectangle with these points as corners.
        private Rectangle MakeRectangle(int x0, int y0, int x1, int y1)
        {
            return new Rectangle(Math.Min(x0, x1), Math.Min(y0, y1), Math.Abs(x0 - x1), Math.Abs(y0 - y1));
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            if (CurrentBitmap == null)
                return;

            pt_st = e.Location;
            StartX = e.X;
            StartY = e.Y;

            // Make the selected image.
            BoxBitmap = new Bitmap(CurrentBitmap);
            BoxGraphics = Graphics.FromImage(BoxBitmap);
            pictureBox1.Image = BoxBitmap;
        }

        // Continue selecting the area.
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (StartX < 0)
                return;

            // Restore the current image.
            BoxGraphics.DrawImage(CurrentBitmap, 0, 0);

            // Draw the selection rectangle.
            using (Pen select_pen = new Pen(Color.Red))
            {
                select_pen.DashStyle = System.Drawing.Drawing2D.DashStyle.Dash;
                Rectangle rect = MakeRectangle(StartX, StartY, e.X, e.Y);
                BoxGraphics.DrawRectangle(select_pen, rect);
            }
            pictureBox1.Refresh();
        }

        // Pixellate the selected area and save the result.
        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            if (StartX < 0)
                return;

            PixellateRectangle(MakeRectangle(StartX, StartY, e.X, e.Y));

            // Remember we're not selecting any more.
            StartX = -1;
            StartY = -1;
            BoxGraphics.Dispose();
            BoxGraphics = null;
            BoxBitmap.Dispose();
            BoxBitmap = null;
        }

        // Pixellate the indicated rectangle.
        private void PixellateRectangle(Rectangle rect)
        {
            // Restrict the rectangle to fit on the image.
            int W = CurrentBitmap.Width;
            int H = CurrentBitmap.Height;
            rect = Rectangle.Intersect(rect, new Rectangle(0, 0, W, H));

            // Process the rectangle.
            const int box_wid = 8;
            using (Graphics gr = Graphics.FromImage(CurrentBitmap))
            {
                int start_y = box_wid * (int)(rect.Top / box_wid);
                int start_x = box_wid * (int)(rect.Left / box_wid);
                for (int y = start_y; y <= rect.Bottom; y += box_wid)
                {
                    for (int x = start_x; x <= rect.Right; x += box_wid)
                    {
                        // Pixellate the area with upper left corner (x, y).

                        // Get the average of the pixels' color component values.
                        int total_r = 0, total_g = 0, total_b = 0, num_pixels = 0;
                        for (int dy = 0; dy < box_wid; dy++)
                        {
                            if (y + dy >= H) break;
                            for (int dx = 0; dx < box_wid; dx++)
                            {
                                if (x + dx >= W) break;
                                Color pixel_color = CurrentBitmap.GetPixel(x + dx, y + dy);
                                total_r += pixel_color.R;
                                total_g += pixel_color.G;
                                total_b += pixel_color.B;
                                num_pixels++;
                            }
                        }
                        byte r = (byte)(total_r / num_pixels);
                        byte g = (byte)(total_g / num_pixels);
                        byte b = (byte)(total_b / num_pixels);
                        Color new_color = Color.FromArgb(255, r, g, b);

                        // Give all pixels in the box this color.
                        using (Brush br = new SolidBrush(new_color))
                        {
                            gr.FillRectangle(br, x, y, box_wid, box_wid);
                        }
                    }
                }

                // Refresh to show the new image.
                pictureBox1.Image = CurrentBitmap;
                pictureBox1.Refresh();
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                using (Bitmap bitmap1 = new Bitmap(filename))
                {
                    CurrentBitmap = bitmap1.Clone() as Bitmap;
                    pictureBox1.Image = bitmap1.Clone() as Image;
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }
    }
}
