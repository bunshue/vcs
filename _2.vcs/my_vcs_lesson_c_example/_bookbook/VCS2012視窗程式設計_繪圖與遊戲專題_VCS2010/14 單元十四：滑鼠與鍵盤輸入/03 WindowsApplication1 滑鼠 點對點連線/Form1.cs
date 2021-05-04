/* 作者：鄞永傳老師‧xnabook@yahoo.com.tw‧2009-09 */
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace WindowsApplication1
{
    public partial class Form1 : Form
    {
        List<Point> pt = new List<Point>(); // 紀錄點座標的 動態陣列
        public Form1()
        {
            InitializeComponent();
        }

        // 表單重畫事件
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            int k = pt.Count; // 點的數目
            k = k * (k - 1) / 2; // 總計 連線數目

            this.Text = "滑鼠 點對點 " + pt.Count.ToString() + " 個點 = " + k.ToString() + " 條線";
            // 點對點 連線
            for (int i = 0; i < pt.Count-1; i++)
                for (int j=i+1; j<pt.Count;j++)
                    e.Graphics.DrawLine(Pens.Black, pt[i], pt[j]); 
        }

        
        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate(); // 要求表單重畫
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left) // 滑鼠左鍵 加入一個點
                pt.Add(e.Location);
            else if (e.Button == MouseButtons.Right) // 滑鼠右鍵 清除全部的點
                pt.Clear();

            this.Invalidate(); // 要求表單重畫
        }
    }
}