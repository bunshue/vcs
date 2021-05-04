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
            GraphicsPath gp = new GraphicsPath(); // GraphicsPath圖形軌跡物件

            int x = this.ClientSize.Width / 2; // 視窗客戶區的正中央
            int y = this.ClientSize.Height / 2;
            // 圓形的  半徑
            int D = Math.Min(this.ClientSize.Width, this.ClientSize.Height) / 8;

            gp.AddPolygon(new Point[]{
                 new Point(x - 2 * D,y - 3*D),
                 new Point(x + 2 * D,y - 3*D),
                 new Point(x + 5 * D,y ),
                 new Point(x + 2 * D,y + 3*D),
                 new Point(x - 2 * D,y + 3*D),
                 new Point(x - 5 * D,y),
               });  // 多邊形
            gp.AddEllipse(x - D, y - D, 2 * D, 2 * D);  // 在 多邊形 正中的 圓形

            Region rgn = new Region(gp); // 區域表面 物件
            LinearGradientBrush brush = new LinearGradientBrush(
                             new Point(x - 2 * D, y - 3 * D), // 線形漸層的開始點。
                             new Point(x + 2 * D, y + 3 * D), // 線形漸層的結束點。
                             Color.White,
                             Color.Red); // 線形漸層塗刷

            e.Graphics.FillRegion(brush, rgn); // 區域表面 繪出
            e.Graphics.DrawPath(Pens.Black, gp); // 圖形軌跡 繪出
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }
    }
}