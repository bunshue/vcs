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
        Point[] pt = new Point[100]; // 一維陣列 內有 100 個 Point
        int pt_index = -1; // 一維陣列 的索引
        Image img = Properties.Resources.Butterfly; // 從資訊上載影像 

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            if (pt_index < pt.Length) // 如果一維陣列內的 100 個位置還沒裝滿
            {
                pt_index++;  // 一維陣列 的索引往前
                pt[pt_index] = new Point(e.X, e.Y); // 存入 滑鼠游標位置
            }
            this.Invalidate(); // 要求表單重畫
        }

        // 表單重畫事件函數
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            // 從一維陣列的開頭 走到 目前已有的位置 
            for (int i = 0; i <= pt_index; i++)
            {
                // 繪出 影像
                e.Graphics.DrawImage(img,
                    pt[i].X - img.Width / 2, pt[i].Y - img.Height / 2, //影像左上角在表單的位置
                    img.Width, img.Height); //影像的寬高
            }
        }
    }
}
