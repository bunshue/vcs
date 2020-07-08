using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1ttttttttttttt
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }


        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void textBox1_Validating(object sender, CancelEventArgs e)
        {
            richTextBox1.Text += "textBox1_Validating\n";
            string errorMsg;
            if (!ValidEmailAddress(textBox1.Text, out errorMsg))
            {
                // Cancel the event and select the text to be corrected by the user.
                e.Cancel = true;
                textBox1.Select(0, textBox1.Text.Length);

                // Set the ErrorProvider error with the text to display. 
                this.errorProvider1.SetError(textBox1, errorMsg);
            }

        }

        private void textBox1_Validated(object sender, EventArgs e)
        {
            richTextBox1.Text += "textBox1_Validated\n";
            // If all conditions have been met, clear the ErrorProvider of errors.
            errorProvider1.SetError(textBox1, "");

        }


        public bool ValidEmailAddress(string emailAddress, out string errorMessage)
        {
            // Confirm that the email address string is not empty.
            if (emailAddress.Length == 0)
            {
                errorMessage = "email address is required.";
                richTextBox1.Text += "XXXX";
                return false;
            }

            // Confirm that there is an "@" and a "." in the email address, and in the correct order.
            if (emailAddress.IndexOf("@") > -1)
            {
                if (emailAddress.IndexOf(".", emailAddress.IndexOf("@")) > emailAddress.IndexOf("@"))
                {
                    errorMessage = "";
                    richTextBox1.Text += "合法";
                    return true;
                }
            }

            //richTextBox1.Text += "email address must be valid email address format.\n" + "For example 'someone@example.com' \n";
            errorMessage = "email address must be valid email address format.\n" + "For example 'someone@example.com' ";
            return false;
        }

    }
}
