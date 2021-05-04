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
        GraphicsPath gp1, gp2; // GraphicsPath圖形軌跡物件
        Region r1, r2; // Region 範圍區域 物件
        bool show_Arrow = false;  // 是否要顯示出 雙箭頭直線
        Pen myPen2 = new Pen(Color.Blue, 20); // 雙箭頭直線 的畫筆

        public Form1()
        {
            InitializeComponent();

            int Cx = this.ClientSize.Width / 2; // 視窗客戶區的中心點
            int Cy = this.ClientSize.Height / 2;

            gp1 = new GraphicsPath(); // 左側圓形的 圖形軌跡
            gp1.AddEllipse(Cx - 50 - 100, Cy - 100, 200, 200);

            gp2 = new GraphicsPath(); // 右側圓形的 圖形軌跡
            gp2.AddEllipse(Cx + 50 - 100, Cy - 100, 200, 200);

            r1 = new Region(gp1); // 左側圓形的 Region 區域表面
            r2 = new Region(gp2); // 右側圓形的 Region 區域表面

            r1.Xor(r2);  // r1 = r1 + r2 - (r1 Intersect r2) 互斥

            myPen2.StartCap = LineCap.ArrowAnchor; // 雙箭頭直線
            myPen2.EndCap = LineCap.ArrowAnchor;
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.FillRegion(Brushes.Red, r1); // r1 區域表面 繪出
            e.Graphics.DrawPath(Pens.Black, gp1); // 圖形軌跡 繪出
            e.Graphics.DrawPath(Pens.Black, gp2); // 圖形軌跡 繪出
            if (show_Arrow)
                e.Graphics.DrawLine(myPen2, 40, this.ClientSize.Height / 2, this.ClientSize.Width - 40, this.ClientSize.Height / 2);
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            // 滑鼠游標在 r1 的區域表面內 而且 雙箭頭直線 未顯示
            if (r1.IsVisible(e.Location) && !show_Arrow)
            {
                show_Arrow = true;
                this.Invalidate();
            } // 滑鼠游標不在 r1 的區域表面內 而且 雙箭頭直線 已顯示
            else if (!r1.IsVisible(e.Location) && show_Arrow)
            {
                show_Arrow = false;
                this.Invalidate();
            }
        }
    }
}