using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;
using System.Drawing.Imaging;

namespace vcs_PictureCrop9
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\picture1.bmp";

        private bool flag_select_area = false;  //開始選取的旗標
        private Point pt_st = Point.Empty;//記錄鼠標按下時的坐標，用來確定繪圖起點
        private Point pt_sp = Point.Empty;//記錄鼠標放開時的坐標，用來確定繪圖終點
        private Bitmap bitmap1 = null;  //原圖位圖Bitmap
        private Bitmap bitmap2 = null;  //擷取部分位圖Bitmap
        private Rectangle select_rectangle = new Rectangle(new Point(0, 0), new Size(0, 0));    //用來保存截圖的矩形

        private int W = 0;  //原圖的寬
        private int H = 0;  //原圖的高
        private int w = 0;  //擷取圖的寬
        private int h = 0;  //擷取圖的高

        Point startPoint, oldPoint;
        private Graphics ig;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Image myImage = System.Drawing.Image.FromFile(filename);
            pictureBox1.Image = myImage;
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                flag_select_area = true;
                startPoint = new Point(e.X, e.Y);
                oldPoint = new Point(e.X, e.Y);
            }
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            Graphics g = this.CreateGraphics();
            if (flag_select_area == true)
            {
                g.DrawRectangle(new Pen(Color.Black, 1), startPoint.X, startPoint.Y, e.X - startPoint.X, e.Y - startPoint.Y);
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            flag_select_area = false;
            ig = pictureBox1.CreateGraphics();
            ig.DrawRectangle(new Pen(Color.Black, 1), startPoint.X, startPoint.Y, e.X - startPoint.X, e.Y - startPoint.Y);
            select_rectangle = new Rectangle(startPoint.X, startPoint.Y, e.X - startPoint.X, e.Y - startPoint.Y);
        }

        private void Form1_MouseClick(object sender, MouseEventArgs e)
        {
            try
            {
                Graphics graphics = this.CreateGraphics();
                Bitmap bitmap = new Bitmap(pictureBox1.Image);
                Bitmap cloneBitmap = bitmap.Clone(select_rectangle, PixelFormat.DontCare);
                graphics.DrawImage(cloneBitmap, e.X, e.Y);
                Graphics g = pictureBox1.CreateGraphics();
                SolidBrush myBrush = new SolidBrush(Color.White);
                g.FillRectangle(myBrush, select_rectangle);
            }
            catch
            { }
        }

    }
}