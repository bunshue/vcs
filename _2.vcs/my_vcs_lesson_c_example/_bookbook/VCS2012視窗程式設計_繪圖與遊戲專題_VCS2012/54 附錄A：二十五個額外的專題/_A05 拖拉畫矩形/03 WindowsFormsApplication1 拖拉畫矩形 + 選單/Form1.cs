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
        Pen myPen = new Pen(Color.Black); // 畫筆

        int size = 100;  // 矩形的邊長
        Color color = Color.Black; // 矩形的顏色

        struct Apoint // 定義新結構
        {
            public Point point;  // 矩形的中心點
            public float angle;  // 矩形的旋轉角度
            public Color color;  // 矩形的顏色
            public int size;     // 矩形的邊長
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

                myPen.Color = pt[i].color;
                e.Graphics.DrawRectangle(myPen, -pt[i].size / 2, -pt[i].size / 2, pt[i].size, pt[i].size); // 繪出矩形
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

            p.color = color;
            p.size = size;
            pt.Add(p);  // 加到動態陣列

            // 只繪出最新的矩形
            Graphics G = this.CreateGraphics(); // 取得 畫布
            G.TranslateTransform(e.X, e.Y); // 平移畫布原點
            G.RotateTransform(angle); // 旋轉畫布

            myPen.Color = color;
            G.DrawRectangle(myPen, -size / 2, -size / 2, size, size); // 繪出矩形
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyData == Keys.Space)
            {
                pt.Clear(); // 清空動態陣列
                this.Invalidate(); // 要求重畫
            }
        }

        private void colorToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                color = colorDialog1.Color; // 設定顏色
            }
        }

        private void toolStripMenuItem2_Click(object sender, EventArgs e)
        {
            clearMenuItem();
            size = 200;
            toolStripMenuItem2.Checked = true;
        }

        private void toolStripMenuItem3_Click(object sender, EventArgs e)
        {
            clearMenuItem();
            size = 100;
            toolStripMenuItem3.Checked = true;
        }

        private void toolStripMenuItem4_Click(object sender, EventArgs e)
        {
            clearMenuItem();
            size = 50;
            toolStripMenuItem4.Checked = true;
        }

        private void toolStripMenuItem5_Click(object sender, EventArgs e)
        {
            clearMenuItem();
            size = 20;
            toolStripMenuItem5.Checked = true;
        }

        private void toolStripMenuItem6_Click(object sender, EventArgs e)
        {
            clearMenuItem();
            size = 10;
            toolStripMenuItem6.Checked = true;
        }

        // 清除 大小選單的 勾勾
        void clearMenuItem()
        {
            toolStripMenuItem2.Checked = false;
            toolStripMenuItem3.Checked = false;
            toolStripMenuItem4.Checked = false;
            toolStripMenuItem5.Checked = false;
            toolStripMenuItem6.Checked = false;
        }

        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
