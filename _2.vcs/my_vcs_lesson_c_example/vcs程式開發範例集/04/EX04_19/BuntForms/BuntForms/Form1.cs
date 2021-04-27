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
            this.BackgroundImage = image;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            try
            {
                Graphics myGraphics = this.CreateGraphics();
                Bitmap bitmap1 = new Bitmap(image);
                myGraphics.Clear(this.BackColor);
                for (int i = 0; i < this.Height; i++)
                {
                    Rectangle rectangle1 = new Rectangle(0, 0, this.Width, i);
                    Rectangle rectangle2 = new Rectangle(0, this.Height - i, this.Width, i + 1);
                    Bitmap cloneBitmap = bitmap1.Clone(rectangle2, PixelFormat.DontCare);
                    myGraphics.DrawImage(cloneBitmap, rectangle1);
                    this.Show();
                }
            }
            catch { }
        }
    }
}