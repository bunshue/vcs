using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D;

namespace TailorStereoEffect
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {

            Graphics ag = this.CreateGraphics();
            for (int i = 0; i < 10; i++)
            {
                Point p1 = new Point();
                p1.X = button2.Left-i;
                p1.Y = button2.Top + button2.Height+i;
                Point p2 = new Point();
                p2.X = button2.Left + button2.Width+i;
                p2.Y = button2.Top + button2.Height+i;
                ag.DrawLine(new Pen(Color.Black, 1), p1, p2);
            }
            for (int i = 0; i < 10; i++)
            {
                Point p1 = new Point();
                p1.X = button2.Left+button2.Width+i;
                p1.Y = button2.Top-i;
                Point p2 = new Point();
                p2.X = button2.Left + button2.Width+i;
                p2.Y = button2.Top + button2.Height+i;
                ag.DrawLine(new Pen(Color.Black, 1), p1, p2);
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Graphics ag = this.CreateGraphics();

            for (int i = 0; i < 10; i++)
            {
                Point p1 = new Point();
                p1.X = button2.Left - i;
                p1.Y = button2.Top;
                Point p2 = new Point();
                p2.X = button2.Left + i;
                p2.Y = button2.Top + button2.Height + i;
                ag.DrawLine(new Pen(Color.Black, 1), p1, p2);
            }
            for (int i = 0; i < 10; i++)
            {
                Point p1 = new Point();
                p1.X = button2.Left-i;
                p1.Y = button2.Top-i;
                Point p2 = new Point();
                p2.X = button2.Left + button2.Width+i;
                p2.Y = button2.Top+i;
                ag.DrawLine(new Pen(Color.Black, 1), p1, p2);
            }

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}