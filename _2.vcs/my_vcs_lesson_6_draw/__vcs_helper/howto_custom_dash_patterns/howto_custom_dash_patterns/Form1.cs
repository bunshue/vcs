using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace howto_custom_dash_patterns
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            ResizeRedraw = true;
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            int y = 20;
            int x1 = 65;
            int x2 = ClientSize.Width - 10;
            using (Pen dashed_pen = new Pen(Brushes.Red, 5))
            {
                dashed_pen.DashStyle = DashStyle.Custom;

                dashed_pen.DashPattern = new float[] { 3, 1 };
                e.Graphics.DrawString("3, 1", this.Font, Brushes.Black, 10, y - 8);
                e.Graphics.DrawLine(dashed_pen, x1, y, x2, y);
                y += 20;

                dashed_pen.DashPattern = new float[] { 5, 1, 5, 5 };
                e.Graphics.DrawString("5, 1, 5, 5", this.Font, Brushes.Black, 10, y - 8);
                e.Graphics.DrawLine(dashed_pen, x1, y, x2, y);
                y += 20;

                dashed_pen.DashPattern = new float[] { 5, 1 };
                e.Graphics.DrawString("5, 1", this.Font, Brushes.Black, 10, y - 8);
                e.Graphics.DrawLine(dashed_pen, x1, y, x2, y);
                y += 20;

                dashed_pen.DashPattern = new float[] { 1, 3 };
                e.Graphics.DrawString("1, 3", this.Font, Brushes.Black, 10, y - 8);
                e.Graphics.DrawLine(dashed_pen, x1, y, x2, y);
                y += 20;

                dashed_pen.DashPattern = new float[] { 3, 1, 1, 1 };
                e.Graphics.DrawString("3, 1, 1, 1", this.Font, Brushes.Black, 10, y - 8);
                e.Graphics.DrawLine(dashed_pen, x1, y, x2, y);
                y += 20;
            }
        }
    }
}
