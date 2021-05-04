// http://en.wikipedia.org/wiki/Butterfly_curve_(transcendental)
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
        G2D_Butterfly butterfly; // 蝴蝶物件
        int eX = 100;  // 蝴蝶 的目標點座標
        int eY = 100;

        public Form1()
        {
            InitializeComponent();
            butterfly = new G2D_Butterfly(3, 30);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
            e.Graphics.FillEllipse(Brushes.Red, eX-5, eY-5, 10, 10); // 畫出 目標點

            butterfly.Draw(e.Graphics);  // 畫出 蝴蝶圖案
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            butterfly.Update(eX, eY); 
            this.Invalidate();
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            eX = e.X;
            eY = e.Y;
            this.Invalidate();
        }

     
    }
}
