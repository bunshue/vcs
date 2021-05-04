/* 作者：鄞永傳老師‧xnabook@yahoo.com.tw‧2010-06 */
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
        Segment Thigh1, Calf1; // 第一組 大腿、小腿
        Segment Thigh2, Calf2; // 第二組 大腿、小腿
        float cycle = 0;  // 旋轉角度
        //int pos = 0;  // X 軸位置
        Point pos = new Point(100, 200); // 大腿上節點的座標位置
        int Dx = 2;

        public Form1()
        {
            InitializeComponent();
            // 第一組 大腿、小腿
            Thigh1 = new Segment(160, 40, Color.Red);
            Calf1 = new Segment(120, 30, Color.Blue);

            // 第二組 大腿、小腿
            Thigh2 = new Segment(160, 40, Color.Green);
            Calf2 = new Segment(120, 30, Color.Yellow);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            // 反鋸齒呈現
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            // 繪出 第一組 大腿、小腿
            Thigh1.Draw(e.Graphics);
            Calf1.Draw(e.Graphics);

            // 繪出 第二組 大腿、小腿
            Thigh2.Draw(e.Graphics);
            Calf2.Draw(e.Graphics);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            cycle += 0.05f;
            // 更新 第一組 大腿、小腿 的座標 角度
            Walk(Thigh1, Calf1, cycle);

            // 更新 第二組 大腿、小腿 的座標 角度 (相位 差 90 度)
            Walk(Thigh2, Calf2, (float)(cycle + Math.PI));
            this.Invalidate();
        }

        // 更新 大腿、小腿 的座標 角度
        void Walk(Segment thigh, Segment calf, float cyc)
        {
            // 大腿的擺盪角度 是介於 -45度 ~ 45度
            float angle = (float)(Math.Sin(cyc) * 45 + 90);
            thigh.Angle = angle;

            // 小腿的擺盪角度 也是介於 -45度 ~ 45度
            // 小腿的擺盪角度 慢大腿 45度
            // 小腿的擺盪角度 受到大腿 的影響
            float angle2 = (float)(Math.Sin(cyc - Math.PI / 2) * 45 + 45);
            calf.Angle = thigh.Angle + angle2;

            pos.X += Dx; // X 軸位置 往前
            if (pos.X > this.ClientSize.Width + 200) pos.X = -200; // 超過右邊太遠
            if (pos.X < -200) pos.X = this.ClientSize.Width + 200; // 超過左邊太遠

            thigh.SetPos(new PointF(pos.X, pos.Y)); // 大腿 位置 往前
            calf.SetPos(thigh.GetPin2()); // 小腿 位置 在 大腿的下節點

            this.Invalidate();
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            // 鍵盤上下鍵調整高度
            if (e.KeyCode == Keys.Up)
                pos.Y--;
            if (e.KeyCode == Keys.Down)
                pos.Y++;

            // 鍵盤左右鍵調整往前或往後的速度
            if (e.KeyCode == Keys.Right)
                Dx++;
            if (e.KeyCode == Keys.Left)
                Dx--;
        }
    }
}
