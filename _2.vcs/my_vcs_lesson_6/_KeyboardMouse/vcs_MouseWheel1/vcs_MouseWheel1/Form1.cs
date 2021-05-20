using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace vcs_MouseWheel1
{
    public partial class Form1 : Form
    {
        Point MousePos; // 滑鼠的位置
        int D = 3; // 視窗四周 每邊的間格數
        public Form1()
        {
            InitializeComponent();
            // 加入滾輪事件、指定事件處理函數
            this.MouseWheel += new System.Windows.Forms.MouseEventHandler(this.Form1_MouseWheel);
        }

        // 滾輪事件處理函數
        private void Form1_MouseWheel(object sender, MouseEventArgs e)
        {
            if (e.Delta > 0) // 滾輪往前
            {
                D++; // 間格數目變大
            }
            else if (e.Delta < 0) // 滾輪往後
            {
                D--; // 間格數目變小
                if (D < 1) D = 1; // 間格數 最小的單位
            }
            this.Invalidate(); // 要求表單重畫
        }

        // 表單重畫事件
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            int w = this.ClientSize.Width; // 視窗客戶區的寬
            int h = this.ClientSize.Height; // 視窗客戶區的高

            Point[] pt = new Point[D * 4]; // 四個邊

            int k = 0;
            for (int i = 0; i < D; i++) // 視窗上緣 的點座標
                pt[k++] = new Point(w * i / D, 0);

            for (int i = 0; i < D; i++) // 視窗右側 的點座標
                pt[k++] = new Point(w, h * i / D);

            for (int i = 0; i < D; i++) // 視窗下緣 的點座標
                pt[k++] = new Point(w * (D-i) / D, h);

            for (int i = 0; i < D; i++) // 視窗左側 的點座標
                pt[k++] = new Point(0, h * (D-i) / D);

            // 將全部的點座標 都連到 滑鼠的位置
            for (int i = 0; i < pt.Length; i++)
                e.Graphics.DrawLine(Pens.Black, pt[i], MousePos); 
        }

        // 滑鼠移動事件
        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            MousePos = e.Location; // 記錄滑鼠的位置
            this.Invalidate(); // 要求表單重畫
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate(); // 要求表單重畫
        }
    }
}