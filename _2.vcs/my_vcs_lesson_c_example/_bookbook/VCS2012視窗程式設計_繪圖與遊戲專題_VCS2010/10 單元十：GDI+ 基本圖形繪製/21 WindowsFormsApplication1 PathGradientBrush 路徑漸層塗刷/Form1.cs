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
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Point[] pt = new Point[3];  // 路徑
            pt[0] = new Point(0, 0);
            pt[1] = new Point(200, 200);
            pt[2] = new Point(400, 0);
            PathGradientBrush lbrush = new PathGradientBrush(pt);  // 中央顏色 
            lbrush.CenterColor = Color.Blue;
            Color[] colorArray = new Color[] { Color.Red, Color.Green, Color.Yellow };
            lbrush.SurroundColors = colorArray; // 路徑中點的顏色
            e.Graphics.FillRectangle(lbrush, 0, 0, 400, 200);
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }
    }
}