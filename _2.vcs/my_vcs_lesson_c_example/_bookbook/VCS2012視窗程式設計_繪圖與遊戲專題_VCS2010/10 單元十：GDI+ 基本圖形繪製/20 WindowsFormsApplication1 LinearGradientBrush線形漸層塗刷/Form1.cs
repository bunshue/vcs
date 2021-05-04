using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D;  // HatchBrush

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            LinearGradientBrush lbrush = new LinearGradientBrush(
                   new Point(0, 0),  // 開始的位置
                   new Point(400, 200),// 結束的位置
                   Color.White, // 第一種顏色
                   Color.Blue); // 第二種顏色

            e.Graphics.FillRectangle(lbrush, 0, 0, 400, 200);
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }
    }
}