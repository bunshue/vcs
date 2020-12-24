using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Text.RegularExpressions;

namespace vcs_RegularExpression
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            txtString_TextChanged(sender, e);
            txtTestString_TextChanged(sender, e);
        }

        private void txtString_TextChanged(object sender, EventArgs e)
        {
            // Display only letters.
            txtLetters.Text = Regex.Replace(txtString.Text, "[^a-zA-Z]", "");

            // Display only digits.
            txtDigits.Text = Regex.Replace(txtString.Text, "[^0-9]", "");
        }

        // Make the replacements.
        private void txtTestString_TextChanged(object sender, EventArgs e)
        {
            Regex reg_exp = new Regex(txtPattern.Text);
            lblResult.Text = reg_exp.Replace(txtTestString.Text, txtReplacementPattern.Text);
        }

        private void do_regular_expression(object sender, EventArgs e)
        {
            try
            {
                Regex reg_exp = new Regex(txtPattern2.Text);
                lblResult2.Text = reg_exp.Replace(txtInput.Text, txtReplacementPattern2.Text);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

    }
}
