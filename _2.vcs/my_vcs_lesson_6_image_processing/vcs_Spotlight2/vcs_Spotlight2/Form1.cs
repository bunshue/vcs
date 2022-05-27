using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D;

namespace vcs_Spotlight2
{
    public partial class Form1 : Form
    {
        Bitmap bitmap2 = Properties.Resources.Picasso_01;
        Point[] pArr1b = new Point[3];
        Point[] pArr2b = new Point[3];
        SolidBrush brush1b = new SolidBrush(Color.FromArgb(64, 255, 255, 0));
        SolidBrush brush2b = new SolidBrush(Color.FromArgb(64, 0, 255, 255));
        int Dx1b = 2;
        int Dx2b = -3;

        //探照燈的位置
        Point mp1; //  moving point
        bool Selected1 = false;
        int dx1, dy1;

        Point mp2; //  moving point
        bool Selected2 = false;
        int dx2, dy2;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.pictureBox_spotlight2.ClientSize = new Size(600, 600);

            mp1 = new Point(450, 600);
            pArr1b[0] = mp1;
            pArr1b[1] = new Point(300 - 70, 0);
            pArr1b[2] = new Point(300 + 70, 0);

            mp2 = new Point(150, 100);
            pArr2b[0] = new Point(0, 0);
            pArr2b[1] = new Point(300 - 100, 600);
            pArr2b[2] = new Point(300 + 100, 600);
        }

        private void timer_spotlight2_Tick(object sender, EventArgs e)
        {
            if (pArr1b[1].X <= 0 || pArr1b[2].X >= 600)
            {
                Dx1b = -Dx1b;
            }
            pArr1b[1].X = pArr1b[1].X + Dx1b;
            pArr1b[2].X = pArr1b[2].X + Dx1b;

            if (pArr2b[1].X <= 0 || pArr2b[2].X >= 600)
            {
                Dx2b = -Dx2b;
            }
            pArr2b[1].X = pArr2b[1].X + Dx2b;
            pArr2b[2].X = pArr2b[2].X + Dx2b;

            this.pictureBox_spotlight2.Invalidate();
        }

        private void pictureBox_spotlight2_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            e.Graphics.DrawImage(bitmap2, 0, 0, bitmap2.Width, bitmap2.Height);

            pArr1b[0] = mp1;
            GraphicsPath gp = new GraphicsPath();
            gp.AddPolygon(pArr1b);
            e.Graphics.FillPath(brush1b, gp);

            pArr2b[0] = mp2;
            GraphicsPath gp2 = new GraphicsPath();
            gp2.AddPolygon(pArr2b);
            e.Graphics.FillPath(brush2b, gp2);

            e.Graphics.FillEllipse(Brushes.Red, mp1.X - 10, mp1.Y - 10, 20, 20);
            e.Graphics.FillEllipse(Brushes.Red, mp2.X - 10, mp2.Y - 10, 20, 20);

        }


        private void pictureBox_spotlight2_MouseDown(object sender, MouseEventArgs e)
        {
            // mp vs e.Location
            double dis = Math.Sqrt((mp1.X - e.X) * (mp1.X - e.X) + (mp1.Y - e.Y) * (mp1.Y - e.Y));
            if (dis <= 10)
            {
                Selected1 = true;
                dx1 = e.X - mp1.X;
                dy1 = e.Y - mp1.Y;
            }

            double dis2 = Math.Sqrt((mp2.X - e.X) * (mp2.X - e.X) + (mp2.Y - e.Y) * (mp2.Y - e.Y));
            if (dis2 <= 10)
            {
                Selected2 = true;
                dx2 = e.X - mp2.X;
                dy2 = e.Y - mp2.Y;
            }

        }

        private void pictureBox_spotlight2_MouseMove(object sender, MouseEventArgs e)
        {
            if (Selected1 == true)
            {
                mp1.X = e.X - dx1;
                mp1.Y = e.Y - dy1;
            }

            if (Selected2 == true)
            {
                mp2.X = e.X - dx2;
                mp2.Y = e.Y - dy2;
            }
        }

        private void pictureBox_spotlight2_MouseUp(object sender, MouseEventArgs e)
        {
            Selected1 = false;
            Selected2 = false;
        }


    }
}
