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
        Cursor myCursor = new Cursor(@"C:\WINDOWS\Cursors\cross_r.cur"); //自定義鼠標 
        Image myImage;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            myImage = System.Drawing.Image.FromFile(filename);
            pictureBox1.Image = myImage;
            pictureBox1.Height = myImage.Height;
            pictureBox1.Width = myImage.Width;
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            int dd = 100;

            //由 20 X 20 放大到 100 X 100
            try
            {
                Cursor.Current = myCursor;
                Graphics graphics = pictureBox1.CreateGraphics();
                Rectangle sourceRectangle = new Rectangle(e.X - 10, e.Y - 10, 20, 20); //要放大的區域 
                Rectangle destRectangle = new Rectangle(e.X - dd / 2, e.Y - dd / 2, dd, dd);
                graphics.DrawImage(myImage, 0, 0, myImage.Width, myImage.Height);
                graphics.DrawImage(myImage, destRectangle, sourceRectangle, GraphicsUnit.Pixel);
            }
            catch
            {
            }
        }
    }
}
