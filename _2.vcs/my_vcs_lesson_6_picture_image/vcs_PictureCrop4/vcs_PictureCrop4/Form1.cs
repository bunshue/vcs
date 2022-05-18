using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for GraphicsPath
using System.Drawing.Imaging;
using System.IO;

namespace vcs_PictureCrop4
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void mnuFileOpen_Click(object sender, EventArgs e)
        {
            openFileDialog1.InitialDirectory = @"C:\______test_files\";
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
                try
                {
                    // Load the image.
                    picSource.Image = LoadUnlocked(openFileDialog1.FileName);
                    picSource.Visible = true;
                    picArea.Image = null;
                    picWithoutArea.Image = null;

                    // Disable the Save menu items.
                    mnuFileSaveArea.Enabled = false;
                    mnuFileSaveWithoutArea.Enabled = false;

                    // Arrange the PictureBoxes.
                    int gap = picSource.Left;
                    picArea.Size = picSource.Size;
                    picArea.Left = picSource.Right + gap;
                    picArea.Visible = true;

                    picWithoutArea.Size = picSource.Size;
                    picWithoutArea.Left = picArea.Right + gap;
                    picWithoutArea.Visible = true;

                    // Make the form big enough.
                    int width = Math.Max(ClientSize.Width,
                        picWithoutArea.Right + gap);
                    int height = Math.Max(ClientSize.Height,
                        picSource.Bottom + gap);
                    this.ClientSize = new Size(width, height);
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message);
                }
        }

        // For selecting an area.
        private List<Point> Points = null;
        private bool Drawing = false;

        // Start selecting an area.
        private void picSource_MouseDown(object sender, MouseEventArgs e)
        {
            Points = new List<Point>();
            Drawing = true;
        }

        // Continue selecting the area.
        private void picSource_MouseMove(object sender, MouseEventArgs e)
        {
            if (!Drawing) return;
            Points.Add(new Point(e.X, e.Y));
            picSource.Invalidate();
        }

        // Stop selecting the area.
        private void picSource_MouseUp(object sender, MouseEventArgs e)
        {
            Drawing = false;
            mnuFileSaveArea.Enabled = true;
            mnuFileSaveWithoutArea.Enabled = true;
            if (Points == null) return;

            // Make the image with only the area.
            Bitmap with_area_bitmap =
                MakeImageWithArea((Bitmap)picSource.Image, Points);
            picArea.Image = MakeSampleImage(with_area_bitmap);

            // Make the image without the area.
            Bitmap without_area_bitmap =
                MakeImageWithoutArea((Bitmap)picSource.Image, Points);
            picWithoutArea.Image = MakeSampleImage(without_area_bitmap);
        }

        // Make an image that includes only the selected area.
        private Bitmap MakeImageWithArea(Bitmap source_bm, List<Point> points)
        {
            // Copy the image.
            Bitmap bm = new Bitmap(source_bm.Width, source_bm.Height);

            // Clear the selected area.
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.Clear(Color.Transparent);

                // Make a brush that contains the original image.
                using (Brush brush = new TextureBrush(source_bm))
                {
                    // Fill the selected area.
                    gr.FillPolygon(brush, points.ToArray());
                }
            }
            return bm;
        }

        // Make an image that includes only the selected area.
        private Bitmap MakeImageWithoutArea(Bitmap source_bm, List<Point> points)
        {
            // Copy the image.
            Bitmap bm = new Bitmap(source_bm);

            // Clear the selected area.
            using (Graphics gr = Graphics.FromImage(bm))
            {
                GraphicsPath path = new GraphicsPath();
                path.AddPolygon(points.ToArray());
                gr.SetClip(path);
                gr.Clear(Color.Transparent);
                gr.ResetClip();
            }
            return bm;
        }

        // Make a sample showing transparent areas.
        private Bitmap MakeSampleImage(Bitmap bitmap)
        {
            const int box_wid = 20;
            const int box_hgt = 20;

            Bitmap bm = new Bitmap(bitmap.Width, bitmap.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                // Start with a checkerboard pattern.
                gr.Clear(Color.White);
                int num_rows = bm.Height / box_hgt;
                int num_cols = bm.Width / box_wid;
                for (int row = 0; row < num_rows; row++)
                {
                    int y = row * box_hgt;
                    for (int col = 0; col < num_cols; col++)
                    {
                        int x = 2 * col * box_wid;
                        if (row % 2 == 1) x += box_wid;
                        gr.FillRectangle(Brushes.LightBlue,
                            x, y, box_wid, box_hgt);
                    }
                }

                // Draw the image on top.
                gr.DrawImageUnscaled(bitmap, 0, 0);
            }
            return bm;
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

        private void mnuFileSaveArea_Click(object sender, EventArgs e)
        {
            //自動檔名 與 存檔語法
            string filename = Application.StartupPath + "\\bmp_area_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

            try
            {
                ((Bitmap)picArea.Image).Save(filename, ImageFormat.Bmp);

                //richTextBox1.Text += "已存檔 : " + filename + "\n";
            }
            catch (Exception ex)
            {
                //richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
        }

        private void mnuFileSaveWithoutArea_Click(object sender, EventArgs e)
        {
            //自動檔名 與 存檔語法
            string filename = Application.StartupPath + "\\bmp_wo_area_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

            try
            {
                ((Bitmap)picWithoutArea.Image).Save(filename, ImageFormat.Bmp);
                //richTextBox1.Text += "已存檔 : " + filename + "\n";
            }
            catch (Exception ex)
            {
                //richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
        }

        private void mnuFileExit_Click(object sender, EventArgs e)
        {
            Close();
        }

        // Return a bitmap without locking its file.
        private Bitmap LoadUnlocked(string file_name)
        {
            using (Bitmap bm = (Bitmap)Image.FromFile(file_name))
            {
                return new Bitmap(bm);
            }
        }
    }
}

