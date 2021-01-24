using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace howto_dashed_lines
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            int y = 20;
            using (Pen dashed_pen = new Pen(Color.Blue, 2))
            {
                for (int i = 0; i < 2; i++)
                {
                    dashed_pen.DashStyle = DashStyle.Dash;
                    e.Graphics.DrawString("Dash", this.Font, Brushes.Black, 10, y - 8);
                    e.Graphics.DrawLine(dashed_pen, 100, y, 250, y);
                    y += 20;

                    dashed_pen.DashStyle = DashStyle.DashDot;
                    e.Graphics.DrawString("DashDot", this.Font, Brushes.Black, 10, y - 8);
                    e.Graphics.DrawLine(dashed_pen, 100, y, 250, y);
                    y += 20;

                    dashed_pen.DashStyle = DashStyle.DashDotDot;
                    e.Graphics.DrawString("DashDotDot", this.Font, Brushes.Black, 10, y - 8);
                    e.Graphics.DrawLine(dashed_pen, 100, y, 250, y);
                    y += 20;

                    dashed_pen.DashStyle = DashStyle.Dot;
                    e.Graphics.DrawString("Dot", this.Font, Brushes.Black, 10, y - 8);
                    e.Graphics.DrawLine(dashed_pen, 100, y, 250, y);
                    y += 20;

                    y += 20;
                    dashed_pen.Width = 10;
                }
            }
        }
    }
}
