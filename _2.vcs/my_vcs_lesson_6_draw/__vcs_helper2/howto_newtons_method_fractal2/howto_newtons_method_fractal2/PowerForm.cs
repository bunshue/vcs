using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace howto_newtons_method_fractal2
{
    public partial class PowerForm : Form
    {
        public PowerForm()
        {
            InitializeComponent();
        }

        // Get and set the Power value.
        public double Power
        {
            get
            {
                return double.Parse(txtPower.Text);
            }
            set
            {
                txtPower.Text = value.ToString();
            }
        }

        // Close the form if the value is a double.
        private void btnOk_Click(object sender, EventArgs e)
        {
            double value;
            if (double.TryParse(txtPower.Text, out value))
            {
                this.DialogResult = DialogResult.OK;
            }
            else
            {
                MessageBox.Show("Please enter a number.");
                txtPower.SelectAll();
                txtPower.Focus();
            }
        }
    }
}
