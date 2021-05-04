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
        List<Point> points = new List<Point>(); // 動態陣列 (點的座標)

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            Graphics G = this.CreateGraphics();

            if (e.Button == MouseButtons.Left) // 滑鼠左鍵
            {
                if (points.Count == 0)  // 第一個點 畫出 小橢圓形
                    G.DrawEllipse(Pens.Black, e.Location.X - 3, e.Location.Y - 3, 6, 6);
                else // 第二個點 以後 就和上一個點 相連
                    G.DrawLine(Pens.Black, points[points.Count - 1], e.Location);

                points.Add(e.Location); // 把點的資料 加到 動態陣列中
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            points.Clear(); // 清空 動態陣列
            this.Invalidate(); // 要求重畫
        }

        // 重畫事件函數
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            if (points.Count == 0) return; // 沒有點 就不用畫了

            // 第一個點 畫出 小橢圓形
            e.Graphics.DrawEllipse(Pens.Black, points[0].X - 3, points[0].Y - 3, 6, 6);

            if (points.Count > 1)  // 如果至少有兩個點
            {
                Point[] PA = new Point[points.Count];  // 建構一個點Point的陣列
                for (int i = 0; i < points.Count; i++)
                    PA[i] = points[i];
                e.Graphics.DrawLines(Pens.Black, PA); // 畫出一連串的線條
            }
        }
    }
}
