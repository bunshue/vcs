using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace howto_required_fields
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // When we start, highlight required fields.
        private void Form1_Load(object sender, EventArgs e)
        {
            // reqChecker.CheckAllFields();
        }

        // True if we should check required fields.
        // Normally this is false so we don't check fields if
        // the user closes the form by pressinng Alt-F4, etc.
        private bool CheckRequiredFields = false;

        // Check that required fields are non-blank.
        private void btnOk_Click(object sender, EventArgs e)
        {
            CheckRequiredFields = true;
            this.Close();
        }

        // Just close.
        private void btnCancel_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        // If we should check required fields, do so.
        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            if (CheckRequiredFields)
            {
                TextBox missing_field = reqChecker.FirstMissingField();
                if (missing_field != null)
                {
                    MessageBox.Show("Please enter all required fields.",
                        "Required Value Missing",
                        MessageBoxButtons.OK,
                        MessageBoxIcon.Exclamation);
                    missing_field.Focus();
                    e.Cancel = true;
                }

                // Next time we try to close, don't check
                // (unless the user clicks OK again).
                CheckRequiredFields = false;
            }
        }
    }
}
