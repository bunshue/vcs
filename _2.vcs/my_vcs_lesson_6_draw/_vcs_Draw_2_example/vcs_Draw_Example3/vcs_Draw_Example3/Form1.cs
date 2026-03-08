using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace vcs_Draw_Example3
{
    public partial class Form1 : Form
    {
        int D = 400; // 國旗的寬
        int Cx, Cy;

        G2D_Flad_USA_Dynamic USA = new G2D_Flad_USA_Dynamic();
        G2D_Flag_Canada_Dynamic Canada = new G2D_Flag_Canada_Dynamic();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.Size = new Size(1600, 800);
            show_item_location();

            // 加入滾輪事件、指定事件處理函數
            this.MouseWheel += new System.Windows.Forms.MouseEventHandler(this.Form1_MouseWheel);
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            //this.Invalidate(); // 要求表單重畫
            show_item_location();
            this.pictureBox0.Invalidate();
            this.pictureBox1.Invalidate();
            this.pictureBox2.Invalidate();
            this.pictureBox3.Invalidate();
            this.pictureBox4.Invalidate();
            this.pictureBox5.Invalidate();
        }

        void show_item_location()
        {
            int BORDER = 20;
            int W = this.ClientSize.Width;
            int H = this.ClientSize.Height;

            int ww = (W - BORDER * 4) / 9;
            int hh = (H - BORDER * 3) / 4;
            //richTextBox1.Text += "ww = " + ww.ToString() + "\n";
            //richTextBox1.Text += "hh = " + hh.ToString() + "\n";
            int block = (ww < hh) ? ww : hh;
            //richTextBox1.Text += "block = " + block.ToString() + "\n";

            int w = block * 3;
            int h = block * 2;
            pictureBox0.Size = new Size(w, h);
            pictureBox1.Size = new Size(w, h);
            pictureBox2.Size = new Size(w, h);
            pictureBox3.Size = new Size(w, h);
            pictureBox4.Size = new Size(w, h);
            pictureBox5.Size = new Size(w, h);

            int x_st = BORDER;
            int y_st = BORDER;
            int dx = w + BORDER;
            int dy = h + BORDER;

            pictureBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox3.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            pictureBox5.Location = new Point(x_st + dx * 2, y_st + dy * 1);
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
                if (D < 10)
                {
                    D = 10; // 間格數 最小的單位
                }
            }
            this.Invalidate(); // 要求表單重畫
            this.pictureBox0.Invalidate();
            this.pictureBox1.Invalidate();
            this.pictureBox2.Invalidate();
            this.pictureBox3.Invalidate();
            this.pictureBox4.Invalidate();
            this.pictureBox5.Invalidate();
        }

        private void pictureBox0_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            Cx = this.pictureBox0.ClientSize.Width / 2;
            Cy = this.pictureBox0.ClientSize.Height / 2;
            G2D_Flag_Greenland.DrawFlag(e.Graphics, Cx, Cy, D);
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            Cx = this.pictureBox1.ClientSize.Width / 2;
            Cy = this.pictureBox1.ClientSize.Height / 2;
            G2D_Flag_Turkey.DrawFlag(e.Graphics, Cx, Cy, D);
        }

        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            Cx = this.pictureBox2.ClientSize.Width / 2;
            Cy = this.pictureBox2.ClientSize.Height / 2;
            G2D_Flag_USA.DrawFlag(e.Graphics, Cx, Cy, D);
        }

        private void pictureBox3_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            Cx = this.pictureBox3.ClientSize.Width / 2;
            Cy = this.pictureBox3.ClientSize.Height / 2;
            USA.DrawFlag(e.Graphics, Cx, Cy, D);
        }

        private void pictureBox4_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            Cx = this.pictureBox4.ClientSize.Width / 2;
            Cy = this.pictureBox4.ClientSize.Height / 2;
            G2D_Flag_Canada.DrawFlag(e.Graphics, Cx, Cy, D);
        }

        private void pictureBox5_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            Cx = this.pictureBox5.ClientSize.Width / 2;
            Cy = this.pictureBox5.ClientSize.Height / 2;
            Canada.DrawFlag(e.Graphics, Cx, Cy, D);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            this.pictureBox3.Invalidate();
            this.pictureBox5.Invalidate();
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

    class G2D_Flad_USA_Dynamic
    {
        Random rd = new Random();
        float offset = 0;
        // 中心點、寬
        public void DrawFlag(Graphics G, int Cx, int Cy, float w)
        {
            float h = w * 10 / 19.0f; // 高是 寬的 10 / 19
            G.FillRectangle(Brushes.White, Cx - w / 2, Cy - h / 2, w, h);

            float L = h / 13; // 條紋的寬
            float x1, y1;
            offset = offset + 2;
            if (offset > L) offset = -L;
            for (int i = 0; i <= 6; i++)
            {
                x1 = Cx - w / 2.0f;
                y1 = (Cy - h / 2.0f) + i * 2 * L + offset;
                if (i == 0 && offset < 0)
                {
                    y1 = (Cy - h / 2.0f) + i * 2 * L;
                    G.FillRectangle(Brushes.Red, x1, y1, w, L + offset);
                }
                else if (i == 6 && offset > 0)
                {
                    G.FillRectangle(Brushes.Red, x1, y1, w, L - offset);
                }
                else
                    G.FillRectangle(Brushes.Red, x1, y1, w, L);
            }

            float D = (int)(h * 0.76); // 左上 藍天
            float C = h * 7 / 13;
            G.FillRectangle(Brushes.Blue, Cx - w / 2, Cy - h / 2, D, C);

            float E = h * 0.054f;
            float H = h * 0.063f;

            float K = h * 0.0616f / 2.0f;

            float x0 = Cx - w / 2;
            float y0 = Cy - h / 2;
            float x, y;
            for (int i = 0; i < 5; i++) // 繪出奇數列 (共5列，每列6顆星星)
            {
                for (int j = 0; j < 6; j++)
                {
                    x = x0 + H + j * 2 * H + (rd.Next(5) - 2);
                    y = y0 + E + i * 2 * E + (rd.Next(5) - 2);
                    Star(G, x, y, K, -90);
                }
            }

            for (int i = 0; i < 4; i++) // 繪出偶數列 (共4列，每列5顆星星)
            {
                for (int j = 0; j < 5; j++)
                {
                    x = x0 + 2 * H + j * 2 * H + (rd.Next(5) - 2);
                    y = y0 + 2 * E + i * 2 * E + (rd.Next(5) - 2);
                    Star(G, x, y, K, -90);
                }
            }

            G.DrawRectangle(Pens.Black, Cx - w / 2, Cy - h / 2, w, h);
        }

        void Star(Graphics G, float Cx, float Cy, float D, double theta0)
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

    class G2D_Flag_Canada
    {
        // 中心點、寬
        static public void DrawFlag(Graphics G, int Cx, int Cy, float w)
        {
            float h = w / 2.0f; // 高是 寬的 1/2
            float x0 = Cx - w / 2;
            float y0 = Cy - h / 2;
            G.FillRectangle(Brushes.White, x0, y0, w, h);

            float h1 = h / 32; // 格子的寬
            G.FillRectangle(Brushes.Red, x0, y0, h1 * 16, h); // 左紅色寬邊

            float x1 = Cx - w / 2 + (h1 * (16 + 32));
            float y1 = Cy - h / 2;
            G.FillRectangle(Brushes.Red, x1, y1, h1 * 16, h); // 右紅色寬邊

            Maple(G, Cx, Cy, h1); // 紅色楓葉

            G.DrawRectangle(Pens.Black, x0, y0, w, h);
        }

        static void Maple(Graphics G, float Cx, float Cy, float D)
        {
            GraphicsPath gp = new GraphicsPath();

            PointF[] pt1 = new PointF[3];
            pt1[0] = new PointF(Cx + 0 * D, Cy - 13 * D);
            pt1[1] = new PointF(Cx + 2.5f * D, Cy - 8.8f * D);
            pt1[2] = new PointF(Cx + 5.1f * D, Cy - 9.6f * D);
            gp.AddCurve(pt1, 0.4f);

            PointF[] pt2 = new PointF[3];
            pt2[0] = new PointF(Cx + 5.1f * D, Cy - 9.6f * D);
            pt2[1] = new PointF(Cx + 4 * D, Cy - 2 * D);
            pt2[2] = new PointF(Cx + 7.5f * D, Cy - 5.5f * D);
            gp.AddCurve(pt2, 0.5f);

            PointF[] pt3 = new PointF[3];
            pt3[0] = new PointF(Cx + 7.5f * D, Cy - 5.5f * D);
            pt3[1] = new PointF(Cx + 8.1f * D, Cy - 3.6f * D);
            pt3[2] = new PointF(Cx + 12 * D, Cy - 4 * D);
            gp.AddCurve(pt3, 0.3f);

            PointF[] pt4 = new PointF[3];
            pt4[0] = new PointF(Cx + 12 * D, Cy - 4 * D);
            pt4[1] = new PointF(Cx + 11 * D, Cy - 0 * D);
            pt4[2] = new PointF(Cx + 12.5f * D, Cy + 1 * D);
            gp.AddCurve(pt4, 0.3f);

            PointF[] pt5 = new PointF[3];
            pt5[0] = new PointF(Cx + 12.5f * D, Cy + 1 * D);
            pt5[1] = new PointF(Cx + 6 * D, Cy + 6 * D);
            pt5[2] = new PointF(Cx + 6.5f * D, Cy + 8.5f * D);
            gp.AddCurve(pt5, 0.3f);

            PointF[] pt6 = new PointF[12];  // 點陣列
            pt6[0] = new PointF(Cx + 6.5f * D, Cy + 8.5f * D);
            pt6[1] = new PointF(Cx + 0.5f * D, Cy + 7.5f * D);
            pt6[2] = new PointF(Cx + 0.2f * D, Cy + 8.0f * D);
            pt6[3] = new PointF(Cx + 0.2f * D, Cy + 10.5f * D);
            pt6[4] = new PointF(Cx + 0.5f * D, Cy + 10.5f * D);
            pt6[5] = new PointF(Cx + 0.5f * D, Cy + 14.0f * D);
            pt6[6] = new PointF(Cx - 0.5f * D, Cy + 14.0f * D);
            pt6[7] = new PointF(Cx - 0.5f * D, Cy + 10.5f * D);
            pt6[8] = new PointF(Cx - 0.2f * D, Cy + 10.5f * D);
            pt6[9] = new PointF(Cx - 0.2f * D, Cy + 8.0f * D);
            pt6[10] = new PointF(Cx - 0.5f * D, Cy + 7.5f * D);
            pt6[11] = new PointF(Cx - 6.5f * D, Cy + 8.5f * D);
            gp.AddLines(pt6); // 將 一系列的直線 加入到 GraphicsPath物件

            PointF[] pt7 = new PointF[3];
            pt7[2] = new PointF(Cx - 12.5f * D, Cy + 1 * D);
            pt7[1] = new PointF(Cx - 6 * D, Cy + 6 * D);
            pt7[0] = new PointF(Cx - 6.5f * D, Cy + 8.5f * D);
            gp.AddCurve(pt7, 0.3f);

            PointF[] pt8 = new PointF[3];
            pt8[2] = new PointF(Cx - 12 * D, Cy - 4 * D);
            pt8[1] = new PointF(Cx - 11 * D, Cy - 0 * D);
            pt8[0] = new PointF(Cx - 12.5f * D, Cy + 1 * D);
            gp.AddCurve(pt8, 0.3f);

            PointF[] pt9 = new PointF[3];
            pt9[2] = new PointF(Cx - 7.5f * D, Cy - 5.5f * D);
            pt9[1] = new PointF(Cx - 8.1f * D, Cy - 3.6f * D);
            pt9[0] = new PointF(Cx - 12 * D, Cy - 4 * D);
            gp.AddCurve(pt9, 0.3f);

            PointF[] pt10 = new PointF[3];
            pt10[2] = new PointF(Cx - 5.1f * D, Cy - 9.6f * D);
            pt10[1] = new PointF(Cx - 4 * D, Cy - 2 * D);
            pt10[0] = new PointF(Cx - 7.5f * D, Cy - 5.5f * D);
            gp.AddCurve(pt10, 0.5f);

            PointF[] pt11 = new PointF[3];
            pt11[2] = new PointF(Cx - 0 * D, Cy - 13 * D);
            pt11[1] = new PointF(Cx - 2.5f * D, Cy - 8.8f * D);
            pt11[0] = new PointF(Cx - 5.1f * D, Cy - 9.6f * D);
            gp.AddCurve(pt11, 0.4f);

            gp.CloseFigure();

            G.FillPath(Brushes.Red, gp);
        }
    }

    class G2D_Flag_Canada_Dynamic
    {
        // 中心點、寬
        double angle = 0;
        public void DrawFlag(Graphics G, int Cx, int Cy, float w)
        {
            float h = w / 2.0f; // 高是 寬的 1/2
            float x0 = Cx - w / 2;
            float y0 = Cy - h / 2;
            G.FillRectangle(Brushes.White, x0, y0, w, h);

            float h1 = h / 32; // 格子的寬
            G.FillRectangle(Brushes.Red, x0, y0, h1 * 16, h); // 左紅色寬邊

            float x1 = Cx - w / 2 + (h1 * (16 + 32));
            float y1 = Cy - h / 2;
            G.FillRectangle(Brushes.Red, x1, y1, h1 * 16, h); // 右紅色寬邊

            Maple(G, Cx, Cy, h1, (float)Math.Sin(angle)); // 紅色楓葉
            angle = angle + 0.03;
            G.DrawRectangle(Pens.Black, Cx - w / 2, Cy - h / 2, w, h);
        }

        void Maple(Graphics G, float Cx, float Cy, float D, float TF)
        {
            GraphicsPath gp = new GraphicsPath();

            PointF[] pt1 = new PointF[3];
            pt1[0] = new PointF(Cx + 0 * D * TF, Cy - 13 * D);
            pt1[1] = new PointF(Cx + 2.5f * D * TF, Cy - 8.8f * D);
            pt1[2] = new PointF(Cx + 5.1f * D * TF, Cy - 9.6f * D);
            gp.AddCurve(pt1, 0.4f);

            PointF[] pt2 = new PointF[3];
            pt2[0] = new PointF(Cx + 5.1f * D * TF, Cy - 9.6f * D);
            pt2[1] = new PointF(Cx + 4 * D * TF, Cy - 2 * D);
            pt2[2] = new PointF(Cx + 7.5f * D * TF, Cy - 5.5f * D);
            gp.AddCurve(pt2, 0.5f);

            PointF[] pt3 = new PointF[3];
            pt3[0] = new PointF(Cx + 7.5f * D * TF, Cy - 5.5f * D);
            pt3[1] = new PointF(Cx + 8.1f * D * TF, Cy - 3.6f * D);
            pt3[2] = new PointF(Cx + 12 * D * TF, Cy - 4 * D);
            gp.AddCurve(pt3, 0.3f);

            PointF[] pt4 = new PointF[3];
            pt4[0] = new PointF(Cx + 12 * D * TF, Cy - 4 * D);
            pt4[1] = new PointF(Cx + 11 * D * TF, Cy - 0 * D);
            pt4[2] = new PointF(Cx + 12.5f * D * TF, Cy + 1 * D);
            gp.AddCurve(pt4, 0.3f);

            PointF[] pt5 = new PointF[3];
            pt5[0] = new PointF(Cx + 12.5f * D * TF, Cy + 1 * D);
            pt5[1] = new PointF(Cx + 6 * D * TF, Cy + 6 * D);
            pt5[2] = new PointF(Cx + 6.5f * D * TF, Cy + 8.5f * D);
            gp.AddCurve(pt5, 0.3f);

            PointF[] pt6 = new PointF[12];  // 點陣列
            pt6[0] = new PointF(Cx + 6.5f * D * TF, Cy + 8.5f * D);
            pt6[1] = new PointF(Cx + 0.5f * D * TF, Cy + 7.5f * D);
            pt6[2] = new PointF(Cx + 0.2f * D * TF, Cy + 8.0f * D);
            pt6[3] = new PointF(Cx + 0.2f * D * TF, Cy + 10.5f * D);
            pt6[4] = new PointF(Cx + 0.5f * D * TF, Cy + 10.5f * D);
            pt6[5] = new PointF(Cx + 0.5f * D * TF, Cy + 14.0f * D);
            pt6[6] = new PointF(Cx - 0.5f * D * TF, Cy + 14.0f * D);
            pt6[7] = new PointF(Cx - 0.5f * D * TF, Cy + 10.5f * D);
            pt6[8] = new PointF(Cx - 0.2f * D * TF, Cy + 10.5f * D);
            pt6[9] = new PointF(Cx - 0.2f * D * TF, Cy + 8.0f * D);
            pt6[10] = new PointF(Cx - 0.5f * D * TF, Cy + 7.5f * D);
            pt6[11] = new PointF(Cx - 6.5f * D * TF, Cy + 8.5f * D);
            gp.AddLines(pt6); // 將 一系列的直線 加入到 GraphicsPath物件

            PointF[] pt7 = new PointF[3];
            pt7[2] = new PointF(Cx - 12.5f * D * TF, Cy + 1 * D);
            pt7[1] = new PointF(Cx - 6 * D * TF, Cy + 6 * D);
            pt7[0] = new PointF(Cx - 6.5f * D * TF, Cy + 8.5f * D);
            gp.AddCurve(pt7, 0.3f);

            PointF[] pt8 = new PointF[3];
            pt8[2] = new PointF(Cx - 12 * D * TF, Cy - 4 * D);
            pt8[1] = new PointF(Cx - 11 * D * TF, Cy - 0 * D);
            pt8[0] = new PointF(Cx - 12.5f * D * TF, Cy + 1 * D);
            gp.AddCurve(pt8, 0.3f);

            PointF[] pt9 = new PointF[3];
            pt9[2] = new PointF(Cx - 7.5f * D * TF, Cy - 5.5f * D);
            pt9[1] = new PointF(Cx - 8.1f * D * TF, Cy - 3.6f * D);
            pt9[0] = new PointF(Cx - 12 * D * TF, Cy - 4 * D);
            gp.AddCurve(pt9, 0.3f);

            PointF[] pt10 = new PointF[3];
            pt10[2] = new PointF(Cx - 5.1f * D * TF, Cy - 9.6f * D);
            pt10[1] = new PointF(Cx - 4 * D * TF, Cy - 2 * D);
            pt10[0] = new PointF(Cx - 7.5f * D * TF, Cy - 5.5f * D);
            gp.AddCurve(pt10, 0.5f);

            PointF[] pt11 = new PointF[3];
            pt11[2] = new PointF(Cx - 0 * D * TF, Cy - 13 * D);
            pt11[1] = new PointF(Cx - 2.5f * D * TF, Cy - 8.8f * D);
            pt11[0] = new PointF(Cx - 5.1f * D * TF, Cy - 9.6f * D);
            gp.AddCurve(pt11, 0.4f);

            gp.CloseFigure();

            G.FillPath(Brushes.Red, gp);
        }
    }
}
