using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D; // for Matrix

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
            int len = this.ClientSize.Height / 7; // 第一根樹枝的高度
            Point p1 = new Point(this.ClientSize.Width / 2, this.ClientSize.Height);
            Point p2 = new Point(this.ClientSize.Width / 2, this.ClientSize.Height - len);
            e.Graphics.DrawLine(Pens.Black, p1, p2); // 繪出第一根樹枝

            Draw(e.Graphics, p2, 10, len); //呼叫 遞迴函數 開始樹木的增長
        }

        void Draw(Graphics G, Point p, int n, int len)
        {
            if (n > 0) // 共有 n 層
            {
                n = n - 1;
                int len2 = (int)(len * 0.9f); // 這一層的 樹枝的高度
                Point p1 = new Point(0, 0);
                Point p2 = new Point(0, -len2);

                G.TranslateTransform(p.X, p.Y); // 從這個點開始長出
                Matrix m = G.Transform; // 暫存目前的 矩陣 (左枝 還要用)

                // 右枝
                G.RotateTransform(15);
                G.DrawLine(Pens.Black, p1, p2);  // 長出
                Draw(G, p2, n, len2);  // 呼叫 下一層

                // 左枝
                G.Transform = m;
                G.RotateTransform(-15);
                G.DrawLine(Pens.Black, p1, p2); // 長出
                Draw(G, p2, n, len2); // 呼叫 下一層
            }
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }
    }
}
