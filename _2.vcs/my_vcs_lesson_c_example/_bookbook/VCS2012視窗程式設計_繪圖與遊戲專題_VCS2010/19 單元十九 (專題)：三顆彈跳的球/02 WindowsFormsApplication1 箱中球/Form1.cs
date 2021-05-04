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
        BallInABox ball;   // 宣告 一個箱中球 物件
        Rectangle boxRect; // 宣告 一個箱子的位置與寬高

        public Form1()
        {
            InitializeComponent();

            // 設定 箱子的位置與寬高
            boxRect = new Rectangle(20, 20, 300, 200);
            // 新增 一個箱中球 物件
            ball = new BallInABox(new Point(150, 150), 
                         new Point(2, 3),
                         boxRect, 
                         20);

            // 調整 視窗的寬高
            this.ClientSize = new Size(boxRect.Width + boxRect.X * 2,
                                       boxRect.Height + boxRect.Y * 2);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            // 反鋸齒設定 ==> 比較好的輸出品質
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            ball.DrawBox(e.Graphics, Color.Black); // 繪出 箱子
            ball.Draw(e.Graphics, Color.Blue);     // 繪出 箱中球
        }

        // 計時器 事件處理函數
        private void timer1_Tick(object sender, EventArgs e)
        {
            ball.Update(); // 更新 箱中球 的位置
            this.Invalidate(); // 向作業系統要求重畫
        }
    }
}
