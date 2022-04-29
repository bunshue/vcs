using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_DragPicture9
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename1 = @"C:\______test_files\__pic\_peony1\p1.jpg";
            string filename2 = @"C:\______test_files\__pic\_peony1\p2.jpg";
            string filename3 = @"C:\______test_files\__pic\_peony1\p3.jpg";
            pictureBox1.Image = Image.FromFile(filename1);
            pictureBox1.ClientSize = new Size(pictureBox1.Image.Width / 2, pictureBox1.Image.Height / 2);
            pictureBox2.Image = Image.FromFile(filename2);
            pictureBox2.ClientSize = new Size(pictureBox2.Image.Width / 2, pictureBox2.Image.Height / 2);
            pictureBox3.Image = Image.FromFile(filename3);
            pictureBox3.ClientSize = new Size(pictureBox3.Image.Width / 2, pictureBox3.Image.Height / 2);

            pictureBox1.MouseDown += PictureBox_MouseDown;
            pictureBox1.MouseMove += PictureBox_MouseMove;
            pictureBox1.MouseUp += PictureBox_MouseUp;
            pictureBox2.MouseDown += PictureBox_MouseDown;
            pictureBox2.MouseMove += PictureBox_MouseMove;
            pictureBox2.MouseUp += PictureBox_MouseUp;
            pictureBox3.MouseDown += PictureBox_MouseDown;
            pictureBox3.MouseMove += PictureBox_MouseMove;
            pictureBox3.MouseUp += PictureBox_MouseUp;
        }

        bool flag_pictureBox_mouse_down = false;
        int pictureBox_position_x_old = 0;
        int pictureBox_position_y_old = 0;
        private void PictureBox_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                flag_pictureBox_mouse_down = true;
                //richTextBox1.Text += "Down : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
                pictureBox_position_x_old = e.X;
                pictureBox_position_y_old = e.Y;
                ((PictureBox)sender).BringToFront();    //選中的那一片拉到最上層顯示
            }
        }

        private void PictureBox_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_pictureBox_mouse_down == true)
            {
                //richTextBox1.Text += "Up : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
                int dx = e.X - pictureBox_position_x_old;
                int dy = e.Y - pictureBox_position_y_old;

                //richTextBox1.Text += "dx, dy : (" + dx.ToString() + ", " + dy.ToString() + ")\n";
                ((PictureBox)sender).Location = new Point(((PictureBox)sender).Location.X + dx, ((PictureBox)sender).Location.Y + dy);
            }
        }

        private void PictureBox_MouseUp(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                flag_pictureBox_mouse_down = false;
                //richTextBox1.Text += "Up : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
                int dx = e.X - pictureBox_position_x_old;
                int dy = e.Y - pictureBox_position_y_old;

                //richTextBox1.Text += "dx, dy : (" + dx.ToString() + ", " + dy.ToString() + ")\n";
                ((PictureBox)sender).Location = new Point(((PictureBox)sender).Location.X + dx, ((PictureBox)sender).Location.Y + dy);
            }
        }
    }
}
