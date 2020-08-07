using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_PingPongGame
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;
        Color color = new Color();

        int W = 0;
        int H = 0;
        int w = 0;
        int h = 0;
        int cx = 0;
        int cy = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox1.Size = new Size(480, 640);
            this.pictureBox1.KeyDown += new KeyEventHandler(pictureBox1_KeyDown);
            this.ActiveControl = this.pictureBox1;//选中pictureBox1，不然没法触发事件


            p = new Pen(Color.Green, 3);
            sb = new SolidBrush(Color.Pink);

            W = pictureBox1.Width;
            H = pictureBox1.Height;

            //新建圖檔, 初始化畫布
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;

            w = 100;
            h = 50;

            color = Color.Lime;

            cx = (W - w) / 2;
            cy = H * 90 / 100;

            draw_bar(color, cx, cy, w, h);
        }

        void draw_bar(Color color, int cx, int cy, int w, int h)
        {
            sb = new SolidBrush(color);
            g.FillRectangle(sb, cx - w / 2, cy - h / 2, w, h);
        }

        void pictureBox1_KeyDown(object sender, KeyEventArgs e)
        {
            if ((e.KeyCode == Keys.PageDown) || (e.KeyCode == Keys.Space))
            {
                mesg.Text = "下一首\n";
            }
            else if (e.KeyCode == Keys.PageUp)
            {
                mesg.Text = "上一首\n";
            }
            else if (e.KeyCode == Keys.Right)
            {
                mesg.Text = "Right\n";
                cx += 10;
                draw_bar(color, cx, cy, w, h);
                pictureBox1.Image = bitmap1;
            }
            else if (e.KeyCode == Keys.Left)
            {
                mesg.Text = "Left\n";
                cx -= 10;
                draw_bar(color, cx, cy, w, h);
                pictureBox1.Image = bitmap1;
            }
            else
            {
                mesg.Text = "xxxxx\n";

            }



        }
    }
}
