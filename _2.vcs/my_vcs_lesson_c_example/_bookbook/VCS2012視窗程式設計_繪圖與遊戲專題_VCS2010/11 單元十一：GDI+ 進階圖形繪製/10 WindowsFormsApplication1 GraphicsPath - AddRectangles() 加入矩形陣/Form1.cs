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
            // 第一個矩形的 寬高是取自視窗客戶區寬高最小者的一半
            int D = Math.Min(this.ClientSize.Width, this.ClientSize.Height) / 4;

            Rectangle[] rects = new Rectangle[5];
            // 第一個矩形
            rects[0] = new Rectangle(Cx - D, Cy - D, 2 * D, 2 * D);

            // 第二個矩形
            rects[1] = new Rectangle(Cx - D - 20, Cy - D - 20, 40, 40);

            // 第三個矩形
            rects[2] = new Rectangle(Cx - D + 2 * D - 20, Cy - D - 20, 40, 40);

            // 第四個矩形
            rects[3] = new Rectangle(Cx - D - 20, Cy - D + 2 * D - 20, 40, 40);

            // 第五個矩形
            rects[4] = new Rectangle(Cx - D + 2 * D - 20, Cy - D + 2 * D - 20, 40, 40);

            gp.AddRectangles(rects); // 將 矩形陣列 加入到 GraphicsPath物件

            // 將 gp 內的形狀 繪出
            e.Graphics.DrawPath(Pens.Black, gp); // 繪出GraphicsPath物件
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }
    }
}