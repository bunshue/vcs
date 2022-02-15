using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//Form1屬性的BackColor改成Color.White
//Form1屬性的TransparencyKey改成Color.White

namespace vcs_ClockE
{
    public partial class Form1 : Form
    {
        int W = 200;
        int H = 200;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.ClientSize = new Size(W, H);

            this.FormBorderStyle = FormBorderStyle.None;
            this.TransparencyKey = Color.White;

            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point(0, 0);
            this.TopMost = true;
            //this.Invalidate();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            this.Invalidate();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Pen p = new Pen(Color.Blue, 8);
            e.Graphics.DrawEllipse(p, 10, 10, W - 20, H - 20);

            SolidBrush sb = new SolidBrush(Color.Blue);
            Font f = new Font("標楷體", 30);
            string current_time = DateTime.Now.ToString("HH:mm:ss");
            int tmp_width = 0;
            int tmp_height = 0;


            tmp_width = e.Graphics.MeasureString(current_time, f).ToSize().Width;
            tmp_height = e.Graphics.MeasureString(current_time, f).ToSize().Height;

            e.Graphics.DrawString(current_time, f, sb, new PointF((W - tmp_width) / 2 - 10, (H - tmp_height) / 2));


        }
    }
}
