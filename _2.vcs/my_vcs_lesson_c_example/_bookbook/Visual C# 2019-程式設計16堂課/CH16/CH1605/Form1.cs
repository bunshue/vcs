using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CH1605
{
    public partial class Form1 : Form
    {
        private Pen myPen = new Pen(Color.Black, 1);
        private Graphics G;
        private int x_center, y_center, hwidth;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.BackColor = Color.White;
            G = this.CreateGraphics();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            x_center = 150;
            y_center = 10;
            hwidth = 10;
            for (int i = 0; i <= 40; i++)
            {
                G.DrawEllipse(myPen, x_center - hwidth, y_center - hwidth, 2 * hwidth, 2 * hwidth);
                y_center += 4;
                hwidth += 2;
            }
        }
    }
}
