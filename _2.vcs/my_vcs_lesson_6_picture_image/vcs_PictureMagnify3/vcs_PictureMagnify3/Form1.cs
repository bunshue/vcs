using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;

using System.Drawing.Drawing2D;
using System.Drawing.Imaging;

namespace vcs_PictureMagnify3
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\picture1.jpg";
        Bitmap bitmap1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            
            bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式

            pictureBox1.Image = bitmap1;
            pictureBox1.Height = bitmap1.Height;
            pictureBox1.Width = bitmap1.Width;
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            int r = 50;
            int R = 200;

            //由 r X r 放大到 R X R
            try
            {
                Graphics g = pictureBox1.CreateGraphics();
                Rectangle rect1 = new Rectangle(e.X - r / 2, e.Y - r / 2, r, r); //要放大的區域 
                Rectangle rect2 = new Rectangle(e.X - R / 2, e.Y - R / 2, R, R);
                g.DrawImage(bitmap1, 0, 0, bitmap1.Width, bitmap1.Height);
                g.DrawImage(bitmap1, rect2, rect1, GraphicsUnit.Pixel);
            }
            catch
            {
            }
        }
    }
}
