// 作者：鄞永傳老師‧xnabook@yahoo.com.tw‧2012-08 
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        Bitmap bitmap = Properties.Resources.Picasso_01;
        Point[] pArr = new Point[3];
        SolidBrush brush = new SolidBrush(Color.FromArgb(64, 255, 255, 0));
        int Dx = 2;

        Point[] pArr2 = new Point[3];
        SolidBrush brush2 = new SolidBrush(Color.FromArgb(64, 0, 255, 255));
        int Dx2 = -3;

        Point mp; //  moving point
        bool Selected = false;
        int dx, dy;

        Point mp2; //  moving point
        bool Selected2 = false;
        int dx2, dy2;

        public Form1()
        {
            InitializeComponent();
            this.ClientSize = new Size(600, 600);

            mp = new Point(450, 600);
            pArr[0] = mp;
            pArr[1] = new Point(300 - 70, 0);
            pArr[2] = new Point(300 + 70, 0);

            mp2 = new Point(150, 100);
            pArr2[0] = new Point(0, 0);
            pArr2[1] = new Point(300 - 100, 600);
            pArr2[2] = new Point(300 + 100, 600);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            e.Graphics.DrawImage(bitmap, 0, 0, bitmap.Width, bitmap.Height);

            pArr[0] = mp;
            GraphicsPath gp = new GraphicsPath();
            gp.AddPolygon(pArr);
            e.Graphics.FillPath(brush, gp);

            pArr2[0] = mp2;
            GraphicsPath gp2 = new GraphicsPath();
            gp2.AddPolygon(pArr2);
            e.Graphics.FillPath(brush2, gp2);

            e.Graphics.FillEllipse(Brushes.Red, mp.X - 10 , mp.Y - 10, 20, 20);
            e.Graphics.FillEllipse(Brushes.Red, mp2.X - 10, mp2.Y - 10, 20, 20);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (pArr[1].X <= 0 || pArr[2].X >= 600) Dx = -Dx;
            pArr[1].X = pArr[1].X + Dx;
            pArr[2].X = pArr[2].X + Dx;

            if (pArr2[1].X <= 0 || pArr2[2].X >= 600) Dx2 = -Dx2;
            pArr2[1].X = pArr2[1].X + Dx2;
            pArr2[2].X = pArr2[2].X + Dx2;

            this.Invalidate();
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            // mp vs e.Location
            double dis = Math.Sqrt((mp.X - e.X) * (mp.X - e.X) + (mp.Y - e.Y) * (mp.Y - e.Y));
            if (dis <= 10)
            {
                Selected = true;
                dx = e.X - mp.X;
                dy = e.Y - mp.Y;
            }

            double dis2 = Math.Sqrt((mp2.X - e.X) * (mp2.X - e.X) + (mp2.Y - e.Y) * (mp2.Y - e.Y));
            if (dis2 <= 10)
            {
                Selected2 = true;
                dx2 = e.X - mp2.X;
                dy2 = e.Y - mp2.Y;
            }
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            Selected = false;
            Selected2 = false;
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (Selected == true)
            {
                mp.X = e.X - dx;
                mp.Y = e.Y - dy;
                //this.Invalidate();
            }

            if (Selected2 == true)
            {
                mp2.X = e.X - dx2;
                mp2.Y = e.Y - dy2;
                //this.Invalidate();
            }
        }
    }
}
