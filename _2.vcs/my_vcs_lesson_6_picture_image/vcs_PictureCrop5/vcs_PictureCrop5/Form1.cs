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

        private float PictureScale = 1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label1.Text = "";

            pictureBox1.Image = Image.FromFile(filename);

            bitmap1 = new Bitmap(filename);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "W = " + pictureBox1.Image.Width.ToString() + ", H = " + pictureBox1.Image.Height.ToString() + "\n";

            button1.Text = "擷取中";

            pictureBox1.Image = bitmap1;
            pictureBox1.MouseDown += pictureBox1_MouseDown;
            pictureBox1.Cursor = Cursors.Cross;
        }

        private Point point_st;
        private Point point_sp;
        private Graphics g;
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            richTextBox1.Text += "pictureBox1_MouseDown\n";
            point_st = e.Location;
            pictureBox1.MouseDown -= pictureBox1_MouseDown;
            pictureBox1.MouseMove += pictureBox1_MouseMove;
            pictureBox1.MouseUp += pictureBox1_MouseUp;

            bitmap2 = (Bitmap)bitmap1.Clone();
            g = Graphics.FromImage(bitmap2);
            pictureBox1.Image = bitmap2;
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            //richTextBox1.Text += "pictureBox1_MouseMove\n";

            // Save the new point.
            point_sp = e.Location;

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

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            richTextBox1.Text += "pictureBox1_MouseUp\n";

            pictureBox1.MouseMove -= pictureBox1_MouseMove;
            pictureBox1.MouseUp -= pictureBox1_MouseUp;
            pictureBox1.Image = bitmap1;
            pictureBox1.Cursor = Cursors.Default;
            pictureBox1.Refresh();

            float x_st = Math.Min(point_st.X, point_sp.X) * PictureScale;
            float y_st = Math.Min(point_st.Y, point_sp.Y) * PictureScale;
            float W = Math.Abs(point_st.X - point_sp.X) * PictureScale;
            float H = Math.Abs(point_st.Y - point_sp.Y) * PictureScale;
            label1.Text = "擷取 x = " + x_st.ToString() + ", y = " + y_st.ToString() + ", W = " + W.ToString() + ", H = " + H.ToString();
            button1.Text = "擷取";

            Bitmap bitmap1b = (Bitmap)bitmap1.Clone();
            Graphics g = Graphics.FromImage(bitmap1b);
            g.DrawRectangle(Pens.Red, x_st, y_st, W, H);
            pictureBox1.Image = bitmap1b;
        }
    }
}


