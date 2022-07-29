using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;   //for DashStyle

//在 pictureBox的圖片上畫矩形

namespace draw_rectangle2
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\picture1.jpg";

        private bool flag_mouse_down = false;
        private int intStartX = 0;
        private int intStartY = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //讀取圖檔, 先放在Bitmap裏
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            //Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            pictureBox1.Image = bitmap1;

            //跟隨鼠標在 pictureBox 的圖片上畫矩形
            pictureBox1.MouseDown += new MouseEventHandler(pictureBox1_MouseDown);
            pictureBox1.MouseMove += new MouseEventHandler(pictureBox1_MouseMove);
            pictureBox1.MouseUp += new MouseEventHandler(pictureBox1_MouseUp);
        }

        void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            flag_mouse_down = true;
            intStartX = e.X;
            intStartY = e.Y;
        }

        void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_mouse_down == true)
            {
                try
                {
                    string filename = @"C:\______test_files\picture1.jpg";
                    Image tmp = Image.FromFile(filename);

                    Graphics g = this.pictureBox1.CreateGraphics();

                    //清空上次畫下的痕跡
                    g.Clear(this.pictureBox1.BackColor);

                    Brush brush = new SolidBrush(Color.Red);
                    Pen pen = new Pen(brush, 1);
                    pen.DashStyle = DashStyle.Solid;
                    g.DrawRectangle(pen, new Rectangle(intStartX > e.X ? e.X : intStartX, intStartY > e.Y ? e.Y : intStartY, Math.Abs(e.X - intStartX), Math.Abs(e.Y - intStartY)));
                    g.Dispose();
                    //this.pictureBox1.Image = tmp;
                }

                catch (Exception ex)
                {
                    ex.ToString();
                }
            }
        }

        void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            flag_mouse_down = false;
            intStartX = 0;
            intStartY = 0;
        }
    }
}
