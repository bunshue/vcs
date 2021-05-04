using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D; //  for Matrix

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
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            int D = this.ClientSize.Height / 6; // 第一個圓的半徑
            Point p = new Point(this.ClientSize.Width / 2, this.ClientSize.Height / 2);

            e.Graphics.TranslateTransform(p.X, p.Y); // 從這個點開始長出
            e.Graphics.FillEllipse(Brushes.Red, -D, -D, 2 * D, 2 * D); // 繪出第一個圓

            int n = 6; // 遞迴深入 6 層
            Matrix m = e.Graphics.Transform;  // 暫存目前的 矩陣
            Draw(e.Graphics, p, n, D, 0); //呼叫 遞迴函數 開始圓圈的增長 右

            e.Graphics.Transform = m;
            Draw(e.Graphics, p, n, D, 90); //呼叫 遞迴函數 開始圓圈的增長 下

            e.Graphics.Transform = m;
            Draw(e.Graphics, p, n, D, 180); //呼叫 遞迴函數 開始圓圈的增長 左

            e.Graphics.Transform = m;
            Draw(e.Graphics, p, n, D, 270); //呼叫 遞迴函數 開始圓圈的增長 上
        }

        // 遞迴函數
        void Draw(Graphics G, Point p, int n, int D, float Angle)
        {
            if (n > 0) // 共有 n 層
            {
                n = n - 1;
                int D2 = (int)(D * 0.5f); // 這一層的 圓的半徑

                Point p1 = new Point(D2, 0);
                G.RotateTransform(Angle);      // 從上一層 圓圈 長出去的角度
                G.TranslateTransform(D + D2, 0); // 從這個點開始長出
                if (n % 2 == 0) // 偶數著紅色
                    G.FillEllipse(Brushes.Red, -D2, -D2, 2 * D2, 2 * D2);
                else  // 奇數著藍色
                    G.FillEllipse(Brushes.Blue, -D2, -D2, 2 * D2, 2 * D2);

                Matrix m = G.Transform; // 暫存目前的 矩陣 
                Draw(G, p1, n, D2, 0); // 同方向 繼續長出去

                G.Transform = m; // 取回先前暫存的 矩陣 
                Draw(G, p1, n, D2, 90); // 同方向 轉 90 度繼續長出去

                G.Transform = m; // 取回先前暫存的 矩陣
                Draw(G, p1, n, D2, -90); // 同方向 轉 -90 度繼續長出去
            }
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }
    }
}