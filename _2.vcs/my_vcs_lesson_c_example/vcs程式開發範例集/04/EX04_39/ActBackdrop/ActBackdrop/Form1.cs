using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;
using System.Drawing.Drawing2D;

namespace ActBackdrop
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        int Sect = 20;
        float[] x = new float[31];
        float[] y = new float[31];

        public void pic()
        {
            int i;
            float r;
            this.ClientSize = new Size(200, 200);
            r = this.ClientSize.Width / 2;
            Graphics g = this.CreateGraphics();
            for (i = 0; i < Sect; i++)
            {
                x[i] = (float)(r * Math.Cos(i * 2 * Math.PI / Sect) + this.ClientSize.Width / 2);
                y[i] = (float)(r * Math.Sin(i * 2 * Math.PI / Sect) + this.ClientSize.Height / 2);
            }
            for (int m = 0; m < Sect - 1; m++)
            {
                for (int n = 0; n < Sect; n++)
                {
                    g.DrawLine(Pens.Blue, x[m], y[m], x[n], y[n]);
                }
            }
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            timer1.Start();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            Graphics g = this.CreateGraphics();
            g.Clear(Color.WhiteSmoke);
            pic();
            timer1.Interval = 200; 
        }
    }
}