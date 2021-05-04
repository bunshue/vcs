using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace WindowsApplication1
{
    public partial class Form1 : Form
    {
        Segment seg, seg2, seg3, seg4, seg5, seg6;
        float cycle = 0;

        public Form1()
        {
            InitializeComponent();
            seg = new Segment(200,40, Color.DarkGray);
            seg2 = new Segment(150, 30, Color.Gray);

            seg3 = new Segment(200, 40, Color.DarkGray);
            seg4 = new Segment(150, 30, Color.Gray);

            seg5 = new Segment(50, 20, Color.Red);
            seg6 = new Segment(50, 20, Color.Red);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            seg.Draw(e.Graphics);
            seg2.Draw(e.Graphics);
            seg5.Draw(e.Graphics);

            seg3.Draw(e.Graphics);
            seg4.Draw(e.Graphics);
            seg6.Draw(e.Graphics);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            cycle += 0.05f;
            Walk(seg, seg2, seg5, cycle);
            Walk(seg3, seg4, seg6, (float)(cycle + Math.PI));
            this.Invalidate();
        }

        void Walk(Segment segA, Segment segB, Segment segC, float cyc)
        {
            float angle = (float)(Math.Sin(cyc) * 45 + 90); // -45 ~ 45 (往下 90)
            segA.Angle = angle;

            float angle2 = (float)(Math.Sin(cyc - Math.PI / 2) * 45 + 45); // -45 ~ 45 (往下 45)
            segB.Angle = segA.Angle + angle2;

            float angle3 = (float)(Math.Sin(cyc ) * 40 - 50); // -40 ~ 40 (往上 45)
            segC.Angle = segB.Angle + angle3;

            segA.SetPos(new PointF(400, 100));
            segB.SetPos(segA.GetPin2());
            segC.SetPos(segB.GetPin2());

            this.Invalidate();
        }

    }
}