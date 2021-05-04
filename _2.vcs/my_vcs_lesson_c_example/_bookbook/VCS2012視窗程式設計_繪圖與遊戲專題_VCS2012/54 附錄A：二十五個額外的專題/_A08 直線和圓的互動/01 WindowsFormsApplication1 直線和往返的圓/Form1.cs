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
        int D = 100;
        G2D_OvalLine ovalLine01;

        public Form1()
        {
            InitializeComponent();

            int Cx = this.ClientSize.Width /2;
            int Cy = this.ClientSize.Height / 2;
            ovalLine01 =  new G2D_OvalLine(Cx, Cy, 0.01, Color.Blue);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            ovalLine01.Draw(e.Graphics);

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            ovalLine01.Update();
            this.Invalidate();
        }

       
    }
}
