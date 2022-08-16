using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;

namespace vcs_Clock9
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            timer1_Tick(sender, e);
        }

        const int s_pinlen = 100;
        const int m_pinlen = 75;
        const int h_pinlen = 50;
        private void timer1_Tick(object sender, EventArgs e)
        {
            int h = DateTime.Now.Hour;
            int m = DateTime.Now.Minute;
            int s = DateTime.Now.Second;
            myClock(h, m, s);
            toolStripStatusLabel1.Text = "目前時間：" + DateTime.Now.ToLongTimeString();
        }

        private void myClock(int h, int m, int s)
        {
            Graphics g = pictureBox1.CreateGraphics();
            g.Clear(Color.White);
            Pen p = new Pen(Color.Black, 1);
            g.DrawEllipse(p, pictureBox1.ClientRectangle);
            Point CPoint = new Point(pictureBox1.ClientRectangle.Width / 2, pictureBox1.ClientRectangle.Height / 2);
            Point SPoint = new Point((int)(CPoint.X + (Math.Sin(6 * s * Math.PI / 180)) * s_pinlen), (int)(CPoint.Y - (Math.Cos(6 * s * Math.PI / 180)) * s_pinlen));
            Point MPoint = new Point((int)(CPoint.X + (Math.Sin(6 * m * Math.PI / 180)) * m_pinlen), (int)(CPoint.Y - (Math.Cos(6 * m * Math.PI / 180)) * m_pinlen));
            Point HPoint = new Point((int)(CPoint.X + (Math.Sin(((30 * h) + (m / 2)) * Math.PI / 180)) * h_pinlen), (int)(CPoint.Y - (Math.Cos(((30 * h) + (m / 2)) * Math.PI / 180)) * h_pinlen));
            g.DrawLine(p,CPoint,SPoint);
            p = new Pen(Color.Black, 2);
            g.DrawLine(p, CPoint, MPoint);
            p = new Pen(Color.Black, 4);
            g.DrawLine(p, CPoint, HPoint);
        }

    }
}