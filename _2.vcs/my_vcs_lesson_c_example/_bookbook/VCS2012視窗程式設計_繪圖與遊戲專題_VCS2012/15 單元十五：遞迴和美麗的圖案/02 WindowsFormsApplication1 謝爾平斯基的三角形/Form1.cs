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
        PointF[] p = new PointF[3];  // 3個點座標陣列

        public Form1()
        {
            InitializeComponent();
        }

        private void DrawTriangle(PointF p0, PointF p1, PointF p2)
        {
            Graphics G = this.CreateGraphics();// 取得 表單畫布
            G.DrawLine(Pens.Black, p0, p1); // 畫出三角形
            G.DrawLine(Pens.Black, p1, p2);
            G.DrawLine(Pens.Black, p2, p0);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // 中心點　在視窗客戶區的　正中心
            PointF center = new PointF(this.ClientSize.Width / 2, this.ClientSize.Height / 2);
            // 半徑　取短的
            float D = Math.Min(this.ClientSize.Width / 2, this.ClientSize.Height / 2) - 10;

            // 　　　　p0
            //      p2     p1 
            for (int i = 0; i < 3; i++) // 定義一個正三角形 的三個角的座標
            {
                p[i].X = (float)(center.X + D * Math.Cos(-Math.PI / 2 + i * 2 * Math.PI / 3));
                p[i].Y = (float)(center.Y + D * Math.Sin(-Math.PI / 2 + i * 2 * Math.PI / 3));
            }

            DrawTriangle(p[0], p[1], p[2]); // 畫出第一個 正三角形
            Sierp(p[0], p[1], p[2], 0);
        }

        void Sierp(PointF p0, PointF p1, PointF p2, int n)
        {
            PointF m0 = new PointF(); // 新的三個點座標
            PointF m1 = new PointF();
            PointF m2 = new PointF();

            if (n < 10)
            {
                // 　　　　p0
                //       /     \
                //     m1        m2
                //    /            \
                // p2 ---- m0 ----  p1
                //
                m2.X = (p0.X + p1.X) / 2; // 新的三個點座標
                m2.Y = (p0.Y + p1.Y) / 2;

                m1.X = (p0.X + p2.X) / 2;
                m1.Y = (p0.Y + p2.Y) / 2;

                m0.X = (p2.X + p1.X) / 2;
                m0.Y = (p2.Y + p1.Y) / 2;

                DrawTriangle(m0, m1, m2); // 畫出 新的三角形

                // 以三個新的三角形 往下呼叫
                Sierp(p0, m2, m1, n + 1);
                Sierp(m1, m0, p2, n + 1);
                Sierp(m2, p1, m0, n + 1);
            }
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }
    }
}