using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        Point p1, p2; // 兩個點
        int D = 1;    // 每次移動的距離
        public Form1()
        {
            InitializeComponent();
            p1 = new Point(0, 0);// 第一個點 在原點
            p2 = (Point)this.ClientSize; // 第二個點 在右下角
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.DrawLine(Pens.Black, p1, p2); // 畫出直線
        }

        // 計時器 定時更新 p1, p2 座標
        private void timer1_Tick(object sender, EventArgs e)
        {
            // 如果到邊緣 就回頭
            if (p1.X > this.ClientSize.Width || p1.X < 0)
                D = -D;

            p1.Offset(D, 0); // 移動 第一個點
            p2.Offset(-D, 0);// 移動 第二個點

            this.Invalidate();// 要求重畫 
        }
    }
}