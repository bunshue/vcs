using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_PictureMagnify4
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.FormBorderStyle = FormBorderStyle.None;//无边框
            this.Cursor = System.Windows.Forms.Cursors.Cross;
            //this.WindowState = FormWindowState.Maximized;
            //this.Opacity = 0.01;
            this.TopMost = true;
            this.ShowInTaskbar = false;

            this.pictureBox1.KeyDown += new KeyEventHandler(pictureBox1_KeyDown);
            this.ActiveControl = this.pictureBox1;//选中pictureBox1，不然没法触发事件
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            this.MoveForm();    //当前窗体自动跟随鼠标
            this.ShowPictureBox(MousePosition);
            this.pictureBox1.Focus();
        }

        void ShowPictureBox(Point p)
        {
            //创建一个画布大小和当前屏幕大小一样
            Bitmap bmp = new Bitmap(20, 20);
            //在这快画布上建立一个绘图对象
            Graphics g = Graphics.FromImage(bmp);
            //截取复制当前屏幕内容
            g.CopyFromScreen(p.X - 10, p.Y - 10, 0, 0, bmp.Size);
            //以缩略图的形式就放大镜
            Image pThumbnail = bmp.GetThumbnailImage(this.pictureBox1.Width, this.pictureBox1.Height, null, new IntPtr());
            //画放大图
            g.DrawImage(bmp, 10, 10, pThumbnail.Width, pThumbnail.Height);
            g.Dispose();

            this.pictureBox1.Image = pThumbnail;
            g = Graphics.FromImage(this.pictureBox1.Image);
            g.DrawRectangle(Pens.Black, this.pictureBox1.Width / 2 - 5, this.pictureBox1.Height / 2 - 5, 10, 10);
            g.Dispose();
        }

        void MoveForm()
        {
            Point p = new Point();
            p.X = MousePosition.X + 10;
            p.Y = MousePosition.Y + 10;

            Size s = Screen.PrimaryScreen.Bounds.Size;

            if (p.X > s.Width - this.Width)
            {
                p.X -= this.Width + 20;
            }
            if (p.Y > s.Height - this.Height)
            {
                p.Y -= this.Height + 20;
            }
            this.Location = p;
        }

        void pictureBox1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Escape)
            {
                this.Close();
            }
        }
    }
}
