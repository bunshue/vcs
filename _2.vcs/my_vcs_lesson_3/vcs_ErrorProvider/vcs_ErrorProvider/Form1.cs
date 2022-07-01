using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Text.RegularExpressions;

namespace vcs_ErrorProvider
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            tb_id.Validating += new CancelEventHandler(tb_id_Validating);
            tb_name.Validating += new CancelEventHandler(tb_name_Validating);
        }

        string strA = null;
        string strB = null;

        private void textBox1_Validating(object sender, CancelEventArgs e)
        {
            //驗證帳號

            if (textBox1.Text != "ims")
            {
                errorProvider1.SetError(textBox1, "登錄名錯誤");
            }
            else
            {
                errorProvider1.SetError(textBox1, "");
                strA = textBox1.Text;
            }
        }

        private void textBox2_Validating(object sender, CancelEventArgs e)
        {
            //驗證密碼
            if (textBox2.Text != "iloveims")//判斷輸入是否正確
            {
                errorProvider2.SetError(textBox2, "密碼確誤");
            }
            else
            {
                errorProvider2.SetError(textBox2, "");
                strB = textBox2.Text;
            }

        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (strA != null && strB != null)
            {
                MessageBox.Show("登錄成功");
            }
            else
            {
                MessageBox.Show("輸入用戶名和密碼");
            }
        }

        // Validate the ID code.
        private void tb_id_Validating(object sender, CancelEventArgs e)
        {
            // Check for missing value.
            if (RequiredFieldIsBlank(errorProvider3, tb_id))
            {
                e.Cancel = true;
                return;
            }

            // Check for correct format.

            //Regex regex = new Regex(@"^(\d{5}|\d{5}-\d{4})$");    //5數 或 5數-4數
            Regex regex = new Regex(@"^[A-Z]{1}[0-9]{9}$");         //1英9數

            if (regex.IsMatch(tb_id.Text))
            {
                // Clear the error.
                errorProvider3.SetError(tb_id, "OK");
            }
            else
            {
                // Set the error.
                errorProvider3.SetError(tb_id, "台灣身份證字號格式 1英9數");
                e.Cancel = true;
            }
        }

        // Validate a required field. Return true if the field is valid.
        private bool RequiredFieldIsBlank(ErrorProvider err, TextBox txt)
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
                err.SetError(txt, CamelCaseToWords(txt.Name) + " must not be blank.");
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
                if (char.IsUpper(ch))
                {
                    result += " ";
                }
                result += ch;
            }

            // Find the first space and remove everything before it.
            return result.Substring(result.IndexOf(" ") + 1);
        }


        // Validate fields.
        private void tb_name_Validating(object sender, CancelEventArgs e)
        {
            TextBox txt = sender as TextBox;
            e.Cancel = RequiredFieldIsBlank(errorProvider3, txt);
        }

        // Validate a required field. Return true if the field is valid.

        //RequiredFieldIsBlank   same
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
                err.SetError(txt, CamelCaseToWords(txt.Name) + " must not be blank.");
                return true;
            }
        }

        // Validate the ID code
        private void ValidateIDCode(ErrorProvider err, TextBox txt)
        {
            // Check for missing value.
            if (ValidateRequiredField(err, txt)) return;

            // Check for correct format.

            //Regex regex = new Regex(@"^(\d{5}|\d{5}-\d{4})$");    //5數 或 5數-4數
            Regex regex = new Regex(@"^[A-Z]{1}[0-9]{9}$");         //1英9數
            if (regex.IsMatch(txt.Text))
            {
                // Clear the error.
                errorProvider3.SetError(txt, "");
            }
            else
            {
                // Set the error.
                errorProvider3.SetError(txt, "ZIP code must have format ##### or #####-####.");
            }
        }

        private void bt_ok_Click(object sender, EventArgs e)
        {
            //richTextBox1.Text += "你按了OK\n";
            // Validate all fields.
            ValidateIDCode(errorProvider3, tb_id);
            ValidateRequiredField(errorProvider3, tb_name);

            // See if any field has an error message.
            foreach (Control ctl in Controls)
            {
                if (errorProvider3.GetError(ctl) != "")
                {
                    MessageBox.Show(errorProvider3.GetError(ctl));
                    return;
                }
            }
            richTextBox1.Text += "資料正確\nID:\t" + tb_id.Text + "\nName:\t" + tb_name.Text + "\n";

        }
        


    }
}
