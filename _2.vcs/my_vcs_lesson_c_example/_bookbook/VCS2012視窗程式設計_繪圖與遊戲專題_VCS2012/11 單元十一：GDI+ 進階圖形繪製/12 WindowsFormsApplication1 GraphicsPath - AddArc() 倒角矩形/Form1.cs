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

            int Cx = this.ClientSize.Width / 2; // 視窗客戶區的正中央
            int Cy = this.ClientSize.Height / 2;
            // 矩形的 寬高是取自視窗客戶區寬高最小者的一半
            int D1 = Math.Min(this.ClientSize.Width, this.ClientSize.Height) / 4;

            gp.AddArc(Cx - D1, Cy - D1, 2 * D1, 2 * D1, 30, 30);
            gp.AddArc(Cx - D1, Cy - D1, 2 * D1, 2 * D1, 90 + 30, 30);
            gp.AddArc(Cx - D1, Cy - D1, 2 * D1, 2 * D1, 180 + 30, 30);
            gp.AddArc(Cx - D1, Cy - D1, 2 * D1, 2 * D1, 270 + 30, 30);
            gp.CloseFigure(); // 封閉形狀 將形狀的頭尾座標連接
            // 將 gp 內的形狀 繪出
            e.Graphics.DrawPath(Pens.Black, gp); // 繪出GraphicsPath物件
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }
    }
}