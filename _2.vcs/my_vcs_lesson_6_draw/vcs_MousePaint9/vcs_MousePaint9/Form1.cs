using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;  // for DashStyle

//跟隨鼠標在 pictureBox 的圖片上畫矩形

namespace vcs_MousePaint9
{
    public partial class Form1 : Form
    {
        private int intStartX = 0;
        private int intStartY = 0;
        private bool isMouseDraw = false;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            isMouseDraw = true;
            intStartX = e.X;
            intStartY = e.Y;
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (isMouseDraw)
            {
                try
                {
                    //Image tmp = Image.FromFile("1.png");
                    Graphics g = this.pictureBox1.CreateGraphics();
                    //清空上次畫下的痕跡
                    g.Clear(this.pictureBox1.BackColor);
                    Brush brush = new SolidBrush(Color.Red);
                    Pen pen = new Pen(brush, 1);
                    pen.DashStyle = DashStyle.Solid;
                    g.DrawRectangle(pen, new Rectangle(intStartX > e.X ? e.X : intStartX, intStartY > e.Y ? e.Y : intStartY, Math.Abs(e.X - intStartX), Math.Abs(e.Y - intStartY)));
                    g.Dispose();
                    //this.pictureBox_Src.Image = tmp;
                }
                catch (Exception ex)
                {
                    ex.ToString();
                }
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            isMouseDraw = false;
            intStartX = 0;
            intStartY = 0;
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {

        }

    }
}
