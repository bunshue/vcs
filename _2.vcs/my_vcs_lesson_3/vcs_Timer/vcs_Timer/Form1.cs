using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Timer
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox_spin.BackColor = Color.LightGray;
            this.DoubleBuffered = true;
        }

        float spin = 0;
        private void pictureBox_spin_Paint(object sender, PaintEventArgs e)
        {
            int w = pictureBox_spin.Width;
            int h = pictureBox_spin.Height;
            int cx = w / 2;
            int cy = h / 2;
            int r = Math.Min(w / 2, h / 2);
            int px = cx + (int)(r * Math.Cos(spin));
            int py = cy + (int)(r * Math.Sin(spin));
            spin += 0.30f;

            using (Pen pen = new Pen(Color.Black, 0))
            {
                e.Graphics.DrawLine(pen, cx, cy, px, py);
            }
        }

        private void timer_spin_Tick(object sender, EventArgs e)
        {
            this.pictureBox_spin.Refresh();
        }


    }
}
