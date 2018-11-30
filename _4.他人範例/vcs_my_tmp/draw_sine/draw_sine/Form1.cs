using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace draw_sine
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // 以紅色繪正弦波
            Graphics g = this.CreateGraphics();
            Pen p = new Pen(Color.Red, 2);
            int h = 100;
            int y1 = 100;
            double angle, y;
            float tmpy, tmpx;
            for (double x = 0; x <= 360; x++)
            {
                angle = x / 180 * Math.PI;
                y = Convert.ToDouble(y1) + Math.Sin(angle) * h;
                tmpx = Convert.ToSingle(x);
                tmpy = Convert.ToSingle(y);
                g.DrawEllipse(p, tmpx, tmpy, 1, 1); //繪製紅色圓點
            }

            g.DrawEllipse(p, 260, 260, 100, 100); //繪製紅色圓點

            SolidBrush sb = new SolidBrush(Color.Green);
            g.FillEllipse(sb, 360, 360, 100, 100); //繪製紅色圓點

        }
    }
}
