using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_MovePicture
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename1 = @"C:\______test_files\peony2\p1.jpg";
            string filename2 = @"C:\______test_files\peony2\p2.jpg";
            string filename3 = @"C:\______test_files\peony2\p3.jpg";
            pictureBox1.Image = Image.FromFile(filename1);
            pictureBox1.ClientSize = new Size(pictureBox1.Image.Width / 2, pictureBox1.Image.Height / 2);
            pictureBox2.Image = Image.FromFile(filename2);
            pictureBox2.ClientSize = new Size(pictureBox2.Image.Width / 2, pictureBox2.Image.Height / 2);
            pictureBox3.Image = Image.FromFile(filename3);
            pictureBox3.ClientSize = new Size(pictureBox3.Image.Width / 2, pictureBox3.Image.Height / 2);
        }

        bool isMouseDown = false;
        int px, py;

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                pictureBox1.BringToFront();
                isMouseDown = true;
                px = e.X;
                py = e.Y;
            }
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (isMouseDown)
            {
                /*  same
                pictureBox1.Left += (e.X - px);
                pictureBox1.Top += (e.Y - py);
                */

                int x = pictureBox1.Location.X;
                int y = pictureBox1.Location.Y;
                x += (e.X - px);
                y += (e.Y - py);
                pictureBox1.Location = new Point(x, y);
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
                isMouseDown = false;

        }

        private void pictureBox2_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                pictureBox2.BringToFront();
                isMouseDown = true;
                px = e.X;
                py = e.Y;
            }
        }

        private void pictureBox2_MouseMove(object sender, MouseEventArgs e)
        {
            if (isMouseDown)
            {
                /*  same
                pictureBox2.Left += (e.X - px);
                pictureBox2.Top += (e.Y - py);
                */

                int x = pictureBox2.Location.X;
                int y = pictureBox2.Location.Y;
                x += (e.X - px);
                y += (e.Y - py);
                pictureBox2.Location = new Point(x, y);
            }
        }

        private void pictureBox2_MouseUp(object sender, MouseEventArgs e)
        {
            pictureBox1_MouseUp(sender, e);
        }

        private void pictureBox3_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                pictureBox3.BringToFront();
                isMouseDown = true;
                px = e.X;
                py = e.Y;
            }
        }

        private void pictureBox3_MouseMove(object sender, MouseEventArgs e)
        {
            if (isMouseDown)
            {
                /*  same
                pictureBox3.Left += (e.X - px);
                pictureBox3.Top += (e.Y - py);
                */

                int x = pictureBox3.Location.X;
                int y = pictureBox3.Location.Y;
                x += (e.X - px);
                y += (e.Y - py);
                pictureBox3.Location = new Point(x, y);
            }
        }

        private void pictureBox3_MouseUp(object sender, MouseEventArgs e)
        {
            pictureBox1_MouseUp(sender, e);
        }
    }
}
