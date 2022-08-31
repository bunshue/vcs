using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Drawing2D;
using System.Drawing.Imaging;

namespace howto_redeye_reduction
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void mnuFileExit_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        // Open a file.
        Bitmap TheBitmap;
        private void mnuFileOpen_Click(object sender, EventArgs e)
        {
            if (ofdImage.ShowDialog() == DialogResult.OK)
            {
                using (Bitmap bm = new Bitmap(ofdImage.FileName))
                {
                    TheBitmap = new Bitmap(bm);
                }
                picImage.Image = TheBitmap;
                this.ClientSize = new Size(
                    picImage.Right + picImage.Left,
                    picImage.Bottom + picImage.Left);
                picImage.Visible = true;
            }
        }

        // Save the file.
        private void mnuFileSaveAs_Click(object sender, EventArgs e)
        {
            if (sfdImage.ShowDialog() == DialogResult.OK)
            {
                SaveBitmapUsingExtension(TheBitmap, sfdImage.FileName);
            }
        }

        // Save the file with the appropriate format.
        // Throw a NotSupportedException if the file
        // has an unknown extension.
        public void SaveBitmapUsingExtension(Bitmap bm, string filename)
        {
            string extension = Path.GetExtension(filename);
            switch (extension.ToLower())
            {
                case ".bmp":
                    bm.Save(filename, ImageFormat.Bmp);
                    break;
                case ".exif":
                    bm.Save(filename, ImageFormat.Exif);
                    break;
                case ".gif":
                    bm.Save(filename, ImageFormat.Gif);
                    break;
                case ".jpg":
                case ".jpeg":
                    bm.Save(filename, ImageFormat.Jpeg);
                    break;
                case ".png":
                    bm.Save(filename, ImageFormat.Png);
                    break;
                case ".tif":
                case ".tiff":
                    bm.Save(filename, ImageFormat.Tiff);
                    break;
                default:
                    throw new NotSupportedException(
                        "Unknown file extension " + extension);
            }
        }

        // Let the user click and drag to select an area.
        private int StartX, StartY;
        private bool Drawing = false;
        private void picImage_MouseDown(object sender, MouseEventArgs e)
        {
            Drawing = true;
            StartX = e.X;
            StartY = e.Y;
        }
        private void picImage_MouseMove(object sender, MouseEventArgs e)
        {
            if (!Drawing) return;
            Bitmap temp_bm = new Bitmap(TheBitmap);
            using (Graphics gr = Graphics.FromImage(temp_bm))
            {
                using (Pen dashed_pen = new Pen(Color.Black, 0))
                {
                    dashed_pen.DashStyle = DashStyle.Dash;
                    gr.DrawRectangle(dashed_pen,
                        Math.Min(StartX, e.X),
                        Math.Min(StartY, e.Y),
                        Math.Abs(StartX - e.X),
                        Math.Abs(StartY - e.Y));
                }
            }
            picImage.Image = temp_bm;
        }
        private void picImage_MouseUp(object sender, MouseEventArgs e)
        {
            if (!Drawing) return;
            Drawing = false;

            // Process the selected area.
            Rectangle rect = new Rectangle(
                Math.Min(StartX, e.X),
                Math.Min(StartY, e.Y),
                Math.Abs(StartX - e.X),
                Math.Abs(StartY - e.Y));
            RemoveRedEye(TheBitmap, rect);
            picImage.Image = TheBitmap;
            picImage.Refresh();
        }

        // Remove redeye in the rectangle.
        private void RemoveRedEye(Bitmap bm, Rectangle rect)
        {
            for (int y = rect.Top; y <= rect.Bottom; y++)
            {
                for (int x = rect.Left; x <= rect.Right; x++)
                {
                    // See if it has more red than green and blue.
                    Color clr = bm.GetPixel(x, y);
                    if ((clr.R > clr.G) && (clr.R > clr.B))
                    {
                        // Convert to grayscale.
                        byte new_clr = (byte)((clr.R + clr.G + clr.B) / 3);
                        bm.SetPixel(x, y, Color.FromArgb(new_clr, new_clr, new_clr));
                    }
                }
            }
        }
    }
}
