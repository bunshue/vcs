using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Draw5_Image2
{
    public partial class Form1 : Form
    {
        string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";

        int W = 0;
        int H = 0;
        int x_st = 0;
        int y_st = 0;
        int sw = 100;
        int sh = 100;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Image img = Image.FromFile(filename);

            W = img.Width;
            H = img.Height;
            x_st = W / 2;
            y_st = H / 2;

            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox1.Size = new System.Drawing.Size(W, H);
            pictureBox1.Image = img;
            this.pictureBox1.KeyDown += new KeyEventHandler(pictureBox1_KeyDown);
            this.ActiveControl = this.pictureBox1;//选中pictureBox1，不然没法触发事件
            pictureBox2.Size = new System.Drawing.Size(sw * 3, sh * 3);
        }

        void pictureBox1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Space)
            {
                label1.Text = "Space";
            }
            else if (e.KeyCode == Keys.PageDown)
            {
                label1.Text = "PageDown";
            }
            else if (e.KeyCode == Keys.PageUp)
            {
                label1.Text = "PageUp";
            }
            else if (e.KeyCode == Keys.Up)
            {
                label1.Text = "Up";
                y_st -= 20;
            }
            else if (e.KeyCode == Keys.Down)
            {
                label1.Text = "Down";
                y_st += 20;
            }
            else if (e.KeyCode == Keys.Left)
            {
                label1.Text = "Left";
                x_st -= 20;
            }
            else if (e.KeyCode == Keys.Right)
            {
                label1.Text = "Right";
                x_st += 20;
            }
            else if (e.KeyCode == Keys.X)
            {
                Application.Exit();
            }
            else
            {
                label1.Text = "你按了" + e.KeyCode.ToString();
            }
            this.pictureBox1.Invalidate();
            this.pictureBox2.Invalidate();
        }

        private void pictureBox1_DoubleClick(object sender, EventArgs e)
        {

        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            x_st = e.X;
            y_st = e.Y;
            this.pictureBox1.Invalidate();
            this.pictureBox2.Invalidate();
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.DrawRectangle(new Pen(Color.Red, 1), x_st - sw / 2, y_st - sh / 2, sw, sh);

        }

        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {
            int sx = x_st - sw / 2;
            int sy = y_st - sh / 2;

            Rectangle srcRect = new Rectangle(sx, sy, sw, sh);   //擷取部分區域
            GraphicsUnit units = GraphicsUnit.Pixel;

            Image img = Image.FromFile("c:\\______test_files1\\picture1.jpg");

            //Bitmap bitmap = new Bitmap(srcRect.Width, srcRect.Height);
            //             貼上位置x,貼上位置y,貼上大小W,貼上大小H
            //g.DrawImage(img, x_st, y_st, W * 10 / 10, H * 10 / 10);

            // 準備貼上的位置與放大縮小量,以平行四邊形(parallelogram)的左上點右上點左下點表示
            int x_st2 = pictureBox2.Width / 2 - sw / 2;
            int y_st2 = pictureBox2.Height / 2 - sh / 2;
            label1.Text = "x_st2 = " + x_st2.ToString() + ", y_st2 = " + y_st2.ToString();

            Point ulCorner = new Point(x_st2, y_st2);
            Point urCorner = new Point(x_st2 + sw * 3, y_st2);
            Point llCorner = new Point(x_st2, y_st2 + sh * 3);

            Point[] destRect1 = { ulCorner, urCorner, llCorner };

            //擷取部分圖片貼上
            //            貼上位置與大小,擷取部分圖片位置與大小,單位

            e.Graphics.DrawImage(img, destRect1, srcRect, units);
        }
    }
}
