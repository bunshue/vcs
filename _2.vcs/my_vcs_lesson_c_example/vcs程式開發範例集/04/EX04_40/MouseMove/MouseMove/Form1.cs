using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;

namespace MouseMove
{
    public partial class Form1 : Form
    {
        bool flag = false;
        int x, y;
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            openFileDialog1.Filter = "*.jpg,*.jpeg,*.bmp,*.gif,*.ico,*.png,*.tif,*.wmf|*.jpg;*.jpeg;*.bmp;*.gif;*.ico;*.png;*.tif;*.wmf";
            openFileDialog1.ShowDialog();
            Image myImage = System.Drawing.Image.FromFile(openFileDialog1.FileName);
            pictureBox1.Image = myImage;
            pictureBox1.Height = myImage.Height;
            pictureBox1.Width = myImage.Width;
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            flag = true;
            x = e.X;
            y = e.Y;
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag)
            {
                pictureBox1.Left = pictureBox1.Left + (e.X - x);
                pictureBox1.Top = pictureBox1.Top + (e.Y - y);
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            flag = false;
        }
    }
}