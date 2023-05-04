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
using System.Drawing.Drawing2D; //for GraphicsPath

namespace vcs_PictureCrop4
{
    public partial class Form1 : Form
    {
        // For selecting an area.
        private List<Point> Points = null;
        private bool flag_mouse_down = false;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }


        // Start selecting an area.
        private void picSource_MouseDown(object sender, MouseEventArgs e)
        {
            Points = new List<Point>();
            flag_mouse_down = true;
        }

        // Continue selecting the area.
        private void picSource_MouseMove(object sender, MouseEventArgs e)
        {
            if (!flag_mouse_down)
            {
                return;
            }
            Points.Add(new Point(e.X, e.Y));
            picSource.Invalidate();
        }

        // Stop selecting the area.
        private void picSource_MouseUp(object sender, MouseEventArgs e)
        {
            flag_mouse_down = false;
            if (Points == null)
            {
                return;
            }

            // Make the image with only the area.
            Bitmap bitmap_with = MakeImageWithArea((Bitmap)picSource.Image, Points);
            picArea.Image = MakeSampleImage(bitmap_with);

            // Make the image without the area.
            Bitmap bitmap_without = MakeImageWithoutArea((Bitmap)picSource.Image, Points);
            picWithoutArea.Image = MakeSampleImage(bitmap_without);
        }

        // Make an image that includes only the selected area.
        private Bitmap MakeImageWithArea(Bitmap bmp, List<Point> points)
        {
            // Copy the image.
            Bitmap bitmap1 = new Bitmap(bmp.Width, bmp.Height);

            // Clear the selected area.
            using (Graphics g = Graphics.FromImage(bitmap1))
            {
                g.Clear(Color.Transparent);

                // Make a brush that contains the original image.
                using (Brush brush = new TextureBrush(bmp))
                {
                    // Fill the selected area.
                    g.FillPolygon(brush, points.ToArray());
                }
            }
            return bitmap1;
        }

        // Make an image that includes only the selected area.
        private Bitmap MakeImageWithoutArea(Bitmap bmp, List<Point> points)
        {
            // Copy the image.
            Bitmap bitmap1 = new Bitmap(bmp);

            // Clear the selected area.
            using (Graphics g = Graphics.FromImage(bitmap1))
            {
                GraphicsPath path = new GraphicsPath();
                path.AddPolygon(points.ToArray());
                g.SetClip(path);
                g.Clear(Color.Transparent);
                g.ResetClip();
            }
            return bitmap1;
        }

        // Make a sample showing transparent areas.
        private Bitmap MakeSampleImage(Bitmap bmp)
        {
            const int box_wid = 20;
            const int box_hgt = 20;

            Bitmap bitmap1 = new Bitmap(bmp.Width, bmp.Height);
            using (Graphics g = Graphics.FromImage(bitmap1))
            {
                // Start with a checkerboard pattern.
                g.Clear(Color.White);
                int num_rows = bitmap1.Height / box_hgt;
                int num_cols = bitmap1.Width / box_wid;
                for (int row = 0; row < num_rows; row++)
                {
                    int y = row * box_hgt;
                    for (int col = 0; col < num_cols; col++)
                    {
                        int x = 2 * col * box_wid;
                        if (row % 2 == 1) x += box_wid;
                        g.FillRectangle(Brushes.LightBlue, x, y, box_wid, box_hgt);
                    }
                }

                // Draw the image on top.
                g.DrawImageUnscaled(bmp, 0, 0);
            }
            return bitmap1;
        }

        // Draw the current selection if there is one.
        private void picSource_Paint(object sender, PaintEventArgs e)
        {
            if ((Points != null) && (Points.Count > 1))
            {
                using (Pen dashed_pen = new Pen(Color.Black))
                {
                    dashed_pen.DashPattern = new float[] { 5, 5 };
                    e.Graphics.DrawLines(Pens.White, Points.ToArray());
                    e.Graphics.DrawLines(dashed_pen, Points.ToArray());
                }
            }
        }

        // Return a bitmap without locking its file.
        private Bitmap LoadUnlocked(string file_name)
        {
            using (Bitmap bitmap1 = (Bitmap)Image.FromFile(file_name))
            {
                return new Bitmap(bitmap1);
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files1\picture1.jpg";

            try
            {
                // Load the image.
                picSource.Image = LoadUnlocked(filename);
                picSource.Visible = true;
                picArea.Image = null;
                picWithoutArea.Image = null;

                // Arrange the PictureBoxes.
                int gap = picSource.Left;
                picArea.Size = picSource.Size;
                picArea.Left = picSource.Right + gap;
                picArea.Visible = true;

                picWithoutArea.Size = picSource.Size;
                picWithoutArea.Left = picArea.Right + gap;
                picWithoutArea.Visible = true;

                // Make the form big enough.
                int width = Math.Max(ClientSize.Width, picWithoutArea.Right + gap);
                int height = Math.Max(ClientSize.Height, picSource.Bottom + gap);
                this.ClientSize = new Size(width, height);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //自動檔名 與 存檔語法
            string filename1 = Application.StartupPath + "\\bmp_area_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
            string filename2 = Application.StartupPath + "\\bmp_wo_area_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

            try
            {
                ((Bitmap)picArea.Image).Save(filename1, ImageFormat.Bmp);

                //richTextBox1.Text += "已存檔 : " + filename + "\n";
            }
            catch (Exception ex)
            {
                //richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }

            try
            {
                ((Bitmap)picWithoutArea.Image).Save(filename2, ImageFormat.Bmp);
                //richTextBox1.Text += "已存檔 : " + filename + "\n";
            }
            catch (Exception ex)
            {
                //richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
        }
    }
}



