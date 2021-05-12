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
        G2D_Radar rada;

        public Form1()
        {
            InitializeComponent();
            rada = new G2D_Radar(100,100,200);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            this.pictureBox1.Invalidate();
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            rada.Draw(e.Graphics);
        }
    }
}
