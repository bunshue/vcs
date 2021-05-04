using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        G2D_Flad_USA_Dynamic USA = new G2D_Flad_USA_Dynamic();
        int D = 600; // 國旗的寬
        int Cx, Cy;

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
                D=D+10; // 間格數目變大
            }
            else if (e.Delta < 0) // 滾輪往後
            {
                D=D-10; // 間格數目變小
                if (D < 10) D = 10; // 間格數 最小的單位
            }
            this.Invalidate(); // 要求表單重畫
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            Cx = this.ClientSize.Width / 2;
            Cy = this.ClientSize.Height / 2;
            USA.DrawFlag(e.Graphics, Cx, Cy, D);
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate(); // 要求表單重畫
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            this.Invalidate(); // 要求表單重畫
        }
    }
}
