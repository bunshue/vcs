// 作者：鄞永傳老師‧xnabook@yahoo.com.tw‧2012-08 
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
        DisplayBoard db; // 展示板物件
        Random rd = new Random();
        int col = 40, row = 40; // 展示板的 行列數目
        int[] values; // 展示板 內 每行的高度
        double theta = 0;  // 徑度

        public Form1()
        {
            InitializeComponent();

            // 調整 視窗客戶區的寬高
            this.ClientSize = new Size(1200 + 20, 300 + 20);

            // 新增 一個展示板物件
            db = new DisplayBoard(new PointF(10, 10),  // 展示板左上角的座標
                1200, 300,  // 展示板的寬高
                col, row,  // 展示板的 行列數目
                0.5f, 0.5f);  // 小方塊間隙 與 小方塊寬高 的比例

            values = new int[col];

            db.Update(values);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            db.Draw(e.Graphics);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            theta = theta + 0.1;
            for (int i = 0; i < values.Length; i++)
            {
                values[i] = (int)((row / 2 ) * Math.Sin(theta + i * 0.1) + row / 2) + 1;
            }

            db.Update(values);
            this.Invalidate();
        }
    }
}
