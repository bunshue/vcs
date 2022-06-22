using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Spider
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.MouseDown += new MouseEventHandler(Form1_MouseDown);
            this.MouseMove += new MouseEventHandler(Form1_MouseMove);
            this.MouseUp += new MouseEventHandler(Form1_MouseUp);
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {

        }

        int x_st = 0;
        int y_st = 0;
        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            this.Text = e.Location.ToString();
            x_st = e.Location.X;
            y_st = e.Location.Y;

            this.Invalidate();
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {

        }

        protected override void OnPaint(PaintEventArgs e)
        {
            int W = ClientRectangle.Width;
            int H = ClientRectangle.Height;

            using (Pen pen = new Pen(Color.Red, 1))
            {
                for (int y = 0; y <= H; y += H / 12)
                {
                    e.Graphics.DrawLine(pen, new Point(x_st, y_st), new Point(0, y));
                    e.Graphics.DrawLine(pen, new Point(x_st, y_st), new Point(W, y));
                }
            }

            using (Pen pen = new Pen(Color.Green, 1))
            {
                for (int x = 0; x <= W; x += W / 12)
                {
                    e.Graphics.DrawLine(pen, new Point(x_st, y_st), new Point(x, 0));
                    e.Graphics.DrawLine(pen, new Point(x_st, y_st), new Point(x, H));
                }
            }
        }
    }
}

