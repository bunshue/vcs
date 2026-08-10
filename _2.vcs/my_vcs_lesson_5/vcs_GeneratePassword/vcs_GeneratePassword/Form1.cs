using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_GeneratePassword
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

            richTextBox1.Size = new Size(300, 690);
            richTextBox1.Location = new Point(x_st + dx * 4 + 100, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1273, 750);
            this.Text = "vcs_test_all_00_Usually";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        // Required implies allowed.
        private void chkRequireLowercase_CheckedChanged(object sender, EventArgs e)
        {
            if (chkRequireLowercase.Checked)
            {
                chkAllowLowercase.Checked = true;
            }
        }
        private void chkRequireUppercase_CheckedChanged(object sender, EventArgs e)
        {
            if (chkRequireUppercase.Checked)
            {
                chkAllowUppercase.Checked = true;
            }
        }
        private void chkRequireNumber_CheckedChanged(object sender, EventArgs e)
        {
            if (chkRequireNumber.Checked)
            {
                chkAllowNumber.Checked = true;
            }
        }
        private void chkRequireSpecial_CheckedChanged(object sender, EventArgs e)
        {
            if (chkRequireSpecial.Checked)
            {
                chkAllowSpecial.Checked = true;
            }
        }
        private void chkRequireUnderscore_CheckedChanged(object sender, EventArgs e)
        {
            if (chkRequireUnderscore.Checked)
            {
                chkAllowUnderscore.Checked = true;
            }
        }
        private void chkRequireSpace_CheckedChanged(object sender, EventArgs e)
        {
            if (chkRequireSpace.Checked)
            {
                chkAllowSpace.Checked = true;
            }
        }
        private void chkRequireOther_CheckedChanged(object sender, EventArgs e)
        {
            if (chkRequireOther.Checked)
            {
                chkAllowOther.Checked = true;
            }
        }

        // Not allowed implies not required.
        private void chkAllowLowercase_CheckedChanged(object sender, EventArgs e)
        {
            if (!chkAllowLowercase.Checked)
            {
                chkRequireLowercase.Checked = false;
            }
        }
        private void chkAllowUppercase_CheckedChanged(object sender, EventArgs e)
        {
            if (!chkAllowUppercase.Checked)
            {
                chkRequireUppercase.Checked = false;
            }
        }
        private void chkAllowNumber_CheckedChanged(object sender, EventArgs e)
        {
            if (!chkAllowNumber.Checked)
            {
                chkRequireNumber.Checked = false;
            }
        }
        private void chkAllowSpecial_CheckedChanged(object sender, EventArgs e)
        {
            if (!chkAllowSpecial.Checked)
            {
                chkRequireSpecial.Checked = false;
            }
        }
        private void chkAllowUnderscore_CheckedChanged(object sender, EventArgs e)
        {
            if (!chkAllowUnderscore.Checked)
            {
                chkRequireUnderscore.Checked = false;
            }
        }
        private void chkAllowSpace_CheckedChanged(object sender, EventArgs e)
        {
            if (!chkAllowSpace.Checked)
            {
                chkRequireSpace.Checked = false;
            }
        }
        private void chkAllowOther_CheckedChanged(object sender, EventArgs e)
        {
            if (!chkAllowOther.Checked)
            {
                chkRequireOther.Checked = false;
            }
        }

        // Generate a new password.
        private void btnGenerate_Click(object sender, EventArgs e)
        {
            try
            {
                txtPassword.Text = RandomPassword();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        // Generate a password that meets the reuirements.
        private string RandomPassword()
        {
            const string LOWER = "abcdefghijklmnopqrstuvwxyz";
            const string UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            const string NUMBER = "0123456789";
            const string SPECIAL = @"~!@#$%^&*():;[]{}<>,.?/\|";
            string other = txtOther.Text;
            if (chkRequireOther.Checked && (other.Length < 1))
            {
                MessageBox.Show("You cannot require characters from a blank string.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error); txtOther.Focus();
                return txtPassword.Text;
            }

            // Make a list of allowed characters.
            string allowed = "";
            if (chkAllowLowercase.Checked)
            {
                allowed += LOWER;
            }
            if (chkAllowUppercase.Checked)
            {
                allowed += UPPER;
            }
            if (chkAllowNumber.Checked)
            {
                allowed += NUMBER;
            }
            if (chkAllowSpecial.Checked)
            {
                allowed += SPECIAL;
            }
            if (chkAllowUnderscore.Checked)
            {
                allowed += "_";
            }
            if (chkAllowSpace.Checked)
            {
                allowed += " ";
            }
            if (chkAllowOther.Checked)
            {
                allowed += other;
            }

            // Pick the number of characters.
            int min_chars = int.Parse(txtMinLength.Text);
            int max_chars = int.Parse(txtMaxLength.Text);
            int num_chars = Crypto.RandomInteger(min_chars, max_chars);

            // Satisfy requirements.
            string password = "";
            if (chkRequireLowercase.Checked && (password.IndexOfAny(LOWER.ToCharArray()) == -1))
            {
                password += RandomChar(LOWER);
            }
            if (chkRequireUppercase.Checked && (password.IndexOfAny(UPPER.ToCharArray()) == -1))
            {
                password += RandomChar(UPPER);
            }
            if (chkRequireNumber.Checked && (password.IndexOfAny(NUMBER.ToCharArray()) == -1))
            {
                password += RandomChar(NUMBER);
            }
            if (chkRequireSpecial.Checked && (password.IndexOfAny(SPECIAL.ToCharArray()) == -1))
            {
                password += RandomChar(SPECIAL);
            }
            if (chkRequireUnderscore.Checked && (password.IndexOfAny("_".ToCharArray()) == -1))
            {
                password += "_";
            }
            if (chkRequireSpace.Checked && (password.IndexOfAny(" ".ToCharArray()) == -1))
            {
                password += " ";
            }
            if (chkRequireOther.Checked && (password.IndexOfAny(other.ToCharArray()) == -1))
            {
                password += RandomChar(other);
            }

            // Add the remaining characters randomly.
            while (password.Length < num_chars)
            {
                password += RandomChar(allowed);
            }

            // Randomize (to mix up the required characters at the front).
            password = RandomizeString(password);

            return password;
        }

        // Return a random character from a string.
        private string RandomChar(string str)
        {
            return str.Substring(Crypto.RandomInteger(0, str.Length - 1), 1);
        }

        // Return a random permutation of a string.
        private string RandomizeString(string str)
        {
            string result = "";
            while (str.Length > 0)
            {
                // Pick a random character.
                int i = Crypto.RandomInteger(0, str.Length - 1);
                result += str.Substring(i, 1);
                str = str.Remove(i, 1);
            }
            return result;
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

