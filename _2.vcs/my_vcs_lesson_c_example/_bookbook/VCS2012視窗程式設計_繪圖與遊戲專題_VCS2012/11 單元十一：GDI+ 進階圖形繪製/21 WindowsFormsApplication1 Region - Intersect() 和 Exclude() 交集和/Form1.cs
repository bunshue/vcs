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
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            int Cx = this.ClientSize.Width / 2; // 視窗客戶區的中心點
            int Cy = this.ClientSize.Height / 2;

            GraphicsPath gp1 = new GraphicsPath(); // 圖形軌跡
            gp1.AddEllipse(Cx - 50 - 100, Cy - 100, 200, 200);

            GraphicsPath gp2 = new GraphicsPath(); // 圖形軌跡
            gp2.AddEllipse(Cx + 50 - 100, Cy - 100, 200, 200);

            Region r1 = new Region(gp1); // Region 區域表面 物件
            Region r2 = new Region(gp2); // Region 區域表面 物件
            Region r3 = new Region(gp1); // Region 區域表面 物件

            r3.Intersect(r2);  // r3 = r1 - r2   交集
            r1.Exclude(r3);    // r1 = r1 - r3   排除
            r2.Exclude(r3);    // r2 = r2 - r3   排除

            e.Graphics.FillRegion(Brushes.Red, r1);  // r1 區域表面  繪出
            e.Graphics.FillRegion(Brushes.Blue, r2); // r2 區域表面 繪出
            e.Graphics.FillRegion(Brushes.Yellow, r3); // r3 區域表面 繪出

            e.Graphics.DrawPath(Pens.Black, gp1); // 圖形軌跡 繪出
            e.Graphics.DrawPath(Pens.Black, gp2); // 圖形軌跡 繪出
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }
    }
}