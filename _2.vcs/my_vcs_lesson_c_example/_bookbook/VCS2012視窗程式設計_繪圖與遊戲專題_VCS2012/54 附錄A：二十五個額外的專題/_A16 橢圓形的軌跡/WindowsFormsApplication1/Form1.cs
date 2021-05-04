// 作者：鄞永傳老師‧xnabook@yahoo.com.tw‧2012-08 
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        G2D_Circle_Grad cir01;
        G2D_EllipsePath ellipsePath;
        PointF center;
        float theta = 0;

        public Form1()
        {
            InitializeComponent();
            //this.ClientSize = new Size(256, 256);

            cir01 = new G2D_Circle_Grad(128, 0.1f, Color.White);
            center = new PointF(300, 200);
            ellipsePath = new G2D_EllipsePath(center, 200, 100);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            ellipsePath.Draw(e.Graphics);

            PointF p = ellipsePath.GetPath(theta);
            e.Graphics.DrawImage(cir01.bitmap, new PointF(p.X - cir01.bitmap.Width / 2, p.Y - cir01.bitmap.Height / 2));
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            theta = theta + 0.01f;
            this.Invalidate();
        }
    }
}
