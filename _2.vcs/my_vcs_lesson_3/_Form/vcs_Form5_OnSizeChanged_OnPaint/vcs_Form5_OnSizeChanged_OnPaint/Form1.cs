using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Form5_OnSizeChanged_OnPaint
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
        protected override void OnSizeChanged(EventArgs e)
        {
            Invalidate();
            base.OnSizeChanged(e);

            label2.Text = this.Size.ToString();
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            int x_st = 0;
            int y_st = 0;
            int W = this.ClientSize.Width;
            int H = this.ClientSize.Height;
            int border = 30;
            int linewidth = 10;

            Graphics g = e.Graphics;
            Pen p = new Pen(Color.Red, linewidth);

            g.DrawRectangle(p, x_st + border, y_st + border, W - border * 2, H - border * 2);
            base.OnPaint(e);
        }
    }
}

