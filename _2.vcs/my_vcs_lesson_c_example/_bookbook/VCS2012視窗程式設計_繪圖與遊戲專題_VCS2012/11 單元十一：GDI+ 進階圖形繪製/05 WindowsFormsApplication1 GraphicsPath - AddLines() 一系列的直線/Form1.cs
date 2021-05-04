using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D;  // for GraphicsPath

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
            GraphicsPath gp = new GraphicsPath(); // GraphicsPath物件

            Point[] pt = new Point[3];  // 點陣列
            pt[0] = new Point(20, 120);
            pt[1] = new Point(120, 20);
            pt[2] = new Point(220, 120);

            gp.AddLines(pt); // 將 一系列的直線 加入到 GraphicsPath物件
            //gp.CloseFigure(); // 封閉 該形狀

            e.Graphics.DrawPath(Pens.Black, gp); // 繪出GraphicsPath物件
        }
    }
}