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
        GraphicsPath gp = new GraphicsPath();
        bool show_Arrow = false;  // 是否要顯示出 箭形直線

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            int Cx = 200;
            int Cy = 100;
            int D = 50;    // 每格 寬
            int x = Cx;    // 心臟的起始點
            int y = Cy;

            //右區
            PointF[] pt = new PointF[]{
                          new PointF(x, y),
                          new PointF(x+D, y +D),
                          new PointF(x+D*2, y+D),
                          new PointF(x+D*3/2, y+D+D/2),
                          new PointF(x, y+ D*4),
                          };
            gp.AddCurve(pt, 0.6f);

            //左區
            PointF[] pt2 = new PointF[]{
                          new PointF(x, y+ D*4),
                          new PointF(x-D*3/2, y+D+D/2),
                          new PointF(x-D*2, y+D),
                          new PointF(x-D, y +D),
                          new PointF(x, y),
                          };
            gp.AddCurve(pt2, 0.6f);
        }

        // 表單重畫
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.DrawPath(myPen, gp);
            if (show_Arrow)//座標落在區域內
            {
                e.Graphics.FillPath(Brushes.Cyan, gp);
            }
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
