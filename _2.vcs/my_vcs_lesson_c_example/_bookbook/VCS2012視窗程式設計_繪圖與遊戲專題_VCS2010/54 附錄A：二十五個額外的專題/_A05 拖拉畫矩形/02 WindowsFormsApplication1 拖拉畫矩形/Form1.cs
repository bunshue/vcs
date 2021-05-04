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
        float angle = 0; // 矩形的旋轉角度
        bool dragging = false; // 是否開始拖拉

        struct Apoint // 定義新結構
        {
            public Point point;  // 矩形的中心點
            public float angle;  // 矩形的旋轉角度
        }

        List<Apoint> pt = new List<Apoint>(); // 動態陣列

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            for (int i = 0; i < pt.Count; i++) // 動態陣列全部重畫
            {
                e.Graphics.ResetTransform(); // 重設畫布變換矩陣
                e.Graphics.TranslateTransform(pt[i].point.X, pt[i].point.Y); // 平移畫布原點
                e.Graphics.RotateTransform(pt[i].angle);  // 旋轉畫布
                e.Graphics.DrawRectangle(Pens.Black, -50, -50, 100, 100); // 繪出矩形
            }
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            dragging = true; // 開始拖拉
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            dragging = false; // 結束拖拉
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (!dragging) return; // 如果不是開始拖拉 就離開

            Apoint p = new Apoint(); // 定義一個新的矩形
            p.point = new Point(e.X, e.Y); // 矩形的中心點

            angle = angle + 10;
            p.angle = angle;  // 矩形的旋轉角度
            pt.Add(p);  // 加到動態陣列

            // 只繪出最新的矩形
            Graphics G = this.CreateGraphics(); // 取得 畫布
            G.TranslateTransform(e.X, e.Y); // 平移畫布原點
            G.RotateTransform(angle); // 旋轉畫布
            G.DrawRectangle(Pens.Black, -50, -50, 100, 100); // 繪出矩形
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyData == Keys.Space)
            {
                pt.Clear(); // 清空動態陣列
                this.Invalidate(); // 要求重畫
            }
        }
    }
}
