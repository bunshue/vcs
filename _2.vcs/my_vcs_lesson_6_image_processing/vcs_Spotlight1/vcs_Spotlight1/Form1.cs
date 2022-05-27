using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D;

namespace vcs_Spotlight1
{
    public partial class Form1 : Form
    {
        string filename1 = @"C:\______test_files\__RW\_png\VanGogh.png";
        Bitmap bitmap1;
        Point[] pArr1a = new Point[3];
        Point[] pArr2a = new Point[3];
        SolidBrush brush1a = new SolidBrush(Color.FromArgb(64, 255, 255, 0));
        SolidBrush brush2a = new SolidBrush(Color.FromArgb(64, 0, 255, 255));

        int Dx1a = 2;
        int Dx2a = -3;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.pictureBox_spotlight1.ClientSize = new Size(600, 600);

            bitmap1 = new Bitmap(filename1);
            pArr1a[0] = new Point(450, 600);
            pArr1a[1] = new Point(300 - 70, 0);
            pArr1a[2] = new Point(300 + 70, 0);

            pArr2a[0] = new Point(0, 0);
            pArr2a[1] = new Point(300 - 100, 600);
            pArr2a[2] = new Point(300 + 100, 600);
        }

        private void timer_spotlight1_Tick(object sender, EventArgs e)
        {
            if (pArr1a[1].X <= 0 || pArr1a[2].X >= 600)
            {
                Dx1a = -Dx1a;
            }
            pArr1a[1].X = pArr1a[1].X + Dx1a;
            pArr1a[2].X = pArr1a[2].X + Dx1a;

            if (pArr2a[1].X <= 0 || pArr2a[2].X >= 600)
            {
                Dx2a = -Dx2a;
            }
            pArr2a[1].X = pArr2a[1].X + Dx2a;
            pArr2a[2].X = pArr2a[2].X + Dx2a;

            this.pictureBox_spotlight1.Invalidate();
        }

        private void pictureBox_spotlight1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            e.Graphics.DrawImage(bitmap1, 0, 0, bitmap1.Width, bitmap1.Height);

            GraphicsPath gp = new GraphicsPath();
            gp.AddPolygon(pArr1a);
            e.Graphics.FillPath(brush1a, gp);

            GraphicsPath gp2 = new GraphicsPath();
            gp2.AddPolygon(pArr2a);
            e.Graphics.FillPath(brush2a, gp2);

        }
    }
}
