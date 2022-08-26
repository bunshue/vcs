using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace vcs_LuckyGame
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //全屏空白表單
            this.BackColor = Color.Black;
            //this.Size = new Size(800, 600);
            ControlBox = false;
            MaximizeBox = false;
            MinimizeBox = false;
            ShowIcon = false;
            ShowInTaskbar = false;
            FormBorderStyle = FormBorderStyle.None;
            StartPosition = FormStartPosition.CenterScreen;
            WindowState = FormWindowState.Maximized;
            TopMost = true;
            KeyPreview = true;

            this.DoubleClick += new EventHandler(Form1_DoubleClick);
        }

        void Form1_DoubleClick(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            this.Invalidate();

        }

        int cnt = 0;
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            int W = Screen.PrimaryScreen.WorkingArea.Width;
            int H = Screen.PrimaryScreen.WorkingArea.Height;
            int cx = W / 2;
            int cy = H / 2;
            int xx;
            int yy;

            int R = 400;
            int r = 50;

            e.Graphics.DrawEllipse(Pens.Red, cx - R, cy - R, R * 2, R * 2);

            for (int i = 0; i < 360; i += 30)
            {
                xx = cx + (int)(R * Math.Cos(Math.PI * i / 180));
                yy = cy + (int)(R * Math.Sin(Math.PI * i / 180));

                e.Graphics.DrawEllipse(Pens.Red, xx - r, yy - r, r * 2, r * 2);
            }

            xx = cx + (int)(R * Math.Cos(Math.PI * cnt / 180));
            yy = cy + (int)(R * Math.Sin(Math.PI * cnt / 180));

            e.Graphics.FillEllipse(Brushes.Red, xx - r, yy - r, r * 2, r * 2);


            cnt += 30;
        }

    }
}
