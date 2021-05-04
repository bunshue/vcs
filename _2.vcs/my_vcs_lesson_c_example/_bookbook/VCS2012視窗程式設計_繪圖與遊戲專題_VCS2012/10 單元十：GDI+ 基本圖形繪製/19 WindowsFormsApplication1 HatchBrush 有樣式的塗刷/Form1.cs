using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D;  // HatchBrush

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            HatchBrush myBrush = new HatchBrush(HatchStyle.Cross, Color.Yellow, Color.Blue);
            e.Graphics.FillEllipse(myBrush, 10, 10, 100, 100);
            e.Graphics.DrawString("Cross", Font, Brushes.Black, 10, 110);

            HatchBrush myBrush2 = new HatchBrush(HatchStyle.DarkVertical, Color.Yellow, Color.Blue);
            e.Graphics.FillEllipse(myBrush2, 120, 10, 100, 100);
            e.Graphics.DrawString("DarkVertical", Font, Brushes.Black, 120, 110);

            HatchBrush myBrush3 = new HatchBrush(HatchStyle.DarkHorizontal, Color.Yellow, Color.Blue);
            e.Graphics.FillEllipse(myBrush3, 230, 10, 100, 100);
            e.Graphics.DrawString("DarkHorizontal", Font, Brushes.Black, 230, 110);

            HatchBrush myBrush4 = new HatchBrush(HatchStyle.DiagonalCross, Color.Yellow, Color.Blue);
            e.Graphics.FillEllipse(myBrush4, 340, 10, 100, 100);
            e.Graphics.DrawString("DiagonalCross", Font, Brushes.Black, 340, 110);

            HatchBrush myBrush5 = new HatchBrush(HatchStyle.Divot, Color.Yellow, Color.Blue);
            e.Graphics.FillEllipse(myBrush5, 450, 10, 100, 100);
            e.Graphics.DrawString("Divot", Font, Brushes.Black, 450, 110);

            HatchBrush myBrush6 = new HatchBrush(HatchStyle.Horizontal, Color.Yellow, Color.Blue);
            e.Graphics.FillEllipse(myBrush6, 560, 10, 100, 100);
            e.Graphics.DrawString("Horizontal", Font, Brushes.Black, 560, 110);

            HatchBrush myBrush7 = new HatchBrush(HatchStyle.Vertical, Color.Yellow, Color.Blue);
            e.Graphics.FillEllipse(myBrush7, 670, 10, 100, 100);
            e.Graphics.DrawString("Vertical", Font, Brushes.Black, 670, 110);

            HatchBrush myBrush8 = new HatchBrush(HatchStyle.Plaid, Color.Yellow, Color.Blue);
            e.Graphics.FillEllipse(myBrush8, 780, 10, 100, 100);
            e.Graphics.DrawString("Plaid", Font, Brushes.Black, 780, 110);



            HatchBrush myBrush9 = new HatchBrush(HatchStyle.Percent50, Color.Yellow, Color.Blue);
            e.Graphics.FillEllipse(myBrush9, 10, 160, 100, 100);
            e.Graphics.DrawString("Percent50", Font, Brushes.Black, 10, 260);

            HatchBrush myBrush10 = new HatchBrush(HatchStyle.Shingle, Color.Yellow, Color.Blue);
            e.Graphics.FillEllipse(myBrush10, 120, 160, 100, 100);
            e.Graphics.DrawString("Shingle", Font, Brushes.Black, 120, 260);

            HatchBrush myBrush11 = new HatchBrush(HatchStyle.SolidDiamond, Color.Yellow, Color.Blue);
            e.Graphics.FillEllipse(myBrush11, 230, 160, 100, 100);
            e.Graphics.DrawString("SolidDiamond", Font, Brushes.Black, 230, 260);

            HatchBrush myBrush12 = new HatchBrush(HatchStyle.Trellis, Color.Yellow, Color.Blue);
            e.Graphics.FillEllipse(myBrush12, 340, 160, 100, 100);
            e.Graphics.DrawString("Trellis", Font, Brushes.Black, 340, 260);

            HatchBrush myBrush13 = new HatchBrush(HatchStyle.Wave, Color.Yellow, Color.Blue);
            e.Graphics.FillEllipse(myBrush13, 450, 160, 100, 100);
            e.Graphics.DrawString("Wave", Font, Brushes.Black, 450, 260);

            HatchBrush myBrush14 = new HatchBrush(HatchStyle.Weave, Color.Yellow, Color.Blue);
            e.Graphics.FillEllipse(myBrush14, 560, 160, 100, 100);
            e.Graphics.DrawString("Weave", Font, Brushes.Black, 560, 260);

            HatchBrush myBrush15 = new HatchBrush(HatchStyle.SmallGrid, Color.Yellow, Color.Blue);
            e.Graphics.FillEllipse(myBrush15, 670, 160, 100, 100);
            e.Graphics.DrawString("SmallGrid", Font, Brushes.Black, 670, 260);

            HatchBrush myBrush16 = new HatchBrush(HatchStyle.ZigZag, Color.Yellow, Color.Blue);
            e.Graphics.FillEllipse(myBrush16, 780, 160, 100, 100);
            e.Graphics.DrawString("ZigZag", Font, Brushes.Black, 780, 260);
        }
    }
}