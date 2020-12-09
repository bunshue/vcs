using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Password2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Display the password form.
        private void Form1_Load(object sender, EventArgs e)
        {
            // Display the password form.
            PasswordForm frm = new PasswordForm();
            if (frm.ShowDialog() != DialogResult.OK)
            {
                // The user canceled.
                this.Close();
            }
            frm.Close();

            // Otherwise go on to show this form.
        }
    }
}
