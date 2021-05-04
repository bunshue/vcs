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
        int Gap = 10; // 角度間隔
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            GraphicsPath gp = new GraphicsPath(); // GraphicsPath物件

            int Cx = this.ClientSize.Width / 2; // 視窗客戶區的正中央
            int Cy = this.ClientSize.Height / 2;
            // 圓形的半徑是取自視窗客戶區寬高最小者的四分之一
            int D1 = Math.Min(this.ClientSize.Width, this.ClientSize.Height) / 4;

            for (int i = 0; i < 360; i = i + Gap) // 每隔 Gap 角度 加入一個 圓形
            {
                int x = (int)(Cx + D1 * Math.Cos(i * Math.PI / 180));
                int y = (int)(Cy + D1 * Math.Sin(i * Math.PI / 180));
                gp.AddEllipse(x - D1, y - D1, 2 * D1, 2 * D1);
            }

            // 將 gp 內的形狀 繪出
            e.Graphics.DrawPath(Pens.Black, gp); // 繪出GraphicsPath物件
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            Gap = trackBar1.Value; // 更改角度間隔
            this.Invalidate(); // 要求重畫
        }
    }
}