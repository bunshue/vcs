// 作者：鄞永傳老師‧xnabook@yahoo.com.tw‧2012-08 
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace WindowsApplication1
{
    public partial class Form1 : Form
    {
        G2D_Line line01;

        public Form1()
        {
            InitializeComponent();

            // 中心圓的位置、旋轉角度、p1 端點 離中心圓的距離、p2 端點 離中心圓的距離
            line01 = new G2D_Line(new Point(150, 150), 0, 100, 100);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            line01.Draw(e.Graphics);
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            line01.MouseDown(e.Location);
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            line01.MouseUp(e.Location);
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            line01.MouseMove(e.Location);
            this.Invalidate();
        }

    }
}