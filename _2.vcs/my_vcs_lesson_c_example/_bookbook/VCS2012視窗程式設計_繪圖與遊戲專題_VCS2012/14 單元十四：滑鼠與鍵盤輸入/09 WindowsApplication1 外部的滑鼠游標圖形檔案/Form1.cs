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
            this.Cursor = new Cursor("../../pen.cur"); // 外部的滑鼠游標圖形檔案
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Point pt = Cursor.Position; // 滑鼠座標
            pt = this.PointToClient(pt); // 螢幕座標 -> 視窗客戶區座標
            this.Text = pt.X.ToString() + ", " + pt.Y.ToString();
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            this.Invalidate();  // 要求表單重畫
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            this.Invalidate();  // 要求表單重畫
        }
    }
}