using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_DragPicture4b
{
    public partial class Form1 : Form
    {
        

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //讀取圖檔
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Image image = System.Drawing.Image.FromFile(filename);
            pictureBox1.Image = image;
            pictureBox1.Height = image.Height;
            pictureBox1.Width = image.Width;
        }

        private Point pictureBox1_position_old; //記錄鼠標指針的坐標
        private bool flag_pictureBox1_mouse_down = false;
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                pictureBox1_position_old.X = e.X;
                pictureBox1_position_old.Y = e.Y;
                flag_pictureBox1_mouse_down = true;
                //richTextBox1.Text += "Down : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
            }
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_pictureBox1_mouse_down == true)
            {
                //richTextBox1.Text += "Up : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
                int dx = e.X - pictureBox1_position_old.X;
                int dy = e.Y - pictureBox1_position_old.Y;

                //richTextBox1.Text += "dx, dy : (" + dx.ToString() + ", " + dy.ToString() + ")\n";
                pictureBox1.Location = new Point(pictureBox1.Location.X + dx, pictureBox1.Location.Y + dy);
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                flag_pictureBox1_mouse_down = false;
            }
        }

    }
}

