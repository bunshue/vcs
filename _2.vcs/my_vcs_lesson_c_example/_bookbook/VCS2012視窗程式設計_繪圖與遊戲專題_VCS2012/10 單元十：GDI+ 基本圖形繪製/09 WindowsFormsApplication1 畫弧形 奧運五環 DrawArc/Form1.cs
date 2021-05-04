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
        Pen penBlack = new Pen(Color.Black, 6); // 黑色的畫筆 筆寬為 6
        Pen penBlue = new Pen(Color.Blue, 6); // 藍色的畫筆
        Pen penRed = new Pen(Color.Red, 6);  // 紅色的畫筆
        Pen penYellow = new Pen(Color.Yellow, 6); // 黃色的畫筆
        Pen penGreen = new Pen(Color.Green, 6); // 綠色的畫筆

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            int D = 50;  // 圓的半徑
            int Gap = 20;// 圓和圓的 間距
            int Cx = this.ClientSize.Width / 2; // 抓一個中心點
            int Cy = this.ClientSize.Height / 2 - D / 2;

            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            e.Graphics.DrawEllipse(penBlack, Cx - D, Cy - D, 2 * D, 2 * D);
            e.Graphics.DrawEllipse(penBlue, Cx - 2 * D - Gap - D, Cy - D, 2 * D, 2 * D);
            e.Graphics.DrawEllipse(penRed, Cx + 2 * D + Gap - D, Cy - D, 2 * D, 2 * D);
            e.Graphics.DrawEllipse(penYellow, Cx - D - Gap / 2 - D, Cy + D - D, 2 * D, 2 * D);
            e.Graphics.DrawEllipse(penGreen, Cx + D + Gap / 2 - D, Cy + D - D, 2 * D, 2 * D);

            // 黑色的弧在上面
            e.Graphics.DrawArc(penBlack, Cx - D, Cy - D, 2 * D, 2 * D, -10, 20);
            e.Graphics.DrawArc(penBlack, Cx - D, Cy - D, 2 * D, 2 * D, 90, 20);

            // 藍色的弧在上面
            e.Graphics.DrawArc(penBlue, Cx - 2 * D - Gap - D, Cy - D, 2 * D, 2 * D, -10, 20);

            // 紅色的弧在上面
            e.Graphics.DrawArc(penRed, Cx + 2 * D + Gap - D, Cy - D, 2 * D, 2 * D, 90, 20);
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }
    }
}
