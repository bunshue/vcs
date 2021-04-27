using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;
using System.Drawing.Imaging;

namespace BuntForms
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\picture1.jpg";

        Image image;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            image = Image.FromFile(filename);
            pictureBox1.Image = image;
            pictureBox1.Size = new Size(image.Width, image.Height - 1);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //推拉效果
            try
            {
                Graphics g = this.pictureBox1.CreateGraphics();
                Bitmap bitmap1 = new Bitmap(image);
                g.Clear(this.pictureBox1.BackColor);
                for (int i = 0; i < this.pictureBox1.Height; i++)
                {
                    Rectangle rectangle1 = new Rectangle(0, 0, this.pictureBox1.Width, i);
                    Rectangle rectangle2 = new Rectangle(0, this.pictureBox1.Height - i, this.pictureBox1.Width, i + 1);
                    Bitmap cloneBitmap = bitmap1.Clone(rectangle2, PixelFormat.DontCare);
                    g.DrawImage(cloneBitmap, rectangle1);
                    this.pictureBox1.Show();
                }
            }
            catch { }
        }
    }
}