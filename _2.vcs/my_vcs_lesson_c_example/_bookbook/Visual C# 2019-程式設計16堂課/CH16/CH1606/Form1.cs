using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CH1606
{
    public partial class Form1 : Form
    {
        private Pen myPen = new Pen(Color.Black, 1);
        private Graphics G;
        private int x_center, y_center, hwidth, hheight;

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
            x_center = 60;
            y_center = 80;
            hwidth = 50;
            hheight = 40;
            for (i = 0; i < +29; i++)
            {
                G.DrawArc(myPen, x_center - hwidth,
                   y_center - hheight, 2 * hwidth,
                   2 * hheight, 0, -180);
                x_center += 4;
                y_center += 4;
                hwidth += 2;
                hheight += 2;
            }
        }
    }
}
