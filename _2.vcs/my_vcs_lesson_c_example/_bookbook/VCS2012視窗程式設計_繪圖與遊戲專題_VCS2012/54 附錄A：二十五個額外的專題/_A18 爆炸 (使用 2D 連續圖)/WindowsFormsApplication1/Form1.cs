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
        G2D_Explores explore;
        Image image = Properties.Resources.Special2;
        public Form1()
        {
            InitializeComponent();
            explore = new G2D_Explores(image, 5, 3);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            explore.Draw(e.Graphics);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (explore.Count > 0)
            {
                explore.Update();
                this.Invalidate();
            }
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            explore.AddPos(e.Location);
        }
    }
}
