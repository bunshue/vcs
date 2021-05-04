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
        Point p;  // 滑鼠游標座標
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Rectangle rect = new Rectangle(50, 50, 200, 100);
            e.Graphics.FillRectangle(Brushes.Green, rect); //綠色矩形區塊

            Rectangle rectMouse = new Rectangle(p.X - 40, p.Y - 40, 80, 80);
            e.Graphics.FillRectangle(Brushes.Red, rectMouse); //紅色矩形區塊

            Rectangle union = Rectangle.Union(rect, rectMouse); //聯集區域
            e.Graphics.DrawRectangle(Pens.Black, union);

            Rectangle intersect = Rectangle.Intersect(rect, rectMouse); //交集區域
            e.Graphics.FillRectangle(Brushes.Yellow, intersect);
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            p = e.Location; // 得到滑鼠游標座標
            this.Invalidate(); // 要求重畫
        }
    }
}
