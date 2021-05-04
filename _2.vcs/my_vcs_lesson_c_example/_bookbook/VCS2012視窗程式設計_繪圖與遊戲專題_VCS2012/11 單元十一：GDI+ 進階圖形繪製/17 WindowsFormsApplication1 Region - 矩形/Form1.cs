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
            GraphicsPath gp = new GraphicsPath(); // GraphicsPath圖形軌跡物件
            Region rgn; // 宣告一個 Region區域表面 物件

            int Cx = this.ClientSize.Width / 2; // 視窗客戶區的中心點
            int Cy = this.ClientSize.Height / 2;
            int W = this.ClientSize.Width / 2;  // 矩形的寬
            int H = this.ClientSize.Height / 2; // 矩形的高

            Rectangle rect = new Rectangle(Cx - W / 2, Cy - H / 2, W, H);
            gp.AddRectangle(rect); // 圖形軌跡物件 加入一個矩形形狀

            rgn = new Region(gp); // 新增一個 Region 區域表面物件，以 gp 為參數
            // rgn = new Region(rect);  // 或是直接以 rect 為參數

            e.Graphics.FillRegion(Brushes.Cyan, rgn); // 區域表面 繪出
            e.Graphics.DrawPath(Pens.Black, gp); // 圖形軌跡 繪出
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }
    }
}