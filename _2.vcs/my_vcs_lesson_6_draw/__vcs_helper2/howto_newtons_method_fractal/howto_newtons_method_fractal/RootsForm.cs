using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace howto_newtons_method_fractal
{
    public partial class RootsForm : Form
    {
        public RootsForm()
        {
            InitializeComponent();
        }

        // Get and set the Power value.
        public int Roots
        {
            get
            {
                return int.Parse(txtNumRoots.Text);
            }
            set
            {
                txtNumRoots.Text = value.ToString();
            }
        }

        // Close the form if the value is a double.
        private void btnOk_Click(object sender, EventArgs e)
        {
            int roots;
            if (int.TryParse(txtNumRoots.Text, out roots))
            {
                this.DialogResult = DialogResult.OK;
            }
            else
            {
                MessageBox.Show("Please enter an integer");
                txtNumRoots.SelectAll();
                txtNumRoots.Focus();
            }
        }
    }
}
