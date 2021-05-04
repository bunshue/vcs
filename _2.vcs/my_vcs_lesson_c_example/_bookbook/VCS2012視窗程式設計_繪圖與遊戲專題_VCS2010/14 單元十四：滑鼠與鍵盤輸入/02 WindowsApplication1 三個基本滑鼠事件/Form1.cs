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
        Bitmap mouseLeft, mouseMiddle, mouseRight, mouseNone;
        Bitmap mouseNow; // 目前要秀 的 滑鼠圖
        Point mousePos; // 記錄滑鼠的位置
        public Form1()
        {
            InitializeComponent();

            mouseLeft = Properties.Resources.mouseLeft; // 滑鼠左鍵按下圖
            mouseMiddle = Properties.Resources.mouseMiddle; // 滑鼠中鍵按下圖
            mouseRight = Properties.Resources.mouseRight; // 滑鼠右鍵按下圖
            mouseNone = Properties.Resources.mouseNone; // 滑鼠圖 無按鍵提示
            mouseNow = mouseNone; // 目前要秀 的 滑鼠圖
        }

        // 滑鼠按下事件
        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left) // 左鍵
            {
                mouseNow = mouseLeft; // 目前要秀  滑鼠左鍵按下圖
            }
            else if (e.Button == MouseButtons.Middle) // 中鍵
            {
                mouseNow = mouseMiddle; // 目前要秀  滑鼠中鍵按下圖
            }
            else if (e.Button == MouseButtons.Right) // 右鍵
            {
                mouseNow = mouseRight; // 目前要秀  滑鼠右鍵按下圖
            }
            mousePos = e.Location; // 記錄滑鼠的位置
            this.Invalidate(); // 要求表單重畫
        }

        // 滑鼠放開事件
        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            mouseNow = mouseNone; // 目前要秀  無按鍵提示的滑鼠圖 
            this.Invalidate(); // 要求表單重畫
        }

        // 滑鼠移動事件
        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            mousePos = e.Location; // 記錄滑鼠的位置
            this.Invalidate(); // 要求表單重畫
        }

        // 表單重畫事件
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            // 在 mousePos 位置 繪出 滑鼠圖
            e.Graphics.DrawImage(mouseNow, mousePos.X - mouseNow.Width / 2, mousePos.Y - mouseNow.Height / 2, mouseNow.Width, mouseNow.Height);
        }
    }
}