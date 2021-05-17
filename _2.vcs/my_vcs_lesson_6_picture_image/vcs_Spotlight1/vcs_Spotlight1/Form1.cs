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
        string filename = @"C:\______test_files\__RW\_png\VanGogh.png";
        Bitmap bitmap1;
        Point[] pArr = new Point[3];
        SolidBrush brush = new SolidBrush(Color.FromArgb(64, 255, 255, 0));
        int Dx = 2;

        Point[] pArr2 = new Point[3];
        SolidBrush brush2 = new SolidBrush(Color.FromArgb(64, 0, 255, 255));
        int Dx2 = -3;

        public Form1()
        {
            InitializeComponent();

            bitmap1 = new Bitmap(filename);
            this.ClientSize = new Size(600, 600);
            pArr[0] = new Point(450, 600);
            pArr[1] = new Point(300 - 70, 0);
            pArr[2] = new Point(300 + 70, 0);

            pArr2[0] = new Point(0, 0);
            pArr2[1] = new Point(300 - 100, 600);
            pArr2[2] = new Point(300 + 100, 600);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            e.Graphics.DrawImage(bitmap1, 0, 0, bitmap1.Width, bitmap1.Height);

            GraphicsPath gp = new GraphicsPath();
            gp.AddPolygon(pArr);
            e.Graphics.FillPath(brush, gp);

            GraphicsPath gp2 = new GraphicsPath();
            gp2.AddPolygon(pArr2);
            e.Graphics.FillPath(brush2, gp2);
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
    }
}
