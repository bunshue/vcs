using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Text.RegularExpressions;   //for Regex

namespace vcs_test_all_21_ToolTip_ErrorProvider
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Add tooltips to the buttons.
        private void button1_Click(object sender, EventArgs e)
        {
            toolTip1.SetToolTip(button1, "Click to add tooltips to the buttons.");
            toolTip1.SetToolTip(button2, "Click to remove tooltips from the buttons.");
        }

        // Remove tooltips from the buttons.
        private void button2_Click(object sender, EventArgs e)
        {
            toolTip1.SetToolTip(button1, "");
            toolTip1.SetToolTip(button2, "");
        }

        // Validate a required field. Return true if the field is valid.
        private bool ValidateRequiredField(ErrorProvider err, TextBox txt)
        {
            if (txt.Text.Length > 0)
            {
                // Clear the error.
                err.SetError(txt, "");
                return false;
            }
            else
            {
                // Set the error.
                err.SetError(txt, CamelCaseToWords(txt.Name) + " 本欄不可空白");
                return true;
            }
        }

        // Split a string in camelCase, removing the prefix.
        private string CamelCaseToWords(string input)
        {
            // Insert a space in front of each capital letter.
            string result = "";
            foreach (char ch in input.ToCharArray())
            {
                if (char.IsUpper(ch)) result += " ";
                result += ch;
            }

            // Find the first space and remove everything before it.
            return result.Substring(result.IndexOf(" ") + 1);
        }


        // Validate fields.
        private void text_data_Validating(object sender, CancelEventArgs e)
        {
            TextBox txt = sender as TextBox;
            ValidateRequiredField(errorProvider1, txt);
        }

        // Validate the telephone
        private void ValidateTelephoneNumber(ErrorProvider err, TextBox txt)
        {
            // Check for missing value.
            if (ValidateRequiredField(err, txt)) return;

            // Check for correct format.
            Regex regex = new Regex(@"^(\d{10}|\d{4}-\d{6})$");
            if (regex.IsMatch(txt.Text))
            {
                // Clear the error.
                errorProvider1.SetError(txt, "");
            }
            else
            {
                // Set the error.
                errorProvider1.SetError(txt, "電話號碼格式 ########## 或 ####-######.");
            }
        }

        // Validate the telephone number.
        private void number_data_Validating(object sender, CancelEventArgs e)
        {
            TextBox txt = sender as TextBox;
            ValidateTelephoneNumber(errorProvider1, txt);
        }

        // The user accepted the values.
        private void button3_Click(object sender, EventArgs e)
        {
            // Validate all fields.
            ValidateRequiredField(errorProvider1, textBox1);
            ValidateRequiredField(errorProvider1, textBox2);
            ValidateRequiredField(errorProvider1, textBox4);
            ValidateTelephoneNumber(errorProvider1, textBox3);

            // See if any field has an error message.
            foreach (Control ctl in Controls)
            {
                if (errorProvider1.GetError(ctl) != "")
                {
                    MessageBox.Show(errorProvider1.GetError(ctl));
                    return;
                }
            }

            richTextBox1.Text += "你輸入的資料\n" + "姓名:\t" + textBox1.Text +
                "\n住址:\t" + textBox2.Text + "\n電話:\t" + textBox3.Text + "\n意見:\t" + textBox4.Text + "\n";
        }

        //Close
        private void button4_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
