using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace _15._3_1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private int c1, c2, c3;
        private Brush yellow_b, green_b, red_b;

        private void Form1_Load(object sender, EventArgs e)
        {
            this.c1 = 0;
            this.c2 = 0;
            this.c3 = 0;
            this.yellow_b = new SolidBrush(Color.Yellow);
            this.green_b = new SolidBrush(Color.Green);
            this.red_b = new SolidBrush(Color.Red);
        }

        private void candidateButton1_Click(object sender, EventArgs e)
        {
            ++this.c1;
            candidateText1.Text = this.c1.ToString();
            this.Refresh();
        }
        private void candidateButton2_Click(object sender, EventArgs e)
        {
            ++this.c2;
            candidateText2.Text = this.c2.ToString();
            this.Refresh();
        }
        private void candidateButton3_Click(object sender, EventArgs e)
        {
            ++this.c3;
            candidateText3.Text = this.c3.ToString();
            this.Refresh();
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            Graphics g = e.Graphics;
            Rectangle r = new Rectangle(20, 10, 220, 220);
            if (this.c1 != 0)
                g.FillPie(yellow_b, r, 0.0F, 360.0F * this.c1 / (this.c1 + this.c2 + this.c3));
            if (this.c2 != 0)
                g.FillPie(green_b, r, 360.0F * this.c1 / (this.c1 + this.c2 + this.c3), 360.0F * this.c2 / (this.c1 + this.c2 + this.c3));
            if (this.c3 != 0)
                g.FillPie(red_b, r, 360.0F * (this.c1 + this.c2) / (this.c1 + this.c2 + this.c3), 360.0F * this.c3 / (this.c1 + this.c2 + this.c3));
            Pen p = new Pen(Color.Black);
            if (this.c1 >= this.c2 && this.c1 >= this.c3 && this.c1 != 0)
                g.DrawPie(p, r, 0.0F, 360.0F * this.c1 / (this.c1 + this.c2 + this.c3));
            else if (this.c2 >= this.c3 && this.c2 != 0)
                g.DrawPie(p, r, 360.0F * this.c1 / (this.c1 + this.c2 + this.c3), 360.0F * this.c2 / (this.c1 + this.c2 + this.c3));
            else if (this.c3 != 0)
                g.DrawPie(p, r, 360.0F * (this.c1 + this.c2) / (this.c1 + this.c2 + this.c3), 360.0F * this.c3 / (this.c1 + this.c2 + this.c3));
            g.Dispose();
            base.OnPaint(e);
        }


    }
}
