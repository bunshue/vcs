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
            G2D_Flag_Turkey.DrawFlag(e.Graphics, Cx, Cy, D);
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate(); // 要求表單重畫
        }
    }

    class G2D_Flag_Turkey
    {
        // 畫布、中心點、寬
        static public void DrawFlag(Graphics G, int Cx, int Cy, float w)
        {
            float h = w * 2 / 3.0f; // 高是 寬的 2 / 3

            float x0 = Cx - w / 2.0f;
            float y0 = Cy - h / 2.0f;
            G.FillRectangle(Brushes.Red, x0, y0, w, h);  // 紅底

            float d1 = h / 2.0f;
            float x1 = x0 + h / 2.0f - d1 / 2.0f;
            float y1 = y0 + h / 2.0f - d1 / 2.0f;
            G.FillEllipse(Brushes.White, x1, y1, d1, d1); // 大白圓形

            float d2 = h * 2.0f / 5.0f;
            float x2 = x0 + h / 2.0f + h / 16.0f - d2 / 2.0f;
            float y2 = y0 + h / 2.0f - d2 / 2.0f;
            G.FillEllipse(Brushes.Red, x2, y2, d2, d2); // 小紅圓形

            //float x3 = x0 + h / 4.0f + (h / 4.0f - (h / 5.0f - h / 16.0f)) + h / 3.0f + h / 8.0f;
            float x3 = x0 + h / 2.0f + h / 3.0f - (h / 5.0f - h / 16.0f) + h / 8.0f;
            float y3 = y0 + h / 2.0f;
            float d3 = h / 8.0f;
            Star(G, x3, y3, d3, 180); // 星星

            G.DrawRectangle(Pens.Black, Cx - w / 2, Cy - h / 2, w, h);
        }

        // theta0 是開始的角度
        // 144 是每個星星尖角的間隔角度 = (360 / 5) * 2
        static void Star(Graphics G, float Cx, float Cy, float D, double theta0)
        {
            PointF[] pt = new PointF[5];

            for (int i = 0; i < pt.Length; i++)
            {
                float x = (float)(Cx + D * Math.Cos((theta0 + i * 144) * Math.PI / 180));
                float y = (float)(Cy + D * Math.Sin((theta0 + i * 144) * Math.PI / 180));
                pt[i] = new PointF(x, y);
            }

            GraphicsPath gp = new GraphicsPath();
            gp.AddLines(pt);
            gp.CloseFigure();
            gp.FillMode = FillMode.Winding; // 指定填滿模式

            G.FillPath(Brushes.White, gp);
        }
    }
}
