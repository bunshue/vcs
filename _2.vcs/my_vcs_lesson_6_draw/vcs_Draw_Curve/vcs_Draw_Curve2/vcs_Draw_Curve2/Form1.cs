using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Draw_Curve2
{
    public partial class Form1 : Form
    {
        float Tension = 0; // 張力 0 ~ 1
        float Tension_D = 0.05f; // 張力增減值

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Point[] pt = new Point[3]; // 定義 三個點
            pt[0] = new Point(100, this.ClientSize.Height / 2);
            //pt[1] = new Point(300, 100);
            pt[2] = new Point(this.ClientSize.Width - 100, this.ClientSize.Height / 2);

            for (int i = 0; i < ClientSize.Height; i = i + 10)
            {
                pt[1] = new Point(this.ClientSize.Width / 2, i);
                e.Graphics.DrawCurve(Pens.Black, pt, Tension); // 曲線的繪出
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            Tension = Tension + Tension_D; // 調整張力
            if (Tension >= 2 || Tension <= -1) Tension_D = -Tension_D;
            this.Invalidate();
        }
    }
}