using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void calButton_Click(object sender, EventArgs e)
        {
            int[,] matrix1 = new int[3, 3];
            matrix1[0, 0] = int.Parse(m1Text1.Text);
            matrix1[0, 1] = int.Parse(m1Text2.Text);
            matrix1[0, 2] = int.Parse(m1Text3.Text);
            matrix1[1, 0] = int.Parse(m1Text4.Text);
            matrix1[1, 1] = int.Parse(m1Text5.Text);
            matrix1[1, 2] = int.Parse(m1Text6.Text);
            matrix1[2, 0] = int.Parse(m1Text7.Text);
            matrix1[2, 1] = int.Parse(m1Text8.Text);
            matrix1[2, 2] = int.Parse(m1Text9.Text);

            int[,] matrix2 = new int[3, 3];
            matrix2[0, 0] = int.Parse(m2Text1.Text);
            matrix2[0, 1] = int.Parse(m2Text2.Text);
            matrix2[0, 2] = int.Parse(m2Text3.Text);
            matrix2[1, 0] = int.Parse(m2Text4.Text);
            matrix2[1, 1] = int.Parse(m2Text5.Text);
            matrix2[1, 2] = int.Parse(m2Text6.Text);
            matrix2[2, 0] = int.Parse(m2Text7.Text);
            matrix2[2, 1] = int.Parse(m2Text8.Text);
            matrix2[2, 2] = int.Parse(m2Text9.Text);

            int[,] matrixr = new int[3, 3];
            for (int i=0; i<3; i++) {
                for (int j=0; j<3; j++) {
                    matrixr[i, j] += matrix1[i, 0] * matrix2[0, j];
                    matrixr[i, j] += matrix1[i, 1] * matrix2[1, j];
                    matrixr[i, j] += matrix1[i, 2] * matrix2[2, j];
                }
            }

            mrText1.Text = matrixr[0, 0].ToString();
            mrText2.Text = matrixr[0, 1].ToString();
            mrText3.Text = matrixr[0, 2].ToString();
            mrText4.Text = matrixr[1, 0].ToString();
            mrText5.Text = matrixr[1, 1].ToString();
            mrText6.Text = matrixr[1, 2].ToString();
            mrText7.Text = matrixr[2, 0].ToString();
            mrText8.Text = matrixr[2, 1].ToString();
            mrText9.Text = matrixr[2, 2].ToString();
        }


    }
}
