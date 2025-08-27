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

namespace vcs_PictureMontageHex
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The height of a hexagon.
        private float HexHeight = 200;
        private float BorderThickness = 5;
 
        // Selected hexagons.
        private List<Hexagon> Hexagons = new List<Hexagon>();

        private int NumRows = 1, NumCols = 1;
        private Bitmap GridImage = null;

        // Draw the grid and its images.
        private void DrawGrid(Graphics gr, int xmax, int ymax)
        {
            gr.Clear(picBackgroundColor.BackColor);
            gr.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the selected hexagons.
            float xmin = BorderThickness / 2f;
            foreach (Hexagon hexagon in Hexagons)
            {
                PointF[] points = Hex.HexToPoints(HexHeight,
                    hexagon.Row, hexagon.Column, xmin, xmin);

                if (points[3].X > xmax) continue;
                if (points[4].Y > ymax) continue;

                Hex.DrawImageInPolygon(gr,
                    Hex.HexToPoints(HexHeight,
                        hexagon.Row, hexagon.Column, xmin, xmin),
                        hexagon.Picture);
            }

            // Draw the grid.
            using (Pen pen = new Pen(picBorderColor.BackColor, BorderThickness))
            {
                Hex.DrawHexGrid(gr, pen,
                    xmin, xmax, xmin, ymax, HexHeight);
            }
        }

        // Display the row and column under the mouse.
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            int row, col;
            Hex.PointToHex(e.X, e.Y, HexHeight, out row, out col);
            int index = FindHexagon(row, col);
            if (index < 0)
                this.Text = "vcs_PictureMontageHex";
            else
            {
                string name = Hexagons[index].FileName;
                int pos = name.IndexOf('.');
                this.Text = name.Substring(0, pos);
            }
        }

        // Add the clicked hexagon to the Hexagons list.
        private void pictureBox1_MouseClick(object sender, MouseEventArgs e)
        {
            // Get the row and column clicked.
            int row, col;
            Hex.PointToHex(e.X, e.Y, HexHeight, out row, out col);

            // Remove any existing record for this cell.
            RemoveHexagon(row, col);

            // Let the user select a new picture.
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                Bitmap bm = LoadBitmapUnlocked(openFileDialog1.FileName);
                Hexagons.Add(new Hexagon(row, col, bm, openFileDialog1.FileName));
            }

            // Redraw.
            MakeGrid();
        }

        // Remove the Hexagon at this position if there is one.
        private void RemoveHexagon(int row, int col)
        {
            int index = FindHexagon(row,col);
            if (index >= 0) Hexagons.RemoveAt(index);
        }

        // Find the Hexagon at this position if there is one.
        private int FindHexagon(int row, int col)
        {
            for (int i = Hexagons.Count - 1; i >= 0; i--)
            {
                if ((Hexagons[i].Row == row) &&
                    (Hexagons[i].Column == col))
                        return i;
            }
            return -1;
        }

        // A parameter changed. Update the drawing.
        private void txt_TextChanged(object sender, EventArgs e)
        {
            float height, thickness;
            if (!float.TryParse(txtHexHeight.Text, out height) ||
                height < 10)
                return;
            if (!float.TryParse(txtBorderThickness.Text, out thickness))
                return;

            HexHeight = height;
            BorderThickness = thickness;
            pictureBox1.Refresh();
        }

        // Save the file with the appropriate format.
        public void SaveImage(Image image, string filename)
        {
            string extension = Path.GetExtension(filename);
            switch (extension.ToLower())
            {
                case ".bmp":
                    image.Save(filename, ImageFormat.Bmp);
                    break;
                case ".exif":
                    image.Save(filename, ImageFormat.Exif);
                    break;
                case ".gif":
                    image.Save(filename, ImageFormat.Gif);
                    break;
                case ".jpg":
                case ".jpeg":
                    image.Save(filename, ImageFormat.Jpeg);
                    break;
                case ".png":
                    image.Save(filename, ImageFormat.Png);
                    break;
                case ".tif":
                case ".tiff":
                    image.Save(filename, ImageFormat.Tiff);
                    break;
                default:
                    throw new NotSupportedException(
                        "Unknown file extension " + extension);
            }
        }

        private void picBorderColor_Click(object sender, EventArgs e)
        {
            colorDialog1.Color = picBorderColor.BackColor;
            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                picBorderColor.BackColor = colorDialog1.Color;
                pictureBox1.Refresh();
            }
        }

        private void picBackgroundColor_Click(object sender, EventArgs e)
        {
            colorDialog1.Color = picBackgroundColor.BackColor;
            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                picBackgroundColor.BackColor = colorDialog1.Color;
                pictureBox1.Refresh();
            }
        }

        // See http://csharphelper.com/blog/2014/07/load-images-without-locking-their-files-in-c/
        // Load a bitmap without locking it.
        private Bitmap LoadBitmapUnlocked(string file_name)
        {
            using (Bitmap bm = new Bitmap(file_name))
            {
                return new Bitmap(bm);
            }
        }

        // Get the hexs' largest X and Y coordinates.
        private void FindGridBounds(out float xmax, out float ymax)
        {
            xmax = 0;
            ymax = 0;
            float xmin = BorderThickness / 2f;

            // Check hex (NumRows - 1, NumCols - 1).
            PointF[] points;
            points = Hex.HexToPoints(HexHeight,
                NumRows - 1, NumCols - 1, xmin, xmin);
            if (xmax < points[3].X) xmax = points[3].X;
            if (ymax < points[4].Y) ymax = points[4].Y;

            // Check hex (NumRows - 1, NumCols - 2).
            points = Hex.HexToPoints(HexHeight,
                NumRows - 1, NumCols - 1, xmin, xmin);
            if (xmax < points[3].X) xmax = points[3].X;
            if (ymax < points[4].Y) ymax = points[4].Y;

            // Add room for the border thickness.
            xmax += xmin;
            ymax += xmin;
        }

        // Make and display a new grid.
        private void MakeGrid()
        {
            // Get the number of rows and columns.
            if (!int.TryParse(txtNumRows.Text, out NumRows)) return;
            if (!int.TryParse(txtNumCols.Text, out NumCols)) return;

            // See how big the image must be.
            float xmax, ymax;
            FindGridBounds(out xmax, out ymax);

            // Make the image.
            int wid = (int)xmax + 1;
            int hgt = (int)ymax + 1;
            GridImage = new Bitmap(wid, hgt);

            // Draw the grid.
            using (Graphics gr = Graphics.FromImage(GridImage))
            {
                DrawGrid(gr, wid, hgt);
            }

            // Display the result.
            pictureBox1.Image = GridImage;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_MU";

            // Get a list of the files in the directory.
            DirectoryInfo dir_info = new DirectoryInfo(foldername);

            List<FileInfo> file_infos = new List<FileInfo>();
            foreach (FileInfo file_info in dir_info.GetFiles())
            {
                string ext = file_info.Extension.ToLower().Replace(".", "");
                if ((ext == "bmp") || (ext == "png") ||
                    (ext == "jpg") || (ext == "jpeg") ||
                    (ext == "gif") || (ext == "tiff"))
                {
                    file_infos.Add(file_info);
                }
            }

            // Calculate the number of rows and columns.
            int num_rows = (int)Math.Sqrt(file_infos.Count);
            int num_cols = num_rows;
            if (num_rows * num_cols < file_infos.Count)
                num_cols++;
            if (num_rows * num_cols < file_infos.Count)
                num_rows++;

            // Load the files.
            Hexagons = new List<Hexagon>();
            int index = 0;
            for (int row = 0; row < num_rows; row++)
            {
                for (int col = 0; col < num_cols; col++)
                {
                    string name = file_infos[index].Name;
                    string full_name = file_infos[index].FullName;
                    Bitmap bm = LoadBitmapUnlocked(full_name);
                    Hexagons.Add(new Hexagon(row, col, bm, name));

                    index++;
                    if (index >= file_infos.Count) break;
                }
                if (index >= file_infos.Count) break;
            }

            MakeGrid();


        }

        private void button2_Click(object sender, EventArgs e)
        {
            // Load the files from a directory.

            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_MU";

            DirectoryInfo dir_info = new DirectoryInfo(foldername);
            List<FileInfo> file_infos = new List<FileInfo>();
            foreach (FileInfo file_info in dir_info.GetFiles())
            {
                string ext = file_info.Extension.ToLower().Replace(".", "");
                if ((ext == "bmp") || (ext == "png") ||
                    (ext == "jpg") || (ext == "jpeg") ||
                    (ext == "gif") || (ext == "tiff"))
                {
                    file_infos.Add(file_info);
                }
            }

            // Calculate the number of rows and columns.
            int num_rows = (int)Math.Sqrt(file_infos.Count);
            int num_cols = num_rows;
            if (num_rows * num_cols < file_infos.Count)
                num_cols++;
            if (num_rows * num_cols < file_infos.Count)
                num_rows++;

            // Load the files.
            Hexagons = new List<Hexagon>();
            int index = 0;
            for (int row = 0; row < num_rows; row++)
            {
                for (int col = 0; col < num_cols; col++)
                {
                    string name = file_infos[index].Name;
                    string full_name = file_infos[index].FullName;
                    Bitmap bm = LoadBitmapUnlocked(full_name);
                    Hexagons.Add(new Hexagon(row, col, bm, name));

                    index++;
                    if (index >= file_infos.Count) break;
                }
                if (index >= file_infos.Count) break;
            }

            MakeGrid();

        }

        private void button3_Click(object sender, EventArgs e)
        {


            string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

            try
            {
                //bitmap1.Save(@file1, ImageFormat.Jpeg);
                //bitmap1.Save(filename, ImageFormat.Bmp);
                //bitmap1.Save(@file3, ImageFormat.Png);

                SaveImage(GridImage, filename);

                //richTextBox1.Text += "已存檔 : " + file1 + "\n";
                richTextBox1.Text += "已存檔 : " + filename + "\n";
                //richTextBox1.Text += "已存檔 : " + file3 + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }





        }



    }
}
