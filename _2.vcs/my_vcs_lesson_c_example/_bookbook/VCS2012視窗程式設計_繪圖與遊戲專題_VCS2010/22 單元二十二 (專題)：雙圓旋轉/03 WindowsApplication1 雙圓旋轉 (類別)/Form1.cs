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

        ClassDoubleCircles doubleCircles, doubleCircles2;

        public Form1()
        {
            InitializeComponent();
            doubleCircles = new ClassDoubleCircles(100, 100, 50, 100);
            doubleCircles2 = new ClassDoubleCircles(400, 400, 50, 100);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            doubleCircles.Draw(e.Graphics);
            doubleCircles2.Draw(e.Graphics);
        }

        // 使用計時器定時更新 小圓球 的旋轉角度
        private void timer1_Tick(object sender, EventArgs e)
        {
            doubleCircles.Update();
            doubleCircles2.Update();
            this.Invalidate();
        }

        // 表單重畫
        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }

        // 滑鼠按下事件
        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            doubleCircles.UpdateNumber(e.Button, e.X, e.Y);
            doubleCircles2.UpdateNumber(e.Button, e.X, e.Y);
        }
    }
}