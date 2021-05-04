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
            GraphicsPath gp = new GraphicsPath();  // GraphicsPath物件
            int Cx = this.ClientSize.Width / 2;  // 視窗客戶區的中心點
            int Cy = this.ClientSize.Height / 2;

            int D = 20;    // 每格 寬
            int x = Cx;         // 心形的起始點
            int y = Cy - 2 * D;

            //心臟右邊的曲線 由上往下
            PointF[] pt = new PointF[]{
                          new PointF(x, y),
                          new PointF(x+3*D, y - 1.5f*D),
                          new PointF(x+5*D, y),
                          new PointF(x+4*D, y+3*D),
                          new PointF(x, y+ 7 *D),
                          };

            gp.AddCurve(pt, 0.6f); // 加入曲線
            e.Graphics.DrawPath(Pens.Black, gp); // 繪出圖形軌跡
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }
    }
}