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
            //Create a Graphics object
            Graphics g = this.CreateGraphics();
            g.Clear(this.BackColor);
            //Create a rectangle
            Rectangle rect =
                new Rectangle(20, 20, 100, 100);
            //Create a solid brush
            SolidBrush brush =
                new SolidBrush(Color.Red);
            //Fill Rectangle
            g.FillRectangle(brush, rect);
            //Translate
            g.TranslateTransform(100.0f, 50.0f,
                MatrixOrder.Prepend);
            //Rotate
            g.RotateTransform(45.0f,
                MatrixOrder.Prepend);

            //Scale
            g.ScaleTransform(1.75f, 0.5f);
            //Fill rectangle again
            g.FillRectangle(brush, rect);
            //Dispose of objects
            brush.Dispose();
            g.Dispose();




        }
    }
}