using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace howto_dash_caps
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            int y = 20;
            using (Pen dashed_pen = new Pen(Color.Green, 15))
            {
                dashed_pen.DashStyle = DashStyle.Dash;

                dashed_pen.DashCap = DashCap.Flat;
                e.Graphics.DrawString("Flat", this.Font, Brushes.Black, 10, y - 8);
                e.Graphics.DrawLine(dashed_pen, 100, y, 250, y);
                y += 20;

                dashed_pen.DashCap = DashCap.Round;
                e.Graphics.DrawString("Round", this.Font, Brushes.Black, 10, y - 8);
                e.Graphics.DrawLine(dashed_pen, 100, y, 250, y);
                y += 20;

                dashed_pen.DashCap = DashCap.Triangle;
                e.Graphics.DrawString("Triangle", this.Font, Brushes.Black, 10, y - 8);
                e.Graphics.DrawLine(dashed_pen, 100, y, 250, y);
                y += 20;
            }
        }
    }
}
