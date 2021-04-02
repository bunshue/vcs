using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WaveImage
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Graphics graphics = this.CreateGraphics();
            Pen myPen=new Pen(Color.Black, 1);
            int beginX = 50;
            int beginY = 65;
            int height = 35;
            int width = 50;
            Point pointX1 = new Point(beginX, beginY);
            Point pointY1 = new Point(beginX + 210, beginY);
            Point pointX2 = new Point(beginX, beginY - 45);
            Point pointY2 = new Point(beginX, beginY + 45);
            graphics.DrawLine(myPen, pointX1, pointY1);
            graphics.DrawLine(myPen, pointX2, pointY2);
            graphics.DrawBezier(myPen, beginX, beginY, beginX + 15, beginY - height, beginX + 40, beginY - height, beginX + width, beginY);
            graphics.DrawBezier(myPen, beginX + width, beginY, beginX + width + 15, beginY + height, 
                beginX + width + 40, beginY + height, beginX + width * 2, beginY);
            graphics.DrawBezier(myPen, beginX + width * 2, beginY, beginX + width * 2 + 15, beginY - height, 
                beginX + width * 2 + 40, beginY - height, beginX + width * 3, beginY);
            graphics.DrawBezier(myPen, beginX + width * 3, beginY, beginX + width * 3 + 15, beginY + height, 
                beginX + width * 3 + 40, beginY + height, beginX + width * 4, beginY);
        }
    }
}