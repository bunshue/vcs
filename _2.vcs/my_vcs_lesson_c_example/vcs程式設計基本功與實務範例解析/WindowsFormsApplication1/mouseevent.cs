using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class mouseevent : Form
    {
        public mouseevent()
        {
            InitializeComponent();
        }

        private void pictureBox1_MouseEnter(object sender, EventArgs e)
        {
            int id = rd.Next(0, 8);
            pictureBox1.Image = imageList1.Images[id];
        }

        Random rd;
        bool isMouseDown = false;
        int px, py;

        private void mouseevent_Load(object sender, EventArgs e)
        {
            rd = new Random();
        }

        private void pictureBox1_MouseLeave(object sender, EventArgs e)
        {
            pictureBox1.Image = imageList1.Images[8];
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                isMouseDown = true;
                px = e.X;
                py = e.Y;
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
                isMouseDown = false;
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (isMouseDown)
            {
                pictureBox1.Left += (e.X - px);
                pictureBox1.Top += (e.Y - py);

                /*int x = pictureBox1.Location.X;
                int y = pictureBox1.Location.Y;
                x += (e.X - px);
                y += (e.Y - py);
                pictureBox1.Location = new Point(x, y);*/

            }
        }
    }
}
