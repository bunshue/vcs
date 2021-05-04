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
        int D = 10; // 每格 寬 (全域變數)
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            GraphicsPath gp = new GraphicsPath();
            int Cx = this.ClientSize.Width / 2; // 視窗客戶區的中心點
            int Cy = this.ClientSize.Height / 2;

            //int D = 20;  // 每格 寬 (改成 全域變數)
            int x = Cx;    // 心形曲線的起始點
            int y = Cy - 2 * D;

            //心形右邊的曲線 由上往下
            PointF[] pt = new PointF[]{
                          new PointF(x, y),
                          new PointF(x+3*D, y - 1.5f*D),
                          new PointF(x+5*D, y),
                          new PointF(x+4*D, y+3*D),
                          new PointF(x, y+ 7 *D),
                          };
            gp.AddCurve(pt, 0.6f);

            //心形左邊的曲線 順時間方向 由下往上 定義點的座標
            PointF[] pt2 = new PointF[]{
                          new PointF(x, y+ 7 *D),
                          new PointF(x-4*D, y+3*D),
                          new PointF(x-5*D, y),
                          new PointF(x-3*D, y - 1.5f*D),
                          new PointF(x, y),
                          };
            gp.AddCurve(pt2, 0.6f);

            //gp.CloseFigure(); //  封閉目前的圖形
            e.Graphics.DrawPath(Pens.Black, gp); // 繪出圖形軌跡
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }

        // trackBar1 被拉扯時的事件
        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            D = trackBar1.Value; // D 等於 trackBar1 的 Value 
            this.Invalidate();  // 要求重畫
        }
    }
}