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


namespace vcs_PictureCropA
{
    public partial class Form1 : Form
    {
        private List<Point> Points = null;
        private bool flag_select_area = false;  //開始選取的旗標
        private Bitmap bitmap1 = null;  //原圖位圖Bitmap

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\bear.jpg";
            bitmap1 = new Bitmap(filename);
            pictureBox1.Image = bitmap1;

            pictureBox1.MouseDown += new MouseEventHandler(pictureBox1_MouseDown);
            pictureBox1.MouseMove += new MouseEventHandler(pictureBox1_MouseMove);
            pictureBox1.MouseUp += new MouseEventHandler(pictureBox1_MouseUp);
            pictureBox1.Paint += new PaintEventHandler(pictureBox1_Paint);
        }

        void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            Points = new List<Point>();
            flag_select_area = true;
        }

        void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_select_area == false)
                return;
            Points.Add(new Point(e.X, e.Y));
            pictureBox1.Invalidate();
        }

        void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            flag_select_area = false;

            richTextBox1.Text += "點數 : " + Points.Count.ToString() + "\n";
        }

        void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            if ((Points != null) && (Points.Count > 1))
            {
                using (Pen dashed_pen = new Pen(Color.Red))
                {
                    dashed_pen.DashPattern = new float[] { 5, 5 };
                    e.Graphics.DrawLines(Pens.White, Points.ToArray());
                    e.Graphics.DrawLines(dashed_pen, Points.ToArray());
                }
            }

        }

        private void button0_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            /*
            if ((Points == null) || (Points.Count <= 1))
                return;
            */

            //擷取不規則區域, 使用Point一維陣列

            Points = new List<Point>();
            Points.Clear();
            int x_st = 0;
            int y_st = 0;
            Points.Add(new Point(x_st, y_st));
            Points.Add(new Point(x_st + 130, y_st));
            Points.Add(new Point(x_st + 130, y_st + 100));
            Points.Add(new Point(x_st + 65, y_st + 250));
            Points.Add(new Point(x_st + 0, y_st + 100));
            Points.Add(new Point(x_st, y_st));

            richTextBox1.Text += "點數 : " + Points.Count.ToString() + "\n";
            int len = Points.Count;

            Graphics g = Graphics.FromImage(bitmap1);
            g.DrawRectangle(Pens.Red, 100, 100, 100, 100);

            Rectangle rect = new Rectangle(570, 60, 130, 150);
            g.DrawRectangle(Pens.Red, rect);

            Pen dashed_pen = new Pen(Color.Red);
            dashed_pen.DashPattern = new float[] { 5, 5 };
            g.DrawLines(Pens.White, Points.ToArray());
            g.DrawLines(dashed_pen, Points.ToArray());

            pictureBox1.Image = bitmap1;

            //gr.FillPolygon(br, points.ToArray());

            // Add a PNG with a transparent background to the DataObject.
            Bitmap bm_transparent = GetSelectedArea(pictureBox1.Image, Color.Transparent, Points);
            pictureBox2.Image = bm_transparent;


            /*

            MemoryStream ms = new MemoryStream();
            bm_transparent.Save(ms, ImageFormat.Png);
            data_object.SetData("PNG", false, ms);

            // Place the data on the clipboard.
            Clipboard.Clear();
            Clipboard.SetDataObject(data_object, true);
            richTextBox1.Text += "已選擇區域複製至剪貼簿\n";
            */




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
                if (xmin > points[i].X)
                {
                    xmin = points[i].X;
                }
                if (xmax < points[i].X)
                {
                    xmax = points[i].X;
                }
                if (ymin > points[i].Y)
                {
                    ymin = points[i].Y;
                }
                if (ymax < points[i].Y)
                {
                    ymax = points[i].Y;
                }
            }

            Rectangle rect = new Rectangle(xmin, ymin, xmax - xmin, ymax - ymin);
            richTextBox1.Text += rect.ToString() + "\n";

            return new Rectangle(xmin, ymin, xmax - xmin, ymax - ymin);
        }


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

                    gr.FillRectangle(br,new Rectangle(100,100,100,100));

                    // Find the bounds of the selected area.
                    Rectangle source_rect = GetPointListBounds(points);//取得擴大矩形

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



    }
}
