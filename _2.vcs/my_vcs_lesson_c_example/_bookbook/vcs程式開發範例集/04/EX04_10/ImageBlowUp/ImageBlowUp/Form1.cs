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

namespace ImageBlowUp
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
            try
            {
                Cursor.Current = myCursor;
                Graphics graphics = pictureBox1.CreateGraphics();
                Rectangle sourceRectangle = new Rectangle(e.X - 10, e.Y - 10, 20, 20); //要放大的區域 
                Rectangle destRectangle = new Rectangle(e.X - 20, e.Y - 20, 40, 40);
                graphics.DrawImage(myImage, destRectangle, sourceRectangle, GraphicsUnit.Pixel);
            }
            catch
            { }
        }

    }
}