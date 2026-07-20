using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Draw_DoubleBuffer1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private const int WIDTH = 100;
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            if (radioButton0.Checked == true)
            {
                this.DoubleBuffered = false;  // 不使用 DoubleBuffer
            }
            else
            {
                this.DoubleBuffered = true;  // 使用 DoubleBuffer
            }

            int r = 50;
            int cx = 320;
            int cy = 80;
            int x_st = cx - r;
            int y_st = cy - r;

            //e.Graphics.DrawEllipse(Pens.Red, cx - r, cy - r, r * 2, r * 2);

            int used = percentage;
            int total = 100;
            int used_angle = (int)(used * 360 / total);

            SolidBrush sb = new SolidBrush(Color.Gray);
            e.Graphics.FillEllipse(sb, x_st + WIDTH / 10, y_st + WIDTH / 10, WIDTH * 80 / 100, WIDTH * 80 / 100);

            sb = new SolidBrush(Color.Lime);
            e.Graphics.FillPie(sb, x_st + WIDTH / 10, y_st + WIDTH / 10, WIDTH * 80 / 100, WIDTH * 80 / 100, -90, used_angle);

            sb = new SolidBrush(Color.White);
            e.Graphics.FillEllipse(sb, x_st + WIDTH / 4, y_st + WIDTH / 4, WIDTH / 2, WIDTH / 2);
        }

        int percentage = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            this.Invalidate();
            Application.DoEvents();

            percentage++;
            if (percentage > 100)
                percentage = 0;
        }
    }
}
