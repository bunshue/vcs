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
        Pen pen01 = new Pen(Color.Red, 4); // 內圓 的筆刷
        Pen pen02 = new Pen(Color.Blue, 4);// 外圓 的筆刷

        double angle = 0;            // 內圓 的角度
        double angle2 = Math.PI; // 外圓 的角度
        double angleDelta = 0.1;     // 旋轉的角度遞增值

        int inner = 100; // 內圓 的半徑
        int outer = 200; // 外圓 的半徑
        int innerNo = 1; // 內圓 的小圓球數目
        int outerNo = 1; // 外圓 的小圓球數目

        public Form1()
        {
            InitializeComponent();
            // 內外圓 的筆刷樣式設定
            pen01.DashStyle = System.Drawing.Drawing2D.DashStyle.Dot;
            pen02.DashStyle = System.Drawing.Drawing2D.DashStyle.Dot;
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            // 視窗客戶區 中心點
            int x0 = this.ClientSize.Width / 2;
            int y0 = this.ClientSize.Height / 2;
            // 繪出內外圓 的大圓
            e.Graphics.DrawEllipse(pen01, x0 - inner, y0 - inner, inner * 2, inner * 2);
            e.Graphics.DrawEllipse(pen02, x0 - outer, y0 - outer, outer * 2, outer * 2);

            int x, y;
            // 繪出內圓 的旋轉小圓球
            for (int i = 0; i < innerNo; i++)
            {
                // 依旋轉角度angle算出 座標
                x = x0 + (int)((inner - 10) * Math.Cos(angle + i * (Math.PI * 2 / innerNo)));
                y = y0 + (int)((inner - 10) * Math.Sin(angle + i * (Math.PI * 2 / innerNo)));
                e.Graphics.FillEllipse(Brushes.Red, x - 10, y - 10, 20, 20);
            }

            // 繪出外圓 的旋轉小圓球
            for (int i = 0; i < outerNo; i++)
            {
                // 依旋轉角度angle2算出 座標
                x = x0 + (int)((outer - 10) * Math.Cos(angle2 + i * (Math.PI * 2 / outerNo)));
                y = y0 + (int)((outer - 10) * Math.Sin(angle2 + i * (Math.PI * 2 / outerNo)));
                e.Graphics.FillEllipse(Brushes.Blue, x - 10, y - 10, 20, 20);
            }
        }

        // 使用計時器定時更新 小圓球 的旋轉角度
        private void timer1_Tick(object sender, EventArgs e)
        {
            angle = angle + angleDelta;
            angle2 = angle2 - angleDelta;
            this.Invalidate();
        }

        // 表單重畫
        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }

        // 滑鼠按下事件
        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            int x0 = this.ClientSize.Width / 2;
            int y0 = this.ClientSize.Height / 2;
            double dist = Math.Sqrt((e.X - x0) * (e.X - x0) + (e.Y - y0) * (e.Y - y0));

            if (dist < inner) // 滑鼠在內圓按下
            {
                if (e.Button == MouseButtons.Left)  // 滑鼠左鍵 增加小圓球
                    innerNo++;
                else if (e.Button == MouseButtons.Right) // 滑鼠右鍵 減少小圓球
                {
                    if (innerNo > 0)
                        innerNo--;
                }
            }
            else if (dist < outer) // 滑鼠在外圓按下
            {
                if (e.Button == MouseButtons.Left)
                    outerNo++;
                else if (e.Button == MouseButtons.Right)
                {
                    if (outerNo > 0)
                        outerNo--;
                }
            }
        }

        // 鍵盤事件
        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyData == Keys.Space) // 空白鍵 旋轉反向
                angleDelta = -angleDelta;
            else if (e.KeyData == Keys.Up) // ↑鍵 旋轉加速
            {
                if (angleDelta > 0) angleDelta += 0.1;
                else angleDelta -= 0.1;
            }
            else if (e.KeyData == Keys.Down) // ↓鍵 旋轉減慢
            {
                if (angleDelta > 0) angleDelta -= 0.1;
                else angleDelta += 0.1;
            }
        }
    }
}