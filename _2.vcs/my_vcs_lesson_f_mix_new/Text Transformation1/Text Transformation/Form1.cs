using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Text;
using System.Windows.Forms;

namespace Text_Transformation
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Graphics g = e.Graphics;
            string str =
            "Colors, fonts, and text are common" +
            " elements of graphics programming." +
            "In this article, you learned " +
            " about the colors, fonts and text" +
            " representations in the " +
            " .NET Framework class library. " +
            "You learned how to create " +
            "these elements and use them in GDI+. ";
            //Create a Matrix object
            Matrix M = new Matrix(1, 0, 0.5f, 1, 0, 0);
            g.RotateTransform(45.0f,
            System.Drawing.Drawing2D.MatrixOrder.Prepend);
            g.TranslateTransform(-20, -70);
            g.Transform = M;
            g.DrawString(str,
            new Font("Verdana", 10),
            new SolidBrush(Color.Blue),
            new Rectangle(50, 20, 200, 300));

        }
    }
}