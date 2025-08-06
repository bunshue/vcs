using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace howto_password_tracker
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private string MasterPassword = "";
        private string MasterDate = "";

        private void Form1_Load(object sender, EventArgs e)
        {
            this.KeyPreview = true;

            // Restore form positions and data.
            LoadSettings();

            richTextBox1.Text += "OK\n";
            this.Size = new Size(1200, 600);
        }

        private void LoadSettings()
        {
            // Get the master password.
            if (InputBox("Master Password", "", out MasterPassword) == DialogResult.Cancel)
            {
                Close();
                return;
            }

            // See if we have any data yet.
            string crypt_master = SettingStuff.GetSetting(SettingStuff.APP_NAME, "Passwords", "Master", "");
            if (crypt_master.Length == 0)
            {
                // This is the first time. Record the master password change date.
                MasterDate = DateTime.Now.ToString();
            }
            else
            {
                // Verify that the user entered the correct master password.
                string salt_master = SettingStuff.GetSetting(SettingStuff.APP_NAME, "Passwords", "MasterSalt", "");
                richTextBox1.Text += "crypt_master : " + crypt_master + "\n";
                richTextBox1.Text += "MasterPassword : " + MasterPassword + "\n";
                richTextBox1.Text += "salt_master : " + salt_master + "\n";
                string plain_master = Crypto.DecryptFromString(crypt_master, MasterPassword, salt_master);
                richTextBox1.Text += "plain_master : " + plain_master + "\n";
                richTextBox1.Text += "MasterPassword : " + MasterPassword + "\n";

                if (plain_master != MasterPassword)
                {
                    MessageBox.Show("Incorrect master password", "Incorrect Password", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
                    MasterPassword = "";
                    Close();
                    return;
                }

                string crypt_masterdate = SettingStuff.GetSetting(SettingStuff.APP_NAME, "Passwords", "MasterDate", DateTime.Now.ToString());
                MasterDate = Crypto.DecryptFromString(crypt_masterdate, MasterPassword, salt_master);
            }

            // Load the password data.
            for (int i = 0; ; i++)
            {
                // Get the next password's name, username, and value.
                string crypt_name = SettingStuff.GetSetting(SettingStuff.APP_NAME, "Passwords", "PasswordName" + i.ToString(), "");
                if (crypt_name.Length == 0)
                    break;
                string crypt_uaername = SettingStuff.GetSetting(SettingStuff.APP_NAME, "Passwords", "PasswordUsername" + i.ToString(), "");
                string crypt_value = SettingStuff.GetSetting(SettingStuff.APP_NAME, "Passwords", "PasswordValue" + i.ToString(), "");
                string salt = SettingStuff.GetSetting(SettingStuff.APP_NAME, "Passwords", "PasswordSalt" + i.ToString(), "");
                string crypt_date = SettingStuff.GetSetting(SettingStuff.APP_NAME, "Passwords", "PasswordDate" + i.ToString(), "");

                // Decrypt the name, username, password, and date.
                string plain_name = Crypto.DecryptFromString(crypt_name, MasterPassword, salt);
                string plain_username = Crypto.DecryptFromString(crypt_uaername, MasterPassword, salt);
                string plain_value = Crypto.DecryptFromString(crypt_value, MasterPassword, salt);
                string plain_date = Crypto.DecryptFromString(crypt_date, MasterPassword, salt);

                // Display the result.
                dgvPasswords.Rows.Add(new Object[] { plain_name, plain_username, plain_value, plain_date, null, null });
            }

            // Restore the form and grid settings.
            SettingStuff.RestoreFormPosition(this, SettingStuff.APP_NAME, "MainForm");
            SettingStuff.RestoreDgvSettings(this.dgvPasswords, SettingStuff.APP_NAME, "MainDgv");
        }

        // Prompt the user for a simple text value.
        private DialogResult InputBox(string prompt, string default_value, out string result)
        {
            frmInputBox dlg = new frmInputBox();
            dlg.Text = prompt;
            dlg.lblPrompt.Text = prompt;
            dlg.txtValue.Text = default_value;

            DialogResult dialog_result = dlg.ShowDialog();

            result = dlg.txtValue.Text;
            return dialog_result;
        }

        // Save form positions and data.
        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            dgvPasswords.EndEdit();
            SaveSettings();
        }

        private void SaveSettings()
        {
            // If we didn't get a valid master password, don't save anything.
            if (MasterPassword.Length == 0) return;

            // Save the form positions.
            SettingStuff.SaveFormPosition(this, SettingStuff.APP_NAME, "MainForm");
            SettingStuff.SaveDgvSettings(this.dgvPasswords, SettingStuff.APP_NAME, "MainDgv");

            // Save the encrypted passwords.
            SettingStuff.SaveSetting(SettingStuff.APP_NAME, "Passwords", "Test", "Value"); // Just so there's something to delete.
            SettingStuff.DeleteSettingSection(SettingStuff.APP_NAME, "Passwords");

            string salt_master = Crypto.RandomSalt();
            string crypt_master = Crypto.EncryptToString(MasterPassword, MasterPassword, salt_master);
            string crypt_masterdate = Crypto.EncryptToString(MasterDate, MasterPassword, salt_master);
            SettingStuff.SaveSetting(SettingStuff.APP_NAME, "Passwords", "Master", crypt_master);
            SettingStuff.SaveSetting(SettingStuff.APP_NAME, "Passwords", "MasterSalt", salt_master);
            SettingStuff.SaveSetting(SettingStuff.APP_NAME, "Passwords", "MasterDate", crypt_masterdate);

            // Save the password data.
            int i = 0;
            foreach (DataGridViewRow row in dgvPasswords.Rows)
            {
                // Get the next password's name, value, and date.
                string plain_name = (string)row.Cells["colName"].Value;
                string plain_username = (string)row.Cells["colUsername"].Value;
                string plain_value = (string)row.Cells["colPassword"].Value;
                string plain_date = (string)row.Cells["colChangedDate"].Value;
                if (plain_name == null)
                    plain_name = "";
                if (plain_username == null)
                    plain_name = "";
                if (plain_value == null)
                    plain_value = "";
                if (plain_date == null)
                    plain_date = "";
                if ((plain_name.Length == 0) || (plain_username.Length == 0) || (plain_value.Length == 0) || (plain_date.Length == 0))
                {
                    row.Cells["colName"].Value = "";
                    row.Cells["colUsername"].Value = "";
                    row.Cells["colPassword"].Value = "";
                    row.Cells["colChangedDate"].Value = "";
                }
                else
                {
                    // Encrypt.
                    string salt = Crypto.RandomSalt();
                    string crypt_name = Crypto.EncryptToString(plain_name, MasterPassword, salt);
                    string crypt_username = Crypto.EncryptToString(plain_username, MasterPassword, salt);
                    string crypt_value = Crypto.EncryptToString(plain_value, MasterPassword, salt);
                    string crypt_date = Crypto.EncryptToString(plain_date, MasterPassword, salt);

                    // Save the values.
                    SettingStuff.SaveSetting(SettingStuff.APP_NAME, "Passwords", "PasswordName" + i.ToString(), crypt_name);
                    SettingStuff.SaveSetting(SettingStuff.APP_NAME, "Passwords", "PasswordUsername" + i.ToString(), crypt_username);
                    SettingStuff.SaveSetting(SettingStuff.APP_NAME, "Passwords", "PasswordValue" + i.ToString(), crypt_value);
                    SettingStuff.SaveSetting(SettingStuff.APP_NAME, "Passwords", "PasswordDate" + i.ToString(), crypt_date);
                    SettingStuff.SaveSetting(SettingStuff.APP_NAME, "Passwords", "PasswordSalt" + i.ToString(), salt);
                    i++;
                }
            }
        }

        // Let the user change settings.
        private void mnuFileChangeMasterPassword_Click(object sender, EventArgs e)
        {
            frmChangeMaster frm = new frmChangeMaster();
            frm.txtDataFile.Text = MasterPassword;
            frm.lblLastChanged.Text = "Master Password last changed " + MasterDate;

            if (frm.ShowDialog() == DialogResult.OK)
            {
                // Save the new master password.
                MasterPassword = frm.txtDataFile.Text;
                MasterDate = DateTime.Now.ToString();

                // Re-encrypt the passwords.
                SaveSettings();

                MessageBox.Show("Master password changed. Values saved.", "Changed", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }

        private void mnuFileExit_Click(object sender, EventArgs e)
        {
            Close();
        }

        // Copy a password to the clipboard or make a new password.
        private void dgvPasswords_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
            if (dgvPasswords.Columns[e.ColumnIndex].Name == "colCopy")
            {
                // Copy to clipboard.
                Clipboard.Clear();
                Clipboard.SetText(dgvPasswords.Rows[e.RowIndex].Cells["colPassword"].Value.ToString());
                System.Media.SystemSounds.Beep.Play();
            }
            if (dgvPasswords.Columns[e.ColumnIndex].Name == "colNew")
            {
                // Make a new password.
                frmNewPassword frm = new frmNewPassword();
                if (dgvPasswords.Rows[e.RowIndex].Cells["colPassword"].Value != null)
                {
                    frm.txtPassword.Text = dgvPasswords.Rows[e.RowIndex].Cells["colPassword"].Value.ToString();
                }
                if (frm.ShowDialog() == DialogResult.OK)
                {
                    dgvPasswords.Rows[e.RowIndex].Cells["colPassword"].Value = frm.txtPassword.Text;
                    dgvPasswords.Rows[e.RowIndex].Cells["colChangedDate"].Value = DateTime.Now.ToString();
                }
            }
        }

        // If this is a password, set the new changed date.
        private void dgvPasswords_CellEndEdit(object sender, DataGridViewCellEventArgs e)
        {
            if (dgvPasswords.Columns[e.ColumnIndex].Name == "colPassword")
            {
                dgvPasswords.Rows[e.RowIndex].Cells["colChangedDate"].Value = DateTime.Now.ToString();
            }
        }

        // Look for Ctrl+V and Ctrl+C.
        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.Control)
            {
                if (e.KeyCode == Keys.C)
                {
                    // Copy the current cell to the clipboard.
                    string text = dgvPasswords.CurrentCell.Value.ToString();
                    if (text.Length > 0)
                    {
                        Clipboard.Clear();
                        Clipboard.SetText(text);
                        System.Media.SystemSounds.Beep.Play();
                    }
                }
                else if (e.KeyCode == Keys.V)
                {
                    // Paste into the current cell.
                    if (!Clipboard.ContainsText())
                    {
                        System.Media.SystemSounds.Beep.Play();
                    }
                    else
                    {
                        dgvPasswords.CurrentCell.Value = Clipboard.GetText();
                    }
                }
            }
        }
    }
}
