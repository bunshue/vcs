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

namespace CH1609
{
    public partial class Form1 : Form
    {
        private Rectangle R;
        private LinearGradientBrush myBrush;
        Graphics G;

        public Form1()
        {
            InitializeComponent();

            this.BackColor = Color.White;
            G = this.CreateGraphics();
        }

        private void Form1_Paint(object sender,
           PaintEventArgs e)
        {
            R = new Rectangle(20, 50, 80, 80);
            myBrush = new LinearGradientBrush(R,
               Color.Green, Color.Yellow, -45);
            G.FillPie(myBrush, R, 30, 300);
            R = new Rectangle(120, 70, 50, 50);
            myBrush = new LinearGradientBrush(R,
               Color.Green, Color.Yellow, -45);
            G.FillPie(myBrush, R, 30, 300);
            R = new Rectangle(190, 85, 30, 30);
            myBrush = new LinearGradientBrush(R,
               Color.Green, Color.Yellow, -45);
            G.FillPie(myBrush, R, 30, 300);
        }
    }
}
