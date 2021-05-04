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
        DisplayBoard db;  // 展示板物件
        Random rd = new Random();
        int col = 20, row = 15;  // 展示板的 行列數目
        int[] values;  // 展示板 內 每行的高度
        int W = 400, H = 300;  // 展示板 的 寬高
        PointF pt = new PointF(10, 10); // 展示板物件 左上角的座標

        public Form1()
        {
            InitializeComponent();

            // 調整 視窗客戶區的寬高
            this.ClientSize = new Size((int)(W + pt.X * 2), (int)(H + pt.Y * 2));

            // 新增 一個展示板物件
            db = new DisplayBoard(
                    new PointF(10, 10), // 展示板左上角的座標
                    W, H, // 展示板的寬高
                    col, row, // 展示板的 行列數目
                    0.5f, 0.5f);  // 小方塊間隙 與 小方塊寬高 的比例

            values = new int[col];
            for (int i = 0; i < values.Length; i++)
            {
                values[i] = 5;  // 預設每行的高度
            }

            db.Update(values); // 更新 展示板 每行的高度
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            db.Draw(e.Graphics);  // 繪出 展示板
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            double d;
            for (int i = 0; i < values.Length; i++)
            {
                d = rd.NextDouble(); // 以亂數當作機率
                if (d < 0.1)  // 有 0.1 的機率 第 i 行要增加
                {
                    values[i] = values[i] + 1;
                    if (values[i] > row)  // 超過 上標
                        values[i] = row;
                }
                else if (d > 0.9)  // 有 0.1 的機率 第 i 行要減少
                {
                    values[i] = values[i] - 1;
                    if (values[i] < 0)  // 低於 下標
                        values[i] = 0;
                }
            }

            db.Update(values);  // 更新 展示板 每行的高度
            this.Invalidate();  // 要求 重畫
        }
    }
}
