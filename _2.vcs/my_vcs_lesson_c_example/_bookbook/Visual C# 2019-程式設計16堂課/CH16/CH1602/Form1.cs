using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CH1602
{
    public partial class Form1 : Form
    {
        Pen myPen = new Pen(Color.Black, 1);
        Graphics G;
        private double x_center, y_center, radius;
        private double x, y;
        private Point[] p = new Point[100];

        public Form1()
        {
            InitializeComponent();

            x_center = this.Size.Width / 2;
            y_center = this.Size.Height / 2 - 20;
            this.BackColor = Color.White;
            G = this.CreateGraphics();
        }

        private void Form1_Paint(object sender,
            PaintEventArgs e)
        {
            radius = 100;
            for (int i = 0; i <= 99; i++)
            {
                x = x_center + radius * Math.Sin(
                   36 * i * Math.PI / 180);
                y = y_center + radius * Math.Cos(
                   36 * i * Math.PI / 180);
                p[i] = new Point((int)x, (int)y);
                radius -= 1;
            }
            G.DrawLines(myPen, p);
        }
    }
}
