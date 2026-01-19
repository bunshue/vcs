using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Draw_Curve1
{
    public partial class Form1 : Form
    {
        float Tension = 0; // 張力 0 ~ 1

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox1.Paint +=new PaintEventHandler(pictureBox1_Paint);
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            this.Text = "畫曲線  DrawCurve： 張力 = " + Tension.ToString();

            int Cx = 100;  // 基準點
            int Cy = 200;
            int D = 60; // 偏移值

            Point[] pt = new Point[4]; // 定義 四個點
            pt[0] = new Point(Cx - D, Cy + D);
            pt[1] = new Point(Cx - D, Cy - D);
            pt[2] = new Point(Cx + D, Cy - D);
            pt[3] = new Point(Cx + D, Cy + D);

            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
            e.Graphics.DrawCurve(Pens.Black, pt, Tension);  // 曲線的繪出

            for (int i = 0; i < pt.Length; i++) // 控制點的繪出
            {
                e.Graphics.DrawEllipse(Pens.Black, pt[i].X - 2, pt[i].Y - 2, 4, 4);
            }

            this.Text = "畫封閉的曲線  DrawClosedCurve： 張力 = " + Tension.ToString();
            //int Cx = 300;  // 基準點
            //int Cy = 200;
            Cx += 200;

            //int D = 60; // 偏移值

            //Point[] pt = new Point[4]; // 定義 四個點
            pt[0] = new Point(Cx - D, Cy + D);
            pt[1] = new Point(Cx - D, Cy - D);
            pt[2] = new Point(Cx + D, Cy - D);
            pt[3] = new Point(Cx + D, Cy + D);

            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
            e.Graphics.DrawClosedCurve(Pens.Black, pt, Tension, System.Drawing.Drawing2D.FillMode.Alternate);  // 曲線的繪出

            for (int i = 0; i < pt.Length; i++) // 控制點的繪出
            {
                e.Graphics.DrawEllipse(Pens.Black, pt[i].X - 2, pt[i].Y - 2, 4, 4);
            }


        }



        private void Form1_Paint(object sender, PaintEventArgs e)
        {
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            Tension += 0.1f;
            if (Tension > 1.0)
            {
                Tension = 0;
            }
            this.Text = "畫曲線  DrawCurve： 張力 = " + Tension.ToString();
            //this.Invalidate();
            this.pictureBox1.Invalidate();
        }

    }
}
