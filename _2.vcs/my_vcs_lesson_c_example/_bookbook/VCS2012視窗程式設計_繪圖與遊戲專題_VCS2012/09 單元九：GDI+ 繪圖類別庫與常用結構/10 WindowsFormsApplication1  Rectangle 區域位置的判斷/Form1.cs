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
        Point p;  // 滑鼠游標座標
        Pen pen = new Pen(Color.Black, 4); // 粗的黑筆
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Rectangle rect = new Rectangle(100, 50, 200, 100);
            e.Graphics.FillRectangle(Brushes.LightGreen, rect); //淡綠色矩形區塊

            Rectangle rectMouse = new Rectangle(p.X - 40, p.Y - 40, 80, 80); //紅色矩形區塊

            bool pointInRect = rect.Contains(p);  // 點在矩形區域中
            bool RectinRect = rect.Contains(rectMouse); // 矩形區域在矩形區域
            bool intersect = rect.IntersectsWith(rectMouse); // 矩形區域和矩形區域有交集

            if (pointInRect) this.Cursor = Cursors.Cross; // 改變游標形狀
            else this.Cursor = Cursors.Default;

            if (RectinRect)
            {
                e.Graphics.FillRectangle(Brushes.DarkGreen, rectMouse); //深綠色矩形區塊
                label2.Text = "深綠色矩形區塊";
            }
            else
            {
                e.Graphics.FillRectangle(Brushes.Red, rectMouse); //紅色矩形區塊
                label2.Text = "紅色矩形區塊";
            }

            if (intersect)
            {
                e.Graphics.DrawRectangle(pen, rect); //綠色矩形區塊 加外框
                label1.Text = "有交集";
            }
            else
            {
                label1.Text = "無交集";
            }

        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            p = e.Location; // 得到滑鼠游標座標
            this.Invalidate(); // 要求重畫
        }
    }
}