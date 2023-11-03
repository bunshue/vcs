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

namespace CH1608
{
    public partial class Form1 : Form
    {
        private HatchBrush myBrush;
        Graphics G;
        Single p1, p2, p3;

        public Form1()
        {
            InitializeComponent();

            this.BackColor = Color.White;
            G = this.CreateGraphics();
        }

        private void Form1_Paint(object sender,
           PaintEventArgs e)
        {
            p1 = 180;
            p2 = 125;
            p3 = 160;
            myBrush = new HatchBrush(
               HatchStyle.DashedDownwardDiagonal,
               Color.White, Color.Red);
            G.FillRectangle(myBrush, 70, 250 - p1, 30, p1);
            myBrush = new HatchBrush(
               HatchStyle.DarkUpwardDiagonal,
               Color.White, Color.Blue);
            G.FillRectangle(myBrush, 120, 250 - p2, 30, p2);
            myBrush = new HatchBrush(
               HatchStyle.DiagonalCross,
               Color.White, Color.Green);
            G.FillRectangle(myBrush, 170, 250 - p3, 30, p3);
            G.DrawLine(new Pen(Color.Black, 2),
               new Point(10, 250), new Point(280, 250));
        }
    }
}
