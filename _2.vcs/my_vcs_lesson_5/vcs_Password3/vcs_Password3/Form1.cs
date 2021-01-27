using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

// Set PasswordForm.btnOk.Modifiers = Public.

namespace vcs_Password3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Get the password from the user.
        private void Form1_Load(object sender, EventArgs e)
        {
            const string real_password = "lion-mouse";

            // Get the password from the user.
            PasswordForm frm = new PasswordForm();
            if (frm.ShowDialog() == DialogResult.Cancel)
                Close();

            // See if the password is correct.
            string password = frm.txtPassword.Text;
            if (password != real_password)
                Close();
        }
    }
}
