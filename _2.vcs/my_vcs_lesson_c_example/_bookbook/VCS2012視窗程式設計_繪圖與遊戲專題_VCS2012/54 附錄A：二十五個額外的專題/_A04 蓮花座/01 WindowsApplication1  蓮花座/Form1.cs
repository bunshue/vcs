// 作者：鄞永傳老師‧xnabook@yahoo.com.tw‧2012-08 
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D;

namespace WindowsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            GraphicsPath gp = new GraphicsPath();  // GraphicsPath物件
            int Cx = this.ClientSize.Width / 2; // 視窗客戶區的中心點
            int Cy = this.ClientSize.Height / 2;

            int D = 40;    // 每格 寬
            int x = Cx;    // 心形曲線的起始點
            int y = Cy - 5 * D;

            //心形右邊的曲線 由上往下
            PointF[] pt = new PointF[]{
                          new PointF(x, y),
                          new PointF(x+1.6f*D, y + 2.5f*D),
                          new PointF(x+2.33f*D, y + 5*D),
                          new PointF(x+2.35f*D, y + 7.0f*D),
                          new PointF(x+1.6f*D, y + 8.8f*D),
                          new PointF(x, y+ 9.3f *D),
                          };
            gp.AddCurve(pt, 0.5f);

            //心形左邊的曲線 順時間方向 由下往上 定義點的座標
            PointF[] pt2 = new PointF[]{
                          new PointF(x, y+ 9.3f *D),
                          new PointF(x-1.6f*D, y + 8.8f*D),
                          new PointF(x-2.35f*D, y + 7.0f*D),
                          new PointF(x-2.33f*D, y + 5*D),
                          new PointF(x-1.6f*D, y + 2.5f*D),
                          new PointF(x, y),
                          };
            gp.AddCurve(pt2, 0.5f); 

            gp.CloseFigure(); //  封閉目前的圖形
            e.Graphics.DrawPath(Pens.Red, gp); // 繪出GraphicsPath物件

            float x0 = x - 3 * D;
            float y0 = y - 10 * D;
            float w = 6 * D;
            float h = 20 * D;

            RectangleF rect = new RectangleF(x0, y0, w, h);
            PointF[] rect3 = new PointF[3];


            rect3[0] = new PointF(x0 , y0);
            rect3[1] = new PointF(x0 + w ,y0);
            rect3[2] = new PointF(x0, y0 + h);


            Matrix myMatrix;

            for (int i = -900; i <= 900; i = i + 200)
            {
                rect3[0].X = x0 + i;
                rect3[1].X = x0 + w + i;
                myMatrix = new Matrix(rect, rect3);
                e.Graphics.Transform = myMatrix;
                e.Graphics.DrawPath(Pens.Black, gp); // 繪出GraphicsPath物件
            }
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }
    }
}