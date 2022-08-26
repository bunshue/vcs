using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace howto_gamma_function_table
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnCalculate_Click(object sender, EventArgs e)
        {
            lvwValues.Items.Clear();
            Cursor = Cursors.WaitCursor;

            int minx = int.Parse(txtMinX.Text);
            int maxx = int.Parse(txtMaxX.Text);
            double dt = double.Parse(txtDt.Text);
            int num_slices = int.Parse(txtNumSlices.Text);
            for (int x = minx; x <= maxx; x++)
            {
                double x_factorial = Factorial(x);
                if (double.IsInfinity(x_factorial)) break;
                double gamma_x = Gamma(x + 1, dt, num_slices);
                double difference = Math.Abs(gamma_x - x_factorial);
                double percent_difference = difference / gamma_x * 100.0;
                lvwValues.AddRow(
                    x.ToString("G4"),
                    x_factorial.ToString("G4"),
                    gamma_x.ToString("G4"),
                    difference.ToString("G4"),
                    percent_difference.ToString("G4"));
            }
            lvwValues.AutoSizeColumns();
            Cursor = Cursors.Default;
        }

        // Return x!.
        private double Factorial(int x)
        {
            double result = 1;
            for (int i = 2; i <= x; i++)
                result *= i;
            return result;
        }

        // Integrate: x^(z-1)*e^(-x) dx from 0 to infinity.
        private double Gamma(double z, double dx, int num_slices)
        {
            double result = 0;
            double x = 0;
            for (int i = 0; i < num_slices; i++)
            {
                double new_term = Math.Pow(x, z - 1) * Math.Exp(-x);
                if (double.IsNaN(new_term)) break;
                if (double.IsInfinity(new_term)) break;
                result += new_term;
                x += dx;
            }
            return result * dx;
        }
    }
}
