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

            Point p1 = new Point(10, 20); // 直線的兩端
            Point p2 = new Point(100, 20);
            gp.AddLine(p1, p2); // 將 直線 加入到 GraphicsPath物件

            //gp.CloseFigure(); // 先封閉 第一條直線

            Point p3 = new Point(10, 50); // 直線的兩端
            Point p4 = new Point(100, 50);
            gp.AddLine(p3, p4); // 將第二條直線 加入到 GraphicsPath物件

            e.Graphics.DrawPath(Pens.Black, gp); // 繪出GraphicsPath物件
        }
    }
}