using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CH1607
{
    public partial class Form1 : Form
    {
        private SolidBrush myBrush;
        private Graphics G;
        private Single p1, p2, p3;

        public Form1()
        {
            InitializeComponent();

            this.BackColor = Color.White;
            G = this.CreateGraphics();

        }

        private void Form1_Paint(object sender,
              PaintEventArgs e)
        {
            p1 = (float)0.3;
            p2 = (float)0.4;
            p3 = (float)0.3;
            myBrush = new SolidBrush(Color.Red);
            G.FillPie(myBrush, 40, 30, 200, 200, 0, 360 * p1);
            myBrush = new SolidBrush(Color.Blue);
            G.FillPie(myBrush, 40, 30, 200, 200,
               360 * p1, 360 * p2);
            myBrush = new SolidBrush(Color.Green);
            G.FillPie(myBrush, 40, 30, 200, 200,
               360 * p1 + 360 * p2, 360 * p3);
        }
    }
}
