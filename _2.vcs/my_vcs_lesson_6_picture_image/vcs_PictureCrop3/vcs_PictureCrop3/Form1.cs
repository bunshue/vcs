using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat
using System.Drawing.Drawing2D;
using System.IO;

namespace vcs_PictureCrop3
{
    public partial class Form1 : Form
    {
        // For selecting an area.
        private List<Point> Points = null;

        private bool flag_select_area = false;  //開始選取的旗標
        private Point pt_st = Point.Empty;//記錄鼠標按下時的坐標，用來確定繪圖起點
        private Point pt_sp = Point.Empty;//記錄鼠標放開時的坐標，用來確定繪圖終點
        private Bitmap bitmap1 = null;  //原圖位圖Bitmap
        private Bitmap bitmap2 = null;  //擷取部分位圖Bitmap
        private Rectangle select_rectangle;//用來保存截圖的矩形

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\bear.jpg";

            bitmap1 = new Bitmap(filename);
            pictureBox1.Image = bitmap1;
        }

        // Return a Rectangle with these points as corners.
        private Rectangle MakeRectangle(int x0, int y0, int x1, int y1)
        {
            return new Rectangle(Math.Min(x0, x1), Math.Min(y0, y1), Math.Abs(x0 - x1), Math.Abs(y0 - y1));
        }

        // Start selecting an area.
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            Points = new List<Point>();
            flag_select_area = true;
        }

        // Continue selecting an area.
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_select_area == false)
                return;
            Points.Add(new Point(e.X, e.Y));
            pictureBox1.Invalidate();
        }

        // Finish selecting the area.
        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            flag_select_area = false;

            // Create a DataObject to hold data
            // in different formats.
            IDataObject data_object = new DataObject();

            // Add a BMP with a white background to the DataObject.
            Bitmap bm_white = GetSelectedArea(
                pictureBox1.Image, Color.White, Points);
            data_object.SetData(DataFormats.Bitmap, bm_white);

            // Add a PNG with a transparent background to the DataObject.
            Bitmap bm_transparent = GetSelectedArea(
                pictureBox1.Image, Color.Transparent, Points);
            MemoryStream ms = new MemoryStream();
            bm_transparent.Save(ms, ImageFormat.Png);
            data_object.SetData("PNG", false, ms);

            // Place the data on the clipboard.
            Clipboard.Clear();
            Clipboard.SetDataObject(data_object, true);
            richTextBox1.Text += "已選擇區域複製至剪貼簿\n";

            // Copy the selected area.
            bitmap2 = GetSelectedArea(pictureBox1.Image, Color.Transparent, Points);
        }

        // Draw the current selection if there is one.
        private void pictureBox1_Paint(object sender, PaintEventArgs e)
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

        // Return the bounds of the list of points.
        private Rectangle GetPointListBounds(List<Point> points)
        {
            int xmin = points[0].X;
            int xmax = xmin;
            int ymin = points[0].Y;
            int ymax = ymin;

            for (int i = 1; i < points.Count; i++)
            {
                if (xmin > points[i].X) xmin = points[i].X;
                if (xmax < points[i].X) xmax = points[i].X;
                if (ymin > points[i].Y) ymin = points[i].Y;
                if (ymax < points[i].Y) ymax = points[i].Y;
            }

            return new Rectangle(xmin, ymin, xmax - xmin, ymax - ymin);
        }

        // Copy the selected piece of the image into a new bitmap.
        private Bitmap GetSelectedArea(Image source, Color bg_color, List<Point> points)
        {
            // Make a new bitmap that has the background
            // color except in the selected area.
            Bitmap big_bm = new Bitmap(source);
            using (Graphics gr = Graphics.FromImage(big_bm))
            {
                // Set the background color.
                gr.Clear(bg_color);

                // Make a brush out of the original image.
                using (Brush br = new TextureBrush(source))
                {
                    // Fill the selected area with the brush.
                    gr.FillPolygon(br, points.ToArray());

                    // Find the bounds of the selected area.
                    Rectangle source_rect = GetPointListBounds(points);

                    // Make a bitmap that only holds the selected area.
                    Bitmap result = new Bitmap(source_rect.Width, source_rect.Height);

                    // Copy the selected area to the result bitmap.
                    using (Graphics result_gr = Graphics.FromImage(result))
                    {
                        Rectangle dest_rect = new Rectangle(0, 0,
                            source_rect.Width, source_rect.Height);
                        result_gr.DrawImage(big_bm, dest_rect, source_rect,
                            GraphicsUnit.Pixel);
                    }

                    // Return the result.
                    return result;
                }
            }
        }

        //貼上 定點
        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "把已選擇區域貼在圖的(100, 100)處\n";

            // Copy the selected area centered at the point clicked.
            // Do nothing if we haven't selected an area.
            if (bitmap2 == null)
                return;

            // See where to put it.
            //int x = e.X - bitmap2.Width / 2;
            //int y = e.Y - bitmap2.Height / 2;
            int x = 100;
            int y = 100;

            using (Graphics gr = Graphics.FromImage(pictureBox1.Image))
            {
                Rectangle source_rect = new Rectangle(0, 0,
                    bitmap2.Width, bitmap2.Height);
                Rectangle dest_rect = new Rectangle(x, y,
                    bitmap2.Width, bitmap2.Height);
                gr.DrawImage(bitmap2, dest_rect, source_rect,
                    GraphicsUnit.Pixel);
            }

            pictureBox1.Refresh();
        }

        // If the user presses Escape, cancel.
        private void Form1_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == 27)
            {

            }
        }

    }
}
