using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Drawing.Drawing2D;

namespace CH1601
{
    public partial class Form1 : Form
    {
        private Pen myPen = new Pen(Color.Black, 1);
        private Graphics G;
        private double x_center, y_center, radius;
        private double[] x = new double[10];
        private double[] y = new double[10];

        public Form1()
        {
            InitializeComponent();

            x_center = this.Size.Width / 2;
            y_center = this.Size.Height / 2 - 20;
            radius = 100;
            this.BackColor = Color.White;
            G = this.CreateGraphics();
        }

        private void Form1_Paint(object sender,
           PaintEventArgs e)
        {
            int i, j;
            for (i = 0; i <= 9; i++)
            {
                x[i] = x_center + radius * Math.Sin(
                   36 * i * Math.PI / 180.0);
                y[i] = y_center + radius * Math.Cos(
                   36 * i * Math.PI / 180);
            }
            for (i = 0; i <= 9; i++)
                for (j = 0; j <= 9; j++)
                    G.DrawLine(myPen, (int)x[i], (int)y[i],
                       (int)x[j], (int)y[j]);
        }
    }
}
