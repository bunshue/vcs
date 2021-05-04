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
            int Cx = this.ClientSize.Width / 2;   // 找到視窗客戶區中心點
            int Cy = this.ClientSize.Height / 2;

            Point p1 = new Point(Cx - 100, Cy); // 計算出 直線的兩端
            Point p2 = new Point(Cx + 100, Cy);
            gp.AddLine(p1, p2); // 將 直線 加入到 GraphicsPath物件

            Rectangle rect1 = new Rectangle(Cx - 100 - 20, Cy - 20, 40, 40);
            Rectangle rect2 = new Rectangle(Cx + 100 - 20, Cy - 20, 40, 40);
            gp.AddRectangle(rect1);  // 將 兩個矩形 加入到 GraphicsPath物件
            gp.AddRectangle(rect2);

            e.Graphics.DrawPath(Pens.Black, gp); // 繪出GraphicsPath物件
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }
    }
}