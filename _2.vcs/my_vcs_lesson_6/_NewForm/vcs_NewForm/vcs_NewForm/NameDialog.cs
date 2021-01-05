using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

// Note: At design time, I set Modifiers = Public for the
// two textboxes so the main program can read their values.
namespace vcs_NewForm
{
    public partial class NameDialog : Form
    {
        public NameDialog()
        {
            InitializeComponent();
        }

        // Validate the user's entries.
        private void btnOk_Click(object sender, EventArgs e)
        {
            if (txtFirstName.Text.Length < 1)
            {
                MessageBox.Show("You must enter a First Name.",
                    "Invalid Name", MessageBoxButtons.OK,
                    MessageBoxIcon.Error);
                txtFirstName.Focus();
            }
            else if (txtLastName.Text.Length < 1)
            {
                MessageBox.Show("You must enter a Last Name.",
                    "Invalid Name", MessageBoxButtons.OK,
                    MessageBoxIcon.Error);
                txtLastName.Focus();
            }
            else
            {
                // It's ok. Close the dialog.
                DialogResult = DialogResult.OK;
            }
        }

        // Replace Show so the program cannot use it.
        private new void Show()
        {
            throw new InvalidOperationException(
                "Use ShowDialog not Show to display this dialog");
        }

        private void btnCancel_Click(object sender, EventArgs e)
        {

        }
    }
}
