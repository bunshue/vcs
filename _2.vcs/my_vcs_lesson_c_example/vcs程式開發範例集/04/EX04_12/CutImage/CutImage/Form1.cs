using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;
using System.Drawing.Imaging;

namespace CutImage
{
    public partial class Form1 : Form
    {
        bool isDrag = false;
        Rectangle theRectangle = new Rectangle(new Point(0, 0), new Size(0, 0));
        Point startPoint, oldPoint;
        private Graphics ig;
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
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                //如果開始繪製，則開始記錄鼠標位置
                if ((isDrag = !isDrag) == true)
                {
                    startPoint = new Point(e.X, e.Y);
                    oldPoint = new Point(e.X, e.Y);
                }
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            isDrag = false;
            ig = pictureBox1.CreateGraphics();
            ig.DrawRectangle(new Pen(Color.Black, 1), startPoint.X, startPoint.Y, e.X - startPoint.X, e.Y - startPoint.Y);
            theRectangle = new Rectangle(startPoint.X, startPoint.Y, e.X - startPoint.X, e.Y - startPoint.Y);
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            Graphics g = this.CreateGraphics();
            if (isDrag)
            {
                g.DrawRectangle(new Pen(Color.Black, 1), startPoint.X, startPoint.Y, e.X - startPoint.X, e.Y - startPoint.Y);
            }
        }

        private void Form1_MouseClick(object sender, MouseEventArgs e)
        {
            try
            {
                Graphics graphics = this.CreateGraphics();
                Bitmap bitmap = new Bitmap(pictureBox1.Image);
                Bitmap cloneBitmap = bitmap.Clone(theRectangle, PixelFormat.DontCare);
                graphics.DrawImage(cloneBitmap, e.X, e.Y);
                Graphics g = pictureBox1.CreateGraphics();
                SolidBrush myBrush = new SolidBrush(Color.White);
                g.FillRectangle(myBrush, theRectangle);
            }
            catch
            { }
        }
    }
}