using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D;  // HatchBrush

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        Bitmap bm = new Bitmap(Properties.Resources.Butterfly);
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Rectangle rect = new Rectangle(0, 0, 50, 50);
            TextureBrush Mybrush = new TextureBrush(bm, rect);  // 使用的影像
            e.Graphics.FillEllipse(Mybrush, 20, 20, 400, 200); //塗刷填滿橢圓形區域
            e.Graphics.DrawEllipse(Pens.Black, 20, 20, 400, 200);  //畫出橢圓形外框
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }
    }
}