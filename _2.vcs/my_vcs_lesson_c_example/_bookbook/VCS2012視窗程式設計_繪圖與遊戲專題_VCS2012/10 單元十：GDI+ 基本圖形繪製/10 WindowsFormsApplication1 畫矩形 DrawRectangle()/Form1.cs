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
            int Cx = this.ClientSize.Width / 2;  // 總中心點
            int Cy = this.ClientSize.Height / 2;
            int W = 20;  // 寬
            int H = 100; // 高
            int D = 50;  // 總中心點 和矩形的中心點 間距

            // 繪出左右 兩個矩形
            e.Graphics.DrawRectangle(Pens.Black, Cx - D - W / 2, Cy - H / 2, W, H);
            e.Graphics.DrawRectangle(Pens.Black, Cx + D - W / 2, Cy - H / 2, W, H);

            // 繪出上下 兩個矩形
            e.Graphics.DrawRectangle(Pens.Black, Cx - H / 2, Cy - D - W / 2, H, W);
            e.Graphics.DrawRectangle(Pens.Black, Cx - H / 2, Cy + D - W / 2, H, W);
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }
    }
}