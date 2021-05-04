using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace _15._5_s
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            timer1.Enabled = true;
        }
        private void timer1_Tick(object sender, EventArgs e)
        {
            this.Refresh();
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            Graphics g = e.Graphics;
            Pen p = new Pen(Color.Black);
            for(int i=0; i<12; ++i)
                g.DrawArc(p, 10, 10, 280, 280, (360*i/12)-5, 10.0F);

            float hour = DateTime.Now.Hour%12 + DateTime.Now.Minute/60.0F;
            g.DrawPie(p, 80, 80, 140, 140, (360*(hour-3)/12), 2.0F);
            float minute = DateTime.Now.Minute + DateTime.Now.Second/60.0F;
            g.DrawPie(p, 60, 60, 180, 180, (360*(minute-15)/60), 1.0F);
            float second = DateTime.Now.Second;
            g.DrawPie(p, 30, 30, 240, 240, (360*(second-15)/60), 0.1F);
            
            g.Dispose();
            base.OnPaint(e);
        }

    }
}
