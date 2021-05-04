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
        BallInACircle ball; // 一個在圓形中的小球
        Rectangle CircleRect; // 邊界圓形的矩形區域

        public Form1()
        {
            InitializeComponent();

            CircleRect = new Rectangle(20, 20, 400, 400); // 邊界圓形的矩形區域
            ball = new BallInACircle(new PointF(210, 310), 
                         new PointF(3, 5),
                         CircleRect, 
                         10,
                         Color.Red);

            // 調整 視窗客戶區的寬高
            this.ClientSize = new Size((int)(CircleRect.Width + 2 * CircleRect.X),
                (int)(CircleRect.Height + 2 * CircleRect.Y));
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            // 反鋸齒設定 ==> 比較好的輸出品質
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            // 輔助線條
            e.Graphics.DrawLine(Pens.Silver, CircleRect.X, CircleRect.Y + CircleRect.Height / 2,
                CircleRect.X + CircleRect.Width, CircleRect.Y + CircleRect.Height / 2);

            e.Graphics.DrawLine(Pens.Silver, CircleRect.X + CircleRect.Width/ 2, CircleRect.Y,
                CircleRect.X + CircleRect.Width/2, CircleRect.Y + CircleRect.Height);


            ball.DrawCircle(e.Graphics, Color.Red); // 繪出 邊界圓形
            ball.Draw(e.Graphics, Color.Blue); // 繪出  圓形中的小球
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            ball.Update(); // 更新 小球 的位置
            this.Invalidate(); // 向作業系統要求重畫
        }
    }
}
