using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_test_all_99_tmp4_draw
{
    public partial class Form1 : Form
    {

        Graphics g;
        Pen pen;
        Font font;
        Brush brush;

        public Form1()
        {
            InitializeComponent();
            g = this.CreateGraphics();
            pen = new Pen(Color.Black, 3);
            font = new Font("標楷體", 16);
            brush = new SolidBrush(Color.Black);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            g.DrawEllipse(pen, 100, 100, 100, 100);
            g.DrawRectangle(pen, 0, 0, 100, 100);
            g.DrawRectangle(pen, 100, 100, 100, 100);
            g.DrawRectangle(pen, 200, 200, 100, 100);

            
        }

        private void button1_Click(object sender, EventArgs e)
        {
            g.DrawEllipse(pen, 100, 100, 100, 100);
            g.DrawRectangle(pen, 0, 0, 100, 100);
            g.DrawRectangle(pen, 100, 100, 100, 100);
            g.DrawRectangle(pen, 200, 200, 100, 100);
        }

        int xx = 110;
        private void timer1_Tick(object sender, EventArgs e)
        {
            xx++;
            g.DrawEllipse(pen, xx, xx, xx, xx);

        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
