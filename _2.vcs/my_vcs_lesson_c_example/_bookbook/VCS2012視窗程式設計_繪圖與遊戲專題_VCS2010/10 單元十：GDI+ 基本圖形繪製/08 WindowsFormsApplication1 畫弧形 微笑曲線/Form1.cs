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
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Pen penBlue = new Pen(Color.Blue, 5); // 藍色的畫筆
            Pen penRed = new Pen(Color.Red, 10);  // 紅色的畫筆

            int D = 100;  // 圓的半徑
            int Cx = this.ClientSize.Width / 2; // 抓一個中心點
            int Cy = this.ClientSize.Height / 2 - D / 2;

            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            // 眼睛
            e.Graphics.DrawArc(penBlue, Cx - 30 - 20, Cy + 20 - 20, 40, 40, -150, 120);
            e.Graphics.DrawArc(penBlue, Cx + 30 - 20, Cy + 20 - 20, 40, 40, -150, 120);

            // 微笑曲線
            e.Graphics.DrawArc(penRed, Cx - D, Cy - D, 2 * D, 2 * D, 45, 90);
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }
    }
}