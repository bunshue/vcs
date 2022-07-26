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
        Bitmap bitmap1; //原圖
        Bitmap bitmap2; //畫臨時框
        string filename = @"C:\______test_files\elephant.jpg";

        private Point point_st;
        private Point point_sp;
        private Graphics g;

        private Rectangle select_rectangle = new Rectangle(new Point(0, 0), new Size(0, 0));    //用來保存截圖的矩形

        private float PictureScale = 1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            pictureBox1.Image = bitmap1;

            pictureBox1.MouseDown += pictureBox1_MouseDown;
            pictureBox1.MouseMove += pictureBox1_MouseMove;
            pictureBox1.MouseUp += pictureBox1_MouseUp;
            pictureBox1.Cursor = Cursors.Cross;
        }

        private Rectangle MakeRectangle(Point pt1, Point pt2)
        {
            return new Rectangle(Math.Min(pt1.X, pt2.X), Math.Min(pt1.Y, pt2.Y), Math.Abs(pt1.X - pt2.X), Math.Abs(pt1.Y - pt2.Y));
        }

        private bool flag_mouse_down = false;
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

                select_rectangle = MakeRectangle(point_st, point_sp);

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

                nud_x_st.Value = (decimal)x_st;
                nud_y_st.Value = (decimal)y_st;
                nud_w.Value = (decimal)W;
                nud_h.Value = (decimal)H;
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

            this.Text = "選取區域 : " + select_rectangle.ToString();
                 
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
