using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CH1604
{
    public partial class Form1 : Form
    {
        private Pen myPen = new Pen(Color.Black, 1);
        Graphics G;
        private int x_center, y_center, hwidth;
        Rectangle[] R = new Rectangle[25];

        public Form1()
        {
            InitializeComponent();

            this.BackColor = Color.White;
            G = this.CreateGraphics();
        }

        private void Form1_Paint(object sender,
              PaintEventArgs e)
        {
            int i;
            x_center = 150;
            y_center = 60;
            hwidth = 50;
            for (i = 0; i <= 24; i++)
            {
                R[i] = new Rectangle(x_center - hwidth,
                   y_center - hwidth, 2 * hwidth, 2 * hwidth);
                y_center += 4;
                hwidth += 2;
            }
            G.DrawRectangles(myPen, R);
        }
    }
}
