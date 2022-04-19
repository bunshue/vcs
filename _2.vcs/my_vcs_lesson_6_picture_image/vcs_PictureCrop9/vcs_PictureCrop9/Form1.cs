using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_PictureCrop9
{
    public partial class Form1 : Form
    {
        public Point firstPoint = new Point(0, 0);  //鼠標第一點 
        public Point secondPoint = new Point(0, 0);  //鼠標第二點 
        public bool begin = false;   //是否開始畫矩形 
        Graphics g;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";
            pictureBox1.Image = Image.FromFile(filename);

            g = this.pictureBox1.CreateGraphics();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (button1.Text == "截圖")
            {
                button1.Text = "截圖中";
                pictureBox1.MouseDown += new System.Windows.Forms.MouseEventHandler(pictureBox1_MouseDown);
            }
            else
            {
                button1.Text = "截圖";

            }
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            begin = true;
            firstPoint = new Point(e.X, e.Y);

            pictureBox1.MouseDown -= new System.Windows.Forms.MouseEventHandler(pictureBox1_MouseDown);
            pictureBox1.MouseMove += new System.Windows.Forms.MouseEventHandler(pictureBox1_MouseMove);
            pictureBox1.MouseUp += new System.Windows.Forms.MouseEventHandler(pictureBox1_MouseUp);
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (begin == true)
            {
                //重新在pictureBox1上面繪圖
                this.Refresh();
                //獲取新的右下角坐標 
                secondPoint = new Point(e.X, e.Y);
                int minX = Math.Min(firstPoint.X, secondPoint.X);
                int minY = Math.Min(firstPoint.Y, secondPoint.Y);
                int maxX = Math.Max(firstPoint.X, secondPoint.X);
                int maxY = Math.Max(firstPoint.Y, secondPoint.Y);

                //畫矩形
                g.DrawRectangle(new Pen(Color.Red), minX, minY, maxX - minX, maxY - minY);
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            begin = false;

            pictureBox1.MouseMove -= new System.Windows.Forms.MouseEventHandler(pictureBox1_MouseMove);
            pictureBox1.MouseUp -= new System.Windows.Forms.MouseEventHandler(pictureBox1_MouseUp);
            button1.Text = "截圖";
        }
    }
}
