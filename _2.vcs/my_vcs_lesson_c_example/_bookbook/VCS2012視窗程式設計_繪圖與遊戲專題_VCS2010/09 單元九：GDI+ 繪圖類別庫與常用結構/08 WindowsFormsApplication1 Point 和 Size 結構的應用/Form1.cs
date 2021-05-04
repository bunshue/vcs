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
        Point p = new Point(); // 滑鼠游標位置
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Point p1; // 左上的矩形 的左上角的座標
            Size clientSize = this.ClientSize; // 視窗客戶區寬高
            clientSize.Width = clientSize.Width / 4; // 四分之一
            clientSize.Height = clientSize.Height / 4;

            p1 = p - clientSize; // Point結構 - Size 結構

            // 繪出 左上的矩形
            e.Graphics.DrawRectangle(Pens.Black, p1.X, p1.Y, clientSize.Width, clientSize.Height);
            // 繪出 右下的矩形
            e.Graphics.DrawRectangle(Pens.Black, p.X, p.Y, clientSize.Width, clientSize.Height);
        }

        // 滑鼠移動事件函數
        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            p = e.Location; // 最新的滑鼠游標位置
            this.Invalidate(); // 要求重畫
        }
    }
}