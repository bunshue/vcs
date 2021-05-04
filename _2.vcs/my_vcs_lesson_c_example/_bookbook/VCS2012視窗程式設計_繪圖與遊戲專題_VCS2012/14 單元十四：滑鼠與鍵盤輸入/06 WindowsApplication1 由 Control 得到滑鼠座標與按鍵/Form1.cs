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
            Point pt = Control.MousePosition; // 取得滑鼠游標在螢幕座標中的位置。
            pt = this.PointToClient(pt); // 螢幕座標 -> 視窗客戶區座標
            label1.Text = pt.X.ToString() + ", " + pt.Y.ToString();

            // 哪一個滑鼠按鍵處於按下狀態的值。
            if (Control.MouseButtons == MouseButtons.Left) // 滑鼠按鍵
                label2.Text = "左鍵";
            else if (Control.MouseButtons == MouseButtons.Right)
                label2.Text = "右鍵";
            else if (Control.MouseButtons == MouseButtons.Middle)
                label2.Text = "中鍵";
            else
                label2.Text = "";

            // 哪一個輔助按鍵(SHIFT、CTRL 和 ALT) 處於按下的狀態。
            if (Control.ModifierKeys == Keys.Control) 
                label3.Text = "Control 鍵";
            else if (Control.ModifierKeys == Keys.Shift)
                label3.Text = "Shift 鍵";
            else if (Control.ModifierKeys == Keys.Alt)
                label3.Text = "Alt 鍵";
            else
                label3.Text = "";
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            this.Invalidate(); // 要求表單重畫
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            this.Invalidate(); // 要求表單重畫
        }
    }
}