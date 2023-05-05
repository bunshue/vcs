using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;
using System.Drawing.Drawing2D; //for DashStyle

namespace vcs_PictureCrop5
{
    public partial class Form1 : Form
    {
        string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";

        private Point point_st;
        private Point point_sp;

        private bool flag_mouse_down = false;
        private Point pt_st = Point.Empty;//記錄鼠標按下時的坐標，用來確定繪圖起點
        private Point pt_sp = Point.Empty;//記錄鼠標放開時的坐標，用來確定繪圖終點
        private Bitmap bitmap1 = null;  //原圖位圖Bitmap
        private Bitmap bitmap2 = null;  //擷取部分位圖Bitmap
        private Rectangle SelectionRectangle = new Rectangle(new Point(0, 0), new Size(0, 0));    //用來保存截圖的矩形

        //private int W = 0;  //原圖的寬
        //private int H = 0;  //原圖的高
        //private int w = 0;  //擷取圖的寬
        //private int h = 0;  //擷取圖的高

        private Graphics g;
        private float PictureScale = 1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            pictureBox1.Image = bitmap1;


            int pbox_w = pictureBox1.ClientSize.Width;
            int pbox_h = pictureBox1.ClientSize.Height;
            int W = bitmap1.Width;
            int H = bitmap1.Height;

            float ratio_w = pbox_w / (float)W;
            float ratio_h = pbox_h / (float)H;

            if ((ratio_w >= 1) && (ratio_h >= 1))
            {
                PictureScale = Math.Min(ratio_w, ratio_h);
            }
            else if ((ratio_w <= 1) && (ratio_h <= 1))
            {
                PictureScale = Math.Min(ratio_w, ratio_h);
            }
            else if ((ratio_w >= 1) && (ratio_h < 1))
            {
                PictureScale = ratio_h;
            }
            else if ((ratio_w < 1) && (ratio_h >= 1))
            {
                PictureScale = ratio_w;
            }
            richTextBox1.Text += "PBOX :\t" + pbox_w.ToString() + "\t" + pbox_h.ToString() + "\n";
            richTextBox1.Text += "PICT :\t" + W.ToString() + "\t" + H.ToString() + "\n";
            richTextBox1.Text += "ratio :\t" + ratio_w.ToString() + "\t" + ratio_h.ToString() + "\n";
            richTextBox1.Text += "PictureScale :\t" + PictureScale.ToString() + "\n";
        }

        void show_item_location()
        {
            //跟隨鼠標在 pictureBox 的圖片上畫矩形
            pictureBox1.MouseDown += new MouseEventHandler(pictureBox1_MouseDown);
            pictureBox1.MouseMove += new MouseEventHandler(pictureBox1_MouseMove);
            pictureBox1.MouseUp += new MouseEventHandler(pictureBox1_MouseUp);
            pictureBox1.Cursor = Cursors.Cross;
        }

        // Return a Rectangle with these points as corners.
        private Rectangle MakeRectangle(int x0, int y0, int x1, int y1)
        {
            return new Rectangle(Math.Min(x0, x1), Math.Min(y0, y1), Math.Abs(x0 - x1), Math.Abs(y0 - y1));
        }

        private Rectangle MakeRectangle(Point pt1, Point pt2)
        {
            return new Rectangle(Math.Min(pt1.X, pt2.X), Math.Min(pt1.Y, pt2.Y), Math.Abs(pt1.X - pt2.X), Math.Abs(pt1.Y - pt2.Y));
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            flag_mouse_down = true;
            richTextBox1.Text += "pictureBox1_MouseDown\n";
            pictureBox1.Refresh();
            point_st = e.Location;

            bitmap2 = (Bitmap)bitmap1.Clone();
            g = Graphics.FromImage(bitmap2);
            pictureBox1.Image = bitmap2;
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_mouse_down == true)
            {
                //richTextBox1.Text += "pictureBox1_MouseMove\n";

                // Save the new point.
                point_sp = e.Location; //終點座標

                SelectionRectangle = MakeRectangle(point_st, point_sp);

                // Draw the selection rectangle.
                g.DrawImage(bitmap1, 0, 0); //恢復原圖
                float x_st = Math.Min(point_st.X, point_sp.X) * PictureScale;
                float y_st = Math.Min(point_st.Y, point_sp.Y) * PictureScale;
                float W = Math.Abs(point_st.X - point_sp.X) * PictureScale;
                float H = Math.Abs(point_st.Y - point_sp.Y) * PictureScale;
                Pen p = new Pen(Color.Red, 1 * PictureScale);
                p.DashStyle = DashStyle.Dash;
                g.DrawRectangle(p, x_st, y_st, W, H);   //畫上臨時框

                pictureBox1.Refresh();

            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            flag_mouse_down = false;

            richTextBox1.Text += "pictureBox1_MouseUp\n";

            float x_st = Math.Min(point_st.X, point_sp.X) * PictureScale;
            float y_st = Math.Min(point_st.Y, point_sp.Y) * PictureScale;
            float W = Math.Abs(point_st.X - point_sp.X) * PictureScale;
            float H = Math.Abs(point_st.Y - point_sp.Y) * PictureScale;

            Bitmap bitmap1b = (Bitmap)bitmap1.Clone();
            Graphics g = Graphics.FromImage(bitmap1b);
            g.DrawRectangle(Pens.Red, x_st, y_st, W, H);
            pictureBox1.Image = bitmap1b;

            Bitmap bitmap2 = new Bitmap((int)W, (int)H);
            Graphics g2 = Graphics.FromImage(bitmap2);

            //             擷取螢幕位置起點  自建bmp的位置起點     擷取大小
            g2.CopyFromScreen(this.Location.X + pictureBox1.Location.X + (int)x_st, this.Location.Y + pictureBox1.Location.Y + (int)y_st, 0, 0, new Size((int)W, (int)H));

            g2.Dispose();

            g.Dispose();

        }
    }
}
