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
        Pen myPen = new Pen(Color.Red, 5);
        Pen myPen2 = new Pen(Color.Blue, 20);
        GraphicsPath gp = new GraphicsPath();
        bool show_Arrow = false;  // 是否要顯示出 箭形直線

        public Form1()
        {
            InitializeComponent();

            int Cx = this.ClientSize.Width / 2; // 視窗客戶區的中心點
            int Cy = this.ClientSize.Height / 2;

            int D = 20;    // 每格 寬
            int x = Cx;    // 心臟的起始點
            int y = Cy - 2 * D;

            //心臟右邊的曲線 由上往下
            PointF[] pt = new PointF[]{
                          new PointF(x, y),
                          new PointF(x+3*D, y - 1.5f*D),
                          new PointF(x+5*D, y),
                          new PointF(x+4*D, y+3*D),
                          new PointF(x, y+ 7 *D),
                          };
            gp.AddCurve(pt, 0.6f);

            //心臟左邊的曲線 順時間方向 由下往上 定義點的座標
            PointF[] pt2 = new PointF[]{
                          new PointF(x, y+ 7 *D),
                          new PointF(x-4*D, y+3*D),
                          new PointF(x-5*D, y),
                          new PointF(x-3*D, y - 1.5f*D),
                          new PointF(x, y),
                          };
            gp.AddCurve(pt2, 0.6f);

            myPen2.EndCap = LineCap.ArrowAnchor;
        }

        // 表單重畫
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.DrawPath(myPen, gp); // 繪製心形 曲線
            if (show_Arrow)
                e.Graphics.DrawLine(myPen2, 20, this.ClientSize.Height / 2,
             this.ClientSize.Width - 20, this.ClientSize.Height / 2); // 繪製箭形直線
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }

        // 滑鼠移動事件
        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            // 滑鼠游標在 gp 的形狀區域內 而且 箭形直線 未顯示
            if (gp.IsVisible(e.Location) && !show_Arrow)
            {
                show_Arrow = true; // 要顯示箭形直線
                this.Invalidate();  // 要求表單重畫
            }
            // 滑鼠游標不在 gp 的形狀區域內 而且 箭形直線 已顯示
            else if (!gp.IsVisible(e.Location) && show_Arrow)
            {
                show_Arrow = false; // 不要顯示箭形直線
                this.Invalidate();// 要求表單重畫
            }
        }
    }
}