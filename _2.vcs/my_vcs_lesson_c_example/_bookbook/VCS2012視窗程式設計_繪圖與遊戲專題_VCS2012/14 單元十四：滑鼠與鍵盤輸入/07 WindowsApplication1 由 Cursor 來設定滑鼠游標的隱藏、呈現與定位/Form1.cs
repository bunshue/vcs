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
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Point pt = Cursor.Position; // 滑鼠座標
            pt = this.PointToClient(pt); // 螢幕座標 -> 視窗客戶區座標
            label1.Text = pt.X.ToString() + ", " + pt.Y.ToString();
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            this.Invalidate();  // 要求表單重畫
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            this.Invalidate();  // 要求表單重畫
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Point pt = new Point(this.ClientSize.Width / 2, this.ClientSize.Height / 2);
            Cursor.Position = this.PointToScreen(pt); // 設定滑鼠座標
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Cursor.Hide(); // 隱藏滑鼠游標
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Cursor.Show(); // 呈現滑鼠游標
        }
    }
}