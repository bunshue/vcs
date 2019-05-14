using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Draw_Moving
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            g = panel1.CreateGraphics();
            p = new Pen(Color.Red, 10);     // 設定畫筆為紅色、粗細為 10 點。

            g.Clear(Color.Red);             //useless??
            panel1.BackColor = Color.Pink;

        }

        double degree = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            int r = 150;
            int x;
            int y;
            degree += 0.4;
            x = r + (int)(r * Math.Cos(degree * Math.PI / 180));
            y = r + (int)(r * Math.Sin(degree * Math.PI / 180));

            g.Clear(Color.Pink);

            Point point1a = new Point(r, r);
            Point point2a = new Point(x, y);
            g.DrawLine(p, point1a, point2a);     // Draw line to screen.


        }

        int cnt = 0;
        private void timer2_Tick(object sender, EventArgs e)
        {
            cnt++;

            if ((cnt % 4) == 0)
            {
                p0.BackColor = Color.Blue;
                p1.BackColor = Color.Gray;
                p2.BackColor = Color.Gray;
                p3.BackColor = Color.Gray;
            }
            else if ((cnt % 4) == 1)
            {
                p0.BackColor = Color.Gray;
                p1.BackColor = Color.Blue;
                p2.BackColor = Color.Gray;
                p3.BackColor = Color.Gray;
            }
            else if ((cnt % 4) == 2)
            {
                p0.BackColor = Color.Gray;
                p1.BackColor = Color.Gray;
                p2.BackColor = Color.Blue;
                p3.BackColor = Color.Gray;
            }
            else if ((cnt % 4) == 3)
            {
                p0.BackColor = Color.Gray;
                p1.BackColor = Color.Gray;
                p2.BackColor = Color.Gray;
                p3.BackColor = Color.Blue;
            }
        }
    }
}
