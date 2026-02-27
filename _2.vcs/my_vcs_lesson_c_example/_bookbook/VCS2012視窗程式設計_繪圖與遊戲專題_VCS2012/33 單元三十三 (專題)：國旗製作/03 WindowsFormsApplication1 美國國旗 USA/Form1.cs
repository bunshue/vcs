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
            G2D_Flag_USA.DrawFlag(e.Graphics, Cx, Cy, D);
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate(); // 要求表單重畫
        }
    }

    class G2D_Flag_USA
    {
        // 中心點、寬
        static public void DrawFlag(Graphics G, int Cx, int Cy, float w)
        {
            float h = w * 10 / 19.0f; // 高是 寬的 10 / 19
            float x0 = Cx - w / 2;
            float y0 = Cy - h / 2;
            G.FillRectangle(Brushes.White, x0, y0, w, h);

            float L = h / 13; // 條紋的寬
            for (int i = 0; i <= 6; i++)
            {
                G.FillRectangle(Brushes.Red, Cx - w / 2.0f, (Cy - h / 2.0f) + i * 2 * L, w, L);
            }

            float D = (int)(h * 0.76); // 左上 藍天
            float C = h * 7 / 13;
            G.FillRectangle(Brushes.Blue, x0, y0, D, C);

            float E = h * 0.054f;
            float H = h * 0.063f;
            float K = h * 0.0616f / 2.0f;

            float x, y;
            for (int i = 0; i < 5; i++) // 繪出奇數列 (共5列，每列6顆星星)
            {
                for (int j = 0; j < 6; j++)
                {
                    x = x0 + H + j * 2 * H;
                    y = y0 + E + i * 2 * E;
                    Star(G, x, y, K, -90);
                }
            }

            for (int i = 0; i < 4; i++) // 繪出偶數列 (共4列，每列5顆星星)
            {
                for (int j = 0; j < 5; j++)
                {
                    x = x0 + 2 * H + j * 2 * H;
                    y = y0 + 2 * E + i * 2 * E;
                    Star(G, x, y, K, -90);
                }
            }

            G.DrawRectangle(Pens.Black, Cx - w / 2, Cy - h / 2, w, h);
        }

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
