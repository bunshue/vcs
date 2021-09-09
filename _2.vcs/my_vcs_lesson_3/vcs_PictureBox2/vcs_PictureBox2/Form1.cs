using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_PictureBox2
{
    public partial class Form1 : Form
    {
        private string image_filename;
        int W = 0;
        int H = 0;
        int w = 0;
        int h = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";
            image_filename = filename;
            Image image = Image.FromFile(filename);
            pictureBox1.Image = image;
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.Location = new Point((W - w) / 2, (H - h) / 2);

            //pictureBox1.Size = new Size(image.Width, image.Height);

            this.pictureBox1.MouseWheel += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseWheel);

            pictureBox1.AllowDrop = true;


            W = this.Width;
            H = this.Height;
            w = image.Width;
            h = image.Height;
        }

        private void pictureBox1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                this.Text = "全螢幕顯示圖片";
                pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
                pictureBox1.Size = new Size(W, H);
                pictureBox1.Location = new Point(0, 0);
            }

            if (e.Button == MouseButtons.Right)
            {
                this.Text = "原始比例顯示圖片";
                pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
                pictureBox1.Size = new Size(w, h);
                pictureBox1.Location = new Point((W - w) / 2, (H - h) / 2);
            }


        }

        private void pictureBox1_PreviewKeyDown(object sender, PreviewKeyDownEventArgs e)
        {
            //this.Text = "pictureBox1_PreviewKeyDown";
            if ((e.KeyCode == Keys.Right) || (e.KeyCode == Keys.Down))
            {
                this.Text = "pictureBox1_PreviewKeyDown 右 下, 下一張";
                //OpenNextFile(image_filename);
            }
            else if ((e.KeyCode == Keys.Left) || (e.KeyCode == Keys.Up))
            {
                this.Text = "pictureBox1_PreviewKeyDown 左 上, 上一張";
                //OpenPreviousFile(image_filename);
            }


        }

        int ratio = 10;
        private void pictureBox1_MouseWheel(object sender, MouseEventArgs e)
        {
            int ww = 0;
            int hh = 0;
            if (e.Delta > 0)
            {
                ratio++;
                if (ratio > 20)
                    ratio = 20;
                this.Text = "放大 " + ratio.ToString();


            }
            else
            {
                ratio--;
                if (ratio < 5)
                    ratio = 5;
                this.Text = "縮小 " + ratio.ToString();
            }

            ww = w * ratio / 10;
            hh = h * ratio / 10;

            pictureBox1.Size = new Size(ww, hh);
            pictureBox1.Location = new Point((W - ww) / 2, (H - hh) / 2);

        }

        int pictureBox1_position_x_old = 0;
        int pictureBox1_position_y_old = 0;
        bool flag_pictureBox1_mouse_down = false;

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            flag_pictureBox1_mouse_down = true;
            //this.Text = "Down : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
            pictureBox1_position_x_old = e.X;
            pictureBox1_position_y_old = e.Y;
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_pictureBox1_mouse_down == true)
            {
                //this.Text = "Up : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
                int dx = e.X - pictureBox1_position_x_old;
                int dy = e.Y - pictureBox1_position_y_old;

                //this.Text = "dx, dy : (" + dx.ToString() + ", " + dy.ToString() + ")\n";
                pictureBox1.Location = new Point(pictureBox1.Location.X + dx, pictureBox1.Location.Y + dy);
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            flag_pictureBox1_mouse_down = false;
            //this.Text = "Up : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
            int dx = e.X - pictureBox1_position_x_old;
            int dy = e.Y - pictureBox1_position_y_old;

            //this.Text = "dx, dy : (" + dx.ToString() + ", " + dy.ToString() + ")\n";
            pictureBox1.Location = new Point(pictureBox1.Location.X + dx, pictureBox1.Location.Y + dy);

        }





    }
}
