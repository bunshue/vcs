// 以滑鼠位置連到中心點的角度 來帶動 小圓的角度
// 作者：鄞永傳老師‧xnabook@yahoo.com.tw‧2012-08 
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
        float Cx, Cy;  // 視窗中心點
        float D_Big, D_Small; // 大小圓的 半徑

        double theta = 0;  // 小圓的角度
        float Sx, Sy;  // 小圓的 圓心座標

        bool drag = false;
        double theta_Mouse = 0; // 滑鼠位置的角度
        double theta_Delta = 0; // theta  -  theta_Mouse

        int Gap = 2;

        public Form1()
        {
            InitializeComponent();
            this.ClientSize = new Size(600, 600);

            Cx = this.ClientSize.Width / 2;
            Cy = this.ClientSize.Height / 2;

            D_Big = Math.Min(this.ClientSize.Width, this.ClientSize.Height) * 0.3f;
            D_Small = D_Big * 0.1f; // 小圓的 半徑
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            byte R=0, G=0, B=0;

            // R 在 0 度、G 在 120 度、B 在 240 度
            R = GetColor(theta, 0);
            G = GetColor(theta, Math.PI * 2 / 3);
            B = GetColor(theta, -Math.PI * 2 / 3);
            label1.Text = "(" + R.ToString() + ", " + G.ToString() + ", " + B.ToString() + ")";

            this.BackColor = Color.FromArgb(R, G, B);
            SolidBrush myBrush = new SolidBrush(Color.FromArgb(R, G, B));
            e.Graphics.FillEllipse(Brushes.White, Cx - (D_Big + D_Small / 2) - Gap, Cy - (D_Big + D_Small / 2) - Gap, 2 * D_Big + D_Small + 2 * Gap, 2 * D_Big + D_Small + 2 * Gap);
            e.Graphics.FillEllipse(myBrush, Cx - (D_Big - D_Small / 2) + Gap, Cy - (D_Big - D_Small / 2) + Gap, 2 * D_Big - D_Small - 2 * Gap, 2 * D_Big - D_Small - 2 * Gap);   // 內圓

            Sx = (float)(Cx + D_Big * Math.Cos(theta));
            Sy = (float)(Cy + D_Big * Math.Sin(theta));
            e.Graphics.FillEllipse(Brushes.Tomato, Sx - D_Small / 2, Sy - D_Small / 2, D_Small, D_Small);
        }

        // 以 小圓的角度  得到 單一個 顏色元素的 值
        byte GetColor(double t, double offset)
        {
            t = t - offset;
            if (t < 0) t = Math.PI * 2 + t;

            if (t >= 2 * Math.PI / 3 && t <= 4 * Math.PI / 3)
                return 0;
            else if (t < 2 * Math.PI / 3)
                return (byte)(255 - 255 * t / (2 * Math.PI / 3));
            else if (t > 4 * Math.PI / 3)
            {
                t = Math.PI * 2 - t;
                return (byte)(255 - 255 * t / (2 * Math.PI / 3));
            }
            else
                return 0;
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            Cx = this.ClientSize.Width / 2;
            Cy = this.ClientSize.Height / 2;

            D_Big = Math.Min(this.ClientSize.Width, this.ClientSize.Height) * 0.3f;
            D_Small = D_Big * 0.1f;

            this.Invalidate();
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            Sx = (float)(Cx + D_Big * Math.Cos(theta));
            Sy = (float)(Cy + D_Big * Math.Sin(theta));

            double dis  = Math.Sqrt((Sx - e.X) * (Sx - e.X) + (Sy - e.Y) * (Sy - e.Y));
            if (dis <= D_Small)  //  確定有點到小圓球
            {
                drag = true;
                theta_Mouse = Math.Atan2(e.Y - Cy, e.X - Cx);
                theta_Delta = theta - theta_Mouse;
            }
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            drag = false;
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            //  轉動時以 滑鼠位置連到中心點的角度 來帶動 小圓的角度
            if (drag)
            {
                theta_Mouse = Math.Atan2(e.Y - Cy, e.X - Cx);
                theta = theta_Mouse + theta_Delta;
                this.Invalidate();
            }
        }
    }
}
