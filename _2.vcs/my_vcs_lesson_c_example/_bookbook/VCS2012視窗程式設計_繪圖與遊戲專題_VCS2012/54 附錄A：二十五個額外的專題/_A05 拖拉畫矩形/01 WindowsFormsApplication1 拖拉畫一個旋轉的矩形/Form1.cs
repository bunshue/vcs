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
        float angle = 0;  // 矩形的旋轉角度
        bool dragging = false; // 是否開始拖拉
        int Mx, My;  // 滑鼠的位置
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            if (dragging) // 如果是在拖拉中
            {
                e.Graphics.TranslateTransform(Mx, My);
                e.Graphics.RotateTransform(angle);
                e.Graphics.DrawRectangle(Pens.Black, -50, -50, 100, 100);
            }
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            angle = 0;
            dragging = true; // 開始拖拉
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            dragging = false;  // 取消拖拉
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            Mx = e.X;  // 記錄滑鼠的位置
            My = e.Y;
            angle = angle + 10; // 增加 旋轉角度
            this.Invalidate();
        }
    }
}
