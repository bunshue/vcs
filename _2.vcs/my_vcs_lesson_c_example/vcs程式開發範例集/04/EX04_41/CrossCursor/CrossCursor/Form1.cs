using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;

namespace CrossCursor
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        Image myImage;
        private void button1_Click(object sender, EventArgs e)
        {
            openFileDialog1.Filter = "*.jpg,*.jpeg,*.bmp,*.gif,*.ico,*.png,*.tif,*.wmf|*.jpg;*.jpeg;*.bmp;*.gif;*.ico;*.png;*.tif;*.wmf";
            openFileDialog1.ShowDialog();
            myImage = System.Drawing.Image.FromFile(openFileDialog1.FileName);
            pictureBox1.Image = myImage;
            pictureBox1.Height = myImage.Height;
            pictureBox1.Width = myImage.Width;
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            Graphics myGraphics = pictureBox1.CreateGraphics();
            myGraphics.DrawLine(new Pen(Color.Black, 1), new Point(e.X, 0), new Point(e.X, e.Y));
            myGraphics.DrawLine(new Pen(Color.Black, 1), new Point(e.X, e.Y), new Point(e.X, pictureBox1.Height-e.Y));
            myGraphics.DrawLine(new Pen(Color.Black, 1), new Point(0, e.Y), new Point(e.X, e.Y));
            myGraphics.DrawLine(new Pen(Color.Black, 1), new Point(e.X, e.Y), new Point(pictureBox1.Width - e.X, e.Y));
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            pictureBox1.Image = myImage;
            pictureBox1.Height = myImage.Height;
            pictureBox1.Width = myImage.Width;
        }
    }
}