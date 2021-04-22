using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;

namespace vcs_PictureCrop8
{
    public partial class Form1 : Form
    {
        Image myImage;

        string filename = @"C:\______test_files\picture1.jpg";
        bool flag_mouse_down = false;

        int x_st = 0;
        int y_st = 0;
        int x_sp = 0;
        int y_sp = 0;

        int w = 0;
        int h = 0;

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

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            int W = pictureBox1.Width;
            int H = pictureBox1.Height;

            flag_mouse_down = true;
            x_st = e.X;
            y_st = e.Y;

            Graphics g = pictureBox1.CreateGraphics();
            g.DrawLine(new Pen(Color.Black, 1), new Point(e.X, 0), new Point(e.X, H));
            g.DrawLine(new Pen(Color.Black, 1), new Point(0, e.Y), new Point(W, e.Y));
            //g.DrawLine(new Pen(Color.Black, 1), new Point(0, e.Y), new Point(e.X, e.Y));
            //g.DrawLine(new Pen(Color.Black, 1), new Point(e.X, e.Y), new Point(W - e.X, e.Y));
            //Application.DoEvents();
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            /*
            //恢復原狀
            pictureBox1.Image = myImage;
            pictureBox1.Height = myImage.Height;
            pictureBox1.Width = myImage.Width;
            */
            if (flag_mouse_down == true)
            {

                int W = pictureBox1.Width;
                int H = pictureBox1.Height;

                Graphics g = pictureBox1.CreateGraphics();
                g.DrawLine(new Pen(Color.Black, 1), new Point(e.X, 0), new Point(e.X, H));
                g.DrawLine(new Pen(Color.Black, 1), new Point(0, e.Y), new Point(W, e.Y));
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            flag_mouse_down = false;
            x_sp = e.X;
            y_sp = e.Y;

            if (x_sp > x_st)
                w = x_sp - x_st;
            else
            {
                w = x_st - x_sp;
                x_st = x_sp;
            }

            if (y_sp > y_st)
                h = y_sp - y_st;
            else
            {
                h = y_st - y_sp;
                y_st = y_sp;
            }

            //恢復原狀
            pictureBox1.Image = myImage;
            pictureBox1.Height = myImage.Height;
            pictureBox1.Width = myImage.Width;

            Application.DoEvents();

            Graphics g = pictureBox1.CreateGraphics();
            g.DrawRectangle(new Pen(Color.Red, 1), x_st, y_st, w, h);
        }
    }
}
