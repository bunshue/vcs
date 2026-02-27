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
        int D = 600; // 國旗的寬
        int Cx, Cy;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Cx = this.ClientSize.Width / 2;
            Cy = this.ClientSize.Height / 2;

            // 加入滾輪事件、指定事件處理函數
            this.MouseWheel += new System.Windows.Forms.MouseEventHandler(this.Form1_MouseWheel);
        }

        // 滾輪事件處理函數
        private void Form1_MouseWheel(object sender, MouseEventArgs e)
        {
            if (e.Delta > 0) // 滾輪往前
            {
                D = D + 10; // 間格數目變大
            }
            else if (e.Delta < 0) // 滾輪往後
            {
                D = D - 10; // 間格數目變小
                if (D < 10) D = 10; // 間格數 最小的單位
            }
            this.Invalidate(); // 要求表單重畫
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            Cx = this.ClientSize.Width / 2;
            Cy = this.ClientSize.Height / 2;
            G2D_Flag_Greenland.DrawFlag(e.Graphics, Cx, Cy, D);
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate(); // 要求表單重畫
        }
    }

    class G2D_Flag_Greenland
    {
        // 畫布、中心點、寬
        static public void DrawFlag(Graphics G, int Cx, int Cy, float w)
        {
            float h = w * 2 / 3.0f; // 高是 寬的 2 / 3
            float x = Cx - w / 2;
            float y = Cy - h / 2;
            G.FillRectangle(Brushes.White, x, y, w, h);  // 白底

            float x1 = Cx - w / 2;
            float y1 = Cy;
            G.FillRectangle(Brushes.Red, x1, y1, w, h / 2); // 下半部是紅色

            float d = w * 4.0f / 18.0f;
            float x2 = x + w * 7.0f / 18.0f - d;
            float y2 = y1 - d;
            G.FillEllipse(Brushes.Red, x2, y2, d * 2, d * 2); // 中間是一個紅色圓形

            G.FillPie(Brushes.White, x2, y2, d * 2, d * 2, 0, 180); // 圓形下半部是白色

            G.DrawRectangle(Pens.Black, x, y, w, h); // 國旗外框
        }
    }
}
