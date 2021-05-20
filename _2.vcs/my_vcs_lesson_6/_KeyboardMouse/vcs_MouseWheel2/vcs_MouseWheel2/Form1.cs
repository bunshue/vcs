using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace vcs_MouseWheel2
{
    public partial class Form1 : Form
    {
        Point MousePos; // 滑鼠的位置
        int D = 3; // 視窗四周 每邊的間格數
        public Form1()
        {
            InitializeComponent();
            // 加入滾輪事件、指定事件處理函數
            this.MouseWheel += new System.Windows.Forms.MouseEventHandler(this.Form1_MouseWheel);
        }

        // 滾輪事件處理函數
        private void Form1_MouseWheel(object sender, MouseEventArgs e)
        {
            if (e.Delta > 0) // 滾輪往前
            {
                D++; // 間格數變大
            }
            else if (e.Delta < 0) // 滾輪往後
            {
                D--; // 間格數變小
                if (D < 1) D = 1; // 間格數 最小的單位
            }
            this.Invalidate();
        }

        // 表單重畫事件
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            int w = this.ClientSize.Width; // 視窗客戶區的寬
            int h = this.ClientSize.Height; // 視窗客戶區的高

            Point[] pt = new Point[D * 4]; // 四個邊

            int k = 0;
            for (int i = 0; i < D; i++)
                pt[k++] = new Point(w * i / D, 0);

            for (int i = 0; i < D; i++)
                pt[k++] = new Point(w, h * i / D);

            for (int i = 0; i < D; i++)
                pt[k++] = new Point(w * (D-i) / D, h);

            for (int i = 0; i < D; i++)
                pt[k++] = new Point(0, h * (D-i) / D);

            for (int i = 0; i < pt.Length; i++)
                e.Graphics.DrawLine(Pens.Black, pt[i], MousePos);

            // 每條線的 往前向量
            PointF[] vect = new PointF[pt.Length];
            double Dx, Dy;
            for (int i = 0; i < pt.Length; i++)
            {
                Dx = (pt[i].X - MousePos.X);
                Dy = (pt[i].Y - MousePos.Y);
                double dis = Math.Sqrt(Dx * Dx + Dy * Dy);
                Dx = 50 * Dx / dis; // 往前向量的長度是 50
                Dy = 50 * Dy / dis;
                vect[i] = new PointF((float)Dx, (float)Dy);
            }

            // 由內往外 走 10 圈
            for (int j = 1; j < 10; j++)
            {
                // 只走一圈
                PointF[] Net = new PointF[pt.Length];
                for (int i = 0; i < pt.Length; i++)
                {
                    Net[i].X = MousePos.X + vect[i].X * j;
                    Net[i].Y = MousePos.Y + vect[i].Y * j;
                }
                e.Graphics.DrawPolygon(Pens.Black, Net); // 用多邊形圍起來
            }

        }

        // 滑鼠移動事件
        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            MousePos = e.Location; // 記錄滑鼠的位置
            this.Invalidate(); // 要求表單重畫
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate(); // 要求表單重畫
        }
    }
}