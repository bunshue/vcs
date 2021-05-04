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
        Rectangle rect; // 矩形區域
        int D = 1; // 增加的速度
        public Form1()
        {
            InitializeComponent();
            int x = this.ClientSize.Width / 2; // 視窗客戶區的中心點
            int y = this.ClientSize.Height / 2;
            rect = new Rectangle(x - 50, y - 50, 100, 100); // 寬高100的矩形區域
        }

        // 表單重畫
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.DrawRectangle(Pens.Black, rect); // 繪出矩形
        }

        // 計時器函數
        private void timer1_Tick(object sender, EventArgs e)
        {
            if (rect.Bottom >= this.ClientSize.Height ||
                rect.Top <= 0) // 已經擴張到 上下邊界 
                D = -1;        // 反向 收縮
            else if (rect.Height < 10) // 已經收縮到 高為 10
                D = 1;                 // 反向 擴張
            rect.Inflate(D, D); // 擴張 或 收縮 矩形區域
            this.Invalidate(); // 要求重畫
        }
    }
}