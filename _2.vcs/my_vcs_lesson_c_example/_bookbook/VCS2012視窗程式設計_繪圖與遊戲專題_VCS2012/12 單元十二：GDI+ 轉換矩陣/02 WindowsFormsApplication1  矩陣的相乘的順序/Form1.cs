using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D; // for Matrix

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
            Matrix A = new Matrix(0, 1, -1, 0, 0, 0);
            Matrix B = new Matrix(1, 0, 0, 1, 1, 0);

            A.Multiply(B);  // A = B x A
            //A.Multiply(B, MatrixOrder.Prepend); // A = B x A
            //A.Multiply(B, MatrixOrder.Append);  // A = A x B

        }
    }
}