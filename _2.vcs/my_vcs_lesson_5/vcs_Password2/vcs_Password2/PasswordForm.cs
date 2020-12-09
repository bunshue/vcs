using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

// Set the TextBox's PasswordChar property
// to X or something at design time.

namespace vcs_Password2
{
    public partial class PasswordForm : Form
    {
        public PasswordForm()
        {
            InitializeComponent();
        }

        // Validate the password.
        private void btnOk_Click(object sender, EventArgs e)
        {
            if (txtPassword.Text == "Secret")
            {
                // The password is ok.
                this.DialogResult = DialogResult.OK;
            }
            else
            {
                // The password is invalid.
                txtPassword.Clear();
                MessageBox.Show("Inivalid password.");
                txtPassword.Focus();
            }
        }
    }
}
